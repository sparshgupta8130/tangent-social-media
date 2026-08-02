# REVENUE — The Money Roadmap

**Owner:** revenue-lead. **Change control:** §2 thresholds and stream statuses change only
inside `/revenue-review`, only with Sparsh + Showrunner joint sign-off (same pattern as
`strategy/BETS.md` / ROLES.md decision right (d)); all money decisions — spend AND pricing —
are Sparsh's alone (ROLES.md (g)). Evidence spine: [MONEY] =
`research/briefs/revamp-2026-08/monetization_economics.md`; [SUBS] =
`research/briefs/revamp-2026-08/subscription_inventory.md`.

**Status: FIRST-PRODUCT BET — DECISION DEFERRED.** Sparsh will choose the first paid product
(preset/prompt pack vs. course vs. app) in a dedicated session. §2.3 presents the options
with evidence; nothing in this file presumes the choice.

---

## §1 The honest math (24-month scenarios, imported from [MONEY §6])

[MONEY §6]'s own caveat carries over verbatim in spirit: the model is a synthesized
arithmetic exercise from sourced inputs, not itself a cited study. Probabilities map the
scenarios onto the measured creator-income distribution ([MONEY §1]).

| Scenario | P(24mo) | Month-24 shape | Arithmetic | Total/yr |
|---|---|---|---|---|
| Conservative | ~50–60% | YT ~8K subs; IG+TT ~15K; list ~800; ~150K views/mo | Ads 1.8M views/yr ÷1000 × $5 RPM = $9,000 · sponsors 2–4 small deals ≈ $1,200 · products 800 list × $0.10–0.50/sub/mo ≈ $2,400 | **≈$12,600** |
| Base | ~10–15% | YT ~50K; IG+TT ~80K; list ~5,000; ~800K views/mo | Ads 9.6M ÷1000 × $6 = $57,600 · sponsors 8–12 × $1.5–3K ≈ $25,000 · products 5,000 × 4% × $79 × 1.5 launches ≈ $23,700 | **≈$106,000** |
| Bull | <2–3% | YT ~400K; IG+TT 500K+; list ~40K; ~6M views/mo | Ads 72M ÷1000 × $8 = $576,000 · sponsors 15–20 × $8–15K ≈ $180,000 · products 40,000 × 2.5% × $1,500 × 2 ≈ $300,000 | **≈$1,056,000** |

Planning rules that follow (V2 realism contract, SYSTEM_DESIGN_V2 §6):
1. **The conservative case is the statistically modal outcome for disciplined execution**, not
   a failure case [MONEY §6]. Every plan must survive it; no plan may assume the bull case.
2. Even in the bull case, ads are ~55% only because the product/sponsor layers lag audience —
   ads-only $1M needs 4–28M views/month, sustained [MONEY §3]. Products and sponsorships are
   what separate base from conservative, so they get the system's revenue effort.
3. What moves us up a scenario band is exactly what §2 sequences: disciplined email capture
   from day one, funnel conversion, and a product layer launched into accumulated trust
   [MONEY design-implications §1, §6].

## §2 Revenue-stream sequencing — activation thresholds

| # | Stream | Status | Activates when | Evidence | Owner |
|---|---|---|---|---|---|
| 1 | Email list | **ACTIVE (week-1 wiring)** | Item #1 — no threshold; capture wired before first post (`publishing-ops.md` §5) | [MONEY design-implications §1] | revenue-lead (P&L) · growth-lead (mechanics) · analyst (numbers) |
| 2 | Keyword-DM free deliverables (list builders) | ACTIVE with first funnel post | First funnel post live; governed by BET-2's gates | BETS.md BET-2; STRATEGY §5 | story-lead/producer (build) · revenue-lead (reads conversion as demand signal) |
| 3 | First paid product | **DEFERRED — Sparsh's dedicated-session choice** | BET-2 VALIDATED **and** BETS.md Deferred trigger met (10K followers or first inbound sponsor interest) **and** `growth-playbook.md`'s four monetization-readiness criteria pass | [MONEY §5]; BETS.md Deferred; growth-playbook | revenue-lead (brief/launch plan) · Sparsh (GO + price) |
| 4 | Sponsorships | DORMANT | Engaged audience crosses ~10K (bottom of the 10–50K activation band) → build media kit + rate card; deals only per fit criteria | [MONEY §2]; growth-playbook "Sponsorship economics" | revenue-lead (kit/rate card) · Sparsh (every deal) |
| 5 | Apps/SaaS (flagship) | HORIZON (6–12 mo) | An audience demonstrably exists (stream 1–2 metrics real) and a validated product thesis from stream 3's pipeline | [MONEY §5]; SYSTEM_DESIGN_V2 §6 | Sparsh (build, via Claude Code/Jules [SUBS]) · revenue-lead (offer/launch) |

**§2.1 Email (stream 1).** The only owned asset (STRATEGY §1). Measured value is humble —
median $4.40/subscriber-year [MONEY §5] — which is precisely why list SIZE must start
compounding now, not at 10K followers: at measured medians, meaningful product revenue needs
thousands of subscribers, and Gumroad's data puts 1–2 years of audience-building ahead of
$10K/month product outcomes [MONEY §5]. Concrete wiring: `publishing-ops.md` §5.

**§2.2 Keyword-DM deliverables (stream 2).** Free products with standalone value (prompt,
preset, process PDF), email-gated after delivery — deliver first, invite second (THE LINE,
`instagram.md` §2). Dual role: they build the list AND they are cheap demand probes — a
deliverable class with high request volume is audience evidence for a paid product in the
same class (§3 test 1). BET-2's kill/pivot discipline applies unchanged.

**§2.3 First paid product (stream 3) — the deferred decision, options with evidence:**
- **Preset/prompt pack.** Fastest to ship off existing craft; sits in Gumroad's $19–49
  pricing sweet spot; with an existing audience, first-$100 arrives in 60–90 days [MONEY §5].
  Ceiling honesty: the median such product earns $364 lifetime — viable only with the
  funnel/list as its distribution engine, not as a shelf item [MONEY §5].
- **Course.** The largest single line in the best-documented 7-figure mix (Ali Abdaal ~40% at
  $995–4,995 [MONEY §2]). But course economics ride on deep accumulated trust and a large
  warm list; launched early it's high effort into a tiny conversion base ([MONEY §5]: warm
  10–20% is unvalidated folklore; engaged-list 3–5% is a heuristic, not a promise).
- **App/SaaS.** Highest margins (85–95% [MONEY §2/§4]) and Sparsh's strongest skill — but
  every credible SaaS-from-content case had the audience BEFORE the product (Pieter Levels:
  350K followers pre-launch [MONEY §5]). Structurally the flagship (stream 5), not the first
  product.
- **UNKNOWN — research gap:** no evidence-backed email-list-size threshold for a first paid
  launch exists in [MONEY] or the knowledge bank; the activation test above is deliberately
  qualitative + BETS-gated. Calibrate with our own first-launch `[OWN-DATA]`.

**§2.4 Sponsorships (stream 4).** Activation band ~10–50K engaged followers, scaling with
niche CPM and audience quality, not raw size [MONEY §2]. Until crossed: no media kit, no rate
card, no outreach (premature kit = failure mode, `revenue-lead.md`). On crossing:
`growth-playbook.md`'s fit criteria bind (sponsor executes inside our owned formats; the
Varun Mayya 10–15x penalty and Harper Carroll #ClaudePartner counter-example; Anthropic/Adobe
as natural fits); BTS +3 mandatory `/consult`; every deal signed by Sparsh.

**§2.5 Apps/SaaS flagship (stream 5).** The 6–12-month horizon bet the realism contract names
as the highest-leverage asset in the portfolio (SYSTEM_DESIGN_V2 §6): software margins, owned
IP, and a production line (Claude Code + Jules [SUBS §Tooling matrix (f)]) that costs
subscription time, not cash. Enters the §3 pipeline like any product — no exemption from the
three tests because it's the glamorous option.

## §3 Product pipeline rules

**Opportunity brief** (`ops/revenue/YYYY-MM-<slug>.md`, one idea per brief): THE PRODUCT
(what/for whom/deliverable form) · AUDIENCE EVIDENCE · EFFORT VS. MARGIN · TRUST TEST ·
DISTRIBUTION PLAN · PRICING HYPOTHESIS (§4) · KILL GATE (pre-registered, numeric) ·
VERDICT (GO/PARK/KILL recommendation; GO is Sparsh's).

**The three validation tests — a product idea passes ALL THREE or it parks:**
1. **Audience-evidence test.** Named demand signal from OUR audience: deliverable-class
   request volume (stream 2 data), recurring comment/DM asks, or a validated bet the product
   extends. "People buy presets generally" is not evidence; our funnel data is [MONEY §5's
   distribution says generic products earn the median].
2. **Effort-vs-margin test.** Honest build-hours (whose hours — Sparsh's are the scarcest,
   V2 principle 1) against realistic revenue at MEDIAN conversion on OUR current list size —
   never at folklore rates. If the median outcome doesn't pay for the effort, the answer is
   park until the list is bigger, not inflate the conversion assumption.
3. **Trust test.** Zero debit to the trust ledger: real standalone value, THE LINE compliant,
   no persona betrayed (`community-trust.md`; `personas.md`), disclosure-consistent, and — if
   BET-5-adjacent — inside the PVC consult's Q3 boundaries (§6).

**Kill gates.** Pre-launch: failing any test = PARK (conditions named) or KILL. Post-launch:
every launch plan pre-registers a numeric kill gate (e.g. "<N sales by day 30 at the planned
distribution volume") and honors it on schedule — sunk-cost discipline identical to BET-3's
"do not run past 12 posts." A killed product's postmortem lands in `ops/revenue/`.

## §4 Pricing doctrine

1. **Anchor digital products in the evidenced $19–49 sweet spot** [MONEY §5, Gumroad
   146K-product dataset]; price above it only with a demonstrated-value case (a course with
   validated demand), below it only as a deliberate list-builder.
2. **India purchasing-power wrinkle** [MONEY §5]: India-targeted digital pricing runs
   ₹499–2,999 vs. $49–299 US-equivalent — 5–10x per-customer compression. Every brief names
   its audience geography: global-USD, India-first, or split (purchasing-power-parity tiers).
   The PVC lane is India-first by design (BET-5) AND trust-constrained (§6) — its economics
   are charity-pass-through-shaped, not margin-shaped.
3. **Plan revenue on measured medians** — $4.40/subscriber-year email revenue, median Gumroad
   outcomes — and treat "3–5% of engaged list buys" as a heuristic to test, never a promise
   to budget [MONEY §5]. First-launch `[OWN-DATA]` recalibrates this doctrine.
4. **Every price is Sparsh's sign-off** (ROLES.md (g)) — including "free" when a deliverable
   gates future paid positioning, and every discount/tier change after launch.

## §5 The metric set (currently-collectable only)

Weekly — collected by analyst, reported in `/weekly-review`; revenue-lead reads (contract (c)):
- **Email adds** (ESP dashboard count, week over week) and **list size** — the P&L's asset side.
- **DM-deliverable requests** (ManyChat trigger events) and **DM→email conversion %** —
  BET-2's own gate metric (≥20% bar).
- **Funnel comment:like** on funnel posts (`tools/metrics.py`, posts.csv `funnel` column;
  ≥0.5 working bar, STRATEGY §6.5).

Monthly — assembled at `/revenue-review` from the weekly rows: adds trend, conversion trend
vs. BET-2 gate, threshold-distance table (§2). **Later, activation-gated (not tracked now):**
revenue by stream, product units/refunds, sponsor inbound count, rate-card realization.
No revenue metrics are invented before a stream is live — a dormant stream reports "dormant,"
not zero-filled projections.

## §6 Standing constraints

1. **Trust before transaction** — `growth-playbook.md`'s four monetization-readiness criteria
   are binding gate conditions for stream 3+, checked at `/consult`/G3, not vibes.
2. **THE LINE is constitutional** (`instagram.md` §2; CLAUDE.md non-negotiable 6): real
   deliverables, specific and earned CTAs, deliver first — invite second, never hostage.
3. **PVC monetization rules** (`ops/council/consults/2026-08-01-pvc-ethics.md` Q3 — cited
   here as settled doctrine; this file never contradicts it): NO keyword-DM/funnel mechanics
   on tribute episodes; NO in-narrative sponsor integration; NO recipient-likeness products
   without family consultation + transparent charitable pass-through; trust-safe forms are
   verified-charity tie-ins and monetizing the pipeline/craft story (C8), never the tribute.
4. **Constitution carries over whole:** never buy reach; no fabricated numbers (every revenue
   stat second-sourced); disclosure-first; zero hallucination (SOURCES.md).
5. **Money decisions are Sparsh's** — spend and pricing, no proxy, no timeout-approve
   (ROLES.md (g)).
6. **The realism contract** (SYSTEM_DESIGN_V2 §6): no plan assumes the bull case; every plan
   survives the conservative case.
