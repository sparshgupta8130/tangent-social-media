---
name: trend-sweep
description: Use daily-ish, or whenever it has been more than 24h since the last ops/calendar/trends-log.md entry — scans Adobe/Anthropic/AI-imaging/competitor sources for news and format ideas and rates each finding's urgency.
---

## Purpose
Keep the team's situational awareness current: Adobe/Anthropic news, trending audio/formats,
and named competitor moves, logged with an actionability rating so hot windows never get
missed and cold context never clutters ideation.

## Preconditions
- None strict. Best triggered per CLAUDE.md's session-start check (>24h since the last
  `trends-log.md` entry).
- Source list: Adobe newsroom/blog, Anthropic news, AI-imaging subreddits, r/ClaudeAI, and the
  seed competitor accounts documented in `research/00_seed_accounts.md` (Sebastien Jefferies,
  Nate Herk, Devin Huynh/"Eleven Percent") plus any others tracked in `research/creators/` or
  `research/ig_harvest/`.

## Protocol
1. Invoke `trend-scout` (Task, subagent_type `trend-scout`) with the source list above and the
   date of the last entry in `ops/calendar/trends-log.md` (so it sweeps forward from there,
   not from scratch every time).
2. Trend-scout checks each source via WebSearch/WebFetch for anything new since that date:
   Adobe/Anthropic product or policy news, a trending audio/format on IG/YT, or a notable post/
   pivot from a tracked competitor account.
3. For every finding, append a dated entry to `ops/calendar/trends-log.md`: date, source
   (with URL), the finding itself, and an actionability rating:
   - **A1** — drop-everything, 0-4 day window (matches STRATEGY's FILLER news-response rule).
     Immediately flag `planner` to insert a news-response item — don't wait for the next
     standup.
   - **A2** — fold into next `/ideate` session (context, not urgent).
   - **A3** — context only, no action; still logged for the pattern-library and future
     reference.
4. Any A1 finding: ping `planner` immediately in this same session (or, if none is running,
   note it as the first item for the next `/plan standup`) to run `/plan replan`. Per
   `ops/RUNBOOK.md` §5, planner reserves a news-response slot in the current week's roadmap as
   FILLER and bumps the lowest-priority FILLER/WORKHORSE item not yet past SCRIPTED to make
   room — never a HERO item, never anything already at G2 or later. If no bumpable slot exists,
   log the window as missed (with the reason) rather than force an insertion.
5. This skill does not touch pipeline items directly — its only output is the log entries and,
   for A1s, the planner flag.
6. Mid-session ad hoc sweeps are expected, not just the scheduled daily pass: if `trend-scout`
   surfaces a hot signal (a competitor post, an Adobe/Anthropic announcement) while working on
   something else, it logs the A1 immediately rather than waiting for the next scheduled sweep.

## Gates
- Every entry must carry a source URL + date + actionability rating. No rating without stated
  evidence — this extends QC_PROTOCOL's no-fabrication rule to trend logging.
- An A1 rating must justify the 0-4 day window explicitly (why this specific finding expires
  that fast) — an unjustified A1 gets downgraded to A2.

## Outputs
- `ops/calendar/trends-log.md` — append-only; existing entries are never edited or removed.
- A `planner` ping (in-session or queued) for any A1 finding.

## On failure
- A source is blocked (e.g., Instagram/TikTok logged-out walls — a known constraint per
  `research/QC_PROTOCOL.md`): log it as a DATA GAP in that entry and continue with the
  remaining sources; don't fabricate a finding to fill the gap.
- No new findings anywhere: still append one dated "swept, nothing new" entry so the >24h
  cadence check has ground truth to compare against.
- WebSearch/WebFetch errors on a given source: log which source failed and why, continue with
  the rest — a partial sweep with logged gaps is acceptable; a silent skip is not.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- Sweeps run without ceremony in both modes — don't narrate routine scans; log and summarize
  in one line ("swept, nothing above A3").
- **A1 findings interrupt the conversation immediately:** what happened, why it's ours (the
  mechanic, not just the event), the recommended news-response angle, and a go/no-go ask —
  window hours matter. The planner ping is still written either way (write-as-you-go).
- **A2 findings:** one-line mention now, full treatment at the next `/ideate` — don't derail
  the current stage for a non-perishable idea.
