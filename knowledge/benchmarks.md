# Benchmarks — Metric Definitions, Bands, and Our Medians

> **WRITE CONTROL: analyst-owned.** This file is written ONLY by the analyst, ONLY through the
> `/postmortem` and `/weekly-review` skills. No other agent or session edits this file — not to
> settle an argument, not to pre-fill a hoped-for number. `SYSTEM_DESIGN.md` §4 rule 2 and
> `ops/RUNBOOK.md`'s calibration/quarterly-review protocols govern every change here.

## 1. Metric definitions (formulas match `tools/metrics.py` exactly)

- **Like-rate (LR)**: `LR = likes / views * 100`. Verdict vs. the organic sanity band:
  `IN-BAND` (1-10%), `BELOW-BAND` (<1%), `ABOVE-BAND` (>10%, treat as suspect — bought/boosted
  or a scraping error until second-sourced).
- **Efficiency**: `median(views) / followers * 100` across a batch of posts (`--csv` +
  `--followers`). The account-health metric — followers alone say nothing; efficiency says
  whether the account's own audience (and beyond) is actually watching.
- **Funnel ratio**: `comments / likes`, computed only over posts flagged `funnel=1` in
  `posts.csv` (carries the comment-keyword-DM mechanic). Measures whether the mechanic is
  actually driving comment volume, not just general engagement.
- **Decomposition quadrants** (`views × LR`, checked in this exact order against the batch's own
  median views/LR):
  1. `LR ≥ median_lr` AND `views < 0.5×median_views` → **HOOK/DISCOVERY FAILURE** (craft was
     fine, distribution/hook didn't earn reach).
  2. `LR < median_lr` AND `views < 0.5×median_views` → **CRAFT FAILURE** (got seen by few, and
     the few weren't compelled).
  3. `views ≥ 2×median_views` AND `LR < 1.0` → **BOOST-SUSPECT** (reach without resonance —
     investigate before crediting the format).
  4. `views ≥ median_views` AND `LR` in `[1,10]` → **HEALTHY**.
  5. else → **IN-BAND** (unremarkable, neither a hit nor a failure).
- **Spread**: `top_to_median_spread = top_views / median_views` across the batch — how lopsided
  the account's hits are relative to its typical post.

## 2. Healthy bands

| Metric | Band | Verdict |
|---|---|---|
| Like-rate | <1% | BELOW-BAND |
| | 1-10% | IN-BAND (organic-healthy) |
| | >10% | ABOVE-BAND (suspect) |
| Efficiency (views/followers) | <5% | WARNING |
| | 5-10% | OK |
| | 10-15% | HEALTHY |
| | 15-20% | GOOD |
| | ≥20% | EXCELLENT |
| Funnel ratio (comments/likes) | ≥0.5 | WORKING |
| | 0.2-0.5 | MIDDLING |
| | <0.2 | FAILING |

**Small-account context**: corpus outlier Devin Huynh's efficiency reached ~156% on his best
post [CORPUS: pattern-library, ig_elevenpercentprod — a funded 3-person team mid-product-launch].
This is an **existence proof that extreme efficiency is possible, not a benchmark to plan
against** — do not set targets or judge early posts against a 156% bar; the 10-20%+ bands above
are the real planning bands (`STRATEGY.md` §6.4).

## 3. OUR MEDIANS

*No data yet — first entry after post 5, per the analyst's `/postmortem` protocol. Do not
backfill or estimate; this table is a hard scaffold until real numbers exist.*

| Date | Window | Median views | Median LR | Efficiency | Spread | Funnel median |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## 4. Early-warning triad (audience-mismatch check, monthly)

Per `strategy/STRATEGY.md` §6.6 and computed by `tools/metrics.py report`:
1. `efficiency_sliding_under_5pct` — `efficiency_pct < 5`.
2. `hits_only_off_pillar` — at least one "hit" exists (`views ≥ 2×median_views`) AND none of the
   hits are `HERO`/`WORKHORSE` pillar.
3. `flat_non_pinned_spread` — `top_to_median_spread < 2.0`.

`strategy_review_triggered = true` when **2 of the 3** are true — the constitutional trigger for
the planner to open a strategy review (not a single flagged metric; correlated signal only).

## 5. Postmortem cadence rule

- **T+72h minimum** — no postmortem is written before 72 hours post-publish; early numbers are
  not yet stable and windfall spikes need time to settle (`STRATEGY.md` §6.1, "plan on medians,
  treat spikes as windfalls").
- **Restate at T+7d** for the weekly rollup — every postmortem's headline numbers get re-pulled
  and re-verified (via `tools/verify_stats.py`) at the one-week mark and folded into that week's
  `/weekly-review`, catching any late-arriving divergence between the T+72h snapshot and the
  settled number.
- Every number entering either the T+72h or T+7d write-up must have passed
  `tools/verify_stats.py` per the second-source rule — see `knowledge/platform/
  publishing-ops.md` §3 and `research/QC_PROTOCOL.md`.

## 6. Where these numbers feed decisions

These are not reporting-only metrics — `strategy/BETS.md`'s validation gates are written
directly in this file's vocabulary: BET-1's gate reads "efficiency ≥ 10% AND lane posts' median
LR in the healthy 1-10% band with ≥1 post breaking 3x account median"; BET-2's gate reads
"funnel posts reach comment:like ≥ 0.5 median across first 5." When the analyst runs
`tools/metrics.py report` for a weekly-review, the output feeds both this file's OUR MEDIANS
table **and** the live bet-gate check in `BETS.md` in the same pass — they are read from the same
underlying numbers, never recomputed separately or allowed to drift apart. If a single post's
decomposition verdict is `BOOST-SUSPECT`, exclude it from the median calculation until the
analyst confirms (or rules out) a boost, rather than letting one anomalous row skew the account
baseline every other post is judged against.
