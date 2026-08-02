---
name: plan
description: Use for the Monday roadmap build/refresh, daily standups, a replan after a delay/news window/pivot, the very first run of the team (bootstrap) to create the Plane project, or a campaign plan (roadmap-level ideation producing a 4-6 week slate from the candidates backlog + research). Invoke as "/plan bootstrap|campaign|roadmap|standup|replan".
---

## Purpose
The TPM function: keep `ops/calendar/ROADMAP.md` and Plane's TANSOC project truthful, chase
`BLOCKED-ON-SPARSH` items as one consolidated ask, and re-sequence on delay/news/pivot.

## Preconditions
- `bootstrap`: only needed once — check first, don't recreate.
- `campaign`: the candidates tracker readable — the Google Sheet "Tangent — Content
  Candidates" (fileId in `strategy/CANDIDATES.md` header; read via Drive MCP
  `read_file_content`) with `strategy/CANDIDATES.md` as the evidence dossiers + offline
  fallback; run `bootstrap` first if Plane isn't set up. Use at launch, at each new
  campaign horizon (~every 4-6 weeks), or when a new lane enters play.
- `roadmap`: `strategy/STRATEGY.md` §7 (cadence bands) and `strategy/BETS.md` (live gates)
  readable; `tools/pipeline.py` operable.
- `standup`: `tools/pipeline.py board`/`blocked` operable.
- `replan`: a concrete trigger exists (overdue item, an A1 trend-sweep finding, or a
  `strategy/BETS.md` status change from `/weekly-review`).

## Protocol

### bootstrap (first run only)
1. `mcp__plane__list_projects` — if "Tangent Social" (identifier `TANSOC`) already exists,
   skip creation and go to step 3.
2. `mcp__plane__create_project(name="Tangent Social", identifier="TANSOC")`.
3. `mcp__plane__list_states` on TANSOC; create any missing from: Backlog, Planned,
   In Progress, Blocked-on-Sparsh, In Review, Done, Killed (`mcp__plane__create_state`).
4. `mcp__plane__list_labels` on TANSOC; create any missing from: `hero`, `workhorse`,
   `filler`, `series`, `news`, `ops`, `sparsh-input` (`mcp__plane__create_label`).
5. If Plane MCP is unavailable: fall back to ROADMAP.md-only operation per §9 and queue a
   sync note for when it returns — never block content work on this.

### campaign (roadmap-level ideation — the bridge from strategy/research to a schedulable slate)
This mode answers "what should the next 4-6 weeks of content BE", not just "when does it
run". It ideates at FRANCHISE/SERIES altitude (which formats, which arcs, what mix) —
individual reels still go through `/ideate` one at a time when their slot comes up.
1. Assemble the planning packet: `strategy/CANDIDATES.md` (the backlog — includes the ideas
   mined from `synthesis/04_TANGENT_STRATEGY.md` with provenance), `strategy/STRATEGY.md`
   (§4 architecture, §7 bands), `strategy/BETS.md` (which bets need validation data and how
   many posts their gates require), `knowledge/brand/content-architecture.md`,
   `knowledge/pattern-library.md` (what formats the corpus proves), the latest
   `ops/calendar/trends-log.md`, and Sparsh's stated project context (e.g. an external
   production like the PVC series — what episodes/assets land when).
2. Invoke `trend-scout` for a horizon sweep (what's coming in the next 4-6 weeks: releases,
   events, seasonal moments worth a slot).
3. Invoke `creative-director` with the full packet to propose the SLATE: which candidates
   activate, in what mix per week (HERO/WORKHORSE/FILLER within STRATEGY §7 bands), which
   bet each slot feeds data to, launch-sequencing per CANDIDATES' mined notes, and 2-3
   candidate additions of its own if the backlog has gaps. Every slate line cites its
   CANDIDATES entry or evidence.
4. Compute the BTS for the slate as a whole (SYSTEM_DESIGN §12.3): any new-lane activation
   (e.g. C7 PVC) or identity-surface implication triggers a mandatory `/consult` NOW —
   portfolio-level questions (brand architecture, lane sequencing, risk) get answered once
   here instead of once per item later.
5. Present slate + consult memos to Sparsh (INTERACTIVE checkpoint below); iterate.
6. On his nod: mark activated candidates `SCHEDULED (weeks N-M)` in the candidates Sheet
   (Sparsh in the Sheet UI, or Showrunner via Claude-in-Chrome; log pending updates if
   neither is possible); write
   the 4-6 week `ops/calendar/ROADMAP.md`; `python tools/pipeline.py new` the first ~2
   weeks' items (stage IDEA, with their candidate ref in the title/next_action) — later
   weeks stay as roadmap lines until their week approaches; sync Plane per `roadmap` mode
   steps 4-5.

### roadmap (Monday)
1. Read `strategy/STRATEGY.md` §7, `strategy/BETS.md`, run `python tools/pipeline.py board`,
   run `python tools/calendar.py` (renders the ROADMAP item table + pipeline state as a
   week-grid; flags cadence-band violations and HERO-drought >7 days).
2. Invoke `planner` (Task, subagent_type `planner`) with the above plus
   `knowledge/brand/content-architecture.md` to build/refresh `ops/calendar/ROADMAP.md` 3-4
   weeks out, staying inside the STRATEGY §7 bands (steady state 3-5 reels/week + 1 long-form/
   month, floor 2/week; launch surge only time-boxed ≤30 days, at most once/quarter, and only
   while pipeline health holds — no backed-up G2 failures, no BLOCKED-ON-SPARSH item >3 days).
3. Write each week's compact table (day/pillar/item-id/stage/risk, cadence-target line,
   HERO-drought check, news-response reserve slot, Sparsh-dependency summary) directly into
   `ops/calendar/ROADMAP.md` per its existing per-week section format — this file is the
   rolling view, not a second source of truth. Only spin out a separate
   `templates/roadmap-week.md` instance for a week that needs extra planning detail (e.g. a
   launch surge or a HERO week with many dependencies); most weeks don't need one.
4. Sync Plane: create work items for any roadmap entry lacking a `plane_issue`
   (`mcp__plane__create_work_item`, TANSOC, correct label/state); update state on existing
   ones to match pipeline stage (`mcp__plane__update_work_item`).
5. Any `calendar.py`-flagged cadence violation or HERO-drought must be resolved in this pass —
   either trim the roadmap back into band, or write an explicit bet-gate justification
   (citing `BETS.md`) for why this week exceeds it.

### standup (daily-ish, cheap)
1. `python tools/pipeline.py board` and `python tools/pipeline.py blocked`.
2. Identify overdue items and `BLOCKED-ON-SPARSH` items; for each, check whether the team can
   unblock it itself before treating it as a real Sparsh dependency.
3. If multiple Sparsh asks are pending, fold them into ONE consolidated message — never a
   drip (SYSTEM_DESIGN §1).
4. If Plane MCP available, sync states for any item whose pipeline stage moved since the last
   sync (`mcp__plane__update_work_item`).
5. No new files — updates land in the affected items' `item.yaml` `next_action` fields.

### replan
1. Confirm the trigger: overdue item, an A1 trend-sweep finding (0-4 day window), or a
   `BETS.md` status change.
2. Invoke `planner` with the trigger, current `ROADMAP.md`, and the pipeline board.
3. Re-sequence ROADMAP.md: insert the news-response/priority item, push out lower-priority
   filler, preserve HERO cadence and any active bet-gate data needs.
4. Update affected `item.yaml` `next_action`/`due` fields and Plane states.
5. Prepend a dated "Replan: `<reason>`" note at the top of ROADMAP.md's change log so the
   roadmap keeps its own audit trail.

## Gates
- `bootstrap` must complete (or be already-satisfied) before any Plane sync in the other
  modes is attempted — otherwise operate file-only.
- `roadmap`/`replan` may not exceed the STRATEGY §7 bands without a written bet-gate
  justification in ROADMAP.md.
- `standup`'s "one consolidated ask" rule is itself a gate on communication style, not optional
  formatting.

## Outputs
- `bootstrap`: Plane project/states/labels created (or confirmed present).
- `campaign`: updated candidate statuses in the Google Sheet tracker; a 4-6 week `ops/calendar/ROADMAP.md`;
  first ~2 weeks of IDEA-stage pipeline items + Plane work items; any portfolio-level consult
  memos filed in `ops/council/consults/`.
- `roadmap`/`replan`: `ops/calendar/ROADMAP.md` created/updated; Plane work items synced.
- `standup`: `item.yaml` `next_action`/`due` fields updated where needed; no dedicated file.
- `/plan` has no single pipeline.py stage transition of its own — it operates across items;
  any stage transitions it triggers belong to the skill that owns that item's next step.

## On failure
- Plane MCP unavailable in any mode: fall back to `ROADMAP.md`-only, queue a "Plane sync
  pending" note, never block content work (§9 explicit fallback).
- `bootstrap` finds a project already existing under a different identifier/state set: do not
  delete or recreate it — add only the missing states/labels and flag the discrepancy to the
  Showrunner for a human decision.
- `calendar.py` flags a cadence violation: resolve before finishing this run (trim, or justify
  in writing) — never silently exceed the band.
- `standup` finds a `BLOCKED-ON-SPARSH` item stale >3 days: escalate its priority in the
  consolidated ask; this also feeds the launch-surge health check in STRATEGY §7.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Campaign slate is a working session, not a reveal:** present the proposed slate as a
  week-by-week grid WITH the reasoning per line (which candidate, which bet it feeds, why
  this week) and the Brand Office's portfolio memos alongside. Sparsh reshapes lanes, cadence,
  and sequencing live; creative-director respins in-session. Nothing is marked SCHEDULED or
  created in the pipeline until his nod.
- **Roadmap is proposed, not imposed:** present the week-grid diff (what's new, moved, bumped,
  at risk) with the cadence choice inside STRATEGY §7 bands and the reasoning. Sparsh's
  priorities reshape it live; planner re-renders in-session.
- **Standup mode stays terse even interactively:** board + blocked + one proposed next action.
  Don't turn a 2-minute standup into a ceremony.
- **Bootstrap:** confirm with Sparsh before creating the Plane project/states/labels (one-time,
  externally visible setup).
- **Replan on an A1 trend:** present the insert-vs-bump tradeoff (which slot dies to make room)
  rather than silently reshuffling; in AUTONOMOUS mode make the swap and log it in ROADMAP.md.
