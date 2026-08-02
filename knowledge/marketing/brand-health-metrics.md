# Brand Health Metrics — The Brand Office's Measurement Layer

**Owner:** shared (brand-director, growth-lead, audience-advocate all draw on this
file; the analyst pulls the raw numbers per its usual write-control role).
**Load context:** read at every G3 (`SYSTEM_DESIGN.md` §12.4) for scoring anchors; read by
the brand-director writing the weekly brand-health section (`SYSTEM_DESIGN.md` §12.6);
read before citing any brand-adjacent metric — if it isn't in this file or
`benchmarks.md`, it isn't cited as a number.

**Constitutional constraint:** every metric below is limited to what
`knowledge/platform/publishing-ops.md` and `tools/metrics.py` actually confirm as
collectable. Where a metric is uncertain, that uncertainty is stated plainly rather than
assumed away — per `SYSTEM_DESIGN.md` §12.5, a metric with no confirmed collection path is
**UNKNOWN**, not estimated.

## 1. Follower-quality proxies

- **Efficiency trend** — `median(views)/followers × 100` over time, not a single snapshot
  [REPO: `benchmarks.md` §1–2; `tools/metrics.py efficiency`]. Already the analyst's
  metric; the Brand Office reads its *trend direction* as a brand signal — declining efficiency
  alongside stable/growing followers is the handlytech pattern
  (`growth-playbook.md` follower-quality-over-count doctrine), flaggable at weekly review
  even before the early-warning triad (`benchmarks.md` §4) formally trips.
- **Non-follower reach %** — the follower/non-follower split of "accounts reached," a
  standard in-app Insights breakdown (unlocks past ~100 accounts reached) [VERIFIED-ONLINE:
  general Instagram Insights documentation, 2026-07-31 — the sub-breakdown isn't itemized
  in `publishing-ops.md`'s own field list, which confirms "reach" broadly [HIGH] but not
  this split; treat as [MED], in-app-pullable, pending an ops-brief confirmation]. Reading:
  >50% non-follower reach = the algorithm is pushing new-audience distribution (the
  penetration pattern `brand-science.md` §3 wants); <50% = mostly re-serving the base — not
  alarming pre-1K followers, since early growth is expected to lean on whatever reach exists.
- **Returning-viewer %** — **NOT collectable.** No confirmed IG field exposes this for
  Reels; `publishing-ops.md`'s YT field list has no "returning viewer" field either. Log
  `UNKNOWN — research gap: does YT Analytics segment retention support a
  new-vs-returning-viewer split` if this becomes decision-relevant; never substitute a
  proxy without flagging it as one.

## 2. Profile-visit rate and visit→follow conversion

Historically an in-app Professional Dashboard metric, still reported available in 2026
[VERIFIED-ONLINE: general Instagram Professional Dashboard documentation, 2026-07-31]. The
discrete `profile_views` Graph API field was deprecated at API v22 in favor of
`views`/`reach`/`follower_count`/`reposts` [VERIFIED-ONLINE:
developers.facebook.com/docs/instagram-platform/insights/, 2026-07-31]. **Status:**
manually pullable in-app; **not confirmed** as a scriptable API field. Visit→follow
conversion = follows ÷ profile visits over the same window — a manually-computed weekly
figure until `publishing-ops.md` confirms an API path. Full funnel-math (worked example)
lives in `growth-playbook.md`; this is the metric-definition entry only.

## 3. DM keyword → email conversion

**Collectable, confirmed:** ManyChat's dashboard logs keyword-trigger events (comment → DM
sent) [HIGH, `publishing-ops.md` §4]. Email signups track via whichever ESP is chosen
(outside `publishing-ops.md`'s current scope, pending an update once selected). Conversion
= email signups ÷ keyword-triggered DMs, over a window (BET-2's gate: "≥20% of deliverable
requests" [REPO: strategy/BETS.md BET-2]). The single highest-confidence number in this
file — both endpoints are first-party dashboards, not inferred IG metrics.

## 4. Comment-sentiment share — manual classification protocol

**Not automatable** — no sentiment tool is part of the stack; a manual read, applied
consistently at weekly review. Four buckets, every substantive comment gets exactly one:

1. **Craft-appreciation** — praises the visual/technical result ("the color grade is unreal").
2. **AI-curiosity** — genuine process questions ("how did the sliders move themselves?").
3. **AI-hostility** — disputes authorship/legitimacy ("this isn't real photography").
4. **Generic** — emoji-only, unrelated, or non-specific praise.

**Reading:** report each bucket's share of substantive (non-generic) comments, per post and
per week. Rising AI-hostility with stable AI-curiosity is a different signal (persona (d)
leakage, `audience/personas.md`) than rising AI-curiosity with stable hostility (persona (b)
engaging more) — read the *mix shift*, not absolute counts, since counts scale with reach.
Manual/small-batch by design; revisit tooling only once comment volume makes manual
classification impractical.

## 5. Saves + shares as brand-relevance signals

**Claim:** content offering practical value gets disproportionately saved/shared, and both
platforms treat saves/sends as stronger intent signals than likes — saving/sending costs the
viewer more. [REPO: research/03_virality_science.md §2.7]. Beyond the reach mechanics
`virality/laws.md` Law 6 already covers: a save/share is a Judgments/Feelings-tier signal on
Keller's CBBE pyramid (`brand-science.md` §5), not just a distribution mechanic. Track
saves/shares alongside likes/comments (`tools/metrics.py report` CSV schema already
ingests both) — strong saves relative to median with unremarkable likes is a
brand-relevance note worth flagging separately from the decompose quadrant
(`benchmarks.md`), which diagnoses craft/hook, not brand fit.

## 6. Branded-search & direct-mention proxies

Realistic scope for a small account — no true "branded search volume" tool exists here:

- **IG "Impressions from Search"** — an available Insights metric per current documentation
  [VERIFIED-ONLINE: general Instagram Insights documentation, 2026-07-31 — not itemized in
  `publishing-ops.md`'s confirmed field list; [MED] confidence, directional only].
- **Name-drops in comments** — the sentiment protocol above already surfaces this: any
  comment naming "Tangent," describing a prior post, or tagging a friend by reference — the
  most reliable *available* recall proxy pre-launch, requiring no extra tooling.
- **Not a substitute for** a true search-volume tool (Google Trends, social listening) —
  none is in the stack; log `UNKNOWN — research gap: no branded-search-volume tool in the
  current stack` rather than approximate from the proxies above.

## 7. G3 scorecard bands — what 1–10 means per lens

Anchored to observable facts and other marketing files' own checklists, never to an
unstructured impression.

| Band | Brand-Equity Impact (strategist) | Growth Contribution (scientist) | Audience Trust (advocate) |
|---|---|---|---|
| 9–10 | One-line test (`positioning-doctrine.md`) passes cleanly; every asset used appeared in fixed form; asset-usage checklist shows zero dilution | Maps clearly to an under-served entry point; fits an owned/audition format; funnel intact; no premature monetization pressure | Disclosure doctrine fully met; trust ledger clean; persona fit appropriate; no elevated crisis risk |
| 7–8 | One-line test passes; minor non-core asset paraphrase/inconsistency (ADVANCE-WITH-NOTES) | Maps to a real entry point; minor lean toward serving the base over reaching new viewers | Disclosure adequate; minor persona tone-fit risk noted, no ledger debit |
| 5–6 | Framing ambiguous/borderline, or one core asset diluted | Entry-point mapping unclear, or mostly base-serving where penetration should dominate | Disclosure present but perfunctory/buried, or unaddressed sentiment risk flagged |
| 3–4 | One-line test fails a load-bearing element, or a build rule broken (e.g. mocked "real UI") | A portfolio/monetization-sequencing rule violated (sponsor overriding format; premature monetization ask) | Disclosure gap, or a promise-keeping risk (funnel not live-tested pre-ship) |
| 1–2 | Positioning drift + a never-list-adjacent element — hard-HOLD | Bought-reach-adjacent behavior or funnel abuse — never-list territory | Never-list-adjacent trust violation, or unmitigated backlash adjacency — hard-HOLD |

Hard-HOLD triggers cross-reference `SYSTEM_DESIGN.md` §12.4 directly — a 1–2 score on any
lens should already correspond to one of that section's named hard-HOLD conditions.

## 8. Weekly brand-health section format (for `/weekly-review`)

Written by the brand-director, synthesizing the other two Brand Office members. Fixed
sections every week, even when the answer is "nothing to report":
1. **Drift check** — one-line test spot-sampled against the week's published items.
2. **Distinctive-asset consistency** — status changes in the register
   (`distinctive-assets.md`); dilution notes from the week's G3 checklists.
3. **Portfolio balance** — entry-point coverage (`positioning-doctrine.md`) and
   HERO/WORKHORSE/FILLER tier balance (`content-architecture.md`).
4. **ADVANCE-WITH-NOTES themes** — recurring notes not yet a HOLD but accumulating
   (`SYSTEM_DESIGN.md` §12.4).
5. **Metrics snapshot** — §§1–6 pulled for the week, each marked per-metric confidence
   ([HIGH]/[MED]/manual) — never one undifferentiated table.
6. **NOT-collectable reminder** — restate §9 by reference, so nothing uncollectable gets
   treated mid-week as if it exists.

## 9. Explicit "NOT collectable yet" list

So nobody invents a number under deadline pressure:
- Returning-viewer % (IG or YT) — no confirmed field.
- Automated sentiment scoring — manual 4-bucket protocol only (§4).
- A true retention curve/average-watch-time for Shorts via API — Studio UI manual pull only
  [REPO: publishing-ops.md §3].
- Branded-search *volume* (vs. the Impressions-from-Search proxy, §6) — no tool in stack.
- DM→email conversion, until an ESP is selected and confirmed in an ops-brief update.
- Profile-visit rate as a *scripted* pull — manual dashboard only, pending API confirmation (§2).
- Any "email subscriber worth $X followers" or similar monetary-equivalence claim —
  `[UNVERIFIED STAT]`, never cite as fact (`growth-playbook.md` owned-audience section).
