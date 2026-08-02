---
name: weekly-review
description: Use every Friday — the ritual that runs growth accounting vs medians, checks strategy/BETS.md gates against real numbers, makes format kill/keep calls, and feeds next week's plan. This is the only skill allowed to change BETS.md status.
---

## Purpose
Turn a week of published, second-sourced data into decisions: bet-gate verdicts with real
numbers, pillar-vs-median accounting, the audience-mismatch early-warning check, and format
kill/keep calls that fold straight into next week's roadmap.

## Preconditions
- At least one week of `PUBLISHED`/`CLOSED` items with postmortems done where T+72h has
  elapsed.
- `tools/metrics.py` operable; `strategy/BETS.md` and `knowledge/benchmarks.md` present.
- The rolling stats CSV (schema in `tools/README.md`: date, platform, url, pillar, views,
  likes, comments, shares, saves, funnel, followers_at_post — all 11 columns required by
  `metrics.py`) is kept at `ops/calendar/posts.csv`, appended to by the analyst as each
  postmortem closes.

## Protocol
1. Confirm `ops/calendar/posts.csv` is current through this week's postmortems (analyst
   appends any rows missed).
2. Run: `python tools/metrics.py report --csv ops/calendar/posts.csv --followers N --json` —
   produces likerate/decompose/efficiency/funnel per row plus the account-level summary
   (medians, spread, efficiency, the audience-mismatch triad check).
3. Invoke `analyst` (Task, subagent_type `analyst`) with the report, `strategy/BETS.md`,
   `knowledge/benchmarks.md` to produce: growth accounting vs medians (plan on medians, treat
   spikes as windfalls per STRATEGY §6.1), pillar-vs-median accounting (HERO vs WORKHORSE vs
   FILLER medians compared), a bet-gate check for every active bet in `BETS.md` (compute
   whether its stated validation gate or kill/pivot trigger is now met, using this week's real
   numbers), and the audience-mismatch early-warning triad (efficiency sliding under ~5%; hits
   coming only from off-pillar content; flat non-pinned spread — STRATEGY §6.6).
4. Analyst DRAFTS, for each bet whose gate condition looks met, a proposed `Status` change
   (UNTESTED → VALIDATING → VALIDATED/FAILED) with the citing numbers — but does not write
   `strategy/BETS.md` unilaterally. Per `ops/ROLES.md` decision right (d), a bet-status change
   is decided only by Sparsh + Showrunner jointly, on the analyst's evidence, inside this
   ritual. Present the draft changes to Sparsh in this session; only once he concurs does the
   Showrunner commit the `Status`/Notes lines to `strategy/BETS.md`. If Sparsh isn't present in
   the session, write the proposed changes into `ops/calendar/review-YYYY-WW.md` as "pending
   Sparsh sign-off" and do not touch `BETS.md` yet — this IS the only skill permitted to ever
   write that file, but permission to write is not permission to decide
   alone.
4b. Invoke `brand-director` (Task, subagent_type `brand-director`) with the analyst's
   report + `ops/council/notes-ledger.md` + audience-advocate's sentiment summary to produce
   the **brand-health section** (RUNBOOK §9): positioning-drift check (one-line-description
   test on the week's output), distinctive-asset consistency, portfolio balance, and any
   ADVANCE-WITH-NOTES themes that should become standing guidance. `knowledge/marketing/`
   [OWN-DATA] updates happen here only (ROLES.md decision right (i)).
5. Invoke `creative-director` (Task, subagent_type `creative-director`) with the analyst's
   report to make format kill/keep calls (STRATEGY §4: ≤3 owned formats, replaceable only at
   this weekly checkpoint, never mid-week). If a format is killed or a new one added, append a
   dated `[OWN-DATA]` decision line to `knowledge/brand/content-architecture.md`'s format
   list.
6. Invoke `planner` (Task, subagent_type `planner`) to fold the creative-director's decisions
   into the roadmap — this reuses `/plan roadmap`'s logic against the now-current
   `BETS.md`/format list.
7. Write the full review into `ops/calendar/review-YYYY-WW.md` from `templates/weekly-review.md`.

## Gates
- No `BETS.md` status change without the exact numeric evidence the bet's own validation-gate
  or kill-trigger language calls for — never a judgment-call promotion.
- No `BETS.md` status change without Sparsh + Showrunner joint sign-off (`ops/ROLES.md`
  decision right (d)) — the analyst proposes, it does not decide.
- The audience-mismatch triad hitting 2-of-3 signals is a mandatory flag in the output doc; it
  cannot be silently absorbed into "things look fine."
- Format kill/keep decisions only happen here, on schedule — a mid-week creative itch to swap
  formats is not honored outside this ritual (STRATEGY §4).

## Outputs
- `ops/calendar/review-YYYY-WW.md` (full review, from `templates/weekly-review.md`).
- `strategy/BETS.md` — status/notes updated in place.
- `knowledge/brand/content-architecture.md` — `[OWN-DATA]` format decisions appended, if any.
- `ops/calendar/ROADMAP.md` — folded-in decisions via `planner`.
- No single `pipeline.py` stage transition ends this skill (it's cross-item); any resulting
  item-level actions (e.g., killing a format's in-flight items) are executed via the normal
  skill for that item (e.g., `pipeline.py kill NNN --reason "format retired at weekly review"`).

## On failure
- Not enough data yet (early weeks, <5 posts): still run the ritual at reduced scope; compute
  medians but flag them low-confidence rather than skipping the ritual entirely.
- `metrics.py report` errors on a malformed CSV row: fix the row per the schema in
  `tools/README.md` before rerunning — don't skip the numeric gate math for a bad row.
- Audience-mismatch triad hits 2/3: this is a mandatory escalation, not a footnote — write one
  consolidated strategy-review note to Sparsh via `planner`.
- Sparsh not present to sign off on a proposed BETS.md change: leave it "pending Sparsh
  sign-off" in the review doc and carry it forward to the next session where he is — never
  auto-approve on timeout, same principle as SHIP approval.
- Plane unavailable when folding decisions into the roadmap: fall back to `ROADMAP.md`-only
  per §9 and queue the sync.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- This ritual is DESIGNED for the interactive session: walk the metrics report, bet-gate
  table, pillar accounting, and triad check together, section by section, with the analyst's
  evidence on screen.
- **BETS.md changes happen live:** analyst proposes with numbers → Showrunner takes a position
  → Sparsh concurs or rejects in-conversation → only then is the status committed (ROLES.md
  decision right (d)). Absent Sparsh, everything stays "pending sign-off" — enthusiasm from
  earlier sessions never counts as concurrence.
- **Format kill/keep is a debate, not a report:** creative-director argues its call; Sparsh
  rules; the [OWN-DATA] decision line records both the ruling and the dissent if any.
