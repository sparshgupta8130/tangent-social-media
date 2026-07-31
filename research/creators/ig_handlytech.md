# Creator Dossier: Ayham Joukhadar / HandlyTech (Instagram @handlytech) — NEGATIVE CASE STUDY

**Corpus role:** This is the designated negative case study in the 24-account study (see
`../ig_harvest/00_INDEX.md`). Niche: "AI in 30 seconds" tutorials + gadget/AI-tool reviews.
989K followers, median reel 9.85K views — a **1.0% median/follower ratio, the worst of all 22
ranked accounts in the study**. The account also carries 3 pinned legacy mega-hits (30.8M–73.6M
views, 2023–2025) that are off-topic relative to its current niche.

All stats as-of **2026-07-25** unless otherwise noted. Primary data source: `../ig_harvest/handlytech.md`
(grid pull + 7 original detail pulls + an "Anomaly re-verification" section appended mid-session by
a separate research agent — confirmed present on re-check, incorporated below). This dossier
independently supplements the harvest with: (a) direct `yt-dlp` metadata pulls against all 8
selected reels (cross-verifying likes/comments/dates), (b) full video downloads + 8-frame,
evenly-spaced contact-sheet extraction via `ffmpeg`/`ffprobe` for visual/structural analysis of
every selected video, and (c) `WebSearch`/`WebFetch` for media-kit and cross-platform context.
`claude-in-chrome` browser tools were NOT used (reserved per task instructions) — all IG access
went through the harvest file, `yt-dlp`, and `WebFetch`. Every substantive claim below is tagged
`[OBSERVED]` / `[REPORTED]` / `[INFERRED]` per `../templates/video_postmortem_template.md`.

---

## A) Account header

- **Handle / name:** @handlytech, Ayham Joukhadar. **Followers:** 989K. **Following:** 196.
  **Posts:** 814. [OBSERVED, `ig_harvest/handlytech.md`, harvest date 2026-07-25]
- **Bio:** "Science & Tech / AI in 30 seconds / Tutorials, honest reviews / Trusted by 1.5M
  followers (cross-platform claim) / handlytech@gmail.com" [OBSERVED, harvest og:description +
  header pull]. Independently corroborated bio text via `WebFetch` of `threads.com/@handlytech`,
  2026-07-25: "Mastering AI, Mobile & PC Tricks • Smart Tips and Honest Reviews • Trusted by 1.5M
  followers" — same "1.5M" figure repeated cross-platform [OBSERVED].
- **Follower-count variance across sources:** search-engine-cached snapshots returned via
  `WebSearch` on 2026-07-25 showed 982K, 968K, and 890.1K for the same account at unknown prior
  cache dates [REPORTED, LOW confidence, no snapshot date available] — all below this dossier's
  authoritative [OBSERVED] harvest figure of 989K. Read as ordinary account growth over time plus
  search-cache staleness, not as evidence of anything anomalous.
- **Median reel views (n=30 most recent, excluding 3 pinned):** **9.85K** [OBSERVED, computed in
  harvest file from sorted 15th/16th values 9,839 / 9,867].
- **Median/follower ratio: 1.0%** — the lowest of 22 ranked accounts in the 24-account study (see
  `00_INDEX.md` "Quick ranking" table; only `chrisdonnellyofficial` at 1.4% comes close).
  [OBSERVED/computed]
- **Pinned legacy hits (3, extreme):** 73.6M (C9PdusWtkOh, 2024-07-10), 63M (DFC6zh3iZKn,
  2025-01-20), 30.8M (CybW5zct2AA, 2023-10-15) — confirmed via independent `yt-dlp` timestamp pulls
  by this dossier, matching the harvest file's date-verification exactly. 100–1000x the rest of the
  visible grid. [OBSERVED, HIGH confidence]
- **True 2026 organic ceiling:** 331K (DZozx8UoTDy) — but this figure's status is complicated by an
  unresolved like-count anomaly (see Video 4 post-mortem and the Autopsy section). Even taking 331K
  at face value, it is 93–222x smaller than the pinned hits' view counts.
- **Cross-platform footprint (media-kit economics — the gap):**
  - ViralMango media kit (`viralmango.com/HandlyTech`, fetched 2026-07-25) [REPORTED]: Instagram
    851.5K, TikTok 494.3K, YouTube 2.4K, **stated total "1.3M."** Location listed as "Croatia"
    [REPORTED, single source, could not independently verify — a search of an "Top Influencers in
    Syria" directory (`infldb.com/top-influencers/Syria`) did not surface this account either way,
    so creator location remains a genuine DATA GAP, not confirmed in either direction].
  - Note the media kit's own IG figure (851.5K) is LOWER than this dossier's directly [OBSERVED]
    989K — i.e., on Instagram specifically the media kit under-states rather than over-states
    reach; the kit is simply stale, not padded, on that one line.
  - Media kit engagement claims [REPORTED, viralmango.com/HandlyTech]: IG "engagement rate 4.17%,"
    "average likes 33.8K," "average comments 1.6K." These numbers are **incompatible with observed
    reality**: this dossier's 8 detail-pulled reels show real like counts ranging from 59–3,595 on
    non-pinned content (median-tier reels), with the only likes counts anywhere near "33.8K" coming
    from the 3 ancient pinned posts (576K–2.1M likes each). [INFERRED, not confirmed]: the "33.8K
    average" plausibly reflects an all-time or pin-weighted average rather than a "what a brand's
    post will actually get" figure — but the media kit does not disclose its methodology, so this
    is an inference, not a confirmed mechanism. Either way, a brand reading "4.17% engagement, 33.8K
    avg likes" and expecting that on a sponsored post would be badly misled: this dossier's two
    actual sponsored posts (Videos 7–8, below) got 66–71 likes on 5,788–6,011 views.
  - TikTok media-kit figures [REPORTED, single source, NOT independently verified — `WebFetch` of
    `tiktok.com/@handlytech` returned only the page title with no data, a JS-rendering limitation
    logged as a DATA GAP]: "TikTok average views: 2.7M, engagement rate: 54.07%, average likes:
    174.7K." A 54.07% engagement rate is implausible at scale for any organic platform and could
    not be corroborated — flagged, not asserted as fact.
  - YouTube: 2.4K subscribers, 0 average views, 0.00% engagement per the media kit [REPORTED] — an
    effectively dormant channel.
  - Threads: 142K followers [OBSERVED via direct `WebFetch`, 2026-07-25], posting the same
    current-era AI-tool content as the IG account (Gemini/Arcads video editing, free-AI-tools
    carousels, Nano Banana/Seedance demos) — a genuine, verifiable cross-platform surface not
    listed in the media kit at all.
  - Reading "1.5M trusted by" as a same-person, all-platforms-summed audience: IG 989K + Threads
    142K + media-kit TikTok 494.3K ≈ 1.6M — in that specific reading the headline number is roughly
    plausible as a FOLLOWER-COUNT SUM. But nothing in the bio or media kit clarifies that framing,
    and a brand paying for "reach" would reasonably read "trusted by 1.5M" as an audience-size or
    engagement claim, not a cross-platform-follower-sum with ~99% of any individual post's actual
    reach concentrated on one platform at a 1.0% median/follower efficiency. **This is the
    documented gap the brief asked for: not fabrication of a number that doesn't exist anywhere,
    but a headline figure whose only defensible reading (a raw follower sum) is not the reading a
    paying brand would naturally make.**
- **Funnel map** [OBSERVED from captions across all 8 detail-pulled videos + Threads content]:
  - Top-of-funnel: Instagram Reels (primary, by far the largest audience), Threads (secondary,
    142K, same content repurposed)
  - Engagement mechanic: "Comment [KEYWORD]" → implied DM funnel, present on every current-era
    (2026) organic top performer and both flops; ABSENT from all 3 legacy pinned mega-hits (see
    Autopsy section — this is a format that postdates the account's biggest wins, not what built
    them)
  - Monetization: disclosed brand partnerships (Pippit AI, Accio Work, and CapCut Design Studio's
    reel — though the CapCut one carries no visible paid-partnership tag, distinguishing it from
    the two clearly-disclosed #ad posts) — contact `handlytech@gmail.com` listed directly in bio
  - No newsletter, no personal website, no linked owned-media surface observed anywhere in the
    sampled content — unusual relative to several other accounts in this study (e.g., Wes Roth's
    Beehiiv newsletter) — DATA GAP on whether one exists but simply wasn't surfaced in this
    dossier's sampling; not found via `WebSearch` either.
- **Cadence:** the 45 non-pinned grid tiles sampled by the harvest span roughly 2026-05-01
  (DXy2ppzokZt, oldest dated non-pinned tile observed) to the harvest date, 2026-07-25 — i.e., high
  cadence, several posts per week, over an observed ~12-week window. [OBSERVED/computed]. **A large
  gap exists between the last pinned hit (2025-01-20) and the earliest non-pinned grid tile observed
  (2026-05-01) — roughly 15.5 months of the account's posting history were not reached by the
  48-tile grid scroll and are therefore NOT observed by this dossier or the harvest.** Logged as a
  DATA GAP, not papered over — see Method Log and Autopsy timeline.

---

## B) Video post-mortems

Selection method (per assignment): 3 pinned legacy mega-hits (all 3 available, exceeding the "2"
floor in the brief to strengthen the autopsy timeline) + top 3 current-era (non-pinned) reels by
view count + 2 worst-performing non-pinned reels (excluding the 3 most-recent grid tiles, per
harvest methodology, to avoid penalizing posts that haven't had time to mature). **8 total
post-mortems**, exceeding the "7+" floor. Channel median for reference throughout: **9.85K views**.

Video-content evidence tier note (applies to ALL 8 post-mortems below, stated once here rather than
repeated verbatim eight times): no ASR/transcript tool is available in this environment, so no
video below carries a verbatim spoken-word transcript. Instead, each video was fully downloaded via
`yt-dlp` and an 8-frame, evenly-time-spaced contact sheet was generated via `ffmpeg` and visually
inspected — this is `[OBSERVED]` evidence (real frames from the real file, not inference), but it
is **partial-sampling observation**, not a continuous watch-through. Burned-in captions legible in
the sampled frames are quoted as observed; the connective narration between sampled frames is
reconstructed and flagged `[INFERRED]` where stated. This is logged once here as the standing
DATA GAP for the "verbatim opening line" template field across every video below.

---

### VIDEO 1 (All-time rank #1 by views — PINNED — 7,471x median): "Find your Stolen Phone Easily!"

#### 0. Identity & stats
- URL: instagram.com/reel/C9PdusWtkOh/. Platform: Instagram Reels. Posted 2024-07-10, 12:09 UTC
  [OBSERVED, `yt-dlp` `timestamp` field, independently pulled 2026-07-25 — exact date match to the
  harvest file's "Jul 10, 2024"]. Duration: 47.4s [OBSERVED, `ffprobe` on the downloaded file].
- Views: 73.6M [OBSERVED, `ig_harvest/handlytech.md` grid pull, 2026-07-25, HIGH confidence].
  Likes: 2,118,218 [OBSERVED via this dossier's independent `yt-dlp` pull; the harvest file's own
  browser-rendered pull showed "2M" rounded — consistent]. Comments: 6,437 [OBSERVED, both pulls
  agree exactly].
- Rank: #1 of 48 sampled grid tiles, all-time, PINNED (floats at grid position 3 despite being the
  2nd-oldest of the 3 pins). 73.6M / 9.85K ≈ **7,471x** the current median — the single largest
  outlier in the account's entire visible catalog.

#### 1. Packaging
- Caption: "Find your Stolen Phone Easily!✅️ #iphone #iphonetricks #iphonetips #stolen #android
  #samsung #samsunggalaxy" [OBSERVED, `yt-dlp` description field]. States the payoff outright — no
  held-back curiosity gap in the text itself, consistent with §1.2.3's point that packaging/caption
  barely matters for feed-native Reels; the caption's real job here is hashtag discoverability.
- Frame 1 [OBSERVED, extracted still + contact sheet]: NOT a talking head. Opens on a moody,
  desaturated narrative shot — a person walking away down a subway/train platform toward a green
  subway car, shot from behind, dim lighting, no text overlay. Stylistically distinct from every
  other video in this dossier, all of which open on Ayham's face or a bold text card.
- Curiosity gap: the wordless subway scene implies an unstated "something is about to happen"
  (a phone theft on transit) without narrating it — a clean partial-information gap per §2.1.1.

#### 2. Hook (0–3s)
- Verbatim opening line: DATA GAP (see standing note above — no ASR).
- Hook taxonomy: **In-medias-res / narrative cold open** (§2.1.2, §3.1) — distinct from the
  "bold claim" or "demo-in-motion" openers that dominate this account's 2026 content.
- What the viewer sees: a stranger's back, walking toward a train — deliberately anonymous framing
  (could be "you"), consistent with the implied "this could happen to you" read of the caption.

#### 3. Structure & retention engineering
- Beat map [OBSERVED, 8-frame sample + caption]: wordless platform/subway scene → cut to Ayham
  on-camera holding up two phones, captioned "for Android" → screen-recording sequence: Google
  Sign-in screen → Google Account device-list screen ("2 sessions on Android phone(s)," "1 session
  on iPhone") → Find My Device map pinpointing a "Galaxy S24 Ultra" with Play Sound / Secure Device
  / Factory Reset options (this beat appears twice across the 8-frame sample, suggesting it runs
  long) → iCloud "Sign in with Apple ID" screen → iCloud Find Devices map showing "Ayham's iPhone"
  with Play Sound / Mark As Lost / Erase This Device options.
- One-idea-per-video: technically TWO parallel payoffs (Android AND iPhone recovery steps) under
  one umbrella promise — a mild 2-item listicle rather than a strict single idea, acceptable under
  §3.2's listicle carve-out since both items share one unifying frame ("find your stolen phone").
- Pacing: screen-recording-heavy (5 of 8 sampled frames are phone-screen captures vs. 2 talking-head
  + 1 narrative b-roll) — high visual variety, frequent scene changes (§3.3.2 marker satisfied).
- Loop design: closes on the iCloud erase/lost screen — a clean end-state, not an explicit rewatch
  hook, though the two-platform structure creates a soft internal loop (an Android user watching to
  see if iPhone gets covered too, or vice versa).
- Captions: only "for Android" observed as burned-in text in the sample; the screen-recorded UI
  text is legible on its own. Notably LESS caption-dense than this account's 2025–2026 word-by-word
  style — DATA GAP on whether this reflects a genuine style evolution or is specific to this video
  (Video 3, below, from an even earlier date, already shows word-by-word captions, complicating a
  simple linear-evolution reading — flagged, not resolved).

#### 4. Value proposition
- Copyable, high-specificity workflow: exact native-OS steps (Google Find My Device, Apple Find My
  iPhone) to locate/lock/wipe a stolen phone. Practical value class: copyable workflow. No product
  pitch, no download, no catch — 100% free, built-in OS functionality.

#### 5. Psychology scoring (STEPPS)
- **Practical Value: HIGH, load-bearing.** An exact "your phone was just stolen — tap here" guide
  is maximally save/send-worthy (preemptive saves, sends to someone who just lost a phone).
- **Emotion:** moderate-to-high arousal anxiety (a common real fear) resolved into competent relief
  — per §2.3, anxiety is high-arousal and share-favorable, and pairing it with resolution (not left
  as pure dread) is a strong combination.
- **Triggers: HIGH** — "losing/having your phone stolen" is an extremely frequent environmental
  cue (commuting, travel, crowds), constantly re-activating the memory of this video per §2.2.
- **Social Currency:** moderate — sharing this signals looking-out-for-others, not primarily status.
- **Public:** low — no trend/sound/challenge participation, pure utility content.
- **Stories:** low-moderate — the wordless cold-open supplies a minimal narrative frame only.

#### 6. CTA & funnel mechanics
- No "comment X" mechanic, no link, no explicit CTA anywhere in caption or sampled frames — a stark
  contrast to virtually every 2026-era video in this dossier. This reel's reach came from pure
  content value, not a manufactured comment funnel.
- Funnel position: pure top-of-funnel awareness — nothing monetizable directly attached.

#### 7. Replicability verdict
- Template: (1) pick a near-universal fear/inconvenience, (2) open on a wordless dramatized
  cold-open implying the bad thing happening, (3) show the EXACT native-app steps for both major
  ecosystems, (4) no CTA, no product pitch — let pure utility carry it.
- Commodity vs. advantage: the underlying feature (Find My Device/iPhone) is 100% commodity
  knowledge; Ayham's advantage was execution/timing/packaging, not proprietary information.
- Difficulty for Tangent: LOW–MED. Format execution is easy; replicating 73.6M-scale reach is a
  tail outcome, not a formula (see Video 3's discussion).

#### 8. Why it won
- The single most load-bearing reason: a broad, universal practical fear + a complete, free,
  no-catch resolution — about as strong a Practical-Value/Triggers combination as short-form
  content can have. This is "utility virality": it reliably outperforms niche-interest content in
  raw reach because the addressable audience is "everyone with a smartphone," not "people
  interested in AI tools."
- Secondary factor: zero friction (no CTA, no link, no comment-gate) between the viewer and the
  payoff, maximizing completion and shareability.
- **This directly feeds the audience-death autopsy:** this video's reach came from a topic with a
  near-universal audience, structurally disconnected from the "AI tutorials" niche the account
  later committed to. The people this video won over were not selected for AI-tool interest.

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp --dump-json` / `--print` metadata pull, instagram.com/reel/C9PdusWtkOh/, 2026-07-25
- Downloaded video file + 8-frame contact sheet (`ffmpeg`/`ffprobe`), analyzed 2026-07-25

---

### VIDEO 2 (All-time rank #2 by views — PINNED — 6,396x median): "If your iPhone got stolen-DO THIS"

#### 0. Identity & stats
- URL: instagram.com/reel/DFC6zh3iZKn/. Posted 2025-01-20, 11:24 UTC [OBSERVED, `yt-dlp`, exact
  match to harvest's "Jan 20, 2025"]. Duration: 32.5s [OBSERVED, `ffprobe`].
- Views: 63M [OBSERVED, harvest grid]. Likes: 576,699 [OBSERVED, `yt-dlp`; harvest's browser pull
  showed "573K" rounded — consistent]. Comments: 3,451 [OBSERVED, both pulls agree].
- Rank: #2 all-time, PINNED (grid position 2). 63M / 9.85K ≈ **6,396x** the current median.

#### 1. Packaging
- Caption: "If your iPhone got stolen-DO THIS🙏 #iphone #iphonetricks #iphonetips #stolen
  #lifehack" [OBSERVED]. Same direct-value-promise caption style as Video 1.
- Frame 1 [OBSERVED]: two people in winter coats/hoodies walking outdoors near a fence — a second
  wordless narrative cold-open, no talking head, no text overlay. This account's two biggest hits
  BOTH open on wordless dramatized b-roll rather than direct camera address — a repeated device.
- Curiosity gap: implied "something is about to happen to one of these people," ambiguous and
  unresolved, per §2.1.1.

#### 2. Hook (0–3s)
- DATA GAP: no verbatim transcript (standing note). Reconstructed from 8 sampled frames + burned-in
  word-by-word captions, which ARE present here (unlike Video 1): "swipe down," "phone so you,"
  "settings then," "is locked no," "your profile," "Now when," "findable even" appear as individual
  caption fragments across the sample.
- Hook taxonomy: in-medias-res narrative cold open — same taxonomy as Video 1.
- What the viewer sees: two strangers walking, then a hard cut to Ayham holding an iPhone close to
  camera with "swipe down" burned in — a pattern-interrupt cut from narrative ambiguity to
  instructional close-up.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: wordless walking scene → phone close-up, "swipe down" → Lock Screen
  SOS/Emergency Call screen, "phone so you" → Settings app walkthrough, "settings then" (a red
  accessibility-style highlight visible on a settings row) → Settings list showing "Handly Tech" as
  the signed-in profile name with a red arrow annotation pointing at a highlighted "your profile"
  row → close-up talking head, "is locked no" / "Now when" → power-off/SOS screen again, "findable
  even."
- One-idea-per-video: yes, single coherent idea (remote-lock a stolen iPhone before recovering it)
  — tighter than Video 1's two-platform listicle.
- Pacing: very high — nearly every sampled frame shows a different screen/angle, several with
  hand-drawn-style red-arrow annotations, a visible production upgrade over Video 1.
- Loop design: closes on a "findable even [after power off]" reveal — a genuine delayed payoff
  (most people don't know a phone stays findable after power-off) per §2.6.1, rather than
  front-loading the most obvious step.
- Captions: dense word-by-word burned-in captions throughout, strongly satisfying §3.3.1.

#### 4. Value proposition
- Copyable, high-specificity workflow (exact Settings path, exact screens) for a universal fear.
  Narrower than Video 1 (iPhone-only) but deeper on the one platform, including a genuinely
  non-obvious fact ("still findable after power-off") — insider knowledge, not generic advice.

#### 5. Psychology scoring (STEPPS)
- **Practical Value: HIGH**, same load-bearing role as Video 1.
- **Triggers: HIGH** — phone theft fear, same as Video 1.
- **Emotion:** anxiety→relief arc, high-arousal per §2.3.
- **Social Currency: moderate-high** — the specific "findable after power-off" fact is exactly the
  kind of non-obvious insider knowledge that makes forwarding it self-flattering per §2.5,
  arguably stronger than Video 1's more generic "the feature exists" framing.
- **Public:** low, no trend/sound participation.
- **Stories:** low-moderate, same minimal narrative device as Video 1.

#### 6. CTA & funnel mechanics
- No comment-bait, no link, no explicit CTA — consistent with Video 1, both pre-dating the
  account's current comment-funnel-heavy era.

#### 7. Replicability verdict
- Template: (1) universal-fear topic, (2) wordless narrative cold-open (a repeatable signature
  device across this account's top 2 hits), (3) dense word-by-word captions + red-arrow tap
  annotations for clarity, (4) end on a specific non-obvious fact rather than the most obvious step.
- Commodity vs. advantage: the underlying OS feature is commodity; the annotation/pacing polish is a
  real, learnable production edge over Video 1.
- Difficulty for Tangent: LOW-MED — arrow overlays and word-timed captions are standard editing
  skills.

#### 8. Why it won
- Load-bearing reason: the same universal-fear utility engine as Video 1, executed with a
  production upgrade (annotations, tighter single-idea focus, a delayed non-obvious payoff) —
  suggesting genuine editing-craft improvement between Jul 2024 and Jan 2025.
- **This is the account's SECOND mega-hit on the exact same off-topic theme (phone security), six
  months after the first.** By early 2025 — one month before this dossier's next-observed content
  window begins — a huge cross-section of the internet, and very plausibly Instagram's own topic
  classifier, had already tagged this account's "identity" as phone-security/life-hack content,
  deepening the mismatch this dossier's autopsy investigates.

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp` metadata pull, instagram.com/reel/DFC6zh3iZKn/, 2026-07-25
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 3 (All-time rank #3 by views — PINNED, OLDEST — 3,127x median): "Never Trust Screenshots EVER Again!!"

#### 0. Identity & stats
- URL: instagram.com/reel/CybW5zct2AA/. Posted 2023-10-15, 17:15 UTC [OBSERVED, `yt-dlp`]. Duration:
  19.1s [OBSERVED, `ffprobe`] — the shortest video in this dossier by a wide margin.
- Views: 30.8M [OBSERVED, harvest]. Likes: 739,240 [OBSERVED, `yt-dlp`; harvest showed "726K" — a
  real ~1.8% discrepancy between the two same-day (2026-07-25) pulls, most plausibly ordinary
  like-count accrual in the hours between pulls rather than an error; logged, not resolved further].
  Comments: 1,944 [OBSERVED, both pulls agree].
- Rank: #3 all-time, PINNED, and the OLDEST post in the account's entire visible catalog (grid
  position 1 — the very first thing a new profile visitor sees today is a ~2.75-year-old video).
  30.8M / 9.85K ≈ **3,127x** the current median.

#### 1. Packaging
- Caption: "Never Trust Screenshots EVER Again!!😱 #website #hack #whatsapp #whatsapptips #virus"
  [OBSERVED]. Bold-claim/warning caption style, distinct from Videos 1–2's direct-value statements.
- Frame 1 [OBSERVED]: Ayham talking directly to camera, dark room, a purple/pink-lit
  "SECRET LAB"-branded monitor visible behind him, burned-in bold caption "NEVER TRUST Screenshots!"
  ("TRUST" in a highlight color). The earliest use of a direct-to-camera talking-head open in this
  sample, and the branded "Secret Lab" backdrop is a recurring visual-identity element not seen in
  Videos 1–2's plainer settings.
- Curiosity gap: the bold claim itself creates an immediate "wait, why not?" gap — a faster
  mechanism than Videos 1–2's slow-burn narrative ambiguity.

#### 2. Hook (0–3s)
- Opening line reconstructed from burned-in captions across the sample: "Never Trust Screenshots!"
  / "know that" — the bold-text hook line is directly [OBSERVED] (burned into frame 1); the full
  verbatim spoken sentence is a DATA GAP (standing note).
- Hook taxonomy: **Bold claim** (§3.1) — direct camera address confronting a common assumption
  ("you trust screenshots as proof — you shouldn't").
- What the viewer sees: talking head only for the opening beat — the most "vlog-native" open of the
  three pinned hits, no b-roll cold-open.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: talking-head bold-claim hook → talking head continues ("know that") → cut to
  a screen-recording of a "Fake [X] Generator" web tool with a dropdown listing Personal Detail /
  Social Media / Text Messenger / Name Generator fields and a platform picker (WhatsApp, Facebook,
  Instagram, Twitter, TikTok, YouTube, Hangouts, Chats) → cut to a fabricated WhatsApp chat
  screenshot example (a conversation about meeting up) → a "Download WhatsApp Chat As Image" button
  shown → back to the platform-picker screen ("make fake" / "platforms" captions) → talking head
  recurs between demo beats.
- One-idea-per-video: yes — "a website exists that fabricates fake screenshots, don't trust them as
  proof" — tight for its 19-second runtime.
- Pacing: fast, short-form-native — the shortest video analyzed, 4–5 distinct beats packed in.
- Loop design: no strong rewatch hook observed; closes on the fake-chat-download demo, a fairly
  abrupt functional ending rather than a crafted final beat — a mild structural weakness relative
  to Videos 1–2's more deliberate closers.
- Captions: word-by-word burned-in style present even in this earliest (Oct 2023) video — meaning
  the account's caption-editing style predates Video 1 (Jul 2024), which complicates a simple
  "captions got denser over time" narrative (Video 1 may simply be an exception; flagged, not
  resolved).

#### 4. Value proposition
- Awareness/media-literacy value (screenshots are fakeable) plus incidental tool discovery.
  Practical value class: mostly "news you can use," secondarily tool-discovery. Medium specificity —
  the tool's exact name/URL is not legible in the sampled frames — DATA GAP.

#### 5. Psychology scoring (STEPPS)
- **Emotion: HIGH-arousal**, the most emotionally-loaded hook of the three pins — a mix of anxiety
  (things I believed were proof aren't) and mild betrayal, both high-arousal per §2.3.
- **Social Currency: HIGH** — prime "I'm ahead of the curve" content; knowing screenshots can be
  faked (and knowing the tool that does it) is directly status-conferring to share per §2.2/§2.5 —
  arguably the strongest Social-Currency activation of the three pinned hits.
- **Triggers: HIGH** — screenshots-as-evidence come up constantly in disputes/arguments.
- **Practical Value: moderate** — useful to know, but "avoid being fooled" is a less directly
  actionable workflow than Videos 1–2's step-by-step recovery tutorials.
- **Public:** low, no trend participation. **Stories:** low, no narrative frame.

#### 6. CTA & funnel mechanics
- No comment-bait or link CTA observed — consistent with Videos 1–2, pre-dating the account's 2026
  comment-funnel format.

#### 7. Replicability verdict
- Template: (1) a bold, confrontational claim undermining a common assumption, (2) direct-to-camera
  delivery for speed, (3) prove the claim with a live tool demo, (4) keep it SHORT — don't pad a
  single-idea reveal.
- Commodity vs. advantage: the fake-screenshot-generator tool is a third-party commodity discovery,
  not Ayham's own product; his advantage is framing/delivery speed.
- Difficulty for Tangent: LOW — bold-claim-plus-tool-demo is a highly replicable, low-cost format.

#### 8. Why it won
- Load-bearing reason: maximum Social-Currency + Trigger density in the shortest possible runtime —
  the most "shareable-because-it-makes-me-look-smart" video of the three pins, and its brevity
  (19s) means a very high share of viewers who start it likely finish it, maximizing the completion
  signal both platforms reward (§1.2.1, §1.2.2).
- **This is the OLDEST of the three pins (Oct 2023) and general "internet/social-media safety"
  content — even less specifically "phone hardware" than Videos 1–2, meaning it won over an even
  broader, more topic-distant audience ("anyone who uses WhatsApp") than the phone-security pins —
  the widest mismatch of the three legacy hits relative to "AI in 30 seconds" tutorials.**

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp` metadata pull, instagram.com/reel/CybW5zct2AA/, 2026-07-25
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 4 (Current-era rank #1 non-pinned — 33.6x median — FLAGGED ANOMALY): "With CapCut Design Studio..."

#### 0. Identity & stats
- URL: instagram.com/reel/DZozx8UoTDy/. Posted 2026-06-16, 07:04 UTC [OBSERVED, `yt-dlp` timestamp,
  exact match to harvest's "Jun 16, 2026"]. Duration: 37.8s [OBSERVED, `ffprobe`].
- Views: 331K [OBSERVED, harvest grid, HIGH confidence]. **Likes/comments — an unresolved,
  three-way-documented conflict:**
  - Harvest file's ORIGINAL pull: 59 likes, 59 comments, as-of 2026-07-25.
  - Harvest file's own appended "Anomaly re-verification" section (a separate research agent,
    same file, same date): re-pulled and got **59 likes, 59 comments again** — "CONFIRMED, not a
    metrics-sync error," per that agent's note.
  - **This dossier's independent `yt-dlp` pulls** (two separate invocations, ~15 minutes apart,
    2026-07-25 ~18:15–18:29 UTC): **114 likes, 59 comments** — both of this dossier's own pulls
    agree with EACH OTHER (114, stable) but conflict with BOTH harvest-file pulls (59).
  - Comments (59) is the only number all four total pulls (2 harvest-side + 2 of this dossier's)
    agree on exactly.
  - [OBSERVED, but presenting a genuine unresolved conflict, not resolving it by fiat.] Most
    plausible explanations, stated as [INFERRED]: (a) Instagram serving inconsistent counts to
    different access paths (browser-render vs. `yt-dlp`'s API-equivalent path) at different cache
    layers, or (b) ordinary like-count growth — though the exact 59/59 double-match on the harvest
    side argues against pure-coincidence timing. Not resolved further in this dossier.
- Rank: #1 non-pinned reel in the current 30-most-recent window, 33.6x the 9.85K median — but given
  the like-count conflict, its status as an unambiguous "top organic performer" (vs. a metrics or
  distribution artifact) remains only partially confirmed even after two independent
  re-verification attempts by two different agents.

#### 1. Packaging
- Caption: "With CapCut Design Studio, I can take a simple concept and transform it into a
  creative, and shareable visual. Upload your image, describe the scene, refine the details, change
  the background, adjust the lighting, add text, and turn it into a short video with motion. No
  design background needed. Stop templating, start designing. Comment AI and I'll send you the
  prompts.👇 #aitools #aidesign #ai #CapCut #CapCutDesignStudio" [OBSERVED]. Long value-forward
  caption ending in a comment-bait CTA — the standard current-era template.
- Frame 1 [OBSERVED]: a dynamic, nested-phone-mockup motion graphic reading "Tutorial incoming" over
  a stack of phone screens showing a Formula 1-style photo and a red-carpet couple photo — a
  produced, graphics-heavy open, not a plain talking head or plain b-roll.
- Curiosity gap: "tutorial incoming" for an unnamed transformation — a mild gap, resolved quickly.

#### 2. Hook (0–3s)
- DATA GAP (standing note). Sample: "Tutorial incoming" graphic → talking head, caption "make all"
  — suggesting a spoken hook near "watch me make all of this."
- Hook taxonomy: **Demo-in-motion** (§3.1) — the opening graphic previews finished outputs (F1
  photo, couple photo) before the process is shown, a result-first structure.
- What the viewer sees: finished-product previews first, talking head second — inverted vs. the
  pinned videos' pattern of talking-head-or-scene-first.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: "Tutorial incoming" graphic → talking head "make all" → a prompt/chat
  interface screenshot, "to generate" → a football-crowd photo composite with a dog inserted,
  "is ready" → more football-stadium composite variations, "background" / "finished" → final frame:
  the finished composite plus a small inset of Ayham's own photo, "video."
- One-idea-per-video: yes — AI image/video compositing in CapCut, shown via one worked example.
- Pacing: high — screen-recording/generated-image cuts dominate (6 of 8 sampled frames).
- Loop design: closes on a finished-result reveal, a clean "ta-da" ending.
- Captions: burned-in single-word style ("make all," "is ready," "background," "finished," "video")
  — the account's now-standard word-by-word style, denser/faster than the 2023–2025 pinned videos.

#### 4. Value proposition
- Tool discovery (CapCut Design Studio) + a worked example, but the ACTUAL prompts are explicitly
  withheld from the video ("Comment AI and I'll send you the prompts") — a meaningfully LOWER-
  specificity video than any of the three pinned hits, all of which showed the complete workflow
  on-screen with nothing gated. A structural value downgrade vs. the account's own historical top
  performers.

#### 5. Psychology scoring (STEPPS)
- **Social Currency: moderate** — "I made this AI composite" is shareable/flex-adjacent, but weaker
  than the pinned videos' "I'm protecting you from a real threat" framing.
- **Emotion:** awe/amusement at the AI result, positive high-arousal per §2.3, but milder than the
  anxiety-driven pins.
- **Practical Value:** undercut by prompt-gating (see #4) — the video advertises value it withholds.
- **Triggers: LOW** — "AI image editing tools" is not a frequent everyday cue the way "losing your
  phone" is — this is the core of the audience-mismatch problem this dossier investigates.
- **Public:** low-moderate (CapCut brand recognition). **Stories:** low.

#### 6. CTA & funnel mechanics
- "Comment AI and I'll send you the prompts" — the dominant current-era mechanic, converting
  comments into an implied DM funnel (§3.4.3 pattern; the specific DM-automation tool used was not
  independently confirmed — DATA GAP).
- Bait-risk: per §1.3.2, bare "comment X" prompts with no standalone value are prohibited
  engagement bait. This video DOES show a worked example on-screen, likely landing it on the
  "compliant" side of that line — but the WITHHELD prompts (§4) push it closer to the bait boundary
  than the account's older, fully-non-gated pinned hits.
- Funnel position: mid-funnel lead-capture, not pure top-of-funnel awareness.

#### 7. Replicability verdict
- Template: (1) open on a finished-result preview graphic, (2) walk through an AI tool's UI on a
  fun example, (3) withhold the exact prompts, (4) gate them behind a comment keyword.
- Commodity vs. advantage: CapCut Design Studio is a public tool anyone can screen-record; the
  account's only real advantage is its existing (if mismatched) follower base for seed distribution.
- Difficulty for Tangent: LOW — no special skill beyond screen-recording a public AI tool.

#### 8. Why it won (with anomaly caveat)
- On the 59/59 reading (two of four total pulls), this would be one of the most anomalous "wins" in
  the dataset: a top-ranked reel by views with a near-zero engagement footprint, hard to reconcile
  with Instagram's stated optimization for likelihood-to-like/save/reshare (§1.1.1/§1.1.2) rather
  than raw impressions. On this dossier's own 114/59 reading, the like-rate is still extremely low
  (0.034%) relative to every other video in this dossier (which range 0.9%–3.8%) — **under EITHER
  reading, this is an engagement-rate outlier at the bottom of the account's own distribution
  despite being its current top-viewed non-pinned reel.**
- Most plausible reading [INFERRED]: unusually passive, low-affinity distribution (e.g., heavy
  Explore/non-following autoplay placement) rather than reach among people who chose to engage —
  views accrued without corresponding intent signals. This directly feeds the autopsy: even the
  account's best current-era performer shows signs of reaching an audience that scrolls past rather
  than one that wants this content.

#### Sources
- `../ig_harvest/handlytech.md` (original pull + appended "Anomaly re-verification" section)
- This dossier's 2 independent `yt-dlp` pulls, instagram.com/reel/DZozx8UoTDy/, 2026-07-25
  (~18:15 and ~18:29 UTC, both 114 likes/59 comments)
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 5 (Current-era rank #2 non-pinned — 11.9x median): "Create long AI videos for free"

#### 0. Identity & stats
- URL: instagram.com/reel/DZUg7ZxIHLv/. Posted 2026-06-08, 09:55 UTC [OBSERVED, `yt-dlp`, matches
  harvest]. Duration: 23.0s [OBSERVED, `ffprobe`].
- Views: 117K [OBSERVED, harvest]. Likes: 3,595 [OBSERVED, `yt-dlp`; harvest showed 3,594 — 1-like
  difference, trivial]. Comments: 5,494 [OBSERVED, `yt-dlp`; harvest showed 5,492 — 2-comment
  difference, trivial]. **Like-rate 3.07%, comment-rate 4.70% — comments EXCEED likes**, a strong
  tell of comment-bait-driven engagement (a comment is a higher-effort action than a like and
  normally trails it heavily on non-bait content).
- Rank: #2 non-pinned reel in current window, 11.9x the 9.85K median.

#### 1. Packaging
- Caption: "Create long AI videos for free 🤯 No credits. No payment. Just one smart trick. Use
  Qwen to generate your first AI video. Then copy the last frame. Paste it back with your next
  prompt. And keep the story going. Same character. Same style. Same scene. Comment "FREE" and I'll
  send you the link. #aitools #ai #freeaitools #free #website" [OBSERVED]. Unlike Video 4, this
  caption explains the FULL technique in text (last-frame-chaining) — the comment-gate is for a
  link/tool access, NOT for withholding the core idea — a meaningfully more generous value
  structure than Video 4.
- Frame 1 [OBSERVED]: bold yellow-on-black text card "MAKE LONG AI VIDEO FOR FREE" over a talking-
  head background with a small inset thumbnail of a football-team photo — a bold-claim text-card
  hook, high production polish.
- Curiosity gap: "for free" + "one smart trick" implies a non-obvious method — gap opens on "how,"
  the caption already answers "what."

#### 2. Hook (0–3s)
- DATA GAP (standing note). The bold text-card hook is likely read aloud near-verbatim in the
  opening seconds — a common short-form device where on-screen hook text doubles as the spoken line.
- Hook taxonomy: **Bold claim / text-card hook** (§3.1).
- What the viewer sees: a graphic promise before any process is shown — pure curiosity-gap opening.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: bold text-card hook → talking head, hand gesture, "trick" → screen-recording
  of an AI prompt/chat interface, "to generate" → a football-player AI composite image, "is ready"
  → a second, different football composite, "Now the" / "same character" (with a diagram-style
  arrow connecting the two images to illustrate the last-frame-chaining concept) → talking head,
  "build one" → final frame: bold bouncing "COMMENT" text over the football composite.
- One-idea-per-video: yes, a tight single technique (frame-chaining for character-consistent AI
  video), reinforced with a visual diagram — a genuine pedagogical upgrade over narration alone.
- Pacing: high, matches the account's current style.
- Loop design: ends on the CTA card rather than a content payoff — a commercially-motivated ending
  (funnel-close), a real difference from the pinned videos' content-first endings.
- Captions: dense word-by-word style, matches current-era norm.

#### 4. Value proposition
- Practical value: HIGH relative to Video 4 — the core technique is explained AND illustrated with
  an arrow diagram; only the specific link is comment-gated, not the method itself. Specificity:
  high.

#### 5. Psychology scoring (STEPPS)
- **Practical Value: HIGH, load-bearing** — a genuinely reusable, specific workflow.
- **Social Currency: moderate-high** — "make long AI videos for free" is a capability flex worth
  sharing to anyone interested in AI content creation.
- **Emotion:** awe/amusement at the free-workaround discovery, high-arousal-positive.
- **Triggers: LOW-moderate** — narrower than the phone-security pins; a real but smaller recurring
  cue than "losing your phone."
- **Public: low-moderate** (Qwen/AI-tool trend adjacency). **Stories: low.**

#### 6. CTA & funnel mechanics
- "Comment 'FREE' and I'll send you the link" — comments (5,494) outnumbering likes (3,595) is
  direct observable evidence the CTA is functioning as a comment-generation mechanic, consistent
  with §1.1.2's framing that comments/sends are heavily weighted ranking signals.
- Bait-risk: LOWER than Video 4 — the caption delivers real standalone value independent of the
  gated link, more clearly on the compliant side of §1.3.2.

#### 7. Replicability verdict
- Template: (1) bold text-card hook naming the outcome + "for free," (2) explain the FULL technique
  in the caption (don't gate the core idea), (3) illustrate the technique visually with a simple
  diagram, not just narration, (4) gate only the specific tool link behind a comment.
- Commodity vs. advantage: last-frame-chaining is public AI-community knowledge (commodity); the
  clear visual diagramming of it is a genuine, replicable production edge.
- Difficulty for Tangent: LOW-MED.

#### 8. Why it won
- Load-bearing reason: this is the account's best CURRENT execution of its comment-bait format —
  real value delivered up front (unlike Video 4), a visual diagram aiding comprehension, and a
  comment mechanic that appears to be genuinely converting (comments > likes). It likely
  out-performs Video 6 on relatability (a viral-style "long AI video" trick vs. Video 6's more
  utilitarian tool-roundup) and out-performs Video 4 on the trustworthiness of its engagement
  numbers (no anomaly flag here).
- Still only 117K views — 11.9x median but a rounding error next to the 63–73.6M pinned hits — even
  the account's best trustworthy current performance is two full orders of magnitude below its
  legacy ceiling.

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp` metadata pull, instagram.com/reel/DZUg7ZxIHLv/, 2026-07-25
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 6 (Current-era rank #3 non-pinned — 5.5x median): "3+5 AI websites, all free"

#### 0. Identity & stats
- URL: instagram.com/reel/DZChXWoIaHF/. Posted 2026-06-01, 10:11 UTC [OBSERVED, `yt-dlp`, matches
  harvest]. Duration: 39.1s [OBSERVED, `ffprobe`].
- Views: 54.2K [OBSERVED, harvest]. Likes: 2,054, Comments: 2,252 [OBSERVED, `yt-dlp` — **this reel
  was NOT one of the harvest file's original 7 detail-pulls; this dossier independently pulled it
  specifically to satisfy the "top 3 current-era reels" requirement**, since the harvest file only
  carried full like/comment/date data for 2 non-pinned reels]. Like-rate 3.79%, comment-rate 4.15%
  — again comments roughly matching/slightly exceeding likes, the same comment-bait signature as
  Video 5.
- Rank: #3 non-pinned reel in current window, 5.5x the 9.85K median — the weakest of the three
  current-era "top" reels selected here, included specifically to round out the top-3 requirement
  and to test whether the Video 4–5 pattern holds at a lower tier.

#### 1. Packaging
- Caption: "3+5 AI websites, all free. Guaranteed.✅️ Use them to create AI images, videos,
  designs, product visuals, voiceovers, podcasts, and more. Comment "Free" and I'll send you the
  links plus 5 extra free AI websites. #aitools #ai #freeaitools #free #website" [OBSERVED].
  Listicle-format caption ("3+5" websites) — the LINKS are gated, but the promise is fully legible.
- Frame 1 [OBSERVED]: Ayham talking head against a green-lit backdrop, caption "first one" — a
  plain talking-head open, no graphic text-card (unlike Video 5) — the least visually elevated hook
  of the three current-era top reels.
- Curiosity gap: "3+5 AI websites" implies a specific, countable list — a classic listicle
  curiosity structure (how many, which ones).

#### 2. Hook (0–3s)
- DATA GAP (standing note). Sample: talking head captioned "first one" suggests the spoken hook
  introduces the list format directly — a lower-novelty opener than Video 5's bold claim card.
- Hook taxonomy: **Listicle / demo-in-motion hybrid** (§3.1, §3.2 listicle carve-out).
- What the viewer sees: a plain talking head, not a graphic or scene — the weakest first-second
  visual hook of the three current-era top reels, and a plausible partial explanation for why this
  reel underperforms Video 5 despite a similar CTA mechanic and comparable per-viewer engagement.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: talking head "first one" → screen-recording of an AI "Image Studio" tool
  interface ("START CREATING WITH [X] IMAGE STUDIO") → a "VIDEO S[TUDIO]" tool screen with
  model-selection options → talking head "and" / "the model" → an AI design-tool "what do you want
  to design today?" prompt interface → a Hugging Face Spaces URL bar visible
  ("huggingface.co/spaces/yassermd/VibeVoice") → a voice-demo (two people talking, waveform
  visualizer) → final frame: bold "COMMENT 'website'" text over a product-mockup collage.
- One-idea-per-video: the LOOSEST adherence to "one idea" of any video in this dossier — a genuine
  multi-tool listicle (image tool, video tool, design tool, voice tool in sequence), each getting
  only 1–2 sampled frames, i.e., less depth per tool than Videos 4–5's single-worked-example
  structure.
- Pacing: high, tool-to-tool cuts.
- Loop design: ends on the CTA card, funnel-close pattern matching Video 5.
- Captions: word-by-word style, current-era norm.

#### 4. Value proposition
- Breadth over depth — a tool-discovery listicle rather than a single deep technique. Lower
  specificity per item than Videos 4–5's worked single examples; more "here's a menu" than "here's
  exactly how."

#### 5. Psychology scoring (STEPPS)
- **Practical Value: moderate** — useful as a bookmarkable reference list (§2.7), genuinely
  save-worthy.
- **Social Currency: moderate** — "I found a free AI tool list" is shareable but generic; less
  specific/surprising than Video 5's named technique.
- **Emotion:** mild positive interest, LOWER arousal than Videos 1–3's anxiety-driven pins or even
  Video 5's "aha" reveal — a flatter emotional register, consistent with §2.3's prediction that
  lower-arousal content underperforms on transmission even when well-produced.
- **Triggers: LOW**, same niche-limitation as Video 5. **Public, Stories: low.**

#### 6. CTA & funnel mechanics
- Same "Comment 'Free'" mechanic as Video 5, converting similarly (comments 2,252 vs. likes 2,054 —
  comments again meet/exceed likes).

#### 7. Replicability verdict
- Template: (1) promise a specific countable list of free tools, (2) plain talking-head open (lower
  production cost than a graphic card), (3) rapid tool-to-tool screen-record montage, (4) gate the
  full list behind a comment.
- Commodity vs. advantage: pure aggregation of publicly-known tools; the lowest-effort, most
  replicable format of the three current-era videos.
- Difficulty for Tangent: LOW.

#### 8. Why it lost (relative to Videos 4–5)
- Load-bearing reason: the weakest first-second visual hook (plain talking head vs. Video 5's
  graphic card or Video 4's motion-graphic preview) combined with the lowest per-item depth
  (breadth-over-depth listicle vs. single worked examples). Per §2.1.3/§1.2.1, the opening moment
  is the single most heavily-weighted checkpoint on both platforms' own stated mechanics, and this
  video's opener is the least distinctive of the three.
- Notably, its LIKE-RATE (3.79%) is actually the HIGHEST of the three current-era top reels, and
  its comment-rate is comparable — meaning viewers who saw it engaged well; the shortfall is in
  REACH/distribution, not in on-platform reception, reinforcing this dossier's broader finding that
  the account's ceiling problem is a distribution/mismatch problem more than a content-quality-
  among-actual-viewers problem.

#### Sources
- `../ig_harvest/handlytech.md` (grid entry only — no original detail pull)
- `yt-dlp` metadata pull, instagram.com/reel/DZChXWoIaHF/, 2026-07-25 (independently sourced by this
  dossier)
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 7 (FLOP #1 — sponsored, below account median): "Escape the MATRIX short story!" (Pippit AI)

#### 0. Identity & stats
- URL: instagram.com/reel/DYcI0guoijZ/. Posted 2026-05-17, 12:25 UTC [OBSERVED, `yt-dlp`, matches
  harvest]. Duration: 50.7s [OBSERVED, `ffprobe`] — the LONGEST video in this dossier.
- Views: 5,788 [OBSERVED, harvest — BELOW the account's own 9.85K median]. Likes: 71, Comments: 69
  [OBSERVED, harvest and `yt-dlp` match exactly]. Like-rate 1.23%.
- Rank: one of the 2 flops selected per QC protocol's "both tails" requirement (the 3 most-recent
  grid tiles were excluded from flop selection per harvest methodology, to avoid penalizing posts
  that haven't matured). At 5,788 views this sits at ~59% of the account's own median — genuinely
  underperforming its own typical reel, not just underperforming the legacy pins.

#### 1. Packaging
- Caption: "Escape the MATRIX short story! Comment "AI" for the full guide👇 Pippit is changing
  content creation. You can create videos faster with AI agents, from ideas and scripts to scenes,
  voice, and visuals. This is built for creators and brands who want to scale content without
  spending hours on every video. Start the next era of content creation. Scale your brand with
  Pippit. Link in bio. @pippitofficial #PippitAI #PippitAgent #PippitPartner #PippitSeedance
  #Seedance" [OBSERVED]. Heavy brand-copy language ("Start the next era," "Scale your brand") —
  reads as ad copy, not Ayham's own voice, a tonal break from every other caption in this dossier.
- Frame 1 [OBSERVED]: NOT Ayham at all — a "Pippit / Dreamina Seedance" branded logo card over a
  stock-style AI-generated photo (a woman answering a phone in an office), with a paragraph of
  small caption text underneath describing camera/lighting direction. **This pattern (branded
  header + AI stock photo + technical caption) repeats across ALL 8 sampled frames** — every single
  sampled frame is a different static AI-generated image (office phone call, doorway portrait,
  phone/landlord text exchange, desk with ring light, food/desk shot, garage/car scene, driving
  shot, aerial highway shot). Ayham's face never appears once in the sample.
- Curiosity gap: minimal — "Escape the MATRIX short story" is a vague, disconnected teaser line that
  doesn't clearly connect to what's actually shown (a slideshow of unrelated AI stock photos) — a
  packaging/content mismatch in itself.

#### 2. Hook (0–3s)
- DATA GAP (standing note) — and notably, frame 1 has NO visible on-screen spoken-word caption at
  all (unlike every other video in this dossier), suggesting this may be a voiceover-narrated or
  music-only slideshow rather than a captioned talking format — a further, more specific DATA GAP
  on whether there is spoken narration at all in this video.
- Hook taxonomy: none of the standard taxonomies in §3.1 cleanly apply — this is closest to a
  "product portfolio showcase," itself a signal this video doesn't fit the account's own proven
  formats.
- What the viewer sees: a branded stock photo with a wall of small caption text — the OPPOSITE of
  §1.2.3's Shorts-native marker (effort spent on caption/text density rather than the in-video
  visual hook), and arguably a partial hit against §1.3.1's "majority text" de-prioritization risk
  if the caption blocks are large enough on-screen (plausible from the sampled frames, not
  frame-by-frame confirmed).

#### 3. Structure & retention engineering
- Beat map [OBSERVED, 8-frame sample]: eight near-identical beats — branded logo card + AI stock
  photo + descriptive caption paragraph, repeated with a different scene each time (office/call →
  portrait → text-message screenshot → desk/ring-light → food/desk → garage/car → driving → aerial
  highway). No talking head, no screen-recording of an actual tool interface being used, no
  demonstrated workflow — this is a slideshow of OUTPUT EXAMPLES, not a tutorial.
- One-idea-per-video: technically one idea ("Pippit makes content like this") delivered as a flat,
  undifferentiated list of 8 similar-looking outputs rather than a structured hook→process→payoff
  arc — closer to a portfolio dump than a story.
- Pacing: visually static WITHIN each beat (a still photo held on screen) despite cutting between
  beats — a materially LOWER-energy pacing profile than every other video in this dossier, all of
  which mix talking-head motion with screen-recording motion.
- Loop design: no crafted ending observed in the sample; the last sampled frame is simply another
  stock photo — a flat, non-payoff close.
- Captions: dense paragraph-style captions (not word-by-word animated captions) — a format
  regression from the account's now-standard punchy single-word caption style seen in Videos 4–6.

#### 4. Value proposition
- Practical value: LOW and abstract — the video shows finished OUTPUTS, not a process; a viewer
  walks away with "this tool can make nice photos" but no workflow, no prompts, no specific
  technique — the least specific, least actionable video in this entire dossier.

#### 5. Psychology scoring (STEPPS)
- **Parasocial/identity (§2.4.1): near-TOTAL BREAK.** Ayham's face, voice, and persona — the
  account's core recognizable identity, which every other video in this dossier relies on for
  mere-exposure/parasocial compounding — are entirely absent. The single most structurally distinct
  video in the dataset.
- **Social Currency: low** — sharing "here's an AI photo tool's marketing images" confers little
  status.
- **Emotion: flat/low-arousal** — aesthetically pleasant stock photography is not emotionally
  activating per §2.3.
- **Practical Value, Triggers, Public, Stories: all low-to-absent.**

#### 6. CTA & funnel mechanics
- "Comment 'AI' for the full guide" — the same comment-gate mechanic as the account's organic top
  performers, but here attached to a video with markedly less standalone value, pushing this
  execution closer to the bare-engagement-bait risk zone per §1.3.2 than any organic video in this
  dossier.
- Funnel position: bottom-of-funnel brand-monetization post, explicitly disclosed (#PippitPartner),
  not organic top-of-funnel content.

#### 7. Replicability verdict
- Template: a NEGATIVE example — do NOT drop the creator's face/persona for a sponsored post; do
  NOT replace a demonstrated workflow with a stock-photo portfolio dump; do NOT swap punchy
  word-by-word captions for paragraph blocks.
- Commodity vs. advantage: the AI-generated stock images are the sponsor's product output, not
  Ayham's craft — this video showcases the SPONSOR's product with almost none of Ayham's own
  format/voice, plausibly exactly why it flopped.
- Difficulty for Tangent: N/A (a what-not-to-do example, not a template to replicate).

#### 8. Why it lost
- Load-bearing reason: total format collapse relative to the account's proven identity — no talking
  head, no demonstrated process, generic paragraph captions, and a caption line ("Escape the MATRIX
  short story") that doesn't even match the content shown. Per §2.4.1/§2.4.2, breaking the
  recognizable persona/format that built the account's mere-exposure familiarity is a direct hit
  against the account's only structural advantage (its 989K-follower identity), and the disclosed-
  sponsorship framing (§1.3.2, §3.4.3) likely compounds the reach penalty further.
- Secondary factor: this is a DISCLOSED BRAND PARTNERSHIP, consistent with the cross-account
  pattern (`00_INDEX.md`) that sponsored content underperforms organic content — but UNLIKE
  tiffintech/networkchuck's sponsored posts elsewhere in this study (which got VIEW-COUNT INFLATION
  paired with near-zero engagement), this post got NEITHER inflated views NOR engagement — a
  "worst of both worlds" sponsored-post outcome, actually falling below the account's own organic
  median.

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp` metadata pull, instagram.com/reel/DYcI0guoijZ/, 2026-07-25
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

### VIDEO 8 (FLOP #2 — sponsored, below account median, oldest current-era tile): "Most people fail at side hustles..." (Accio Work)

#### 0. Identity & stats
- URL: instagram.com/reel/DXy2ppzokZt/. Posted 2026-05-01, 11:38 UTC [OBSERVED, `yt-dlp`, matches
  harvest]. Duration: 48.1s [OBSERVED, `ffprobe`].
- Views: 6,011 [OBSERVED, harvest — also below the 9.85K median, though slightly higher than Video
  7]. Likes: 66, Comments: 43 [OBSERVED, harvest and `yt-dlp` match exactly]. Like-rate 1.10%.
- Rank: the second of the 2 flops selected. Also the OLDEST post in the current-era (non-pinned)
  grid window sampled by the harvest (2026-05-01 is the earliest date observed anywhere in the 45
  non-pinned grid tiles) — this video anchors the very start of this dossier's visible current-era
  timeline.

#### 1. Packaging
- Caption: "Most people fail at side hustles because they copy the idea, not the system.✅️ Accio
  Work helps you find products worth selling based on demand, competition, and profit potential.
  Then it handles supplier sourcing, negotiation, Shopify listings, profit margins, ROI, daily
  reports, and dashboards. This is not a chatbot. This is a revenue engine. Comment "ACCIO WORK"
  and I will send you direct access.👇 Download Accio Work for Desktop from the link in my bio.☝️
  https://www.accio.com/work?src=p_igkol_handlytech @accio_b2b #AccioWork #AgenticBusiness
  #MyAccioWorks #AIAgent #AITools" [OBSERVED]. Note the tracked bio-link URL
  (`src=p_igkol_handlytech`) embedded directly in the caption — a trackable affiliate-attribution
  parameter, confirming this is a measurable paid placement, not just a disclosed brand mention.
- Frame 1 [OBSERVED]: Ayham talking head, hand raised, caption "already" — persona IS present here
  (unlike Video 7), a talking-head open consistent with the account's standard format.
- Curiosity gap: the caption's bold claim ("most people fail... because they copy the idea, not the
  system") is a legitimate bold-claim hook, business-advice framing.

#### 2. Hook (0–3s)
- DATA GAP (standing note). Sample shows talking head + a folder/copy-icon animation captioned
  "already," consistent with an opening line resembling "I already [built/found/tried] this."
- Hook taxonomy: **Bold claim** (business-advice framing) per §3.1.
- What the viewer sees: talking head + a small UI animation — a fairly standard current-era open.

#### 3. Structure & retention engineering
- Beat map [OBSERVED]: talking head "already" → screen-recording of a "Shopify Operator" AI-agent
  dashboard interface, captions "different" / "potential" / "pricing" → talking-head cutaways
  between demo beats → a product-listing screenshot (a "Braided Rope Dog Leash" product card) → a
  text/analysis panel ("The images") → an ROI/numbers breakdown panel → talking head "access now" →
  final bold "COMMENT 'Accio Work'" CTA card.
- One-idea-per-video: yes — "this AI agent automates dropshipping product research," a single
  coherent demo, structurally closer to Videos 4–6 than to Video 7's portfolio-dump.
- Pacing: high, matches current-era norm, talking-head/screen-record hybrid fully intact.
- Loop design: ends on the CTA card, funnel-close pattern (same as Videos 5–6).
- Captions: word-by-word style, matches current-era norm — format-consistent with the account's
  organic content, UNLIKE Video 7.

#### 4. Value proposition
- Practical value: moderate — shows a real tool's dashboard and a worked product example (dog
  leash) with ROI numbers, more demonstrated process than Video 7, but the topic itself
  (dropshipping/e-commerce automation) is a further step away from "AI in 30 seconds" tutorial
  content than even the account's other current AI-tool videos — a business-opportunity pitch
  dressed as a tool demo.

#### 5. Psychology scoring (STEPPS)
- **Parasocial/identity: INTACT** — unlike Video 7, Ayham's face and the account's standard visual
  format are fully present.
- **Practical Value: moderate** — real numbers/dashboard shown, but oriented toward starting a
  side-business (a bigger commitment ask) rather than a quick free trick.
- **Social Currency: low-moderate** — "side-hustle automation tool" is more of a personal-interest
  topic than a broadly shareable status signal.
- **Emotion: aspirational/low-arousal-positive** (financial-opportunity framing) rather than the
  high-arousal awe/anxiety that drives the account's biggest hits — per §2.3, a weaker emotional
  register. **Triggers, Public, Stories: low.**

#### 6. CTA & funnel mechanics
- "Comment 'ACCIO WORK' and I will send you direct access" PLUS a tracked bio-link URL — a
  dual-mechanic funnel (comment-DM AND trackable link), the most monetization-instrumented CTA in
  this dossier.
- Disclosed brand partnership (#AccioWork, @accio_b2b tag) — bottom-of-funnel paid content, same
  category as Video 7.

#### 7. Replicability verdict
- Template (as a CAUTIONARY example, not a recommended one): format-consistency (keeping the
  talking head, screen-record, word captions) is NOT sufficient by itself to save a sponsored post
  if the underlying TOPIC (e-commerce/dropshipping tooling) sits further from the account's stated
  niche ("AI in 30 seconds" tutorials/reviews) than its organic content does.
- Commodity vs. advantage: the Accio Work tool and dashboard are the sponsor's product; Ayham's
  format execution here is competent and on-brand, making this a useful control case — it isolates
  TOPIC MISMATCH and DISCLOSED-SPONSORSHIP as the likely drags, since the production/format
  variable is held constant with his organic top performers.
- Difficulty for Tangent: N/A (cautionary case).

#### 8. Why it lost
- Load-bearing reason: unlike Video 7 (total format collapse), this video's format is fully
  on-brand — persona, screen-record style, and captions all match the account's organic winners.
  Its underperformance therefore isolates two other variables: (a) disclosed sponsorship (§1.3.2/
  §3.4.3, a consistent cross-account pattern of paid posts underperforming), and (b) topic distance
  — dropshipping/e-commerce automation is arguably even further from "AI in 30 seconds" tutorial
  positioning than the account's typical AI-image/video tool content, compounding the mismatch this
  dossier's autopsy centers on.
- **The DELTA between Video 7 and Video 8 is instructive:** both flops, both sponsored, similar
  view counts (5,788 vs. 6,011 — a difference within noise). Video 8's meaningfully better format
  execution (persona intact, standard structure) did NOT translate into meaningfully better
  performance than Video 7's total format collapse — suggesting that once a post is
  disclosed-sponsored on this account, format quality has limited power to rescue it; sponsorship
  status and topic-fit appear to dominate the outcome more than execution craft does.

#### Sources
- `../ig_harvest/handlytech.md` (harvest 2026-07-25)
- `yt-dlp` metadata pull, instagram.com/reel/DXy2ppzokZt/, 2026-07-25
- Downloaded video file + 8-frame contact sheet, analyzed 2026-07-25

---

## C) The audience-death autopsy

**Central question:** how does an account with 989K followers end up with a 9.85K median reel
(1.0% median/follower ratio — the worst of 22 ranked accounts in this study)?

### Timeline [OBSERVED dates from `yt-dlp` timestamp pulls, cross-verified against the harvest file]

| Date | Event | Evidence |
|---|---|---|
| 2023-10-15 | Pin #3 posted: "Never Trust Screenshots" (30.8M views) — general social-media-safety content, no phone-hardware angle, no AI angle | [OBSERVED] |
| 2024-07-10 | Pin #1 posted: "Find your Stolen Phone Easily" (73.6M views) — phone-security/recovery tutorial | [OBSERVED] |
| 2025-01-20 | Pin #2 posted: "If your iPhone got stolen-DO THIS" (63M views) — phone-security tutorial, 2nd mega-hit on the same theme in 6 months | [OBSERVED] |
| **2025-01-21 → 2026-04-30** | **~15.5-month DATA GAP.** The 48-tile grid scroll performed for this study did not reach far enough back to surface any posts in this window. The exact date the account's bio/branding pivoted to "AI in 30 seconds" is therefore UNKNOWN — bracketed only by "after Jan 2025" (last pinned hit still on the old theme) and "by May 2026" (earliest observed current-era post is already fully AI-niche). | DATA GAP, logged in Method Log |
| 2026-05-01 | Earliest current-era grid tile observed: Video 8 (Accio Work, sponsored, FLOP, 6,011 views) — the account is already fully in "AI tools" niche and already running comment-bait CTAs by this date | [OBSERVED] |
| 2026-05-17 | Video 7 (Pippit, sponsored, FLOP, 5,788 views — persona absent entirely) | [OBSERVED] |
| 2026-06-01 | Video 6 (organic, 54.2K views, listicle format) | [OBSERVED] |
| 2026-06-08 | Video 5 (organic, 117K views, best trustworthy current performer) | [OBSERVED] |
| 2026-06-14 | DZj_knxI-vk (organic, 44K views, grid-only, not detail-pulled) | [OBSERVED, harvest grid] |
| 2026-06-16 | Video 4 (organic, 331K views, ANOMALOUS like-rate) | [OBSERVED] |
| 2026-07-25 | Harvest + this dossier compiled. 989K followers, 9.85K median. | [OBSERVED] |

### Testing the four hypotheses against the evidence

**(a) Audience-content mismatch — STRONGLY SUPPORTED, the primary driver.**
All 3 pinned mega-hits are general-audience "life hack" / digital-safety content (phone recovery
x2, fake-screenshot detection x1) — topically unrelated to "AI in 30 seconds" tutorials. None of the
3 pins mention AI, tools, or tutorials in any form. A viewer who followed after watching "Find your
Stolen Phone Easily" had zero signal they were about to receive an AI-tools feed. This is the
textbook setup for audience-content mismatch: virality imported an audience selected for a
completely different value proposition than what the account now delivers. Critically, **the three
pins are STILL PINNED at the very top of the profile today** (2026-07-25) — meaning any new visitor
discovering the account via search, a tagged mention, or a profile click still sees 2023–2025
phone-security content as the account's most prominent self-presentation, actively reinforcing the
mismatch for every new arrival rather than resolving it.

**(d) Algorithm demotion patterns — SUPPORTED as the MECHANISM through which (a) manifests, not
as an independent cause.**
Engagement-rate archaeology is the key evidence here. Comparing like-rates across eras (excluding
Video 4's disputed anomaly):
- Legacy pins: 2.40% (Video 3), 2.88% (Video 1), 0.92% (Video 2)
- Current-era organic tops: 3.79% (Video 6), 3.07% (Video 5)

**Per-viewer engagement quality has NOT collapsed — if anything it is comparable or slightly
better in the current era than on two of the three legacy hits.** What collapsed is REACH: 30.8M–
73.6M views (legacy) vs. 54K–331K views (current), a 93–1,350x drop. This is the signature of a
DISTRIBUTION problem, not a RECEPTION problem: the people who do see current content engage with it
reasonably well; the platform is simply showing it to far fewer people. The most coherent reading
[INFERRED, reasoned synthesis, not an official Instagram-disclosed mechanism]: a 989K-follower base
that is majority-mismatched (per hypothesis a) generates a persistently weak predicted-engagement
score for this account's posts among ITS OWN FOLLOWERS specifically (per §1.1.1, "your history with
the poster" and "information about the poster" are named ranking-signal families) — even though
NEW, well-targeted viewers who do see the content like it fine. That weak predicted-engagement
signal plausibly caps how aggressively Instagram expands distribution beyond the small initial test
audience (the "audition" model, §1.1.3), producing the current era's structurally low ceiling
regardless of individual video quality.

**(b) Follower-quality decay (bots/giveaway-chasing) — UNRESOLVED, not confirmed either way.**
No giveaway or contest posts were found via `WebSearch` or in any of the 8 detail-pulled captions.
No bot-detection/audit tool (e.g., HypeAuditor-class) was available in this environment — DATA GAP,
not investigated further. It remains [INFERRED, plausible but unconfirmed] that 30M–70M-view
general-audience virality is a classic vector for picking up large numbers of low-affinity
(not necessarily fake, just uninterested) followers who reflexively hit "follow" after one
viral watch — this is a real, distinct mechanism from (a)'s content-topic mismatch (this is about
follower INTENT/QUALITY, not topic fit), but this dossier could not independently verify it.

**(c) Content decline — WEAKLY SUPPORTED, not the primary driver.**
The current-era organic videos (5–6) show genuine craft: visual diagrams explaining techniques
(Video 5), clear multi-tool demos (Video 6), consistent branding, dense readable captions. This is
not obviously worse content than the legacy pins on a pure craft basis — and the like-rate evidence
above argues against a pure quality-decline story. The clearest CONTENT-level self-inflicted wound
is narrower: **near-universal reliance on withheld-value comment-gating** (Video 4 withholds the
actual prompts; nearly every current top performer and both flops use "Comment X" as the primary
mechanic) — a format the account's own three biggest-ever hits (Videos 1–3) never used at all. This
is a real, documented shift in strategy, but it reads more as a symptom of chasing a
comment/DM-funnel growth tactic once organic reach had already narrowed, not as the root cause of
the narrowing.

**Verdict:** (a) audience-content mismatch is the root cause; (d) algorithmic demotion is the
mechanism that turns that mismatch into a persistently low view ceiling; (c) content decline is not
well supported (per-viewer engagement holds up) except for the specific comment-gating pattern,
which is better read as a downstream coping strategy than a cause; (b) is a live, plausible,
UNRESOLVED hypothesis this dossier could not confirm or rule out with available tools.

### Warning signs, in sequence (for a new account's owner to recognize early)
1. A mega-viral hit lands on a topic ADJACENT TO but not identical with your stated niche (phone
   security vs. AI tools) — the first fork in the road; decide deliberately whether to lean into it
   or protect the niche, rather than letting the algorithm's reward signal make the decision for you.
2. A SECOND mega-hit lands on the SAME off-niche topic 6 months later (Video 1 → Video 2, Jul 2024 →
   Jan 2025) — this is the point the platform's own topic classifier, and the audience's own
   expectations, have concretely locked in around the wrong identity. This is the last easy point to
   course-correct before the mismatch compounds.
3. A pivot happens (sometime in the ~15.5-month observed gap) WITHOUT reworking the pinned/top-of-
   profile content — the account's self-presentation to new visitors still contradicts its output.
4. Median views on the new-niche content settle at a small fraction of follower count (this
   account: 1.0%) while per-viewer engagement RATE stays reasonable — the tell that this is a
   distribution/mismatch problem, not a quality problem, and that simply "making better videos"
   will not fix it alone.
5. The account leans increasingly on comment-gated CTAs as the primary growth lever — a
   compensating mechanic for lost organic reach that (per §1.3.2) risks reading as engagement bait
   and, per this dossier's evidence, was never needed for the account's actual biggest wins.
6. Sponsors keep booking based on follower count / media-kit stats rather than delivered
   performance, and NONE of the sponsored posts observed outperform organic median (here, both
   flops examined were sponsored AND below median) — a sign the monetization layer has decoupled
   from the actual audience relationship.

### What recovery would look like — and evidence of attempting it
Recovery, per the evidence base (§2.4 mere exposure/parasocial consistency, §3.4.2 series effects,
§4 niche-laddering) would look like: (i) narrowing/re-committing to one legible niche and keeping
format-consistent, on-persona content (exactly what Videos 5–6 do, and exactly what Video 7 breaks);
(ii) NOT diluting the new niche with off-niche monetization (Video 8's dropshipping-tool pivot works
against this); (iii) reworking the profile's own self-presentation (un-pinning or reframing the
legacy hits) so new visitors' first impression matches current output; (iv) sustained high-frequency
posting to rebuild a fresh predicted-engagement signal within the new niche (§3.4.1) — the account
IS doing this (observed ~4 posts/week cadence across the May–Jul 2026 window).

**Evidence of attempting recovery, observed:** the niche rebrand itself ("AI in 30 seconds" bio
positioning) is itself a deliberate recovery move — choosing a more monetizable/coherent lane
instead of continuing pure phone-tips content. High, consistent 2026 posting cadence. Consistent
comment-CTA format testing (a repeatable, scalable production system, even if its overuse is itself
a warning sign per above). Active brand-sponsorship pursuit within the new niche (Pippit, Accio
Work, CapCut).

**Evidence NOT observed (DATA GAP, not a confirmed absence):** no pinned "here's my new direction"
explainer post found anywhere in the 48-tile grid sample; the 3 off-niche pins remain pinned as of
2026-07-25 with no visible attempt to un-pin, reframe, or contextualize them for new visitors — the
single most actionable, currently-unaddressed lever available to this account.

### Why brands still pay him — media-kit economics vs. real reach
Per Account Header (§A), the ViralMango media kit and IG/Threads bio both advertise headline
follower/reach figures ("1.3M cross-platform," "1.5M trusted by," "4.17% engagement, 33.8K avg
likes") that a brand would reasonably read as a proxy for expected campaign performance. The two
disclosed sponsored posts this dossier examined (Videos 7–8) delivered 5,788 and 6,011 views and
66–71 likes — 0.6% of the account's own follower count, and BELOW the account's own organic median.
**Connecting to the ad-boost pattern documented elsewhere in this study (`00_INDEX.md`):** on
tiffintech and networkchuck, sponsored posts get artificially INFLATED view counts (10–74M) paired
with near-zero engagement — a paid-media view-boost that at least LOOKS good on a delivery report
even though it isn't real organic reach. **HandlyTech's sponsored posts get neither the inflation
nor the engagement** — Videos 7–8 are the most straightforwardly honest data points in this entire
study: two paid placements that simply underperformed, with no artificial view-boost cushioning the
number. The most likely explanation for continued brand interest [INFERRED]: deals are plausibly
priced and booked off the headline follower count and media-kit engagement-rate claims BEFORE
posting, with payment terms likely settled independent of (or before visibility into) actual
delivered performance — meaning the media kit's inflated-looking numbers are doing real commercial
work upstream of the point where a brand could discover the gap from the post itself.

---

## D) What NOT to do — anti-patterns for a new account

1. **Don't let an off-topic viral hit define your account's algorithmic/audience identity without a
   deliberate decision.** A second off-niche mega-hit compounds the problem fast (Videos 1→2, six
   months apart, same off-niche theme) — treat an early off-niche spike as a fork in the road, not
   a template to repeat.
2. **Don't leave off-niche legacy hits pinned once you've pivoted.** This account's top-of-profile
   content still (as of 2026-07-25) tells every new visitor "this is a phone-security channel,"
   directly contradicting its current "AI in 30 seconds" positioning — the single most fixable,
   currently-unfixed issue found in this dossier.
3. **Don't gate your core value behind a comment.** Video 4 withholds its actual prompts; the
   account's three biggest-ever hits (Videos 1–3) withheld nothing and needed no comment mechanic
   at all. Gating correlates with weaker structural trust, not stronger growth — deliver the full
   technique in-caption/on-screen (as Video 5 does) and gate only a secondary resource (a link).
4. **Don't drop your persona/format for sponsored content.** Video 7's total face/format
   replacement with a client's stock-photo slideshow is the single most damaging pattern observed
   in this dossier — it broke every mere-exposure/parasocial mechanism the account otherwise relies
   on, and the post fell below organic median with no compensating view-boost.
5. **Don't assume format consistency alone rescues a topic or sponsorship mismatch.** Video 8 kept
   the account's standard on-persona format and still flopped at nearly the same rate as Video 7's
   total format collapse — once a post is disclosed-sponsored and off-niche, execution craft has
   limited power to save it.
6. **Don't let your media kit / bio "trusted by" numbers drift unreconciled from observed reach.**
   A 34–150x gap between a headline follower/reach figure and actual median per-post reach is a
   governance problem waiting to be discovered by a skeptical brand, journalist, or (per this
   dossier) a research audit — reconcile or caveat the number before a partner does the math
   independently.
7. **Don't stack low-fit sponsorships once volume is up.** Every sponsored post examined in this
   dataset underperformed organic median; more off-niche paid deals compound the mismatch rather
   than monetizing genuine reach.
8. **Don't over-index on "comments > likes" as proof a growth tactic is working.** It shows the CTA
   mechanically converts, but leaning on it as the SOLE lever (visible on nearly every current top
   reel in this dossier) is a fragile dependency if it ever reads as bait (§1.3.2) or if a genuinely
   broad-appeal video doesn't reappear to reset the account's predicted-engagement baseline.
9. **If you pivot niches, don't do it silently.** No pinned "here's my new direction" explainer post
   was found anywhere in the sampled grid — a low-cost, high-leverage move (helping a mismatched
   existing audience self-select in or stop expecting old content) that this account has not
   visibly taken.
10. **Don't mistake reach for reception, or vice versa, when diagnosing a stall.** This account's
    per-viewer engagement RATE on current organic content (3.07%–3.79%) is comparable to or better
    than two of its three legacy hits — the failure mode here is DISTRIBUTION, not content quality.
    Misdiagnosing this as "make better videos" would waste effort; the actual lever is closing the
    audience-content gap (points 1–2, 9 above).

---

## E) Method log

**Read (mandatory, first):** `QC_PROTOCOL.md`, `templates/video_postmortem_template.md`,
`03_virality_science.md` — full text of all three, before any analysis.

**Primary data:** `ig_harvest/handlytech.md` — read in full at task start (84 lines, no anomaly
section present at that point); re-checked via `grep` mid-task and found a 7-line **"## Anomaly
re-verification" section had been appended by a separate research agent** since the first read
(confirmed present, re-read in full, incorporated into Video 4's post-mortem and the Autopsy
section above). `ig_harvest/00_INDEX.md` — read in full for cross-account context and the
median/follower ranking table.

**`yt-dlp` metadata pulls** (`--print`/`--dump-json`, no download), all 2026-07-25, against all 8
selected shortcodes: CybW5zct2AA, DFC6zh3iZKn, C9PdusWtkOh, DZUg7ZxIHLv, DYcI0guoijZ, DXy2ppzokZt,
DZj_knxI-vk (grid-context only), DZChXWoIaHF. All returned like_count/comment_count/timestamp/
description fields; **view_count and play_count were consistently `None`/`NA` for every reel** —
Instagram does not expose view counts via this access path, logged as a standing method
limitation (view counts throughout this dossier come exclusively from the harvest file's
browser-rendered grid pull, not from `yt-dlp`).

**DZozx8UoTDy (Video 4) specifically:** first `yt-dlp` attempt returned "Instagram sent an empty
media response" (a transient failure, not a genuine access block). Retried ~3 seconds later:
succeeded, returned 114 likes/59 comments. Retried again ~15 minutes later: returned 114 likes/59
comments again (stable, matching the first successful pull) — this dossier's own two pulls agree
with each other but conflict with the harvest file's two pulls (both 59/59). Presented as an
unresolved conflict in Video 4's post-mortem and the Autopsy, not adjudicated.

**Video downloads:** all 8 selected reels downloaded in full via `yt-dlp -f "best[height<=720]/best"`
into the scratchpad (`handlytech_videos/`), 1.96MB–4.96MB each, all 720x1280 native vertical, no
watermarks observed. Duration and resolution confirmed via `ffprobe`.

**Visual analysis:** for each of the 8 videos, generated an 8-frame contact sheet via `ffmpeg`
(`fps=8/duration,scale=200:-1,tile=4x2`, i.e., 8 frames evenly spaced across the FULL runtime, not
just the first second) and visually inspected all 8 sheets. This is the evidentiary basis for the
Packaging/Hook/Structure sections of every post-mortem above, and is explicitly a
partial-sampling `[OBSERVED]` tier (8 stills per video), not a continuous watch-through — logged
once as the standing DATA GAP for verbatim transcripts across all 8 videos (no ASR/speech-to-text
tool is available in this environment).

**`WebSearch` queries run:** "Ayham Joukhadar HandlyTech viralmango media kit"; "\"handlytech\"
instagram Ayham Joukhadar AI tutorials"; "\"Ayham Joukhadar\" HandlyTech brand partnerships";
"handlytech Ayham Joukhadar TikTok YouTube followers"; "\"handlytech\" OR \"Ayham Joukhadar\"
interview podcast creator growth story"; "Ayham Joukhadar HandlyTech when started AI content pivot
2025"; "\"handlytech\" giveaway OR contest instagram". No interview/press coverage of the creator
was found (DATA GAP — his growth story, exact pivot date, and real-world background remain
unconfirmed beyond the media-kit's single "Croatia" claim). No giveaway/contest content was found
(relevant to hypothesis b, which remains unresolved).

**`WebFetch` calls:** `viralmango.com/HandlyTech` (succeeded — the media-kit data used throughout
§A and the Autopsy); `threads.com/@handlytech` (succeeded — 142K followers, bio, recent post
topics); `tiktok.com/@handlytech` (FAILED — returned only the page title, JS-rendered content not
accessible via this tool, logged as a DATA GAP on independently verifying the media kit's TikTok
figures); `instagram.com/handlytech/` direct fetch (FAILED — returned only base64 image data, no
extractable text, logged as a DATA GAP, though superseded by the harvest file's own browser-based
pull of the same information); `web.archive.org` snapshot listing and Wayback Availability API for
the profile (both returned no usable archived snapshots — logged as a DATA GAP on reconstructing
historical, era-specific follower counts to compute view/follower ratios for the 2023–2025 pinned
hits specifically); `infldb.com/top-influencers/Syria` (succeeded as a fetch, but the account did
not appear in the listing — inconclusive on creator location, not treated as either confirmation or
refutation).

**Explicitly NOT used, per task constraint:** `claude-in-chrome` / browser-automation tools —
reserved, honored throughout; all Instagram-side data came from the harvest file, `yt-dlp`, and the
downloaded video files.

**Not attempted / out of scope given time budget:** independent bot/follower-authenticity audit
(no tool available); full continuous watch-through with real-time note-taking for all 8 videos
(substituted with the 8-frame contact-sheet method, disclosed above); pulling additional grid tiles
beyond the harvest's original 48 to close the ~15.5-month 2025 observation gap.

---

## F) Compact summary

**Autopsy verdict:** @handlytech's 1.0% median/follower ratio — the worst in this 24-account study —
is primarily an **audience-content mismatch** problem, not a content-quality problem. All 3 of the
account's all-time mega-hits (30.8M–73.6M views, 2023–2025) are general-audience phone-security/
digital-safety content, topically unrelated to the account's current "AI in 30 seconds" niche, and
all 3 remain pinned at the top of the profile today — actively re-priming every new visitor toward
the wrong expectation. Per-viewer engagement RATE on current organic content (3.07%–3.79% like-rate)
is comparable to or better than 2 of the 3 legacy hits (0.92%–2.88%), which rules against a pure
content-decline story: the failure mode is DISTRIBUTION (reach collapsed 93–1,350x), not RECEPTION.
The most coherent mechanism connecting the two: a majority-mismatched follower base plausibly caps
Instagram's own predicted-engagement scoring for this account, structurally suppressing distribution
regardless of individual-video quality — algorithmic demotion as the transmission mechanism for an
underlying audience mismatch, not an independent cause. One hypothesis (follower-quality decay via
giveaway/bot growth) could not be confirmed or ruled out with available tools — an honest open
question, not resolved here.

**Anti-pattern list (10, full detail in §D):** don't let off-niche virality define your identity;
don't leave off-niche hits pinned after a pivot; don't gate your core value behind a comment; don't
drop your persona for sponsored content; don't assume format consistency alone rescues a
mismatched/sponsored post; don't let media-kit numbers drift unreconciled from real reach; don't
stack low-fit sponsorships; don't over-index on comments-beating-likes as proof of health; don't
pivot niches silently; don't misdiagnose a distribution problem as a content-quality problem.

**Surprises:**
1. The account's three biggest-ever hits used ZERO comment-bait CTAs — the mechanic dominating
   100% of its current top performers and both flops was never needed for its actual virality.
2. Per-viewer engagement quality has NOT meaningfully declined in the current era versus the legacy
   pins — the ceiling problem is almost entirely a reach/distribution collapse, not a "people don't
   like this content" problem.
3. The account's sponsored posts get NEITHER the view-count inflation seen on other accounts in
   this study (tiffintech, networkchuck) NOR real organic-level engagement — they are the most
   "honestly bad" data points in the whole 24-account corpus, underperforming even this account's
   own weak organic median.
4. One flop (Video 7, Pippit-sponsored) abandoned the creator's face/persona entirely in favor of a
   client stock-photo slideshow — the single most extreme format break found in any post-mortem in
   this dossier.
5. This dossier's own independent re-verification of the flagged 331K-view/59-like anomaly reel
   produced a THIRD data point (114 likes) that conflicts with both of the harvest file's own two
   internal pulls (59 likes each) — a genuine, still-unresolved measurement discrepancy, disclosed
   rather than papered over, exactly as the QC protocol requires.
