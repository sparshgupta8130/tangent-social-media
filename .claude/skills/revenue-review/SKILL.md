---
name: revenue-review
description: Use monthly (first working session of each month) — the ritual where revenue-lead reviews the month's metrics against strategy/REVENUE.md §2 thresholds, checks the product pipeline, flags threshold crossings, and proposes REVENUE.md changes for Sparsh + Showrunner sign-off. The ONLY skill allowed to change REVENUE.md §2 thresholds/stream statuses. Output: ops/revenue/review-YYYY-MM.md.
---

## Purpose
Turn a month of list/funnel (and later revenue) data into sequencing decisions: is any
revenue stream's activation threshold newly crossed, is any product passing or failing its
gates, and does `strategy/REVENUE.md` §2 still describe reality? Same governance pattern as
`/weekly-review`'s BETS.md discipline — the reviewing agent proposes with numbers; Sparsh +
Showrunner decide; the file changes only here.

## Preconditions
- `strategy/REVENUE.md` exists and its §2 table is current (last month's review committed).
- The analyst's latest weekly report (`ops/calendar/review-YYYY-WW.md`) is available — the
  weekly email/funnel KPI rows are this ritual's raw input; revenue-lead never re-derives them.
- ESP and ManyChat dashboards reachable for month-end counts (list size, adds, DM trigger
  events, DM→email conversion). If the ESP isn't chosen/wired yet (`publishing-ops.md` §5),
  that is itself the month's headline finding — run at reduced scope and flag it.

## Protocol
1. Assemble the month's numbers from the weekly reviews (+ dashboard month-end pulls):
   email adds by week, list size, DM requests, DM→email %, funnel comment:like medians.
   Second-source discipline applies: dashboard counts are platform-official primaries, but
   any number that also appears in a weekly report must agree with it — divergence is
   resolved before the review proceeds, not averaged over.
2. Invoke `revenue-lead` (Task, subagent_type `revenue-lead`) with `strategy/REVENUE.md`,
   the assembled numbers, `strategy/BETS.md` (BET-2 status), and the month's `ops/revenue/`
   files, to produce the four analytical sections of `templates/revenue-review.md`:
   metrics-vs-thresholds table, stream-by-stream status, product-pipeline table (every open
   opportunity brief: stage, test verdicts, kill-gate check), threshold-crossing flags.
3. For each threshold-crossing flag (a §2 stream whose activation condition is newly met —
   or a live stream hitting a kill/park condition), revenue-lead DRAFTS a proposed §2
   status/threshold change with the citing numbers — it does not write `strategy/REVENUE.md`.
4. Sparsh + Showrunner sign-off, in-session (same pattern as BETS.md): present each proposed
   change; Showrunner takes a position; Sparsh concurs or rejects; only then does the
   Showrunner commit the §2 lines. If Sparsh isn't present, the change is recorded in the
   review doc as "pending Sparsh sign-off" and `REVENUE.md` is not touched.
5. Decisions with money attached (a GO on a product, a price, any spend) are NEVER made
   inside this ritual by default-approve — they are put to Sparsh explicitly (ROLES.md (g)),
   and an unanswered ask stays open as a `BLOCKED-ON-SPARSH` action.
6. Write `ops/revenue/review-YYYY-MM.md` from `templates/revenue-review.md`, including the
   decisions log (with sign-off lines) and next-month actions; hand roadmap-relevant actions
   (e.g., "commission media kit," "schedule launch posts") to `planner` for
   `ops/calendar/ROADMAP.md`.

## Gates
- This is the ONLY skill that may change `strategy/REVENUE.md` §2 thresholds/statuses — and
  permission to write is not permission to decide alone (Sparsh + Showrunner joint sign-off,
  mirroring ROLES.md decision right (d)'s pattern).
- No status change without the exact numeric evidence the §2 activation condition names —
  never a judgment-call activation, never "close enough."
- A stream never activates on enthusiasm ahead of its threshold — the premature-media-kit
  failure mode (`revenue-lead.md`) is checked by name when sponsorship status is discussed.
- Product kill gates are honored on schedule: a product past its pre-registered gate is
  killed or gets an explicit, recorded Sparsh override — sunk-cost discipline is not
  negotiable (REVENUE.md §3).
- Every number in the review doc traces to a dashboard pull, a weekly report, or
  `[OWN-DATA]` — else it is written UNKNOWN with a research gap (SOURCES.md rule).

## Outputs
- `ops/revenue/review-YYYY-MM.md` (from `templates/revenue-review.md`).
- `strategy/REVENUE.md` — §2 statuses/thresholds updated in place (signed-off changes only).
- `BLOCKED-ON-SPARSH` next-actions for any open money ask; roadmap deltas via `planner`.
- No pipeline stage transition ends this skill (it's cross-item, like `/weekly-review`).

## On failure
- ESP/ManyChat unreachable or not yet wired: run at reduced scope on weekly-report data
  alone; log the gap as the review's first flag — never skip the month.
- Fewer than 4 weekly reports this month (early weeks): run anyway, mark all trend reads
  low-confidence; thresholds are checked against whatever real numbers exist.
- Sparsh absent: all proposed §2 changes and money asks recorded "pending Sparsh sign-off,"
  carried to the next session he attends — never auto-approved on timeout.
- A metrics divergence (dashboard vs. weekly report) that can't be resolved in-session:
  the affected threshold check is marked UNRESOLVED, not decided on the friendlier number.
- **AUTONOMOUS mode** (house convention, RUNBOOK §1): produce everything through step 3 —
  assembled numbers, filled review doc, drafted proposals — but commit nothing to
  `strategy/REVENUE.md` and approve no money decision; consolidate every ask into one
  `BLOCKED-ON-SPARSH` action with a due date, and log the decisions taken on high-confidence
  defaults (metric assembly choices only, never activations).

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- Walk the review section by section with Sparsh: metrics vs. thresholds first (with the
  weekly evidence on screen), then pipeline, then crossings.
- **Threshold crossings are a debate, not an announcement:** revenue-lead argues the numbers;
  the Showrunner takes a position (including "the threshold itself is miscalibrated —
  propose a threshold change instead"); Sparsh rules; the decisions log records ruling and
  dissent.
- **Product GO/PARK/KILL and every price are put to Sparsh as single, concrete asks** — one
  decision per ask, with the brief's evidence attached, never a bundle of "approve all."
- REVENUE.md §2 edits happen live in-session after sign-off, on screen — the file is the
  record, the conversation is the interface.
