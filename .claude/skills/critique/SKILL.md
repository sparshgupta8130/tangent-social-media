---
name: critique
description: Use when a pipeline item is at stage SCRIPTED and needs its G1 script gate, or at stage CUT and needs its G2 cut gate — runs the 8-lens scorecard and writes a binding SHIP/FIX/KILL verdict. Also use for a re-review after a FIX round.
---

## Purpose
The independent quality gate. Scores the actual work product — never the author's opinion of
it — against the 8-lens scorecard, and writes a verdict nothing may bypass.

## Preconditions
- G1 mode: stage == `SCRIPTED`; `script.md` and `assets.md` present.
- G2 mode: stage == `CUT`; a cut file (or full description + stills if it can't be attached)
  and `assets.md` present. `tools/hygiene_check.py` PASS is required before the critic scores
  — not after.
- Structural independence (SYSTEM_DESIGN §3): pass the critic the raw work product only — no
  story-lead/producer self-assessment, cover note, or "here's why this works" summary.

## Protocol
1. Read `item.yaml` to determine mode (stage SCRIPTED → G1, stage CUT → G2) and round: check
   `NNN-slug/critiques/` for an existing `G1-script.md`/`G2-cut.md` to know if this is round 2
   (`-r2` suffix) or round 3 (`-r3` suffix).
2. **G2 only — run first, before any critic involvement:**
   `python tools/hygiene_check.py <path-to-cut>`. If overall result is FAIL, STOP here — do
   not invoke the critic. Return to `/produce` with the exact failing checks named (see On
   failure).
3. Invoke `critic` (Task, subagent_type `critic`) with the stripped work product
   (script.md+assets.md for G1; cut+assets.md+hygiene PASS confirmation for G2) plus:
   `templates/critique-scorecard.md`, `knowledge/craft/*`, `knowledge/virality/laws.md`,
   `knowledge/virality/failure-modes.md`, the matching `knowledge/platform/*.md`,
   `knowledge/pattern-library.md`, `knowledge/audience/*`, `knowledge/brand/*`.
4. Critic scores lenses 1-7 1-10 each, with cited evidence (a knowledge-file + law per
   deduction, never a vibe): HOOK, STRUCTURE & RETENTION, EMOTION & INTENSITY,
   CLARITY & ONE-IDEA, CRAFT & AESTHETICS, AUDIENCE FIT & SHAREABILITY, DIFFERENTIATION. Lens 8
   HYGIENE & COMPLIANCE is scored separately as binary PASS/FAIL per check (platform penalty
   list, engagement-bait line, disclosure rules, brand non-negotiables) — it is NOT part of the
   1-10 mean, any single FAIL blocks SHIP regardless of the mean.
5. Compute gate math exactly as `templates/critique-scorecard.md` specifies (deterministic, not
   the critic's call to fudge) — **only lenses 1-7 feed the mean, HOOK counted twice, divided
   by 8** (not 9 — lens 8 is excluded, it's binary, not a score):
   `weighted_mean = (2×HOOK + STRUCTURE + EMOTION + CLARITY + CRAFT + AUDIENCE + DIFFERENTIATION) / 8`
   Eligible for SHIP only if: weighted_mean ≥ 7.5 AND HOOK ≥ 8 AND lens-8 ALL-PASS.
6. Critic writes the verdict: **SHIP** / **FIX** (ranked, concrete fixes) / **KILL** (reason +
   salvage note) — plus, always, "what would make this a 10."
7. Write the full scorecard + verdict to `NNN-slug/critiques/G1-script.md` or
   `G2-cut.md` (round 1); `-r2.md` / `-r3.md` for re-reviews, instantiating
   `templates/critique-scorecard.md`. **The template's own `## VERDICT: SHIP | FIX | KILL`
   heading is NOT what the tool checks** — under it, the critic must also write a standalone
   line reading exactly `VERDICT: SHIP` (no `##`, no ` | FIX | KILL`, case-sensitive) when and
   only when the verdict is SHIP. `pipeline.py`'s gate check greps the file for that literal
   line before allowing the stage transition in step 8; a FIX/KILL verdict must NOT contain it.
8. Update `item.yaml` per verdict:
   - G1 SHIP → `python tools/pipeline.py stage NNN PRODUCING --next-action "Execute assets.md" --next-action-owner producer`
   - G2 SHIP → `python tools/pipeline.py stage NNN READY --next-action "Sparsh SHIP approval" --next-action-owner sparsh`
   - FIX → stage unchanged; record it as a same-stage touch (this only updates fields, no
     transition is attempted, so it can never trip the legality check):
     `python tools/pipeline.py stage NNN SCRIPTED --next-action "Revise per critiques/G1-script.md round N" --next-action-owner story-lead`
     (swap `SCRIPTED`/`story-lead` for `CUT`/`producer` in G2 mode).
   - KILL → `python tools/pipeline.py kill NNN --reason "<critic's reason>"`.

## Gates
- Gate math exactly as in step 5 — no rounding favors, no "close enough."
- Max 2 FIX rounds per gate. Round 1 = the base file; round 2 = `-r2`; if round 2 is FIX
  again, that is the second and last permitted FIX. The round-3 review (`-r3`) MUST resolve to
  SHIP or KILL — a third FIX verdict is not a legal output.
- If round 3 can't honestly resolve to SHIP or KILL (genuine creative disagreement), the
  critic does not force one: write the open question + the team's best two options + a
  recommendation into the item folder and flag `planner` to surface it to Sparsh, per
  CLAUDE.md's low-confidence protocol.
- G2 hygiene PASS is a precondition to scoring, not a lens — a hygiene FAIL never reaches the
  scorecard.
- The literal `VERDICT: SHIP` line is the only thing `pipeline.py stage` checks for — writing
  it without the gate math actually being met is a process violation, not just a formality.

## Outputs
- `NNN-slug/critiques/G1-script.md` or `G2-cut.md` (+ `-r2`/`-r3` on re-review).
- `item.yaml` stage transition per verdict (PRODUCING / READY / unchanged-with-next_action /
  KILLED) — this transition is what ends the skill.

## On failure
- Hygiene FAIL (G2): list the failing ffprobe checks verbatim (resolution/aspect ratio,
  duration band, audio stream, codec, black-border/cropdetect, duplicate hash) in a note back
  to `/produce`; do not proceed to critic scoring until a rerun of `hygiene_check.py` is PASS.
- Critic returns an uncited or vague lens score: re-dispatch the critic once, same round,
  demanding a knowledge-file + law citation per deduction. This does not consume one of the
  author's 2 FIX rounds — it's a critic-output defect, not a work-product defect.
- Round 3 still unresolved: escalate per the Gates section above; never leave an item sitting
  at an ambiguous stage.
- Plane sync: note the stage change so `planner` can reflect it in Plane on its next pass;
  critique doesn't call Plane MCP directly.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **The critic runs isolated in BOTH modes.** Never pass it Sparsh's opinions, the session
  conversation, or the author's case for the work; never re-run it hoping for a friendlier
  verdict. One critique per round, as specced.
- **Checkpoint — verdict walkthrough (after the critique file is written):** walk the
  scorecard together: per-lens scores with their cited laws, the ranked fixes, "what would
  make this a 10." Showrunner states its own position (agree/disagree with the critic, and why).
- **Sparsh's options:** accept fixes (→ respin via the owning skill); accept a KILL; or
  overrule — an overrule is written into the critique file as a logged knowledge-law exception
  (CLAUDE.md final paragraph) and the item proceeds. A hygiene FAIL can never be overruled.
- Fix-round cap (2) holds in both modes — iteration happens in /script and /produce, not by
  burning critique rounds.
