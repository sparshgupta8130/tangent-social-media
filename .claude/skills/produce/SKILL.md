---
name: produce
description: Use when a pipeline item is at stage PRODUCING (has passed G1) — executes the asset manifest, drives capture and generative queuing, assembles the cut, and runs hygiene checks toward CUT.
---

## Purpose
Turn a G1-approved script into an actual cut: execute every `[AGENT]` and `[GEN]` asset,
collapse every `[SPARSH]` need into one tracked request, and hand off a hygiene-clean file.

## Preconditions
- Item stage == `PRODUCING` (G1 SHIP already recorded).
- `NNN-slug/assets.md` present with provider tags from `/script`.

## Protocol
1. Confirm stage via `python tools/pipeline.py board`; read `NNN-slug/script.md` and
   `assets.md`.
2. Invoke `producer` (Task, subagent_type `producer`) with: `assets.md`, `script.md`,
   `knowledge/production/adobe-playbook.md`, `knowledge/production/assembly-playbook.md`,
   `knowledge/production/genvideo-playbook.md`.
3. `[AGENT]` assets: producer runs Lightroom-via-Claude-in-Chrome capture sessions per
   `adobe-playbook.md`'s session protocol (capture-worthy moments as defined there), then
   assembles per `assembly-playbook.md`'s exact capture → cut → captions → export settings.
4. `[GEN]` assets: producer queues generation (Veo/Flow b-roll, TTS narration) per
   `genvideo-playbook.md` prompt patterns, honoring the disclosure rules in
   `knowledge/audience/positioning.md` for every generated asset — log the disclosure
   treatment used next to the asset row.
5. `[SPARSH]` assets: do not ping Sparsh per line item. Consolidate every outstanding
   `[SPARSH]` need from `assets.md` into ONE request via a same-stage touch (no stage change,
   just field updates):
   `python tools/pipeline.py stage NNN PRODUCING --next-action "<all SPARSH needs in one line>" --next-action-owner sparsh --due YYYY-MM-DD`
   This is what makes the item show up as `BLOCKED-ON-SPARSH` on `pipeline.py blocked`. Flag
   `planner`, which also adds the `sparsh-input` Plane label the first time
   `next_action_owner` becomes `sparsh` (`ops/RUNBOOK.md` §6) — one consolidated ask, never a
   drip.
6. Update `assets.md`'s status column for every row as work completes (queued →
   in-progress → done, with the actual path/source recorded — never leave a row silently
   stale).
7. Once assembly produces a candidate cut, run:
   `python tools/hygiene_check.py <path-to-cut>` and log the PASS/FAIL per check.
8. If PASS: `python tools/pipeline.py stage NNN CUT --next-action "Run G2 critique" --next-action-owner critic`.
   If FAIL: fix (re-export/re-crop/re-encode per the failing check) and rerun `hygiene_check`
   — loop until PASS or until genuinely blocked on a `[SPARSH]` asset needed to fix it (fold
   that into the same consolidated request from step 5).

## Gates
- `hygiene_check.py` overall PASS is required before the CUT transition — this doesn't
  replace G2's own independent hygiene re-check in `/critique`, it just means `/produce` never
  hands off a cut it already knows is failing.
- Every `assets.md` row must be `status: done` or explicitly `blocked-on-sparsh` with a due
  date before advancing — no row left blank or silently unresolved.

## Outputs
- `NNN-slug/assets.md` fully updated (status + final path/source per asset).
- The assembled cut file, at the path/source recorded in `assets.md` (the physical export
  location follows `knowledge/production/assembly-playbook.md`'s export path convention —
  produce does not invent a new location for it).
- `pipeline.py stage NNN CUT --next-action ... --next-action-owner critic` is the state
  transition that ends this skill.

## On failure
- Hygiene FAIL after producer's own fix attempts are exhausted: do not push to `/critique`;
  keep the item at PRODUCING, log the persistent failing check, and if it requires new raw
  material, fold it into the consolidated `[SPARSH]` ask.
- Lightroom/Chrome capture session fails (site change, auth issue): log the failure in
  `assets.md`; if unresolved within producer's own retry budget, add it to the single
  consolidated Sparsh ask (e.g., "needs a fresh screen recording") rather than opening a
  second separate request.
- `[GEN]` tool errors or quota exhaustion: log in `assets.md`, try the fallback prompt pattern
  in `genvideo-playbook.md`; if still broken, surface as a tooling blocker to the Showrunner —
  this is not automatically a Sparsh ask.
- A required `knowledge/production/*` playbook is missing/empty: halt and report it as a
  build gap. Never improvise capture or assembly steps ad hoc without the playbook to cite.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Checkpoint 1 — capture plan (before any long Lightroom session):** one short block — which
  raw, what edit arc, which capture-worthy moments we're hunting (sliders/masks/critic-
  rejection/before-after), expected session length. He may redirect the edit intent cheaply here.
- **Checkpoint 2 — [SPARSH] assets:** ask in-conversation the moment the need is confirmed AND
  record it as the BLOCKED-ON-SPARSH next-action (write-as-you-go; the ask must survive a
  context reset).
- **Checkpoint 3 — cut review (before G2):** show the assembled cut (export path, stills or a
  beat-by-beat description, hygiene_check output). Quick reactions → re-cut now; only a cut
  Sparsh has seen goes to the cold critic.
- AUTONOMOUS: proceed per playbooks; consolidate asks; G2 is the only reviewer.
