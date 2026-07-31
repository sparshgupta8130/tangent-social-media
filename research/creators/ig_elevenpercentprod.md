# Creator Dossier: Devin Huynh / Eleven Percent (Instagram @elevenpercentprod)

**Status:** SEED account (user-provided) + the highest non-follower-reach account in the entire
24-account study (156% median-views-to-followers). Held to maximum scrutiny per the assignment
brief — Devin sells **AutoEdit**, a Claude-powered Adobe Premiere Pro plugin, making this the single
most strategically relevant account in the corpus for a Claude-based creative-plugin brand.

**Analyst method:** Primary data = `research/ig_harvest/elevenpercentprod.md` (live IG grid + 7
detail pulls, harvested 2026-07-25) and `research/ig_harvest/00_INDEX.md` (cross-account context),
per assignment instructions. This dossier **re-verified and deepened** that primary data with direct
`yt-dlp` pulls against the same 7 Instagram reel URLs (exact like/comment counts, full captions,
precise durations, and downloaded video files), then extracted 1fps contact-sheet frame grids via
`ffmpeg` and visually inspected every frame of all 7 videos (this is the primary evidentiary basis
for Hook/Structure/Production sections below — Instagram reels carry no transcript/subtitle track,
and the reels are burned-in-caption + trending-audio format, not narrated talking-head, so visual
frame inspection is the correct and highest-fidelity method available). Cross-referenced against
YouTube (`@elevenpercent`) and TikTok (`@elevenpercentprod`) via `yt-dlp` flat-playlist catalog
scans and direct video/caption pulls to find literal cross-posts (proxies) and to benchmark
cross-platform performance. `claude-in-chrome` browser tools were **not used**, per instructions
(reserved). WebSearch/WebFetch were used for AutoEdit product/funnel research (Product Hunt,
elevenpercent.net, autoeditai.net).

All figures are `[OBSERVED]` with source + as-of date unless tagged `[REPORTED]` or `[INFERRED]`.

---

## A. Account header + funnel map

### A.1 Cross-platform identity

| Platform | Handle | Followers/Subs | Source | As-of | Confidence |
|---|---|---|---|---|---|
| Instagram | `@elevenpercentprod` | **85K** (84.9K header / 606 following / 203 posts per og:description) | `ig_harvest/elevenpercentprod.md` `[OBSERVED]` | 2026-07-25 | HIGH |
| YouTube | `@elevenpercent` | **~40.7K** subs, 3.73M total views, 592 videos | `00_seed_accounts.md` citing vidIQ `[REPORTED]`, carried forward, not re-verified this pass | 2026-07-25 | MED (single-tracker) |
| TikTok | `@elevenpercentprod` | Not obtainable — `yt-dlp --flat-playlist` on the profile URL returns only per-video rows, no `channel_follower_count` field populated | This dossier, direct attempt | 2026-07-25 | **DATA GAP** |
| Website/store | elevenpercent.net (legacy preorder pages) + **autoeditai.net** (live product, current) | — | `[OBSERVED]` via WebFetch, both domains active simultaneously | 2026-07-25 | HIGH |

Bio (`[OBSERVED]`, harvest): *"Helping Video Editors save time with AI Plugins, Tutorials, and
Templates. / No. 3 on Product Hunt"* — the creator's own bio self-reports **#3**, which matches this
dossier's direct WebFetch of the Product Hunt page (see A.3). Note: a WebSearch AI-summary
independently claimed AutoEdit "reached #1 Product of the Day in both Marketing and Photo & Video
categories" — three independent sources (his own bio, `00_seed_accounts.md`, and this dossier's
direct Product Hunt WebFetch) agree on **#3 overall / 329 upvotes**; the "#1" claim could not be
corroborated on the Product Hunt page itself and is flagged as a likely search-summary error, not
used as fact.

### A.2 Origin story (carried forward from `00_seed_accounts.md`, not re-researched this pass)

Started as a free high-school videographer, built a paid videography/production service business
over ~5 years (Mercedes, Coachella, touring with Lil Baby), CSU Northridge Film & Cinema Production.
**The AI-plugin pivot is recent**: this dossier's own YouTube catalog scan (§D) independently
confirms this — the oldest ~20 items in a 200-video flat-playlist sweep of `@elevenpercent/shorts`
are generic editing tutorials (Frutiger Metro Y2K overlay tutorials, camera-shake VFX tricks, title-
card design) with **zero** AutoEdit/Claude/plugin content, while the most recent ~180/200 are almost
entirely AutoEdit demo/CTA content. This is independent visual confirmation of the pivot timeline
the seed doc reported from bio/scholarship-page research.

### A.3 The product: AutoEdit

`[OBSERVED via WebFetch, 2026-07-25]` AutoEdit is built by a **3-person team** — Istiak Ahmad, Devin
Huynh, Priyanka Mandal (Product Hunt maker credits) — not a solo-creator side project. Mechanism, per
WebSearch summary of product pages: **transcribes audio via ElevenLabs, sends the transcript to
Claude, and Claude builds a rough cut based on meaning** (removes filler words, repeated takes,
dead air; not just silence-detection). Modes: Creator Mode (talking-head/YouTube), Music Video Mode,
Event Recap Mode, Gaming Mode (per `00_seed_accounts.md`, corroborated by reel content in §B).

**Pricing timeline — a real, observed shift, not inference:**
- `elevenpercent.net/pages/autoedit-creator` (legacy page, still live) shows a **one-time preorder**
  model: Creator Basic $9.99 (90 min processing) / Creator Pro $109 (1,200 min), "converts to
  subscription after launch," no refunds, beta access framed as "early creator group." This matches
  the Apr–May 2026 reel captions ("preorder this plugin").
- `autoeditai.net` (current live product, `[OBSERVED via WebFetch]` 2026-07-25) shows a **live
  subscription SaaS**: Lite $9.99/mo (4 videos/45 min), Creator $29.99/mo (currently 51% off first
  month), Pro $79.99/mo, Business/Enterprise custom — with a genuine **free trial, no credit card
  required**. Claims "15,000+ editors," 4.67/5 Trustpilot, 100+ reviews.
- **Reconciliation**: the product visibly moved from preorder (beta, Mar–June 2026) to live paid
  SaaS with a real free trial (post Product Hunt launch, June 2026 onward) — this maps cleanly onto
  the reel caption language changing from "preorder" (April reels) to "download/try for free" (May
  reels and later), i.e., the captions accurately tracked the product's real commercial state at
  time of posting rather than being deceptive `[INFERRED, but directly supported by dated evidence]`.

### A.4 Funnel map — the "comment KEYWORD" mechanic

**What was confirmed:**
- Every one of the top 5 reels (and the overwhelming majority — 180/200 — of his YouTube Shorts
  catalog, and every TikTok video sampled) runs a **comment-a-keyword-for-the-link** CTA: keywords
  observed include CLAUDE, CREATOR, AUTOEDIT, EVENTS, SUITE, TEXT, ANGLES, FABLE — i.e., this is not
  one keyword but a **rotating set tied to specific product modes/features**, tested across dozens of
  near-identical videos.
- `[OBSERVED, direct discrepancy]` One top reel (DWqP0Exk0iW, 916K views) has an Instagram **caption**
  reading "comment 'Claude' if you want the link to preorder this plugin," but its own **burned-in
  on-screen CTA text** reads "comment 'creator' if you want try this plugin" — and its exact
  cross-post to YouTube (`wNgVCxz7mgo`, verified word-for-word identical description, see §C) also
  says "creator," not "Claude." This means the true, video-embedded keyword and the platform caption
  text can diverge on the same post — evidence the keyword is a tracked/functional variable (almost
  certainly tied to a specific automation trigger per product mode) rather than cosmetic copy, and
  that caption text is written somewhat loosely relative to the "real" in-video CTA.
- **What the DM delivers, and by what tool — DATA GAP.** This dossier searched his own site pages
  (`elevenpercent.net/pages/autoedit-creator`, `elevenpercent.net/pages/affiliate`, `autoeditai.net`)
  via WebFetch and found **no mention of ManyChat, DM automation, or any comment-to-DM mechanism** on
  any owned page. WebSearch for "elevenpercentprod ManyChat" returned only generic ManyChat/Claude
  integration tutorials, not anything specific to this account. The mechanism is almost certainly
  ManyChat or an equivalent Instagram-approved comment-automation tool (this is the standard,
  Meta-approved way this exact CTA pattern is executed at this comment volume — 11K–61K comments
  per top post is not manually repliable — and `03_virality_science.md` §3.4.3 documents ManyChat's
  product behavior directly for this pattern), but **no direct first-party confirmation was found
  that Devin/AutoEdit specifically uses ManyChat** — logged as a gap per protocol, not asserted as fact.
- **Funnel shape (what IS confirmed):** Reel/Short with CTA → comment triggers automated(-presumed)
  DM → DM contains a link → link routes to either the preorder page (`elevenpercent.net`, Apr–May
  reels) or the live product (`autoeditai.net`, current) → free-trial/preorder signup → paid
  conversion (Lite/Creator/Pro tiers). This is a **single-hop, direct-to-product funnel** — unlike
  `nateherk`'s two-hop Short→long-form-video→Skool pattern documented in `yt_nateherk.md`, Devin's
  reels sell the product directly with no intermediate content layer.
- **Affiliate layer**: `elevenpercent.net/pages/affiliate` confirms a tiered commission program —
  25% (Starter, "$37.25 per sale" implying a ~$149 reference sale price), 30–40% (Verified Creator),
  50% (Partner/Scale) — a secondary, creator-to-creator distribution channel alongside his own reels,
  `[OBSERVED via WebFetch]`.

### A.5 Multi-platform cross-post structure (sets up §C)

The **same underlying content** is posted near-simultaneously to Instagram Reels, YouTube Shorts,
and TikTok — confirmed via an exact-match proxy (§C.2: `wNgVCxz7mgo` YT Short = `DWqP0Exk0iW` IG
reel, identical caption, identical 24s duration, posted 5 days apart). Performance across platforms
for the same content type is **not remotely comparable**: IG reels in this dossier's sample run
800K–2.5M views; the YouTube Shorts catalog (200-video sweep) tops out at ~12,000 views with a
median in the low hundreds; TikTok samples (15 most recent) run 151–1,859 views. Instagram is where
essentially all of this creator's reach lives — a critical, quantified finding for §C.

---

## B. Video post-mortems (7 videos: top 5 by views + 2 flops)

Selection: exactly per assignment spec — the 5 highest-view reels and 2 lowest-view reels from
`ig_harvest/elevenpercentprod.md`'s detail-pull table (itself selected as top-5/bottom-2 from the
60-tile grid sweep). All 7 videos were downloaded directly via `yt-dlp` from their live Instagram
URLs on 2026-07-25 and visually inspected frame-by-frame (1fps contact sheets, ~24–34 frames/video).

---

### VIDEO 1 (TOP #1, 2.5M views): "POV: you got tired of editing so you ask claude to edit for you under 2 min"

#### 0. Identity & stats
- URL: instagram.com/reel/DX-bJErPxe7/. Platform: Instagram Reels. Posted **2026-05-05**
  `[OBSERVED, yt-dlp timestamp/upload_date, 2026-07-25]`. Length: **24.13s** `[OBSERVED, ffprobe]`.
- Views: **2.5M** `[OBSERVED, ig_harvest grid scrape, 2026-07-25, HIGH]` (Instagram does not expose
  view_count via yt-dlp's extractor for this creator — grid scrape is the only view-count source).
  Likes: **53,167**. Comments: **61,429**. Both `[OBSERVED directly via yt-dlp info.json, 2026-07-25,
  HIGH — exact figures, not the harvest file's rounded "53K/61K"]`.
- Rank: #1 of 60 tiles surveyed; ~18.8x the account's 133K median (`ig_harvest` computed stat).
  **Comments (61,429) exceed likes (53,167)** — like-rate 2.13%, comment-rate 2.46% — an inverted
  ratio versus normal engagement patterns (likes almost always exceed comments by 5–20x on typical
  content); see §C for why this is the funnel's fingerprint.

#### 1. Packaging (the pre-click/pre-swipe layer)
- First on-screen text (visible from frame 1): **"POV: you got tired of editing so you ask claude to
  edit for you under 2 min"** — full sentence present in frame 1, not built up gradually.
- First-frame visual: Devin lying in bed, laptop balanced on his chest/lap, small Premiere Pro (Pr)
  and an orange sunburst icon (AutoEdit brand mark) badges pinned in the top area of frame from
  roughly frame 3 onward `[OBSERVED, frame sheet]`.
- Curiosity gap: the promise ("edit for you under 2 min") is named upfront but not yet shown —
  classic result-promised/process-teased structure.

#### 2. Hook (0–3s)
- No verbatim spoken line obtainable — `DATA GAP: no narration audio; this is a burned-in-caption +
  trending-audio reel. YouTube auto-caption pull on a thematically related proxy (Xp3aUNp30gU) only
  transcribed background song lyrics ("Formula... on the Monday too... With the Probate Crew"), not
  narration — confirms there is no spoken dialogue to transcribe.` Text overlay carries the hook.
- Hook taxonomy: **"POV" / in-medias-res framing** combined with a **result-first curiosity gap**
  (§2.1.1/§3.1 of `03_virality_science.md`) — viewer is placed directly into a relatable scenario
  ("you got tired of editing") with an immediate promised payoff (2-min AI edit).
- What the viewer sees: a real person, in a mundane bedroom setting, with a real laptop and real
  Premiere Pro UI already open — not a polished studio shot. This "authenticity" staging is
  consistent across the top 5 (see §7).

#### 3. Structure & retention engineering
- Beat map (frame-sheet-derived, `[OBSERVED]`, timestamps approximate ±1s from 1fps sampling):
  - 0–5s: Hook text + bed/laptop scene, transitions into a live Premiere Pro timeline with waveform.
  - 5–11s: "and i still charge my clients $5k/project for editing😭" (status-flex reveal) → "this
    claude plugin uses AI to understand your video" over timeline with green AI-selected takes.
  - 11–17s: AutoEdit panel UI shown on a tablet: "Select Takes / AI has detected repeated takes" with
    real flagged transcript lines ("So as I was saying, as a video editor you should... um. Wait no I
    messed up again." tagged "Bad Take") → "it finds the best takes in the video for me" → Captions
    styling panel (font/size/weight sliders) → "it adds captions too*" → cutaway to a Dwayne Johnson
    clip demonstrating the tool cutting "actual bad takes."
  - 18–24s: "it works on any video with talking in it..." → cutaway to Fortnite gaming footage with
    kinetic-typography captions ("THIS IS / PLUGIN FOR...") demonstrating cross-genre versatility →
    final CTA "comment 'claude' to try it for free" over the Premiere timeline.
- Open loop: "under 2 min" claim opened in the hook is implicitly closed by the demo montage showing
  the full pipeline (select takes → captions → done) compressed into ~13s of screen-time.
- One-idea-per-video: yes — single throughline (AI edits for you fast), no digression.
- Payoff placement: **drip** — a new capability is revealed roughly every 3–4s (finds best takes →
  adds captions → cuts bad takes → works on any content type), each with its own micro-caption,
  rather than one single reveal — classic multi-loop retention structure (§2.6.1).
- Pacing: high — a hard cut or UI-panel change roughly every 1–2s throughout; no static shot exceeds
  ~3s. Captions/text overlay present on effectively every frame (sound-off legible, §3.3.1 compliant).
- Loop design: ending CTA text sits over the same Premiere timeline visual the video opened with —
  mild visual rhyme, not a strong rewatch trap.

#### 4. Value proposition
- Walk-away: a named tool (AutoEdit), a named AI brand (Claude) doing something concrete and
  legible (finds takes, cuts bad ones, adds captions), demonstrated on real UI, not described in the
  abstract.
- Practical value class: **tool discovery** primarily, with a thin layer of **copyable workflow**
  (viewer sees the actual panel sequence: Select Takes → Captions → Generate Rough Cut).
- Specificity: MED-HIGH — real UI screenshots with real flagged-takes transcript text are shown, but
  no exact prompt/settings values are dictated for the viewer to replicate; it's a product demo, not
  a tutorial.

#### 5. Psychology scoring
- STEPPS: **Practical Value** (a real time-saving tool) is the dominant pillar. **Social Currency**
  is present via the flex line ("i still charge my clients $5k/project") — sharing/discussing this
  signals insider knowledge of a new AI tool. **Triggers** — editing is a frequent pain point for the
  video-editor niche audience specifically. **Emotion** — the register is closer to amusement/mild
  awe ("wait, AI can actually do this?") than high-arousal anger/anxiety; moderate arousal.
- Primary emotion: amusement + mild awe/surprise. Not sadness/calm (favorable per §2.3).
- Identity-signaling share motive: an editor sharing this to a peer editor says "I found the tool
  that's about to change our job" — high social-currency payload for the specific niche audience.
- Save/send trigger: strong — this is exactly the "send this to a specific editor friend" content
  type Instagram's own signals reward (§1.1.2), and the abnormally high comment-rate (§0) shows the
  CTA successfully converted attention into the sends/comments Instagram weighs most.

#### 6. CTA & funnel mechanics
- Explicit CTA: "comment 'claude' to try it for free" — bare comment-keyword gate, but attached to a
  video that already delivers substantial standalone content (a real product demo), which is the
  distinguishing test `03_virality_science.md` §1.3.2 uses to separate this from prohibited
  content-free engagement bait.
- Comment-bait mechanics: comment volume (61,429) exceeding like volume (53,167) is itself evidence
  the CTA is functioning as designed — comments are being driven specifically by people executing the
  "comment claude" instruction, not just organically reacting.
- Funnel position: **top-of-funnel viral bait that IS the sales page** — no nurture layer; comment →
  (presumed DM) → product link, directly.

#### 7. Replicability verdict
- Extractable template: (1) mundane/relatable real-life setting for the hook (bed, not a studio); (2)
  name a specific, high dollar-figure status flex tied to your niche's pain point; (3) reveal the AI
  tool by name within the first ~5s; (4) screen-record the REAL product UI doing the REAL task,
  captioned every ~2s; (5) show it working on at least 2 different content genres to broaden
  perceived utility; (6) close on a comment-keyword CTA tied to a working (even if manual-at-small-
  scale) DM delivery.
- Commodity vs unfair advantage: the hook structure and pacing are fully commodity/copyable by any
  creator. Devin's unfair advantage is that **he owns the product being demoed** — the UI screen-
  recordings are real, not staged/mocked, which is not replicable by an affiliate or a creator
  covering someone else's tool with the same credibility.
- Difficulty for Tangent to execute: **LOW-MED** — the hook/structure/pacing formula is directly
  copyable; the constraint is needing a real, demoable product (Tangent doesn't sell a plugin, so
  this specific "product demo as viral hook" format would need adaptation to a service/portfolio
  framing rather than a literal SaaS UI demo).

#### 8. Why it won
- The single most load-bearing factor: **a legible, high-curiosity claim ("AI edits your video for
  you") demonstrated with real, credible screen-capture evidence**, inside a relatable/authentic
  (bed, not studio) framing that lowers the perceived "ad" feel despite being a direct product pitch.
- Secondary factors: posting date (May 5, 2026) sits right at AutoEdit's public launch window (May
  2026 per `00_seed_accounts.md`), so this reel likely benefited from genuine product-news timeliness,
  not just format quality. The multi-genre demo (talking-head AND gaming footage) broadens the
  addressable "send this to..." audience beyond just YouTube-style creators.
- No evidence of luck/trend-surfing (no trending-audio-based virality detected; hook is fully
  content-driven) — this reads as a **repeatable, engineered formula**, not a one-off fluke, which
  §C substantiates by showing 4 more near-identical reels also cleared 800K+.

#### Sources
- https://www.instagram.com/reel/DX-bJErPxe7/ (yt-dlp direct pull, video + info.json, 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md` (view count, grid rank)
- `research/03_virality_science.md` §1.1.2, §1.3.2, §2.1.1, §2.6.1, §3.1

---

### VIDEO 2 (TOP #2, 2.1M views): "i charge my clients $26K/mo for video editing... and i let claude AI edit for me in under 2 min"

#### 0. Identity & stats
- URL: instagram.com/reel/DXlFWL5EkaN/. Posted **2026-04-26** `[OBSERVED, yt-dlp]`. Length: **24.13s**
  `[OBSERVED, ffprobe — identical duration to Video 1 to 6 decimal places, see §D]`.
- Views: **2.1M** `[OBSERVED, harvest grid]`. Likes: **26,429**. Comments: **47,699**
  `[OBSERVED, yt-dlp, 2026-07-25, HIGH]`. Like-rate 1.26%, comment-rate 2.27% — comments again nearly
  **double** likes, an even more extreme version of Video 1's inversion.
- Rank: #2 of 60; ~15.8x the 133K median.

#### 1. Packaging
- First-frame text: "i charge my clients $26K/mo for video editing..." over a shot of Devin sitting
  ON A TOILET in what is unmistakably a public restroom (visible grab-bars, institutional tile,
  toilet-paper dispenser), laptop balanced on his lap `[OBSERVED, frame sheet]`.
- The location choice is a deliberate absurdist pattern-interrupt — a much stronger visual hook than
  Video 1's bed setting; it is genuinely odd and attention-grabbing on sight, independent of the text.

#### 2. Hook (0–3s)
- No spoken narration — text overlay again carries the full hook in frame 1 (no build-up).
- Hook taxonomy: **bold income claim** ("$26K/mo") combined with **pattern-interrupt setting**
  (bathroom) — a compound hook stacking two taxonomy types from §3.1 simultaneously.
- What the viewer sees: an incongruous, comedic scene (person editing/working while seated on a
  toilet) that is visually arresting even muted and even before the text registers.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED, frame sheet]`:
  - 0–5s: toilet-scene hook, "$26K/mo" flex, cuts to laptop-screen close-up (top-down POV of hands on
    keyboard) with Pr + AutoEdit badges.
  - 5–11s: "and i let claude AI edit for me in under 2 min" → Premiere timeline with gaming footage
    (a build-battle/exploration game) being processed, green AI-selected segments appear, on-screen
    text reads "i don't think im ever editing again bro 😭" (a second, escalating reaction beat).
  - 11–17s: "it adds captions too*" over a tablet showing multiple demo output clips (a "CIGACHAD"
    labeled clip, a "JELLYBEAN?" labeled clip, a skateboarding clip with "SKIBIDI RIZZ" captions) —
    demonstrating caption-styling variety across different meme/caption aesthetics.
  - 17–24s: "it uses AI to cut out the actual bad takes" over a finger tapping through the Premiere
    timeline, cutting between clips → final CTA "comment 'creator' if you want try this plugin"
    (note: keyword is "creator," not "Claude," despite the account/product being Claude-branded — see
    §A.4 for the cross-platform confirmation this is a real, intentional variant, not a typo).
- Open loops: the toilet setting itself functions as an unstated loop ("why is he on a toilet") that
  is never explicitly addressed/resolved — it's a sustained sight gag rather than a plot loop, but it
  keeps visual interest for the full 24s since he stays in that setting through the opening act.
- One-idea discipline: yes, same core message as Video 1, restructured.
- Pacing: high, same cadence as Video 1 (cut/UI-change roughly every 1–2s).

#### 4. Value proposition
- Same core proposition as Video 1 (AI tool discovery), with more emphasis this time on **caption/
  meme-styling variety** (three different caption aesthetics shown back to back) as a distinct
  feature callout not emphasized in Video 1.
- Practical value class: tool discovery, MED specificity (shows the styling options concretely).

#### 5. Psychology scoring
- STEPPS: Social Currency is amplified here relative to Video 1 — a $26K/mo income flex is a bigger,
  more shareable/screenshot-able claim than $5K/project, and the toilet setting adds a comedic/
  "iconic" quality that makes the clip itself more memorable and describable to a friend ("dude he
  filmed this on a toilet").
- Primary emotion: amusement (comedic setting) blended with the same mild-awe tool-discovery beat.
  Arguably higher arousal than Video 1 due to the comedic surprise of the setting.
- Identity signaling: sharing "look at this guy on the toilet talking about his $26K/mo editing
  business" carries entertainment-social-currency independent of the product pitch — a second,
  parallel share-reason beyond the tool itself, likely explaining why this reel out-performed on raw
  view count relative to Video 1 despite a lower like-rate.
- Save/send: the toilet gag specifically creates an addressable "you have to see this" moment distinct
  from the product-utility send-trigger in Video 1.

#### 6. CTA & funnel mechanics
- CTA keyword "creator" (in-video) vs "Claude" (IG caption text) — see §A.4 discrepancy note. Both
  routes presumably resolve to the same funnel, but this is the clearest direct evidence in the
  sample that caption text and video-embedded CTA are not always kept in lockstep.
- Same bare-comment-keyword-attached-to-real-demo-content structure as Video 1.

#### 7. Replicability verdict
- Extractable template: same core formula as Video 1, PLUS the specific lesson that an absurd/
  incongruous filming location (bathroom, in this case) can function as a zero-cost, high-impact
  pattern-interrupt hook layered on top of the income-flex text hook.
- Commodity vs unfair advantage: the bathroom-stunt device is fully commodity and directly copyable
  by anyone regardless of product; the underlying product demo remains Devin's unfair advantage.
- Difficulty for Tangent: LOW for the stunt-location device itself; MED for the overall format for
  the same product-ownership reason as Video 1.

#### 8. Why it won
- Most load-bearing factor: the compound hook (absurd location + income flex) generates two
  independent share/attention triggers stacked in the same 3 seconds, which likely explains why this
  out-ranks Video 3–5 despite a materially lower like-rate — raw reach (views) and comment-conversion
  (funnel efficiency) are not the same axis, and this video appears to have won primarily on reach/
  novelty rather than on-topic funnel efficiency (see the like-rate table in §C).
- No trending-audio or news-cycle luck detected — again a content-engineered result, timed 9 days
  before Video 1, both inside AutoEdit's beta window (per `00_seed_accounts.md`, beta = March 2026).

#### Sources
- https://www.instagram.com/reel/DXlFWL5EkaN/ (yt-dlp direct pull, 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md`
- `research/03_virality_science.md` §2.1.2 (pattern interrupt), §2.2 (Social Currency)

---

### VIDEO 3 (TOP #3, 916K views): "claude can edit videos??"

#### 0. Identity & stats
- URL: instagram.com/reel/DWqP0Exk0iW/. Posted **2026-04-03** `[OBSERVED, yt-dlp upload_date; harvest
  file logged Apr 2 — 1-day discrepancy, likely timezone rounding between the two pull methods]`.
  Length: **24.13s** `[OBSERVED, identical to Videos 1–2]`.
- Views: **916K** `[OBSERVED, harvest]`. Likes: **14,535**. Comments: **11,909**
  `[OBSERVED, yt-dlp, HIGH]`. Like-rate 1.59%, comment-rate 1.30% — **this is the one top-5 video
  where likes exceed comments**, breaking the pattern seen in Videos 1, 2, and 5.
- Rank: #3 of 60; ~6.9x the median.
- **Cross-platform proxy confirmed**: this video's caption is word-for-word identical to YouTube
  Short `wNgVCxz7mgo` ("how to auto edit YouTube videos under 2 mins with Claude"), posted 2026-03-29
  (5 days earlier on YouTube), same 24s duration — a confirmed same-content cross-post, used per
  assignment instructions as a corroborating proxy. `[OBSERVED via yt-dlp on both URLs, 2026-07-25]`

#### 1. Packaging
- First-frame text: "claude can edit videos??" over a tight face close-up — Devin wearing over-ear
  headphones, mouth open, eyebrows raised in a shocked/surprised reaction expression, shot against a
  plain wall (a different, more "studio-lite" location than Videos 1–2) `[OBSERVED, frame sheet]`.

#### 2. Hook (0–3s)
- Hook taxonomy: **confronting question / bold-claim-as-question** (§3.1) — "claude can edit
  videos??" — combined with a **reaction-shot visual** (shocked face) rather than a POV/skit framing.
  This is the most "traditional creator-hook" of the top 5 — closest to a standard reaction-video
  opener rather than the stunt/skit style of Videos 1–2.
- What the viewer sees: a real human reacting with apparent genuine surprise, immediately legible
  even muted via the exaggerated facial expression.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED]`:
  - 0–3s: shocked reaction hook (2 near-identical frames, i.e., a held beat, not a quick cut) then
    cut to a Premiere Pro timeline (waveform audio-selection UI) with the same headphone-guy visible
    at a desk in an arch-windowed loft space (a location shared with Video 4, suggesting a shared
    shoot day — see §D).
  - 3–11s: "this claude plugin understands what your video is about..." over the Premiere timeline
    with green AI-selected segments and a MrBeast-labeled gaming clip visible in the source-preview
    pane; caption changes to "i don't think im ever editing again bro 😭" (the SAME escalation line
    used in Video 2, confirming this is a recurring, reusable stock reaction line across multiple
    posts — see §D).
  - 11–17s: AutoEdit UI on a phone/tablet — a home screen reading "Afternoon, Devin Huynh" with a
    chat-style AI assistant panel — cut to demo output clips labeled "CIGACHAD," "JELLYBEAN?," and a
    skateboarding "SKIBIDI RIZZ" caption example, captioned "it adds captions too*."
  - 17–24s: finger taps through a Premiere timeline ("it uses AI to cut out the actual bad takes")
    → final CTA "comment 'creator' if you want try this plugin" (the "creator"-keyword outlier — see
    §A.4; this IS the video whose YouTube cross-post independently confirms "creator" as the real,
    intended keyword for this specific video/mode).
- Open loop: the reaction-shock hook ("claude can edit videos??") is closed by the demo itself
  functioning as visual proof — the loop resolution IS the screen-recording, a clean and efficient
  design.
- Pacing: high, consistent with Videos 1–2, though the opening 2-frame held reaction beat is
  marginally slower than Videos 1–2's continuous motion opens.

#### 4. Value proposition
- Same tool-discovery proposition; slightly more emphasis on "understands what your video is about"
  (implying semantic/content understanding, not just silence-cutting) — a differentiation-from-
  competitors message (most editing tools only cut silence; this reads transcripts for meaning).
- Specificity: MED — shows a real AI-assistant chat panel, implying natural-language interaction with
  the tool, though no exact prompt text is legible in the frames sampled.

#### 5. Psychology scoring
- STEPPS: Practical Value dominant again; Social Currency present but weaker than Videos 1–2 (no
  income-flex line in this variant — this is the one top-5 video that skips the $-flex hook entirely).
- Primary emotion: awe/surprise, directly named in the hook itself ("??"), high-arousal-favorable.
- Save/send: MED-HIGH — the "understands what your video is about" claim is the kind of specific,
  differentiating detail a viewer might screenshot to send a fellow editor with "this is different
  from the other AI editors."

#### 6. CTA & funnel mechanics
- Confirmed "creator" keyword (in-video AND on the exact-match YouTube cross-post) vs "Claude" in the
  IG caption text — the clearest evidence in this sample that Devin/his team runs **multiple parallel
  keyword-tracked funnels** (at minimum CLAUDE and CREATOR observed; also EVENTS, AUTOEDIT, SUITE,
  TEXT, ANGLES, FABLE seen elsewhere in the YouTube catalog, §A.4), consistent with A/B-testing which
  keyword/mode drives better conversion, not a single static CTA.

#### 7. Replicability verdict
- Extractable template: reaction-shot-as-hook is the lowest-production-cost variant of the formula
  (no location scouting/stunt needed, just a genuine or performed surprised expression to camera) —
  arguably the MOST replicable of the 5 top videos for a creator without Devin's access to varied
  filming locations.
- Difficulty for Tangent: LOW — a reaction-to-a-genuinely-surprising-AI-capability hook is directly
  portable to a Claude-based creative-plugin brand with zero adaptation needed to the format itself.

#### 8. Why it won
- Most load-bearing factor: differentiation messaging ("understands what your video is about," not
  just cuts silence) paired with a classic, low-friction reaction hook — this is the most
  "textbook-correct" viral hook of the 5, and it performed respectably (916K) but is the LOWEST of
  the top 5, suggesting the compound/stunt hooks in Videos 1–2 (income flex + unusual setting) carry
  a genuine incremental lift over the plain reaction-hook format, even holding the underlying demo
  content constant.

#### Sources
- https://www.instagram.com/reel/DWqP0Exk0iW/ ; https://www.youtube.com/shorts/wNgVCxz7mgo (proxy,
  exact caption match, `[OBSERVED via yt-dlp]`, both 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md`

---

### VIDEO 4 (TOP #4, 860K views): "this AI claude plugin edits in under 2min by typing..."

#### 0. Identity & stats
- URL: instagram.com/reel/DXCWgz9k2Ag/. Posted **2026-04-12** `[OBSERVED, yt-dlp]`. Length: **24.13s**
  `[OBSERVED, identical to Videos 1–3]`.
- Views: **860K** `[OBSERVED, harvest]`. Likes: **14,161**. Comments: **11,309**
  `[OBSERVED, yt-dlp, HIGH]`. Like-rate 1.65%, comment-rate 1.31% — likes exceed comments here too,
  same pattern as Video 3, and this is its near-neighbor by both date (10 days after Video 3) and
  location (same arch-window loft, see §D).
- Rank: #4 of 60; ~6.5x median.

#### 1. Packaging
- First-frame text: "this AI claude plugin edits in under 2min by typing..." over a wide shot of
  Devin walking toward camera, pointing, in the same arched-window loft space as Video 3
  `[OBSERVED, frame sheet]` — confirming a shared shoot location/day across these two videos.

#### 2. Hook (0–3s)
- Hook taxonomy: **bold claim + demo-in-motion** — the "by typing..." clause is a genuine curiosity
  gap (typing WHAT? into WHERE?) that is distinct from Videos 1–3's framing and gets resolved later
  in the video.
- What the viewer sees: physical motion (a person walking/gesturing toward camera) rather than a
  static reaction or POV lie-down — the most kinetic opening of the top 5.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED]`:
  - 0–5s: walking/pointing hook, cuts directly into the Premiere timeline UI (same loft desk setup).
  - 5–11s: "and i still charged my client $800/hr for editing" (the income-flex device recurs a
    third time, now framed as hourly rate rather than monthly/per-project) → "claude understands what
    your video is actually about..." over the timeline, a green "BECAUSE" caption card visible
    mid-transition (kinetic-typography style filler word).
  - 11–17s: **this is the video that resolves the "by typing" hook** — shows the AutoEdit "Creator
    Mode" panel's free-text instructions field with real typed text: *"this is a youtube tutorial of
    me talking about an AI claude plugin that edits in premiere pro. I repeat myself a lot and mak[e
    mistakes]"* — i.e., the user types a plain-English description of their own footage/quirks, and
    the AI uses that as context. Captioned "you can type what your video is about 😏". This is the
    single most concrete, specific product-mechanic reveal across all 5 top videos.
  - 17–24s: AutoEdit "Select Takes" panel with real flagged-transcript bad-takes text ("So as I was
    saying, as a video editor you should... um. Wait no I messed up again.") → "it uses AI to cut out
    the actual bad takes of real footage" → CTA "comment 'claude' if you want try this plugin" (this
    one's on-screen keyword DOES match its IG caption — no discrepancy here, unlike Video 3).
- Open loop: the "by typing" curiosity gap opened at 0s is deliberately held until ~11s before being
  resolved with the free-text-instructions-field reveal — the clearest example of engineered mid-
  video loop-closure timing in the sample (§2.6.1).

#### 4. Value proposition
- Highest specificity of the top 5: an actual, readable, verbatim example of the custom-instructions
  text field is shown on-screen — a viewer could plausibly copy that exact framing pattern for their
  own use of the tool.
- Practical value class: tool discovery + a genuine sliver of copyable workflow (the instruction-
  writing pattern).

#### 5. Psychology scoring
- STEPPS: Practical Value strongest of the top 5 due to the concrete instructions-field reveal.
  Social Currency present via the $800/hr flex (a third distinct dollar-framing variant: project,
  monthly, hourly — see §D for the pattern across all income-flex hooks).
- Primary emotion: same amusement/mild-awe register as siblings; the "by typing" curiosity gap adds
  a small information-gap-driven engagement spike not present in Videos 1–2.

#### 6. CTA & funnel mechanics
- Keyword "claude" consistent between on-screen text and IG caption — no discrepancy (contrast
  Video 3).

#### 7. Replicability verdict
- Extractable template: opening with an unresolved "by doing X" clause and deliberately delaying the
  resolution of X until mid-video is a strong, directly reusable retention device, independent of the
  specific product.
- Difficulty for Tangent: LOW — this loop-structure device transfers directly to any tool demo.

#### 8. Why it won
- Most load-bearing factor: the deliberate hook/payoff separation (0s "by typing..." → 11s reveal)
  is the strongest pure retention-engineering example in the top 5, even though its raw performance
  (860K) sits below Videos 1–3 — suggesting hook novelty/stunt-value (Videos 1–2's settings) still
  out-competes pure structural craft (this video) for peak reach, though this video's higher
  specificity may correlate with the account's actual purchase-funnel quality even if raw views
  are lower (untestable without conversion data — `DATA GAP`).

#### Sources
- https://www.instagram.com/reel/DXCWgz9k2Ag/ (yt-dlp direct pull, 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md`
- `research/03_virality_science.md` §2.1.1, §2.6.1

---

### VIDEO 5 (TOP #5, 799K views): "I charge my clients $17.9K/mo for editing videos... and I didn't even edit them"

#### 0. Identity & stats
- URL: instagram.com/reel/DYm3hE9T75T/. Posted **2026-05-21** `[OBSERVED, yt-dlp]`. Length: **24.13s**
  `[OBSERVED, identical to Videos 1–4]`.
- Views: **799K** `[OBSERVED, harvest]`. Likes: **13,643**. Comments: **21,005**
  `[OBSERVED, yt-dlp, HIGH]`. Like-rate 1.71%, comment-rate 2.63% — comments again clearly exceed
  likes (the third of five top videos to show this inversion).
- Rank: #5 of 60; ~6.0x median. This is the most recent of the top 5 (18 days after Video 1, the
  next most recent), and sits after AutoEdit's public launch (May 2026).
- **Cross-platform proxy candidate**: YouTube Short `-ALAXEyt8JE` ("got tired so I let Claude AI edit
  for me while I slept 🛌") shares this reel's exact upload date (2026-05-21) and duration (24s), and
  its thematic content (asleep-in-bed framing) closely matches this reel's "im literally asleep bro"
  beat — a strong same-day proxy, though the title wording differs from the IG caption, so this is
  logged as a **probable same-shoot-day sibling/proxy, not a confirmed word-for-word cross-post**
  (unlike Video 3's confirmed match) `[OBSERVED via yt-dlp, dates/durations only — DATA GAP on exact
  identity]`.

#### 1. Packaging
- First-frame text: "I charge my clients $17.9K/mo for editing videos..." over Devin lying in bed
  facing away from camera, eyes apparently closed `[OBSERVED, frame sheet]` — a variant of Video 1's
  bed setting, now with an explicit "asleep" performance rather than just lying down.

#### 2. Hook (0–3s)
- Hook taxonomy: **bold income claim**, again — the fourth distinct dollar-figure variant across the
  top 5 ($5K/project, $26K/mo, [no flex], $800/hr, $17.9K/mo) — see §D for the pattern.
- What the viewer sees: a performed-asleep person, laptop still visible/active nearby, immediately
  setting up the "the AI is working even though I'm not" punchline.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED]`:
  - 0–5s: bed/asleep hook, "$17.9K/mo" flex.
  - 5–11s: "and I didn't even edit them 💀" (the punchline lands early here, faster than Videos 1–2's
    slower build) → "claude AI edited for me in under 2 mins" over the Premiere timeline (waveform +
    AutoEdit panel visible) → "im literally asleep bro 😭" (a second escalation line, distinct from
    but structurally parallel to Video 2/3's "i don't think im ever editing again bro").
  - 11–17s: a **notable departure from Videos 1–4's structure** — cuts to a different, unidentified
    young woman speaking directly to camera in what appears to be a hotel room, saying (via on-screen
    text) "this is a custom Caption effect..." and "you can make CAPTIONS just like this," followed by
    a phone screen showing an app labeled "AutoEdit / Creator Pro / Premium" with tabs for "Creator
    Mode," "Captions," "Templates," "AI Motion Graphics" and a credits meter ("AI Processing Credits
    247/500 min"). `[OBSERVED, frame sheet]` — **this segment's provenance is ambiguous**: it could be
    (a) a teammate/co-founder demo cut (AutoEdit's Product Hunt maker list includes Priyanka Mandal,
    a second team member, per §A.3), or (b) licensed/repurposed third-party marketing footage for a
    mobile companion app. `[INFERRED — flagged as unresolved, not asserted either way]`.
  - 17–24s: back to Devin, "it cuts out all the bad takes & repeats" over Fortnite gaming-footage
    processing, "this is literally perfect for content creation" → final CTA "comment 'claude' to try
    the plugin for free."
- This is the only top-5 video to feature a second on-camera presenter, and the only one to show a
  distinct **mobile-app UI** (Creator Pro) rather than exclusively the desktop Premiere Pro plugin —
  evidence the product surface expanded beyond the original desktop plugin by May 2026.

#### 4. Value proposition
- Same core proposition, broadened this time to imply a mobile/companion-app surface in addition to
  the Premiere Pro desktop plugin — signals product-line expansion.

#### 5. Psychology scoring
- STEPPS: Social Currency (largest flex figure of the sample, $17.9K/mo) + Practical Value. The
  "didn't even edit them" punchline compresses the value prop into a single, highly quotable line.
- Primary emotion: amusement, same register as siblings.
- Save/send: the second-presenter segment (if genuinely a different, relatable creator persona) may
  broaden the addressable audience for sends beyond "people who know Devin specifically."

#### 6. CTA & funnel mechanics
- "Claude" keyword, consistent with the caption — no discrepancy.

#### 7. Replicability verdict
- Extractable template: the "asleep while the AI works" framing is a strong, minimal-effort variant
  of the passive-flex hook, and the fast punchline placement (5s, not 8–9s as in Video 2) suggests
  faster payoff delivery may be part of what's being iterated toward over time (this is the most
  recent of the top 5).
- Difficulty for Tangent: LOW for the hook device; the multi-presenter segment is MED difficulty
  (requires a second on-camera collaborator).

#### 8. Why it won
- Most load-bearing factor: the fastest punchline-to-hook gap of the sample (~5s) combined with the
  largest single dollar-figure flex, landing right after AutoEdit's public launch — likely benefiting
  from genuine product-news relevance in addition to the format's now-proven track record (this is
  the 5th deployment of a near-identical structure and still cleared 799K, evidence the format was
  not yet fatigued by repetition — see §C/§D).

#### Sources
- https://www.instagram.com/reel/DYm3hE9T75T/ (yt-dlp direct pull, 2026-07-25)
- https://www.youtube.com/shorts/-ALAXEyt8JE (probable proxy, date/duration match only)
- `research/ig_harvest/elevenpercentprod.md`
- `research/00_seed_accounts.md` (AutoEdit public launch = May 2026)

---

### VIDEO 6 (FLOP #1, 2,528 views): "comment 'ANGLES' for the link"

#### 0. Identity & stats
- URL: instagram.com/reel/DURH42UkjE7/. Posted **2026-02-02** `[OBSERVED, yt-dlp]`. Length: **48.42s**
  `[OBSERVED, ffprobe]` — roughly **2x the top-5 videos' 24.13s**, the first structural difference
  found between winners and this flop.
- Views: **2,528** `[OBSERVED, harvest]`. Likes: **3**. Comments: **9** `[OBSERVED, yt-dlp, HIGH —
  this is an exact count, not rounded]`. Like-rate **0.12%**, comment-rate **0.36%** — roughly
  **13–18x lower** than the top 5's like-rates, and this is BEFORE accounting for the much smaller
  view base.
- Rank: #59 of 60 (second-lowest in the grid). ~53x below the account's 133K median.

#### 1. Packaging
- **Critical finding**: this video's content is **not Devin's own product demo at all**. Frame-sheet
  inspection shows a completely different presenter (a young man, not Devin) talking about
  "Higgsfield['s] Angles 2.0" — a third-party AI camera-angle-generation tool — demonstrated on
  Taylor Swift Grammy-awards footage and a Dwayne Johnson clip, with on-screen captions like "change
  the Angle? after you shot it," "generate 12 different angled full video with content accurate to,"
  "3D cube," "generates," "hallucinations." `[OBSERVED, frame sheet]` The IG caption (confirmed via
  yt-dlp) is simply "comment 'ANGLES' for the link ✨" with no further text.
- This is a **repost/curation of someone else's video** (or a very close re-edit of another creator's
  Higgsfield-tool demo) republished under elevenpercentprod's own account with Devin's own
  comment-keyword CTA appended — he does not appear on camera in this video at all in the sampled
  frames.

#### 2. Hook (0–3s)
- First frame is mid-scene (a face close-up, no text yet) — text ("change the Angle?") does not
  appear until frame 2, a slower text-reveal than any top-5 video (all of which had full hook text in
  frame 1).
- Hook taxonomy: bold-claim-adjacent ("change the angle after you shot it"), but delivered by an
  unfamiliar face with no established parasocial connection to this account's audience.

#### 3. Structure & retention engineering
- Beat map: a fairly dense, well-produced kinetic-typography breakdown of the Higgsfield Angles 2.0
  tool (before/after examples, a 3D-cube angle-picker UI, Taylor Swift/Dwayne Johnson demo footage) —
  production quality is arguably HIGHER than Devin's own top-5 videos (more graphic design, tighter
  word-by-word caption timing) `[OBSERVED, frame sheet]`.
- Despite the higher production polish, pacing/structure quality is not the differentiator here (see
  §8) — this flopped despite being well-made by conventional standards.
- Length (48s) is double the winning format's 24s — violates the "one idea, tight runtime" discipline
  relative to the proven top-5 template.

#### 4. Value proposition
- Tool discovery for a DIFFERENT product (Higgsfield Angles), not AutoEdit — meaning this post does
  not build AutoEdit brand/product recognition at all, unlike every one of the top 5.
- Specificity: actually HIGH (shows a real UI, real before/after demo) — value prop clarity is not
  the failure mode here.

#### 5. Psychology scoring
- STEPPS: Practical Value and mild awe are present in the content itself, but **Devin himself is
  entirely absent** — no parasocial continuity with his established audience (§2.4.1), and no
  personal stake/authenticity signal ("I built this" vs. "someone else built this, comment for a
  link").
- This is the single clearest psychology-level explanation available in this sample: the top 5 all
  put Devin's own face/voice/persona in the first 3 seconds; this flop does not feature him until
  possibly much later (not observed in the sampled frames at all).

#### 6. CTA & funnel mechanics
- Same "comment KEYWORD for link" mechanic as the winners (comment "ANGLES") — proving the CTA
  mechanic alone is not sufficient for performance; it requires the surrounding content/persona
  package the top 5 have and this video lacks.
- Unclear what product/affiliate relationship, if any, connects Devin to Higgsfield — `DATA GAP`,
  not researched further as out of scope (this is not his product).

#### 7. Replicability verdict
- Extractable (negative) lesson: reposting/curating a well-made third-party tool demo with your own
  comment-CTA bolted on, without your own on-camera presence, does NOT reliably transfer performance
  — even when the source content and production quality are good.
- Difficulty/lesson for Tangent: this is a clear anti-pattern to avoid — don't rely on curated
  third-party content with a bolted-on CTA as a growth strategy; own-voice/own-product content in the
  same account's top 5 outperforms this by 300–1000x.

#### 8. Why it lost
- Most load-bearing factor: **no Devin on camera, no AutoEdit branding, no established persona
  continuity** — this reads as an off-brand, low-authenticity post relative to the account's winning
  formula, despite comparable-or-better production polish and an identical CTA mechanic.
- Secondary factor: posted **2026-02-02**, before the AutoEdit beta (March 2026) — i.e., before this
  account had ANY product of its own to consistently push, which is itself informative: the entire
  top-5 cluster only exists AFTER Devin had his own product and his own on-camera format to attach it
  to (see §C for the full before/after contrast).
- Delta vs. top 5: length (2x longer), presenter (absent vs. present), brand (third-party vs. own
  product), timing (pre-launch vs. launch-window) — every major variable that differs, differs in the
  direction that favors the winners.

#### Sources
- https://www.instagram.com/reel/DURH42UkjE7/ (yt-dlp direct pull, 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md`

---

### VIDEO 7 (FLOP #2, 3,285 views): "how to edit EVENT videos" / Event Recap Mode preorder pitch

#### 0. Identity & stats
- URL: instagram.com/reel/DUEFiGlAYW4/. Posted **2026-01-28** `[OBSERVED, yt-dlp]`. Length: **67.19s**
  `[OBSERVED, ffprobe]` — **~2.8x the top-5 videos' 24.13s**, the longest video in this dossier's
  sample by a wide margin.
- Views: **3,285** `[OBSERVED, harvest]`. Likes: **3**. Comments: **51** `[OBSERVED, yt-dlp, HIGH]`.
  Like-rate **0.09%** (the lowest in the sample), comment-rate **1.55%** (still exceeds likes 17x —
  the comment-exceeds-likes inversion pattern from the top 5 is present even in this flop, suggesting
  the comment-keyword mechanic drives disproportionate comments regardless of overall reach).
- Rank: #58 of 60. ~40x below the median.

#### 1. Packaging
- First-frame text: "how to edit EVENT VIDEOS" in bold yellow kinetic type, over Devin holding a
  camera at an event (a festival/crowd setting), Premiere Pro icon badge visible `[OBSERVED, frame
  sheet]`.
- This IS Devin on camera, at his actual past videography work — a more "credentialing"-oriented
  packaging (establishing expertise) than the top 5's "look at this trick" packaging.

#### 2. Hook (0–3s)
- Hook taxonomy: **informational/how-to framing** ("how to edit event videos") rather than a bold
  claim, reaction, or POV skit — the weakest hook taxonomy of the full 7-video sample per §3.1's
  categories (closest to the generic "so today I want to talk about..." pattern §3.2 flags as the
  anti-pattern to avoid).
- Second frame: "Best AI Plugin." — a claim, but delivered flatly, without the shock/absurdity/flex
  devices used throughout the winning top 5.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED]`: an extended founder-story/credentialing section — "6 years [as a]
  videographer," "speed is everything," on-camera direct-address explaining his own past pain point
  as an event videographer (getting out-competed by faster editors) — followed by a straightforward,
  undramatized feature list: "AI Plugin / Pr / making this," "edits event recap," "AutoEdit™ / Music /
  B-Roll / Performance / upload your raw [footage]," "Cuts on beat," "'Best Quotes' w/ Interviews,"
  Rolling Loud/festival b-roll, timeline screenshots, "It even comes with transitions, cards," and
  finally, ~50s in, "guys, cause... ahead of 90%... Like... your clients keep hiring... Right now
  we're... March 2026 available... pre-order and comment 'EVENTS'... pre-order link."
- This is a **direct pitch/infomercial structure** (credential → problem → solution → feature list →
  pricing/availability → CTA) — the classic long-form sales-page structure compressed into a Reel,
  NOT the hook→drip-reveal→CTA structure the top 5 use.
- Pacing: static talking-head segments run noticeably longer between cuts than any top-5 video
  (visually confirmed — several consecutive sampled frames at 0.5fps show no scene change, meaning
  multiple real seconds of unchanging shot, versus the top 5's near-continuous 1–2s cut rate).
- One-idea discipline: **violated** — this video tries to cover founder credibility, the problem, the
  full feature set (cuts on beat, best-quotes detection, transitions, cards), AND pricing/availability
  in one 67s video, versus the top 5's single-minded "AI edits fast" message.

#### 4. Value proposition
- Highest RAW information density of the 7-video sample (most named features: beat-sync cutting,
  best-quote/interview detection, auto-transitions, title cards) — but density without the drip-
  pacing structure that makes information digestible in short-form (§3.2's "one idea per video" is
  explicitly about avoiding exactly this failure mode).
- Specificity: HIGH in content terms, but buried in a slower/denser delivery.

#### 5. Psychology scoring
- STEPPS: Practical Value present but delivered as an announcement/pitch rather than a demonstrated-
  in-action proof; the founder-story segment does carry some authenticity/parasocial value (§2.4.1)
  but at the cost of runtime that could otherwise be spent on the actual product demo.
- Primary emotion: low arousal — informational/explanatory register, closer to the "calm-useful"
  category §2.3 flags as share-unfavorable relative to amusement/awe/anger.
- This is the clearest §2.3 (arousal) violation in the sample: every top-5 video targets amusement or
  awe; this flop targets calm, explanatory informativeness — precisely the emotional register Berger
  & Milkman's research found under-performs for virality.

#### 6. CTA & funnel mechanics
- CTA: "comment 'EVENTS' and I'll send you the link... pre-order link" — same mechanic, but delivered
  after 50+ seconds of setup, versus the top 5's CTA landing at the very end of a tight 24s (i.e., the
  CTA-to-total-runtime ratio is far worse here).
- Pricing disclosed directly in-video ("$49.99... discounted 1-time preorder... beta testing opens in
  1 week") `[OBSERVED via full caption text, yt-dlp]` — none of the top 5 disclose exact pricing
  on-screen or in-caption, always deferring price discovery to the link/DM. This is a meaningful
  funnel-design difference: winners create curiosity and defer price; this flop discloses price
  upfront, which may itself reduce the "what's behind the link" curiosity gap (§2.1.1) that makes the
  comment-CTA compelling in the winners.

#### 7. Replicability verdict
- Extractable (negative) lesson: don't front-load founder-story/credentialing before the demo; don't
  cram the full feature list into one video; don't disclose price in a format designed to run on
  curiosity-gap CTA mechanics.
- Difficulty/lesson for Tangent: this is the clearest evidence in the whole dossier that **format
  discipline, not topic or product quality, is the swing factor** — this pitches a real, credible
  product (Event Recap Mode, a real AutoEdit SKU) with real founder credibility, and still flopped,
  because the packaging violated nearly every structural principle the winning format follows.

#### 8. Why it lost
- Most load-bearing factor: **runtime/pacing mismatch with the short-form medium** — a 67s
  infomercial-structured pitch, front-loaded with credentialing and back-loaded with price disclosure,
  directly violates the "hook→drip-reveal→CTA in under 25s" template that all 5 winners follow.
- Secondary factor: posted **2026-01-28**, the earliest video in this dossier's entire sample — before
  Devin had settled on ANY of the winning format's devices (income-flex hook, screen-recording drip
  reveal, multi-genre demo montage). This flop and Video 6 (Feb 2) together bracket the **pre-formula
  era**; the top 5 (Apr–May) are uniformly **post-formula**. This before/after contrast is the
  single cleanest piece of evidence in the whole dossier that the winning format was **deliberately
  engineered and iterated into existence**, not a lucky one-off (see §C, §D).

#### Sources
- https://www.instagram.com/reel/DUEFiGlAYW4/ (yt-dlp direct pull, full caption + exact like/comment
  counts, 2026-07-25)
- `research/ig_harvest/elevenpercentprod.md`
- `research/03_virality_science.md` §2.3, §3.2

---

## C. The non-follower-reach decomposition (centerpiece)

**Central question: how does an 85K-follower account get a 133K median reel views (156% of its own
follower count) — the highest ratio in this 24-account study?** Decomposed by the 4 factors named in
the assignment brief:

### C.1 The demo format (before/after editing transformations)

The top 5 do NOT use a literal "before/after" split-screen edit-comparison format (unlike, e.g., the
Higgsfield "Angles 2.0" flop's before/AFTER labels, or classic transformation-reveal content). Instead
the format is a **live-process demo**: the viewer watches the actual product UI perform the task in
real time (Select Takes → flags bad takes with real transcript text → Captions panel → Generate Rough
Cut), narrated entirely through burned-in caption call-outs, not voiceover. This is closer to a
**"demo-in-motion" hook (§3.1)** sustained for the full runtime than a single before/after reveal. The
credibility payload comes from the UI being visibly real and specific (real flagged "bad take"
transcript lines, real font-styling sliders) rather than a polished marketing render — `[OBSERVED
across Videos 1–5]`.

### C.2 The comment-keyword funnel as ranking fuel

This is the most quantifiable lever found. Across the top 5 videos:

| Video | Views | Likes | Comments | Like-rate | Comment-rate | Comments > Likes? |
|---|---|---|---|---|---|---|
| DX-bJErPxe7 (2.5M) | 2.5M | 53,167 | 61,429 | 2.13% | 2.46% | **YES** |
| DXlFWL5EkaN (2.1M) | 2.1M | 26,429 | 47,699 | 1.26% | 2.27% | **YES** |
| DWqP0Exk0iW (916K) | 916K | 14,535 | 11,909 | 1.59% | 1.30% | no |
| DXCWgz9k2Ag (860K) | 860K | 14,161 | 11,309 | 1.65% | 1.31% | no |
| DYm3hE9T75T (799K) | 799K | 13,643 | 21,005 | 1.71% | 2.63% | **YES** |
| **Flop** DURH42UkjE7 | 2,528 | 3 | 9 | 0.12% | 0.36% | YES (tiny N) |
| **Flop** DUEFiGlAYW4 | 3,285 | 3 | 51 | 0.09% | 1.55% | YES (tiny N) |

`[OBSERVED, all figures via direct yt-dlp pull against live Instagram URLs, 2026-07-25]`. Three of
five top videos, and both flops, show **comments exceeding likes** — the inverse of typical social-
video engagement, where likes normally outnumber comments 5–20x. This is the direct fingerprint of
the "comment KEYWORD for the link" mechanic converting viewer attention specifically into comments.
Per `03_virality_science.md` §1.1.1/§1.1.2, Instagram's own stated ranking signals emphasize "likelihood
to reshare" and (per convergent secondary reporting) weight sends/shares and — plausibly, though not
officially confirmed as comments specifically — engagement volume broadly, more heavily than passive
likes for reaching non-follower/Explore audiences. The mechanic is engineered to maximize exactly the
metric (comment volume, and presumably downstream DM/sends) the algorithm is most reported to reward
for cold-audience distribution. **Important tension, addressed honestly**: §1.3.2 of the same
document names bare "comment X" prompts as Instagram's own named example of prohibited engagement
bait. The distinguishing test given there — "does the video have standalone value without the bait"
— is met here: every top-5 video delivers a real, specific, credible product demo independent of the
CTA (§B). The flops (Video 6, no Devin/no product; Video 7, real content but badly paced) show the
CTA mechanic ALONE is insufficient — it is necessary but not sufficient, and only pays off when paired
with credible standalone demo content.

### C.3 Topic white space

Instagram's short-form AI-tool-demo space is dominated by generic "AI tools you need to try" listicle
content (observed pattern across most other accounts in the wider 24-account corpus per `00_INDEX.md`
— e.g. godofprompt, tech.unicorn, ai_ankitarora). **"Claude specifically editing video specifically
inside Adobe Premiere Pro"** is a narrow, concrete, verifiable claim rather than a vague "AI is
amazing" gesture — it satisfies Loewenstein's curiosity-gap requirement for *partial, specific*
information (§2.1.1: too little context creates confusion, not curiosity; this format supplies just
enough specific context — "Claude," "Premiere Pro," "2 minutes" — to create a sharp, resolvable gap).
This is `[INFERRED]`: no direct competitor-density study was run, but zero other accounts in the full
24-account corpus (per `00_INDEX.md`) are observed running a comparable "AI edits video inside a named
NLE" demo format, making this a plausible, if not directly measured, white-space claim.

### C.4 Production

Production is **deliberately low-fi/authentic** (bedroom, bathroom, informal loft), NOT polished —
this is a strategic choice, not a resource constraint (the same account also produces high-polish
kinetic-typography content, visible in Video 7 and the YouTube catalog's pre-pivot tutorials). The
production investment is concentrated in **post-production density** (a cut/UI-change roughly every
1–2s, captions on every frame) rather than **pre-production polish** (lighting, sets, wardrobe) —
consistent with §3.3.2's pacing principle and §1.2.3's point that packaging/production polish matters
less than in-video hook/pacing for feed-native short-form.

### C.5 Cross-platform reach comparison (the platform-specific multiplier)

The same content, posted to three platforms, performs at wildly different absolute scale:

| Platform | Same/proxy content | Views | Source |
|---|---|---|---|
| Instagram | DWqP0Exk0iW | **916,000** | `ig_harvest`, `[OBSERVED]` |
| YouTube Shorts | `wNgVCxz7mgo` (confirmed exact-caption cross-post) | **843** | yt-dlp, `[OBSERVED]` 2026-07-25 |
| Instagram | DYm3hE9T75T | **799,000** | `ig_harvest`, `[OBSERVED]` |
| YouTube Shorts | `-ALAXEyt8JE` (same-date probable proxy) | **1,439** | yt-dlp, `[OBSERVED]` 2026-07-25 |
| TikTok | 15 most-recent samples, same format | **151–1,859** (median ~700) | yt-dlp flat-playlist, `[OBSERVED]` 2026-07-25 |

**This is a >1,000x gap between Instagram and YouTube/TikTok for the identical or near-identical
underlying content.** This decisively rules out "the content/format is just universally excellent" as
the sole explanation — the SAME format, SAME hook, SAME product demo, SAME CTA mechanic performs
2–3 orders of magnitude worse off-Instagram. The reach outlier is **platform-specific**, not
content-universal: something about Instagram's Reels algorithm, this account's specific history on
Instagram, or Instagram's audience composition for this topic is doing most of the work that a
"content quality" story alone cannot explain. `[OBSERVED comparison; the underlying causal "why
Instagram specifically" is INFERRED — most likely some combination of Instagram Reels' documented
audio/Explore-surface mechanics (§1.1.1) and this creator having built his specific audience/posting
history on Instagram first, but this dossier cannot fully isolate the cause from the available data]`.

### C.6 Ad-boost check (answering assignment Q3 directly)

Per `00_INDEX.md`'s documented ad-boost signature (near-zero like-rates, 0.003%–0.4%, paired with
massively inflated views, observed on tiffintech's and networkchuck's #ad posts), **this account's
top 5 show like-rates of 1.26%–2.13%** — squarely within the 1–10% organic norm `00_INDEX.md` uses as
the baseline, nowhere close to the ad-boost signature. **Verdict: the Apr–May 2026 top-5 cluster shows
no evidence of paid boosting; it reads as organic**, and its timing lines up precisely with AutoEdit's
own real product milestones (beta = March 2026, Videos 3–4 in the beta window; public launch = May
2026, Videos 1 and 5 in/after the launch window) — i.e., this is a genuine, deliberate **organic
content push timed to a real product launch**, not luck and not paid media. `[OBSERVED via like-rate
calculation, cross-referenced against 00_INDEX.md's independently-derived ad-boost benchmark]`

---

## D. Content architecture: key vs. filler, cadence, and how a tiny catalog sustains reach

### D.1 The catalog is not diverse — it is one message, dozens of surface variants

A 200-item flat-playlist sweep of `@elevenpercent/shorts` (YouTube) found **180/200 (90%) titles
directly reference Claude, AutoEdit, Premiere Pro, or "plugin"/"edit"** `[OBSERVED, yt-dlp, 2026-07-25]`.
The remaining ~20 (the oldest in the sweep) are pre-pivot generic editing tutorials (Frutiger Metro
overlay tutorials, camera-shake VFX tricks, title-card design, productivity tips) — confirming the
account pivoted almost its entire output to a single message once AutoEdit existed.

Within that 180, this dossier counted **at least 7 distinct tracked keywords** (CLAUDE, CREATOR,
AUTOEDIT, EVENTS, SUITE, TEXT, ANGLES, FABLE) rotating across near-duplicate videos — this is not
"diverse content pillars sustaining reach" but rather **one core claim, systematically A/B-tested**
across hook variant, filming location, and CTA-keyword, at high volume.

### D.2 The recurring "income-flex" hook device, quantified

Across just the 5 top videos in this sample, the income-flex hook appears in 4 of 5, with 4 distinct,
escalating dollar-framings: **$5K/project** (Video 1) → **$26K/mo** (Video 2) → **$800/hr** (Video 4)
→ **$17.9K/mo** (Video 5). This is a single reusable hook *template* ("I charge clients $X for editing
… and [Claude/I] did it in under 2 min instead") with the dollar amount and time-unit as the only
varied inputs — a low-cost, high-leverage content-production pattern: one script skeleton, minimal
new footage required beyond a new opening line and setting.

### D.3 Recurring stock reaction lines

Two escalation captions — **"i don't think im ever editing again bro 😭"** (Videos 2 and 3) and its
structural sibling **"im literally asleep bro 😭"** (Video 5) — recur verbatim or near-verbatim across
multiple videos `[OBSERVED, frame sheets]`, further confirming a reusable line-bank rather than
bespoke scripting per video.

### D.4 Fixed-duration templating

All 5 top videos measured **exactly 24.13 seconds** (`[OBSERVED, ffprobe, identical to 6 decimal
places]`) — near-certain evidence of a fixed edit-template/timeline duration reused across the entire
winning series, into which different cold-opens and B-roll are dropped. The two flops ran 48.4s and
67.2s respectively — 2–2.8x longer, outside the template.

### D.5 Reused B-roll/demo footage across posts

The same underlying screen-recordings recur across multiple videos: the "Select Takes" panel with the
identical flagged bad-take transcript line ("So as I was saying, as a video editor you should... um.
Wait no I messed up again.") appears in BOTH Video 1 and Video 4; the same arch-window loft location
and desk setup appears in BOTH Video 3 and Video 4 (10 days apart); the same Fortnite gaming-footage
demo clip appears in BOTH Video 1 and Video 5. This is a **small, reusable footage library** (one or
two demo-recording sessions) repackaged behind many different cold-opens — the actual novel
production cost per video is concentrated almost entirely in the first ~5 seconds (a new hook/setting),
with the remaining ~19s substantially recycled.

### D.6 How this sustains >100% non-follower reach with a tiny effective catalog

Per Instagram's documented "audition" model (`03_virality_science.md` §1.1.3), each new post is
tested against a fresh cold audience regardless of the account's posting history. Because the
underlying claim ("Claude edits your video") is inherently novel/curiosity-triggering to any viewer
encountering it for the first time, and because Devin varies the **hook** (setting, dollar-figure,
question framing) while reusing the **payoff** (the same demo footage), each new post can win a fresh
audition on hook novelty alone even though the substance is highly repetitive. The flat, consistently
elevated like-rate across all 5 top videos (1.26%–2.13%, a narrow band) despite this being roughly
the 4th–7th deployment of the same underlying formula (by the account's own chronology) is direct
evidence the format was **not yet fatigued** as of this July 2026 harvest — repetition of the payoff
has not visibly degraded performance, so long as the hook keeps varying.

### D.7 Cadence

Precise posting cadence for elevenpercentprod specifically is a `DATA GAP` (Instagram does not expose
a clean date-indexed feed via the harvest method used), but the YouTube catalog (a near-mirror
content stream, cross-posted per §A.5) shows the AutoEdit-era content occupying the most recent
~180 of ~592 total channel videos, i.e., a clear step-change to much higher-frequency, single-topic
output coinciding with the pivot — consistent with (though not proof of) a near-daily or
multiple-times-weekly cadence during the Apr–July 2026 window, `[INFERRED]` from catalog density, not
directly measured by post-date.

---

## E. Method log (per QC Protocol §7)

**What was read (mandatory, in order):**
1. `research/QC_PROTOCOL.md` — evidence-tier rules, template compliance, both-tails requirement.
2. `research/templates/video_postmortem_template.md` — the exact 9-section structure applied to all
   7 videos above.
3. `research/03_virality_science.md` — cited throughout, tags (RESEARCH-BACKED / INDUSTRY DATA /
   PRACTITIONER LORE / UNVERIFIED) respected; no UNVERIFIED-STAT figures used as fact anywhere above.
4. `research/ig_harvest/elevenpercentprod.md` (primary data, per assignment) — grid, computed stats,
   7 detail pulls — used as the view-count source throughout (Instagram hides view_count from
   yt-dlp's extractor for this creator; the harvest's browser-based grid scrape is the only view-count
   source available).
5. `research/ig_harvest/00_INDEX.md` — cross-account context, the ad-boost like-rate benchmark used
   in §C.6, and the ranking table confirming this account's 156% ratio is the study's highest.
6. `research/00_seed_accounts.md` §3 (Devin Huynh) — origin story, AutoEdit timeline (beta March 2026,
   public launch May 2026, Product Hunt June 14–15 2026), makers, prior follower/subscriber figures
   (carried forward, not re-verified, and cited as such throughout).

**Tools used (this dossier's own verification layer, beyond the primary harvest):**
- `yt-dlp` direct pulls against all 7 live Instagram reel URLs — `info.json` (exact like/comment
  counts, full captions, precise duration, upload timestamp) for every video, PLUS full video
  download for all 7.
- `ffmpeg` 1fps (top 5) / 0.5fps (2 flops, longer runtime) frame extraction, tiled into contact-sheet
  images per video, visually inspected via the Read tool — this is the primary evidentiary basis for
  all Hook/Structure/Production sections above, since Instagram reels in this sample carry no spoken
  narration to transcribe.
- `yt-dlp --write-auto-subs` attempted on 3 YouTube proxy candidates (`wNgVCxz7mgo`, `-ALAXEyt8JE`,
  `Xp3aUNp30gU`) — **failed to produce useful transcripts**: the auto-captions transcribed background
  trending-song lyrics ("Chanel, Chanel..." / "Formula... on the Monday too...") rather than any
  narration, confirming these are music-scored, caption-overlay videos with no spoken dialogue —
  logged as a `DATA GAP` per protocol §3 rather than silently dropped.
- `yt-dlp --flat-playlist` sweep of `@elevenpercent/shorts` (200 items) and `@elevenpercentprod`
  TikTok profile (15 items) — used for the cross-platform reach comparison (§C.5) and the content-
  architecture catalog analysis (§D.1).
- WebSearch + WebFetch: Product Hunt page (`producthunt.com/products/autoedit` — direct fetch,
  confirmed #3/329 upvotes/3 makers), `elevenpercent.net/pages/autoedit-creator` (preorder pricing),
  `elevenpercent.net/pages/affiliate` (commission tiers), `autoeditai.net` (current live subscription
  pricing/free-trial), and a general search for ManyChat/DM-automation confirmation specific to this
  account (returned no first-party confirmation — logged as `DATA GAP`, §A.4).
- `claude-in-chrome` browser tools were **not used**, per explicit instruction (reserved).

**What failed / data gaps (honest accounting):**
- TikTok follower count: not extractable via `yt-dlp --flat-playlist` (no `channel_follower_count`
  field populated for this extractor/profile) — logged as `DATA GAP`, consistent with
  `00_seed_accounts.md`'s prior finding of the same gap.
- Exact DM-delivery mechanism (ManyChat or otherwise) for the "comment KEYWORD" funnel: not confirmed
  on any first-party page. Logged honestly as `DATA GAP` rather than assumed — the dossier states the
  industry-standard mechanism and cites `03_virality_science.md` §3.4.3 for what that mechanism
  generically does, without claiming Devin specifically uses ManyChat.
- Video 5's second on-camera presenter and the "Creator Pro" mobile-app UI segment: provenance
  (teammate vs. licensed footage) could not be confirmed — flagged `[INFERRED]`/unresolved rather than
  asserted.
- Exact IG posting cadence: not date-indexed in the available harvest method — cadence claims in §D.7
  are `[INFERRED]` from the YouTube catalog's relative density, not directly measured on Instagram.
- Minor cross-source date discrepancies (1 day, e.g. Video 3's Apr 2 vs Apr 3) between the original
  harvest pull and this dossier's independent yt-dlp pull — most likely timezone-boundary rounding
  between two different pull methods on different dates; noted inline where relevant, not treated as
  a material conflict.

---

## Summary (for the requesting agent / final synthesis)

**Reach decomposition verdict:** The 156% median-to-follower ratio is explainable by a **stacked,
engineered system**, not a single trick: (1) a fixed, ~24-second templated demo format showing real
product UI in motion, (2) a comment-keyword CTA that measurably converts attention into comments at a
rate that inverts the normal likes>comments pattern (confirmed via exact yt-dlp counts — comments
exceeded likes on 3 of 5 top videos), feeding whatever engagement/reshare-adjacent signals Instagram's
Reels ranking weights most for cold/Explore audiences, (3) genuine topic white space (no other account
in the 24-account corpus runs a comparable "named-AI-inside-named-NLE" demo format), and (4) low-fi,
high-cut-density production that reads as authentic rather than promotional. Crucially, this dossier's
own like-rate check (1.26%–2.13% across the top 5, versus a documented 0.003%–0.4% ad-boost signature
elsewhere in the study) rules out paid boosting — this is organic, and its Apr–May 2026 timing lines
up precisely with AutoEdit's real beta/launch milestones, i.e., a genuine, well-timed organic push, not
luck.

**Funnel mechanics:** Comment a keyword (CLAUDE/CREATOR/EVENTS/AUTOEDIT/SUITE/TEXT/ANGLES, at least 7
observed, rotating and apparently A/B-tested) → presumed automated DM (ManyChat-class tool; **not
first-party confirmed** — logged as a data gap, not fabricated) → link to either a one-time preorder
page (Apr–May 2026 captions) or, currently, a live subscription product at autoeditai.net with a real
free trial. This is a **single-hop, direct-to-product funnel** — no content-nurture layer between the
reel and the sale, unlike some other creators in the corpus.

**Formula bullets (top-5-derived, directly replicable):**
- Fixed short runtime (~24s), reused across every winning post — build one edit template, drop in
  new footage.
- Hook = a specific, escalating dollar-figure status flex OR a genuinely surprised reaction shot,
  landing complete in frame 1, no build-up.
- Payoff = real, credible screen-recording of the actual product doing the actual task, drip-revealed
  with a new caption call-out every 1–2 seconds.
- Show the tool working across at least 2 visibly different content genres in the same video to widen
  the addressable "send this to..." audience.
- Close on a comment-keyword CTA — but only after the video has already delivered standalone value
  (this is what separates the winners from the flops, both of which used the identical CTA mechanic
  and still failed).
- Vary the hook aggressively across posts; reuse the payoff footage aggressively. Novel cold-opens
  keep re-auditioning well even when the underlying demo is substantially recycled.

**What a Claude-based creative-plugin brand can copy directly:** the entire top-5 formula transfers
with near-zero adaptation, since it is itself a Claude-powered creative tool being demoed for a
creator-tool audience — the single highest-leverage move visible in this dossier is **do not describe
the tool in the abstract; screen-record it doing the real task on real (or realistic) content**, and
attach that demo to a fast, specific, escalating hook rather than an explainer/credentialing preamble
(Video 7's flop is the clearest cautionary tale on this point).

**Surprises:**
- The account is not a solo creator — AutoEdit has a 3-person maker team (Product Hunt credits),
  complicating any narrative of this as a single person's organic hustle.
- Comments exceeding likes on the biggest hits is a striking, directly measurable fingerprint of the
  CTA mechanic that the rounded harvest-file figures alone would not have surfaced — only visible via
  this dossier's exact-count re-pull.
- The product itself visibly changed business model mid-study (one-time preorder → live subscription
  SaaS with free trial) between the April captions and the current live site — the captions' "free"
  language tracks the product's real state at time of posting rather than being static/misleading.
- Instagram's reach advantage over YouTube/TikTok for the identical content is not a small edge — it
  is a >1,000x gap on a confirmed exact-match cross-post, meaning platform choice/history is doing
  enormous, probably underappreciated, work independent of content quality.
- One of the two flops isn't even Devin's own content — it's a repost of a competitor/adjacent tool
  (Higgsfield Angles 2.0) with his CTA bolted on, and it performed 300–1000x worse than his own
  product content despite comparable-or-higher production polish — direct evidence that owned-product
  authenticity, not just format mechanics, is load-bearing.
