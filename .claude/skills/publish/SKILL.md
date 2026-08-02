---
name: publish
description: Use when a pipeline item is at stage READY and Sparsh has given final SHIP approval — finalizes publish.md per the platform checklist, posts, and records the published URL.
---

## Purpose
Turn a READY, Sparsh-approved item into a live post: finalize every publishing-ops checklist
field, confirm the funnel deliverable is real, and close the loop with a recorded URL.

## Preconditions
- Item stage == `READY` (G2 SHIP already recorded).
- **G3 brand verdict present**: `critiques/G3-brand*.md` with `VERDICT: ADVANCE` or
  `VERDICT: ADVANCE-WITH-NOTES` (run `/brand-review` first — `pipeline.py publish` hard-blocks
  without it; a HOLD needs Sparsh's override recorded as `G3-brand-r2.md`). SYSTEM_DESIGN §12.4.
- `item.yaml` `approved_by_sparsh` is set to a date — Sparsh's hard SHIP gate
  (CLAUDE.md non-negotiable #7: "Nothing publishes without G2 SHIP + G3 ADVANCE + Sparsh
  approval"). If this field is blank, this skill does not proceed past step 2.

## Protocol
1. `python tools/pipeline.py board` — confirm stage READY for NNN.
2. Read `item.yaml`'s `approved_by_sparsh`. If blank, STOP (see On failure) — the recording
   mechanism (once Sparsh has actually said yes) is a same-stage touch, since READY is already
   the current stage and no transition is being attempted:
   `python tools/pipeline.py stage NNN READY --approved-by-sparsh` (bare flag stamps today's
   date; pass an explicit `--approved-by-sparsh YYYY-MM-DD` to backdate it). Only planner runs
   this, and only after Sparsh's actual decision — never speculatively.
3. Invoke `producer` (platform mechanics) and `planner` (scheduling/Plane bookkeeping)
   together with: the full item folder (`script.md`, `assets.md`, the cut) and
   `knowledge/platform/publishing-ops.md`'s checklist.
4. Write `NNN-slug/publish.md` covering every checklist field from `publishing-ops.md`: final
   caption (per platform variant), cover/thumbnail choice, audio credit, hashtags, DM keyword +
   the exact deliverable file path it triggers, the disclosure line (per
   `knowledge/audience/positioning.md`), and posting time (per platform playbook / roadmap
   cadence). If a dedicated `templates/publish.md` exists by the time this runs, instantiate
   it; otherwise construct `publish.md` directly from this field list.
5. Confirm the funnel deliverable file actually exists at the stated path — a keyword-DM CTA
   with no real deliverable behind it is the constitutional engagement-bait line
   (CLAUDE.md #6); block until it's real.
6. Post per platform. If native scheduling/posting automation is available and in-scope for
   `producer`, use it; otherwise hand the finalized `publish.md` + asset bundle to Sparsh as
   the single posting action needed (this is a posting mechanics gap, not a re-approval ask).
7. Once the post is live and its URL is known, record it AND the export for the repost guard
   in one call (requires stage READY + `approved_by_sparsh` set, both from steps 1-2; this call
   performs the READY→PUBLISHED transition):
   `python tools/pipeline.py publish NNN --url <url> --video <path-to-exported-cut>`
   — `--video` is what triggers the SHA-256 repost-guard hash into
   `ops/pipeline/.published_hashes.json`; omitting it records the URL but skips the guard, so
   always pass it when the file is available.
8. Immediately follow with a same-stage touch to hand off the postmortem trigger (`publish`
   itself takes no `--next-action` flags):
   `python tools/pipeline.py stage NNN PUBLISHED --next-action "Run /postmortem" --next-action-owner analyst --due <post-date+3d>`

## Gates
- `approved_by_sparsh` must be a set date before step 7 — `pipeline.py publish` itself refuses
  to run without it. No exceptions, no "he said it was fine earlier" — this is the human
  hard-approval point named in SYSTEM_DESIGN §1.
- Every `publish.md` checklist field filled — no blank caption, hashtags, disclosure line, or
  posting time.
- Any DM-keyword funnel line requires a verified-existing deliverable file before posting.

## Outputs
- `NNN-slug/publish.md` finalized.
- `item.yaml`: `approved_by_sparsh` set, stage=`PUBLISHED`, `published` map recorded, fresh
  `next_action`/`due` for the postmortem.
- `ops/pipeline/.published_hashes.json` updated (via `--video`, not by hand).
- `pipeline.py publish NNN --url <url> --video <path>` is the state transition that ends this
  skill.

## On failure
- `approved_by_sparsh` missing: stop at step 2; write one consolidated `next_action`
  ("final SHIP approval needed") and flag `planner` — do not draft around it or post anyway.
- G2 wasn't actually SHIP (stage isn't really READY despite what was assumed): abort, route
  back to `/critique`.
- Funnel deliverable missing: block; either produce it now (folds into `/produce` if assets
  are incomplete) or delay the post — never ship the CTA without the payoff.
- `pipeline.py publish` errors (video file not found for hashing, bad URL, or the exact file
  hash was already published — the repost guard firing on a real repost): fix the path/URL or
  stop if it's a genuine repost; never hand-edit `item.yaml` to fake the PUBLISHED state or
  bypass the guard.
- No posting automation available: hand off the complete `publish.md` + asset bundle as a
  single "please post this now" ask to Sparsh, due today, flagged to `planner`.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- This skill is inherently interactive — it contains a hard approval point that no mode
  removes.
- **Walk publish.md together field by field:** caption (first-125-chars read aloud), cover
  frame, audio pick + fallback, DM keyword + deliverable (test it live), disclosure line,
  posting time with the reasoning. Showrunner recommends; Sparsh decides.
- **SHIP:** `pipeline.py stage NNN READY --approved-by-sparsh` only on his explicit yes in
  this conversation — never inferred from enthusiasm earlier in the session.
- **Post + confirm:** after posting, run `pipeline.py publish NNN --url <url> --video <path>`
  in the same sitting — a published item whose URL isn't recorded is a broken postmortem later.
- AUTONOMOUS: stop at READY + queued consolidated ask. Publishing never happens unattended.
