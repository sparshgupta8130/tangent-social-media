# Creator Dossier: Sebastien Jefferies (Instagram @sebastien)

**Assignment status:** SEED account (user-provided). Held to standard QC per `QC_PROTOCOL.md`.

**Analyst method:** Primary data is the already-harvested `ig_harvest/sebastien.md` (live Instagram
pull, read-only, dated 2026-07-25) — this dossier does not re-scrape Instagram (browser tools were
reserved by another agent this session). Cross-platform verification/transcripts obtained via
`yt-dlp` against TikTok (`@sebastienjefferies`) and two YouTube channels, plus `WebSearch`/`WebFetch`
for funnel/business context. All dates below are 2026 unless stated otherwise. Every claim is tagged
`[OBSERVED]` / `[REPORTED]` / `[INFERRED]` per the mandatory template.

---

## A. Account header

| Metric | Value | Source | As-of | Confidence |
|---|---|---|---|---|
| Followers | **777K** | `ig_harvest/sebastien.md` (live IG pull) | 2026-07-25 | HIGH |
| Following | 847 (og:description) vs 759 (header) — minor cache-lag discrepancy, both `[OBSERVED]` on the same page | same | 2026-07-25 | HIGH (value), MED (which is current) |
| Posts | 1,102 | same | 2026-07-25 | HIGH |
| Bio | "Where creators come to learn AI 🧩 / info@sebastienjefferies.com / Create your own AI Character in 7 days -> www.skool.com/aicreatorlab/about" | same | 2026-07-25 | HIGH |
| Median reel views (n=30, most recent tiles) | **140K** | same, computed from grid | 2026-07-25 | HIGH |
| Top 5 by views | DaAlMicsiBD 2.4M, DVylvZbDGTo 1.6M, DYSWrorMzBA 1M, DW_VCbrDPWM 950K, DWotUKUjJq2 922K | same | 2026-07-25 | HIGH |
| Bottom 2 (flops, excl. 3 most-recent tiles per harvest methodology) | DaffjwFsX85 19.9K, DaiKv3Ls_tT 21.5K | same | 2026-07-25 | HIGH |
| Top/median ratio | 17.1x | computed | 2026-07-25 | HIGH |
| Median/follower ratio | 18% | computed | 2026-07-25 | HIGH |
| Pinning | None detected — spikes scattered through grid, not concentrated at top | same | 2026-07-25 | MED (heuristic, not date-confirmed for every tile, but the 7 detail-pulled tiles' dates are consistent with organic scatter, not a pin cluster) |

**Cadence caveat [OBSERVED + flagged inconsistency]:** the harvest's grid-position ordering does not
cleanly track post date for this account. Of the 7 videos with confirmed dates in this dossier,
grid position 1 (nominally "most recent") is dated **May 13**, while grid positions 9–10 (nominally
older, further down the grid) are dated **July 7–8** — i.e., *more recent* than position 1. This
means grid position cannot be trusted as a recency proxy for `@sebastien` the way it can for
strictly-chronological accounts in this study; only the 7 explicitly-dated tiles are treated as
reliable dates below. This is a methodology note for future harvests of this account, not a
correction to the underlying stats (views/likes/comments are unaffected).

**IG native posting cadence:** cannot be established with confidence — the only 7 dated data points
(Mar 12, Apr 2, Apr 11, May 13, Jun 25, Jul 7, Jul 8) were selected for top-5/flop-2 relevance, not
cadence sampling, and are too sparse/biased to infer a rate. **DATA GAP.**

**Cross-platform cadence proxy [OBSERVED via yt-dlp, 2026-07-25]:** TikTok `@sebastienjefferies`
posted ~120 videos sampled from Apr 2025–Jul 2026, averaging roughly one post every 4–7 days, with
two multi-week gaps (~Dec 22, 2025–Jan 13, 2026, ~3 weeks, likely holiday break; ~Mar 19–Apr 8, 2026,
~3 weeks). Whether Instagram mirrors this rhythm exactly is unconfirmed — **DATA GAP** — but it is
the best available proxy for overall content-production rhythm.

### Cross-platform footprint
- **Instagram @sebastien** (primary, this dossier) — 777K `[OBSERVED]`.
- **Instagram @sebastienjefferies** (secondary/legacy) — 270 followers, bio literally states "Main
  Account @sebastien" `[OBSERVED, ig_harvest/00_INDEX.md]` — dormant, not analyzed further.
- **TikTok @sebastienjefferies** — 558.3K followers, ~7M cumulative likes `[REPORTED, search-indexed
  profile meta via `00_seed_accounts.md`, MED confidence — a live yt-dlp pull in this session could
  not surface `channel_follower_count` for TikTok (extractor returns `NA` for this field), so the
  figure is carried forward from the prior harvest pass, not independently re-verified this session]`.
  Confirmed via this session's own crawl: TikTok is **structurally a much smaller distribution
  channel** than IG for this creator — see Section C for the per-video view-count gap (as wide as
  ~180x on one matched pair).
- **YouTube — two channels, distinct roles:**
  - `youtube.com/c/SebastienJefferies` — the original, personal, long-form/tutorial channel (dates
    back to Nov 2020 per `[REPORTED, 00_seed_accounts.md, LOW-MED]`); catalog `[OBSERVED via yt-dlp
    flat-playlist, 2026-07-25]` runs from old editing-tips content (Premiere Pro, Lightroom,
    "How To Post High Quality Instagram Reels In 2022") through current AI-tool tutorials (Kling 3.0,
    Seedance 2.0, Nano Banana Pro), confirming the niche-pivot story from general editing creator to
    AI-tools educator.
  - `youtube.com/@sebintel` ("Seb Intel") — a separate, newer channel, Shorts-only (no `/videos` tab)
    `[OBSERVED]`; per `[REPORTED, WebSearch result summarizing the channel's own framing]` this is a
    **fully AI-generated/automated pipeline channel** (scripting, avatar, voice, editing, publishing)
    that Sebastien "oversees but doesn't film" — functions as a live proof-of-concept for the
    "faceless AI brand" module he sells in AI Creator Lab.
- **X/Twitter @SebJefferies, Threads @sebastienjefferies, LinkedIn /in/sebastienjefferies/,
  newsletter sebtips.kit.com, business site sjorigin.com** — all `[REPORTED, 00_seed_accounts.md /
  WebFetch this session]`, not deep-dived (out of scope; IG is the seed platform).

### Funnel map
- **Primary in-video mechanic (6 of the 7 analyzed videos):** "Comment [KEYWORD] and I'll send you
  [the link/prompt/guide]" `[OBSERVED across the harvest's own detail pulls]` — a comment-triggered
  DM-capture pattern consistent with the ManyChat-style mechanic documented in
  `03_virality_science.md` §3.4.3. **Whether an actual automation tool (ManyChat or IG's native
  "reply-to-comment" automation) executes the DM, versus manual replies, was not independently
  confirmed** — TikTok comment-thread extraction failed in this session (yt-dlp's TikTok extractor
  did not return a `comments` array for this build; see Method log) and IG comment threads were not
  accessible without the reserved browser tools. **DATA GAP** on the automation-tool question
  specifically; the CTA *pattern* itself is fully `[OBSERVED]`.
- **Bio link (secondary/passive path):** `skool.com/aicreatorlab/about` — the only persistent
  bio-link CTA; most individual reels do not verbally reference "link in bio," relying instead on the
  per-video comment mechanic as the primary conversion path (see Section D).
- **AI Creator Lab (paid Skool community):**
  - Pricing: **$57/mo founding rate (300 spots), rising to $79/mo** `[OBSERVED via WebFetch,
    skool.com/aicreatorlab/about, 2026-07-25]` — matches the assignment brief's stated range exactly.
    A separate landing page (`sjorigin.com`) lists a *different* founding tier — **$67/mo (150 spots)
    rising to $87/mo** `[OBSERVED via WebFetch, sjorigin.com, 2026-07-25]`. This is a genuine
    cross-source discrepancy, not a typo on this dossier's part; most likely explained by different
    marketing pages reflecting different points in a rolling founding-cohort promotion, but the two
    sources were not reconciled — logged honestly rather than picking one.
  - 7-day free trial, cancel anytime `[OBSERVED, skool.com]`.
  - Member count: **265–287 active members** across two independent snapshots (skool.com's own page
    showed 265; a third-party review site `skoolmakers.com` showed 287) `[OBSERVED/REPORTED, both
    WebFetch 2026-07-25, MED]` → implies roughly **$15K–23K MRR** at listed pricing `[INFERRED, simple
    multiplication, MED-LOW confidence since both the member count and the applicable per-member
    price tier are ranges, not exact]`.
  - Curriculum `[OBSERVED, skool.com/aicreatorlab/about]`: 7-day AI-character quick-start course,
    weekly live coaching calls, an expanding prompt/template library with weekly tool updates,
    discounts up to 60% on AI tools, and a $1,000 cash-prize contest pool.
  - Founder framing `[OBSERVED/REPORTED]`: positions itself on Sebastien's claimed brand work with
    Google, Meta, Samsung, Adobe, TikTok, X, DJI (self-reported, `sjorigin.com`, not independently
    confirmed by any brand-side source — LOW-MED confidence on the credential itself) and a claim of
    having grown "a faceless AI account to 300K followers" using the taught system — the **platform
    for that 300K claim is never specified in any source found**, a pre-existing DATA GAP carried
    forward from `00_seed_accounts.md`.
- **Funnel shape:** Reel/Short hook (usually a specific AI tool/model demo) → comment keyword → DM
  with link/prompt/guide → (implied, not directly observed) newsletter or Skool trial → $57–79/mo
  membership. This is a **single-hop, per-video** funnel design — contrast with e.g. `nateherkai` in
  this same study, whose funnel is two-hop (Short → long-form YouTube video → Skool), per
  `creators/yt_nateherk.md`. Sebastien's design makes every individual reel a standalone lead-capture
  unit rather than routing traffic through an intermediate content layer.

---

## B. Video post-mortems (7 videos: top 5 by views + 2 flops)

**Selection method:** the 7 videos below are exactly the 7 reel-detail pulls already performed by the
IG harvest agent (`ig_harvest/sebastien.md`), which itself selected the account's top 5 by view count
and bottom 2 (excluding the 3 most-recent tiles, to avoid unfairly flagging still-accruing posts as
flops). This dossier did not re-select a different sample — it deepens analysis on the harvest's own
selection, per the assignment brief's instruction to analyze exactly this set.

**Cross-post matching result (see Method log for full search trail):** 5 of 7 videos have a confirmed
TikTok cross-post (exact caption match, and in 4 of 5 cases an exact date match) — full verbatim
transcripts obtained for 4 of those 5 (the 5th, DW_VCbrDPWM's TikTok twin, is a 7-second clip with no
spoken dialogue and no subtitle track). 2 of 7 (DYSWrorMzBA, DWotUKUjJq2) have **no cross-post found**
on TikTok or either YouTube channel after an exhaustive search — logged as DATA GAP, analyzed from
caption + stats + established account-format patterns only.

---

### VIDEO 1 (TOP #1, 2.4M views): "20M views. 1 AI filmmaker."

#### 0. Identity & stats
- Shortcode `DaAlMicsiBD`. Platform: Instagram Reels. Posted **Jun 25, 2026** `[OBSERVED,
  ig_harvest/sebastien.md, HIGH]`.
- IG: 2.4M views, 435 likes, 193 comments `[OBSERVED, HIGH]`.
- Cross-platform proxy: TikTok video `7655313528919788802`, posted the **same date** (Jun 25, 2026),
  76s long, 301K views, 29.4K likes, 111 comments, 232 reposts `[OBSERVED via yt-dlp, 2026-07-25]`.
  Exact caption match confirms this is the same underlying content (case study of AI filmmaker "PJ"
  using Dreamina Octo/Seedance 2.0), used here as a transcript proxy per QC protocol §"cross-post"
  rule.
- Rank: **#1 of the account's top 5** by views; 17.1x the account's 140K median.
- **Flagged stat anomaly:** IG like-rate is **0.018%** (435/2.4M) — the single lowest like-rate of
  any of the 5 top videos in this sample, despite having the highest view count. The TikTok twin's
  like-rate is 9.8% (29.4K/301K) — over 500x higher on a per-view basis despite 8x fewer raw views.
  This is the widest engagement-rate gap between IG and TikTok versions of any matched pair in this
  dossier. See Section C for the account-wide pattern this fits into.

#### 1. Packaging
- Caption: "20M views. 1 AI filmmaker. And a workflow that's changing how cinematic AI films are
  made. Comment 'BTS' and I'll send it over." `[OBSERVED]`.
- Curiosity gap: opens on someone **else's** proven stat (20M views) as borrowed social proof before
  revealing what this video itself will show — a "credibility transfer" packaging move distinct from
  the account's more common "here's a tool" framing.
- The TikTok description (identical core text, `[OBSERVED]`) carries additional hashtags not present
  in the IG caption's visible portion: `#MadeWithDreaminaAI #PJ #DreaminaSeedance2 #DreaminaAI
  #AIvideo`. This reads as at minimum an earned/incentivized case-study relationship with Dreamina
  (ByteDance's AI creative suite) `[INFERRED — the hashtag density and repeated product naming suggest
  a brand tie-in, though no explicit "#ad" or "paid partnership" disclosure is present on either
  platform's visible caption]`.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via TikTok transcript]`: **"Alright, this video just got 20 million views. And
  the crazy part is it was made in just two weeks by one of the best AI filmmakers in the world. And
  I'm gonna show you exactly how he did it."**
- Hook taxonomy: **bold claim + "insider access"** hybrid — leads with someone else's proven result,
  then promises to reveal the hidden mechanism (a variant of "nobody talks about X," per
  `03_virality_science.md` §3.1, applied to a process rather than a fact).
- What the viewer sees: `[DATA GAP]` — no frame-level video review was performed (method is
  transcript + metadata only, consistent with the validated approach used across this study); likely
  opens on footage from the finished AI film itself, given the 0:10 line ("first thing you'll notice
  is the character quality") implies something is already visible on screen, but this is `[INFERRED]`,
  not confirmed.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via transcript, timestamps as given]`:
  - [0:00] Hook: 20M-view claim + 2-week build-time claim.
  - [0:10] Directs attention: "the first thing you'll notice is the character quality."
  - [0:19] Technique reveal: "ingredient-based workflow" in Dreamina AI.
  - [0:36] Problem framing: "the problem with AI filmmaking is... consistency is extremely hard."
  - [0:46] Open loop planted: "if you stick around till the end, I'll send you the exact guide."
  - [0:49] Second workflow stage: Dreamina Seedance 2.0 for cinematic motion/continuity.
  - [1:00] Reframe: AI as "creative partner," not just an asset generator.
  - [1:09] CTA/loop close: "comment BTS and I'll send it over."
- One-idea-per-video: yes (the ingredient-based Dreamina workflow), told as a case study.
- Payoff placement: **drip, then externally gated** — the video never actually delivers the "exact
  guide" it promises at 0:46; the loop technically closes into an off-platform DM step, not an
  on-screen resolution. Worth flagging structurally: viewers who want the full payoff must leave the
  video's own narrative arc unresolved and take an off-platform action.
- Pacing: `[DATA GAP]` — cut frequency not observable without frame-level review; `[INFERRED]` from
  genre (narrated screen-capture case study, consistent with the account's other case-study-style
  videos) that pacing is a steady demo-reel montage, not a talking-head format.
- Loop/rewatch design: none apparent — linear explainer, not built for rewatching.

#### 4. Value proposition
- Walk-away value: tool-name discovery (Dreamina Octo, Dreamina Seedance 2.0) + a workflow *concept*
  (build ingredients — characters/locations/props/styles — individually before combining) +
  aspiration (association with "one of the best AI filmmakers in the world").
- Practical value class: tool discovery (primary) + conceptual workflow (not literally demonstrated
  step-by-step) + aspiration.
- Specificity: **MED** — names the specific product suite and the conceptual workflow shape, but does
  not show an actual prompt, UI walkthrough, or literal step sequence within the free 76s; the "exact
  guide" is explicitly withheld behind the comment CTA, meaning the public video is intentionally
  under-specified to manufacture DM-funnel dependency.

#### 5. Psychology scoring
- STEPPS: **Social Currency** is the dominant pillar — being able to say "I know the actual method
  behind that 20M-view AI film" confers insider status independent of ever using the technique.
  **Practical Value** is present but incomplete/gated. **Emotion**: awe/amazement at the borrowed
  stat, transferred to admiration for the enabling tool — high-arousal positive per Berger & Milkman
  (§2.3).
- Primary emotion: awe (vicarious, borrowed from a third party's achievement).
- Identity-signaling: sharing this says "I follow serious AI filmmaking, not toy demos."
- Save/send trigger: MED — informational/reference value is real but capped by the video's own
  incompleteness (no literal prompts shown on-screen).

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'BTS' and I'll send it over" `[OBSERVED]` — classic comment-keyword-to-DM
  mechanic (§3.4.3).
- 193 IG comments on 2.4M views = **0.008% comment rate** — the lowest comment-conversion rate of the
  5 top videos, despite the video's entire second half being built around driving that comment. This
  is consistent with the low like-rate finding: a large share of this video's 2.4M "views" appear to
  come from low-intent/passive-reach audiences who did not register (or act on) the 1:09 CTA.
- Funnel position: top-of-funnel discovery bait using a **third party's** proven virality (not
  Sebastien's own) as the entry hook, funneling toward Sebastien's own guide/DM list and, eventually,
  AI Creator Lab.

#### 7. Replicability verdict
- Template: (1) source a genuinely viral third-party AI creation and get access to its creator, (2)
  narrate a conceptual workflow breakdown over screen-capture, (3) name the specific tool prominently,
  (4) gate the literal step-by-step behind a comment CTA.
- Commodity: the narration/explainer format is fully replicable. Unfair advantage: access to the
  original filmmaker (PJ) and an apparent tool-partnership relationship with Dreamina — not something
  Tangent could replicate without a comparable case-study relationship.
- Difficulty for Tangent: **MED** — the format itself is executable solo, but sourcing an equally
  impressive third-party case study (and any accompanying tool-maker relationship) raises the floor
  above pure solo execution.

#### 8. Why it won (or underperformed on engagement, despite leading on views)
- Single most load-bearing reason: **borrowed virality** — opening on someone else's already-proven
  20M-view result establishes stakes far beyond what any of Sebastien's own cold demos could claim,
  functioning as pre-validated social proof.
- Secondary factors: a currently-hyped tool (Dreamina/Seedance 2.0 — actively covered by third-party
  AI-industry blogs during this pull window, see Video 5's sourcing), likely amplified distribution
  from a tool-maker relationship (the Dreamina-specific hashtags suggest bidirectional promotion).
- Caveat: the video's own IG like-rate (0.018%) is dramatically below what its view count would
  predict, and is the *lowest* of the account's 5 top reels — a pattern consistent with broad
  passive-reach distribution rather than deep audience resonance. By engagement-rate standards, this
  is arguably the *weakest* of the 5 "top" videos despite ranking #1 by raw views — see Section C.

#### Sources
- `ig_harvest/sebastien.md`
- TikTok video 7655313528919788802, `https://www.tiktok.com/@sebastienjefferies/video/7655313528919788802` (yt-dlp metadata + `eng-US` auto-subtitle transcript, pulled 2026-07-25)

---

### VIDEO 2 (TOP #2, 1.6M views): "Changing the style of a video like this would take hours..."

#### 0. Identity & stats
- Shortcode `DVylvZbDGTo`. Posted **Mar 12, 2026** `[OBSERVED]`.
- IG: 1.6M views, 379 likes, 95 comments `[OBSERVED]`.
- TikTok twin: `7616407657204780310`, posted the **same date** (Mar 12, 2026), 35s, **1.9M views**,
  2,074 likes, 86 comments, 107 reposts `[OBSERVED via yt-dlp]` — notably, this is the *only* one of
  the 5 matched pairs where the TikTok version out-performed the IG version by raw views (1.9M vs
  1.6M), suggesting this specific hook/content resonated on its own merits across platforms rather
  than being an IG-algorithm-specific favorite.
- IG like-rate: 0.024% (379/1.6M). TikTok like-rate: 0.109% (2,074/1.9M) — still low by general
  social-video norms but the smallest IG/TikTok engagement-rate gap of the three matched top videos.

#### 1. Packaging
- Caption: "Changing the style of a video like this would take hours... You'd need VFX skills,
  complex masks, lighting tweaks, maybe even a full CGI pipeline. Now AI can do it in minutes. Comment
  'AI' and I'll send the tool so you can test it." `[OBSERVED]` — matches the TikTok description
  almost verbatim, confirming a true cross-post rather than a similar-topic coincidence.
- Curiosity gap: sets up a labor/skill contrast (hours of specialist VFX work) before the reveal
  (AI does it in minutes) — a before/after value-gap frame.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via TikTok transcript]`: **"This is a brand new workflow that allows you to
  completely restyle any video to whatever you want, and it's absolutely insane."** (auto-caption
  rendered "restyle" as "restart" in one instance — transcript corrected here based on context and
  the caption's own wording.)
- Hook taxonomy: **bold claim** ("brand new," "absolutely insane") blended with **demo-in-motion**
  (the transformation itself is the payoff, shown immediately after the claim).
- What the viewer sees: `[DATA GAP, no frame review]` — `[INFERRED]` a before/after or live restyle
  demo given the entire caption's framing is built around a visible transformation.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via transcript]`:
  - [0:00] Bold-claim hook.
  - [0:07] Tool name reveal: "Ray3.14... Luma... Modify Video."
  - [0:13] Feature explainer: guided frame + intensity/strength slider.
  - [0:21] Payoff: "the agent will restyle your video, keeping your original motion intact."
  - [0:26] Drip use-case list: swap characters, change environment, relight scenes.
  - [0:31] CTA: "comment AI and I'll send it over."
- One-idea-per-video: yes. Payoff placement: **front/mid-loaded** — unlike Video 1, the actual
  mechanism (tool name + concrete steps: upload → Modify Video → guided frame → strength slider →
  create) is shown in full within the free video; nothing essential is withheld behind the CTA except
  the literal tool link itself.
- Pacing: `[DATA GAP]`, `[INFERRED]` steady screen-capture demo, consistent with the account norm.
- Loop/rewatch design: none — linear demo.

#004. Value proposition
- Walk-away value: named tool (Luma Ray3.14) + literal usable steps + a vivid contrast framing (VFX
  pipeline → AI in minutes).
- Practical value class: tool discovery + copyable workflow — genuinely higher specificity than Video
  1: this names the exact product, the exact menu action ("Modify Video"), and the exact controls
  (guided frame, strength slider).
- Specificity: **HIGH** relative to the account's norm — closer to a literal mini-tutorial than Video
  1's conceptual case study.

#### 5. Psychology scoring
- STEPPS: **Practical Value** is dominant here (a real, immediately usable tool + steps), with
  **Social Currency** as a secondary layer (the "VFX skills replaced by AI" framing flatters early
  adopters who can now do professional-grade work without professional training).
- Primary emotion: awe/amazement at the transformation's apparent ease ("absolutely insane").
- Identity signal: "I know the shortcut around a skill most people think requires years of training."
- Save/send trigger: HIGH — this is exactly the "news you can use" pattern §2.7 flags as
  disproportionately saved; a viewer with video-editing needs has an obvious reason to bookmark this.

#### 6. CTA & funnel mechanics
- "Comment AI and I'll send it over" `[OBSERVED]`. 95 comments / 1.6M views = 0.006% — again low in
  absolute conversion terms relative to view count, reinforcing the broad/passive-reach read that
  applies across most of this account's highest-view videos (DW_VCbrDPWM, Video 4, is the exception).
- Funnel position: top-of-funnel tool-discovery bait; generic and repeatable — unlike Video 1, this
  format does not require any third-party relationship, just a Luma Labs account and a demo clip.

#### 7. Replicability verdict
- Template: pick a newly-released or newly-trending creative AI tool → show a clear before/after or
  labor-contrast framing → name the exact product and menu path → CTA-gate the link only (not the
  method itself).
- Commodity: entirely — no special access required. Unfair advantage: minimal; this is close to
  Sebastien's most replicable format in the sample.
- Difficulty for Tangent: **LOW** — requires only early access to/awareness of a trending creative AI
  tool and a demo clip; no relationships, no proprietary content.

#### 8. Why it won
- Single most load-bearing reason: rode a **specific, newly-relevant tool** (Luma's Ray3.14) with an
  unusually strong labor-contrast framing ("hours of professional VFX work → minutes"), maximizing
  the perceived value gap — a textbook application of the trending-tool-early-adoption principle
  (§3.3.3, adapted from audio to tools).
- Secondary factor: unlike Video 1, this is the one top video where the **TikTok twin actually
  out-performed the IG original** by raw views, suggesting the hook/content is unusually strong on its
  own terms across platforms, not merely favored by IG's specific distribution algorithm that week —
  a stronger signal of genuine content-market fit than Video 1's more one-sided IG performance.
- No luck/timing components beyond general tool-launch-window timing could be confirmed; no evidence
  of paid promotion or trend-surfing beyond the tool's own release cycle.

#### Sources
- `ig_harvest/sebastien.md`
- TikTok video 7616407657204780310, `https://www.tiktok.com/@sebastienjefferies/video/7616407657204780310` (yt-dlp metadata + transcript, 2026-07-25)

---

### VIDEO 3 (TOP #3, 1M views): "The fastest way to create insane YouTube thumbnails"

#### 0. Identity & stats
- Shortcode `DYSWrorMzBA`. Posted **May 13, 2026** `[OBSERVED, ig_harvest]`.
- IG: 1M views, 395 likes, 247 comments `[OBSERVED]`. Like-rate: 0.0395%. Comment rate: 0.0247% (the
  second-highest *absolute* comment count of the 5 tops, after Video 4).
- **No cross-platform copy found.** See Method log for the full search trail (TikTok grid scanned
  ~120 items spanning Apr 2025–Jul 2026 with no title/date match; both YouTube channels' full
  catalogs checked with no "thumbnail" title anywhere). **DATA GAP: no verbatim transcript
  obtainable.** All hook/structure analysis below is built from the IG caption + stats + the
  established format pattern confirmed across the other 4 transcribed videos in this account's
  catalog, and is explicitly `[INFERRED]` where noted.

#### 1. Packaging
- Caption (full, per harvest): "This is the fastest way to create insane YouTube thumbnails in
  seconds with AI. Comment AI for the full guide" `[OBSERVED]` — the harvest's own note flags this as
  the **shortest/most terse** hook of the 5 top performers.
- Curiosity gap: double superlative ("fastest," "insane") + speed claim ("seconds") with no named
  tool — maximal curiosity gap given zero information about *how*.

#### 2. Hook (0–3s)
- No verbatim transcript available — `[DATA GAP]`.
- Hook taxonomy `[INFERRED from caption text alone]`: **bold claim / speed-superlative** — reads as
  a tool-agnostic promise, distinct from Videos 1–2's explicit early tool-naming.
- What the viewer sees: unknown — `[DATA GAP]`.

#### 3. Structure & retention engineering
- `[INFERRED from the account's consistent format across the 4 verified/transcribed videos]`: almost
  certainly follows the established skeleton — hook claim → tool name reveal → 2–4 step screen-capture
  demo → CTA gated behind "comment AI." This inference is justified because every transcribed video
  from this account follows this exact skeleton with no exceptions observed in this sample, but it
  remains an inference, not an observation, for this specific video.
- Beat map: cannot be produced without a transcript — `[DATA GAP]`.
- Pacing/loop design: unknown — `[DATA GAP]`.

#### 4. Value proposition
- Walk-away value: `[INFERRED]` likely a named AI thumbnail-generation tool + a short demo, per the
  account's established pattern.
- Practical value class: tool discovery (inferred).
- Specificity: **cannot be scored** without knowing which tool is shown — `[DATA GAP]`. A WebSearch
  for "Sebastien Jefferies YouTube thumbnails AI" surfaced only generic third-party AI-thumbnail SEO
  content (Pikzels, Thumbmagic, ThumbnailCreator, Thumber, WayinVideo) — **none of these are confirmed
  to be the tool used in this specific video**; they are listed only to show the product category
  exists, not as identification of Sebastien's actual tool choice.

#### 5. Psychology scoring
- STEPPS: **Practical Value** is likely dominant — YouTube thumbnails are a near-universal creator
  pain point (broader addressable relevance than a niche VFX trick), which may explain the relatively
  high comment count despite a modest like-rate. **Triggers/anxiety**: thumbnails directly gate
  YouTube CTR, a topic creators are chronically anxious about — plausible FOMO-adjacent driver.
- Cannot score emotion/arousal precisely without the verbatim delivery — `[INFERRED, MED confidence]`
  the caption's tone (terse, confident, no case-study framing) suggests a flatter, more utility-driven
  register than Videos 1–2.

#### 6. CTA & funnel mechanics
- "Comment AI for the full guide" `[OBSERVED]` — the same mechanic as the majority of this account's
  catalog.
- Funnel position: top-of-funnel tool-discovery bait, standard pattern.

#### 7. Replicability verdict
- Template `[INFERRED]`: identify a genuine creator pain point with a large addressable audience
  (packaging/thumbnails, not a niche VFX trick) → terse, no-fluff hook → named tool demo → CTA gate.
- Commodity vs. unfair advantage: cannot be assessed without knowing the specific tool shown —
  `[DATA GAP]`.
- Difficulty for Tangent: **LOW–MED** (topic itself is broadly accessible; specific execution
  unconfirmed).

#### 8. Why it likely won
- `[INFERRED, MED confidence]`: **topic breadth** — "YouTube thumbnails" addresses a near-universal
  creator problem, unlike the account's narrower VFX/niche-tool content, giving it a larger
  addressable audience within the AI-creator-tools niche. The hook's terseness (shortest of the 5
  tops, per the harvest's own note) may also read as higher-confidence/lower-friction than the
  account's longer case-study-style captions (Video 1) — consistent with the general finding that
  unnecessary preamble costs retention (§2.6.2), though this video's caption has essentially none to
  begin with.
- This assessment is **inference-heavy and should be weighted accordingly** — it is the least
  evidentially supported of the 5 top-video post-mortems in this dossier, purely due to the absence of
  any cross-platform copy.

#### Sources
- `ig_harvest/sebastien.md` (sole source; no cross-platform copy located — see Method log)

---

### VIDEO 4 (TOP #4, 950K views): "Breaking the barrier between what's real and what's not"

#### 0. Identity & stats
- Shortcode `DW_VCbrDPWM`. Posted **Apr 11, 2026** `[OBSERVED]`.
- IG: 950K views, **61K likes**, 1,789 comments `[OBSERVED]`. Like-rate: **6.4%** — by far the highest
  of any video in this sample, roughly 260x Video 1's rate and ~100x Video 2's rate.
- This is the flagged anomaly from `ig_harvest/00_INDEX.md` and `ig_harvest/sebastien.md`. **Status:
  CONFIRMED, not a data artifact** — the harvest file's own "Anomaly re-verification" section
  (added between this dossier's initial read and its finalization, per the assignment's instruction
  to check) re-pulled the reel fresh on 2026-07-25 and got an **exact match** (61K likes, 1,789
  comments, same date). The re-verification's own read: both likes AND comments are elevated together
  (unlike an ad-boost signature, which shows huge views paired with *near-zero* likes/comments) — the
  shape is genuine outsized organic virality, not a metrics-sync glitch or paid-boost artifact. No
  "#ad"/paid-partnership indicator is visible in the caption.
- TikTok cross-post: `7630445809162652950`, posted **Apr 19, 2026** — an **8-day gap** from the IG
  date (the only one of the 5 matched pairs without an exact date match, though the caption is
  identical, confirming it as the same content re-posted slightly later). Only **7 seconds** long,
  5,229 views, 141 likes, 12 comments, 6 reposts `[OBSERVED via yt-dlp]`. No subtitle track exists for
  this clip (confirmed via `--list-subs`) — consistent with a very short, dialogue-free visual demo.
- **Cross-platform view gap: ~182x** (950K IG vs. 5,229 TikTok) — the widest gap of any matched pair
  in this dossier, suggesting this specific piece of content found outsized resonance specifically
  within Instagram's distribution/audience, not a generically strong format that would travel equally
  well to TikTok.

#### 1. Packaging
- Caption (identical across both platforms, confirmed via WebFetch/yt-dlp description comparison):
  "comment 'AI' for the prompt — Breaking the barrier between what's real and what's not, this was
  created with Seedance 2, the latest AI video model. Tutorial coming soon. save this post for later"
  `[OBSERVED]`.
- Curiosity gap: the "real vs. not real" framing is a direct uncanny-valley hook — promises the
  viewer's own perception will be challenged, the strongest curiosity-gap type in this sample (per
  Loewenstein §2.1.1: partial information — "this looks real, it isn't" — with the mechanism withheld).

#### 2. Hook (0–3s)
- No spoken dialogue; `[DATA GAP]` on exact visual content (no frame-level review performed).
  `[INFERRED, based on duration and caption]`: at 7 seconds, this is almost certainly a single
  continuous AI-generated clip shown cold, likely with on-screen text carrying the caption's core line,
  functioning as pure spectacle rather than tutorial.
- Hook taxonomy: **demo-in-motion** — the finished, uncanny-realistic clip IS the hook, with zero
  narrative setup (distinct in kind from Videos 1–3, which are all narrated 30–80s explainers).

#### 3. Structure & retention engineering
- `[INFERRED from duration/format]`: effectively no "structure" in the multi-beat sense used
  elsewhere in this dossier — a near-pure single-shot demo with caption-only context. This is
  structurally the simplest video in the entire sample.
- One-idea-per-video: trivially yes (there is only one idea, shown once).
- Payoff placement: the payoff (an uncanny-realistic AI clip) is front-loaded and IS the entire video
  — no drip, no build.
- Pacing/loop design: `[DATA GAP]` for pacing internals within the 7s; no loop/rewatch mechanism
  apparent from caption alone.

#### 4. Value proposition
- Walk-away value: pure spectacle/demo value (a striking AI clip) + a named tool (Seedance 2) rather
  than an in-video lesson — viewer reaction is "is this real?" not "here's how I'd do this."
- Practical value class: news/reveal (a new model's capability ceiling) + entertainment/awe, with
  tool-discovery as a secondary, name-only layer (no workflow shown).
- Specificity: **LOW** within the video itself (no visible steps — explicitly deferred: "tutorial
  coming soon") but **HIGH intent-to-convert** (the prompt is the entire commented-for offer).

#### 5. Psychology scoring
- STEPPS: **Emotion** is the clearly dominant pillar here — "breaking the barrier between what's real
  and what's not" is squarely the Berger & Milkman high-arousal-awe mechanism (§2.3), and unlike
  Videos 1–3, the emotional hit appears to be the *primary* vector, not a byproduct of a tutorial.
  **Social Currency** is also strong: sharing an "is this even real" clip is inherently
  status-conferring (I found the thing that fooled me).
- Primary emotion: **awe / uncanny amazement** — the clearest, least-diluted example of this emotion
  in the entire 7-video sample.
- Save/send trigger: explicit — the caption literally instructs "save this post for later," directly
  invoking the saves mechanism §2.7 identifies as an algorithmically weighted signal.

#### 6. CTA & funnel mechanics
- "Comment 'AI' for the prompt" `[OBSERVED]`. **1,789 comments is the highest absolute comment count
  of any video in this sample** (nearly 4x Video 3's 247, and roughly 16x Video 5's 110) — consistent
  with a video whose entire content essentially IS the trigger for a reaction/comment, with nothing
  else to parse in 7 seconds except "how did you make this."
- Funnel position: top-of-funnel spectacle bait, explicitly deferring the tutorial ("tutorial coming
  soon") — this video's job is pure reach/reaction generation, with the actual workflow content
  planned as a *future* piece, an unusually explicit example of splitting spectacle and instruction
  into separate posts.

#### 7. Replicability verdict
- Template: source a genuinely uncanny/impressive output from a cutting-edge model release → post it
  with minimal framing and a direct "is this real" caption → explicitly defer the tutorial to a later
  post → CTA-gate the prompt only.
- Commodity: the *format* (short spectacle clip + deferred tutorial) is replicable by anyone with
  access to the underlying model (Seedance 2 at the time of its release window). Unfair advantage:
  early access to a hyped, newly-released model capable of producing convincingly uncanny output —
  a moving target that requires staying current on model releases, not a durable one-time asset.
- Difficulty for Tangent: **MED** — requires both early awareness of a qualifying model release and a
  genuinely striking output (not every generation from a new model will clear the "is this real" bar).

#### 8. Why it won
- Single most load-bearing reason: this is the account's clearest case of the classic short-form
  virality mechanism working exactly as designed — a high-arousal emotional payload (uncanny AI
  realism) + zero-friction reaction media (7 seconds, nothing to parse) + an explicit save-trigger +
  comment-gated payoff — and, unusually for this account's top tier, it converted views into
  genuinely *proportional* engagement (both likes and comments scaled with views), not just raw reach.
- Secondary factor: the confirmed absence of an ad-boost signature (no #ad tag, and — critically —
  likes and comments moving together rather than the "huge views + near-zero engagement" shape seen
  on paid content elsewhere in this study) supports reading this as genuine organic resonance.
- Contrast: Video 1 had 2.5x this video's views but ~140x *fewer* likes in absolute terms. By
  engagement-quality standards (not raw view count), **this is arguably Sebastien's strongest true
  viral hit in this sample**, even though it ranks #4 by raw views. See Section C.

#### Sources
- `ig_harvest/sebastien.md`, including its "Anomaly re-verification" section (added 2026-07-25)
- TikTok video 7630445809162652950, `https://www.tiktok.com/@sebastienjefferies/video/7630445809162652950` (yt-dlp metadata, 2026-07-25; no subtitles available)

---

### VIDEO 5 (TOP #5, 922K views): "Head to head test: Seedance 2.0 vs Veo 3.1 vs Kling 3.0"

#### 0. Identity & stats
- Shortcode `DWotUKUjJq2`. Posted **Apr 2, 2026** `[OBSERVED]`.
- IG: 922K views, 5,763 likes, 110 comments `[OBSERVED]`. Like-rate: **0.625%** — second-best of the 5
  top videos (after Video 4's 6.4%), and notably the **only one of the 5 top videos without any
  comment-keyword CTA** (per the harvest's own note).
- **No cross-platform copy found.** TikTok grid confirmed a genuine ~3-week posting gap spanning this
  exact date (last TikTok post before: Mar 19; next: Apr 8) — no video exists on TikTok for Apr 2.
  Both YouTube channels' catalogs checked — no 3-way comparison video found; the closest matches are
  two *separate*, single-tool videos ("Seedance 2.0 is FINALLY HERE," "This Is How To Use Kling 3.0
  Like A PRO") which are **not** the same content as a head-to-head comparison. **DATA GAP: no
  verbatim transcript obtainable.**

#### 1. Packaging
- Caption: "head to head test: Seedance 2.0 vs Veo 3.1 vs Kling 3.0" `[OBSERVED]` — factual, direct,
  no superlative language, no CTA-bait. Reads closer to a headline than a hook.
- Curiosity gap: implicit ("which one actually wins") rather than stated.

#### 2. Hook (0–3s)
- No transcript — `[DATA GAP]`.
- Hook taxonomy `[INFERRED from caption]`: **comparison / "which is best"** framing — a distinct
  category from the bold-claim and demo-in-motion types dominant elsewhere in this account's catalog,
  closer to a "confronting question" that forces the viewer to self-locate ("which one am I already
  using / should I switch").

#### 3. Structure & retention engineering
- `[INFERRED, MED confidence]`: near-certainly a rapid-fire 3-way structure — same prompt/scene run
  through each of the three models back-to-back with narrated commentary on differences, a
  well-established comparison-video template. Given the absence of any CTA, the payoff is likely
  self-contained (a stated verdict) rather than gated off-platform.
- Beat map: cannot be produced — `[DATA GAP]`.

#### 4. Value proposition
- Walk-away value: a **decision-aid** — helps viewers choose which of three newly-competing flagship
  AI video models to invest time learning.
- Practical value class: news/comparison — arguably the single most "useful reference" video in this
  sample, since it directly answers a live, contested question rather than teaching one tool in
  isolation.
- Timing/topicality context `[OBSERVED via WebSearch]`: this is confirmed as a genuinely hot,
  industry-wide topic at the time — numerous independent third-party AI blogs (magicshot.ai,
  wavespeed.ai, aijourn.com, flixly.ai, pixara.ai) published near-identical "Seedance 2.0 vs Kling 3.0
  vs Veo 3.1" comparison content in the same 2026 window. **None of these third-party articles are by
  or about Sebastien** — they establish only that the topic itself was contested/timely industry-wide,
  not that Sebastien's specific video was covered or amplified externally.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (a genuine decision-aid) + **Triggers** (any of the three named
  models becomes a recurring cue every time a viewer considers making AI video, re-activating memory
  of this comparison per the mere-exposure/triggers mechanism, §2.2).
- Primary emotion: **lower-arousal than Video 4** — closer to "calm-useful" than "awe." Per
  `03_virality_science.md` §2.3, low-arousal-but-positive content is known to under-perform pure
  awe/anger content specifically on *shares*, even when it performs fine on likes/views — plausibly
  explaining why this ranks #5 by views despite strong topicality and the second-best like-rate.

#### 6. CTA & funnel mechanics
- **None** `[OBSERVED, per harvest]` — the only top-5 video without a comment-to-DM mechanic.
- Funnel position: pure top-of-funnel **authority-building** rather than direct lead capture —
  positions Sebastien as a fast-moving, objective AI-video authority. Value here is reputational, not
  a direct funnel step.

#### 7. Replicability verdict
- Template: identify a moment when 2–3 flagship tools in a niche are simultaneously newly-relevant
  → run the same test prompt through each → deliver a direct verdict, no CTA required.
- Commodity: entirely — requires only access to the compared tools, no relationships or proprietary
  content.
- Difficulty for Tangent: **LOW–MED** — the format is simple, but correctly timing it to a genuine
  multi-tool "moment" (not inventing an artificial comparison) is the actual skill.

#### 8. Why it won
- Caught a genuine, industry-wide hot-topic window (three major AI video models newly competitive
  simultaneously) with a direct, no-nonsense comparison framing precisely when competing SEO/blog
  content on the identical topic was also proliferating — strong evidence of real cross-platform
  demand for this specific comparison at that moment, a timing/trend-surfing win independent of any
  funnel mechanic.
- Notable secondary finding: this is the **only top-5 video with no CTA at all**, yet it still posted
  the second-best like-rate of the group — suggesting that for this account, topicality/stakes may
  drive genuine engagement more reliably than the comment-keyword mechanic does. Single-data-point,
  flagged as suggestive not conclusive.

#### Sources
- `ig_harvest/sebastien.md` (sole direct source)
- WebSearch results establishing topical timing (magicshot.ai, wavespeed.ai, aijourn.com, flixly.ai, pixara.ai — cited for topicality context only, not as sources about Sebastien)

---

### VIDEO 6 (FLOP #1, 19.9K views): "How to make Music Videos with AI"

#### 0. Identity & stats
- Shortcode `DaffjwFsX85`. Posted **Jul 7, 2026** `[OBSERVED]`.
- IG: 19.9K views, 205 likes, 114 comments `[OBSERVED]`. Like-rate: **1.03%** — higher than 4 of the 5
  top videos. Comment rate: **0.573%** — by far the highest comment *rate* of any video in this
  7-video sample (roughly 23x Video 1's rate, 72x Video 5's rate).
- Rank: **19.9K vs. the account's 140K median — a 7x under-performance**, and the account's #2 flop
  overall (of the 2 sampled).
- TikTok twin: `7659766030515932418`, posted the **same date** (Jul 7, 2026), 31s, 1,895 views, 66
  likes, 5 comments, 4 reposts `[OBSERVED via yt-dlp]`. TikTok like-rate: 3.48% — also higher than
  most of the account's TikTok top-performer rates, reinforcing that the engagement-quality pattern
  holds cross-platform, not just on IG.

#### 1. Packaging
- Caption: "How to make Music Videos with AI. Comment 'OPUS' and I'll send you the link." `[OBSERVED]`
  — per the harvest's own note, this uses the **same hook style** ("comment KEYWORD") as the account's
  top performers, confirming the hook-format itself is not the differentiator here.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via TikTok transcript]`: **"Here's how you can make this music video using
  AI."**
- Hook taxonomy: **flat/plain instructional** — no bold claim, no stat, no stakes, no superlative
  language. Contrast directly with Video 1's "this video just got 20 million views" or Video 2's
  "brand new workflow... absolutely insane" — this hook has zero amplifying language of any kind.
- What the viewer sees: `[INFERRED]` likely opens on a music-video clip already in motion, given the
  immediate cut to "you'll start by heading over to Agent Opus."

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via transcript]`:
  - [0:00] Flat hook.
  - [0:06] Tool name: "Agent Opus" — upload your song.
  - [0:09] Style/reference-adding step.
  - [0:13] Iteration step: "use the agent to make any changes" (pacing, characters).
  - [0:18] Generate + result shown.
  - [0:26] Result playback ("let's check it out").
  - [0:28] CTA: "comment the word Opus and I'll send you the link as well as the full guide."
- One-idea-per-video: yes, but the underlying idea (an AI music-video-specific agent) has a
  meaningfully narrower relevance ceiling than Videos 1–2's broader AI-video-model topics — AI music
  video generation is a smaller, more specialized use case even within an already-niche AI-creator
  audience.
- Payoff placement: front-loaded and complete within the video (tool name + steps + result all shown)
  — similar specificity to Video 2, not gated like Video 1.

#### 4. Value proposition
- Walk-away value: tool discovery (Agent Opus specifically) + a shown workflow.
- Practical value class: tool discovery + copyable workflow.
- Specificity: **MED** — names the tool and shows step order, structurally similar to Video 2, but
  the tool itself (a music-video-specific AI agent) serves a much narrower audience segment than a
  general video-restyling tool.

#### 5. Psychology scoring
- STEPPS: **Practical Value** present but narrow-audience — only creators who make music videos need
  this specific tool, which caps the Social-Currency ceiling too (knowing a music-video AI tool
  signals less broadly than knowing how to restyle any video with AI).
- Primary emotion: flat/informational — no awe-language anywhere in the hook or beats (contrast
  Videos 1–2's "insane," "crazy," "20 million views").
- Save/send trigger: MED-LOW — useful only to a subset of viewers with an active music-video need.

#### 6. CTA & funnel mechanics
- "Comment the word Opus..." `[OBSERVED]` — same mechanic as top performers.
- **Notable finding:** this flop has the **highest comment RATE of any video in the sample** (0.573%)
  — the audience that *did* see this video engaged with the CTA disproportionately well. The problem
  is not funnel conversion among reached viewers; it is reach/distribution itself.

#### 7. Replicability verdict
- Template: pick a tool, name it, show 3–5 steps, CTA-gate the link.
- Commodity vs. unfair advantage: requires access to/knowledge of the specific niche tool (Agent
  Opus) — otherwise fully commodity execution.
- Difficulty for Tangent: **LOW-MED**.

#### 8. Why it lost
- Single most load-bearing reason: **narrow topical addressable-audience** — AI-generated music
  videos is a sub-niche within an already-niche AI-creator-tools audience — combined with a flat,
  unembellished hook carrying zero stakes/superlative/news-hook language. The video reads as a routine
  tutorial rather than an event.
- Consistent with the "audition"/test-and-expand distribution model (§1.1.3): the tiny absolute view
  count relative to the account's median (19.9K vs. 140K, a 7x under-performance) despite the reached
  audience engaging at an above-average *rate* suggests Instagram's early test-wave simply did not
  expand distribution beyond an initial small cohort — a reach failure, not an engagement failure.

#### Sources
- `ig_harvest/sebastien.md`
- TikTok video 7659766030515932418, `https://www.tiktok.com/@sebastienjefferies/video/7659766030515932418` (yt-dlp metadata + transcript, 2026-07-25)

---

### VIDEO 7 (FLOP #2, 21.5K views): "How to create a 3D rotating logo effect using 1 app on your phone"

#### 0. Identity & stats
- Shortcode `DaiKv3Ls_tT`. Posted **Jul 8, 2026** `[OBSERVED]` — **one day after Video 6**, forming a
  genuine two-post consecutive-flop cluster (see Section C for the cross-video timing analysis).
- IG: 21.5K views, 182 likes, 128 comments `[OBSERVED]`. Like-rate: 0.85%. Comment rate: **0.595%** —
  the single highest comment rate of any video in the entire 7-video sample, edging out Video 6.
- TikTok twin: `7660151929825201430`, posted the **same date** (Jul 8, 2026), 20s, 1,888 views, 46
  likes, 8 comments, 1 repost `[OBSERVED via yt-dlp]`. TikTok like-rate: 2.44% — again above most of
  the account's TikTok top-performer rates.

#### 1. Packaging
- Caption: "How to create a 3D rotating logo effect using 1 app on your phone. Comment 'logo' to get
  the app + prompts" `[OBSERVED]` — per the harvest's own note, a full numbered-steps tutorial using
  the same hook style as top performers. Notably **vague on the tool name in the caption itself**
  ("1 app" — unnamed).

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via TikTok transcript]`: **"Here's how to do this with one app on your phone."**
- Hook taxonomy: same flat/plain instructional pattern as Video 6 — no stakes, no superlative, no
  news-peg.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via transcript]`:
  - [0:00] Flat hook.
  - [0:02] Step 1: "tap on AI image."
  - [0:04] Step 2: "upload your photo and paste my prompt."
  - [0:07] Step 3: "choose 4K and hit generate."
  - [0:10] Mid-result shown (still image).
  - [0:11] Step 4: "tap on video, select [K]ling [rendered "cling" in auto-captions], paste my prompt,
    hit generate."
  - [0:15] Result: "3D rotating effect."
  - [0:17] CTA: "comment logo to get the app and the prompts."
- **Specificity gap, load-bearing finding:** the transcript never names the actual "AI image" app used
  — only the generic action label "tap on AI image," not a brand name — despite the caption's promise
  of "1 app on your phone." The app identity is the single most important piece of replication
  information and it is the one thing withheld until after the comment-gate. Contrast with every one
  of the account's transcribed top performers, which all name their tool explicitly within the first
  10–20 seconds (Dreamina, Luma Ray3.14, Seedance 2 even in the untranscribed Video 4's caption). This
  is the **least tool-specific** of all 7 videos in this sample.
- One-idea-per-video: yes, but a narrow aesthetic/design trick rather than a broadly useful AI-video
  capability.

#### 4. Value proposition
- Walk-away value: an aesthetic/visual-effect trick (3D rotating logo) — a design/branding-adjacent
  use case, narrower than general AI-video-model content, and arguably more "nice to have" than
  "need to have" for this account's core AI-tools-for-creators audience.
- Practical value class: tool discovery (partial — tool identity withheld) + copyable visual trick.
- Specificity: **LOW-MED** on tool identity (the single biggest gap in this sample) despite HIGH
  step-level specificity (four clear numbered actions).

#### 5. Psychology scoring
- STEPPS: **Practical Value** present via numbered steps but **low Social Currency** — a logo-spin
  effect is a minor aesthetic flourish, not an "insider knowledge" or "impressive capability" reveal
  on the order of Video 4's "breaking the barrier between real and fake" or Video 2's "hours of VFX
  in minutes."
- Primary emotion: flat/utility — no arousal language anywhere in hook or beats.

#### 6. CTA & funnel mechanics
- "Comment logo to get the app and the prompts" `[OBSERVED]`. Same pattern as Video 6: **highest-
  in-sample comment rate (0.595%)** despite lowest-in-sample absolute reach, reinforcing the Video 6
  finding — the funnel mechanic converts fine among whoever sees these videos; distribution/reach is
  the actual bottleneck, not the CTA design.

#### 7. Replicability verdict
- Template: numbered 4-step visual trick + CTA-gate the specific tool name.
- Commodity vs. unfair advantage: fully commodity, though the account's own choice to withhold the
  tool name even in the free video is itself a (possibly counterproductive) choice worth noting for
  Tangent to avoid replicating.
- Difficulty for Tangent: **LOW**.

#### 8. Why it lost
- Same core diagnosis as Video 6: a narrow-appeal aesthetic trick, a flat un-amplified hook, and
  (uniquely for this video) unusual vagueness about its own core tool even relative to the account's
  own norms — all consistent with the account's low-arousal/flat-hook videos consistently
  under-performing regardless of an otherwise-identical CTA mechanic.
- Posted one day after Video 6 (Jul 7 → Jul 8), forming a genuine two-post cluster of consecutive
  under-performers immediately following the account's highest-view post in this sample (Video 1, Jun
  25) — see Section C for the cross-video pattern analysis of this cluster.

#### Sources
- `ig_harvest/sebastien.md`
- TikTok video 7660151929825201430, `https://www.tiktok.com/@sebastienjefferies/video/7660151929825201430` (yt-dlp metadata + transcript, 2026-07-25)

---

## C. TOP vs. FLOP delta

The harvest's own pattern note is correct as far as it goes — the "comment KEYWORD for the link" hook
*format* appears on 4 of 5 tops AND both flops, so format alone is not the differentiator. Digging
into topic/emotion/specificity/timing across the full post-mortems above surfaces a much clearer,
consistent signal:

**1. Topicality/news-timing is the single strongest differentiator.** 4 of 5 tops tie directly to a
newly-released or actively-contested AI model/tool moment: Video 1 (a viral third-party case study,
riding an existing 20M-view moment), Video 2 (Luma's then-new Ray3.14), Video 4 (Seedance 2's release
window, independently corroborated as a live topic by third-party AI blogs), Video 5 (a literal 3-way
comparison of three simultaneously-hyped flagship models, also independently corroborated as an
industry-wide hot topic at the time via WebSearch). Only Video 3 lacks a confirmed news peg (DATA GAP
on its transcript). Both flops are evergreen niche tutorials (a music-video-specific agent; an
unnamed "1 app" logo trick) with no news hook, no release-window timing, no comparison/stakes framing.

**2. Audience-breadth of the underlying tool/topic.** Tops name broadly-relevant, high-profile tools
that the entire AI-creator niche is actively tracking (Dreamina, Luma, Seedance, Veo, Kling — all
major, competing flagship products). Flops feature narrower tools with smaller addressable relevance
even *within* the already-niche AI-creator audience (a music-video-specific agent; an unnamed generic
"AI image" app).

**3. Hook amplification language — the cleanest, most directly verifiable finding.** Every
transcribed top video (1, 2) opens with superlative/stakes language ("this video just got 20 million
views," "brand new workflow... absolutely insane"); Video 4's caption uses comparably high-stakes
framing ("breaking the barrier between what's real and what's not"). Both transcribed flops (6, 7)
open with flat, zero-amplification instructional language ("here's how you can make this," "here's
how to do this") — nearly identical phrasing to each other, and the weakest hook language in the
entire sample. This is a directly `[OBSERVED]` pattern across all 4 transcribed videos, not an
inference.

**4. The engagement-rate paradox — the dossier's most non-obvious finding.** Raw view count and
engagement *rate* are close to inversely correlated among this account's "top 5." Like-rates for the
5 tops: Video 1 (2.4M views) 0.018%, Video 2 (1.6M) 0.024%, Video 3 (1M) 0.040%, Video 4 (950K) 6.4%,
Video 5 (922K) 0.625%. **Both flops (19.9K, 21.5K views) have higher like-rates (1.03%, 0.85%) than
three of the five "top" videos**, and both flops have the **highest comment rates in the entire
7-video sample** (0.573%, 0.595% — well above every top video except Video 4's 0.188%). This pattern
holds on TikTok too (flops' TikTok like-rates of 3.48%/2.44% exceed Video 2's TikTok rate of 0.109%),
confirming it is a genuine content-resonance signal, not an IG-specific artifact. **Practical
implication: "top 5 by views" and "top 5 by genuine audience resonance" are not the same ranking for
this account.** Only Video 4 (the confirmed anomaly) combines high reach with high engagement rate;
the other four "tops" appear to be reach-inflated relative to how deeply their actual viewers engaged
— a pattern structurally similar to (though not proven to share the mechanism of) the "passive
distribution" signature flagged for `100xengineers` elsewhere in this study (`ig_harvest/00_INDEX.md`),
though **no ad/sponsor tag is present on any of Sebastien's five**, so this is explicitly *not* the
same confirmed paid-boost mechanism documented for `tiffintech`/`networkchuck` — just a structurally
similar view/engagement mismatch, flagged honestly as unresolved rather than asserted as ad-driven.

**5. Funnel mechanic converts fine; distribution is the actual bottleneck for the flops.** Both flops
show *above-average* comment-rate conversion on their CTA — the "comment KEYWORD" mechanic is working
exactly as designed among whoever actually sees these videos. What differs is whether Instagram's
early-audition test wave (§1.1.3) expanded distribution beyond the initial small cohort — and
findings 1–3 above (topicality, audience breadth, hook amplification) are the most likely drivers of
that early-wave signal, since the funnel/CTA mechanic itself is held constant across tops and flops.

**6. Cluster timing.** Both flops landed on consecutive days (Jul 7–8, 2026), immediately following a
stretch that included the account's #1 all-time top video in this sample (Video 1, Jun 25). This
raises the possibility of an "after the big one" reversion-to-mean effect — `[INFERRED, LOW-MED
confidence]`, one data point, insufficient to establish a rule, and explicitly the open question the
original harvest flagged as unresolved. Cross-referenced against TikTok's contemporaneous posting
cadence for this same window (steady output through Jul 23, 2026, no gap or shift in volume/topic
mix) — this shows **no corresponding TikTok-side disruption**, suggesting the July dip is not a
broad content-production slowdown or creative dry spell, but something narrower: either IG-specific
algorithmic variance on these 2 specific posts, or a genuine niche-fit miss on 2 topic choices in a
row (both flops score weakest on findings 1–3 above, which is consistent with a topic-choice
explanation rather than a production-quality one).

---

## D. Content architecture

**Key vs. filler.** "Key" content — the material anchoring this account's growth ceiling — is
tool-launch/model-comparison news content tied to major, competing AI video models (Seedance, Veo,
Kling, Luma) and third-party viral case studies. "Filler" content — maintaining posting cadence and
account activity between key hits — is evergreen niche tutorials (specialized agents, single-use
visual tricks) that rarely break out but, per Section C finding 5, still convert well on a
per-viewer basis; they simply don't get shown to enough viewers to matter at scale.

**Series formats.** No numbered/episodic series ("Part 2," "Episode N") was observed in this 7-video
sample, and none appears across a wider scan of ~120 TikTok titles from the same account `[OBSERVED
via yt-dlp]`. The format is better described as a recurring **thematic template** — hook → tool name
→ 2–4 step demo → comment-keyword CTA — applied to a rotating cast of individual AI tools, rather
than a formal series structure. This is a meaningfully different content architecture from, e.g.,
`nateherkai` in this same study, whose funnel routes through a distinct long-form-video layer.

**Posting rhythm.** TikTok proxy (the best available signal, `[OBSERVED]`) shows roughly one post
every 4–7 days across the sampled window, with two multi-week gaps (late Dec 2025–mid Jan 2026,
~3 weeks, likely a holiday break; mid-Mar–early-Apr 2026, ~3 weeks, unexplained). IG's native cadence
could not be independently confirmed beyond the 7 sparse dated points in this sample — **DATA GAP**,
flagged for any future harvest of this account to fill via a dedicated cadence sweep (not performed
here, as it was out of scope for the top-5/flop-2 selection this dossier was built on).

**How content feeds the paid community.** Every analyzed video except Video 5 (6 of 7) uses the
identical comment-keyword → DM/link mechanic, making each individual reel a standalone lead-capture
unit rather than routing viewers through an intermediate content layer before any monetization touch.
The bio link (`skool.com/aicreatorlab/about`) is a secondary, passive path; the primary conversion
path is per-video and comment-triggered. This feeds a **$57–79/mo Skool community** (AI Creator Lab,
265–287 members, implying roughly $15K–23K MRR at listed pricing) offering a 7-day AI-character
quick-start course, weekly live coaching, an expanding prompt/template library, and tool discounts up
to 60%. The whole-account design pattern is thus: **high-frequency, single-hop, tool-specific lead
magnets**, in contrast to a lower-frequency, narrative-building content strategy — consistent with an
account whose primary asset is breadth of tool coverage (staying current across every major AI-video
model release) rather than a single signature format or persona hook.

---

## E. Method log

**Primary data:** read `ig_harvest/sebastien.md` and `ig_harvest/00_INDEX.md` in full before any
other work, per the assignment's mandatory-first instruction. Also read `QC_PROTOCOL.md`,
`templates/video_postmortem_template.md`, and `03_virality_science.md` in full before beginning
analysis, per the assignment's mandatory-first instruction.

**Anomaly check (required by the assignment brief):** re-checked `ig_harvest/sebastien.md` for an
"Anomaly re-verification" section before finalizing this dossier. Found it present (added by the
separate browser-agent re-verification pass referenced in the assignment) — confirms the DW_VCbrDPWM
61K-like anomaly as genuine, not a data artifact. Incorporated into Video 4's post-mortem.

**TikTok cross-referencing (yt-dlp, no browser tools used, per the assignment's channel restriction):**
- `yt-dlp --flat-playlist --playlist-items 1:50` and `51:120` against
  `https://www.tiktok.com/@sebastienjefferies` — pulled 120 videos spanning Apr 2025–Jul 2026, with
  id/title/upload_date/view_count for each, used to date-match and caption-match against the 7 target
  IG shortcodes' detail-pull captions.
- Matches found (5 of 7): DaAlMicsiBD ↔ TikTok 7655313528919788802 (exact date, Jun 25); DVylvZbDGTo
  ↔ TikTok 7616407657204780310 (exact date, Mar 12); DW_VCbrDPWM ↔ TikTok 7630445809162652950
  (caption-identical, 8-day date offset — Apr 11 IG vs. Apr 19 TikTok); DaffjwFsX85 ↔ TikTok
  7659766030515932418 (exact date, Jul 7); DaiKv3Ls_tT ↔ TikTok 7660151929825201430 (exact date, Jul
  8).
- Matches not found (2 of 7): DYSWrorMzBA (May 13) and DWotUKUjJq2 (Apr 2) — confirmed no TikTok post
  exists on or near either date (checked the surrounding ±1–2 weeks of the 120-item TikTok timeline
  for both windows; Apr 2 falls inside a confirmed ~3-week TikTok posting gap, Mar 19–Apr 8).
- For each of the 5 matches: pulled full `description` field (`--print "%(description)s"`) to confirm
  caption identity (not just topical similarity), pulled precise stats (`duration`, `view_count`,
  `like_count`, `comment_count`, `repost_count`, `upload_date`) via `--print`, and attempted
  `--write-subs --sub-langs eng-US` for transcripts. 4 of 5 had an available `eng-US` auto-caption
  track and were downloaded in full (`.vtt` files, read verbatim); DW_VCbrDPWM's twin (7s, no spoken
  dialogue) returned "no subtitles for the requested languages" — confirmed via `--list-subs`, not
  assumed.
- **Failed:** attempted `--write-comments --write-info-json` on one TikTok video (DaAlMicsiBD's twin)
  to check for automated-DM-bot reply patterns in the comment thread (to help confirm/deny the
  ManyChat-automation question in the funnel section). The resulting `info.json` had no `comments`
  key populated — this yt-dlp build's TikTok extractor (version 2026.07.04) does not appear to support
  comment extraction, or requires additional undiscovered flags. Not pursued further given time
  constraints; logged as a DATA GAP on the funnel-automation-tool question rather than fabricated.

**YouTube cross-referencing (yt-dlp):**
- `yt-dlp --flat-playlist --playlist-items 1:60` against `youtube.com/@sebintel/videos` — returned
  "This channel does not have a videos tab" (confirmed Shorts-only channel).
- Same against `youtube.com/@sebintel/shorts` — 60 items returned, titles reviewed for topic match
  against DYSWrorMzBA/DWotUKUjJq2 — no match (channel's content is generic AI-tool-news shorts in a
  different voice/format from the IG account's personal-hook style, consistent with its reported
  automated-pipeline nature).
- Same against `youtube.com/c/SebastienJefferies/videos` — 62 items returned (full catalog from
  current AI content back through 2022-era editing-tips content), titles reviewed — no title match for
  either target video; closest topical neighbors identified and explicitly distinguished as NOT the
  same content in Video 5's post-mortem (separate single-tool videos vs. a 3-way comparison).

**WebSearch queries run (8 total):**
1. "Sebastien Jefferies YouTube channel AI" — surfaced both YouTube channels, Skool page, LinkedIn, X.
2. `"Sebastien Jefferies" OR sebastienjefferies "YouTube thumbnails" AI tool` — no video-specific
   match, only generic third-party AI-thumbnail-tool SEO results.
3. `Sebastien Jefferies "Seedance 2.0" "Veo 3.1" "Kling 3.0" comparison` — no Sebastien-specific
   match, only third-party AI-blog comparison articles (used only to establish topical timing).
4. "Sebastien Jefferies AI Creator Lab Skool price" — confirmed $57→$79 founding-rate pricing.
5. `Sebastien Jefferies "fastest way" YouTube thumbnails AI seconds Instagram` — no match, same
   generic-tool-SEO result set as query 2.
6. "Sebastien Jefferies YouTube channel AI" (repeat framing) — see query 1.

**WebFetch pulls (3):**
1. `skoolmakers.com/communities/ai-creator-lab/` — third-party Skool review, member count (287),
   founder background, curriculum, marketing-approach critique.
2. `skool.com/aicreatorlab/about` — direct community page, member count (265), pricing, curriculum,
   contest details.
3. `sjorigin.com/` — personal brand site, background/credentials, alternate pricing tier ($67→$87 —
   flagged as a discrepancy against the skool.com page rather than silently reconciled), funnel-layer
   description.

**What was NOT done / explicit limitations:**
- No frame-level video review was performed for any video (transcript + metadata + caption only, per
  the validated method used consistently across this research pass) — flagged as `[DATA GAP]`
  wherever visual-only information (on-screen text overlays, cut frequency, exact opening frame
  content) would have been needed.
- IG comment threads were not read directly (browser tools reserved this session) — CTA
  conversion is inferred from aggregate comment *counts* only, not comment *content*.
- The ManyChat/automation-tool question for the funnel (native IG comment-automation vs. a third-party
  tool vs. manual replies) remains unconfirmed — logged as DATA GAP rather than assumed.
- Instagram's own grid-position-vs-date inconsistency (Section A) was noted but not independently
  resolved — this dossier did not re-scrape Instagram to investigate further, consistent with the
  channel restriction for this task.

## GATE C CORRECTION (2026-07-25)

[OBSERVED] Independent Gate C audit + full-corpus remediation found this dossier is the one in the
corpus that skipped the standard practice (independent `yt-dlp` verification of IG likes against the
IG reel itself) that 6+ peer dossiers used — this file's own Method log above confirms cross-platform
verification was obtained via `yt-dlp` against TikTok/YouTube only, never against the IG reels
themselves. As a direct result, Videos 1-3's IG like counts were wrong by 7x-27x. Video 4 and Video 5
are unaffected (already independently confirmed accurate). Full methodology and corpus-wide analysis:
`research/critic/GATE_C_REMEDIATION.md` §3(c). Corrected via `yt-dlp -j` against the public reel URL,
2026-07-25; comments/dates unchanged on all three:

| Video | Shortcode | Old IG likes | Corrected IG likes | Ratio | Old like-rate | Corrected like-rate |
|---|---|---|---|---|---|---|
| Video 1 | `DaAlMicsiBD` | ~~435~~ | **3,867** | 8.89x | 0.018% | **0.161%** |
| Video 2 | `DVylvZbDGTo` | ~~379~~ | **2,730** | 7.2x | 0.024% | **0.171%** |
| Video 3 | `DYSWrorMzBA` | ~~395~~ | **10,594** | 26.82x | 0.0395% | **1.059%** |

**Superseded claims (Video 1, §0/§5/§8):**
- "IG like-rate is 0.018%... the single lowest like-rate of any of the 5 top videos" — SURVIVES-
  WEAKENED: V1 is still the lowest of the 5 (corrected 0.161% vs. V2's 0.171%, a narrow margin), but
  the stated magnitude (0.018%) was wrong by 8.89x.
- "TikTok twin's like-rate is 9.8% — over 500x higher on a per-view basis" — DIES: using the corrected
  IG rate (0.161%), the true gap is **~61x**, not "over 500x."

**Superseded claim (Video 3, §0/§5):**
- "like-rate 0.0395%" — DIES, corrected to **1.059%** — Video 3 is now the **second-highest** like-rate
  of the 5 top videos, not third-lowest as originally stated.

**Superseded claim (§8, cross-video ranking):** the stated like-rate ranking (lowest→highest)
V1<V2<V3<V5<V4 DIES and becomes **V1<V2<V5<V3<V4** (V3 and V5 swap position). Video 1's "arguably the
weakest of the 5 top videos despite ranking #1 by raw views" framing survives directionally (V1 is
still lowest), but any "500x" magnitude language tied to it does not.

**What still holds:** the account-level "engagement-rate paradox" (this dossier's flops out-engaging
3 of 5 tops) SURVIVES under corrected numbers — flops run 0.85%-1.03% like-rate, still exceeding 3 of
the 5 tops, though the specific set changes from {V1,V2,V3} to {V1,V2,V5}. Video 4 and Video 5's
figures and conclusions are entirely unaffected (both were independently confirmed accurate,
MATCH ≤1.0x).
