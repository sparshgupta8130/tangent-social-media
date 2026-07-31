# FINAL SYNTHESIS AUDIT — Independent Adversarial Critic Pass

Auditor: independent critic agent, fresh context, no stake in the work under review. Default posture:
refute. Scope: `synthesis/01_VIRAL_MECHANICS.md`, `02_MEGA_VS_WANNABE.md`, `03_WHITE_SPACES.md`,
`04_TANGENT_STRATEGY.md` — checked against `research/critic/GATE_C_youtube_half.md`,
`GATE_C_instagram_half.md`, `GATE_C_REMEDIATION.md`, all 18 creator dossiers, `ig_harvest/00_INDEX.md`,
`research/04_whitespace_demographics.md`, `00-04` research files, `synthesis/00_INTERIM_convergences.md`,
and `QC_PROTOCOL.md`. Every finding below traces to a specific file/line I read, not a plausibility
read — quoted excerpts and re-derived arithmetic are shown inline.

---

## OVERALL VERDICT: **FIX-THEN-SHIP**

This is a well-built synthesis sitting on top of an unusually rigorous, twice-audited, once-remediated
corpus. It gets the hard part right almost everywhere I checked: the two headline retracted findings
(tiffintech "near-zero engagement," the sebastien "500x" TikTok gap) are correctly resolved, not
leaked; the corpus-wide error rate is correctly reported as 15.5% (not the critic-sample's biased 45%);
Curious Refuge's Adobe-hosted 561K short and Futurepedia's dormancy-causation claim are both kept out
of the final docs entirely. But I found **one confirmed retraction leak** (a stale, pre-correction
number that should not exist in a document titled "post-Gate-C"), **one mislabeled corrected number**
(a corrected figure carried forward under the wrong metric name), and — the more consequential
category — **several unhedged logical leaps in `04_TANGENT_STRATEGY.md`** that lean on a single,
structurally unusual data point (Devin Huynh / elevenpercentprod) harder than the evidence supports,
and **one materially omitted finding** (Skill Leap's AI-topic reach ceiling) that the source dossier
itself flags as "the most important finding for Tangent's own strategy" and that never appears
anywhere in the synthesis, despite Tangent's content being squarely AI-topic. None of this requires
new research — it's all fixable with targeted edits — but none of it should reach the owner unfixed
given his explicit "will be audited by the owner" standard.

**Per-doc verdicts:**
- `01_VIRAL_MECHANICS.md` — **MATERIAL** (one confirmed retraction leak + one misapplied/incomplete
  citation)
- `02_MEGA_VS_WANNABE.md` — **MINOR-MATERIAL** (one mislabeled metric)
- `03_WHITE_SPACES.md` — **MINOR-MATERIAL** (one untraceable number, one confidence-bundling
  overstatement, one over-precise rounding)
- `04_TANGENT_STRATEGY.md` — **MATERIAL** (four compounding logic/omission issues that bear directly
  on the action plan, not just the data layer)

---

## 1. RETRACTION LEAK CHECK (highest priority)

### FINDING 1 — MAJOR — CONFIRMED RETRACTION LEAK
**Location:** `synthesis/01_VIRAL_MECHANICS.md`, Law 0.1, lines 12–13:
> "self-funded undisclosed (kallaway 35-74M spikes @ 0.0009-0.008%)"

**Evidence this is the retracted number, not the corrected one:**
`research/ig_harvest/kallaway.md` line 87 (its own GATE C CORRECTION table):
```
| DVhB8rMjp1m | ~~678~~ | 64,910 | 95.74x | 0.0009% | 0.088% |
| DXSDF9djpRD | ~~476~~ | 4,223  | 8.87x  | 0.0012%| 0.0107% |
| DY7GAsGuwGr | ~~2,850~~ | 5,188| 1.82x  | 0.008% | 0.0145% |
```
`0.0009-0.008%` is explicitly the struck-through, **pre-correction** column ("old like-rate"). The
Gate-C-corrected range is **0.0107%–0.088%**, and `ig_harvest/00_INDEX.md` line 76 states this
explicitly: "~~near-zero like-rate signature (0.0009%-0.008%)~~ **GATE C CORRECTION... Corrected
like-rates are 0.0107%-0.088%**." `GATE_C_REMEDIATION.md` §3(d) further instructs: "The '~15-400x below
organic' language the critic recommended is accurate and should be adopted verbatim in place of the
original '100-1000x.'"

01_VIRAL_MECHANICS.md cites the **struck-through, retracted figure** with no multiplier-based
alternative nearby to soften it — unlike its own correct handling of tiffintech (1.55%, corrected) and
networkchuck (0.070%/0.53%, corrected) two lines above and below it in the same Law 0.1 paragraph. This
is the exact failure mode the audit brief flagged as highest priority: a document explicitly subtitled
"Final Synthesis (post-Gate-C)" carrying forward a number the corpus itself struck through.

**Root cause:** the number appears verbatim in `synthesis/00_INTERIM_convergences.md` line 11
("kallaway (self-funded, 0.0009-0.008%, 15-400x below own baseline)") — itself an internally
inconsistent line, pairing the corrected *multiplier* language ("15-400x below own baseline," which IS
the corrected framing) with the *uncorrected* raw percentage. 01_VIRAL_MECHANICS appears to have copied
the raw percentage from this interim note without re-deriving it against the later remediation, even
though it evidently did re-derive tiffintech and networkchuck correctly elsewhere in the same law.

**Required fix:** replace `0.0009-0.008%` with `0.0107-0.088%`, or (preferred, matching the account's
own dossier convention) drop the raw percentage and use the remediation-endorsed "~15-400x below
organic norm" language, consistent with how kallaway is already described in `00_INDEX.md`.

### No other confirmed leaks of the five flagged retractions
I specifically greped and read context for all five items named in the brief across all four synthesis
docs plus `00_INTERIM`:
- **tiffintech Lenovo "near-zero engagement":** correctly resolved. `01_VIRAL_MECHANICS.md` line 14
  pairs the corrected 1.55% like-rate ("real engagement") with the still-valid 5,900x *view-count*
  cross-platform gap ("bought distribution") — a genuinely well-constructed, self-consistent resolution
  that separates the two claims the pre-correction dossier had conflated. `00_INTERIM` line 13-14
  explicitly states "RETRACTED: tiffintech Lenovo/FIFA as 'near-zero engagement.'" Not leaked anywhere
  in 01-04.
- **sebastien TikTok "500x":** correctly resolved to "61x (corrected)" in 01 item 10 — see Finding 3
  below for a related but distinct mislabeling issue (the 61x/182x figures get their *metric types*
  conflated, but the *magnitude* itself is never the old retracted 500x).
- **kallaway magnitudes (15-400x):** the multiplier language is used correctly everywhere it appears
  (`00_INTERIM`, and implicitly nowhere else in 01-04) — only the raw percentage in Finding 1 leaked.
- **networkchuck post-2 weakened framing:** correctly carried as "post #2 milder at 0.53%" in
  `00_INTERIM` and folded into 01's Law 0.1 correctly (0.070%/54-66x for post 1; the milder post 2 is
  referenced in `00_INTERIM` only, not restated with a number in 01-04, which is a safe omission, not a
  leak).
- **Futurepedia dormancy causation:** never stated as causal anywhere in 01-04. Confirmed absent by
  grep (`Futurepedia` appears in 01/00_INTERIM only for the Grammarly boost case and the "dormant
  shorts lanes" descriptive note, never for the acquisition-timing causal claim).
- **Curious Refuge 561K Adobe-hosted short:** the "561K" figure does not appear anywhere in 01-04
  (confirmed by grep). Only `00_INTERIM` references it, correctly caveated ("hosted on Adobe's channel,
  not CR's — attribute accordingly if cited"). Clean.

---

## 2. CITATION FIDELITY

I traced more than 25 load-bearing quantitative claims across the four documents to their source
dossiers/files. The large majority check out exactly (verified: Berman 85x/85.5x OpenClaw gap;
Curious Refuge 228x long-form/Short gap; handlytech 93-1,350x distribution collapse; sabrina 176x
spread; Devin's >1,000x IG-over-YT gap and 156% ratio; Harper's 2K→200K/3-week figure, correctly tagged
"press-verified" matching the source's own `[REPORTED, MED-HIGH, The Ankler]` tag; O'Reilly-collab
underperformance; Sisinty's 99%-AI claim; Berman's "staffed" claim; Riley/Vibecode's tripled-revenue-
in-2-months and $9M/10K-paying-users figures; the WS demographic figures — 35.4%/51.9%/52% YouTube 35+
share, Pew's 24%/23% gender-parity + 16/−10 sentiment gap, Cara's 40K→650K, SDCC/FanX bans, the July
2026 Meta Muse Image retreat — all confirmed against `04_whitespace_demographics.md`). Three issues
did not check out:

### FINDING 2 — MAJOR — mislabeled corrected metric (sebastien TikTok gap)
**Location:** `synthesis/02_MEGA_VS_WANNABE.md` line 22:
> "sebastien's TikTok twin: 558K followers, 61-182x fewer views — an audience that size, worth nothing
> un-natively."

Also, more mildly, `01_VIRAL_MECHANICS.md` line 96: "sebastien's IG beats his 558K-follower TikTok 61x
(corrected) to 182x per matched pair."

**Problem:** "61x" and "182x" are not the same kind of measurement, and 02's phrasing states both are a
"views" gap, which is true for only one of them.
- **182x** is a genuine view-count ratio, from `creators/ig_sebastien.md` line 464: "Cross-platform
  view gap: ~182x (950K IG vs. 5,229 TikTok)" — for **Video 4** (`DW_VCbrDPWM`).
- **61x** is a corrected **like-rate** (engagement-rate) ratio, from `ig_sebastien.md`'s own GATE C
  CORRECTION section, line 1025-1026: "'TikTok twin's like-rate is 9.8% — over 500x higher on a
  per-view basis' — DIES: using the corrected IG rate (0.161%), the true gap is **~61x**" — for
  **Video 1** (`DaAlMicsiBD`), a completely different video, and an engagement-rate comparison, not a
  raw view-count comparison.

02's "61-182x fewer views" asserts both numbers measure views; 61x never measured views at all — it
measured like-rate. This isn't a magnitude error (the number 61x is the *correct*, Gate-C-corrected
value) but a unit/metric error: carrying forward a corrected number under the wrong description.
01's phrasing ("per matched pair") is slightly better hedged but still doesn't disambiguate that the
two figures are different metric types from different videos.

**Required fix:** disambiguate explicitly, e.g. "sebastien's TikTok twin: 558K followers, but a
61x-worse engagement rate on one matched clip and up to a 182x raw-view gap on another — an audience
that size converts to functionally nothing un-natively."

### FINDING 3 — MINOR — untraceable derived statistic
**Location:** `synthesis/03_WHITE_SPACES.md` line 19-20 (WS-2):
> "r/ClaudeAI 250K→1M in 13 months (verified, accelerating **+37%/90d**)"

I grepped the entire `research/` corpus for "37%" in any Claude/subreddit context — it does not appear
anywhere. The only sourced growth-rate figure for r/ClaudeAI, in `research/04_whitespace_demographics.md`
line 115, is "**+9.5%/~2,750 new members per day** in the most recent 30-day window." Compounding that
over 90 days gives ≈31%, not 37% — close but not a match, and nowhere is "37%" itself derived or
sourced. Per `QC_PROTOCOL.md` rule 1 ("a stat without a source is deleted, not kept"), this specific
figure should not appear with this precision. The underlying claim (r/ClaudeAI's growth is real,
large, and accelerating) is true and well-sourced by the 250K→500K→1M trajectory itself — only the
"+37%/90d" gloss is unsupported.

**Required fix:** either cite the sourced rate ("+9.5%/30d, the fastest of any AI-brand subreddit
checked") or drop the specific rate and keep "quadrupled in 13 months" (which `04_whitespace_demographics.md`'s
own bottom line, line 184, uses).

### FINDING 4 — MINOR — confidence-tier bundling overstates the weakest component
**Location:** `synthesis/03_WHITE_SPACES.md` line 13 (WS-1):
> "Demand: tens of millions of hashtagged posts, r/photography ~5.5M members, sustained search interest
> in AI photo editing [MED-HIGH]."

Source (`04_whitespace_demographics.md` line 91): r/photography's 5.5M figure is tagged **[MED]**; the
"tens of millions of hashtagged posts" figure (#lightroom 28.83M, #photoshop 44.91M) is explicitly
tagged **[LOW, hashtag-scraper aggregator, methodology undisclosed]** — the source file's own text
warns "shouldn't be treated as precise." Rolling both into a single "[MED-HIGH]" tag overstates the
confidence of the weaker, LOW-tagged half of the evidence bundle. Doesn't change the ranked verdict
(WS-1 is still the top-tier white space on the MED-tier subreddit evidence alone) but is a QC_PROTOCOL
evidence-tier discipline slip.

### FINDING 5 — MINOR — over-precise rounding
**Location:** `synthesis/03_WHITE_SPACES.md` line 27-28 (WS-3): "Riley 16x median."

Source (`creators/yt_rileybrown.md` line 1524): "these are the videos that reach the **3x-16x-median**
outlier tier" — describing five different videos (Videos 1-5), not one fixed ratio. Citing only the top
of the range as if it's a single number overstates precision. Low practical impact.

---

## 3. LOGIC AUDIT (04_TANGENT_STRATEGY.md's reasoning chain)

This is where the audit brief's stress-tests land hardest, and where I found the most consequential
issues — not data errors, but unhedged leaps from evidence to recommendation.

### FINDING 6 — MAJOR — the ">20% while small" target and "proves small accounts can exceed 100%"
claim rest on n=1, with undisclosed disanalogies

**Location:** `synthesis/04_TANGENT_STRATEGY.md` §5, line 79: "target: hold >20% while small — Devin
proves small accounts can exceed 100%." Also `03_WHITE_SPACES.md` WS-1 (line 13-14: "Devin Huynh...
proving the demand reaches non-followers hard") and WS-3 (line 28: "Devin 156% efficiency").

**The cherry-pick, quantified:** `ig_harvest/00_INDEX.md`'s full 22-account efficiency ranking (lines
44-65) shows elevenpercentprod (85K followers, 156%) is the **only account under ~300K followers in the
entire ranked corpus**. Every other account that clears 20% efficiency — realrileybrown (328K, 54.1%),
kallaway (442K, 40%, itself caveated "extreme-variance"), tiffintech (793K, 35.5%), nick_saraev (568K,
23.3%), vaibhavsisinty (2M, 23.3%), thevarunmayya (1M, 20.6%) — is medium-to-large, not small. There is
no second small account in the study to corroborate that smallness itself drives high efficiency; n=1.

**What the source dossier itself says drives the 156%:** `creators/ig_elevenpercentprod.md`'s own
"Reach decomposition verdict" (line 1070) attributes it to "**a stacked, engineered system**" — a fixed
24s template, a comments-exceed-likes CTA funnel, "genuine topic white space (no other account in the
24-account corpus runs a comparable... demo format)," and timing that "lines up precisely with
AutoEdit's real beta/launch milestones." Nothing in that decomposition names account size as a causal
factor.

**The undisclosed disanalogy:** the same dossier's "Surprises" section (line 1112-1113) states: "**The
account is not a solo creator — AutoEdit has a 3-person maker team** (Product Hunt credits),
complicating any narrative of this as a single person's organic hustle." This fact appears nowhere in
03 or 04. Devin's account is also, per WS-1's own text, a **video**-editing tool (not photo editing —
"the one big 'editing' adjacent account (elevenpercent) is video-editing, not photography"), and is
backed by a funded product mid-launch, not a hobbyist pipeline.

The same n=1 data point is used as load-bearing evidence for three separate claims across three
documents (WS-1's demand proof, WS-3's demand proxy, 04 §5's KPI target) without ever disclosing that
it is a team-backed, differently-scoped, product-launch-timed outlier — the single clearest
survivorship-bias compounding pattern in the synthesis.

**Required fix:** disclose the 3-person-team and video-vs-photo-editing caveats wherever Devin's ratio
is cited as generalizable evidence; reframe the ">20% while small" line as an aspirational best case,
not a benchmarked norm (most of the corpus's non-mega accounts sit well under 20%).

### FINDING 7 — MAJOR — "the proven reach grammar" drops the source's own "bet, not demonstrated" hedge
**Location:** `synthesis/04_TANGENT_STRATEGY.md` §1, lines 15-16: "Why this wins per the evidence: (a)
it IS demo-in-motion, **the proven reach grammar** (01 §1.5)."

This states as settled fact that demo-in-motion will work for Tangent's actual content (an AI agent
editing *art*), when the two research documents that actually studied this specific transfer question
both explicitly refuse to make that claim:
- `research/04_whitespace_demographics.md` §3(c), on "watch an AI agent create art": "zero existing
  supply is consistent with *both* 'untapped white space' and 'tried informally, didn't stick'...
  **This is a bet, not a demonstrated opportunity** — flagged explicitly rather than inflated."
- `synthesis/00_INTERIM_convergences.md` §C, the orchestrator's own open-questions log: "Does the
  demo-in-motion formula transfer to ART content, or does art follow the Curious Refuge
  entertainment-craft path instead? **(Tangent hinges on this.)**"
- `03_WHITE_SPACES.md` WS-3 itself is more careful — it labels this "**Demand proxy**" and flags a
  backlash risk — but even WS-3's own verdict language ("the differentiation play") doesn't carry the
  "bet, not demonstrated" caveat forward, and 04 drops the hedge entirely.

01 §1.5 ("demo-in-motion grammar for 'watch AI work' content") is itself accurately evidenced — for
*tool/app/automation* demos (Riley, Devin, Herk). The leap 04 makes is applying "proven" to a
genre (art) none of that evidence covers, exactly the transfer the corpus's own demand-research
explicitly refuses to call proven. This sits under the foundational bet of the entire plan — the HERO
content pillar and the positioning statement itself — so the overclaim is not cosmetic.

**Required fix:** reframe 04 §1(a) as "the best-evidenced bet available, unproven specifically for art
content per the corpus's own demand research" rather than "the proven reach grammar."

### FINDING 8 — MAJOR — genre-lane inversion tension not reconciled
**Location:** `04_TANGENT_STRATEGY.md` §1-2 (HERO = 2/week short-form reels) vs. `01_VIRAL_MECHANICS.md`
item 10 and `03_WHITE_SPACES.md` WS-4, both citing the same corpus finding: "Genre-lane inversion:
tool-demo content wins in shorts/reels; **art-spectacle wins LONG-FORM** (Curious Refuge: top long-form
228x their top Short; even their MEDIAN long-form beat their best Short)."

Tangent's actual deliverable is fine-art photography — art-spectacle by the corpus's own taxonomy —
yet 04 assigns the bulk of cadence and resourcing (HERO, 2/week) to short-form reels, treating the
*editing process* as tool-demo content (favoring short-form) rather than classifying the *output*
(finished gallery art) under the corpus's own art-spectacle rule (favoring long-form). The plan does
include a monthly long-form flagship citing this exact rule (§2, "LONG-FORM FLAGSHIP"), which is the
right instinct, but 04 never explicitly states which genre classification the HERO reels fall under or
defends why the process should inherit the tool-demo lane rather than the art-spectacle one its subject
matter would suggest. This is a defensible bet, not an error, but it's presented without acknowledging
the tension against the corpus's own stated rule — the kind of smuggled leap the audit brief asks to be
surfaced.

**Required fix:** add one sentence in §1 or §2 explicitly naming this as a bet ("we are treating the
agentic *process* as tool-demo grammar even though the *output* is art-spectacle, because—") rather
than leaving the classification implicit.

### FINDING 9 — MAJOR — cadence math is internally inconsistent
**Location:** `04_TANGENT_STRATEGY.md` §2, §4, §5.

§2 lays out: HERO 2/week + WORKHORSE A ("daily for launch month") + WORKHORSE B 1/week + FILLER 1/week.
§4's own Week 1-2 launch plan ("3 HERO reels + Day 1-14 of the series") works out to 3 + 14 = 17 posts
in 2 weeks ≈ **8.5 posts/week**. §5 then states: "Cadence total: **~4 reels** + 1 long-form/month-scaled
— the honest solo+agents ops model (02 §7)." Read literally this contradicts the ~16/week (or
higher, during the daily-series launch month) implied two sections earlier by roughly 2-4x, and the
"~4 reels" figure never states whether it's weekly or monthly, nor whether it includes the daily-series
stream at all.

More importantly, the evidence 04 cites as the basis for this cadence — `02_MEGA_VS_WANNABE.md` §7's
"honest solo pattern (Riley): ~4-5 crafted + 2 trend posts/week" (≈6-7/week) — is itself **lower** than
the ~8.5/week the launch-month plan actually produces, and 02 §7 separately warns: "Solo creators who
copy staffed cadences produce filler-tier quality at hero-tier frequency and burn out" — precisely the
risk the launch-month burst doesn't address or even acknowledge as a tradeoff.

**Required fix:** state explicitly whether "~4 reels" is weekly or monthly and whether it includes the
daily series; reconcile the launch-month volume against the "honest solo" (6-7/week) benchmark it cites
as its own justification, or explicitly note the daily series is a bounded, one-time exception to that
principle and why it's safe.

### FINDING 10 — MAJOR — the "AI-topic reach ceiling" (Skill Leap) is entirely absent, not merely buried
**Location:** should appear somewhere in `03_WHITE_SPACES.md` or `04_TANGENT_STRATEGY.md`; does not
appear in either, nor in `01_VIRAL_MECHANICS.md`, nor in `00_INTERIM_convergences.md` (confirmed by
grep across all four synthesis docs plus the interim file for "reach ceiling," "topic-affinity,"
"Howfinity").

**What the source dossier actually found:** `creators/yt_skillleap.md` §C (lines 577-589) is explicit
that this is "**the dossier's most important finding for Tangent's own strategy**" (line 585):
AI-topic Shorts on this channel get **equal-or-better engagement rates** than the channel's two
off-topic outlier hits (Video 7: 4.01% like-rate vs. the #1 hit's 3.32%, at only 14,309 views vs. 1.03M)
— but are structurally **capped on reach**, not resonance, because of smaller cold-audience
topic-affinity pools. The dossier's explicit "Bottom line for Tangent" (line 589): "the ceiling is real
and structural... it's a reach ceiling," and names two specific, transferable mitigations (device/
context-hybrid framing; ruthlessly universal, non-conditional hook phrasing).

**What synthesis actually cites from this dossier instead:** 01 item 2 (line 43) uses the *same*
dossier's off-topic iPhone-trick outlier as evidence for a *different* point — "a universal frame
wrapped around a niche topic — Skill Leap's iPhone-frame nearly 3x'd their pure-AI median" — without
ever surfacing the dossier's own more important, Tangent-specific warning that pure-AI content faces a
structural audience-size ceiling regardless of content quality. (The iPhone-frame data point is itself
also a partial mischaracterization: the dossier attributes most of that outlier's edge to 4.5 years of
algorithmic compounding from a 2021 post under a since-abandoned legacy identity, not simply "universal
framing" — see `yt_skillleap.md` lines 579-587 — and explicitly tags manufacturing that content as
"structurally irrelevant" / "off-mission" for Tangent, line 98.)

This matters directly: Tangent's entire content plan (per 04) is AI-topic content — an AI agent editing
photos. This is exactly the content class the source's own analysis says faces a structural reach
ceiling on audience-size grounds, independent of craft quality. The synthesis should have surfaced this
as a named risk and adopted the dossier's own two actionable mitigations; instead it is not mentioned
anywhere, which is the omission-audit item the brief specifically asked about, confirmed absent rather
than merely under-weighted.

**Required fix:** add a risk/mitigation note to `04_TANGENT_STRATEGY.md` (likely §6, Risks & standing
rules) naming the AI-topic reach ceiling and its two dossier-endorsed mitigations (device/context-hybrid
framing where relevant; ruthlessly universal, non-conditional hook phrasing on every HERO reel).

---

## 4. OMISSION AUDIT — what IS handled well

To be fair to the synthesis, three of the four omission risks the brief flagged are handled honestly:
- **Luck/survivorship caveats:** `02_MEGA_VS_WANNABE.md` item 9 ("Honest residual: luck and survivorship
  are real... every mega-creator we studied is by construction a survivor... the wannabe error is
  planning on the outlier instead of the median") is present, load-bearing, and closes the document —
  not buried. Good.
- **Front-loaded-not-compounding series finding:** `01_VIRAL_MECHANICS.md` item 7 states it plainly:
  "episode views FRONT-LOAD and decline; the series' power is commitment-signaling... not view
  compounding (ig_harpercarrollai §C, honest complication)." Present and load-bearing, not suppressed.
  One MINOR precision gap: the decline-shape evidence is drawn from YouTube per-episode data
  (`ig_harpercarrollai.md` §C4), while the "2K→200K" growth event being explained happened on
  Instagram/TikTok; the dossier itself logs this as an explicit DATA GAP ("It is not established
  whether the Instagram version showed the same declining shape"), which 01 doesn't carry forward. Does
  not change the downstream recommendation (series-as-follow-conversion-wrapper, not
  compounding-engine) either way, so this is genuinely low-stakes — noted for completeness, not a
  required fix.
- **Kallaway "serial mega-viral producer" retraction:** correctly kept out of 01-04 entirely; kallaway
  is never cited as a "winner" exemplar anywhere in `02_MEGA_VS_WANNABE.md`'s winners list. Clean.
- **AI-topic reach ceiling:** the fourth flagged item — see Finding 10 above. Not handled; fully absent.

---

## 5. INTERNAL CONSISTENCY ACROSS THE FOUR DOCS

Cross-checked recurring figures for drift between documents: 156% (elevenpercentprod), 85x/85.5x
(Berman), 176x (sabrina), 228x (Curious Refuge), 93-1,350x (handlytech), 15.5%/110-reel corpus error
rate, 5,900x/1.55% (tiffintech), 0.070%/0.53% (networkchuck) — all consistent everywhere they recur, no
drift found. The two inconsistencies present are the ones already itemized above (Finding 1's leaked
kallaway percentage appearing only in 01, and Finding 2's sebastien metric-type conflation appearing in
both 01 and 02 with slightly different, both-imprecise phrasing) — not additional new drift, the same
root issues surfacing more than once.

---

## SHIP CHECKLIST — fixes required before this reaches the owner

1. **01_VIRAL_MECHANICS.md, Law 0.1:** replace kallaway's `0.0009-0.008%` with the corrected
   `0.0107-0.088%` (or the "~15-400x below organic" phrasing already validated elsewhere in the
   corpus). [Finding 1, MAJOR]
2. **01 + 02:** disambiguate sebastien's "61x" (a corrected like-rate ratio, Video 1) from "182x" (a
   raw view-count ratio, Video 4) — do not present both as "fewer views." [Finding 2, MAJOR]
3. **04_TANGENT_STRATEGY.md §5 and §1, 03_WHITE_SPACES.md WS-1/WS-3:** disclose that Devin
   Huynh/elevenpercentprod (the sole basis for the ">20% while small" target and a load-bearing citation
   in two white-space arguments) is a 3-person funded team on a video-editing product mid-launch, not a
   comparable solo/small case — and soften the ">20%" line to aspirational, not benchmarked. [Finding 6,
   MAJOR]
4. **04_TANGENT_STRATEGY.md §1:** replace "it IS demo-in-motion, the proven reach grammar" with
   language that carries forward the source research's own "bet, not demonstrated opportunity" /
   "Tangent hinges on this" hedge for the art-content transfer question specifically. [Finding 7, MAJOR]
5. **04_TANGENT_STRATEGY.md §1-2:** add one sentence acknowledging the genre-lane-inversion tension
   (art-spectacle-wants-long-form vs. the short-form HERO allocation) as a named bet. [Finding 8, MAJOR]
6. **04_TANGENT_STRATEGY.md §5:** fix the "Cadence total: ~4 reels" line — specify weekly vs. monthly,
   include or explicitly exclude the daily launch-month series, and reconcile against the "honest solo"
   6-7/week benchmark it cites as its own justification. [Finding 9, MAJOR]
7. **04_TANGENT_STRATEGY.md §6:** add the AI-topic reach-ceiling risk (Skill Leap) and its two named
   mitigations (device/context-hybrid framing; ruthlessly universal, non-conditional hooks) — currently
   absent despite being the source dossier's own flagged "most important finding for Tangent." [Finding
   10, MAJOR]
8. Minor cleanup (not blocking, but should be swept in the same pass): soften 03's "[MED-HIGH]" WS-1
   demand tag to reflect the LOW-confidence hashtag-count component [Finding 4]; either source or drop
   "+37%/90d" for r/ClaudeAI [Finding 3]; note "Riley 16x median" is the top of a 3x-16x range, not a
   flat ratio [Finding 5].

None of these require new research or re-opening the corpus — every fix is a rewording, a caveat, or a
number swap against data that already exists in the dossiers. Once applied, I'd expect this synthesis
to clear a re-audit clean.
