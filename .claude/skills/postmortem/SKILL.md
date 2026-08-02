---
name: postmortem
description: Use at T+72h or later on a PUBLISHED pipeline item — collects and second-sources stats, decomposes performance, fills the 9-section postmortem, updates the knowledge bank, and closes the item.
---

## Purpose
Turn a published post into verified evidence: no single-sourced numbers, a
views×like-rate decomposition, a critic-calibration note, and durable `[OWN-DATA]` knowledge
updates.

## Preconditions
- Item stage == `PUBLISHED`.
- At least 72 hours elapsed since the recorded post time in `item.yaml`. If not, do not run —
  reschedule (see On failure).

## Protocol
1. Confirm stage PUBLISHED and elapsed time ≥72h (compare `item.yaml`'s publish timestamp to
   now). Then open the postmortem window explicitly — `POSTMORTEM` is its own stage in
   `tools/_common.py`'s `STAGE_SEQUENCE` (PUBLISHED → POSTMORTEM → CLOSED is forward-only, one
   step at a time; jumping straight to CLOSED is an illegal transition):
   `python tools/pipeline.py stage NNN POSTMORTEM --next-action "Analyst working postmortem" --next-action-owner analyst`
2. Collect raw stats (views, likes, comments, shares, saves, followers_at_post) from the live
   post.
3. Second-source every stat: `python tools/verify_stats.py <post-url>` — pulls independent
   metadata via yt-dlp and diffs against the claimed numbers, flagging >10% divergence. No
   number enters the postmortem on a single source (STRATEGY §6.2; QC_PROTOCOL's 15.5%
   browser-scrape error-rate finding is exactly why this step is non-optional).
4. If divergence >10%: use the yt-dlp (independently sourced) figure as authoritative and note
   both values plus the divergence in the postmortem.
5. Run the metrics suite against `knowledge/benchmarks.md`'s current medians:
   `python tools/metrics.py likerate --views N --likes N`
   `python tools/metrics.py decompose --views N --likes N --median-views N --median-lr X`
   `python tools/metrics.py funnel --comments N --likes N` (only if this was a funnel post).
6. Invoke `analyst` (Task, subagent_type `analyst`) with: the verified stats, the metrics
   outputs, the full item folder (`brief.md`, `script.md`, `critiques/G1-script.md`,
   `critiques/G2-cut.md`), `knowledge/benchmarks.md`, `strategy/BETS.md`.
7. Analyst fills `templates/postmortem.md` into `NNN-slug/postmortem.md` — the 9 numbered
   sections (0-8, adapted from `research/templates/video_postmortem_template.md` but applied
   to our own post): (0) Identity & stats, (1) Packaging (cover/first line as actually
   published), (2) Hook (0-3s, verbatim opening as shipped), (3) Structure & retention
   engineering (beat map/loop map as published vs script.md — note drift), (4) Value
   proposition, (5) Psychology scoring (STEPPS scan against `knowledge/virality/laws.md`), (6)
   CTA & funnel mechanics (`metrics.py funnel` result if applicable), (7) Repeatability verdict
   (extractable template, format keep/audition recommendation), (8) Why it won or lost
   (analyst synthesis, named delta vs recent flops/hits). A section that doesn't apply says
   why — never collapsed or skipped. Then fill the template's trailing required blocks: the
   Verified-stats table (claimed vs `verify_stats.py`, divergence, verdict), the Views×LR
   decomposition verdict, the Critic-calibration block, the Knowledge-bank update list, and the
   One-line lesson.
8. Analyst writes `[OWN-DATA]`-tagged entries into the relevant `knowledge/craft/*`,
   `knowledge/virality/*`, or `knowledge/platform/*` files (listed in the Knowledge-bank update
   list block), and refreshes `knowledge/benchmarks.md` medians/bands. The analyst is the only
   writer of these files outside `/weekly-review` (SYSTEM_DESIGN §4.2).
9. Critic-calibration block: compare the critic's G2 8-lens scores against the actual
   performance quadrant from step 5, lens by lens (right/wrong, by how much). If this reveals a
   systematic miss (not a one-off), name the specific proposed critic-prompt change in that
   block and flag it to the Showrunner for approval — the analyst does not edit
   `.claude/agents/critic.md` directly (§8 calibration loop: analyst proposes, Showrunner
   approves).
10. Advance stage: `python tools/pipeline.py stage NNN CLOSED --next-action "" --next-action-owner planner`.

## Gates
- 72h minimum elapsed — this is a hard precondition, not a suggestion; early data is noisy.
- The `PUBLISHED → POSTMORTEM → CLOSED` sequence is forward-only, one stage at a time — do not
  attempt to skip `POSTMORTEM`.
- Every stat second-sourced or explicitly flagged as a DATA GAP with a stated reason — never
  silently treated as verified.
- `benchmarks.md` and other knowledge-bank writes happen only through this step (or
  `/weekly-review`) — never ad hoc.

## Outputs
- `NNN-slug/postmortem.md` (all 9 sections filled).
- `knowledge/benchmarks.md` updated; `[OWN-DATA]` entries added to the relevant craft/virality/
  platform files.
- `pipeline.py stage NNN POSTMORTEM` (opens the window) then `pipeline.py stage NNN CLOSED`
  (closes it) are the two state transitions that end this skill.

## On failure
- <72h elapsed: do not run; set `next_action` = "run /postmortem", due = publish time + 72h,
  owner = analyst.
- `verify_stats.py` fails (post deleted/private, network error): log a DATA GAP per
  QC_PROTOCOL (state what was tried and what's missing); use the best single-sourced number
  with a LOW-confidence tag rather than blocking the whole postmortem — never silently upgrade
  it to verified.
- Divergence >10% and unresolved after retry: use the more conservative (lower) number, flag
  it for extra scrutiny, and say so in section 1.
- `knowledge/benchmarks.md` missing/empty: halt, report as a build gap — never invent medians
  from nothing to make the decompose math run.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Checkpoint — findings review (before knowledge-bank writes):** present the verified-stats
  table (claimed vs verify_stats), the views×LR decomposition verdict, the critic-calibration
  block (where the critic's G2 scores were wrong, shown not hidden), the draft one-line
  lesson, and the proposed [OWN-DATA] knowledge updates.
- **Iterate:** Sparsh sharpens the lesson or challenges the decomposition read; the analyst
  defends with numbers or concedes. Only then are [OWN-DATA] lines written to knowledge files
  and benchmarks.md refreshed.
- What is NOT negotiable in any mode: the numbers themselves (second-sourced or absent) and
  logging the postmortem at all — flops get autopsies especially when they're ours.
- AUTONOMOUS: write updates directly; surface surprises (decomposition ≠ expectation, critic
  badly miscalibrated) in the next standup.
