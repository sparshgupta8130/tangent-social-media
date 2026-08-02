---
name: script
description: Use when a pipeline item is at stage BRIEFED and needs a shot-by-shot script before it can face the G1 gate — turns brief.md into script.md and a provider-tagged asset manifest.
---

## Purpose
Turn an approved brief into an executable script: hook variants, a full beat sheet with loop
discipline, and an asset manifest that minimizes what only Sparsh can supply.

## Preconditions
- Item stage == `BRIEFED` (verify with `python tools/pipeline.py board`).
- `NNN-slug/brief.md` exists and is complete: concept, five selector scores, target emotion,
  payoff, pillar.

## Protocol
1. Confirm stage: `python tools/pipeline.py board`, locate NNN, confirm stage is BRIEFED. If
   not, stop (see On failure).
2. Invoke `story-lead` (Task, subagent_type `story-lead`) with inputs: `NNN-slug/brief.md`,
   `knowledge/craft/reels/hooks.md`, `knowledge/craft/reels/structure-and-retention.md`,
   `knowledge/craft/reels/scripting-voice.md`, `knowledge/brand/tangent-voice.md`, and whichever of
   `knowledge/platform/instagram.md` / `knowledge/platform/youtube.md` match the brief's
   platform(s).
3. Scriptwriter writes `templates/script.md` into `NNN-slug/script.md` containing: ≥3 hook
   variants, a beat sheet with timestamps, on-screen text, VO, audio plan, and a loop map
   (every loop opened must show where it closes).
4. Scriptwriter writes/updates `NNN-slug/assets.md`: every asset gets exactly one provider tag
   — `[AGENT]`, `[GEN]`, or `[SPARSH]`. Every `[SPARSH]` line must carry a one-line
   justification of why no `[AGENT]`/`[GEN]` substitute reaches the quality bar (per
   SYSTEM_DESIGN §1's autonomy contract) — an unjustified `[SPARSH]` tag is a defect.
5. Skill-level check before advancing (not a critic pass): loop map has zero unclosed loops,
   hook variants ≥3, no asset row missing a provider tag or status. If `[SPARSH]` count is
   high (>2) for the item, ask story-lead to re-attempt substitutions before accepting it.
6. Advance stage and hand off to G1 in one call:
   `python tools/pipeline.py stage NNN SCRIPTED --next-action "Run G1 critique" --next-action-owner critic`
7. `[SPARSH]` lines in assets.md are not chased individually here — full consolidation into one
   tracked ask happens at `/produce` (step 5 of that skill). This step is just the completeness
   gate (step 5 above); do not ping Sparsh per-asset from `/script`.

## Gates
- script.md must have ≥3 hook variants and a fully-closed loop map before the item can leave
  this skill — this is a completeness gate, distinct from and prior to the G1 critique gate.
- assets.md must have zero blank/missing provider tags and every `[SPARSH]` line justified.
- Failing either gate means the item stays at BRIEFED; it does not advance to SCRIPTED.

## Outputs
- `NNN-slug/script.md` (hooks, beat sheet, on-screen text, VO, audio plan, loop map).
- `NNN-slug/assets.md` (full manifest, provider-tagged, [SPARSH] minimized and justified).
- `pipeline.py stage NNN SCRIPTED --next-action ... --next-action-owner critic` is the state
  transition that ends this skill.

## On failure
- Loop map incomplete or <3 hooks: re-dispatch `story-lead` with the named defects (which
  loop doesn't close, which beat lacks a variant) — same re-dispatch-with-named-defects
  pattern as QC_PROTOCOL Gate B. Cap at 2 re-dispatches; if still failing, escalate to the
  Showrunner rather than accepting a weak script into G1.
- brief.md missing required fields (no target emotion, no scored selector points): kick back
  to `/ideate` — never fabricate a missing score to unblock scripting.
- Item stage isn't BRIEFED (e.g., already SCRIPTED or killed): abort, run
  `python tools/pipeline.py board` to find the correct next skill; don't force a transition.
- knowledge/craft files missing or empty: halt and surface as a build gap — don't script from
  memory when the craft substrate isn't there to cite.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Checkpoint 1 — hook & shape (before full polish):** present the ≥3 hook variants (frame-0
  described in words, per the first-frame test) + the beat-sheet skeleton + which owned format
  this rides. Recommend one hook. Sparsh picks/blends/redirects; story-lead respins inline.
- **Checkpoint 2 — pre-G1 read-through:** present the finished script, the loop map, and
  assets.md — flag every [SPARSH] line and its justification so he can veto or volunteer
  early. Fold his reactions in BEFORE `/critique`; the critic still grades the result cold.
- His taste enters here, not at the gate: shaping the script with Sparsh is exactly the point;
  softening the critic later is forbidden.
- AUTONOMOUS: story-lead ranks its own hook variants, straight to G1.
