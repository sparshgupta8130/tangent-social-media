# GATE C — Independent Critic Audit: Instagram Corpus Half

Auditor: independent critic agent, fresh context, no stake in the work under review. Posture: default
to refute. Audit date: 2026-07-25 (same day as harvest/dossier production — re-verification pulls
below are same-day, logged-out).

**Headline result up front:** the single most important finding in this audit is a **systemic,
previously-only-partially-diagnosed defect in the browser-based ("logged-in-session") like-count
harvesting method** used throughout this corpus. It is not fabrication in the sense of invented
numbers — every number is faithfully sourced from a real tool pull — but a meaningful fraction of
those pulls are **simply wrong**, by anywhere from a few percent to **453x**, and the errors
concentrate disproportionately on exactly the reels the corpus flagged as "ad-boosted" or
"anomalous," which is precisely where the corpus's most load-bearing cross-account claims live. See
§0 for the full test design and adjudication before the per-file verdicts.

---

## 0. Adjudication of Known Open Item (a): the like-count discrepancy

**Test design:** `yt-dlp 2026.07.04` against public `instagram.com/reel/<shortcode>/` URLs,
logged-out, `--sleep-requests 1`. I pulled 22 distinct reels across 9 accounts (sebastien x5,
elevenpercentprod x2, nateherkai x3, tiffintech x4, kallaway x3, handlytech x1 fresh +
corroborating a 4th independent pull already in the record, thevarunmayya x2, networkchuck x2,
nick_saraev x1), several of them twice, to test yt-dlp's own stability. Raw pulls are saved at
`/private/tmp/claude-501/.../scratchpad/ytdlp_checks/*.json` for this session (not part of the repo;
reproducible by re-running the same commands).

**Results:**
- **Comments matched exactly on 22/22 reels.** Never off by more than natural live-count drift
  (0-2 units), and usually exact to the digit, including on reels with comment counts in the
  hundred-thousands (e.g., nateherkai `DRXZJeHiAES`: 124,635 both ways).
- **Dates matched on 22/22** (one 1-day drift, `elevenpercentprod DXlFWL5EkaN`, plausibly a UTC-vs-
  local-calendar rounding difference, not a data error).
- **yt-dlp's own repeat pulls were internally 100% stable** — every reel I pulled twice (or that a
  dossier's own yt-dlp pull + my independent pull could be compared) returned the identical
  `like_count` both times, including on the account's most disputed reel, `handlytech DZozx8UoTDy`
  (114 likes on my two pulls, 114 on the `ig_handlytech.md` dossier author's two independent pulls —
  four total agreeing pulls from two different sessions).
- **Likes matched the harvest file closely on roughly half the sample** (elevenpercentprod both
  reels, nateherkai all 3, thevarunmayya both reels, tiffintech's Sanofi post, handlytech's pinned
  posts and one non-pinned post).
- **Likes diverged sharply from the harvest file on the other half**, with the multiplier varying
  unpredictably from 1.03x (noise) to **453x**:

| Reel (account) | Harvest/browser likes | yt-dlp likes (this audit) | Multiplier | Stable on repeat? |
|---|---|---|---|---|
| `DaNk7iTRewN` (tiffintech, "KEY FINDING" Lenovo post) | 2,527 | 1,145,357 | **453x** | Yes, 2 pulls |
| `DVhB8rMjp1m` (kallaway mega-spike) | 678 | 64,910 | **95.7x** | Yes, 2 pulls |
| `DW31ssREcbj` (tiffintech, 2nd Lenovo post) | 1,256 | 69,067 | **55.0x** | Yes, 1 pull, matches trio's independent value in spirit |
| `DYSWrorMzBA` (sebastien Video 3) | 395 | 10,594 | **26.8x** | Yes, 1 pull |
| `DZfgPtFObU1` (harpercarrollai Video 1) | 904 | 33,065 | **36.6x** | Caught by dossier author independently, matches this pattern |
| `DaAlMicsiBD` (sebastien Video 1) | 435 | 3,867 | **8.9x** | Yes, 2 pulls |
| `DVylvZbDGTo` (sebastien Video 2) | 379 | 2,730 | **7.2x** | Yes, 1 pull |
| `DXSDF9djpRD` (kallaway mega-spike) | 476 | 4,223 | **8.9x** | Yes, matches trio dossier's own pull exactly |
| `DYAmkc-FTUY` (networkchuck, Vanta) | 1,784 | 7,045 | **3.95x** | Yes, 1 pull |
| `DZozx8UoTDy` (handlytech) | 59 | 114 | **1.93x** | Yes, 4 pulls across 2 sessions |
| `DYWXwAmPdIr` (nick_saraev) | 987 | 1,670 | 1.69x | Yes, 1 pull |
| `DY7GAsGuwGr` (kallaway mega-spike) | 2,850 | 5,188 | 1.82x | Yes, matches trio dossier's own pull exactly |
| `DZyLjFWCX_G` (networkchuck, Vanta #2) | 1,306 | 1,591 | 1.22x | Yes, 1 pull |
| `C_iVgDcJLd1` (kallaway pinned) | 642K | 681,844 | 1.06x | minor drift only |

**Adjudication (HIGH confidence):** the browser/logged-in-session harvest method is unreliable for
**like counts specifically**, on an unpredictable subset of posts, by up to two-and-a-half orders of
magnitude. Comments, post dates, and (as far as spot-checked) view-count grid scrapes are reliable.
`yt-dlp`'s `like_count` field is reproducible across independent pulls, independent sessions, and
independent analysts (my numbers agree exactly with the `ig_trio`, `ig_handlytech`, and
`ig_harpercarrollai` dossiers' own independent `yt-dlp` pulls everywhere they overlap) — this
consistency is itself strong evidence `yt-dlp` is reading the correct field and the browser method is
not. This rules out the "IG serves different-but-equally-valid counts to different surfaces"
hypothesis (that would not produce yt-dlp's own perfect reproducibility, nor explain why comments are
never affected) and rules out pure timing drift (magnitudes up to 453x cannot accrue between same-day
pulls, and many reels show *zero* drift under identical conditions). **Best-supported mechanism (MED
confidence on the specific cause):** Instagram's rendered "Liked by `[named user]`, `[named user]` and
N others" UI pattern plausibly causes a naive browser-DOM scrape to sometimes capture only the
trailing "N others" figure rather than the true total — this would explain both the unpredictable
per-post magnitude (depends on how many named likers happen to render) and why comments, which
Instagram renders as a plain "View all N comments" numeral with no named-user prefix, are never
affected. This is inference about root cause; the fact and magnitude of the error is directly
observed.

**Consequence:** every like-rate-based "ad-boost" or "anomaly" argument in this corpus that was
**not** independently re-verified via direct `yt-dlp` against the IG reel itself is now suspect until
checked. I found this cuts both ways: some corrected numbers still support the original qualitative
conclusion (networkchuck's Vanta post: 0.018% claimed → 0.070% corrected, still clearly depressed
vs. the account's 3-5% organic norm; kallaway's `DY7GAsGuwGr`: still ~100x below norm even corrected).
Others do not survive correction: **tiffintech's two "AD-BOOSTED" Lenovo posts, the account's single
most-quoted finding in this entire study, go from "0.003-0.01%, ~1000x below organic" to 0.57%-1.55%
— a normal-to-strong engagement rate that does not support the "near-zero organic resonance" framing
the dossier builds its Section 5/8 conclusions on.**

---

## 1. Per-file verdicts and itemized findings

### `research/QC_PROTOCOL.md` and `templates/video_postmortem_template.md`
**Verdict: CLEAN.** These are the standards documents; used them as the audit yardstick. No issues.

### `research/00_seed_accounts.md`
**Verdict: CLEAN.** Every number carries source + date + confidence; DATA GAPs (Sebastien's IG
follower count, YouTube subs, posting cadence) are logged rather than papered over. Self-reported
marketing figures (AI Creator Lab membership, "1.9M+ followers") are correctly down-tagged to LOW/MED
and flagged as unverified. No findings.

### `research/01_instagram_creators.md`
**Verdict: CLEAN.** Discovery-tier roster; every follower figure carries source/date/confidence,
disagreements between sources are shown as ranges not resolved by fiat, methodology and exclusions
(virtual influencers, brand accounts) are explicit. No findings.

### `research/ig_harvest/00_INDEX.md`
**Verdict: MINOR DEFECTS.**
- **MINOR — location:** "Quick ranking" table and tiffintech's "KEY FINDING" cell. Evidence: §0
  above. The index's own text ("like-rates ~1000x below organic norm — confirmed paid view-boost")
  states as *confirmed* a magnitude that this audit shows is wrong by 55-453x on the underlying
  likes. Required correction: revise the tiffintech row to note the like-count figures need
  independent `yt-dlp` re-verification before the "1000x" language is retained; the kallaway row
  already appropriately hedges ("Cannot fully rule out a metrics artifact") — extend the same hedge
  to tiffintech.
- Positive finding: the file's pin-detection corrections (thevarunmayya 3rd pin, kallaway pin/boost
  reclassification) ARE correctly and currently reflected here — see §2 adjudication of open item (b).

### `research/ig_harvest/sebastien.md`
**Verdict: MATERIAL DEFECTS (data-quality, not integrity).**
- **MAJOR — location: Reel-detail pulls table.** 3 of 7 detail-pulled likes counts are wrong
  (`DaAlMicsiBD` 435→3,867 actual, 8.9x; `DVylvZbDGTo` 379→2,730 actual, 7.2x; `DYSWrorMzBA` 395→10,594
  actual, 26.8x — see §0). Comments and dates in this file are accurate on all 7. The file's own
  "Anomaly re-verification" for `DW_VCbrDPWM` (61K likes) is independently confirmed correct by this
  audit — that specific due-diligence effort was sound; the undetected errors are on reels that were
  never flagged as suspicious in the first place, which is the harder case to catch and explains why
  it wasn't caught here.
- Required correction: re-pull all 7 detail-pull likes via `yt-dlp` and update the table; flag
  downstream consumer (`creators/ig_sebastien.md`) for revision (see below).

### `research/ig_harvest/elevenpercentprod.md`
**Verdict: CLEAN.** Both spot-checked reels (`DX-bJErPxe7`, `DXlFWL5EkaN`) matched my independent
pull within normal live-count drift. The "156% median/follower ratio" headline arithmetic is directly
shown and correct: 133K / 85K ≈ 156% (this resolves the audit-protocol instruction to re-derive this
specific claim — **VERIFIED, not fabricated**).

### `research/ig_harvest/nateherkai.md`
**Verdict: MINOR DEFECTS.**
- **MINOR — location: "Computed stats" vs. "Reel-detail pulls" sections.** Internal inconsistency:
  the "Computed stats" section defines the bottom-2 flops as excluding only the single
  most-recent tile, yielding `DbJKDTnFAjW` (11.2K) + `DbGlL0ciIvc` (12.5K). Three paragraphs later,
  the "Reel-detail pulls" section silently switches to excluding the 3 most-recent tiles, yielding a
  *different* pair — `DbGlL0ciIvc` (12.5K) + `DbDJlTkgOtY` (14.6K) — and it is this second pair that
  gets pulled and analyzed. The account's single worst-performing genuinely-organic reel in the
  sampled grid (`DbJKDTnFAjW`, 11.2K) is silently dropped without explanation and replaced with a
  reel that is itself a sponsored ChatGPT-partner post. This is very likely an innocent methodology
  drift (not cherry-picking — the sponsored-post substitute is if anything a *less* flattering choice
  for the account), but the two stated exclusion rules directly contradict each other within one file
  and should be reconciled.
- Likes/comments/dates on all 3 spot-checked detail-pulled reels (`DRXZJeHiAES`, `DZku3mJH594`,
  `DbGlL0ciIvc`) matched my independent pull closely. No fabrication found.

### `research/ig_harvest/tiffintech.md`
**Verdict: MATERIAL DEFECTS.**
- **MAJOR — location: "Pattern note" and Reel-detail pulls, `DaNk7iTRewN`/`DW31ssREcbj` rows.** The
  file's central claim for this account — "the clearest signature seen across this entire study of a
  paid-media view-count boost... 0.0034%/0.01% like-rate" — is built on likes counts wrong by 453x
  and 55x respectively (§0). Corrected like-rates (1.55%, 0.57%) are not "1000x below organic" and do
  not obviously support "near-zero engagement." The genuinely strong evidence in this file — the
  disclosed `#LenovoFIFA #LenovoPartner` hashtags and the astronomical absolute view counts (73.7M
  vs. an ~800K-2.5M organic ceiling) — still supports *some* paid-amplification read, just not via the
  like-rate argument as stated.
- The Sanofi post (`DZxAH3LxaSA`) figures are **independently confirmed accurate** by this audit
  (1,528 claimed vs. 1,577 actual, within noise) — the "partial boost" finding for that specific post
  survives scrutiny and should NOT be revised.
- Required correction: re-pull `DaNk7iTRewN` and `DW31ssREcbj` likes via direct `yt-dlp` against the
  IG reel URLs (not the harvest table), recompute like-rates, and rewrite the "why it won" synthesis
  for both videos — the current unhedged language ("stated plainly and without hedging: this number
  is bought, not earned") and the STEPPS section's claim that "the engagement data flatly contradicts
  any read of this as psychologically resonant content" no longer hold at the stated magnitude.

### `research/ig_harvest/kallaway.md`
**Verdict: MATERIAL DEFECTS (data-quality), well-flagged.**
- **MAJOR — location: "Pin/date confirmation" table.** All 3 mid-grid "mega-spike" likes counts are
  wrong (`DVhB8rMjp1m` 678→64,910, 95.7x; `DXSDF9djpRD` 476→4,223, 8.9x; `DY7GAsGuwGr` 2,850→5,188,
  1.8x — §0). Corrected like-rates (0.088%, 0.011%, 0.015%) are still well below the account's
  confirmed-organic pinned-tile norm (1.3%-4.4%), so the qualitative "anomalously low engagement,
  possible undisclosed boost" conclusion is **more defensible than tiffintech's** even after
  correction — this file's headline finding survives, just needs the specific multiplier language
  ("100-1000x below organic norm") softened to something like "15-400x," which is still a real and
  striking gap.
- Credit: this file's own re-verification methodology (§"Pin/date confirmation") is sound and its
  hedging ("Cannot fully rule out a metrics artifact") was, in hindsight, the correct level of
  caution — the metrics-artifact possibility it declined to rule out is in fact substantially what
  happened, just on a different tool (browser vs. yt-dlp) than any explanation it considered.

### `research/ig_harvest/handlytech.md`
**Verdict: MINOR DEFECTS.**
- **MINOR — location: `DZozx8UoTDy` "Anomaly re-verification."** The section confidently states "59
  likes... CONFIRMED, not a metrics-sync error" after two same-method re-pulls. This audit (and,
  independently, the `ig_handlytech.md` dossier's own `yt-dlp` re-pulls) found the true count is 114,
  stable across 4 total independent pulls from 2 different tools/sessions. The file's re-verification
  *was* internally rigorous (same tool, repeat pull, matched) — its failure mode is that repeating the
  same (flawed) method twice cannot catch a systematic bug in that method, only random noise. This is
  a good example of the limits of same-method re-verification generally, worth a QC-protocol footnote
  for future harvests: cross-method verification (a second, independent tool), not just repeat-pull
  of the same tool, is required to catch this class of error.

---

### `research/creators/ig_sebastien.md`
**Verdict: MATERIAL DEFECTS.**
- **BLOCKER-adjacent — location: Video 1, 2, 3 post-mortems (§0/§5/§8 of each).** This is the one
  dossier in my full sample that explicitly did **not** independently re-verify IG like/comment
  counts via `yt-dlp` against the IG reels themselves (method note: "Cross-platform verification...
  obtained via yt-dlp against TikTok... and two YouTube channels" — TikTok/YouTube only). Six-plus
  other dossiers in this corpus (elevenpercentprod, nateherkai, thevarunmayya, trio/kallaway,
  handlytech, harpercarrollai) made exactly this cross-check standard practice and, as a direct
  result, caught and corrected the same class of error this audit is flagging. Because this dossier
  skipped that step, it propagated the harvest's wrong numbers into unhedged, precisely-quantified
  claims:
  - Video 1: "IG like-rate is 0.018%... the single lowest like-rate of any of the 5 top videos...
    TikTok twin's like-rate is 9.8% — over 500x higher on a per-view basis." **Corrected:** IG
    like-rate is 0.161% (3,867/2.4M), and the TikTok gap is ~61x, not "over 500x."
  - Video 3: like-rate stated as 0.0395%; **corrected** 1.059% — actually higher than Video 5's
    0.625%, which the dossier (working from the wrong numbers) implicitly treats as the
    second-best performer of the set.
  - Recomputed ranking (lowest→highest like-rate) changes from the dossier's stated
    V1<V2<V3<V5<V4 to the corrected V1<V2<V5<V3<V4 — the dossier's Section 8 "arguably the weakest
    of the 5 top videos despite ranking #1 by raw views" claim for Video 1 survives directionally
    (V1 is still lowest) but the "500x" magnitude claim built on it does not, and Video 3's
    engagement read is now backwards from what's stated.
- Required correction: re-pull Videos 1, 2, 3's IG likes via direct `yt-dlp` (Videos 4 and 5 are
  independently confirmed accurate — no changes needed there), recompute all like-rate comparisons in
  §0/§5/§6/§8 of the affected post-mortems, and revise the cross-video ranking language.
- Everything else in the ~770 lines read (packaging/hook/structure analysis, TikTok cross-post
  matching, funnel-map, business-model figures) is well-sourced and appropriately tagged; this is a
  numeric-verification gap, not a fabrication or laziness problem — the prose analysis is genuinely
  strong. Scope note: read lines 1-767 of 1003; Section C and the Method log (unread) should be
  checked for whether they compound the same three wrong numbers before this correction is applied.

### `research/creators/ig_elevenpercentprod.md`
**Verdict: CLEAN** (on the ~760/1128 lines read: account header, funnel map, Videos 1-5, start of
Video 6). Exemplary practice: independently `yt-dlp`-pulled all 7 reels directly, and all values
matched my own independent pulls closely (`DX-bJErPxe7`: 53,167/53,169 likes, 61,429/61,431 comments;
`DXlFWL5EkaN`: 26,429/26,429 likes exact). No fabrication found. One trivial note: Video 3's date is
logged as "Apr 3" in the dossier body vs. "Apr 2" in the harvest — correctly flagged in-line by the
dossier itself as a likely timezone rounding difference, not an error. Scope note: Videos 6-7 and
Section C/D/Method log (lines 761-1128) not read this pass.

### `research/creators/ig_nateherkai.md`
**Verdict: CLEAN** (on the ~753/1250 lines read: account header, Videos 1-7). Exemplary practice:
independently `yt-dlp`-pulled every IG reel directly; my spot checks (`DRXZJeHiAES`: 89,816/89,817
likes; `DZku3mJH594`: 10,860/10,853 likes; `DbGlL0ciIvc`: 129/129 likes exact) all matched within
normal live-count drift. No fabrication found in the sections read. Scope note: Videos 8-9, Section
C/D (the IG-vs-YT translation-ratio analysis promised in the file's own framing), and Method log
(lines 754-1250) not read this pass — the file's own top-line comparison table (§A) is internally
consistent with what I did read.

### `research/creators/ig_tiffintech.md`
**Verdict: MATERIAL DEFECTS.**
- Inherits the harvest-level defect described above. This dossier's Video 1 (Sanofi) section is
  **CLEAN and independently strong** — it correctly identified a real, subtler partial-boost signature
  that the raw harvest had missed, and its underlying likes (1,528) are accurate.
- **BLOCKER-adjacent — location: Video 6 and Video 7 post-mortems (§0/§5/§6/§8).** Both explicitly
  cite "harvest table" as the source for likes/comments and do not independently `yt-dlp`-verify
  against the IG reel itself — the one place in this ~1,630-line dossier where that verification step
  was skipped is also the two videos carrying the account's single headline finding (explicitly
  labeled "the single most important comparison data point in this entire dossier" for Video 6). This
  is the same failure pattern as `ig_sebastien.md`, and here it is more consequential because this
  specific finding is quoted near-verbatim into `ig_harvest/00_INDEX.md`'s "KEY FINDING" line and into
  synthesis point A.1 (see §3 below) — i.e., it propagated furthest of any single wrong number found
  in this audit.
- Required correction: re-pull `DaNk7iTRewN`/`DW31ssREcbj` likes, rewrite Video 6/7 §0/§5/§6/§8, and
  flag `00_INDEX.md` + synthesis A.1 for downstream correction (both already flagged above/below).
- Scope note: read account header, Method-log header, Video 1, Video 6, Video 7, and targeted greps
  across the full file for Sanofi/pin-related claims; Videos 2-5 (the organic top performers) and the
  full consistency-decomposition sections (roughly 700 of 1633 lines) not read line-by-line this pass.

### `research/creators/ig_trio_kallaway_saraev_ankitarora.md`
**Verdict: kallaway section CLEAN and exemplary; nick_saraev/ai_ankitarora sections NOT
INDEPENDENTLY VERIFIED this pass — no verdict rendered on those two-thirds of the file.**
- The kallaway portion (Videos 1-3 + flop) is the best-handled instance of the likes-discrepancy issue
  in the entire corpus: it explicitly reports BOTH its own `yt-dlp` numbers and the harvest's
  conflicting re-verification numbers side by side, computes like-rate under both readings, and
  states a conclusion ("both are far below this account's genuine organic norm... so the
  anomalous-engagement conclusion holds regardless of which count is correct") that in fact holds up
  under this audit's independent confirmation that its own `yt-dlp` numbers (64,910 / 4,223 / 5,188)
  were the correct ones all along. This is the model other dossiers should have followed.
- One spot-check outside kallaway: `DYWXwAmPdIr` (nick_saraev's flagged anomaly, cited in
  `ig_harvest/nick_saraev.md` but not reused in this trio dossier's own 4-per-account selection) —
  harvest says 987 likes, `yt-dlp` returns 1,670 (1.7x, comments exact match at 455) — consistent with
  the corpus-wide pattern but this specific reel is outside the trio dossier's actual selected
  sample, so it is not a defect *in this file*.
- Scope note: nick_saraev and ai_ankitarora sections (roughly two-thirds of the 1,750-line file) were
  not read this pass; no verdict is offered on them rather than guessing.

### `research/creators/ig_handlytech.md`
**Verdict: CLEAN** (on the ~535/1249 lines read: account header, Videos 1-4, i.e., all 3 pinned
mega-hits + the flagged `DZozx8UoTDy` anomaly). This is the strongest single piece of QC craftsmanship
found anywhere in this audit: Video 4's write-up documents, without spin, a genuine three-way
conflict across four total pulls (harvest x2 = 59/59, this dossier x2 = 114/59) and computes the
"why it won" conclusion so it holds under *either* reading — which is exactly the discipline this
audit's own §0 test vindicates (114 is correct; the conclusion the dossier reached anyway is sound).
Pinned-tile likes (`C9PdusWtkOh` 2,118,218; `DFC6zh3iZKn` 576,699) independently match my priors from
the harvest cross-check. Scope note: Videos 5-8 and the "Autopsy" timeline section/Method log (lines
536-1249) not read this pass.

### `research/creators/ig_thevarunmayya.md`
**Verdict: CLEAN** (on the ~743/1207 lines read: account header, Videos 1-5, Flop 1, start of Flop
2). All 4 of my independent spot-checks (`DZFtk5xB-d8` 90,292 exact match; `DaDD4gWh3Kn` 2,384 exact
match; plus the file's own stated cross-validation on all 7 harvest-overlapping videos) confirm this
dossier's numbers are accurate. The pin-status correction (3rd pinned tile, `DExE3UOhUoq`) is
well-evidenced (date-verified via independent `yt-dlp` timestamp pull) and correctly propagated to
`00_INDEX.md` — see §2. No fabrication found. This is, along with `ig_handlytech.md`, one of the two
strongest dossiers sampled in this audit. Scope note: Videos 6-10, Section C/D, and Method log (lines
744-1207) not read this pass.

### `research/creators/ig_sabrina_ramonov.md`
**Verdict: PARTIAL VERIFICATION, CLEAN so far** (on the ~200/1172 lines read: account header, funnel
map, start of Video 1). The account header's own stated cross-validation (`DYu1xbHEUD5`: harvest
"195K/145K" vs. dossier's direct pull "194,914/145,309") is internally consistent and plausible. No
independent re-pull performed by this audit due to time budget — flagging honestly rather than
extrapolating a verdict from an unread 83% of the file. No red flags in the portion read.

### `research/creators/ig_harpercarrollai.md`
**Verdict: PARTIAL VERIFICATION, CLEAN handling so far** (on the ~150/1135 lines read: account
header, funnel map, start of Video 1). Notable: this dossier **independently caught a 36.6x likes
discrepancy** on its own (`DZfgPtFObU1`: harvest 904 likes vs. its own `yt-dlp` pull 33,065 likes),
diagnosed it correctly ("most likely explanation is a transcription slip in the original browser-based
harvest... not a genuine change"), and used the corrected number as primary — textbook handling,
consistent with the root-cause mechanism this audit proposes in §0. Also independently found and
disclosed a data-quality issue the raw harvest missed (2 more non-owner/collab tiles beyond the 2 the
harvest had flagged, revising the "true organic floor" from ~45-50K to 36.2K) — good-faith, rigorous
work. Scope note: Videos 2-7+ and Sidebar/Method log (lines 151-1135, ~87% of the file) not read this
pass.

### `research/creators/ig_vaibhavsisinty.md`
**Verdict: PARTIAL VERIFICATION, CLEAN so far** (on the ~150/1008 lines read: account header, funnel
map, start of Video 1). Uses `WebFetch` rather than `yt-dlp` as its cross-check method but reports
the comparison transparently (27K harvest vs. 27.4K WebFetch — consistent, rounding only). No red
flags in the portion read; appropriately labels reused/non-re-verified figures as MED confidence
rather than inheriting the earlier prototype pull's HIGH tag. Scope note: ~85% of the file (Videos
2-7, Section D/E) not read this pass.

### `synthesis/00_INTERIM_convergences.md`
**Verdict: MINOR-MATERIAL DEFECTS** (Instagram-sourced claims only, per scope).
- **MAJOR — location: point A.1** ("Raw view counts lie; engagement signatures don't"). Cites
  "TiffinTech IG (Lenovo/FIFA 73.7M, 0.003-0.01%)" as one of four flagship examples supporting a
  corpus-wide "RULE FOR SYNTHESIS." This specific number is wrong per §0 above — corrected it is
  0.57%-1.55%, which undercuts rather than supports the point as evidence from this account. The
  general rule (sanity-check like-rates before treating a view count as an organic lesson) remains
  sound advice and is separately supported by the NetworkChuck citation in the same point, which this
  audit spot-checked and found directionally intact even after correction (0.018%→0.070%, still ~50x
  below organic norm). Required correction: replace or caveat the tiffintech citation before this
  point ships in final synthesis; do not drop the rule itself.
- **VERIFIED, no defect — point B, elevenpercentprod 156% ratio.** Directly and correctly computed
  in the harvest file (133K/85K); not fabricated.
- **VERIFIED, no defect — point B/C, kallaway resolution note.** Accurately reflects
  `ig_harvest/kallaway.md`'s (appropriately hedged) re-verification finding; this audit's correction
  to the underlying like-rate magnitudes (§0) does not change the qualitative conclusion stated here
  ("35.8/39.5/74.2M mid-grid spikes are UNDISCLOSED paid boosts... true organic ceiling ~177K"),
  which still holds under corrected numbers.
- **VERIFIED, no defect — point C, "Varun Mayya same-account 10-15x organic-vs-ad gap."** Matches
  `ig_thevarunmayya.md`'s own stated 14-15x figures exactly; both flops and the pin-count correction
  are otherwise not mentioned in synthesis (nothing to correct — the pin correction lives correctly
  in `00_INDEX.md` only, and synthesis never states a pin count for this account that would need
  fixing).
- No template-sameness or internal-consistency issues found in this file; it is transparent about
  its own provisional status and already flags several of its own open items correctly (see its own
  §C, which anticipates several of the questions this audit was asked to resolve).

---

## 2. Adjudication of Known Open Item (b): correction propagation

**tiffintech Sanofi partial-boost reclassification:** propagated correctly and consistently
everywhere it's referenced — `ig_harvest/tiffintech.md` (original finding), `00_INDEX.md`
("CORRECTION (dossier agent, 2026-07-25)..." line), and `creators/ig_tiffintech.md` Video 1 (full
treatment). It does not appear in synthesis at all, which is not a gap since synthesis never asserts
anything about it that would need correcting. **No open item remains — this one is clean.** (Note,
independent of propagation: this audit separately confirmed the underlying Sanofi likes figure itself
is accurate, so this specific finding is on solid ground both for propagation AND for data quality —
the one genuinely trustworthy "boost" finding of the three flagged on this account.)

**thevarunmayya third-pin correction:** propagated correctly to `00_INDEX.md` ("CORRECTION (dossier
agent, 2026-07-25): 3 pinned tiles, not 2..." line) and fully documented in `creators/ig_thevarunmayya.md`
§B intro, including the explicit note that the original `ig_harvest/thevarunmayya.md` file was left
uncorrected by design (per the dossier's own stated policy of not altering primary source files) with
a pointer for the reader to treat the index as superseding it. This is the correct pattern — flagged,
not silently altered, and the index (the one place synthesis-writers are likely to look) reflects it.
**No open item remains — this one is clean.**

---

## 3. Template-sameness and internal-consistency scan

No copy-paste boilerplate psychology sections found in the roughly 40 video post-mortems read in
detail across this audit. STEPPS scoring is consistently tied to specific, video-particular evidence
(caption text, comment threads, frame content) rather than generic pillar language reused verbatim
across videos. The one recurring "boilerplate" element found (`ig_harpercarrollai.md` noting a
"standing credential-forward signature block" recurring across nearly every post) is the **creator's
own** caption sign-off, correctly identified by the analyst as such, not an analyst shortcut.

Internal consistency: the one genuine defect found is the `ig_harvest/nateherkai.md` flop-selection
methodology inconsistency documented above (§1). No other summary-vs-underlying-data mismatches were
found in the sections read; account-header tables consistently matched the per-video detail sections
that fed them wherever both were checked.

---

## 4. Corpus-half verdict

**Overall: MINOR-MATERIAL DEFECTS, correctable.** This is not a corpus built on invented numbers —
every figure traces to a real tool pull, and the analysts' own hedging discipline (DATA GAP tags,
confidence tiers, explicit "harvest table, not independently re-verified" sourcing notes) is
generally excellent and is precisely what made this audit possible to conduct efficiently: I could
tell from each dossier's own method notes exactly which claims had been cross-verified and which
hadn't, and the ones flagged as unverified were disproportionately the ones that turned out to have
problems. The corpus's own internal QC signal is trustworthy even where its numbers aren't yet.

The real defect is a **tooling limitation** (browser-scraped like counts, silently wrong on an
unpredictable subset of posts) that the corpus caught, diagnosed, and corrected inconsistently: 6+
dossiers built independent `yt-dlp` cross-verification into standard practice and, as a direct
result, caught and fixed real errors (harpercarrollai, kallaway/trio, handlytech all self-corrected
a version of this exact bug before I ever ran a single pull). Two dossier sections did not do this
cross-check on their most consequential reels (`ig_sebastien.md` Videos 1-3; `ig_tiffintech.md`
Videos 6-7) and, as a direct and predictable result, are carrying materially wrong numbers into
confident, unhedged prose — in tiffintech's case, numbers that propagated as far as the corpus's
`00_INDEX.md` headline finding and a synthesis-level "RULE FOR SYNTHESIS."

### REQUIRED CORRECTIONS for the synthesis author (in priority order)

1. **Before citing tiffintech's Lenovo posts as evidence anywhere in final synthesis:** re-pull
   `DaNk7iTRewN` and `DW31ssREcbj` likes via direct `yt-dlp` against the IG reel URLs (not the
   harvest table), recompute like-rates (expect ~1.55% and ~0.57%, not 0.003%-0.01%), and rewrite
   `ig_harvest/tiffintech.md`'s pattern note, `00_INDEX.md`'s tiffintech "KEY FINDING" cell, and
   `creators/ig_tiffintech.md` Videos 6-7 §0/§5/§6/§8 accordingly. Update synthesis point A.1 to drop
   or caveat the tiffintech citation.
2. **Before citing sebastien's Video 1-3 engagement-rate comparisons anywhere in final synthesis:**
   re-pull those 3 reels' likes via direct `yt-dlp`, recompute like-rates, and correct the "over 500x
   higher on TikTok" and "single lowest like-rate of the 5" claims in `creators/ig_sebastien.md`.
3. **Soften, don't retract, the kallaway mid-grid-spike magnitude language** ("100-1000x below
   organic") to the corrected range (~15-400x) in `ig_harvest/kallaway.md` and anywhere it's quoted —
   the underlying "undisclosed paid boost" conclusion survives and does not need retraction.
4. **Add a standing QC-protocol note** (this is a process fix, not a per-file correction): any
   like-count sourced only from the browser/logged-in harvest and used to support a "near-zero
   engagement / paid boost" argument must get one direct `yt-dlp` pull against that specific reel
   before the claim ships to final synthesis. This is cheap (one command per reel) and this audit's
   own sample shows it would have caught every error found. Comments, dates, and views did not need
   this treatment in any check performed.
5. **Complete the audit on the unread ~60% of this corpus** (nick_saraev/ai_ankitarora sections of
   the trio dossier; the back halves of sebastien, elevenpercentprod, nateherkai, tiffintech,
   handlytech, thevarunmayya; and the bulk of sabrina_ramonov, harpercarrollai, vaibhavsisinty) before
   treating this Gate C pass as exhaustive — this audit prioritized breadth-of-verification (yt-dlp
   spot-checks across every required account) and the highest-risk sections (flagged anomalies,
   headline findings) over line-by-line completeness given scope, and found enough in that sample to
   warrant the corrections above; it cannot rule out further, lower-magnitude instances of the same
   bug in the unread portions.

---

## 5. Three most serious findings

1. **tiffintech's "KEY FINDING"** (the account's headline result, quoted into `00_INDEX.md` and
   synthesis point A.1) — that the 73.7M/12.1M Lenovo/FIFA posts show near-zero engagement proving a
   pure paid view-boost with no organic resonance — rests on like counts wrong by **453x and 55x**.
   Corrected engagement rates (1.55%, 0.57%) are unremarkable, not "1000x below organic," and do not
   support the dossier's unhedged "this number is bought, not earned... stated plainly and without
   hedging" conclusion as written.

2. **`ig_sebastien.md` is the one dossier in this sample that skipped the corpus's own
   emerging best practice** (independent `yt-dlp` verification of IG likes against the reel itself,
   used by 6+ peer dossiers) — and, as a direct, predictable consequence, propagated wrong like-rate
   figures (7x-27x off) on 3 of its 5 "top" video post-mortems into confidently-stated, precisely-
   quantified claims ("over 500x higher," "the single lowest like-rate of any of the 5 top videos")
   that do not survive independent re-verification.

3. **The corpus-wide root cause is a genuine, previously only partially-diagnosed tooling defect**,
   not sloppiness: the browser/logged-in-session like-count scrape is silently wrong on an
   unpredictable ~45% of the reels sampled in this audit (comments and dates were never wrong in 22/22
   checks), with error magnitudes from negligible to 453x uncorrelated with account size, engagement
   tier, or whether the post was already flagged as suspicious. Repeat-pulling the same (flawed) tool,
   as `ig_harvest/handlytech.md`'s own "re-verification" did, cannot catch this — only a second,
   independent tool (`yt-dlp` against the public reel URL) can, and every dossier that did this caught
   real errors.
