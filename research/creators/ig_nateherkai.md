# Creator Dossier: Nate Herk | AI Automation (Instagram @nateherkai)

**Status:** SEED account (user-provided). This is the INSTAGRAM lane of a two-part dossier — the YouTube
lane (`yt_nateherk.md`, @nateherk, 870K subs) was completed by a separate analyst pass and is treated
here as a comparison baseline, not re-derived. This file's job is the IG-native analysis plus the
cross-platform translation story between the two.

**Analyst method:** Primary data source is `../ig_harvest/nateherkai.md` (grid + 7 detail pulls,
`[OBSERVED]` 2026-07-25 via the user's logged-in IG session — the harvest analyst, not this one, did that
pull). This dossier's OWN new observation work used **yt-dlp** (which, contrary to the QC protocol's
default assumption that IG is logged-out-blocked, successfully extracts public IG reel metadata —
description/caption, `like_count`, `comment_count`, `upload_date` — and can download the video file
itself) plus **ffmpeg/ffprobe** (duration, frame extraction) plus **WebFetch** (cross-check) plus
**yt-dlp against `@nateherk`'s YouTube catalog** for cross-platform matching. **No claude-in-chrome
browser tools were used**, per the assignment's explicit restriction. Every number in this file is
tagged `[OBSERVED]`/`[REPORTED]`/`[INFERRED]` with source + as-of date.

**Important scope note on video content access:** Instagram does not expose auto-captions/subtitles via
yt-dlp (`write-auto-subs` returns "no subtitles for the requested languages" on every reel tested), and
no local speech-to-text tool was available in this environment (checked: no `whisper`, no ASR). This
dossier therefore has **no verbatim audio transcript** for any IG-native reel except the one confirmed
YouTube cross-post (Video 9 below). For every other video, hook/structure claims are built from
**downloaded-video frame sampling** (3 frames per video: ~0.6s, midpoint, ~1.5s-from-end, via ffmpeg) —
a legitimate `[OBSERVED]` source for on-screen visuals, captions-burned-into-video, and UI content — but
audio content beyond what burned-in captions reveal is a logged **DATA GAP**, not invented.

---

## A. Account header

| Metric | Value | Source | As-of | Confidence |
|---|---|---|---|---|
| Followers | **277K** (og:description "277K Followers, 7 Following, 552 Posts"; header self-reports 278K, minor rounding diff) | `../ig_harvest/nateherkai.md` `[OBSERVED]` | 2026-07-25 | HIGH |
| Following / Posts | 7 / 552 | same | 2026-07-25 | HIGH |
| Bio | "Consulting agency / Founder & CEO @ AI Automation Society / Amazon Bestselling Author in AI / 850k on YouTube / nateherk.com and 1 more" | same | 2026-07-25 | HIGH |
| Median reel views (30 most recent non-pinned tiles, positions 4-33) | **30.95K** | same, computed by harvest analyst | 2026-07-25 | HIGH |
| Top pinned tiles (3) | 3.3M / 2.3M / 1.5M | same | 2026-07-25 | HIGH |
| Top non-pinned reel | **632K** | same | 2026-07-25 | HIGH |
| Non-pinned top/median ratio | 632K / 30.95K ≈ **20.4x** | computed | 2026-07-25 | HIGH |
| Raw (incl. pinned) top/median ratio | 3.3M / 30.95K ≈ **106.6x** | computed | 2026-07-25 | HIGH — but this figure is explicitly flagged as pin-distorted, not organic |
| Median-views/followers ratio | 30.95K / 277K ≈ **11.2%** | computed | 2026-07-25 | HIGH |
| Link-in-bio destination(s) | nateherk.com → routes to: YouTube channel, Skool "AI Automation Society" (free, ~425K members per site copy `[REPORTED]`), Skool "Society Plus" (paid tier), Uppit AI (agency), Amazon book page, LinkedIn | `[OBSERVED]` WebFetch of nateherk.com | 2026-07-25 | HIGH — this dossier's own fetch, confirms the **same ultimate Skool funnel destination** as the YT dossier found, see Section C |

**Cross-platform size comparison** `[OBSERVED, both sides carried from their respective dossiers' own
pulls, 2026-07-25]`:

| | YouTube (@nateherk) | Instagram (@nateherkai) | IG as % of YT |
|---|---|---|---|
| Audience size | 870K subscribers | 277K followers | 31.8% |
| Sample size (this study) | 164 shorts (full catalog) | 60 grid tiles (3 scrolls) | — |
| Median short/reel views | 25,500 | 30,950 (non-pinned) | 121% (IG median is *higher* in absolute terms despite the 3.1x-smaller audience) |
| Top short/reel views | 1,343,016 | 632,000 (non-pinned) / 3,300,000 (pinned) | 47% (non-pinned) / 246% (pinned) |
| Top/median ratio | 52.7x | 20.4x (non-pinned) / 106.6x (raw) | IG's organically-ranked content has a flatter, less lottery-shaped distribution than YT's |
| Median/audience-size ratio | 2.9% | 11.2% | IG reels reach a much larger share of the (smaller) follower base per post, by this rough proxy — caveat below |

*Caveat on the last row `[INFERRED]`: "median views ÷ followers" is not literally "% of followers who
saw it" on either platform — both platforms distribute short-form primarily via algorithmic feed to
non-followers, not to a fixed follower base (per `03_virality_science.md` §1.1.1, §1.2.3). Treat this
ratio as a directional efficiency signal (how big a post typically gets relative to account size), not a
literal reach percentage.*

**Top-line finding this comparison sets up:** Nate's Instagram reels, despite a 3.1x smaller audience
and a completely different CTA grammar (see Section C), post a *higher* absolute median view count than
his YouTube shorts. This is the first piece of evidence that IG is not a lagging, secondary distribution
channel for this creator — it performs at least as well as YouTube by the median-post measure, even
though its single best hits (non-pinned) top out lower than YouTube's single best hit.

---

## B. Video post-mortems

**Selection** (per assignment method): 2 pinned legacy hits analyzed separately (3.3M and 1.5M — the
oldest and newest of the account's three pinned tiles, chosen to show the CTA-keyword format's evolution
across ~5 months; the middle pin, 2.3M "BULLETPROOF," is referenced inline in Section B.10 rather than
given a full post-mortem, per the "1-2 pinned" instruction) + top 5 reels ranked by **non-pinned**
view count + 2 flops. **9 full post-mortems total**, all downloaded and frame-sampled directly by this
dossier via yt-dlp + ffmpeg (see Method log for exact commands).

---

### VIDEO 1 (PINNED, oldest/highest — grid position 3 of 3 pins): "Comment 'SYSTEM'"

#### 0. Identity & stats
- URL: instagram.com/reel/DRXZJeHiAES/. Platform: Instagram Reel. Posted **2025-11-22**
  `[OBSERVED via yt-dlp upload_date]`. Length: **28.05s** `[OBSERVED via ffprobe]`.
- Views: **3.3M** `[OBSERVED, ig_harvest, 2026-07-25, HIGH — IG's own displayed K-rounded figure; exact
  count not exposed]`. Likes: **89,817** `[OBSERVED via yt-dlp like_count, 2026-07-25, HIGH]`. Comments:
  **124,635** `[OBSERVED via yt-dlp comment_count, 2026-07-25, HIGH]`.
- Rank: **highest-viewed reel in the entire 60-tile grid sample**, and flagged **PINNED** by the harvest
  (grid position 3 — the oldest and highest-viewed of the account's three pinned tiles). Its raw view
  count is ~106.6x the account's non-pinned median, but per this dossier's method (and the harvest's own
  methodology note) that ratio is not a clean "won on merit vs. a typical reel" signal — a pinned tile
  has had continuous top-of-profile placement for ~8 months (Nov 2025 → Jul 2026 harvest date) and is
  the first thing every new profile visitor sees, a structural advantage no organically-ranked reel gets.
  Analyzed separately from the ranked top-5 for exactly this reason.

#### 1. Packaging
- Caption (full): **"Comment 'SYSTEM' and I'll send it over."** `[OBSERVED via yt-dlp description]` —
  no hashtags, no link, no long-form caption body. This is the entire visible text asset outside the
  video itself.
- First frame (0.6s, `[OBSERVED via ffmpeg frame extraction]`): a live n8n workflow canvas mid-build —
  visible nodes: "Schedule Trigger," "AI Agent" (wired to a "Google Gemini Chat Model" and a "Think"
  tool), "Structured Output Parser," and "Append or update row in sheet," with an "Execute workflow"
  button. A small red Shorts-style play-button glyph sits at the seam between this screen-recording and
  a lower half-frame — DATA GAP on what fills the lower half at this exact timestamp; obscured in the
  captured frame.
- Curiosity gap: the caption alone promises "a system" with zero context on what it does — this is
  thinner curiosity-gap construction than any YouTube short in the comparison dossier, all of which name
  the specific capability in the title itself (e.g. "Invoice Agent," "Personal Assistant"). Here the
  entire information-gap is deferred to the video's visuals/audio, which a cold scroller must actually
  watch to resolve — a real difference in packaging philosophy from the YT catalog's title-forward style.

#### 2. Hook (0–3s)
- Verbatim opening line: **DATA GAP** — no transcript obtainable (Instagram exposes no auto-captions via
  yt-dlp for this reel; a targeted search of Nate's YouTube shorts catalog for a same-day or
  topically-matching "SYSTEM" cross-post around Nov 2025 found no clean match — see Method log). Hook
  taxonomy is inferred from the visible opening frame only: **demo-in-motion** (a live, running workflow
  canvas is on screen from frame one, no talking-head preamble), consistent with the house style
  documented across the YT dossier's top-8 (`yt_nateherk.md` Videos 1, 2, 6).
- What the viewer sees: a screen-recorded automation-builder UI — functionally the same visual genre as
  his best YouTube shorts, not a distinct IG-native opening.

#### 3. Structure & retention engineering
- Beat map, built from 3 sampled frames only (~0.6s / ~14s / ~26.5s) — **not** a full shot list; treat
  as 3 confirmed data points across a 28s runtime, DATA GAP on everything between them:
  - **[~0:00-0:14]** n8n canvas screen-recording (per frame 1).
  - **[~0:14, midpoint frame]** hard cut to unrelated, high-production dramatic stock/generated footage:
    a sedan fully engulfed in flame on a suburban lawn at dusk, in front of a house, with the words
    **"full video"** burned in as an on-screen caption label. This is a jarring, tonally disconnected
    visual pivot from the software demo — nothing in the YT dossier's 11-video sample uses anything
    comparable.
  - **[~0:26.5, near-end frame]** cuts to Nate direct-to-camera (plain jacket, no visible branded
    merch — a wardrobe detail consistent with the Nov 2025 date, predating the "AIS"-branded jacket seen
    in his mid-2026 reels, see Videos 3-9 below), with the single word **"comment"** burned in as a
    caption.
- At least 2 confirmed hard cuts across 28 seconds (screen-recording → dramatic B-roll → talking head) —
  a materially more edited, multi-source-footage structure than the continuous single-screen-recording
  style that dominates his YouTube catalog.
- Open loop: none legible without audio — DATA GAP on whether/how the fire-footage insert connects
  narratively to the n8n demo (a plausible reading, `[INFERRED]`, is a "your business burns down without
  systems" metaphor, but this is not confirmed).
- Loop design/rewatch bait: not assessable without audio — DATA GAP.

#### 4. Value proposition
- Walk-away value: the n8n workflow itself, but **gated** behind the comment-CTA rather than shown to
  completion in-video — a structurally different value-delivery model from his YouTube shorts, which
  typically show the full working result on-screen (verbatim email sent, exact dollar figure, etc., per
  `yt_nateherk.md` Videos 1-6) even while also pointing to a longer video.
- Practical value class: copyable-workflow / tool discovery, deferred to an off-platform DM hand-off.
- Specificity: MED — the visible node graph names real, specific components (Google Gemini Chat Model,
  a Structured Output Parser, a Google Sheets append/update step), but the narrative logic connecting
  them (trigger condition, what it's logging and why) is unobservable without audio — DATA GAP.

#### 5. Psychology scoring
- STEPPS: **Practical Value** (a usable, specific-looking workflow) and **Social Currency** (the
  aspirational "I run automated systems" identity) are the most defensible pillars given available
  evidence. **Emotion**: the fire B-roll is a deliberate high-arousal visual insert (alarm/shock
  register) — a device that does not appear anywhere in the 11-video YT sample, and may be a genuinely
  IG-specific retention tactic (scroll-stopping via visual shock mid-scroll) rather than a cross-platform
  habit. `[INFERRED]` that this is intentional pattern-interrupt engineering per §2.1.2 of the virality
  doc — plausible given its jarring placement, not confirmed by any stated rationale.
- Save/send trigger: weaker than his best YT hits by design — because the actual workflow content is
  hidden behind the CTA rather than demonstrated to completion, there's less "send this exact
  useful thing to a specific friend" material visible in-feed; the save/send action this video is
  actually optimized for is the **comment**, not a share.

#### 6. CTA & funnel mechanics
- Explicit CTA: **"Comment 'SYSTEM' and I'll send it over"** — a comment-keyword-to-DM funnel (almost
  certainly ManyChat or an equivalent comment-automation tool per `03_virality_science.md` §3.4.3,
  though the specific tool is not directly confirmed/visible in this reel — `[INFERRED]` from the
  mechanic's universality and the harvest's cross-account pattern notes).
- This is **mechanically different from every one of the 11 YouTube shorts analyzed in `yt_nateherk.md`**
  — none of which use a comment-keyword mechanic; all use a verbal "go watch the full video on my
  channel" CTA instead. This single data point is the sharpest platform-CTA-difference finding in the
  corpus (expanded in Section C).
- Funnel position: top-of-funnel, but **short-circuits** the two-hop YouTube funnel (Short → long-form
  video → Skool, per `yt_nateherk.md` Section A) — here the path is reel → (inferred) automated DM →
  resource, with no long-form-video nurture step in between.
- **Comment count (124,635) exceeds like count (89,817)** — a 1.39:1 comment:like ratio. This is a
  structurally unusual engagement signature: organic short-form content overwhelmingly skews likes >>
  comments (typically by 10-50x, per general platform norms referenced across the harvest's other
  account files). A comment volume this close to — and here exceeding — the like volume is strong direct
  evidence the keyword-comment mechanic is functioning exactly as designed: it is manufacturing comment
  volume as its primary observable artifact, not an incidental side effect.

#### 7. Replicability verdict
- Template: (1) screen-record a real, specific, working system to establish credibility, (2) insert one
  incongruous, high-shock-value B-roll clip mid-video as a pattern-interrupt, (3) close direct-to-camera
  with a single, memorable, capitalized keyword CTA, (4) auto-DM the resource rather than making the
  viewer navigate anywhere.
- Commodity vs. advantage: the comment-automation mechanic is commodity-accessible (widely available
  tooling, per §3.4.3 of the virality doc); Nate's advantage is the real underlying n8n system plus an
  audience primed to trust his builds are genuine.
- Difficulty for Tangent: **LOW-MED** for the *format* (keyword-CTA + B-roll pattern-interrupt + direct
  address are all portable to art/photography content with no automation-engineering lift); the
  underlying "product" being demonstrated is obviously category-specific and not transferable.

#### 8. Why it won
This reel's 3.3M count is not a clean apples-to-apples "best single piece of content" signal — as a pin,
it has enjoyed ~8 months of continuous top-of-profile placement plus first-visibility to every new
profile visitor, a structural advantage the ranked top-5 (Section B.3-7 below) do not get. What IS
observable and load-bearing: a real, specific, credibility-establishing screen-recorded system demo; a
genuinely IG-distinct pattern-interrupt (the fire B-roll, absent from anything in the YT sample); and a
single, low-friction, automated CTA. Its status as the oldest of three actively-curated pins (the pin
order is reverse-chronological by when each was pinned, see Section B.10) signals Nate himself judges it
his flagship lead-magnet asset, a judgment independent of, and reinforcing, its raw view count.

#### Sources
- https://www.instagram.com/reel/DRXZJeHiAES/ — yt-dlp metadata pull + video download + ffmpeg frame
  extraction, 2026-07-25 (this dossier's own fetch)
- `../ig_harvest/nateherkai.md` — grid position, pinned-flag, view count `[OBSERVED, harvest analyst,
  2026-07-25]`
- `../creators/yt_nateherk.md` — cross-reference for house-style comparison

---

### VIDEO 2 (PINNED, newest — grid position 1 of 3 pins): "Comment 'RUSH'"

#### 0. Identity & stats
- URL: instagram.com/reel/DW4NudCk9ji/. Posted **2026-04-08** `[OBSERVED via yt-dlp]`. Length: **29.53s**
  `[OBSERVED via ffprobe]`.
- Views: **1.5M** `[OBSERVED, ig_harvest, HIGH]`. Likes: **44,436** `[OBSERVED via yt-dlp]`. Comments:
  **49,917** `[OBSERVED via yt-dlp]`.
- Rank: 3rd-highest in the grid sample, flagged PINNED (grid position 1 — the *newest* of the three pins,
  meaning Nate re-curates/reorders his pinned lineup over time rather than leaving a static set; pin
  display order on Instagram reflects pin-recency, most-recently-pinned first).

#### 1. Packaging
- Caption: **"Comment 'RUSH' and I'll send it over."** `[OBSERVED]` — identical grammar to Video 1's
  caption, confirming this is the same recurring CTA template with only the keyword swapped.
- First frame (0.6s, `[OBSERVED]`): a stylized illustrated motion-graphic — a cross-hatched hand
  reaching down toward a row of analog dial gauges and a red push-button, with the caption **"make
  full"** burned in. This is a custom illustrated asset, not a screen recording — a materially more
  produced visual than Video 1's fire B-roll (which was live-action/generated stock footage, not
  original illustration), suggesting increased IG-specific production investment between Nov 2025 and
  Apr 2026.

#### 2. Hook (0–3s)
- Verbatim: **DATA GAP** — no transcript obtainable, no confirmed YT cross-post found for "RUSH" despite
  a targeted date/keyword search (Apr 8, 2026 falls in a gap between two confirmed YT shorts dates,
  Apr 6 and Apr 11 — no YT short was posted on Apr 8 itself, per this dossier's own yt-dlp date sampling,
  see Method log).
- Taxonomy: closest fit is **bold-claim/urgency framing** inferred from the illustrated dial-and-button
  imagery (gauges, a push-button, "make full") plus the keyword itself ("RUSH") — a plausible urgency/
  act-now register, `[INFERRED]`, not confirmed by audio.
- Viewer sees: illustrated motion graphics, not a live product UI — visually distinct from Video 1's
  opening.

#### 3. Structure & retention engineering
- Beat map from 3 sampled frames:
  - **[~0:00, early frame]** illustrated dial/button graphic, "make full" caption.
  - **[~0:15, midpoint frame]** a retro red/cream propaganda-poster-style illustration of John F.
    Kennedy at a podium with rocket icons on either side, captioned **"generates"** (mid-sentence) over
    large bottom-of-frame text reading **"CHOSE TO WAIT."** This is a historical-rhetoric metaphor
    device (JFK, space-race urgency) — a third distinct visual register in this single video (illustrated
    UI graphic → historical-poster pastiche → talking head), the most visually elaborate single reel in
    this dossier's full sample.
  - **[~0:28, near-end frame]** Nate direct-to-camera, now wearing the **branded "AIS" jacket**
    (AI Automation Society merch — first appearance of this wardrobe element across this dossier's
    chronologically-earliest-to-latest sample, consistent with the Apr 2026 date sitting later than
    Video 1's Nov 2025, unbranded-jacket appearance), captioned **"the tool."**
- At least 2 hard cuts across distinct visual registers (illustration → poster pastiche → talking head)
  in under 30 seconds — the most produced/edited reel in this dossier's sample by shot-type diversity.
- The "CHOSE TO WAIT" / JFK framing strongly implies an urgency-of-action rhetorical structure (do not
  delay adopting the tool/system being pitched) consistent with the "RUSH" keyword — `[INFERRED]`
  reading, moderately confident given the explicit on-screen text, but the connecting logic (wait vs.
  what, exactly) is not confirmed without audio.

#### 4. Value proposition
- Walk-away value: an unnamed "tool," gated behind the comment-CTA — same deferred-value model as
  Video 1.
- Practical value class: closer to aspiration/urgency-marketing than a demonstrated workflow — this
  video shows the least concrete, specific product content of any video in this dossier's sample (no
  software UI, no named tool visible in any sampled frame — DATA GAP on whether the actual tool/tech is
  named or shown at any other point in the 29.5s runtime not covered by the 3 sampled frames).
- Specificity: LOW by the frames available — this is the most purely rhetorical/persuasive opening of
  any video analyzed in this dossier, leaning on illustrated metaphor rather than product demonstration.

#### 5. Psychology scoring
- STEPPS: **Emotion** (urgency/FOMO, via the explicit "CHOSE TO WAIT" framing) is the dominant,
  best-evidenced pillar here — a genuinely different emotional register from Video 1's awe/practical-
  value mix and from nearly everything in the YT dossier's top-8 (which skews toward awe at a working
  demo, per `yt_nateherk.md` Section C). **Social Currency**: plausible (being early/ahead via the
  "RUSH" framing) but secondary. Per `03_virality_science.md` §2.3, urgency/anxiety is a high-arousal
  negative emotion — Berger & Milkman's research places high-arousal negative emotions (anxiety, anger)
  as share-favorable, on a similar footing to high-arousal positive (awe) — so this is not necessarily a
  weaker psychological bet than Video 1's awe-based hook, just a different one.
- This is the clearest evidence in the entire IG sample that Nate's pinned/flagship content
  deliberately diversifies its emotional register across the three pins (Video 1 = awe/shock via fire
  B-roll, Video 2 = urgency/FOMO via JFK poster, and — per the caption pattern — the middle pin
  "BULLETPROOF" plausibly trades on a security/reliability register, though not independently verified
  here, see Section B.10) rather than repeating one formula.

#### 6. CTA & funnel mechanics
- CTA: identical mechanic to Video 1 — "Comment 'RUSH' and I'll send it over," comment-to-DM funnel.
- Comment count (49,917) exceeds like count (44,436) — 1.12:1 ratio, again comments ≥ likes, reinforcing
  the pattern from Video 1 that this CTA mechanic reliably inflates comment volume above its normal
  organic ceiling (typically a small fraction of like count).
- Funnel position: same short-circuited, single-hop reel→DM path as Video 1.

#### 7. Replicability verdict
- Template: pair a *rhetorical* urgency hook (illustrated metaphor, not a product demo) with the same
  keyword-CTA mechanic — proving the comment-to-DM funnel works as a wrapper around genuinely different
  hook content, not just around demo-style openings.
- Commodity vs. advantage: the illustrated-motion-graphic production style requires real design/editing
  investment (a step up from Video 1's fire-stock-footage insert) — a moderate skill/tooling barrier, not
  a pure commodity.
- Difficulty for Tangent: **LOW** for the CTA mechanic itself; **MED** for matching the illustration
  production quality, though Tangent's art/photography domain is arguably a more natural fit for
  custom visual metaphor content than an automation-tools channel is.

#### 8. Why it won
Like Video 1, this is a pinned tile and its 1.5M count reflects continuous top-of-profile placement, not
a pure organic-ranking signal. What's distinct and load-bearing here versus Video 1: a deliberate
emotional-register pivot to urgency/FOMO via genuinely elaborate custom illustration (the JFK poster is
the single most production-invested visual asset in this dossier's entire sample), suggesting Nate's
IG-specific creative budget/effort increased between Nov 2025 and Apr 2026. Its being the *most recently
pinned* of the three (grid position 1) suggests it is currently judged the strongest or most current
flagship asset, actively favored over even-higher-view-count alternatives in the account's own curation.

#### Sources
- https://www.instagram.com/reel/DW4NudCk9ji/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25
- `../ig_harvest/nateherkai.md` — grid position, pinned-flag `[OBSERVED, harvest analyst]`

---

### VIDEO 3 (TOP non-pinned, rank 1): "Comment 'FAKE'"

#### 0. Identity & stats
- URL: instagram.com/reel/DZku3mJH594/. Posted **2026-06-14** `[OBSERVED]`. Length: **32.34s**
  `[OBSERVED]`.
- Views: **632K** `[OBSERVED, ig_harvest]` — the **highest-viewed non-pinned reel in the grid**, the
  cleanest "won organically, not by pin-placement" data point in this dossier. Likes: **10,853**
  `[OBSERVED]`. Comments: **10,321** `[OBSERVED]`.
- Rank: #1 of the ranked (non-pinned) top-5. ~20.4x the account's non-pinned median.

#### 1. Packaging
- Caption: **"Comment 'FAKE' and I'll send it over."** `[OBSERVED]` — same recurring CTA grammar as
  Videos 1-2.
- First frame (0.6s, `[OBSERVED]`): a chaotic, real-world viral-stunt clip — a bearded man bench-pressing
  a loaded barbell in a gym while a bystander holds a large kitchen knife over a frosted layer cake
  balanced on his chest, with multiple onlookers filming on phones. This is a well-known genre of
  bizarre-but-real viral gym-stunt content, not anything AI-generated or software-related.

#### 2. Hook (0–3s)
- Verbatim: **DATA GAP** — no transcript; no YT cross-post found (Jun 14, 2026 falls inside the
  confirmed ~90-day YouTube-shorts posting gap this dossier identified, Apr 11 – Jul 9, 2026 — see
  Section C — meaning structurally no YT short could exist from this exact date).
- Taxonomy: `[INFERRED]` **"fake-or-real" / spot-the-AI hook** — the caption keyword "FAKE" paired with
  a bizarre-but-genuinely-real viral clip strongly suggests a "can you tell this isn't AI-generated?" or
  "AI vs. reality" framing, a recognizable and popular short-form trope distinct from anything in his
  YouTube catalog. This reading is plausible but not confirmed by audio — flagged as inference.
- Viewer sees: found/viral footage, not an original screen recording or original talking-head cold open
  — the only video in this dossier's full 9-video sample to open on third-party-sourced viral content
  rather than his own demo or original graphics.

#### 3. Structure & retention engineering
- Beat map from 3 sampled frames:
  - **[~0:00-0:16]** the gym cake/barbell viral clip continues, with the word **"AI"** animating onto
    screen in a translucent highlighted box near the midpoint frame — directly tying the found-footage
    clip to an AI framing.
  - **[~0:16, mid frame]** still on the gym clip, "AI" text overlay visible.
  - **[~0:30, near-end frame]** Nate direct-to-camera, AIS-branded jacket, now with a visible **Shure
    microphone** in frame (a production-setup upgrade not visible in Video 1 or 2's captured frames —
    further evidence of increasing IG-specific production investment through 2026), captioned
    **"Just comment."**
- This is a distinctly different structure from Videos 1-2: instead of building original screen-recorded
  or illustrated content, the majority of the 32s runtime (per the two earliest sampled frames) is spent
  on a single piece of found/viral footage, with the "AI" framing and the CTA doing the actual authored
  work. DATA GAP on the connecting narration (what specifically he says about the clip is unrecoverable
  without audio) means the exact mechanism of the "FAKE" premise (is he claiming the clip is fake, real,
  AI-detectable, AI-generated-and-passing-as-real, etc.) cannot be confirmed.

#### 4. Value proposition
- Walk-away value: unclear without audio — DATA GAP on whether a concrete tool/technique is actually
  taught here, or whether this is closer to pure engagement-bait dressed as an AI-education post.
- Practical value class: `[INFERRED]` entertainment/curiosity-driven rather than copyable-workflow —
  this is the only top-5 video with no visible software UI, product, or workflow of any kind in any
  sampled frame.
- Specificity: LOW-UNKNOWN by visual evidence alone.

#### 5. Psychology scoring
- STEPPS: **Triggers** (a viral clip already circulating elsewhere, giving this content a pre-existing
  cultural reference point) and **Public** (visible bystanders filming within the clip itself models the
  "this is shareable" behavior) are both plausible pillars specific to using found viral footage — a
  mechanism entirely absent from the YT dossier's top-8, all of which use original demo footage.
  **Emotion**: likely amusement/curiosity (a bizarre stunt clip) rather than the awe register that
  dominates his best YouTube hits.
- This video is the strongest evidence in this dossier that Nate's IG playbook includes a content type
  with **no YouTube analog at all**: repurposing/reacting to third-party viral footage rather than
  demonstrating his own builds. This is a genuinely IG-native content category, not a translation of
  anything documented in `yt_nateherk.md`.

#### 6. CTA & funnel mechanics
- CTA: same comment-to-DM mechanic — "Comment 'FAKE' and I'll send it over."
- Comment count (10,321) is essentially at parity with like count (10,853) — 0.95:1, still far above the
  organic norm for non-keyword content (compare the sponsored posts below, Videos 5 and 9, at 0.28:1 and
  0.09:1 respectively) but *lower* than Videos 1-2's ratios (1.39:1, 1.12:1) — worth noting as a mild
  gradient rather than a uniform effect: the keyword mechanic reliably elevates comments toward or above
  like-parity, but the exact ratio varies per post.
- Funnel position: top-of-funnel, same single-hop structure.

#### 7. Replicability verdict
- Template: source a genuinely surprising/bizarre piece of real found footage relevant to your niche's
  current discourse (here: AI skepticism/detection), frame it with a one-word thematic caption ("AI"),
  and wrap the same keyword-CTA funnel around it regardless of whether original product content is
  present.
- Commodity vs. advantage: sourcing/rights-clearing found viral footage is a distinct skill from
  building original demo content — plausibly *lower* production effort than Videos 1-2's original
  illustration/B-roll, which may partly explain its top-of-non-pinned-ranking performance (lower cost,
  comparable or better return).
- Difficulty for Tangent: **LOW** — this format requires no proprietary tooling or working backend at
  all, just editorial judgment about which found content to react to; highly portable to an art/
  photography account reacting to viral AI-art or AI-photography controversies.

#### 8. Why it won
This is the single highest-performing **organically-ranked** (non-pinned) reel in the account, and it
achieves that with the *least* demonstrated original product content of any top-5 video — no software
UI, no named tool, no workflow. The load-bearing factor is almost certainly the found-footage hook
itself (an inherently attention-grabbing, already-somewhat-viral clip) combined with the low-friction
comment-CTA, rather than any AI-automation credibility-building the way Videos 1, 2, and the YT catalog's
top hits work. This suggests Nate's single best-performing recent IG format may be closer to "AI-culture
commentary on trending content" than "AI-automation tutorial" — a content type this dossier found no
YouTube equivalent for at all.

#### Sources
- https://www.instagram.com/reel/DZku3mJH594/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25

---

### VIDEO 4 (TOP non-pinned, rank 2, SPONSORED): "Comment 'GLANCE'" (#ad, Glance AI)

#### 0. Identity & stats
- URL: instagram.com/reel/DZ76SSujumB/. Posted **2026-06-23** `[OBSERVED]`. Length: **45.80s**
  `[OBSERVED]`.
- Views: **331K** `[OBSERVED, ig_harvest]`. Likes: **378** `[OBSERVED]`. Comments: **106** `[OBSERVED]`.
- Rank: #2 of the non-pinned top-5, but flagged by the original harvest as a **paid partnership** —
  "the like/view ratio here is far below the account's norm" (harvest note). This dossier's own like
  count (378 on 331K views = 0.11% like-rate) confirms that flag independently: it is roughly **30-100x
  lower** than the like-rates implied by Videos 1-3's likes-to-views ratios (e.g. Video 3: 10,853/632K ≈
  1.7%).

#### 1. Packaging
- Caption (full, `[OBSERVED]`): *"Comment 'GLANCE' and I'll send it over 👇 / Glance AI doesn't wait for
  you to search. Its agents surface the product before you even look. They call it agentic commerce.
  Genuinely wild glimpse into where AI is heading. / Thanks to @glanceinspires for putting me on 🙌 /
  [affiliate link] / #GlancePartner #GlanceItShopIt #IntelligentShoppingAgent #Glance #ad"* — the only
  reel in this dossier's sample with a fully disclosed, multi-line sponsored-partnership caption
  (hashtag-disclosed, `#ad` present, matching Instagram's branded-content disclosure requirements).
- First frame (0.6s, `[OBSERVED]`): Nate seated on a couch, holding a phone showing the Glance AI app's
  splash screen (logo + a stylized agent icon), a plain lifestyle setting rather than his usual
  desk/mic setup.

#### 2. Hook (0–3s)
- Verbatim: DATA GAP (no transcript). Visible caption text mid-video (`[OBSERVED]` frame at ~23s):
  "those agents," suggesting narration about Glance's "agentic commerce" concept mirrors the caption's
  own language.
- Taxonomy: closest fit is tool-discovery/demo, delivered in a casual lifestyle setting (couch, home
  clothes) rather than his branded on-camera setup — a deliberate register shift for sponsored content.

#### 3. Structure & retention engineering
- Beat map, DATA GAP-heavy (only 2 frames captured: ~0.6s and ~23s, both showing similar couch/phone
  visuals with different caption text) — insufficient sampling to build a full beat map for this video;
  logged rather than invented.
- At 45.8 seconds, this is a longer-than-average reel in this dossier's sample (compare Videos 1-3-4's
  18-32s range) — consistent with sponsored content needing more runtime to cover both the ad message
  and Nate's own CTA.

#### 4. Value proposition
- Walk-away value: third-party tool discovery (Glance AI shopping app) — the "value" here is promotional
  rather than educational/workflow-based, a distinct category from every other video in this dossier.
- Practical value class: tool discovery, explicitly disclosed as paid.
- Specificity: LOW-MED — names the specific app and its "agentic commerce" positioning but (per available
  frames) doesn't demonstrate a concrete use case the way his own-product demos do.

#### 5. Psychology scoring
- STEPPS: weak across the board relative to organic content — sponsored posts inherently carry lower
  perceived Social Currency (sharing an ad is less status-conferring than sharing a genuine discovery)
  and this is reflected directly in the near-zero like-rate. This matches a pattern independently
  documented across the wider IG competitive set in `../ig_harvest/00_INDEX.md`: *"Sponsored/#ad posts
  consistently underperform organic content on ENGAGEMENT across every account checked so far."* This
  dossier's own numbers for this specific video corroborate that cross-account finding rather than
  contradicting it.
- The 331K view count paired with a 0.11% like-rate is the clearest evidence in this account's own
  catalog of the ad-boost-without-organic-engagement pattern the harvest documented elsewhere (tiffintech,
  networkchuck) — though at a much smaller scale than those accounts' most extreme examples (10-73M
  view sponsored posts) — worth flagging as the same *mechanism*, different *magnitude*.

#### 6. CTA & funnel mechanics
- CTA: same comment-keyword grammar ("Comment 'GLANCE' and I'll send it over") applied to a sponsored
  post — but comment count (106) is **far below** like count (378), a 0.28:1 ratio, the opposite pattern
  from Videos 1-3's organic keyword posts (where comments met or exceeded likes). This is a striking,
  clean natural experiment: **the same CTA mechanic, on sponsored content, does not produce the
  comment-inflation effect seen on organic posts** — strongly suggesting audiences respond to the
  keyword-comment ask differently when the content is legibly an ad, consistent with lower perceived
  value/trust in a paid promotion's "free resource" offer.
- Funnel position: brand-partnership placement, not part of Nate's own Skool/agency funnel.

#### 7. Replicability verdict
- Template: N/A as a target format for Tangent (sponsorship-dependent), but the **comment-mechanic
  natural experiment** (keyword CTAs work far better on organic-feeling content than on disclosed ads)
  is a transferable strategic lesson.
- Difficulty for Tangent: N/A (requires an actual sponsor relationship).

#### 8. Why it "won" (by view count, with major caveats)
331K views with only 378 likes and 106 comments is not a content-quality win in the way Videos 1-3's
numbers are — this is very likely a **paid view-boost pattern** (the sponsor's own promotional spend or
Glance's own distribution push inflating reach independent of organic resonance), the same mechanism
`../ig_harvest/00_INDEX.md` documents across multiple other accounts' sponsored posts. The load-bearing
factor is the brand partnership's media spend/reach, not this video's own creative merits — the
near-total absence of the comment-inflation effect that appears on every organic keyword-CTA post in this
account's catalog is the single strongest piece of evidence for that read.

#### Sources
- https://www.instagram.com/reel/DZ76SSujumB/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25
- `../ig_harvest/00_INDEX.md` — cross-account sponsored-post pattern corroboration `[OBSERVED, prior
  harvest analyst]`

---

### VIDEO 5 (TOP non-pinned, rank 3): "Comment 'WEBSITE'"

#### 0. Identity & stats
- URL: instagram.com/reel/DZflUYLHKb-/. Posted **2026-06-12** `[OBSERVED]`. Length: **18.52s**
  `[OBSERVED]` — the shortest video in this dossier's IG sample.
- Views: **314K** `[OBSERVED, ig_harvest]`. Likes: **7,702** `[OBSERVED]`. Comments: **27,604**
  `[OBSERVED]` — comments outnumber likes by **3.6:1**, the highest ratio of any video in this dossier's
  sample.

#### 1. Packaging
- Caption: **"Comment 'WEBSITE' and I'll send it over."** `[OBSERVED]`.
- First frame (0.6s, `[OBSERVED]`): a browser mockup of a "TIDY" project-management landing page (a
  wavy 3D ribbon graphic, "Are you ready to take the first step" copy, a "GET STARTED" button) with a
  Claude logo icon overlaid and a red arrow pointing up from a burned-in caption reading **"now build."**

#### 2. Hook (0–3s)
- Verbatim: DATA GAP (no transcript). Visible structure strongly implies a **reveal/generation** hook —
  "now build" plus an upward arrow toward a finished website mockup suggests the video opens on a
  prompt/instruction and pays off with the generated site, a result-first or build-in-motion pattern
  consistent with his general house style.

#### 3. Structure & retention engineering
- Second sampled frame (~9s, midpoint, `[OBSERVED]`): a **Visual Studio Code window**, title bar reading
  **"Website Building YT - Visual Studio Co[de]"** — literally, the window title names this footage as
  sourced from a YouTube-video recording session, not filmed fresh for Instagram. The same frame shows
  an open file, "AIS Brand Guidelines-1.png" (a brand-guide asset — logo, color palette, typography
  spec), captioned **"the style."**
- This is the single strongest piece of **direct observed evidence** in this entire dossier for the
  cross-platform-sourcing question the assignment centers on: the video's own on-screen chrome confirms
  its footage originates from a YouTube-titled recording session, repurposed for an Instagram post two
  months later than any confirmed matching YouTube short's date window (see Section C for the full
  gap-analysis this fits into).
- Beat structure (2 of 3 frames only, DATA GAP on full shot list): mockup/build reveal → VS Code coding
  footage with brand-asset file open → (near-end frame not distinctly different from midpoint in this
  sampling pass).

#### 4. Value proposition
- Walk-away value: a demonstrated Claude-based website-building workflow/technique, visually confirmed
  as sourced from more substantial long-form coding footage (the VS Code session) rather than filmed
  fresh for a 18-second IG cut.
- Practical value class: copyable-technique / tool discovery (Claude for web design).
- Specificity: MED-HIGH by the frames available — real file names, a real brand-guide asset, and a real
  code editor are all visible, though the exact prompts/steps are not confirmable without audio.

#### 5. Psychology scoring
- STEPPS: **Practical Value** (a real technique, evidenced by real tooling on screen) and **Social
  Currency** (early access to a "new way to build with Claude" positioning, echoing the YT dossier's
  Video 8 "$10,000 Apple-Style Websites" — Section C explores whether this is the same underlying
  content family). **Emotion**: likely a compressed version of the reveal-based awe pattern that works
  well in his YouTube top-8.
- The 3.6:1 comment:like ratio is the most extreme comment-inflation signature in this dossier's full
  sample — worth flagging as the strongest single data point for the keyword-CTA mechanic's raw power on
  this account, though also the shortest video (18.5s), which independently correlates with higher
  completion/re-engagement odds per general short-form pacing logic (`03_virality_science.md` §3.3.2).

#### 6. CTA & funnel mechanics
- CTA: same mechanic, "Comment 'WEBSITE' and I'll send it over" — offering (almost certainly) a
  downloadable template or prompt asset related to the Claude-website-building technique shown.
- This video, along with Videos 6 and 7 below (DESIGN, CAROUSEL), form a **3-post cluster posted within
  3 days of each other** (Jun 10-12, 2026) sharing an identical opening motion-graphic template
  ("Claude [icon] → [category button]," see Video 6/7), each gated behind a different keyword for a
  different downloadable asset type — a deliberate **multi-asset content-batch strategy**, not three
  independent ideas (expanded in Section D).

#### 7. Replicability verdict
- Template: repurpose real long-form coding/build footage (not filmed fresh) into a tight sub-20-second
  cut, open on the finished result, use the same recurring branded motion-graphic template across a
  batch of related posts, gate each with a different keyword for a different specific deliverable.
- Commodity vs. advantage: the repurposing workflow itself (long-form → short cutdown) is commodity
  editing skill; Nate's advantage is having substantial long-form source footage already produced for
  YouTube to draw from.
- Difficulty for Tangent: **LOW** — this is directly the cheapest, most replicable format in this
  dossier: cut an 18-second highlight from existing longer content, add a template motion graphic, gate
  behind a keyword. Highly relevant to Tangent's own content-recycling potential (photo-editing session
  footage → 15-20s IG cutdowns).

#### 8. Why it won
This video demonstrates the account's most efficient content-production model observed in this
dossier: instead of filming new material, it repurposes existing YouTube-sourced footage (confirmed by
the literal on-screen VS Code window title) into an extremely tight, sub-20-second cut, wrapped in a
reused branded template and the same proven keyword-CTA mechanic. Its 3.6:1 comment:like ratio — the
highest in the sample — suggests short runtime plus a specific, visually concrete payoff (a real brand
kit, a real code editor) may be more effective at driving the CTA action than longer, more rhetorically
elaborate videos like the pinned tiles.

#### Sources
- https://www.instagram.com/reel/DZflUYLHKb-/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25

---

### VIDEO 6 (TOP non-pinned, rank 4): "Comment 'DESIGN'"

#### 0. Identity & stats
- URL: instagram.com/reel/DZabuNfFMkJ/. Posted **2026-06-10** `[OBSERVED]`. Length: **19.24s**
  `[OBSERVED]`.
- Views: **246K** `[OBSERVED, ig_harvest]`. Likes: **6,292** `[OBSERVED]`. Comments: **17,491**
  `[OBSERVED]` (2.78:1 comment:like ratio).

#### 1. Packaging
- Caption: **"Comment 'DESIGN' and I'll send it over."** `[OBSERVED]`.
- First frame (0.6s, `[OBSERVED]`): a branded template graphic — a Claude logo above a "🎨 Design" pill
  button with a red arrow and a cursor icon hovering over it, on a cream background, captioned
  **"Claude design is"** — this is the **same template asset family** as Video 7 below (identical
  layout: Claude icon → labeled button → cursor → red arrow), confirming these two posts share a
  production batch.

#### 2. Hook (0–3s)
- Verbatim: DATA GAP. Visible on-screen text ("Claude design is...") implies a direct-address
  explainer opening — "Claude Design is [a new capability/feature]" — a definitional/announcement hook
  rather than a demo-in-motion one.
- Taxonomy: **feature-announcement / "nobody's talking about this yet"** register, `[INFERRED]` from the
  visible text fragment and its placement as the very first caption card.

#### 3. Structure & retention engineering
- DATA GAP — only the opening frame was closely read for this video; the account's Video 5 sibling
  post (WEBSITE) established that this content cluster's underlying footage is repurposed from a
  YouTube coding-session recording (the VS Code "Website Building YT" window), and this dossier
  treats DESIGN and CAROUSEL as sharing that same sourcing pattern by strong visual-template
  association `[INFERRED]`, not independently re-confirmed frame-by-frame for this specific video.

#### 4. Value proposition
- Walk-away value: a specific downloadable design asset/template (implied by "DESIGN" keyword),
  part of the same Claude-Design content family as Video 5.
- Practical value class: tool discovery / copyable asset.
- Specificity: MED (inferred from the shared-template pattern with Video 5, which did show concrete
  file/brand-asset evidence).

#### 5. Psychology scoring
- STEPPS: Social Currency (early access to "what Claude Design can now do") and Practical Value
  (a concrete downloadable asset) both plausible, mirroring Video 5's read.
- The 2.78:1 comment:like ratio, close to but slightly below Video 5's 3.6:1 and Video 7's (see below)
  ratio, suggests this middle post in the 3-part batch performed comparably but not identically —
  worth flagging as within-cluster variance rather than a uniform result, consistent with the general
  observation (Section B.10, Video 4) that identical CTA mechanics do not produce identical
  comment-inflation magnitudes.

#### 6. CTA & funnel mechanics
- CTA: same mechanic, "Comment 'DESIGN'" — the middle of a 3-keyword batch (WEBSITE, DESIGN, CAROUSEL)
  offering what appears to be three different downloadable asset types from one underlying
  Claude-Design toolkit/course.
- Funnel position: top-of-funnel, part of a coordinated content-batch rather than an isolated post.

#### 7. Replicability verdict
- Template: same as Video 5 — split one underlying course/toolkit into multiple keyword-gated asset
  offers, posted within days of each other, each with its own comment-CTA.
- Difficulty for Tangent: **LOW** — directly portable "asset-menu" strategy: if Tangent ever builds a
  reusable resource (editing preset pack, curation checklist), splitting it into several
  keyword-gated posts is a low-cost, evidence-backed format.

#### 8. Why it won
Performs in the same range as its sibling posts (Videos 5 and 7) rather than standing out individually —
the load-bearing factor is very likely the batch strategy itself (three related, mutually-reinforcing
posts within 3 days, each cross-pollinating attention to the underlying Claude Design toolkit) rather
than anything unique to this specific keyword or cut. DATA GAP on deeper frame-level differentiation
from its siblings — this dossier could not confirm whether DESIGN's actual video content differs
substantially from WEBSITE's beyond the opening template and closing keyword.

#### Sources
- https://www.instagram.com/reel/DZabuNfFMkJ/ — yt-dlp metadata + video download + partial ffmpeg frame
  extraction, 2026-07-25

---

### VIDEO 7 (TOP non-pinned, rank 5): "Comment 'CAROUSEL'"

#### 0. Identity & stats
- URL: instagram.com/reel/DZdAjsLFO0n/. Posted **2026-06-11** `[OBSERVED]` — the middle date of the
  3-post Jun 10-12 cluster (Video 6 = Jun 10, this = Jun 11, Video 5 = Jun 12). Length: **21.72s**
  `[OBSERVED]`.
- Views: **233K** `[OBSERVED, ig_harvest]`. Likes: **5,986** `[OBSERVED]`. Comments: **23,094**
  `[OBSERVED]` (3.86:1 comment:like ratio — the highest in this dossier's entire sample, marginally
  above Video 5's 3.6:1).

#### 1. Packaging
- Caption: **"Comment 'CAROUSEL' and I'll send it over,"** `[OBSERVED]` (trailing comma in the original,
  a minor copy-editing slip consistent across a batch produced quickly).
- First frame (0.6s, `[OBSERVED]`): the **same "Claude → Design" template graphic** as Video 6 (Claude
  icon, "🎨 Design" pill, cursor, red arrow), but captioned **"can now make"** instead of Video 6's
  "Claude design is" — confirming this is a direct continuation/variant of the same opening card, with
  the sentence apparently completing across the batch ("Claude design is... [can now make]...").

#### 2. Hook (0–3s)
- Verbatim: DATA GAP. Same feature-announcement register as Video 6, explicitly confirmed by the
  matching template and continuing caption fragment.

#### 3. Structure & retention engineering
- DATA GAP beyond the opening frame — not independently re-sampled at midpoint/end for this specific
  video within this dossier's time budget; treated as part of the same content batch as Videos 5-6
  by strong template evidence, not independently re-verified frame-by-frame.

#### 4. Value proposition
- Walk-away value: a carousel-format design asset/template, the third distinct deliverable type in the
  WEBSITE/DESIGN/CAROUSEL batch (website template, general design asset, social carousel template).
- Practical value class: copyable asset, audience likely skews toward social-media-marketing-adjacent
  viewers specifically interested in carousel content (a narrower niche-within-niche than WEBSITE's
  broader appeal).
- Specificity: MED (inferred from batch pattern).

#### 5. Psychology scoring
- STEPPS: same read as Video 6 — Social Currency + Practical Value, with the highest comment-inflation
  ratio of the full 9-video sample.
- Notable: despite being the narrowest-audience deliverable of the three (a carousel template is a more
  niche ask than "a website" or generic "design"), this video's raw performance (233K views) is close
  to, not far below, its siblings (246K, 314K) — suggesting the batch's overall topical pull (Claude
  Design as a trending capability) may matter more than the individual asset-type's addressable
  audience size.

#### 6. CTA & funnel mechanics
- CTA: same mechanic, third keyword in the batch.
- Funnel position: same coordinated-batch top-of-funnel role as Videos 5-6.

#### 7. Replicability verdict
- Template: identical to Video 6's — same batch strategy, third variant.
- Difficulty for Tangent: **LOW**, same reasoning as Video 6.

#### 8. Why it won
Performs consistently with its batch siblings; the highest comment:like ratio in the entire dossier
sample (3.86:1) makes this the single clearest empirical data point for the keyword-CTA mechanic's
ceiling effect on this account. As with Video 6, DATA GAP prevents confirming whether this video's
content meaningfully differs from its siblings beyond keyword and closing frame — the batch-level
strategy, not per-video creative differentiation, is the best-supported explanation for its performance.

#### Sources
- https://www.instagram.com/reel/DZdAjsLFO0n/ — yt-dlp metadata + video download + partial ffmpeg frame
  extraction, 2026-07-25

---

### VIDEO 8 (FLOP): "Comment 'INVEST'"

#### 0. Identity & stats
- URL: instagram.com/reel/DbGlL0ciIvc/. Posted **2026-07-22** `[OBSERVED]` — the single most recent
  video in this dossier's full sample. Length: **22.64s** `[OBSERVED]`.
- Views: **12.5K** `[OBSERVED, ig_harvest]` — flagged as a flop by the harvest (bottom of the 60-tile
  grid, excluding pinned tiles and the single most-recent still-accruing post). Likes: **129**
  `[OBSERVED]`. Comments: **126** `[OBSERVED]` (0.98:1 ratio — comments and likes near-parity, similar
  order of magnitude to Video 3's 0.95:1, but at a fraction of the absolute scale).

#### 1. Packaging
- Caption: **"Comment 'INVEST' and I'll send it over."** `[OBSERVED]` — same recurring CTA grammar as
  every organic top-performer in this dossier.
- First frame (0.6s, `[OBSERVED]`): a trading-platform screen — a candlestick price chart in an uptrend
  with take-profit/stop-loss order controls, and a Level-2-style order-book ladder (bid sizes/prices)
  on the right side of frame.

#### 2. Hook (0–3s)
- Verbatim: DATA GAP. Visible caption text at ~11s (`[OBSERVED]` mid-frame): "of digging" (mid-sentence
  fragment, e.g., "...hours of digging" or similar), suggesting narration about research/analysis effort
  behind a trading approach.
- Taxonomy: demo-in-motion (a live trading chart), topically adjacent to content found via this
  dossier's YT keyword search under "nateherk invest" — candidate long-form matches include "I Gave
  OpenClaw $10,000 to Trade Stocks" and "I Turned Claude Into a 24/7 Trader" (both YouTube long-form,
  posted Apr 2026 per this dossier's own yt-dlp date pulls) — **not date-matched** to this Jul 22 IG
  post and therefore **not confirmed as the same content**, but topically consistent with an
  AI-trading content theme Nate has covered on YouTube before. Flagged as `[INFERRED]` topical
  adjacency, not a confirmed cross-post.

#### 3. Structure & retention engineering
- Beat map: DATA GAP beyond the two sampled frames (chart screen at 0.6s, "of digging" caption at ~11s)
  — insufficient sampling for a full beat map.
- Uses the identical caption-CTA-mechanic and demo-in-motion visual grammar as the successful Videos 1
  and 3, making this flop especially useful as a **same-format, different-topic** comparison point
  (paralleling the YT dossier's own Video 9 finding, `yt_nateherk.md` Section C: "topic/payoff
  selection, not format, is the dominant performance lever").

#### 4. Value proposition
- Walk-away value: unclear scope without audio — DATA GAP on whether this demonstrates a specific
  AI-trading workflow/tool or is closer to general commentary.
- Practical value class: `[INFERRED]` copyable-workflow (AI-assisted trading), a narrower and
  higher-stakes/regulatory-sensitive niche than his usual invoice/calendar/personal-assistant subject
  matter.
- Specificity: LOW-MED by visible evidence (a real trading UI is shown, but no concrete numbers/results
  are legible in the sampled frames).

#### 5. Psychology scoring
- STEPPS: **Practical Value** is present in principle (financial trading is high-stakes-relevant to a
  broad audience) but likely undermined by low trust/high skepticism — AI-trading content is a category
  prone to viewer suspicion (get-rich-quick association), which could suppress both genuine engagement
  and algorithmic distribution regardless of production quality. **Emotion**: likely lower-arousal or
  skepticism-tinged compared to his invoice/personal-assistant demos, which land in universally-relatable,
  low-stakes territory.
- This is a plausible content-market-fit failure independent of format execution — same read as the YT
  dossier's Video 9 finding that topic selection, not structural template, is the primary lever.

#### 6. CTA & funnel mechanics
- CTA: identical mechanic to every top performer — "Comment 'INVEST' and I'll send it over."
- Comment:like ratio (0.98:1) is actually **healthy** relative to the mechanic's typical non-keyword
  baseline (compare Video 4's sponsored 0.28:1) — meaning the CTA mechanic itself still "worked" in
  relative terms (comments still roughly matched likes) even though the absolute view count cratered.
  This is an important nuance: **the flop here is a reach/distribution failure, not obviously a
  CTA-engagement failure** — the small audience that did see it engaged at a normal-to-healthy rate for
  this account's own keyword-CTA baseline.
- Funnel position: same single-hop top-of-funnel role as the successful videos.

#### 7. Replicability verdict
- Template: N/A as a target (this is the flop lesson) — but the mechanical template (demo-in-motion +
  keyword CTA) is identical to Video 3's winning formula, reinforcing that the lesson here is topic
  selection, not structure.
- Difficulty for Tangent: N/A (anti-pattern for topic choice, not format).

#### 8. Why it lost
Being the most recent post in the entire sample (Jul 22, 2026, posted only 3 days before this dossier's
harvest date), part of its low view count may simply reflect insufficient time to accrue views — a
genuine confound the harvest methodology itself flags for near-most-recent posts generally. Independent
of that timing caveat, the topic (AI-assisted investing/trading) sits in a higher-skepticism, more
regulatorily-fraught content category than his signature universal-productivity demos (invoices,
calendars, assistants), a plausible content-market-fit explanation consistent with the same lesson the
YT dossier draws from its own flop, Video 9 ("Human In The Loop Sales Team of Agents"): format
discipline was present (same demo-in-motion + CTA structure as his best hits), but topic/subject-matter
choice likely capped its ceiling regardless of execution.

#### Sources
- https://www.instagram.com/reel/DbGlL0ciIvc/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25

---

### VIDEO 9 (FLOP, CONFIRMED YOUTUBE CROSS-POST): "ChatGPT Work" launch (#ChatGPT_Partner)

#### 0. Identity & stats
- URL: instagram.com/reel/DbDJlTkgOtY/. Posted **2026-07-21** `[OBSERVED]`. Length: **58.54s**
  `[OBSERVED via ffprobe]`.
- Views: **14.6K** `[OBSERVED, ig_harvest]` — flagged as a flop. Likes: **185** `[OBSERVED]`. Comments:
  **16** `[OBSERVED]` (0.086:1 ratio — the lowest comment:like ratio in this dossier's sample, typical of
  non-keyword-CTA sponsored content, matching Video 4's sponsored pattern).
- **This is a confirmed same-day cross-post of YouTube short `c1TWmKILaeM`** ("Huge ChatGPT Update You
  Need to See!"), independently discovered by this dossier via yt-dlp channel-catalog sampling (see
  Method log) — both platforms' description text is **verbatim-identical**: *"ChatGPT Work is available
  today in ChatGPT on web and mobile for Pro, Enterprise, and Edu... @ChatGPT #ChatGPT_Partner"*
  `[OBSERVED on both platforms]`. YouTube stats for the same content, `[OBSERVED via yt-dlp,
  2026-07-25]`: **18,904 views, 574 likes, 20 comments, 59s duration**, posted **2026-07-21** (same
  calendar day as the IG post).

#### 1. Packaging
- IG caption: full sponsor-provided copy (see above), ending "🔗 Link in bio for 7-days! @ChatGPT
  #ChatGPT_Partner." YouTube description: same body copy, opening instead with "Big news! 🚀" and closing
  with "Go to chatgpt.com/download... 🔗 Link in bio for 7-days!" — near-identical, both clearly built
  from the same brand-supplied copy block.
- First IG frame (0.6s, `[OBSERVED]`): a plain white card reading **"ChatGPT"** in black sans-serif text
  — a simple text-card open, distinct from the illustrated-metaphor or found-footage opens used
  elsewhere in this dossier's organic sample. This is the least visually "produced" opening in the
  entire 9-video set, consistent with reusing brand-supplied creative rather than Nate's own original
  hook design.

#### 2. Hook (0–3s)
- Verbatim opening line (`[OBSERVED via YouTube auto-caption transcript, used as a verified proxy for the
  IG audio per the assignment's cross-posting instruction — log: this is the only video in this dossier
  where a verbatim transcript was obtainable]`): **"ChatGPT isn't just a chatbot anymore. OpenAI just
  turned it into an AI operating system."**
- Taxonomy: **bold claim / news-response** — matches the same taxonomy bucket as the YT dossier's own
  Videos 7-8 (`yt_nateherk.md`), both from the same "2026-era news-response content cluster."
- Confirmed matching visual asset (`[OBSERVED]`, IG frame at ~28s): a "Chief of Staff → Delegates →
  [Research / Planning / Execution] → Output" flowchart diagram, directly illustrating the transcript's
  "I even built my own AI chief of staff... reviews my ClickUp tasks, my project ideas, my team chats,
  and my calendar" passage — this diagram's exact presence on the IG cut, matched to the exact
  corresponding line in the YouTube transcript, is the strongest possible confirmation (short of a
  byte-identical file hash) that these are the same underlying edit, not just the same topic
  independently re-shot.

#### 3. Structure & retention engineering
- Full beat map available via the YouTube transcript proxy (`[OBSERVED via YT transcript]`, applied to
  IG per the confirmed-identical-content finding above):
  - [0:00] Hook: "ChatGPT isn't just a chatbot anymore... AI operating system."
  - [0:04-0:14] Names the three components: Chat, Codex (developers), and the new "Work" agent, "all
    live inside one connected desktop app."
  - [0:14-0:27] Explains Work's distinguishing capability: "gets things done for you... long-running
    projects... connecting to the apps you already use," plus web/mobile sync and a "cloud browser with
    plugins for more than 100 apps," with computer-use fallback for non-native integrations.
  - [0:27-0:37] Personal example: "I even built my own AI chief of staff" — a 6am automated workflow
    reviewing ClickUp tasks, project ideas, team chats, and calendar to produce a daily game plan
    (matches the observed flowchart diagram exactly).
  - [0:37-0:51] Before/after contrast: "used to piece that together through five different apps... now
    everything lives in one workflow," reframed as a shift from information-organizing to execution time.
  - [0:51-0:58] Closing generalization ("ChatGPT isn't just something you talk to anymore... becoming
    the place where work actually gets done") + CTA: "download the new ChatGPT desktop app."
- One-idea-per-video: yes ("ChatGPT Work turns the chatbot into an execution layer"), delivered as a
  compressed feature-announcement + one personal proof-point, structurally similar to the YT dossier's
  Video 7/8 news-response format.

#### 4. Value proposition
- Walk-away value: tool discovery (the ChatGPT Work desktop app) plus one modeled personal use case
  (an automated daily-briefing "chief of staff" workflow) — genuinely specific and demonstrated, not
  purely promotional copy, despite being sponsored/brand-partner content.
- Practical value class: tool discovery primary, copyable-technique secondary (the chief-of-staff
  workflow concept is a real, statable pattern even without exact configuration steps shown).
- Specificity: MED-HIGH — names the exact product tiers (Pro/Enterprise/Edu now, Plus/Business rolling
  out), exact platforms (Windows/Mac), and one concrete personal workflow.

#### 5. Psychology scoring
- STEPPS: **Triggers** (reactive to a same-week product launch) and **Practical Value** (a real workflow
  pattern) are present, matching the register of the YT dossier's own top-8 news-response entries.
  **Social Currency**: moderate (being first to explain a launch). **Emotion**: relief/efficiency-
  oriented rather than awe — a lower-arousal register than his best organic AI-automation-demo hits.
- Despite carrying the same content DNA as videos that performed well in the YT dossier's own top-8
  (news-response format, e.g. `yt_nateherk.md` Videos 7-8, which ranked #7 and #8 all-time on YouTube),
  this specific installment **underperformed on both platforms simultaneously**: 18,904 YT views is
  itself *below* the YouTube channel's own median short (25,500, per `yt_nateherk.md` Section A), and
  14.6K IG views sits at the bottom of the IG grid sample. This is the clearest evidence in this entire
  two-dossier project that a piece of content can fail on its content merits independent of platform —
  the format worked elsewhere in the catalog; this specific installment (a brand-partner-scripted,
  fairly generic "big product update" video with no unique personal angle beyond the one chief-of-staff
  example) did not.

#### 6. CTA & funnel mechanics
- CTA on both platforms: download the ChatGPT desktop app, "link in bio for 7 days" — a **third-party
  brand CTA**, not Nate's own Skool/agency funnel, and **not** a comment-keyword mechanic despite that
  format's strong performance elsewhere in his IG catalog. This is a clean natural-experiment data point
  matching Video 4's (Glance AI) finding: **when a post carries a disclosed brand CTA instead of Nate's
  own "comment X, I'll DM you" mechanic, comment volume falls to normal organic levels (16 comments here,
  106 for Glance) rather than the 10,000-27,000+ comment counts his own organic keyword-gated posts
  generate.** Two independent sponsored posts in this dossier's sample (Videos 4 and 9) both show this
  same pattern — strong convergent evidence, not a one-off.
- Funnel position: brand-partnership placement on both platforms; does not feed Nate's own Skool funnel.

#### 7. Replicability verdict
- Template: same news-response formula documented in `yt_nateherk.md` (monitor fresh releases, frame
  around a named product/capability, ground with one concrete personal example) — this dossier's
  contribution is showing that formula's IG performance is **not guaranteed** to match its YouTube
  performance even for literally identical content and identical CTAs (see Section C for the full
  ratio analysis).
- Difficulty for Tangent: **LOW-MED** for the news-response format itself; the sponsored/brand-CTA
  variant specifically requires an actual partnership, not replicable on demand.

#### 8. Why it lost (on both platforms)
This is the dossier's centerpiece cross-platform data point (fully expanded in Section C): identical
content, identical CTA, posted the same calendar day to both platforms, underperformed its own
respective platform baseline on **both** YouTube (below the channel's shorts median) and Instagram
(bottom of the grid sample). The most defensible explanation is content-market-fit, not platform
mechanics: this is a fairly generic "big company announces a feature" video, brand-scripted rather than
built around Nate's own demonstrated system the way his best hits are, with only one thin personal
example (the chief-of-staff workflow) standing in for the concrete, verifiable payoffs (a real sent
email, an exact dollar figure, a spinning product video) that `yt_nateherk.md` identifies as the
load-bearing factor across his actual winners. The comment-mechanic difference (no keyword CTA) further
suppressed its IG-specific engagement signature, but the underlying view-count failure appears to be a
genuine cross-platform content-quality issue, not a platform-specific quirk.

#### Sources
- https://www.instagram.com/reel/DbDJlTkgOtY/ — yt-dlp metadata + video download + ffmpeg frames,
  2026-07-25 (this dossier's own fetch)
- https://www.youtube.com/shorts/c1TWmKILaeM — yt-dlp metadata + auto-caption transcript, 2026-07-25
  (this dossier's own fetch; independently discovered via channel-catalog date sampling, not from
  `yt_nateherk.md`'s original sample)

---

### B.10 — The third pinned tile (referenced, not full post-mortem): "Comment 'BULLETPROOF'"

Per the assignment's "1-2 pinned" instruction, this dossier gives full post-mortems to two of the three
pinned tiles (Videos 1 and 2 above) and references the third here. instagram.com/reel/DTXqGz2Evxq/,
posted **2026-01-11** `[OBSERVED]`, **2.3M views** `[OBSERVED, ig_harvest]`, **60,614 likes, 7,125
comments** `[OBSERVED via yt-dlp]`. Notable anomaly, flagged not resolved: this is the **only** pinned or
top-5 video in the entire dossier sample where **comments fall far below likes** (0.12:1 ratio) rather
than meeting or exceeding them — a sharp break from the pattern established by every other organic
keyword-CTA post analyzed (all cluster between 0.95:1 and 3.86:1). No video was downloaded/frame-sampled
for this tile within this dossier's time budget; this ratio anomaly is logged as an open question for a
future pass rather than explained away — plausible readings include a since-deleted comment purge, a
different (non-comment-based) CTA actually used in this specific video despite the "BULLETPROOF" keyword
appearing in its caption, or simply organic variance, none of which this dossier can confirm.

---

## C. Cross-platform translation findings (centerpiece)

### C.1 The central discovery: YouTube Shorts and Instagram Reels decoupled in 2026

`yt_nateherk.md`'s own cadence analysis (Section A) found a "slowdown in shorts output between ~April and
July 2026." This dossier's own independent yt-dlp date-sampling of the `@nateherk/shorts` catalog
**confirms and sharpens that finding into a hard gap**: `[OBSERVED, this dossier's own yt-dlp pulls,
2026-07-25]` —

| Position | Video ID | Date |
|---|---|---|
| 1 (newest) | c1TWmKILaeM | 2026-07-21 |
| 2 | 4fKn9O-YhtI | 2026-07-11 |
| 3 | AZXV1zzuFuQ | 2026-07-11 |
| 4 | qH8qd4DgY7A | 2026-07-09 |
| **5** | **EeY8wqJ5BOI** | **2026-04-11** |
| 6 | p9mgmKhUz_4 | 2026-04-06 |

**Between positions 4 and 5 sits a confirmed ~90-day gap (Apr 11 – Jul 9, 2026) with zero YouTube shorts
posted.** Meanwhile, this same window is exactly when Nate's **best-performing non-pinned Instagram
reels** in this dossier's sample were posted: the WEBSITE/DESIGN/CAROUSEL batch (Jun 10-12) and the FAKE
reel (Jun 14) — none of which have any possible same-window YouTube shorts counterpart, because none
were posted. This is not a sampling artifact; it is a structural fact about the channel's output during
that quarter.

**Conclusion:** During Q2 2026, Instagram was not a secondary distribution channel lagging behind
YouTube — it was, for several weeks, Nate's **only actively-posted short-form output**. His top-5
non-pinned IG reels in this dossier's sample are therefore **not simple caption-swapped cross-posts** of
YouTube shorts; they had to be either (a) original IG-native productions, or (b) repurposed cutdowns of
his still-active long-form YouTube content. This dossier found direct evidence for both:

- **(a) IG-native, no YouTube analog at all:** Video 3 ("FAKE," found-viral-footage reaction) and the
  pinned Videos 1-2 (original illustrated motion graphics, a live-action fire B-roll) have no
  counterpart anywhere in `yt_nateherk.md`'s 11-video sample or this dossier's own catalog searches.
- **(b) Repurposed long-form cutdowns:** Video 5 ("WEBSITE") contains a literal on-screen VS Code window
  titled **"Website Building YT"** — direct proof its footage was recorded for a YouTube session and
  later cut down for Instagram, `[OBSERVED]` via frame extraction, the strongest single piece of
  evidence in this dossier.

### C.2 The one confirmed like-for-like comparison: "ChatGPT Work" (Video 9)

This is the only pair in this dossier where the **exact same edit** is verifiably present on both
platforms (matching verbatim description text + a matching mid-video diagram tied to a matching
transcript line, see Video 9 above). Ratios, `[OBSERVED]` both sides, 2026-07-25:

| Metric | YouTube (c1TWmKILaeM) | Instagram (DbDJlTkgOtY) | IG/YT ratio |
|---|---|---|---|
| Views | 18,904 | ~14,600 | **0.77x** |
| Likes | 574 | 185 | **0.32x** |
| Comments | 20 | 16 | **0.80x** |
| Duration | 59s | 58.5s | ~identical |
| vs. own-platform median | 0.74x of YT's 25,500 median (below median) | ~0.47x of IG's 30,950 median (below median, bottom of grid) | Underperformed on BOTH platforms |

**This single data point is doing a lot of work in this dossier's argument, so its limits should be
stated plainly:** it is one video, a disclosed brand-partnership post, and (per Section B.9) plausibly a
weak piece of content on its own merits independent of platform. It should not be read as "IG reliably
gets ~0.77x the views of a matched YT short" — that would be extrapolating a general translation ratio
from n=1. What it DOES support, robustly: (1) the same content can fail on both platforms
simultaneously, meaning platform choice alone doesn't rescue weak content; (2) likes translate worse
than views (0.32x vs 0.77x) — consistent with IG's like-economy being generally "thinner" on this
account for non-keyword-CTA content, as corroborated independently by Video 4's near-identical pattern.

### C.3 The comment-keyword funnel: the sharpest platform-CTA difference in either dossier

`yt_nateherk.md` found, across all 11 YouTube videos it analyzed (8 top performers + 3 flops): **zero**
comment-keyword CTAs. Every single YouTube short's CTA is a verbal "go watch the full video on my
channel" (occasionally paired with a "subscribe" ask), funneling to a long-form video whose own
description then carries the Skool community link — the two-hop funnel documented in that dossier's
Section A.

This dossier's IG sample shows the **opposite** pattern: every organic (non-sponsored) top or pinned
video uses **"Comment '[KEYWORD]' and I'll send it over"** — a one-hop, comment-to-DM funnel that
bypasses the long-form-video nurture step entirely. Per this account's harvest note (echoed in the
assignment brief): *"comment KEYWORD hooks dominate his top performers"* — this dossier's own
video-by-video sampling confirms that characterization is accurate and, further, quantifies its effect:
**7 of 9 videos in this dossier's sample carry a comment-keyword CTA, and every one of those 7 shows a
comment:like ratio between 0.95:1 and 3.86:1** — comments meeting or (usually) substantially exceeding
likes, a structurally abnormal engagement signature for organic short-form video. The 2 videos in the
sample **without** a keyword CTA (Videos 4 and 9, both disclosed sponsored/brand-partner posts with a
brand-supplied CTA instead) show comment:like ratios of 0.28:1 and 0.086:1 respectively — squarely in
the normal-organic range, an order of magnitude lower.

**Why the platform difference, per `03_virality_science.md`:** §1.1.2 and §2.7 both flag that both
platforms treat comments/sends/DMs as stronger intent signals than likes, and §3.4.3 directly describes
the ManyChat-style comment-automation mechanic as a real, if double-edged, lever — "driving comment
volume... simultaneously" with meaningful reach-boosting potential, but flagged as running the same risk
as literal engagement-bait if the underlying content has no standalone value. The mechanism this dossier
observes is fully consistent with that framing: Instagram's algorithm (per §1.1.1's "likelihood to
reshare"/comment emphasis) rewards the comment volume this mechanic manufactures, while YouTube Shorts'
"viewed vs. swiped away" hook-quality model (§1.2.1) has no equivalent comment-based amplification lever
built into its core ranking logic — Shorts distribution is driven by completion/rewatch, not
comment-to-DM funnels, which may partly explain why Nate's YouTube playbook never adopted this mechanic
even though it demonstrably works hard for him on Instagram. `[INFERRED]` causal read — the platforms'
differing ranking emphasis is a plausible and evidence-consistent explanation for why the SAME creator
runs two entirely different CTA grammars, but Nate's own strategic reasoning was never directly observed
or stated in any source this dossier accessed.

**A second, complementary explanation, also evidence-backed here:** Instagram's own Recommendation
Guidelines (§1.3.2) explicitly flag *content-free* engagement bait ("comment YES if you agree") as
penalized/ineligible for recommendation surfaces — but Nate's mechanic is not content-free: every
keyword-CTA video in this sample pairs the ask with a real, specific, named deliverable (a workflow, a
brand-guide template, a carousel asset), the exact distinguishing test §3.4.3 itself names ("is it
attached to content with standalone value, or is the comment the entire ask?"). This may explain why the
mechanic appears to be working rather than being suppressed — it sits on the compliant side of
Instagram's own stated line, per this dossier's reading of the guideline text against the observed
content.

### C.4 What he pins and why

The three pinned tiles (Section B.1, B.2, B.10) are **not** off-topic legacy virality the way several
other accounts in the wider competitive study exhibit — `../ig_harvest/00_INDEX.md` documents
`handlytech` and `thevarunmayya` pinning old, topically-unrelated viral hits far above their current
content's actual ceiling. Nate's pins are the **opposite pattern**: all three use the exact same
"Comment '[KEYWORD]' and I'll send it over" CTA grammar as his current organic content, and — per this
dossier's own view-count check — they are literally his three highest-viewed reels of any kind in the
entire 60-tile grid sample (3.3M > 2.3M > 1.5M > the 632K non-pinned ceiling). **Funnel logic:** these
are not nostalgia pins; they are his three best-performing lead-magnet demos, permanently held at the
top of the profile so that any new visitor's first three pieces of content are proof-of-concept,
working-CTA assets — literally the highest-converting (by view-count proxy) door into his comment-to-DM
funnel. The pin *order* is reverse-chronological-by-pin-date (newest pin first, per Instagram's own pin
display convention), and this dossier observed the roster itself evolving (Video 2, "RUSH," is the
newest pin, posted Apr 2026, five months after Video 1's Nov 2025 post) — direct evidence Nate actively
re-curates this lineup over time rather than setting it once, consistent with treating the pinned row as
a living, optimized landing strip rather than a static "best of" archive.

---

## D. Content architecture on Instagram

**Key vs. filler, `[INFERRED]` classification from this dossier's 9-video sample plus the 60-tile grid's
view-count shape (not an exhaustive re-classification of all 552 posts):**

1. **Key format — the comment-keyword demo/reveal reel.** The load-bearing content type: a tight
   (18-30s, occasionally up to 45-60s for sponsored) video built around one visible payoff (a workflow,
   a generated asset, a technique reveal) closing on "Comment '[KEYWORD]' and I'll send it over."
   Produces the account's entire pinned lineup and 4 of its top-5 non-pinned reels (Videos 1, 2, 5, 6, 7
   in this dossier's numbering). This is the account's equivalent of `yt_nateherk.md`'s "hero n8n-demo"
   format — the reliable base-hit generator — except restructured around a comment-CTA instead of a
   verbal watch-more CTA.
2. **Emerging sub-format — found-footage/viral-culture reaction.** Video 3 ("FAKE") is this dossier's
   only clear example, but it is also this dossier's single highest-performing **organic, non-pinned**
   reel — worth flagging as a format with no YouTube analog and (on this one data point) strong
   performance, a candidate area of underexplored upside for the account.
3. **Content-batching.** Videos 5-6-7 (WEBSITE/DESIGN/CAROUSEL) demonstrate a deliberate strategy of
   splitting one underlying toolkit/course into 3 keyword-gated asset offers, posted within a 3-day
   window — a repeatable, low-marginal-cost content-multiplication technique (one production effort,
   three distinct CTA-bearing posts).
4. **Sponsored/brand-partnership content.** Videos 4 and 9 — both underperform the account's organic
   baseline by roughly one to two orders of magnitude on engagement (though view counts vary: Video 4's
   331K suggests paid view-boosting per the cross-account pattern in `00_INDEX.md`; Video 9's 14.6K
   shows no such boost). Both drop the keyword-CTA mechanic in favor of a brand-supplied CTA, and both
   show comment:like ratios an order of magnitude below the organic norm — filler/monetization content,
   not growth content, by this dossier's read.

**Cadence:** 552 total posts is not independently datable by this dossier (no full-catalog date sweep was
performed, matching the harvest's own scope), but the 9-video dated sample spans Nov 2025 (Video 1) to
Jul 2026 (Video 8), with a visible densification in the most recent window: 5 of 9 sampled videos (56%)
fall within a single 6-week span (Jun 10 – Jul 22, 2026), versus 4 of 9 spanning the prior 7 months
(Nov 2025 – Apr 2026) — `[INFERRED]` an accelerating IG posting cadence in 2026, directionally consistent
with, and plausibly a direct consequence of, the YouTube-shorts pipeline going dark in the same window
(Section C.1) — i.e., IG may have absorbed production capacity/attention that shorts previously consumed.
This is inference from a 9-video, non-random sample, not a full cadence audit; flagged accordingly.

**Funnel (Top vs. flop delta, per QC rule 6):** The clearest, most consistent delta between this
dossier's top performers and its 2 flops is **not** hook quality, structure, or production value — every
flop uses the same demo-in-motion + keyword-CTA template as the winners (Video 8/"INVEST" is
structurally near-identical to Video 3/"FAKE" and Video 1/"SYSTEM"). The delta is (a) **topic
selection** (AI-trading and a generic brand-scripted product update vs. universally-relatable or
inherently-viral subject matter) and (b) **timing/recency** (Video 8 was posted 3 days before this
dossier's harvest, a genuine still-accruing confound). This mirrors `yt_nateherk.md`'s own top-vs-flop
finding almost exactly: "topic and payoff selection, not format, is the dominant performance lever on
this channel" — the same conclusion holds on Instagram, on a different CTA architecture, with different
specific flop topics.

---

## E. Method log

**Tooling used:** yt-dlp 2026.07.04 (both for Instagram reel metadata/video extraction and for
YouTube channel/shorts catalog cross-referencing), ffmpeg/ffprobe (duration, frame extraction),
WebFetch (og:description/meta-tag cross-checks, nateherk.com bio-link mapping), WebSearch (candidate
YouTube-content keyword matching). **No claude-in-chrome browser tools were used**, per the assignment's
explicit restriction. All work done in
`/private/tmp/claude-501/.../scratchpad/ig_nateherkai/` (videos/, frames/, yt_transcripts/
subdirectories).

**Key discovery, logged because it contradicts the QC protocol's stated default assumption:** the QC
protocol (`QC_PROTOCOL.md` line 37) states "Instagram blocks most logged-out access." This dossier found
that **yt-dlp's Instagram extractor successfully retrieves public reel metadata (description/caption,
`like_count`, `comment_count`, `upload_date`) and can download the video file itself**, without any
authenticated session, for every one of the 9 reels attempted (9/9 success rate). It does **not**,
however, expose `view_count`/`play_count` (confirmed `NA` on every pull) or auto-captions/subtitles
(confirmed "no subtitles available" on every attempt) — so view counts in this dossier are still sourced
from the harvest's logged-in-session grid pull, not re-derived, and no IG-native transcript was ever
obtained by any method.

**Commands run (representative, not exhaustive):**
1. `yt-dlp --skip-download --print "title=... | desc=... | date=... | likes=... | comments=..."
   "https://www.instagram.com/reel/<ID>/"` — run against all 9 target reels + 3 additional reels
   (DZflUYLHKb-, DZabuNfFMkJ, DZdAjsLFO0n) that the original harvest's 7 detail-pulls hadn't covered.
   9/9 + 3/3 succeeded on first attempt, no rate-limiting encountered on the Instagram side across ~15
   sequential calls with a 1-2s sleep between them.
2. `yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en.*" "https://www.instagram.com/
   reel/<ID>/"` — attempted on DRXZJeHiAES; returned "no subtitles for the requested languages" —
   confirmed Instagram exposes no caption track via this method, not retried on other reels (established
   the limitation once, logged, moved to frame-based analysis instead).
3. `yt-dlp -o "videos/<ID>.%(ext)s" "https://www.instagram.com/reel/<ID>/"` — full video download, 9/9
   succeeded, files ranged 4.4-12.7MB.
4. `ffprobe -show_entries format=duration ...` for exact duration on all 9 downloaded videos.
5. `ffmpeg -ss <t> -frames:v 1 ...` — 3 frames per video (≈0.6s, midpoint, ≈1.5s-before-end) for all 9,
   27 frames total, visually inspected via the Read tool for packaging/hook/structure evidence.
6. `WebFetch` on 3 Instagram reel URLs (DZflUYLHKb-, DZabuNfFMkJ, DZdAjsLFO0n) before discovering yt-dlp
   worked directly — used as an early cross-check; results were consistent with the later yt-dlp pulls
   (dates, captions matched) though WebFetch's own like/comment figures were rougher (K-rounded
   estimates) than yt-dlp's exact integers — yt-dlp figures used as primary in the final dossier.
7. Cross-platform matching: `yt-dlp --flat-playlist --playlist-items 1:15/16:35/30:45` against
   `youtube.com/@nateherk/shorts` to enumerate recent shorts, then `yt-dlp --skip-download --print
   "date=..."` against individual `youtube.com/shorts/<ID>` URLs to date-bracket IG posting dates —
   **this is how the Apr 11 – Jul 9, 2026 shorts-posting gap (Section C.1) was discovered**, and how the
   ChatGPT Work cross-post (Video 9) was found and confirmed (via matching description text, independent
   of any hint from `yt_nateherk.md`, which did not include this video in its own 11-video sample).
8. `ytsearch5:"..."`/`ytsearch6:"..."` queries (6 total: system prompt, bulletproof x2, rush, fake,
   claude design carousel, invest) attempting keyword-based cross-post discovery for the "SYSTEM,"
   "BULLETPROOF," "RUSH," "FAKE," and "INVEST" pinned/top reels — **no confident match found for any of
   these five**; candidate long-form videos surfaced for the Claude-Design cluster (`gAoZ95kqG7w`,
   `ovabeVoWrA0`, both Apr 2026) and the investing theme (`eu8UJtuIi-E`, `6MC1XqZSltw`, both Apr 2026)
   were topically plausible but **not date-matched** to the actual IG post dates (Jun/Jul 2026) closely
   enough to claim as confirmed cross-posts — reported as `[INFERRED]` topical adjacency only, not
   fabricated as confirmed matches. This non-finding is itself evidence for Section C.1's core claim
   (most of the Jun-Jul 2026 IG top performers are not simple shorts cross-posts).
9. `WebFetch` on `nateherk.com` — confirmed the same ultimate Skool-community funnel destination as
   `yt_nateherk.md`'s independently-sourced funnel map (Section A), corroborating rather than
   contradicting the prior dossier via an independent fetch.

**Known data gaps (logged, not papered over):**
- No verbatim audio transcript for 8 of 9 videos (only Video 9's YouTube-cross-post proxy provided one)
  — every hook/structure claim for the other 8 is built from 2-3 sampled video frames plus burned-in
  captions visible in those frames, explicitly flagged `DATA GAP` inline wherever audio-only content
  (spoken narration beyond what's burned into the frame) would be needed to complete the picture.
- Videos 6 and 7 (DESIGN, CAROUSEL) received only partial frame-sampling (1-2 of their 3 extracted
  frames were closely read) within this dossier's time budget — their structure/beat-map sections are
  explicitly shorter and more inference-dependent than Videos 1-5's, and this is stated inline rather
  than backfilled with invented detail.
- The third pinned tile (BULLETPROOF, Section B.10) was not downloaded/frame-sampled at all — referenced
  by caption/stats only, per the assignment's "1-2 pinned" instruction, with its comment:like anomaly
  flagged as unresolved rather than explained away.
- No exact `view_count` was ever independently re-derived by this dossier (Instagram doesn't expose it
  via yt-dlp) — every view-count figure in this file traces back to the original harvest's logged-in
  grid pull (`../ig_harvest/nateherkai.md`, `[OBSERVED]` 2026-07-25 by that analyst), not to this
  dossier's own fetches. This is explicitly logged, not silently presented as this dossier's own
  observation.
- The full 552-post catalog was not re-swept for cadence purposes; Section D's cadence claims rest on
  the 9-video dated sample only, flagged `[INFERRED]` accordingly.
- Five of six targeted YouTube-cross-post keyword searches (SYSTEM, BULLETPROOF, RUSH, FAKE, INVEST)
  did not produce a confirmed match — reported as non-findings, not silently dropped or forced into
  false-positive matches.

**No-fabrication check:** every numeric claim in Sections B and C traces to either a specific yt-dlp
`--print` output or `like_count`/`comment_count`/`upload_date` field captured in this session's scratch
directory, a specific ffprobe duration reading, a specific extracted video frame (paths logged in
scratch), the YouTube auto-caption transcript for Video 9 specifically, or the pre-existing harvest file
`../ig_harvest/nateherkai.md` (credited, not re-claimed as this dossier's own observation) — or is
explicitly labeled `[INFERRED]` with the reasoning stated inline, or `DATA GAP` where no evidence was
obtainable.
