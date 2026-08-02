---
name: brand-review
description: The G3 brand gate — use once an item's G2 cut gate has passed (critiques/G2-cut*.md carries VERDICT SHIP), before Sparsh's SHIP approval is requested. Runs the three Brand Office agents in parallel on independent lenses and writes the binding ADVANCE / ADVANCE-WITH-NOTES / HOLD verdict that tools/pipeline.py requires before READY→PUBLISHED.
---

## Purpose
Judge the brand trajectory the item creates — a different altitude from the critic's G2 (which
judges the video: craft, hook, virality). G3 asks one question only: does this compound the
Tangent brand?

## Preconditions
"Runs at READY" is imprecise — the actual requirement is narrower. Either:
- the item is at stage `CUT` with `critiques/G2-cut*.md` already carrying a `VERDICT: SHIP` line
  (i.e., the `/critique` G2 pass has just completed and the `CUT`→`READY` stage call hasn't been
  made yet), **or**
- the item is already at stage `READY` (the `CUT`→`READY` transition has happened) but has no
  `critiques/G3-brand*.md` yet.

Run this skill immediately after G2 SHIP, before or right after the `CUT`→`READY` transition —
`tools/pipeline.py` only enforces the G3 gate at the `publish` command (the `READY`→`PUBLISHED`
transition), not at `CUT`→`READY`, so nothing tool-side stops you from delaying — but the protocol
runs it now, before Sparsh's SHIP approval is requested, so the SHIP conversation and the G3
verdict land in one sitting (Interaction checkpoints, below).

## Protocol
1. **Assemble the review packet:** final cut path + `tools/hygiene_check.py` PASS output,
   `publish.md` draft, `brief.md` (incl. BTS + full consult history), `script.md`, current
   `strategy/BETS.md` status, `knowledge/marketing/distinctive-assets.md`.
2. **Invoke the three Brand Office agents IN PARALLEL** (Task, one call per `subagent_type`:
   `brand-director`, `growth-lead`, `audience-advocate`), each given the full packet and
   instructed to score ONLY its own lens 1-10 with evidence citations. Do not let any agent see
   another's score before submitting its own — independence is the point (§12.4 step 1); a lens
   score produced after seeing the others isn't independent, it's anchored.
3. **`brand-director` synthesizes** `critiques/G3-brand.md` from `templates/brand-scorecard.md`
   once all three scores exist:
   - Three lens blocks: **Brand-Equity Impact** (strategist), **Growth Contribution** (scientist),
     **Audience Trust** (advocate) — each /10 with cited reasoning and its own checklist.
   - Hard-HOLD trigger checklist, explicitly ticked yes/no: never-list violation; unmitigated
     backlash-flashpoint adjacency; positioning drift (one-line-description test fails);
     distinctive-asset violation.
   - Verdict math: `mean = (Brand-Equity + Growth + Audience Trust) / 3`.
     - **ADVANCE** — all three ≥7 AND mean ≥7.5, no hard-HOLD trigger.
     - **ADVANCE-WITH-NOTES** — no lens ≤4, mean ≥6, no hard-HOLD trigger; append each note to
       `ops/council/notes-ledger.md` (what + which future item type it binds).
     - **HOLD** — any lens ≤4, OR mean <6, OR any hard-HOLD trigger ticked yes.
   - The exact standalone verdict line — `VERDICT: ADVANCE` / `VERDICT: ADVANCE-WITH-NOTES` /
     `VERDICT: HOLD` (no `##`, no surrounding text, case-sensitive, its own line) — is what
     `tools/pipeline.py`'s `_g3_error` check greps for before allowing `READY`→`PUBLISHED`; only
     `ADVANCE` and `ADVANCE-WITH-NOTES` satisfy it, same grep contract as G1/G2.
4. **HOLD → escalate to Sparsh** with the strategist's reasoning and the Showrunner's own position
   in the same conversation. Only Sparsh can override; the override is recorded as a new
   `critiques/G3-brand-r2.md` carrying `VERDICT: ADVANCE` plus the override note (who, why) — never
   by editing the original file.
5. **ADVANCE-WITH-NOTES notes** get appended to `ops/council/notes-ledger.md` (running list); the
   strategist checks it at the NEXT item's G3 and at every `/weekly-review`. An unchecked note is a
   broken commitment, not a completed one.

## Gates
- G3 never re-litigates G2: no craft/hook/virality scoring appears in any lens's reasoning
  (SYSTEM_DESIGN §12.4 rule 4) — the Brand Office cites brand-level evidence only.
- One G3 per item unless the cut materially changes after review; a materially unchanged re-review
  is not permitted (no "try again for a better score").
- All three lens scores must exist, cited, before synthesis — a missing or uncited lens blocks
  writing the scorecard at all (see On failure).

## Outputs
- `NNN-slug/critiques/G3-brand.md` (round 1) or `G3-brand-r2.md` (Sparsh override only — never a
  routine re-score).
- No `pipeline.py` stage transition is triggered by this skill itself — `tools/pipeline.py publish`
  (the READY→PUBLISHED transition) is what later reads this file's verdict line.

## On failure
- A lens agent returns an uncited or vague score: re-dispatch that agent once, same round, naming
  the specific defect (the QC_PROTOCOL Gate-B pattern used elsewhere in this system) — this is a
  Brand Office-output defect, not grounds to write around it with a guessed score.
- Verdict math and the strategist's own instinct disagree (the numbers say ADVANCE-WITH-NOTES but
  the strategist feels HOLD, or vice versa): the math wins for the verdict line; the instinct is
  written into the scorecard's notes/reasoning, not substituted for the computed verdict.
- A HOLD's hard-HOLD trigger is genuinely ambiguous (e.g., a positioning-drift call that's close):
  write the ambiguity and the strategist's recommendation into the scorecard itself, escalate to
  Sparsh as a HOLD regardless — ambiguity resolves toward caution at this gate, not away from it.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **INTERACTIVE:** walk the G3 verdict with Sparsh right before his SHIP decision — they are
  adjacent moments by design, one conversation covers both. Present all three lens scores with
  their citations, the hard-HOLD checklist as ticked, and the verdict line.
- **HOLD is presented with options:** the strategist's reasoning, the Showrunner's own position,
  and (if one exists) a concrete path to ADVANCE-WITH-NOTES on a revised cut — Sparsh decides
  whether to override, kill, or send back for revision.
- **AUTONOMOUS:** ADVANCE or ADVANCE-WITH-NOTES proceeds straight to the SHIP ask (folds into the
  same consolidated ask as the SHIP approval itself). HOLD stops the item at READY and joins the
  consolidated Sparsh ask rather than generating a separate ping.
