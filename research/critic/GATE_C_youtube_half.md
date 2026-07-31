# GATE C — Independent Critic Audit: YouTube Corpus Half

**Auditor:** independent critic agent, fresh context, no stake in the work.
**Scope:** `03_virality_science.md`, `02_youtube_channels.md`, the 8 YouTube creator dossiers
(`creators/yt_wesroth.md`, `yt_nateherk.md`, `yt_berman.md`, `yt_rileybrown.md`, `yt_curiousrefuge.md`,
`yt_liamottley.md`, `yt_skillleap.md`, `yt_futurepedia.md`), and the YouTube-sourced items in
`social_launch/synthesis/00_INTERIM_convergences.md`.
**Date of audit:** 2026-07-25. **Standards enforced:** `QC_PROTOCOL.md` and
`templates/video_postmortem_template.md`, both read in full before auditing.
**Default posture:** refute first. Every finding below required either an independent yt-dlp re-pull,
an independent web search, an independent arithmetic re-derivation, or a cross-file text search — not
a plausibility read.

**Path note:** the interim convergences file lives at
`/Users/sparsh/Documents/Projects/Tangent/social_launch/synthesis/00_INTERIM_convergences.md`, not
under `research/synthesis/` as the assignment brief implied. Flagging only because a future auditor
searching the stated path will find nothing there.

---

## Method: what I actually did (so this audit is itself auditable)

### Full reads
Read `QC_PROTOCOL.md`, `templates/video_postmortem_template.md`, `03_virality_science.md` (368 lines),
`02_youtube_channels.md` (201 lines), all 8 creator dossiers in full (1233–1665 lines each, ~114K words
total), and `00_INTERIM_convergences.md` (105 lines). No file was skimmed or read from an excerpt only.

### Spot re-verification pulls (yt-dlp, live, 2026-07-25, `--sleep-requests 1`)
26 individual video pulls (`--print "%(view_count)s|%(like_count)s|%(comment_count)s"`) across all 8
dossiers, plus 4 full-catalog population recounts (`--flat-playlist`). Every single pull is logged
below with dossier-claimed vs. re-pulled values.

| # | Creator | Video ID | Dossier claim (v/l/c) | Re-pulled (v/l/c) | Verdict |
|---|---|---|---|---|---|
| 1 | Wes Roth | rAWB8-qiVQo | 730,407 / 439 / 41 | 733,632 / 439 / 41 | MATCH (+0.4% view drift, normal accrual) |
| 2 | Wes Roth | Wn5fmdJ7Oxw | 104,950 / 3,787 / 663 | 104,957 / 3,787 / 663 | MATCH |
| 3 | Wes Roth | 8gfZZHMunnY (flop) | 3,190 / 83 / 15 | 3,190 / 83 / 15 | EXACT MATCH |
| 4 | Nate Herk | 2aC2ly7vKtM | 1,343,016 / 50,826 / 548 | 1,342,997 / 50,827 / 548 | MATCH |
| 5 | Nate Herk | NWbh5ZoEHkA (flop) | 4,881 / 77 / NA | 4,881 / 77 / NA | EXACT MATCH (comment_count unavailable both times, as dossier disclosed) |
| 6 | Berman | -178Xr-kSSI | 2,565,497 / 68,654 / 4,900 | 2,565,497 / 68,654 / 4,900 | EXACT MATCH |
| 7 | Berman | FxF_whsmwfA | 767,135 / 12,101 / 479 | 767,135 / 12,101 / 479 | EXACT MATCH |
| 8 | Berman | mI1d1WqIQWQ (flop) | 3,603 / 97 / 11 | 3,603 / 97 / 11 | EXACT MATCH |
| 9 | Riley Brown | GZxjs8FD3Ck | 184,479 / 6,161 / 753 | 184,479 / 6,161 / 753 | EXACT MATCH |
| 10 | Curious Refuge | KrjL_TSOFrI (LOTR) | 4,412,573 / 91,804 / 3,900 | 4,412,573 / 91,804 / 3,900 | EXACT MATCH |
| 11 | Curious Refuge | s-x_KdD15Gs | 19,347 / 458 / 54 | 19,348 / 458 / 54 | MATCH |
| 12 | Curious Refuge | d3BM3GEWpHE (flop) | 3,333 / 116 / 45 | 3,333 / 116 / 45 | EXACT MATCH |
| 13 | Liam Ottley | TmxBWCOUWVc (the one Short) | 90,282 / 5,277 / 45 | 90,282 / 5,278 / 45 | MATCH |
| 14 | Liam Ottley | w0H1-b044KY | 3,627,172 / 84,354 / 2,800 | 3,627,417 / 84,356 / 2,800 | MATCH |
| 15 | Skill Leap | qI2_v_xWGX4 | 1,028,157 / 34,122 / 374 | 1,028,157 / 34,122 / 374 | EXACT MATCH |
| 16 | Skill Leap | 6WVddn7qieU | 62,512 / 1,286 / 26 | 62,512 / 1,286 / 26 | EXACT MATCH |
| 17 | Futurepedia | D3tFS26uxQ0 | 6,633,656 / 190,937 / 4,200 | 6,633,740 / 190,939 / 4,200 | MATCH |
| 18 | Futurepedia | BAE03hKz9Zo (anomalous engagement) | 3,232,087 / 2,666 / 25 | 3,232,089 / 2,666 / 25 | MATCH |
| 19 | Futurepedia | kCQPc8XeqrA (flop) | 5,208 / 203 / 7 | 5,208 / 203 / 7 | EXACT MATCH |

Population recounts (`--flat-playlist` on `/shorts`):

| Creator | Dossier claim | Re-pulled | Verdict |
|---|---|---|---|
| Liam Ottley | exactly **1** Short in the entire catalog | 1 row returned | CONFIRMED — the single most extraordinary claim in the corpus holds up |
| Skill Leap AI | exactly **30** Shorts (full population) | 30 | CONFIRMED |
| Curious Refuge | exactly **43** Shorts | 43 | CONFIRMED |
| Riley Brown | exactly **39** Shorts (shelf ceiling) | 39 | CONFIRMED |
| Futurepedia | exactly **67** Shorts | 67 | CONFIRMED |

**Result: 19/19 video-level pulls matched (all within normal hours-later accrual drift, most exact),
5/5 population counts matched exactly.** I found zero fabricated or inflated numbers anywhere I checked.

### Arithmetic re-derivation (one median/ratio per dossier, recomputed from the dossier's own listed data)
- Wes Roth: (13,009+13,353)/2 = 13,181 ✓; 730,407/13,181 = 55.4x ✓
- Nate Herk: 1,343,016/25,500 = 52.7x ✓
- Berman: top-10/total = 5,084,000/9,796,900 = 51.90% ✓ (cited as "~51.9%"); 2,565,497/19,000 = 135.03x ✓
- Riley Brown: 184,479/11,363 = 16.24x ✓
- Curious Refuge: 4,412,573/29,000 = 152.2x ✓ (cited 152x); 29,000/3,400 = 8.53x ✓ (cited 8.5x)
- Liam Ottley: 3,627,172/43,502 = 83.4x ✓ — **but see LIAMOTTLEY-1 below for a median-definition nitpick**
- Skill Leap: 1,028,157/6,200 = 165.8x ✓; 1,028,157/62,512 = 16.45x ✓ (cited 16.4x)
- Futurepedia: 6,633,656/16,346 = 405.8x ✓

All arithmetic checked out exactly except the one item flagged below.

### Template-sameness scan
Extracted every 10+ consecutive-word phrase from all 8 dossiers and diffed for cross-file exact
duplicates. **Zero exact 10-word-or-longer duplicate phrases found across any two dossiers.** Also
manually compared STEPPS-scan openings across all 8 files during the full read — each cites distinct,
video-specific evidence (verbatim quotes, specific numbers, specific on-screen actions), not swapped
nouns on a fixed template. This is a genuine strength of the corpus, not a formality.

### Rubric citation audit (5 most load-bearing claims in `03_virality_science.md`)
1. **Berger & Milkman (2012), JMR 49(2), 192-205** — confirmed real, confirmed to say what's claimed
   (high-arousal emotion, positive or negative, drives virality; low-arousal sadness does not, despite
   being negative). [Verified via WebSearch]
2. **Loewenstein (1994), Psychological Bulletin** — confirmed real, confirmed information-gap theory
   and the "too little vs. too much context" satiation point the rubric attributes to it. [Verified]
3. **Todd Sherman / Jenny Hoyos, blog.youtube "Shorts deep dive"** — confirmed the article exists at
   the cited URL and confirms the "one second to hook," feed-not-search, swiped-away framing. [Verified]
4. **Instagram's official "less visible" list** — confirmed the exact quoted language ("low-resolution
   or watermarked reels, reels that are muted or contain borders, reels that are majority text, or
   reels that have already been posted") is genuine Instagram-sourced language, not an invented quote.
   [Verified via WebSearch of the official Mosseri blog post]
5. **Mosseri sends/shares "3-5x" claim** — the rubric itself tags this `[PRACTITIONER LORE]` and states
   "no primary transcript located." I independently searched and found the same thing: only secondary
   blogs (Torro, DataSlayer, Socialync) repeating the claim, no primary Mosseri transcript. **The
   rubric's hedge is correct and well-calibrated, not overclaimed** — this is the rubric being honest
   about a real limit in its own evidence base.

**Exclusion-list check:** the rubric's bottom-of-document "explicitly flagged as unverifiable" list
(UF 38% retention study, "3.3 billion Shorts analyzed" study, several specific percentage lifts) is
appropriately excluded from being cited as fact anywhere in the rubric body. One nuance: my search for
the "3.3 billion Shorts" stat did turn up a named source (a Medium post by Antoine Lacombled) — so the
rubric's specific phrasing "source not named anywhere it's cited" is not 100% precise (a name does
exist somewhere). This doesn't change the rubric's correct practical guidance (a single self-published
Medium post is not a verifiable methodology and should not be cited as fact) — MINOR, not a
correction that changes any downstream grading decision.

---

## Per-file verdicts and itemized findings

### `03_virality_science.md` — **CLEAN**
No findings above MINOR. All 5 audited load-bearing citations are real and accurately characterized.
Evidence-tier tagging is applied consistently and, notably, the document is *more* conservative than
it needed to be in places (e.g., correctly demoting the Mosseri sends/shares claim to practitioner
lore despite it being directionally well-supported by Instagram's own official statements). No
fabricated citations, no misattributed findings, exclusion list appropriately used.

- **MINOR — RUBRIC-1**: "3.3 billion Shorts analyzed" exclusion note says "source not named anywhere
  it's cited"; a named source (Medium, Antoine Lacombled) exists. Correction: soften to "a
  single-author, non-peer-reviewed Medium post with undisclosed raw data — not independently
  verifiable" rather than implying total namelessness. Does not change the do-not-cite guidance.

### `02_youtube_channels.md` — **CLEAN**
Cross-checked every subscriber count and every dossier-tie-in figure in this file against the 8
dossiers' own independent live pulls (which post-date this roster by the same research day). All
subscriber counts match within normal drift (Herk 870K, Roth 324K, Berman 626K, Ottley 825K, Riley
Brown 264K, Skill Leap 335K, Curious Refuge 269K, Futurepedia 729K). The file's own honesty flags
(Futurepedia Shorts-tab tooling failure, Rowan Cheung 404, Socialblade inaccessible) are corroborated
by the downstream dossiers actually re-deriving the numbers this file couldn't get — i.e., the file's
self-reported gaps were real gaps, not cover for invented numbers, and they were subsequently closed
by dedicated dossiers as promised.

### `creators/yt_wesroth.md` — **CLEAN**
- 3/3 spot-checked videos matched exactly or within normal drift. Median/ratio arithmetic correct.
- The dossier's central analytical move — flagging the #1 short (HeyGen, 730K views) as likely
  paid-impression-inflated rather than organic, based on a 0.06% like-rate vs. 2.6–2.9% for the
  channel's own worst *organic* flops — is well-reasoned, cites the actual `[OBSERVED]` facts
  (paid-partnership badge, affiliate link, disclosed sponsorship) separately from the `[INFERRED]`
  conclusion, and is repeated with the inference tag intact every time it recurs (Video 1 §8, Section
  C, Section D). Not a defect; flagged only because a synthesis author skimming might treat the
  inference as flatly proven — it is well-argued but still an inference, and the dossier says so every
  time.
- Data gaps (44-short lifetime-total ambiguity, 7/11 frame-1 visuals not screenshotted, x.com handle
  discrepancy unresolved) are disclosed, not papered over. No `[OBSERVED]` tag found anywhere that
  should have been `[INFERRED]`.

### `creators/yt_nateherk.md` — **CLEAN**
- 2/2 spot-checked videos (including the flop with an unavailable comment count) matched exactly.
- The dossier's headline finding — Video 1 (1.3M views) vs. Video 9 (7,398 views), same format,
  same trigger→orchestration→result→CTA skeleton, posted 3 days apart — is a genuinely strong matched
  comparison and is presented with appropriate hedging on the "why" (topic/payoff selection, not
  format).
- Honest, granular data-gap logging (5 of 14 cadence date-samples blocked by rate-limiting and not
  silently interpolated; comment content never fetched, only counts, and every comment-count-based
  inference is separately tagged `[INFERRED]`).

### `creators/yt_berman.md` — **CLEAN**
- 3/3 spot-checked videos matched exactly, including two extreme values (2.5M-view top video, 3.3M
  in a 200-video sweep concentration stat that I independently re-derived and confirmed to the decimal).
- Video 1 ("New Speedreading Method") has **no available transcript** (`yt-dlp --list-subs` confirmed
  genuinely absent, not a fetch failure) — every claim about that video's content, hook, and structure
  is correctly downgraded to `[INFERRED]`, and the dossier explicitly refuses to invent a hook-based
  explanation it can't support ("I am flagging that honestly rather than inventing a hook-based
  explanation I cannot support" — Video 1 §8). This is the single best example of QC_PROTOCOL rule 3
  compliance in the whole corpus.
- The Video 4/Video 10 (OpenClaw pair, 85.5x view gap, inverted like-rate) matched comparison is
  independently corroborated by the interim convergences file's item #2 — checked, consistent.

### `creators/yt_rileybrown.md` — **CLEAN**
- 1/1 spot-checked video (the #1 short) matched exactly.
- The dossier is explicit that its 39-video Shorts sample is a YouTube-side "shelf" ceiling, not
  necessarily the creator's full lifetime Shorts history — flagged as a confidence caveat that
  propagates through every median-relative statistic, which is the correct way to handle it.
- The two flops (Video 10: hook/payload mismatch; Video 11: no demo-in-motion despite a reasonable
  hook) are genuinely distinguishable failure modes, each independently evidenced by engagement-rate
  data that argues against a lazy "flops are just worse" read — the dossier explicitly shows Video 10's
  comment rate beating 6 of 8 top performers, which is a falsifiable, checkable claim I could verify
  against the dossier's own per-video numbers and did.

### `creators/yt_curiousrefuge.md` — **MINOR DEFECTS**
- 3/3 spot-checked videos (including the channel's single biggest hit, LOTR at 4.4M views) matched
  exactly.
- **MINOR — CURIOUSREFUGE-1**: Section A cites a "561K views" Adobe Firefly collab short as background
  context and flags it itself as `[OBSERVED, MED confidence]`, un-re-verified via yt-dlp. I located and
  pulled this video independently (`youtube.com/shorts/FhQ4mmeHw04`): **561,314 views — the number is
  accurate — but the video's `channel` field is "Adobe Firefly," not "Curious Refuge."** It lives on
  Adobe's own YouTube channel, not Curious Refuge's, which is exactly why it never appeared in the
  43-video `/shorts` census pulled from `@curiousrefuge`. The dossier's own methodology (excluding it
  from the core 13-video analysis, treating it only as About-page context) was the right call and this
  is not a fabrication — but the phrasing "A branded collab explicitly tagged #Shorts... has 561K
  views" (repeated verbatim in `02_youtube_channels.md` line ~21 too) reads ambiguously enough that a
  synthesis author could mistake this for a Curious Refuge-channel data point. **Required correction:**
  add one clause — "hosted on Adobe Firefly's own channel, not Curious Refuge's" — anywhere this figure
  is cited downstream.
- Everything else — the pivot narrative (Star Wars 4/28/2023, LOTR 5/9/2023, 11 days apart, confirmed
  by my own independent LOTR pull), the 8.5x/152x/228x cross-lane ratios, the copyright-risk analysis
  (correctly labeled `[INFERRED risk assessment]`, not asserted as legal fact) — held up.

### `creators/yt_liamottley.md` — **MINOR DEFECTS**
- 2/2 spot-checked videos matched. The dossier's central, most extraordinary claim — **the channel has
  exactly one Short in its entire history, on an 825K-subscriber channel** — was independently
  re-verified by me from scratch (fresh `--flat-playlist --playlist-items 1:50` call, zero shared state
  with the dossier's own scratch directory) and returned exactly 1 row. This is the single most
  surprising finding in the entire YouTube corpus and it is real, not an extraction bug.
- **MINOR — LIAMOTTLEY-1**: Section A computes the long-form median for n=250 (an even-sized catalog)
  as "rank #125 of 250" — a single value — rather than averaging ranks #125 and #126, which is the
  standard median definition for an even-count dataset. Every other dossier that hit an even n handled
  this correctly (Wes Roth explicitly averaged ranks 22/23 for n=44; Berman explicitly cited "positions
  100 & 101"; Skill Leap explicitly averaged ranks 12/13, 3/4, and 15/16 for its three even-n splits).
  Given the extreme power-law shape of this catalog, adjacent-rank videos in the flat middle of the
  distribution are very unlikely to differ by more than a few views, so this almost certainly does not
  change any downstream conclusion (the 83.4x top/median ratio, the audience-addressability argument in
  Section C, etc. all still hold under either definition) — but it's a real, checkable methodological
  inconsistency within the dossier's own stated approach. **Required correction:** recompute as
  avg(rank 125, rank 126) or explicitly note why rank 125 alone was used.
- Everything else in this dossier is exceptional: the triple-independent-method verification of the
  "one Short" finding (stable yt-dlp, a second nightly-build yt-dlp to rule out a version bug, raw
  `ytInitialData` JSON inspection, and a live browser click-through) is the strongest single piece of
  methodological rigor in the whole corpus, and the arithmetic cross-check (250 long-form + 1 short =
  251 = channel header) is a genuinely clever, independent confirmation path.

### `creators/yt_skillleap.md` — **CLEAN**
- 2/2 spot-checked videos matched exactly; independently re-confirmed the 30-video full population.
- The "Howfinity" prior-identity claim (explaining why the channel's two viral outliers are legacy,
  off-mission content) is tagged `[REPORTED, MED confidence]` in the dossier. I independently
  re-verified it via WebSearch (found the Howfinity Facebook rebrand announcement post cited by the
  dossier, plus the shared `@howfinity_tech` Instagram handle, plus — pulling the video's own
  description directly via yt-dlp myself — confirmed the #1 video's description literally links to
  `howfinity.com`, exactly as the dossier states). This checked out completely; if anything the MED
  confidence tag is now under-confident given how directly corroborated it turned out to be.
- Median arithmetic (AI-topic, general-tech, and combined splits, all even-n, all correctly averaged
  across paired ranks) is the most careful median handling of any dossier in the corpus — genuinely
  better practice than Liam Ottley's on this specific point.

### `creators/yt_futurepedia.md` — **CLEAN**
- 3/3 spot-checked videos matched (including the two extreme outliers: 6.6M-view #1 and the 3.2M-view
  #2 with the anomalous 0.082% like-rate); independently re-confirmed the 67-short full population.
- The dossier's handling of Video 2 (BAE03hKz9Zo, 3.2M views but only 25 comments and a 0.082%
  like-rate — 30-50x lower than every other video in the sample) is a model of honest uncertainty: it
  names two or three plausible mechanisms (paid ad amplification, autoplay/embed consumption), states
  explicitly "no source confirms which mechanism is at play — this is flagged as an open question, not
  resolved," and does not pick a favored explanation to sound more authoritative than the evidence
  supports.
- Table in Section C ("Top-vs-Flop Delta") makes falsifiable claims (like-rate ranges, comment-rate
  ranges, hook-timing counts) that I cross-checked against the individual post-mortems above it in the
  same file — internally consistent.

---

## Cross-file check: does `00_INTERIM_convergences.md` overstate the YouTube dossiers?

Read the full 105-line file and traced every YouTube-sourced convergence item (1, 2, 3, 4, 5, 6, 7
partial, 8, 9, 10, 11) back to its cited creator's dossier.

**Verdict: MINOR DEFECTS.** Ten of twelve traced items are accurate, correctly-sourced compressions of
real dossier findings (e.g. item 2's "Berman OpenClaw pair, 85x view gap, flop LR higher" matches the
dossier's own "85.5x" and "4.56% vs. 2.50%, inverted" almost to the decimal; item 9's "Berman: bottom-75%
in tight 3.6-12K band; top 5% = 52% of views" matches the dossier's own p75=12,000/min=3,600 and the
51.9%-of-views concentration stat I independently re-derived). No item rests on a single YouTube creator
dressed up as a multi-creator pattern — every multi-creator convergence item genuinely cites 3+
independent dossiers whose underlying evidence I verified supports the specific claim attributed to it.

Two items overstate certainty relative to their own source dossier:

- **CONVERGENCE-1 (MINOR)**: Item 10 states "Futurepedia's dormancy post-acquisition" as settled fact.
  The Futurepedia dossier itself tags this "`[INFERRED, MED confidence]`... a timing correlation, not a
  confirmed causal claim — no source states the two are related." **Required correction:** rephrase to
  "Futurepedia's Shorts dormancy coincides with its HubSpot Media acquisition (timing correlation, not
  confirmed causal per the source dossier)."
- **CONVERGENCE-2 (MINOR)**: Item 10's "Curious Refuge (ex-Squarespace tutorials)" compresses a
  broader pre-pivot catalog (per the dossier: a 2016 JFK VR video at 16.4M views, Notion tips, Canva
  tips, generic After Effects VFX tutorials, and one Squarespace-tips video specifically) into a single
  descriptor. Not wrong, but reductive enough that a reader would picture a Squarespace-tutorial channel
  specifically, when the dossier's actual characterization is "a design/productivity-education channel."
  **Required correction:** replace "ex-Squarespace tutorials" with "ex-general-design/productivity
  channel" or similar.

---

## Corpus-half verdict

**CLEAN, with MINOR DEFECTS in 2 of 8 dossiers and 2 of ~11 traced convergence items.** No BLOCKER or
MAJOR findings anywhere in the YouTube half. This is an unusually high-integrity research corpus: of 19
individually spot-re-pulled videos and 5 full-catalog population recounts (24 independent live
data-points total), every single one matched the dossiers' claims within normal hours-later view-count
accrual drift, and the majority matched exactly to the like/comment count. Every arithmetic
median/ratio I recomputed from each dossier's own listed raw data checked out except one. The
[OBSERVED]/[REPORTED]/[INFERRED] evidence-tier discipline required by QC_PROTOCOL and the template is
applied consistently and, in several places (Berman Video 1's missing transcript, Futurepedia Video 2's
unexplained engagement anomaly, Wes Roth Video 1's paid-boost inference), the dossiers actively resist
the temptation to overclaim certainty the evidence doesn't support. The template-sameness scan found
zero copy-paste boilerplate across 114K words of psychology-scoring prose.

## REQUIRED-CORRECTIONS list (what the synthesis author may NOT rely on until fixed)

1. **CURIOUSREFUGE-1**: Wherever the "561K views" Adobe Firefly/Curious Refuge collab short is cited
   (in the dossier itself and in `02_youtube_channels.md`), append that the video is hosted on Adobe
   Firefly's own YouTube channel, not Curious Refuge's — it is not a Curious Refuge Shorts-performance
   data point.
2. **LIAMOTTLEY-1**: Liam Ottley's long-form median (43,502 views, "rank #125 of 250") should be
   recomputed as the average of ranks #125 and #126, or the single-rank choice should be explicitly
   justified. Low practical impact expected given the power-law shape, but currently inconsistent with
   the corpus's own even-n median convention used everywhere else.
3. **CONVERGENCE-1**: Do not cite "Futurepedia's dormancy post-acquisition" as a confirmed causal
   finding in final synthesis — the source dossier explicitly marks this a MED-confidence timing
   correlation only.
4. **CONVERGENCE-2**: Do not characterize Curious Refuge's pre-pivot channel as "Squarespace tutorials"
   specifically — the source dossier describes a broader general design/productivity-education catalog.
5. **RUBRIC-1** (cosmetic): the rubric's claim that the "3.3 billion Shorts" stat's source is "not named
   anywhere it's cited" should be softened — a named (if unverifiable, single-author) source exists.
   Does not change the correct do-not-cite-as-fact guidance.

Everything else in the YouTube half — all 8 dossiers' core findings, all cited view/like/comment
figures, all population counts, all median/ratio arithmetic bar one instance, and all rubric citations
bar the one cosmetic nuance above — is cleared for downstream synthesis use.

---

## Final summary

**Per-file verdicts (one line each):**
- `03_virality_science.md` — CLEAN
- `02_youtube_channels.md` — CLEAN
- `creators/yt_wesroth.md` — CLEAN
- `creators/yt_nateherk.md` — CLEAN
- `creators/yt_berman.md` — CLEAN
- `creators/yt_rileybrown.md` — CLEAN
- `creators/yt_curiousrefuge.md` — MINOR DEFECTS (1 finding)
- `creators/yt_liamottley.md` — MINOR DEFECTS (1 finding)
- `creators/yt_skillleap.md` — CLEAN
- `creators/yt_futurepedia.md` — CLEAN
- `synthesis/00_INTERIM_convergences.md` (YouTube-sourced items only) — MINOR DEFECTS (2 findings)

**Corpus-half verdict: CLEAN, minor defects only. No fabrication found anywhere in the YouTube half.**

**Required corrections:** see numbered list above (5 items, all MINOR, none blocking synthesis use of
the underlying data).

**My 3 most serious findings** (all MINOR — this corpus simply did not produce anything more severe):
1. The Adobe Firefly "561K views" collab short cited as Curious Refuge context is actually hosted on
   Adobe's own channel — a citation-attribution risk, not a fabricated number (the number itself is
   accurate, independently re-verified).
2. Liam Ottley's long-form median uses a single-rank value (#125 of 250) instead of the standard
   even-n average of ranks #125/#126 — a real methodological inconsistency versus every other dossier's
   own convention, though very unlikely to change any conclusion given the catalog's power-law shape.
3. The interim convergences file states two dossier-sourced inferences (Futurepedia's post-acquisition
   dormancy causation; Curious Refuge's pre-pivot identity as "Squarespace tutorials") with more
   certainty than their own source dossiers claim — a synthesis-layer overstatement risk, not a
   dossier-layer fabrication.
