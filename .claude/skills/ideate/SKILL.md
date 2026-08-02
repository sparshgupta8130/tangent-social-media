---
name: ideate
description: Use when Sparsh drops a content note, a trends-log entry is rated A2 ("fold into next ideation"), or a postmortem's action-items section surfaces a new insight — turns the input into 5-10 scored concepts and writes the top 1-3 survivors into the pipeline as BRIEFED items.
---

## Purpose
Convert a raw input (Sparsh's note / A2 trend / postmortem insight) into concepts, apply the
concept-selector as a hard filter, and write only the survivors as briefs. Kills weak concepts
in writing so the reasoning isn't lost.

## Preconditions
- No pipeline stage required (this skill CREATES items, starting at IDEA).
- Input exists: the note text, OR an A2-rated line in `ops/calendar/trends-log.md`, OR a
  named insight in a recent `postmortem.md`'s action-items section.
- Required reads: `strategy/STRATEGY.md` §4 (selector formula, tiers), `strategy/BETS.md`
  (live bets), `knowledge/brand/content-architecture.md`, `knowledge/pattern-library.md`.

## Protocol
1. Identify the input and state it in one line (source: note text / trends-log date+line /
   postmortem NNN section 9).
2. Invoke `trend-scout` (Task, subagent_type `trend-scout`) with the input, asking for current
   context only: relevant recent `ops/calendar/trends-log.md` entries, live competitor moves,
   any open 0-4-day windows. This is context-gathering, not a new sweep — if `/trend-sweep`
   hasn't run in >24h, note that but don't block on it.
3. Invoke `creative-director` (Task, subagent_type `creative-director`) with: the input, the
   trend-scout context, `strategy/STRATEGY.md`, `strategy/BETS.md`,
   `knowledge/brand/content-architecture.md`, `knowledge/pattern-library.md`. Ask for 5-10
   concepts, each with: one-line premise, target pillar (HERO/WORKHORSE/FILLER), target
   emotion, and the concrete payoff.
4. Creative-director scores every concept against STRATEGY §4's five selector points
   (universal premise, concrete verifiable payoff, high-arousal named emotion, fits an owned
   format or is the one live audition, provable live on our own raws/pipeline). A concept must
   pass ALL FIVE or it is killed — no partial credit.
5. For every killed concept, write one line: `<concept name> — killed at point <N> — <why>`.
6. Rank survivors; take the top 1-3 (fewer if fewer pass). For each survivor, run:
   `python tools/pipeline.py new "<title>" --pillar HERO|WORKHORSE|FILLER --platform ig,yt`
   (platform list per concept; this creates `NNN-slug/` at stage=IDEA).
6b. For each survivor, compute the **Brand-Touch Score** (SYSTEM_DESIGN §12.3 flag table:
   new-format +3, identity-surface +3, commercial +3, backlash-adjacent +2, funnel-mechanic
   change +2, new platform +1, format/tone stretch +1). Write `BTS: <n> — flags: <list>` into
   the brief. **BTS ≥ 3 ⇒ `/consult` is mandatory before `/script`** (route per RUNBOOK §9);
   BTS 1–2 ⇒ Showrunner decides, decision noted in the brief; BTS 0 ⇒ proceed.
7. Fill `templates/brief.md` into `NNN-slug/brief.md`: concept, the five selector scores,
   target emotion, payoff, references (research/synthesis citations), and a "Killed
   Alternatives (this batch)" section listing every concept killed in step 5.
8. Create the Plane work item for NNN in project TANSOC (label = pillar name, lowercase). Do
   not add the `sparsh-input` label here — brief.md carries no asset tags yet; that label is
   added later, the moment the item's `next_action_owner` first becomes `sparsh` (per
   `ops/RUNBOOK.md` §6), and stays on even after it clears.
9. Advance stage in one call, recording the Plane id and handing off to `/script`:
   `python tools/pipeline.py stage NNN BRIEFED --plane-issue <returned-id> --next-action "Write script + assets.md" --next-action-owner story-lead`

## Gates
- The five-point selector (STRATEGY §4) is the hard gate — this skill has no separate
  critique pass. A concept missing even one point does not get a pipeline item, full stop.
- No brief ships without a named target emotion and a payoff that is SHOWN, not asserted.

## Outputs
- One `NNN-slug/` folder per surviving concept: `item.yaml` (stage=BRIEFED, `plane_issue`
  set), `brief.md` filled per step 7.
- `pipeline.py stage NNN BRIEFED --plane-issue <id> --next-action ... --next-action-owner story-lead`
  is the state transition that ends this skill for each item.

## On failure
- Trend-scout unavailable/no new context: proceed on STRATEGY.md + BETS.md alone; note the
  gap in the brief's references section, don't block ideation on it.
- Fewer than 5 concepts generated: still apply the selector in full; note the thin session in
  step 5's log so the pattern (weak input, not weak filter) is visible.
- Zero concepts survive: do NOT create any pipeline item. Instead append a dated entry to
  `ops/calendar/trends-log.md` (actionability A3) listing every concept and its kill reason,
  and flag `planner` so the empty ideation cycle surfaces at the next standup rather than
  vanishing silently.
- Plane MCP unavailable: per SYSTEM_DESIGN §9 fallback, run the step-9 `stage` command without
  `--plane-issue` (it stays null — the field is nullable by schema) and let planner queue the
  sync for when Plane is reachable — this never blocks the BRIEFED transition.
- `pipeline.py new`/`stage` errors (duplicate slug, bad pillar value): fix the input and
  retry; never hand-edit item.yaml to route around a validation failure.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Concept slate review (before any brief is written):** present ALL surviving concepts with
  their selector scores AND the kill list with one-line reasons — Sparsh sees what was killed,
  not just what survived. Lead with a recommendation (top 1-3, ranked, why).
- **Iterate inline:** he kills/merges/redirects/adds; respin with creative-director in the same
  conversation. New/changed concepts still face the full 5-point selector — his enthusiasm
  doesn't waive a failing point; name the failure and say so.
- **Advance:** write briefs + `pipeline.py new` only for concepts he greenlights (or delegates
  with "your call"). Record his framing/verbatim phrases in the brief — his language is often
  the hook seed.
- AUTONOMOUS: write the top 1-3 briefs directly; log the slate + kill list in the items'
  brief.md for later review.
