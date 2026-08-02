# Weekly Review — week ending YYYY-MM-DD

Produced by: analyst → planner → creative-director, via `/weekly-review` (Friday ritual,
`ops/RUNBOOK.md` §3). Saved as `ops/calendar/review-YYYY-WW.md`. This is the only session in
which `strategy/BETS.md` status and `strategy/STRATEGY.md` content may change, and only jointly
(Sparsh + Showrunner, `ops/ROLES.md` decision rights (d)/(f)).

## 1. Metrics summary block
`tools/metrics.py report --csv ops/calendar/posts.csv --followers N --json` output for the
week (CSV schema: date, platform, url, pillar, views, likes, comments, shares, saves, funnel,
followers_at_post — `tools/README.md`): per-post decomposition, account medians, efficiency,
funnel ratios.

```
<paste tools/metrics.py report output>
```

## 2. Per-pillar medians vs account median
STRATEGY §6.1 — growth accounting runs on medians per tier.

| Pillar | Median views | Median LR | Median efficiency (views/follower) | vs account median |
|---|---|---|---|---|
| HERO | | | | |
| WORKHORSE | | | | |
| FILLER | | | | |

**HERO drought check:** days since last HERO publish — flag if >7 (`tools/calendar.py`).

## 3. Bet-gate checks

| Bet | Gate (from BETS.md) | Current numbers | Verdict |
|---|---|---|---|
| BET-1 (editing lane) | median/follower ≥10% AND lane LR in 1–10% band AND ≥1 post >3x median by post 20 | | UNTESTED\|VALIDATING\|VALIDATED\|FAILED |
| BET-2 (Claude for creatives) | funnel comment:like ≥0.5 median (first 5) AND DM→email ≥20% | | UNTESTED\|VALIDATING\|VALIDATED\|FAILED |
| BET-3 (agentic editing spectacle) | after ≥8 HERO: HERO median ≥ WORKHORSE median AND HERO LR in band | | UNTESTED\|VALIDATING\|VALIDATED\|FAILED |
| BET-4 (long-form spectacle) | first 3 long-forms: retention ≥ platform-typical AND ≥1 breaks 5x Shorts median | | UNTESTED\|VALIDATING\|VALIDATED\|FAILED |
| LENS-1 (35+ calm-craft tone) | qualitative — comment sentiment once insights unlock; revisit at 1K followers | | UNTESTED\|VALIDATING\|VALIDATED\|FAILED |

Status changes recorded here AND in `strategy/BETS.md`'s `Status:` field, with the evidence
that justified the change.

## 4. Audience-mismatch triad check
STRATEGY §6.6, checked monthly — 2 of 3 triggers a strategy review session
(`ops/RUNBOOK.md` §8):

| Signal | Current reading | Triggered? |
|---|---|---|
| Efficiency sliding under ~5% | | yes/no |
| Hits coming only from off-pillar content | | yes/no |
| Flat non-pinned spread | | yes/no |

**Triad count this month:** _/3 — <action if ≥2>

## 5. Format kill/keep decisions
Creative-director's review of the ≤3 owned formats (STRATEGY §4) against this week's evidence.
Decisions happen ONLY here, never mid-week. Any kill or add gets a dated `[OWN-DATA]` line
appended to `knowledge/brand/content-architecture.md`'s format list.

| Format | Keep / Kill / Audition-promote | Rationale |
|---|---|---|

## 6. Wins / losses narrative
**Wins** (3 lines max):
-

**Losses** (3 lines max):
-

## 7. Next-week cadence choice
Chosen band (STRATEGY §7: steady-state 3–5 reels + ≤1 long-form/month, floor 2/week; or
time-boxed launch surge ≤30 days, ≤once/quarter) + why (pipeline health, Sparsh availability,
news windows, bet-validation needs).

**Chosen:** steady-state | launch-surge
**Why:**

## 8. Roadmap changes handed to planner
Concrete deltas to `ops/calendar/ROADMAP.md` for next week — new items, re-sequenced items,
items pulled/added per the format and bet decisions above.
