# Creator Dossier: Riley Brown (@rileybrownai) — YouTube Shorts

**Niche:** Vibe coding (Claude Code, Codex, Cursor) — build-a-mobile/web-app-by-prompt demos.
**Why he's in scope:** shorts-native leader of the exact niche the owner's planned channel will occupy;
directly transferable format, especially his "show the AI building something live" mechanics.

Cross-referenced against: `/Users/sparsh/Documents/Projects/Tangent/social_launch/research/QC_PROTOCOL.md`,
`templates/video_postmortem_template.md`, `03_virality_science.md`. Evidence tags `[OBSERVED]` /
`[REPORTED]` / `[INFERRED]` used per protocol on every substantive claim.

---

## A. Channel Header

### Identity & scale
- **Handle:** [@rileybrownai](https://www.youtube.com/@rileybrownai) | **Subscribers: 264,000**
  `[OBSERVED]` — direct yt-dlp fetch of channel page, 2026-07-25, HIGH confidence.
- **Total video count:** 202 videos, 10.8M total channel views, 27.1K average views/video
  `[REPORTED]` — developereducators.com channel-stats aggregator page, fetched via WebFetch
  2026-07-25, MED confidence (third-party aggregator, methodology not disclosed, but numbers are
  internally consistent with the shorts+long-form split observed directly below). A same-day prior
  pull in this research pipeline (`02_youtube_channels.md`, 2026-07-25) recorded 204 videos via a
  direct live channel-page count — HIGH confidence for that specific figure. The two counts (202 vs
  204) are close enough to be explained by snapshot timing (new upload between pulls) and are not a
  material discrepancy.
- **Engagement rate:** 2.88% channel-wide; 718 avg likes/video; 64 avg comments/video `[REPORTED]`,
  developereducators.com, 2026-07-25, MED. Ranked "top 43% of AI Coding educators" among 1,715
  channels in that vendor's category taxonomy `[REPORTED]`, MED — the ranking methodology is not
  disclosed and should be read as rough positioning, not a precise percentile.
- **Cadence:** "Weekly" upload frequency, classified "Very Active" `[REPORTED]`, developereducators.com,
  MED. Independently corroborated at higher resolution by a 2026-04-28 podcast appearance (see below):
  **4-5 high-quality educational shorts/week + 2 additional trending-topic shorts/week (~6-7
  shorts/week total)**, down from a higher-volume "quantity" phase earlier in the channel's history
  `[REPORTED]`, Creator Science podcast #303 show notes (podcast.creatorscience.com/riley-brown/),
  fetched via WebFetch 2026-07-25, MED confidence — this is a podcast-page summary of Riley's own
  stated numbers, not an independently verified production log, and not a primary transcript listen-through.
- **30-day trajectory (as of 2026-07-25 snapshot):** +6.5% subscribers, +10.6% views over the prior 30
  days; view growth described as "decelerated" vs the previous 30-day window (+11.6%) `[REPORTED]`,
  developereducators.com, MED.

### Shorts performance sample (this dossier's dataset)
- **Method:** `yt-dlp --flat-playlist --playlist-items 1:150` (then re-confirmed at `1:300`) against
  `https://www.youtube.com/@rileybrownai/shorts`, 2026-07-25. Both pulls returned the **identical
  39 videos** — this is a data-access ceiling, not a true "all shorts ever posted" catalog (see Method
  log / data gaps). `[OBSERVED]`, HIGH confidence for the 39 raw view/date numbers themselves; MED
  confidence that this 39-video set is representative of the channel's full shorts history, since the
  channel's implied total video count (202-204) minus the ~25 long-form videos visible on the /videos
  tab implies well over 39 shorts have been posted historically. Treat the 39-video sample as YouTube's
  shelf-exposed set (likely recency + evergreen-popularity weighted), not a random or complete sample.
- **Median short (of 39): 11,363 views** — "Claude Code on the phone, and it builds mobile apps"
  (Zdq5nrWB4uc), posted 2025-10-28. `[OBSERVED]`, HIGH.
- **Top short: 184,479 views** — "Claude is so much better when you use MCP" (GZxjs8FD3Ck), posted
  2025-06-18. `[OBSERVED]`, HIGH.
- **Top/median ratio: 16.24x.** `[OBSERVED]`, calculated from the above, HIGH.
- **Range:** 3,156 – 184,479 views across the 39-video sample. `[OBSERVED]`, HIGH.
- **Long-form comparison (important, counterintuitive finding):** a parallel sweep of the /videos tab
  (`yt-dlp --flat-playlist --playlist-items 1:25`, 2026-07-25, `[OBSERVED]` HIGH) shows long-form
  substantially OUT-performing shorts in absolute views on this channel — range 6,800–343,000, with a
  rough median in the ~50K neighborhood (computed from the 25-video sample), roughly **4-5x the shorts
  median**. Top long-form: "Learn 95% of Codex in 30 minutes" at 343,000 views. This is atypical for a
  "shorts-native" framing and matters for Tangent: on this channel, shorts function primarily as a
  **discovery/top-of-funnel layer that feeds long-form**, not as the terminal content product — see
  Funnel map below and video pDsd2FiMUt8's explicit CTA.

### Funnel map: how content feeds Vibecode
- Riley Brown is **co-founder and CEO of Vibecode** (vibecode.dev / vibecodeapp.com / "Vibecode AI App
  Builder" on the App Store), an AI mobile-app-building startup `[REPORTED]`, getlatka.com company
  profile, fetched via WebFetch 2026-07-25, MED.
- **Funding: $9.4M seed round, 2025** `[REPORTED]`, getlatka.com, MED — corroborated by an independent
  secondary source title ("How Riley Brown Built a $9M AI App Using 'Vibe Coding'",
  nazdiocampo.com) found via WebSearch, MED, and by this pipeline's own prior research
  (`02_youtube_channels.md`, "~$9M raised," MED). Lead investor not disclosed in the sources found.
  **~10 employees** as of September 2025 `[REPORTED]`, getlatka.com, MED.
- **Beta traction:** 200 initial beta users produced ~3,000 apps, with a stated ~20-minute build time
  per app `[REPORTED]`, WebSearch summary of press coverage aggregating multiple secondary sources
  (developereducators.com bio, follow-on press), MED, no single primary press release located and
  verified directly. A separately-cited figure of **10,000+ paid users** appears in secondary sources
  `[REPORTED]`, MED, same caveat.
- **Direct funnel evidence, observed in this dossier's own video sample:**
  - 5 of the 11 analyzed videos are literal Vibecode/vibecode.dev product demos (wrLSsAjR19Q,
    9GWxBG9f564, Mq1rijmpzX8, Zdq5nrWB4uc, hX7D1pMOEzw) `[OBSERVED]`, transcripts.
  - wrLSsAjR19Q's description contains a direct App Store purchase link:
    `https://apps.apple.com/us/app/vibecode-ai-app-builder/id6742912146` `[OBSERVED]`.
  - pDsd2FiMUt8 (a NON-Vibecode video, general Codex content) ends with an explicit verbal CTA
    redirecting viewers to Riley's own 1h43m long-form Codex/GPT-5.5 explainer: *"I just made an hour
    and 43-minute video that explains every single thing you need to know about Codex and GPT-5.5...
    you will literally get fully up to speed if you watch this video."* `[OBSERVED via transcript]` —
    this is the clearest shorts→long-form funnel hop in the sample, and given the long-form median
    (~50K) vastly exceeds the shorts median (11.3K), this hop is plausibly where most of the channel's
    actual watch-time and ad/sponsor value accrues.
  - tN42JpEwAro is a **paid sponsor read** for Code Rabbit with a personal discount code ("RILEY") and
    a "link in bio" CTA `[OBSERVED]` — direct affiliate-revenue funnel, separate from the Vibecode
    product funnel, showing the channel monetizes shorts on (at least) two parallel tracks: owned
    product (Vibecode) and third-party sponsorship (Code Rabbit and likely others).
  - 3M_ydA_cuMQ (OpenAI Agent Builder news) explicitly pivots mid-video to Riley's own company: *"for
    instance, my company Vibe Code, we could use the apps SDK to allow for the following
    experience..."* — even pure tech-news content gets steered back to the product `[OBSERVED]`.
- **Content-ops → funnel amplification:** per the Creator Science podcast (see Content Architecture,
  section D), Riley reposts his best-performing video weekly across **7 X/Twitter accounts (200K+
  combined followers)**, which he states **tripled his company's [Vibecode's] revenue in two months**
  `[REPORTED]`, MED — a direct, quantified link between the content operation and the startup's
  business outcomes.

---

## B. Per-Video Post-Mortems (11 videos: top 8 + median + 2 flops)

**Selection method:** Per QC_PROTOCOL step 2 (top 8 by views + 2-3 flops excluding 5 most recent +
median). Selected top 8, the exact median, and 2 flops (one on-formula, one off-formula) = 11 videos,
inside the "10-11" deliverable target. The 5 most-recent videos (by upload date: 0v9MGS_GMWI 2026-07-16,
C64tVVgquhc 2026-06-24, cHdaCCpJ1CY 2026-06-17, 3mm-hxVtjkM 2026-05-15, pDsd2FiMUt8 2026-04-25) were
excluded from flop consideration per protocol — note 3mm-hxVtjkM and pDsd2FiMUt8 are in this list AND
in the top-8-by-views list; that's fine, the recency exclusion only gates FLOP selection, not top-N
selection (a video can be both recent and already a proven top performer).

---

## VIDEO 1 (Rank #1 of 39 — TOP): "Claude is so much better when you use MCP"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/GZxjs8FD3Ck | **Platform:** YouTube Shorts
- **Post date:** 2025-06-18 `[OBSERVED]`, yt-dlp metadata fetch, 2026-07-25, HIGH
- **Length:** 86 seconds `[OBSERVED]`, HIGH
- **Views: 184,479** | **Likes: 6,161** | **Comments: 753** — all `[OBSERVED]`, yt-dlp direct video-page
  fetch, 2026-07-25, HIGH confidence, as-of the fetch date (views/likes/comments continue to accrue).
- **Like rate:** 3.34% of views. **Comment rate: 0.408%** of views — by far the highest comment rate of
  any video in this 11-video sample (next highest is hX7D1pMOEzw's flop-tier 0.228%, and most top
  performers sit at 0.10-0.14%). `[OBSERVED]`, calculated.
- **Rank:** #1 of 39 in the shorts sample (highest by views). **16.24x the channel's shorts median**
  (11,363 views). This is the single clearest outlier in the dataset.

### 1. Packaging
- **Title:** "Claude is so much better when you use MCP #claude #mcp #automation #aivideo" — a bold,
  comparative claim ("so much better") tied to a specific named technology (MCP = Model Context
  Protocol) that functions as a keyword/hashtag cluster as much as a title.
- **Description:** empty `[OBSERVED]` — DATA GAP note: no supplementary caption text exists beyond the
  title; all context comes from the title and the video itself.
- **Curiosity gap:** the title promises a comparative claim ("better") but doesn't explain the
  mechanism — "when you use MCP" is named but not defined, creating a real information gap for
  viewers who know Claude but not MCP specifically (per Loewenstein's partial-knowledge framing,
  03_virality_science.md §2.1.1).
- **Text overlay on frame 1:** not independently verifiable without visual frame capture — DATA GAP,
  transcript-only analysis; based on the opening line (immediate live demo, no title card described in
  audio), `[INFERRED]` there is likely minimal/no text overlay delaying the hook, consistent with this
  creator's dominant pattern across the sample.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"I just plugged this AI agent into this app
  that I vibe coded and it has access to my Slack, my notion to-do list, and my calendar."*
- **Hook taxonomy:** Result-first / demo-in-motion, layered with a bold-claim setup (per
  03_virality_science.md §3.1). The viewer is dropped directly into an already-built, already-connected
  system — no preamble, no "hey guys."
- **What the viewer sees:** screen-recording of a live agent interface, immediately followed by a
  spoken command. This is pure demo-in-motion from frame one — no talking-head cold open.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:04 — Hook: agent has access to Slack/Notion/Calendar
  - 0:04-0:14 — First command: "add a calendar event in 30 minutes to edit this short form video" →
    event appears, agent confirms verbally ("Perfect. I've created a calendar event for you.")
  - 0:14-0:32 — Explains this is a persistent/autonomous agent ("will actually use these tools for as
    long as it needs to... you can do many things at once")
  - 0:32-0:53 — Second, more elaborate multi-task command: send Slack messages to two named
    colleagues ("Muhammad," "Kihan"), add a to-do item, schedule an absurd/comedic calendar event
    ("dance around the room at 8pm tonight")
  - 0:53-1:09 — Payoff montage: agent visibly executes each sub-task in sequence, closing every loop
    opened in the command ("make sure to hit the gym... water the plants... dance around the room" —
    each shown landing)
  - 1:09-1:26 — Close: framed as "one of the biggest trends in AI," explicit comment-bait CTA: "if you
    want to learn how to do this, comment [MCP]"
- **Open loops:** each verbal sub-command is its own mini open loop (will it actually send that Slack
  message? will it actually add that to-do?) — all are visibly closed within the same video, satisfying
  §2.6.1's "close what you open" principle at a granular level. The overall "is this really autonomous"
  claim is the macro loop, closed by the final montage.
- **One-idea-per-video:** yes — the single idea is "one agent, many connected tools, autonomous
  execution." The multiple sub-tasks are sub-payoffs within one coherent frame (comparable to a
  listicle's "one unifying frame" per §3.2), not scope creep.
- **Pacing:** screen-recording throughout, cuts appear to track each new command/response pair (based
  on caption timestamp clustering) — dynamic, task-by-task pacing rather than one long static take.
- **Loop design / rewatch bait:** the comedic absurdity of the final task ("dance around the room")
  functions as a light rewatch trigger and a shareable, quotable moment distinct from the utilitarian
  Slack/calendar tasks.

### 4. Value proposition
- **What the viewer walks away with:** a concrete workflow concept (agent-connected-to-your-tools via
  MCP) plus, implicitly, a call to get the "how" via commenting — the actual how-to is gated behind
  engagement, not shown in full.
- **Practical value class:** tool discovery + workflow concept, with the deepest "how" withheld as
  comment-bait.
- **Specificity level:** moderate — real tool names (Slack, Notion, calendar) and a real (if
  ASR-ambiguous — see below) agent framework are shown, but no exact MCP server config, prompt text, or
  setup steps are shown on-screen; the mechanism is demonstrated, not taught.
- **Transcription note:** the auto-caption renders one term as "NAND agent" — this is almost certainly
  an ASR mis-hearing of "**n8n** agent" (n8n is a workflow-automation tool, pronounced "en-eight-en"),
  not a real "NAND agent." `[INFERRED]`, flagged rather than presented as fact, because the audio itself
  was not independently re-verified beyond the auto-caption.

### 5. Psychology scoring (against 03_virality_science.md)
- **STEPPS scan:**
  - *Social Currency* — high. Commenting the keyword to unlock the "how" is a status-signaling,
    in-the-know action; sharing this positions the sharer as ahead of the automation curve.
  - *Triggers* — moderate. Slack/calendar/to-do are near-universal daily-use tools, giving the content
    a frequent environmental cue (§2.2).
  - *Emotion* — awe/amusement blend, high-arousal per Berger & Milkman (§2.3): the "dance around the
    room" absurd task specifically manufactures an amusement beat inside an otherwise utilitarian demo.
  - *Public* — moderate; the comment section itself becomes a visible signal of interest (753 comments
    is unusually public proof of demand).
  - *Practical Value* — high in concept, deliberately incomplete in execution (see CTA below) — this is
    the video's central design choice.
  - *Story* — thin narrative arc (agent given tasks → tasks completed) but functional as a Trojan horse
    for the underlying MCP concept.
- **Primary emotion + arousal:** awe (capability surprise) + amusement (absurd task), both high-arousal
  per §2.3 — squarely in the share-favorable emotional register.
- **Identity-signaling share motive:** sharing this says "I'm plugged into agentic AI / MCP before most
  people," per §2.2/§2.5.
- **Save/send trigger:** the comment-gated CTA substitutes for a save trigger — instead of "save this,"
  the design goal is "comment this," converting a save-type intent into a comment-type action, which
  per §1.1.2/§2.7 is a weaker distribution signal than a share/send but a very strong on-platform
  engagement signal, and the 753-comment count (0.408% of views) suggests it worked as designed.

### 6. CTA & funnel mechanics
- **Explicit CTA:** "if you want to learn how to do this, comment [keyword, presumably MCP]" —
  classic comment-bait mechanic per §3.4.3, functionally identical to a ManyChat-style keyword capture
  even if no bot is confirmed to be running. `[OBSERVED]` for the CTA language; `[INFERRED]` that this
  triggers an automated DM (ManyChat or similar) rather than a manual reply — not independently
  confirmable from the video alone. DATA GAP: could not verify whether commenting actually triggers a
  DM funnel without commenting live (out of scope for passive research).
- **QC compliance check (§1.3.2):** this sits right at the edge of Instagram/Meta's stated
  "engagement-bait" policy line, but the distinguishing test given in the virality doc — "does the video
  have standalone value without the bait" — is satisfied: the video already delivers a full demo with a
  visible payoff before the CTA lands, so this reads as a compliant CTA-on-top-of-real-content rather
  than bare bait. (Note: this policy citation is Instagram-specific in the source doc; YouTube's
  Shorts-specific engagement-bait stance was not separately verified — flagged as `[INFERRED]`
  application by analogy.)
- **Funnel position:** top-of-funnel viral bait, not a direct sales push — no product name, no link, no
  price. The ask is pure engagement/audience-growth, consistent with this being his single highest
  performer.

### 7. Replicability verdict
- **Extractable template:**
  1. Open cold, mid-demo, with a bold comparative claim in the first sentence.
  2. Show a real (or real-looking) autonomous agent executing multiple distinct, named real-world tools.
  3. Include one deliberately absurd/comedic sub-task among the utilitarian ones.
  4. Visibly close every loop you open (show each task landing).
  5. Withhold the exact "how" and gate it behind a comment-keyword CTA.
  6. Keep runtime tight (86s) relative to task count — dense but not padded.
- **Commodity vs unfair advantage:** the demo-in-motion mechanic and comment-gating are fully
  copyable by any creator. Riley's unfair advantage is that he has a genuinely working, already-built
  agent stack to demo (not staged) and an existing audience primed to comment on AI-tool videos.
- **Difficulty for Tangent: MED.** The structural template (bold claim → live demo → absurd sub-task →
  gated CTA) is straightforward to imitate; the harder part is having a genuinely working, camera-ready
  automation stack to demo rather than a mockup, and building the initial audience base that makes a
  comment-gate worth using at all (low-follower accounts get few comments regardless of CTA quality).

### 8. Why it won
This is the clearest single outlier in the entire sample (16.24x median), and the load-bearing reason
is the **comment-count anomaly**: at 0.408% comment rate it is roughly 3-4x the comment rate of every
other top-tier video in this sample, strongly suggesting the explicit comment-gated CTA is directly
responsible for both the engagement spike and, via YouTube's algorithmic weighting of engagement signals
(§1.2.2), the outsized view count — comments are a stronger, more effortful signal than likes, and
elevated comment velocity in the "audition window" (§1.1.3/§1.2.2) plausibly triggered broader
algorithmic push. Secondary factors: the "MCP" keyword was, per this pipeline's own prior research
(`02_youtube_channels.md`), independently flagged as his top-performing short before this dossier even
began, and MCP was a genuinely trending, high-search-interest term in the AI-coding space around this
period — likely some trend-surfing/timing tailwind (§1.4 "velocity of trend response") in addition to
the format itself. `[INFERRED]` on the timing-tailwind component specifically, since exact MCP search-
trend data was not independently pulled for this dossier.

### Sources
- https://www.youtube.com/shorts/GZxjs8FD3Ck (yt-dlp metadata + auto-captions, 2026-07-25)
- `/Users/sparsh/Documents/Projects/Tangent/social_launch/research/02_youtube_channels.md` (prior-session
  cross-check confirming this video as previously-flagged top performer)

---

## VIDEO 2 (Rank #2 of 39 — TOP): "With Codex and GPT 5.5 you can just do things."

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/pDsd2FiMUt8 | **Platform:** YouTube Shorts
- **Post date:** 2026-04-25 `[OBSERVED]`, HIGH. (Note: among the 5 most-recent videos in the sample —
  excluded from flop eligibility, but eligible and selected as a top performer on its own merits.)
- **Length:** 163 seconds (2:43) — the longest of the 8 top-tier videos analyzed. `[OBSERVED]`, HIGH.
- **Views: 144,230** | **Likes: 5,381** | **Comments: 146** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 3.73%. **Comment rate:** 0.101%.
- **Rank:** #2 of 39. **12.69x the shorts median.**

### 1. Packaging
- **Title:** "With Codex and GPT 5.5 you can just do things." — a bold, almost meme-register claim
  ("you can just do things" is a recognizable internet-culture phrase pattern) rather than a specific
  feature callout.
- **Description:** "Codex with GPT 5.5 / Fun stuff." `[OBSERVED]` — minimal, low-effort caption; nearly
  all packaging weight sits on the title and the in-video hook, consistent with §1.2.3's finding that
  packaging is largely moot for Shorts.
- **Curiosity gap:** "you can just do things" is intentionally vague — it promises capability without
  specifying which capability, maximizing the gap per §2.1.1.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"Oh my god, Codex is actually insane. Look at
  this."*
- **Hook taxonomy:** Bold claim + immediate visual demo-in-motion — an unscripted-sounding reaction
  ("Oh my god") functions as a genuine-surprise signal, distinct from more polished/scripted top-tier
  hooks elsewhere in the sample.
- **What the viewer sees:** a real-time AI animation engine already running on screen — the payoff is
  visible before it's explained.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:08 — Hook + reveal of a new AI animation engine (poses generated in real time)
  - 0:08-0:34 — Personal framing: "I used to get FOMO... I wasn't technical... but now we have AI. I
    was able to get it running in about 5 minutes using Codex" — an origin-story/relatability beat
    (self-disclosure, per §2.4.1 parasocial mechanism)
  - 0:34-0:50 — Shows the source: a GitHub repo he found on X, pastes the link into Codex, asks it to
    run locally
  - 0:50-1:17 — Payoff: working demo, customizes character (dog → corgi), notes "some of them are a lot
    worse than others" (unscripted-feeling authenticity beat)
  - 1:17-2:07 — Escalation: adds video-game mechanics (health system, enemy characters, shooting),
    generates custom background music via suno.ai, adds sound effects — each addition is a new closed
    loop
  - 2:07-2:36 — Plays the finished mini-game live on camera
  - 2:36-2:44 — Explicit funnel CTA to his own 1h43m long-form video
- **Open loops:** "will this actually work when I try it myself" (opened at 0:34, closed at 0:50-1:17);
  "can I make this into an actual game" (opened ~1:17, closed by 2:07 playable demo) — nested loops per
  §2.6.1's leaked-MrBeast-doc pattern (multiple sub-loops building to a final payoff).
- **One-idea-per-video:** the core idea ("Codex can build/extend a real working project from a found
  GitHub repo, fast") is single and clear despite the video's unusual length and multiple escalating
  steps — this reads as a mini-vlog/build-log rather than a listicle, and it holds together.
  Runtime (163s) is roughly 2x this channel's typical short — an outlier in format, not just performance.
- **Pacing:** high — new visual state roughly every 10-20 seconds (new pose, new character skin, new
  game mechanic, new audio) sustained across nearly 3 minutes, which is doing real retention work
  given the length.
- **Loop design:** ends by explicitly sending the viewer to ANOTHER piece of content (his long-form
  video) rather than looping back to this video's start — a funnel-style ending rather than a
  rewatch-bait ending.

### 4. Value proposition
- **What the viewer walks away with:** proof-of-capability (Codex can extend a random open-source repo
  into a playable, scored, sound-tracked mini-game with conversational prompts) plus a direct pointer to
  a deeper tutorial.
- **Practical value class:** primarily aspiration/proof-of-capability + tool discovery, secondarily a
  funnel to a copyable workflow (in the linked long-form video, not this short itself).
- **Specificity level:** moderate-high — real tool chain shown (X → GitHub → Codex → suno.ai →
  finished game), real timestamps cited ("7 minutes and 26 seconds later"), but exact prompts are not
  displayed on-screen text, only spoken/summarized.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — high; being able to say "I built a working game from a random tweet using AI"
    is a strong flex.
  - *Triggers* — moderate; "I saw this on X and was FOMO" is a relatable, frequently-recurring feeling
    among the target audience (non-technical people watching technical builders online).
  - *Emotion* — awe, sustained across a longer runtime via escalating reveals (new skin, new mechanic,
    new sound) rather than one single spike — a "compounding awe" structure.
  - *Public* — moderate; the original GitHub repo's "lot of stars" is cited as social proof that primed
    Riley's own interest, modeling public-proof-driven curiosity for the viewer.
  - *Practical Value* — moderate; concept is transferable (find trending open-source project, feed to
    Codex) even without an exact prompt shown.
  - *Story* — strong; this is the most narratively complete video in the sample — clear
    setup (FOMO) → complication (not technical) → resolution (AI closes the gap) → escalating build →
    climax (playable game) → new call-to-action.
- **Primary emotion + arousal:** awe, high-arousal, sustained rather than single-spike.
- **Identity-signaling share motive:** "I could actually do this even though I'm not a programmer" —
  aspirational identity content, shareable to non-technical friends specifically.
- **Save/send trigger:** the "I wasn't technical either" framing creates a strong "send this to a
  non-technical friend who'd be surprised" moment (§2.7's addressable-recipient marker).

### 6. CTA & funnel mechanics
- **Explicit CTA:** verbal-only redirect to his own long-form video (no on-screen link, no comment-gate)
  — a pure content-to-content funnel rather than a product or engagement-bait funnel.
- **Comment-bait mechanics:** none present — this video relies on the story/value itself, not a gated ask.
- **Funnel position:** top-of-funnel discovery feeding his OWNED long-form catalog directly (nurture,
  not top-of-funnel-only) — distinct in kind from Video 1's audience-growth-only CTA.

### 7. Replicability verdict
- **Extractable template:**
  1. Open on an unscripted-feeling reaction to something you found (not something you built from
     scratch) — lowers the bar to "I discovered this," which is more relatable than "I invented this."
  2. Self-disclose a relatable limitation (non-technical) before showing the capability that erases it.
  3. Escalate in visible stages (skin → mechanic → mechanic → audio) rather than one big reveal.
  4. Let the runtime run long if the escalation stays dense — don't force an artificial cut.
  5. Close with a verbal pointer to a deeper owned asset rather than an engagement-bait CTA.
- **Commodity vs unfair advantage:** the "find something on X, extend it live" mechanic is fully
  copyable; Riley's unfair advantage is a pre-existing long-form catalog deep enough to credibly promise
  "everything you need to know" as the payoff destination.
- **Difficulty for Tangent: MED-HIGH.** Requires (a) actually monitoring trending open-source/AI
  projects to react to quickly, (b) comfort with a longer, multi-stage runtime that most Shorts advice
  argues against, and (c) an existing long-form library worth funneling into — without that library,
  the ending CTA has nowhere to send people.

### 8. Why it won
Two load-bearing factors: first, the escalating multi-reveal structure sustains genuine watch-time
across an unusually long 163-second runtime, which — per §1.2.2's completion-rate mechanism — likely
earned outsized algorithmic distribution if completion held up (a 60s video needs one hook; a 163s video
needs several, and this one delivers a new visual payoff roughly every 15-20 seconds). Second, the
relatable "I wasn't technical" framing broadens the addressable audience beyond people who already know
what Codex is, functioning as an on-ramp for a wider swipe-feed audience than the more insider-coded
Video 1. Recency is a plausible minor tailwind (posted 2026-04-25, among the 5 most recent in the
sample, so the algorithm has had comparatively less total exposure time to fully mature this one's
final view count — meaning its TRUE outlier multiple, once it fully matures, may end up even higher
than currently measured). `[INFERRED]` on the still-maturing-views point specifically.

### Sources
- https://www.youtube.com/shorts/pDsd2FiMUt8 (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 3 (Rank #3 of 39 — TOP): "Openclaw Blender part 2"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/uhVEIJXXvU4 | **Platform:** YouTube Shorts
- **Post date:** 2026-02-19 `[OBSERVED]`, HIGH. **Length:** 113 seconds `[OBSERVED]`, HIGH.
- **Views: 116,375** | **Likes: 5,486** | **Comments: 117** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 4.71% — the highest like-rate of any video in this 11-video sample. **Comment rate:**
  0.101%.
- **Rank:** #3 of 39. **10.24x the shorts median.**

### 1. Packaging
- **Title:** "Openclaw Blender part 2" — terse, assumes prior-video familiarity ("part 2"), names two
  proper nouns (a tool called "OpenClaw" and the 3D software Blender) without explanation.
- **Description:** identical to title, "Openclaw blender part 2" `[OBSERVED]` — no supplementary text.
- **Curiosity gap:** for anyone who saw "part 1," this promises continuation (open loop from a prior
  video); for anyone who didn't, the title alone is genuinely curiosity-inducing (what is "OpenClaw"?
  why is it in Blender?) even without that context — the title works on two different audience
  segments simultaneously.
- **Series signal (§3.4.2):** "part 2" is an explicit series marker, a format this creator uses at
  least occasionally to build appointment-viewing habits, though DATA GAP: part 1's own performance was
  not part of this 11-video sample and was not independently pulled.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"No way. This right here is my OpenClaw AI
  agent running on this Mac Mini and it can literally control Blender."*
- **Hook taxonomy:** Bold claim ("no way," "literally control") + demo-in-motion, applied to a genuinely
  novel domain — an AI agent controlling professional 3D-animation software is a less commonly
  demonstrated capability than coding/app-building, giving this an extra novelty layer beyond most of
  the sample.
- **What the viewer sees:** a live screen-recording of Blender's interface with a 3D character model
  already on screen, framed as physically running on a specific piece of hardware (Mac Mini) — grounds
  the abstract "AI agent" claim in a concrete, ownable object.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:10 — Hook: OpenClaw agent controls Blender, running on a named machine
  - 0:10-0:15 — First command: "make this guy amazing and red"
  - 0:15-0:38 — Iterative refinement in real time: material preview toggle, "it's red but not red
    enough," eye spacing, arm size — a rapid-fire sequence of small, visible adjustments
  - 0:38-0:53 — Waits for render (explicit "now we're going to wait" — an honest, unhidden processing
    beat rather than a hard cut, which paradoxically builds credibility)
  - 0:53-1:01 — Payoff: animation request ("how would I animate this... wave... blinks")
  - 1:01-1:18 — Second creative pass: final consolidated prompt (make more red, download the model,
    build a landing page, make it spinnable, run locally) — deploys via localhost
  - 1:18-1:32 — Opens localhost link on screen, character ("Billy Bob") appears live in browser, spins
    it interactively
  - 1:32-1:54 — Deploys publicly ("please deploy this to Vercel, send me a public link"), opens on
    phone, spins the character again on a second device — cross-device proof
- **Open loops:** "will the render actually look good" (opened 0:10, closed 0:19 "oh, look at it");
  "will it deploy and actually work on another device" (opened 1:32, closed 1:44-1:54 phone demo) —
  a clean nested-loop structure.
- **One-idea-per-video:** yes — "AI agent operates real professional software end-to-end, from edit to
  public deployment." Every beat serves that single claim.
- **Pacing:** very high — visible state changes roughly every 5-10 seconds through most of the runtime,
  the densest pacing of the top-8 set.
- **Loop design:** the cross-device reveal (same character, now spinnable on a phone via a public URL)
  is a strong "wait, it's really live" rewatch-worthy beat.

### 4. Value proposition
- **What the viewer walks away with:** proof that AI agents can operate outside the coding/app domain
  entirely — into professional creative software (Blender) — end to end, including public deployment.
- **Practical value class:** primarily aspiration/tool-discovery (this is a novelty capability
  demonstration, not a copyable workflow — no setup steps for "OpenClaw" itself are shown).
- **Specificity level:** low-moderate on setup (no install/config instructions), high on demonstrated
  outcome (specific, visible before/after states at each step).

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — high; this is squarely "look what AI can do that you didn't know it could do,"
    the archetypal in-the-know share.
  - *Triggers* — low-moderate; Blender/3D software is a narrower recurring cue than Slack/calendar
    from Video 1, but "AI controlling my computer" as a general concept is broadly triggering.
  - *Emotion* — awe, high-arousal, arguably the purest awe-only video in the top tier (fewer comedic
    beats than Videos 1 or 9GWxBG9f564).
  - *Public* — low; no visible external social proof cited within the video itself.
  - *Practical Value* — low-moderate; entertaining/aspirational more than directly actionable.
  - *Story* — moderate; iterative refinement (fix red → fix eyes → fix arms → animate → deploy) gives a
    light narrative arc even without an explicit setup/complication/resolution frame.
- **Primary emotion + arousal:** awe, high-arousal — the video's entire design is optimized around
  successive small "wait, it actually did that" beats.
- **Identity-signaling share motive:** shares position the sharer as someone tracking the frontier of
  agentic AI beyond the (by 2026) more commoditized "AI writes code" claim.
- **Save/send trigger:** moderate — closer to a "watch and be amazed" video than a "save this for later
  reference" video, consistent with its practical-value score being the section's weakest STEPPS pillar
  despite the video's strong overall performance — a useful counter-example to the assumption that
  practical value is required for outlier performance (awe alone carried this one).

### 6. CTA & funnel mechanics
- **Explicit CTA:** none observed in the transcript — no comment-gate, no link, no verbal redirect.
  `[OBSERVED]` (absence noted, not inferred).
- **Comment-bait mechanics:** none.
- **Funnel position:** pure top-of-funnel brand/capability content — reinforces "Riley Brown = frontier
  AI demos" positioning without an immediate monetization or growth ask.

### 7. Replicability verdict
- **Extractable template:**
  1. Pick a domain outside the expected "AI codes apps" lane (here: professional 3D software) for
     novelty.
  2. Anchor the abstract "AI agent" claim in a concrete physical object (named hardware).
  3. Show rapid, granular, iterative refinement (several small visible changes, not one big jump).
  4. Include an honest "now we wait" beat rather than hiding processing time — builds authenticity.
  5. Close with cross-device/public-deployment proof, not just an on-machine result.
- **Commodity vs unfair advantage:** the underlying "OpenClaw" agent/tool integration into Blender is
  the least commodity element in the sample — most viewers cannot trivially replicate this specific
  setup, unlike the Vibecode-app videos which show a consumer product anyone could download.
- **Difficulty for Tangent: HIGH.** Requires genuine technical capability to wire an AI agent into
  specialized creative software (not just prompt a chat interface), which is a materially higher setup
  bar than the phone-app-building demos elsewhere in the sample.

### 8. Why it won
The load-bearing factor is domain novelty combined with the highest like-rate in the sample (4.71%):
viewers who stayed clearly found the specific spectacle of AI operating professional 3D software (not
just chat or code) to be a strong "like"-worthy surprise, even without a strong practical-value or
CTA layer to convert that liking into comments or saves. The "part 2" series framing likely also carried
forward some warm audience from a "part 1" this dossier did not independently verify (DATA GAP) —
mere-exposure/appointment-viewing effects (§2.4.2, §3.4.2) plausibly contributed, but this is
`[INFERRED]`, not confirmed, since part 1's performance was out of sample.

### Sources
- https://www.youtube.com/shorts/uhVEIJXXvU4 (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 4 (Rank #4 of 39 — TOP): "Claude 4.5 Sonnet Builds a Mobile App"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/9GWxBG9f564 | **Platform:** YouTube Shorts
- **Post date:** 2025-09-29 `[OBSERVED]`, HIGH. **Length:** 87 seconds `[OBSERVED]`, HIGH.
- **Views: 35,539** | **Likes: 789** | **Comments: 27** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 2.22% (the lowest of the top-8 tier). **Comment rate:** 0.076% (also the lowest of the
  top-8 tier).
- **Rank:** #4 of 39. **3.13x the shorts median** — a clear step down in outlier magnitude from videos
  1-3, marking the boundary between "extreme outlier" and "solidly above-average" performance in this
  sample.

### 1. Packaging
- **Title:** "Claude 4.5 Sonnet Builds a Mobile App" — names a specific, dated model release, positions
  it as news (implies "just released," confirmed in the description).
- **Description:** "The best Coding Model in the world was JUST released... Claude 4.5 Sonnet... And
  it's so good at building and designing Mobile Apps in a single prompt." `[OBSERVED]` — reinforces the
  "best in the world" bold claim and the "single prompt" specificity hook.
- **Curiosity gap:** moderate — model-release videos carry an inherent "is it actually better" gap for
  an audience that tracks model releases closely, but this is a narrower/more insider-coded gap than
  the broader claims in Videos 1-3.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"Claude just released the most powerful
  coding model in the world and it is insane at building mobile apps. Build a mobile app that is like
  Instagram for dogs."*
- **Hook taxonomy:** Bold claim (news framing) immediately followed by an absurd/comedic task
  assignment ("Instagram for dogs") — the comedic specificity of the task is doing hook work that the
  generic "best model" claim alone would not.
- **What the viewer sees:** presumably a prompt interface (not independently frame-verified — DATA GAP),
  transitioning quickly into visible app-building progress based on the transcript's pacing.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:13 — Hook + absurd task assignment ("Insta Woof")
  - 0:13-0:22 — Fast build claim: "it's just noticeably faster... only been like 1 minute... it's done"
  - 0:22-0:38 — Reveal of the built app (search tab, feed posts named "Golden boy," "husky heaven,"
    "Frenchie fan" — comedic specificity continues)
  - 0:38-0:52 — Unscripted-feeling error moment: "Oh no, an error. Oh god." → fixes by copy/pasting the
    error back to the model → "that was literally 20 seconds. It fixed the error in 20 seconds" — an
    authenticity/trust beat similar to Video 3's "now we wait"
  - 0:52-1:01 — Confirms the fix, shows the working profile screen
  - 1:01-1:27 — Ships to the App Store via vibecode.dev: generates an app icon, enters Apple developer
    account, submits
- **Open loops:** "will the model actually be fast" (opened 0:13, closed 0:20 "it's done"); "will the
  error break the demo" (opened 0:39, closed 0:53 "we are fixed") — the error-and-recovery loop is the
  strongest trust-building device in this specific video, arguably more persuasive than a flawless run
  would have been, because it demonstrates resilience, not just initial output quality.
- **One-idea-per-video:** yes — "the newest model builds and fixes a mobile app end-to-end, fast."
- **Pacing:** high, comparable to Video 3, new visible state roughly every 10-15 seconds.
- **Loop design:** ends on a forward-looking "it's being sent to Apple" cliffhanger rather than a
  completed/closed beat — a soft, non-rewatch-optimized ending.

### 4. Value proposition
- **What the viewer walks away with:** confidence that a specific, named model (Claude 4.5 Sonnet) is
  fast and self-correcting for app-building, plus a visible end-to-end path to the App Store via
  Vibecode.
- **Practical value class:** tool discovery (model comparison/recommendation) + product funnel
  (Vibecode).
- **Specificity level:** moderate — the exact "Instagram for dogs" prompt is shown/spoken but the full
  build session (all follow-up prompts) is compressed/summarized, not shown in full.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — moderate; "I know which model is actually good right now" is a smaller flex
    than Videos 1-3's broader claims, appropriate to its smaller outlier multiple.
  - *Triggers* — low; tied to a specific, time-bound model release rather than an evergreen daily-use
    trigger — this content has a shorter relevance half-life by design.
  - *Emotion* — amusement (the comedic app concept and copy) + mild relief/trust (error recovery) —
    lower peak arousal than Videos 1-3.
  - *Public* — low.
  - *Practical Value* — moderate; a real signal about model choice for app-building.
  - *Story* — the error-recovery beat gives this the closest thing to a complication/resolution arc in
    the top-8 tier below Video 2.
- **Primary emotion + arousal:** amusement + mild awe, moderate-high arousal — a notch below the pure
  awe register of Videos 1-3.
- **Identity-signaling share motive:** "I know which coding model to use" — a narrower, more
  practitioner-coded status claim than the broader top-3 videos.
- **Save/send trigger:** moderate — model-comparison content has some reference/save value for people
  actively choosing tools, time-bound to the model's relevance window.

### 6. CTA & funnel mechanics
- **Explicit CTA:** none verbal; the App Store submission IS the implicit CTA (showing the path to
  ship your own app via Vibecode functions as an unstated product demo).
- **Funnel position:** product funnel (Vibecode) layered under a model-news hook.

### 7. Replicability verdict
- **Extractable template:**
  1. React to a model release with a bold "best in the world" framing.
  2. Assign an absurd, specific, comedic build task rather than a generic one.
  3. Deliberately include and narrate an error, then show the fast fix — resist the urge to edit out
     mistakes.
  4. Close on the shipping/deployment step to reinforce "this is real, not a toy."
- **Commodity vs unfair advantage:** highly commodity — any creator with access to the same model and
  a builder tool could replicate this almost exactly; Riley's edge here is speed-to-publish (being
  early on a fresh model release) more than any unique asset.
- **Difficulty for Tangent: LOW-MED.** Requires only a builder tool and willingness to publish reactive,
  timely content quickly after model releases — the main constraint is speed/monitoring, not technical
  depth.

### 8. Why it won (moderately, not extremely)
This video performed well (3.13x median) but notably less than Videos 1-3, and the STEPPS/emotion
analysis explains why: it lacks the sustained or peak-awe moment those videos have (its highest-emotion
beat, the error recovery, is a smaller "phew" rather than a "whoa"), its social-currency claim is
narrower (model choice vs. general AI capability), and it has zero explicit CTA or engagement mechanic
driving comments (0.076% comment rate, the lowest of the top-8 tier). It over-performs the channel
median primarily on the strength of a timely, bold hook and reliable demo-in-motion execution — a solid,
repeatable "good, not great" template rather than a viral spike.

### Sources
- https://www.youtube.com/shorts/9GWxBG9f564 (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 5 (Rank #5 of 39 — TOP): "OpenAI just released Codex Mobile"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/3mm-hxVtjkM | **Platform:** YouTube Shorts
- **Post date:** 2026-05-15 `[OBSERVED]`, HIGH (among the 5 most recent in the sample; excluded from
  flop eligibility but selected here as a top performer). **Length:** 98 seconds `[OBSERVED]`, HIGH.
- **Views: 32,415** | **Likes: 1,153** | **Comments: 44** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 3.56%. **Comment rate:** 0.136%.
- **Rank:** #5 of 39. **2.85x the shorts median.**

### 1. Packaging
- **Title:** "OpenAI just released Codex Mobile" — news-framed, names the product precisely.
- **Description:** "OpenAI just released Codex Mobile / Directly inside ChatGPT. / Codex is OpenAI's
  version of Claude Code, and arguably better. / Now you can control the Codex desktop app with your
  phone." `[OBSERVED]` — notably positions a COMPETITOR product (Codex, OpenAI) as "arguably better"
  than Claude Code, on a channel whose other content frequently features Claude — a credibility signal
  (not a brand-loyalty channel) worth noting for Tangent's own positioning decisions.
- **Curiosity gap:** moderate; "control the desktop app with your phone" is a specific, checkable claim.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"Yep. Open AI just added the Codex app, which
  is their version of Claude code directly inside chat GPT."*
- **Hook taxonomy:** News/bold-claim hybrid, immediate and flat-affect delivery ("Yep") that reads as
  confirmation of something viewers may have already heard rumored, rather than a fresh reveal —
  functions differently from the more surprised/excited hooks elsewhere in the sample.
- **What the viewer sees:** the ChatGPT mobile app interface, transitioning into remote control of a
  desktop application.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:09 — Hook + product identification
  - 0:09-0:25 — Demonstrates phone-to-desktop control chain: phone → ChatGPT app → Codex → desktop app
    → "computer use" → browser control
  - 0:25-0:40 — First real task: "go through my email, find brands who reached out this week, compile a
    spreadsheet"
  - 0:40-0:53 — Waits (stated: "can take up to 10 minutes"), then shows the completed spreadsheet
  - 0:53-1:03 — Reveals this used a custom "brand deal researcher skill" he built — a callback to his
    own prior tool-building, implying series/system depth
  - 1:03-1:16 — Second task: generate a landing page "of me," using an autonomous "YOLO mode" skill
    that auto-deploys to Vercel
  - 1:16-1:29 — Shows the live deployed site, plugs an "agent library" resource
  - 1:29-1:37 — Explicit next-video teaser (open loop): "in my next video, I'm going to talk about
    building iOS apps directly from my phone"
- **Open loops:** "will the email research actually work" (opened 0:25, closed 0:53 spreadsheet
  reveal); "will the landing page actually deploy live" (opened 1:03, closed 1:16 live site) — nested
  loops, consistent with the channel's dominant pattern.
- **One-idea-per-video:** yes, "phone-controlled Codex can do real business tasks autonomously," though
  it covers two distinct task types (research + deployment) under that one frame.
- **Pacing:** high, though slightly more talk-heavy/explanatory in the middle third (0:25-0:53 spans a
  wait period) than the purely visual density of Videos 1 and 3.
- **Loop design:** explicit series hook at the close — directly sets up appointment viewing for the
  next video (§3.4.2 mechanism), a more deliberate rewatch/return driver than most videos in the sample.

### 4. Value proposition
- **What the viewer walks away with:** a business-relevant workflow example (automated brand-deal
  research, automated landing-page deployment) beyond pure app-building, widening this channel's
  practical-value range.
- **Practical value class:** copyable workflow (conceptually) + tool discovery + series/appointment hook.
- **Specificity level:** moderate; the "brand deal researcher skill" and "YOLO mode" are named but not
  taught step-by-step in this short.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — moderate-high; automating your own business admin (brand deals) is a relatable
    flex for the creator-economy-adjacent segment of this audience specifically.
  - *Triggers* — moderate; "email/inbox management" is a near-universal frequent-cue task.
  - *Emotion* — calm-competent more than high-arousal-awe — this video reads more like a practical
    business-workflow demo than a spectacle, consistent with its more modest (though still
    above-median) performance.
  - *Public* — low.
  - *Practical Value* — the highest of the top-8 tier on this specific pillar — real business-task
    automation, not just app-building novelty.
  - *Story* — moderate; two sequential mini-demos rather than one arc.
- **Primary emotion + arousal:** competence/calm-useful, lower arousal than Videos 1-3 — directly
  illustrating §2.3's finding that low-arousal content (even when genuinely useful) under-performs
  high-arousal content on relative virality, despite being arguably the single MOST practically useful
  video in the entire 11-video sample.
- **Identity-signaling share motive:** "I automate my business with AI" — professional/entrepreneurial
  identity signal, narrower audience than the broader amazement plays.
- **Save/send trigger:** the strongest save-candidate in the top-8 tier — a viewer managing their own
  inbox/brand deals has genuine reason to bookmark this for later application (§2.7).

### 6. CTA & funnel mechanics
- **Explicit CTA:** next-video teaser (series/appointment mechanic), plus a passing plug for an "agent
  library" resource at a URL the auto-captions render as "chorus.com/skills" — this is very likely an
  ASR mis-transcription of the actual spoken URL and should NOT be treated as a verified real domain.
  `[INFERRED]`/flagged, not presented as fact.
- **Funnel position:** nurture (series continuation) more than top-of-funnel or direct-sale.

### 7. Replicability verdict
- **Extractable template:**
  1. React to a competitor-product release with genuine, non-defensive credit ("arguably better") —
     credibility-building even on a brand-aligned channel.
  2. Demonstrate the tool on a real personal-business task, not just a toy app.
  3. Show the wait time honestly rather than hiding it.
  4. Close with an explicit "next video will cover X" hook to build appointment viewing.
- **Commodity vs unfair advantage:** the workflow demonstrated (email research automation) is broadly
  replicable by any creator with an inbox and the same tools; Riley's edge is a pre-built custom "skill"
  he can casually reference, implying an accumulated toolkit newcomers won't yet have.
- **Difficulty for Tangent: LOW-MED.** The mobile-remote-control demo itself is straightforward; the
  custom-skill callback is a nice-to-have, not a requirement, for replicating the core format.

### 8. Why it won
This is a moderate, not extreme, outlier (2.85x median), and the psychology analysis is instructive:
it is arguably the highest genuine-practical-value video in the entire sample, yet it under-performs the
lower-practical-value, higher-arousal videos ranked above it — direct empirical support for
03_virality_science.md §2.3's core finding that arousal, not just objective usefulness, drives sharing.
Its above-median performance is well explained by solid demo-in-motion execution, real named tools, and
an explicit series hook; its failure to reach the extreme-outlier tier is well explained by its calmer,
more "business-competent" emotional register relative to Videos 1-3's higher-arousal awe/absurdity.

### Sources
- https://www.youtube.com/shorts/3mm-hxVtjkM (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 6 (Rank #6 of 39 — TOP): "vibecode app is insane"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/wrLSsAjR19Q | **Platform:** YouTube Shorts
- **Post date:** 2025-10-30 `[OBSERVED]`, HIGH. **Length:** 118 seconds `[OBSERVED]`, HIGH.
- **Views: 20,963** | **Likes: 700** | **Comments: 20** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 3.34%. **Comment rate:** 0.095%.
- **Rank:** #6 of 39. **1.84x the shorts median.**

### 1. Packaging
- **Title:** "vibecode app is insane" — all-lowercase, casual register, generic superlative ("insane")
  with no specific claim attached — the weakest, least differentiated title in the top-8 tier.
- **Description:** "Building an iOS app From my Phone. / This has never been easier. /
  https://apps.apple.com/us/app/vibecode-ai-app-builder/id6742912146 / Vibecode will win."
  `[OBSERVED]` — contains a direct App Store purchase link, the only such direct link in this sample.
- **Curiosity gap:** low-moderate on the title alone; the description does more curiosity-gap work
  ("never been easier" is a checkable claim).

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"I saw this post on Twitter yesterday.
  Startup idea, Tinder but for guys to find other guys to do cool projects with. So, I'm going to build
  this with AI and get it on the App Store."*
- **Hook taxonomy:** Trend-jacking / reactive-build hook — distinct from the sample's dominant "bold
  claim about a tool" pattern; here the hook is "I'm going to build a specific, already-viral internet
  idea live," borrowing curiosity from a pre-existing viral tweet rather than generating a fresh claim.
- **What the viewer sees:** presumably a phone screen (Vibecode app interface) — not independently
  frame-verified, DATA GAP.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:09 — Hook: reacting to a viral tweet, committing to build it
  - 0:09-0:33 — States the plan/spec verbally (5 project categories, swipe-right submits a video pitch)
  - 0:33-0:56 — Executes: pastes the prompt into the Vibecode app on his phone, notes it "uses Claude
    code"
  - 0:56-1:10 — Fills dead time productively: generates a logo while the app builds (comedic
    placeholder concept: "Abraham Lincoln holding an axe," picks a favorite from 8 generated options)
  - 1:10-1:22 — Places the logo in the app via a follow-up prompt
  - 1:22-1:37 — Reveals the built app, tests the swipe/submit flow with a joke pitch ("Yo Mike, I'm
    trying to build a treehouse with you, bro")
  - 1:37-1:58 — Generates a real App Store icon, submits toward App Store listing, explicitly defers
    backend/user-auth work to "the next video" (open loop)
- **Open loops:** "will the app actually match the tweet's concept" (opened 0:09, closed ~1:22-1:30);
  explicit next-video deferral for backend work (unclosed by design — series hook).
- **One-idea-per-video:** yes, "watch me build a viral tweet's startup idea live, phone-only."
- **Pacing:** high, with an efficient dead-time-filling beat (logo generation while waiting) that other
  videos in the sample don't always include — a small but replicable retention technique.
- **Loop design:** ends mid-build (backend not yet added), explicit series continuation, not a closed
  rewatch loop.

### 4. Value proposition
- **What the viewer walks away with:** proof that a viral internet idea can go from tweet to
  App-Store-submitted app, phone-only, in under 2 minutes of screen time — an aspirational,
  low-barrier-to-entry demonstration.
- **Practical value class:** primarily aspiration/proof-of-capability + direct product funnel
  (Vibecode, with the App Store link in the description).
- **Specificity level:** moderate; the concept/spec is narrated in full, but exact prompt text is
  spoken/summarized, not shown as on-screen text.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — moderate; building something already-viral (not an original idea) borrows
    social currency rather than generating fresh in-the-know status.
  - *Triggers* — low; tied to a specific, dated tweet rather than an evergreen cue.
  - *Emotion* — amusement (the comedic logo/pitch content) rather than awe — a lighter emotional
    register than the top-3 videos.
  - *Public* — the "I saw this on Twitter" framing itself models public social proof driving the
    creator's own interest.
  - *Practical Value* — moderate; the "how to fill dead build-time productively" beat has minor
    transferable value.
  - *Story* — clean but small-scale: react to trend → build → partial reveal → defer rest to next video.
- **Primary emotion + arousal:** amusement, moderate arousal — notably lower-key than the top 5 videos
  above it, consistent with its comparatively modest 1.84x multiple.
- **Identity-signaling share motive:** "I can build viral internet ideas myself" — a fairly broad,
  low-friction identity claim.
- **Save/send trigger:** low-moderate; more watch-and-move-on than reference-worthy.

### 6. CTA & funnel mechanics
- **Explicit CTA:** direct App Store link in the description — the most literal, lowest-ambiguity
  purchase/download funnel mechanic in the entire 11-video sample. `[OBSERVED]`.
- **Comment-bait mechanics:** none observed in-video; the description's "Vibecode will win" is a brand
  slogan/tagline rather than an engagement mechanic.
- **Funnel position:** direct product funnel — the closest thing to a straight-line "watch, then
  download" video in the sample.

### 7. Replicability verdict
- **Extractable template:**
  1. Find an already-viral idea (tweet, meme, comment) and commit to actually building it on camera.
  2. State the spec conversationally before building — sets clear expectations for the payoff.
  3. Fill unavoidable build/wait time with a small parallel task (logo generation) rather than a hard
     cut or dead air.
  4. Test the finished product with a joke/personal example rather than a generic placeholder.
  5. Defer remaining scope explicitly to a next video rather than rushing a complete build into one short.
- **Commodity vs unfair advantage:** highly commodity — reacting to viral tweets is available to any
  creator; Riley's edge is simply having Vibecode itself as an owned tool to demo, making this
  simultaneously content AND a product ad.
- **Difficulty for Tangent: LOW.** Requires only a builder tool and a habit of monitoring viral
  trend-adjacent posts to react to — one of the more accessible formats in the sample.

### 8. Why it won (moderately)
This performed above-median (1.84x) but is the weakest of the top-8 tier, and the packaging analysis
explains a plausible ceiling: the title itself ("vibecode app is insane") is generic and does none of
the curiosity-gap work the stronger top performers' titles do, leaning entirely on the in-video hook and
description to carry interest. The trend-jacking mechanic borrows rather than generates curiosity, and
the emotional register (amusement, not awe) sits at the lower-arousal end of this sample's top tier.
Its above-median floor is well explained by reliable demo-in-motion execution and the productive
dead-time-filling technique, which are transferable regardless of the specific trend being reacted to.

### Sources
- https://www.youtube.com/shorts/wrLSsAjR19Q (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 7 (Rank #7 of 39 — TOP): "OpenAI's New Agent Builder Is Here!"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/3M_ydA_cuMQ | **Platform:** YouTube Shorts
- **Post date:** 2025-10-06 `[OBSERVED]`, HIGH. **Length:** 143 seconds `[OBSERVED]`, HIGH.
- **Views: 18,446** | **Likes: 749** | **Comments: 19** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 4.06%. **Comment rate:** 0.103%.
- **Rank:** #7 of 39. **1.62x the shorts median.**

### 1. Packaging
- **Title:** "OpenAI's New Agent Builder Is Here!" — straightforward news framing with an exclamation
  point for urgency, no comparative or absurd hook.
- **Description:** long, substantive — explains Agent Builder + Apps SDK, teases future content ("I'll
  be making a lot of content on how to actually get your app into ChatGPT very soon"), makes a broader
  industry claim ("traffic to your site will increasingly depend on how it shows up inside AI
  chatbots"). `[OBSERVED]` — this is the most analytically substantive description in the sample,
  reading more like a mini-blog-post than ad copy.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"OpenAI just released this agent builder
  which could kill [n8n] and Zapier."*
- **Hook taxonomy:** Bold claim via competitive-displacement framing ("could kill X and Y") — names two
  specific, recognizable incumbent products as the stakes, a distinct hook mechanic from the rest of the
  sample (most other videos claim a tool is good; this one claims a tool will destroy other tools).
  Transcription note: the auto-caption renders "n8n" as "Nan" — same likely ASR mis-hearing pattern
  flagged in Video 1. `[INFERRED]`.
- **What the viewer sees:** presumably a workflow-builder interface — DATA GAP on exact frame content;
  the transcript's phrasing ("if you go to this link right here, paste it in") suggests screen-recording
  of the actual tool.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:07 — Hook: competitive-displacement claim
  - 0:07-0:38 — Explains Agent Builder mechanics: create a workflow, select model, set reasoning effort,
    attach MCP-server tools
  - 0:38-1:00 — Transitions to a second product: the Apps SDK ("add your software platform to chat
    GPT"), cites the Canva app as a real example already built on it
  - 1:00-1:22 — Narrates (appears to be describing existing footage/screenshots of someone else's demo,
    not a live first-person build — a notably different register from most of the sample): Canva
    generating a poster inside ChatGPT, then a second example (Zillow inside ChatGPT)
  - 1:22-1:52 — Pivots explicitly to his own business: "my company Vibe Code, we could use the apps SDK
    to allow for the following experience" — walks through a hypothetical Vibecode-inside-ChatGPT flow
  - 1:52-2:24 — Closes on a broader strategic point: "millions and soon billions of people are on chat
    GPT... how do you give them an experience... to start using your software?"
- **Open loops:** none strongly closed — this video is structured more as an explainer/analysis piece
  than a demo-and-resolve narrative, a structurally different (and, per its lower relative performance,
  less effective) pattern than the demo-in-motion top performers above it.
- **One-idea-per-video:** borderline — covers TWO distinct OpenAI products (Agent Builder AND Apps SDK)
  under one title, which stretches the "one idea" discipline (§3.2) more than any other top-8 video.
- **Pacing:** moderate — more talk-explainer, less rapid visual-state-change than the demo-heavy top
  performers; likely the least "demo-in-motion" video of the entire top-8 tier.
- **Loop design:** ends on a broad, somewhat abstract strategic question rather than a concrete payoff
  or CTA — a soft, analytical close.

### 4. Value proposition
- **What the viewer walks away with:** conceptual understanding of two new OpenAI products and their
  strategic implications, plus an early look at how Riley is thinking about applying them to his own
  business.
- **Practical value class:** news + strategic analysis — a different value class than the dominant
  "watch AI build something" pattern; closer to industry commentary.
- **Specificity level:** moderate on product mechanics, low on Riley's own hypothetical Vibecode
  application (described, not demonstrated).

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — moderate; being early on two significant OpenAI product launches carries some
    "ahead of the curve" value.
  - *Triggers* — low; time-bound news content.
  - *Emotion* — informational/calm-useful register, the lowest-arousal video in the top-8 tier — closer
    to a briefing than a spectacle.
  - *Public* — the cited real examples (Canva, Zillow) function as third-party social proof.
  - *Practical Value* — moderate-high for viewers who build products themselves (a strategic
    "should I build on this SDK" signal) but low for general viewers.
  - *Story* — weak; this is closer to a structured briefing than a narrative.
- **Primary emotion + arousal:** low-arousal informational interest — directly consistent with
  03_virality_science.md §2.3's finding that lower-arousal content under-performs even when
  substantively valuable, and this video has both the longest runtime-to-payoff-density ratio and the
  lowest outlier multiple of the top-8 tier as a result.
- **Identity-signaling share motive:** "I track platform-strategy shifts in AI" — a narrow,
  business/builder-coded identity claim, smaller audience than the broader amazement-driven videos.
- **Save/send trigger:** genuinely the strongest save-candidate for a specific professional
  audience (people building AI-integrated products) even though its general-audience appeal is lower.

### 6. CTA & funnel mechanics
- **Explicit CTA:** none in-video; the description teases future content ("I'll be making a lot of
  content on how to actually get your app into ChatGPT") — a soft content-pipeline tease rather than an
  action CTA.
- **Funnel position:** thought-leadership/positioning content, indirectly in service of the Vibecode
  brand's product-strategy narrative rather than a direct growth or sales mechanic.

### 7. Replicability verdict
- **Extractable template:**
  1. Frame a new tool via competitive displacement ("could kill X and Y") rather than a standalone
     capability claim.
  2. Cite real, named third-party examples already using the new tool as social proof.
  3. Pivot explicitly to "here's how MY business could use this" to connect news to personal stakes.
- **Commodity vs unfair advantage:** highly commodity as an explainer format — many AI-news channels
  produce this exact content type; Riley's differentiator is having an actual company (Vibecode) to
  credibly apply the news to, which most explainer-only creators lack.
- **Difficulty for Tangent: LOW**, but with a caveat: this format underperforms the channel's own
  demo-in-motion top performers, so while it's easy to produce, it is not the highest-leverage format to
  copy — useful mainly as a lower-effort filler/cadence-maintenance format (see Content Architecture).

### 8. Why it won (modestly)
This is the lowest-outlier video among the top-8 tier (1.62x median) and the STEPPS analysis makes the
reason legible: it is an explainer/analysis piece, not a demo-in-motion piece, and per §2.3 low-arousal
informational content structurally underperforms high-arousal demo content on this channel even when
well-produced and substantively valuable. It clears the channel median comfortably on the strength of
timely news framing, real third-party proof points, and Riley's credible personal stakes in the topic,
but the DELTA between this video and Videos 1-3 is best explained by hook taxonomy and emotional
register, not production quality — a directly useful data point for Tangent: demo-in-motion content
meaningfully outperforms explainer content on this specific channel, even on the same general topic
(AI agent tooling).

### Sources
- https://www.youtube.com/shorts/3M_ydA_cuMQ (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 8 (Rank #8 of 39 — TOP): "Claude Opus Created a Mobile app in one prompt"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/Mq1rijmpzX8 | **Platform:** YouTube Shorts
- **Post date:** 2025-09-09 `[OBSERVED]`, HIGH. **Length:** 72 seconds `[OBSERVED]`, HIGH.
- **Views: 18,175** | **Likes: 655** | **Comments: 24** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 3.60%. **Comment rate:** 0.132%.
- **Rank:** #8 of 39, the bottom edge of the top-8 selection. **1.60x the shorts median.**

### 1. Packaging
- **Title:** "Claude Opus Created a Mobile app in one prompt" — bold-claim + specificity ("one prompt")
  hook, naming the exact model.
- **Description:** "From my phone, using vibecodeapp.com I created an app using @google new
  Nano-Banana API. This app allowed me to use AI to edit my thumbnails. Claude Opus 4.1 and GPT-5 high
  are the 2 best coding models... I'll do a full app store tutorial video very soon." `[OBSERVED]` —
  notably self-referential: the app being demoed edits HIS OWN YouTube thumbnails, tying the demo
  directly to his content-creator identity.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"The best AI coding model in the entire world
  created this app in a single prompt."*
- **Hook taxonomy:** Bold claim, result-first (shows the app already exists before explaining how).
- **What the viewer sees:** presumably the finished thumbnail-editing app already open — DATA GAP on
  exact frame, but transcript pacing (immediately describing app features) supports this.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:05 — Hook + result-first reveal
  - 0:05-0:33 — Narrates the app's own feature set in second person as if giving a live tour: photo
    upload, iterative edit requests (beanie, background gradient/text, icon placement, shirt color,
    background scene, glow effect, sunglasses, border) — an unusually long single-breath list of
    granular edit options, demonstrating depth of customization rather than a single wow-moment
  - 0:33-0:44 — Reveals the exact prompt used to build the whole app, on Claude Opus 4.1
  - 0:44-0:58 — Meta-detail: notes the prompt explicitly asked the agent to search the internet for how
    others implement similar features and incorporate that research — a "the AI does its own research"
    beat, a capability angle not used elsewhere in the sample
  - 0:58-1:12 — Shifts to App Store submission: generate icon, enter Apple developer info, submit
- **Open loops:** minimal explicit loop-and-close structure; this video is closer to a single extended
  feature-list reveal than a nested-loop narrative, which may partly explain its middling (bottom-of-
  top-8) performance relative to the more loop-driven videos above it.
- **One-idea-per-video:** yes, "one prompt built a full-featured app," though the feature list itself
  risks listicle-style attention dilution within a 72-second runtime.
- **Pacing:** moderate; the long feature-enumeration section (0:05-0:33) is more verbally dense than
  visually dynamic relative to other top-tier videos.

### 4. Value proposition
- **What the viewer walks away with:** the actual exact prompt used (higher specificity than most
  videos in the sample, which usually only summarize prompts) plus a self-referential proof point
  (Riley uses his own product for his own content-creation workflow — practicing what he demos).
- **Practical value class:** copyable workflow (the prompt is shown) + tool discovery + light aspiration.
- **Specificity level:** the HIGHEST in the top-8 tier — this is the only video where the "exact prompt"
  claim is followed through with the prompt actually being shown/read, not just referenced.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency*: moderate; "I built a tool for my own YouTube workflow" is a creator-specific flex.
  - *Triggers*: low; time-bound to a specific model/API release.
  - *Emotion*: mild awe at the depth of one-shot customization, but delivered in a fairly flat,
    enumerative register — lower arousal than the visually-escalating top performers.
  - *Public*: low.
  - *Practical Value*: the highest specificity in the sample (actual prompt shown) gives this genuine
    save/reference value for viewers who want to replicate it exactly.
  - *Story*: weak; feature-list format rather than narrative arc.
- **Primary emotion + arousal:** mild awe / competence, moderate-low arousal.
- **Identity-signaling share motive:** "I use AI tools in my actual content-creation pipeline" —
  authenticity/practitioner-credibility signal.
- **Save/send trigger:** the strongest save-candidate on pure specificity grounds in the top-8 tier — an
  exact, reusable prompt is genuinely bookmark-worthy.

### 6. CTA & funnel mechanics
- **Explicit CTA:** none in-video; description teases a future "full app store tutorial video."
- **Funnel position:** product funnel (Vibecode/vibecodeapp.com) + light content-pipeline tease.

### 7. Replicability verdict
- **Extractable template:**
  1. Use the product on a task tied to your OWN visible work (here: thumbnails for this very channel)
     for authenticity and self-referential proof.
  2. Actually show/read the exact prompt used, not just a summary — the single highest-specificity move
     available in this format.
  3. Include a "the AI researched this itself" beat to signal depth beyond a single static prompt.
- **Commodity vs unfair advantage:** the prompt-sharing itself is fully commodity/replicable; the
  self-referential thumbnail-editing framing is a nice authenticity touch specific to being a content
  creator, less directly transferable to non-creator use cases.
- **Difficulty for Tangent: LOW.** Showing an exact prompt costs nothing extra to produce and is a
  straightforward, high-value addition to any similar demo video.

### 8. Why it won (modestly)
The weakest of the top-8 tier by outlier multiple (1.60x), consistent with its comparatively low-arousal,
enumerative structure (a feature list, not an escalating reveal) and its narrower niche framing
(a thumbnail-editing tool specifically useful to other content creators, a smaller addressable audience
than general "build any app" demos). It clears the median via a genuinely strong specificity/practical-
value play (showing the real prompt) and authentic self-referential use, but the delta versus the top-3
videos is well explained by its comparatively flat emotional arc.

### Sources
- https://www.youtube.com/shorts/Mq1rijmpzX8 (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 9 (Rank #20 of 39 — MEDIAN): "Claude Code on the phone, and it builds mobile apps"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/Zdq5nrWB4uc | **Platform:** YouTube Shorts
- **Post date:** 2025-10-28 `[OBSERVED]`, HIGH. **Length:** 108 seconds `[OBSERVED]`, HIGH.
- **Views: 11,363** | **Likes: 249** | **Comments: 14** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 2.19% — the lowest like-rate of the top-9-plus-median tier. **Comment rate:** 0.123%.
- **Rank:** #20 of 39 — this IS the exact channel median by definition (1.00x).

### 1. Packaging
- **Title:** "Claude Code on the phone, and it builds mobile apps" — descriptive/functional, no bold
  claim, no absurdity, no comparative framing — the most generically descriptive title in this entire
  11-video sample.
- **Description:** "This is the vibecode app. Elevenlabs, Nano banana, and OpenAI image-1 built in."
  `[OBSERVED]` — a feature/integration list, not a hook.
- **Curiosity gap:** low — the title states what happens rather than implying a gap to close, a direct
  contrast to every top-8 video's title.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"So in this app I created an AI powered voice
  notes app and all I did was add a simple API..."*
- **Hook taxonomy:** Flat feature-tour opening — NOT a bold claim, NOT in-medias-res drama, NOT a
  curiosity-gap question. This is the single clearest structural difference between this median video
  and the top-8 tier: every top-8 video opens with some form of claim, reaction, or immediate visual
  payoff; this one opens with a plain declarative sentence describing what was already done.
  `[OBSERVED]` — directly checkable against 03_virality_science.md checklist item 1 ("does the video
  deliver a visible payoff, promise, or unresolved gap within the first second") — this hook arguably
  fails that checklist item, or at best satisfies it weakly.
- **What the viewer sees:** presumably the Vibecode app interface already mid-tour — DATA GAP on exact
  frame.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:10 — Flat opening: "I created an AI-powered voice notes app... added a simple API... select
    from all these different APIs... image generation, data, audio, etc."
  - 0:10-0:32 — Demonstrates voice recording, generates a matching sound effect within the app
  - 0:32-0:52 — Shows AI summarization of the voice note, generates audio output
  - 0:52-1:10 — Uses "clawed code" [likely ASR mis-hearing of "Claude Code"] to select a generated
    voice line and add it to the build prompt for an onboarding flow
  - 1:10-1:43 — Shows the onboarding voiceover playing live in the app, tours the generated image assets
  - 1:43-1:48 (transcript ends here at 1:48, video runs to 1:48 per available caption data) — shows
    selecting a specific placement area for a generated asset within the app UI
- **Open loops:** minimal — this video is structured as a sequential feature tour (voice → summary →
  onboarding → images → placement), each beat self-contained rather than opening a suspenseful question
  that a later beat resolves. This is the weakest loop-structure of any video in the 11-video sample.
- **One-idea-per-video:** borderline-listicle — "here are several AI features in this app," without a
  single unifying claim beyond "this app has many AI features," which is weaker framing than the top-8
  tier's consistently singular claims.
- **Pacing:** moderate-high visually (genuine feature diversity: voice, audio, image, UI placement) but
  the lack of a driving question means the pacing services a tour, not a mystery.
- **Loop design:** ends mid-task (placing an asset), no closing beat, no CTA, no callback to the opening.

### 4. Value proposition
- **What the viewer walks away with:** a broad sense of the Vibecode app's feature depth (voice,
  image, audio APIs all built in) — genuinely informative about product capability.
- **Practical value class:** tool discovery / product tour.
- **Specificity level:** moderate — real named integrations (ElevenLabs, Nano Banana, OpenAI image-1
  per the description) but no exact prompts shown in the transcript excerpt available.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — low; a straightforward product tour carries little "I'm ahead of the curve"
    charge.
  - *Triggers* — low.
  - *Emotion* — the flattest emotional register in the sample; competence-signaling at best, no awe
    spike, no comedic beat, no error-recovery trust moment.
  - *Public* — none observed.
  - *Practical Value* — moderate; useful for someone specifically evaluating Vibecode as a tool, low for
    a general swipe-feed viewer with no prior product interest.
  - *Story* — essentially none; sequential feature list.
- **Primary emotion + arousal:** low-arousal, informational-neutral — squarely the "share-unfavorable"
  register per Berger & Milkman (§2.3), and this video's exact-median performance is a clean natural
  experiment confirming that finding: same general topic and production quality tier as the top-8 set,
  same channel/audience, same product being demoed, but a measurably flatter hook and emotional arc,
  landing at precisely median rather than outlier performance.
- **Identity-signaling share motive:** weak; nothing distinctly shareable/flex-worthy is offered.
- **Save/send trigger:** low-moderate; a product-feature tour has some reference value but no specific
  "send to person X" moment.

### 6. CTA & funnel mechanics
- **Explicit CTA:** none observed. **Funnel position:** implicit product demo (Vibecode) with no
  explicit ask.

### 7. Replicability verdict
- **Extractable template (what NOT to do, as much as what to do):**
  1. Do not open with a flat declarative "here's what I made" sentence — even genuinely good work
     underperforms without SOME claim, reaction, or visual gap in the first line.
  2. A sequential feature tour needs either a unifying question ("can this replace 3 separate apps?")
     or an emotional beat (comedy, error-recovery, surprise) to avoid reading as a flat product demo.
  3. Product depth alone (multiple real integrations) is necessary but not sufficient for outlier
     performance on this channel.
- **Commodity vs unfair advantage:** the product itself (Vibecode with multiple AI APIs built in) is a
  real asset, but the VIDEO fails to translate that asset into a compelling hook — a packaging failure,
  not a substance failure.
- **Difficulty for Tangent: LOW to replicate the mistake; the lesson itself (hooks matter more than
  substance for Shorts distribution) is the valuable, easily-internalized takeaway.**

### 8. Why it landed at exactly median (not higher, not lower)
This video is a clean, almost textbook illustration of the sample's central finding: identical general
subject matter (Vibecode app demo), identical production register (screen-recording, spoken narration,
real product depth) to several top-8 videos, but a measurably weaker hook (no bold claim, no in-medias-
res drama, no visible payoff in the first line) and a flatter emotional arc (no awe spike, no comedy, no
trust-building error-recovery beat). It does not fail outright — it has real content and reasonable
engagement rates — but it also does not clear the bar that distinguishes an above-median from an
outlier video on this channel. This is arguably the single most useful video in the entire sample for
Tangent's purposes: it isolates the hook/emotion variable while holding topic, production quality, and
product constant.

### Sources
- https://www.youtube.com/shorts/Zdq5nrWB4uc (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 10 (Rank #35 of 39, i.e. 5th-lowest — FLOP, on-formula): "Vibecoding the 'Swifties' App with Backend From my Phone"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/hX7D1pMOEzw | **Platform:** YouTube Shorts
- **Post date:** 2025-11-03 `[OBSERVED]`, HIGH. **Length:** 168 seconds — the longest video in the
  entire 11-video sample. `[OBSERVED]`, HIGH.
- **Views: 3,950** | **Likes: 126** | **Comments: 9** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 3.19% (respectable — higher than several top-8 videos). **Comment rate:** 0.228% (the
  SECOND-HIGHEST comment rate in the entire 11-video sample, behind only Video 1's 0.408%).
- **Rank:** 5th-lowest of 39 sampled shorts. **0.348x the shorts median** — roughly a third of median
  performance. Excluded from the 5-most-recent recency window, so eligible as a genuine flop per
  protocol.

### 1. Packaging
- **Title:** "Vibecoding the 'Swifties' App with Backend From my Phone" — descriptive, names the
  specific fan-culture target ("Swifties" = Taylor Swift fans) and a technical detail (backend, phone).
- **Description:** notably includes a long, generic "Vibecode Key Words" paragraph stuffed with
  competitor tool names (Replit, v0, Cursor, Bolt AI) in a way that reads as SEO/algorithm-bait copy
  rather than organic caption writing: *"That is simple a fact with the vibecode app which can vibecode
  ANYTHING ai. If you don't want to destroy, rork or ruin your apps... you will use the vibecode app."*
  `[OBSERVED]` — this is a genuinely unusual, lower-quality piece of copy relative to the rest of the
  sample; `[INFERRED]` this may be templated/reused boilerplate across multiple videos rather than
  bespoke per-video writing, given its generic, keyword-stuffed character, though this specific
  inference was not cross-checked against other video descriptions for exact-text reuse.
- **Curiosity gap:** the title itself is fine (comparable in quality to several top-8 titles); the
  packaging problem, if any, is not obviously in the title.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"Taylor Swift is a billionaire, and while
  she's done an amazing job monetizing her fans, I think she could do an even better job."*
- **Hook taxonomy:** Opinion/business-analysis hook — NOT a demo-in-motion, NOT a bold claim about an AI
  tool, NOT in-medias-res on the actual build. This is a fundamental hook/content mismatch: the opening
  promises a Taylor-Swift-business-commentary video, and the actual payload (an AI app-building demo) is
  a full topic pivot that doesn't arrive until roughly 20+ seconds in. Per §1.2.1/§2.1.3, Shorts viewers
  decide to keep watching within roughly one second based on what's promised — a viewer drawn in by
  "Taylor Swift billionaire" commentary and then redirected to an app-building tutorial is being served
  a bait-and-switch relative to their own selection criteria, even though both halves are individually
  fine content.
- **What the viewer sees:** presumably a talking-head or stat-graphic opening (not independently
  frame-verified) before transitioning to the phone/app screen-recording — DATA GAP on exact visual,
  but the spoken content strongly implies this structure.
- **Unsourced statistics red flag:** the hook cites specific-sounding numbers — "over 104 million
  Swifties," "42% of US households," "$50,000 per year or less" — with no source cited on-screen or
  verbally. `[OBSERVED]` that these numbers are stated; `[INFERRED]`, and explicitly flagged per this
  dossier's own no-fabrication standard, that these read as exactly the kind of specific-sounding,
  uncited statistic that 03_virality_science.md warns analysts to distrust when found in the wild (see
  the doc's own "UNVERIFIED STAT" category) — this dossier does NOT verify or cite these numbers as
  fact, and notes their uncited presence in Riley's own video as a possible authenticity/credibility
  weak point that may have suppressed engagement independent of the hook-mismatch issue.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:25 — Taylor Swift business-opinion hook + uncited stats + pivot to "she needs a Swifties app"
  - 0:25-0:45 — Spec statement: authentication, database, storage, two features (events, feed)
  - 0:45-1:06 — Executes build via Vibecode app on phone; fills wait time generating an app icon
    ("blonde woman, mid-40s, guitar, 3D render icon" — 8 variations)
  - 1:06-1:24 — App is done; signs in, creates an event, attempts a joke about sponsor pricing
    ("$1.25 million... discount for Pfizer, only 250,000") — an attempted comedy beat that reads as
    somewhat random/non-sequitur (Pfizer has no established connection to the Swifties premise)
  - 1:24-2:00 — Cross-device database test: signs in as a second profile ("Travis Kelsey"), creates a
    second event, confirms both show up on both devices/profiles — a genuine technical-proof beat,
    structurally similar to Video 3's cross-device demo
  - 2:00-2:29 — Generates final app icon, submits to App Store
- **Open loops:** the cross-device database test (opened 1:24, closed 1:55-2:00) is a well-executed
  loop, technically comparable to the top-performing Video 3's cross-device proof — the STRUCTURE later
  in the video is genuinely competent.
- **One-idea-per-video:** the video actually contains TWO ideas loosely stitched together (Taylor
  Swift business commentary + Vibecode app demo) without a strong throughline connecting them beyond
  "wouldn't this be useful for Swift" — a clearer §3.2 one-idea-discipline violation than any other
  video in the sample.
- **Pacing:** reasonable once the build begins (~0:25 onward), comparable to top-tier videos; the
  problem is concentrated in the first 25 seconds, not the whole runtime.
- **Loop design:** ends on submission (open/forward-looking), similar to several top-8 videos.

### 4. Value proposition
- **What the viewer walks away with:** (once past the hook) a legitimate demo of backend/database/
  multi-user functionality in Vibecode — arguably showing MORE technical depth (real multi-device data
  sync) than several higher-performing videos.
- **Practical value class:** tool discovery + light business-strategy commentary (the Swift-monetization
  angle).
- **Specificity level:** moderate, comparable to the top-8 tier once the actual build begins.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — the Taylor Swift hook likely APPEALS to social currency in isolation (pop-culture
    commentary is inherently shareable) but the payload doesn't deliver on that specific promise, which
    may undercut the sharing motive it establishes.
  - *Triggers* — Taylor Swift is a very high-frequency cultural trigger, arguably higher-frequency than
    any cue used in the top-8 tier — this makes the hook choice interesting rather than simply "bad";
    the trigger itself is strong, but attached to the wrong payload.
  - *Emotion* — the celebrity-business-commentary opening aims for a different emotional register
    (cultural/financial curiosity) than the awe/amusement register the actual payload delivers,
    creating tonal whiplash rather than a coherent arc.
  - *Public* — low.
  - *Practical Value* — genuinely present (backend/multi-user demo) but arrives too late relative to
    what the hook promised.
  - *Story* — the two-part structure (commentary → build) is closer to two separate videos stitched
    together than one coherent narrative.
- **Primary emotion + arousal:** mixed/incoherent — likely the core issue, per §2.1.1's requirement that
  the opening gap be a SPECIFIC, closeable gap; here the opened gap (will Taylor Swift actually get an
  app, or is this cultural commentary) is answered by a pivot to generic tool demo, which may read as
  the gap never actually closing on its own terms.
- **Identity-signaling share motive:** unclear/split — the video doesn't cleanly serve either a
  "I'm into pop culture business analysis" sharer OR a "I'm into AI app-building" sharer, potentially
  falling into a gap between two audiences rather than serving either fully.
- **Save/send trigger:** the SECOND-HIGHEST comment rate in the entire sample (0.228%) suggests that
  viewers who DID watch through engaged actively — the problem is plausibly reach/discovery, not
  content quality among those who saw it.

### 6. CTA & funnel mechanics
- **Explicit CTA:** none observed. **Funnel position:** product demo (Vibecode), same as several
  higher-performing videos in the sample.

### 7. Replicability verdict
- **Extractable lesson (what to avoid):**
  1. Do not open with a hook from a different content category (celebrity/business commentary) than the
     actual payload (tool demo) delivers — even if both halves are independently well-executed, per
     §1.2.1 the viewer decides to stay based on the FIRST promise, and a mismatched payload risks high
     early swipe-away regardless of downstream quality.
  2. Uncited statistics in a hook are a credibility risk worth flagging even in a fast-moving demo video
     — this dossier could not verify the Swiftie statistics cited and neither, presumably, could most
     viewers in the first few seconds, which may read as filler rather than substance.
  3. A joke/comedy beat should connect to the video's own established premise (the Pfizer sponsorship
     joke has no built-in connection to Taylor Swift or the app being built, unlike Video 1's
     "dance around the room" gag, which stays inside its own established frame).
- **Difficulty for Tangent: N/A (this is a failure-mode lesson, not a template to copy).**

### 8. Why it lost — and the delta vs the top tier
The single most load-bearing reason this video underperforms is **hook/payload mismatch**: it opens in
the wrong content category (celebrity business commentary) for what it actually delivers (an AI app
demo), which per the channel's own dominant winning pattern (bold claim OR demo-in-motion, delivered
IMMEDIATELY and consistently with the rest of the video) breaks the format viewers have been trained to
expect from this channel. This is corroborated by the engagement-rate data: like rate (3.19%) and
especially comment rate (0.228%, second-highest in the whole sample) are both COMPETITIVE with or
better than several top-8 videos — meaning the content itself, once watched, performs reasonably. The
failure is concentrated in REACH, not RECEPTION, strongly implicating the first-few-seconds hook
mismatch (and the resulting poor "viewed vs. swiped away" ratio, per YouTube's own primary Shorts
ranking signal, §1.2.1) as the specific mechanism, rather than a generalized quality problem. **Delta
vs. top tier:** the top-8 videos are hook-payload coherent within the first sentence; this video is not,
despite comparable build-execution quality once the payload actually starts.

### Sources
- https://www.youtube.com/shorts/hX7D1pMOEzw (yt-dlp metadata + auto-captions, 2026-07-25)

---

## VIDEO 11 (Rank #37 of 39, i.e. 3rd-lowest — FLOP, off-formula): "Review Code with Code Rabbit Pro"

### 0. Identity & stats
- **URL:** https://www.youtube.com/shorts/tN42JpEwAro | **Platform:** YouTube Shorts
- **Post date:** 2025-04-09 `[OBSERVED]`, HIGH. **Length:** 54 seconds — the shortest video in the
  11-video sample. `[OBSERVED]`, HIGH.
- **Views: 3,630** | **Likes: 90** | **Comments: 2** — `[OBSERVED]`, 2026-07-25 fetch, HIGH.
- **Like rate:** 2.48%. **Comment rate: 0.055%** — the LOWEST of the entire 11-video sample, by a wide
  margin (next-lowest is 9GWxBG9f564's 0.076%).
- **Rank:** 3rd-lowest of 39 sampled shorts — the true floor of this channel's shorts performance in the
  sample (excluding the 5 most-recent, still-maturing videos). **0.319x the shorts median.**

### 1. Packaging
- **Title:** "Review Code with Code Rabbit Pro" — names a third-party product directly in the title,
  reading as an ad from the title alone.
- **Description:** "Start reviewing code with AI that actually knows your repo. Get 1 free month of
  Code Rabbit pro with code 'RILEY'. Link in bio" `[OBSERVED]` — explicit affiliate/discount-code
  sponsor copy, the clearest sponsored-content marker in the entire sample.
- **Curiosity gap:** essentially none — the title states the exact product and its function; there is no
  promise or gap to close, only a direct product name.

### 2. Hook (0-3s)
- **Verbatim opening line** `[OBSERVED via transcript]`: *"Everyone is now vibe coding because AI has
  quickly caught up to the average developer. People who have never written a single line of code are
  building apps with AI. But some vibe coders are actually not making sure their code is secure."*
- **Hook taxonomy:** Attempted "nobody talks about X" / warning hook (fear/anxiety framing about
  security) — this is a legitimate, well-established hook type per §3.1, and the opening two sentences
  are genuinely reasonable, on-topic for the channel, and consistent with the channel's dominant subject
  matter (vibe coding). The hook ITSELF is not obviously the failure point, unlike Video 10.
- **What the viewer sees:** DATA GAP — no screen-recording is described anywhere in the transcript for
  this entire video; the language throughout ("that's why I use Code Rabbit... My favorite feature...")
  is consistent with a straight-to-camera or voiceover-over-static-graphics read, not a live demo.
  `[INFERRED]` from the complete absence of any deictic screen-reference language ("look at this,"
  "here," "boom," "let's go") that saturates every other video in this sample — this is the only video
  in the 11-video set with no such language at all.

### 3. Structure & retention engineering
- **Beat map** `[OBSERVED via transcript]`:
  - 0:00-0:14 — Hook: vibe-coding-security-risk framing
  - 0:14-0:21 — Product introduction: "that's why I use Code Rabbit to catch mistakes before they
    happen"
  - 0:21-0:37 — Feature-benefit list: "clean, efficient, shippable... one-click commitable fixes...
    automated error detection"
  - 0:37-0:48 — Integration list: "GitHub, GitLab, Bitbucket, and Azure DevOps with no setup headaches"
  - 0:48-0:55 — Close: free-for-open-source mention + "link in bio" CTA
- **Open loops:** none — this is a linear feature-benefit list with no suspense, no build-in-progress,
  no before/after reveal, no error-and-recovery beat. It is the only video in the sample with literally
  zero narrative or demonstrative structure — a pure spoken advertisement.
- **One-idea-per-video:** technically yes (one product, one message) but delivered as an undifferentiated
  feature list rather than a single memorable claim or demo.
- **Pacing:** by construction, "pacing" as defined by visual-state-change (§3.3.2) cannot be assessed
  from the transcript because no visual builds or changes are described at all — `[INFERRED]` this is
  very likely low visual pacing (static or B-roll-only), a direct contrast to every other video in the
  sample, all of which are screen-recording-heavy.
- **Loop design:** no rewatch hook, no callback, ends on a standard CTA.

### 4. Value proposition
- **What the viewer walks away with:** awareness of a product name and a discount code — essentially
  zero demonstrated capability, no proof, no live example of the tool catching a real bug.
- **Practical value class:** pure advertisement — the weakest practical-value class available (no
  workflow shown, no tool discovery beyond the name, no news).
- **Specificity level:** low — generic feature-benefit language ("clean, efficient, shippable") without
  a single concrete example.

### 5. Psychology scoring
- **STEPPS scan:**
  - *Social Currency* — essentially none; sharing a sponsor read confers no in-the-know status.
  - *Triggers* — the security-anxiety opening does tap a real, recurring concern among vibe coders, but
    it is not followed through with any specific, memorable trigger-reinforcing content.
  - *Emotion* — the hook aims for mild anxiety (§2.3's anxiety/urgency register, which IS high-arousal
    and normally share-favorable) but the anxiety is never resolved with a concrete demonstration (no
    "here's an actual bug it caught"), leaving the emotional payoff hollow relative to the setup.
  - *Public* — none.
  - *Practical Value* — nominal only; a product name and generic claims, no demonstrated proof.
  - *Story* — none; pure feature list.
- **Primary emotion + arousal:** attempted anxiety/urgency (a legitimate high-arousal register per
  §2.3) but undermined by the complete absence of a payoff or demonstration — the emotional setup and
  the structural delivery are mismatched, similar in kind (though different in mechanism) to Video 10's
  hook/payload mismatch.
- **Identity-signaling share motive:** none meaningfully present.
- **Save/send trigger:** very low — a discount code has some minor bookmark value but nothing else in
  the video is reference-worthy.

### 6. CTA & funnel mechanics
- **Explicit CTA:** "check the link in my bio to learn more about Code Rabbit," paired with a stated
  personal discount code ("RILEY") — classic affiliate-marketing CTA mechanics, cleanly compliant with
  disclosure norms (the sponsor relationship is made explicit, not hidden) but structurally this is a
  pure top-of-funnel-for-a-THIRD-PARTY product, unlike every other CTA in the sample which routes back
  to Riley's own Vibecode product or his own long-form content.
- **Funnel position:** third-party affiliate/sponsor funnel — the only video in the 11-video sample that
  is NOT part of the Vibecode-or-own-content funnel described in Section A.

### 7. Replicability verdict
- **Extractable lesson (what to avoid):** sponsored-content reads that abandon the channel's own
  dominant demo-in-motion format for a straight feature-benefit list appear to structurally underperform
  on this channel, independent of hook quality — the opening two sentences here are genuinely
  reasonable by this dossier's own hook-taxonomy standards, yet the video still lands at the near-floor
  of the sample, strongly suggesting the ABSENCE of any screen-recorded demo (not the hook) is the
  primary driver of underperformance.
- **Difficulty for Tangent: N/A (failure-mode lesson).** If Tangent ever takes a sponsorship, this
  video's data suggests: keep the demo-in-motion format even inside a sponsored read (show the tool
  actually doing something on screen) rather than defaulting to a spoken feature list.

### 8. Why it lost — and the delta vs. the top tier
This is the true floor of the sample (0.319x median, lowest comment rate of all 11 videos at 0.055%),
and unlike Video 10, the failure here is NOT primarily attributable to the hook (which is reasonable and
on-topic) but to the **complete absence of the channel's core winning mechanic: demo-in-motion.** Every
top-8 video, the median video, and even the other flop (Video 10) contain substantial screen-recorded,
visibly-building demonstrations; this video appears to contain none. Combined with its sponsor-read
register (feature-list delivery, third-party product, no personal build story, no error-recovery trust
beat, no absurdist humor), this video is missing nearly every mechanic this dossier has identified as
load-bearing across the top-8 tier. **Delta vs. top tier:** the top-8 videos consistently show something
being built/changed/fixed in real time on screen; this video tells rather than shows, and its
near-floor performance — despite a competent hook — is the clearest single piece of evidence in this
sample that demo-in-motion, not hook quality alone, is this channel's primary performance driver.

### Sources
- https://www.youtube.com/shorts/tN42JpEwAro (yt-dlp metadata + auto-captions, 2026-07-25)

---

## C. Top-vs-Flop Delta

**In two sentences:** The delta between Riley Brown's top and flop shorts is driven far more by
**hook/payload coherence and the presence (or absence) of a real, screen-recorded build-in-motion
demonstration** than by production polish, topic relevance, or even engagement quality among viewers who
actually watch — both flops have like-rates competitive with the top tier (3.19% and 2.48% vs. a top-8
range of 2.22-4.71%), and Video 10 even out-comments 6 of the 8 top performers by rate, showing these
are **reach/discovery failures rooted in the first few seconds, not reception failures**. Video 10 fails
because its hook (Taylor Swift business commentary) promises a different video than it delivers (an app
demo); Video 11 fails because it abandons the demo-in-motion format entirely for a spoken feature list,
despite having a perfectly reasonable hook — together they isolate hook-coherence and demo-presence as
two INDEPENDENT necessary conditions for this channel's outlier performance, since each flop is missing
only one of the two and neither is enough alone to reach even median performance.

**Supporting detail:**
- **Engagement-rate evidence for "reach problem, not reception problem":** Video 10's comment rate
  (0.228%) is the 2nd-highest in the entire 11-video sample; only the extreme-outlier Video 1 (0.408%,
  driven by an explicit comment-gate CTA) beats it. This directly contradicts a naive "the content is
  bad" explanation and supports a "the content is fine but under-distributed due to a poor hook" reading.
- **The median video (Video 9) is the cleanest natural experiment:** same topic (Vibecode demo), same
  production register, same channel/audience as several top-8 videos, but a flat declarative hook with
  no bold claim, no visible payoff in the first line, and no emotional arc — it lands at exactly the
  channel median, neither an outlier nor a flop, illustrating that hook/emotion quality operates on a
  continuum, not a binary.
- **What does NOT explain the delta:** topic (both flops are on-topic — AI/vibe-coding — same as every
  top performer); runtime (Video 10 at 168s is the longest in the sample yet flops, while Video 2 at
  163s is a top performer — length alone is not predictive); presence of a real product/company behind
  the content (both flops and most top performers promote Vibecode or Riley's own content).

---

## D. Content Architecture: Key vs. Filler, Series Formats, What Sustains Between Hits

`[REPORTED]`, primarily sourced from the Creator Science podcast #303 show notes
(podcast.creatorscience.com/riley-brown/), fetched via WebFetch 2026-07-25, MED confidence throughout
this section unless otherwise tagged — this is podcast-page-summary level, not a verified primary
transcript listen-through or an independently audited production log.

### Cadence and volume
- **Current stated cadence: 4-5 high-quality educational shorts/week + 2 additional trending-topic
  shorts/week (~6-7/week total).** Riley describes this as a deliberate SHIFT from an earlier,
  higher-volume "quantity" phase to a "quality" phase — an explicit strategic pivot, not a constant
  practice over the channel's whole history. `[REPORTED]`, MED.
- Cross-checked against this dossier's own 39-video shorts sample: the observed posting-date gaps are
  uneven (dense clusters, e.g. 6 videos within Oct 28-Nov 18 2025, alongside multi-month gaps, e.g.
  Jun 18-Aug 12 2025 has only 1 video visible), consistent with either genuine cadence variation over
  time or — more likely, given the "weekly" classification from developereducators.com — with this
  39-video sample being a curated/shelf-limited subset that does not capture the full continuous
  posting record (see Method log, data gaps). `[INFERRED]` that the true cadence is more consistent
  than the visible sample suggests.

### Key content ("hits") vs. filler
Based on this dossier's own 11-video analysis, three tiers emerge:
1. **Tentpole demo-in-motion videos (the "key" content):** bold-claim or result-first hook + a real,
   screen-recorded, visibly-progressing build, ideally with an error-and-recovery or escalating-reveal
   beat and a comedic or awe-inducing moment. These are the videos that reach the 3x-16x-median outlier
   tier (Videos 1-5 in this sample). `[OBSERVED]`, derived from this dossier's own analysis.
2. **Reliable mid-tier demo/news content:** solid demo-in-motion or product-tour execution without a
   strong hook or emotional arc — clears the median comfortably but doesn't spike (Videos 6-9).
   `[OBSERVED]`.
3. **Filler/cadence-maintenance content:** news-explainer pieces (Video 7) and sponsor reads
   (Video 11) that exist primarily to maintain posting cadence and/or fulfill sponsor obligations
   rather than to drive growth — these sustain channel presence between hits but do not themselves
   generate outlier reach. `[OBSERVED]`/`[INFERRED]` synthesis.
- The 4-5 "high-quality" + 2 "trending-topic" weekly split described in the podcast source maps
  reasonably well onto this tiering: the "high-quality" bucket likely corresponds to tentpole
  demo-in-motion content (tier 1), and the "trending-topic" bucket likely corresponds to faster-turn
  news-reaction content (tier 2/3, e.g. Video 7's Agent Builder explainer, Video 4's and Video 5's
  same-week-as-launch model reactions). `[INFERRED]`, reasonable mapping but not directly confirmed by
  the source.

### Series formats
- **"Part N" series** (e.g. "Openclaw Blender part 2," Video 3) — an explicit appointment-viewing
  mechanic per §3.4.2, though this dossier could not independently verify part 1's performance
  (DATA GAP) to confirm whether the series structure measurably lifts part 2+ versus a standalone video.
- **Next-video verbal teasers** without a numbered title (e.g. Video 5's "in my next video, I'm going to
  talk about building iOS apps directly from my phone," Video 6's implicit "next video" deferral of
  backend work) — a lighter-weight series mechanic than numbered parts, used more frequently in this
  sample than explicit numbering.
- **Model-reaction "micro-series"**: multiple videos in the sample react to sequential model/product
  releases (Claude 4.5 Sonnet, Codex Mobile, OpenAI Agent Builder, GPT-5.5) using a consistent
  build-and-ship structural template each time — functionally a recurring FORMAT even without explicit
  numbering or franchise branding, which is itself a form of format-ownership/mere-exposure compounding
  per §2.4.2 (viewers who've seen 2-3 of these learn to expect and recognize the pattern: react → build
  → error/reveal → ship).

### What sustains between hits
- **Production infrastructure, not just individual creative choices:** two overseas editing agencies
  (a 10-hour-turnaround option and a 3-day-turnaround higher-polish option) plus a dedicated thumbnail
  designer (former Matt Wolf designer, 1-day turnaround), at a stated **$800-1,200 cost per long-form
  episode edit**. `[REPORTED]`, MED. This is a real production operation, not a solo-creator ad hoc
  workflow, and is a meaningful resourcing signal for Tangent to calibrate expectations against.
- **Cross-platform repurposing at scale:** the single highest-leverage sustaining mechanic described is
  reposting the best-performing video of the week across **7 X/Twitter accounts (200K+ combined
  followers)** on a standing weekly cadence — described as tripling Vibecode's revenue in two months.
  `[REPORTED]`, MED. This means a single strong "hit" (like Video 1 or 2 in this sample) is not a
  one-platform event but gets systematically re-distributed, extending its effective reach and
  business impact well beyond its native YouTube view count.
- **Retention/personality gimmicks:** described use of physical props (plastic pointer fingers, giant
  pencils) to boost retention in some content `[REPORTED]`, MED — not directly observed in this
  dossier's 11 transcripts (transcript-only analysis cannot confirm visual gimmick usage; DATA GAP on
  which specific videos use these props).
- **Explicit anti-AI-script philosophy:** Riley is quoted describing AI-written scripts as
  counterproductive to voice/authenticity ("the more you use AI for writing your scripts, the more
  you're going to sound like AI... sounding like AI is suicide"), while using AI for research/learning.
  `[REPORTED]`, MED. This is consistent with this dossier's own observation that the strongest videos in
  the sample (1, 2, 3) have unscripted-feeling, reactive verbal delivery ("Oh my god," "No way") rather
  than polished ad-copy phrasing.
- **Screen-share-specific formula, stated directly by Riley:** a 1-minute hook explaining what the
  viewer will learn, followed by immediate value delivery via screen demonstration, using simple/cheap
  tools (Tella or Descript, a ~$100 wireless mic), with an explicit recommendation to build to 50K
  subscribers before over-optimizing production. `[REPORTED]`, MED. Riley considers this format "the
  single biggest content opportunity right now" per the same source.

---

## E. Method Log

**What was searched/fetched:**
1. `yt-dlp --flat-playlist --playlist-items 1:150` and separately `1:300` against
   `https://www.youtube.com/@rileybrownai/shorts` (2026-07-25) — both returned the identical 39 videos,
   establishing this as a stable but non-exhaustive shelf-limited sample (see data gaps below).
2. Per-video full metadata (`--print` for id/date/views/likes/comments/duration/title) pulled for all
   39 sampled shorts via individual `yt-dlp` calls against `youtube.com/shorts/<id>`, `--sleep-requests
   0.75`, 2026-07-25 — used to compute the exact median, top/median ratio, and select the 11-video
   deep-dive list (top 8 + median + 2 flops, excluding the 5 most-recent from flop eligibility per
   protocol).
3. Full `%(description)s` pulled for the 11 selected videos.
4. Auto-generated English captions (`--write-auto-subs --sub-langs en.* --sub-format vtt`) pulled for
   all 11 selected videos, then read in full and manually de-duplicated (VTT auto-captions repeat lines
   across overlapping timestamp windows by design) to produce verbatim hooks and timestamped beat maps.
5. `yt-dlp --flat-playlist --playlist-items 1:25` against `https://www.youtube.com/@rileybrownai/videos`
   (2026-07-25) for long-form context/cadence comparison.
6. `WebFetch` attempted on `youtube.com/@rileybrownai/about` and the channel's `/about` URL twice — both
   FAILED to return substantive bio/link data (YouTube's About tab is JS-rendered and WebFetch's
   static-HTML fetch only returned footer/navigation boilerplate). Logged as a genuine data gap, not
   papered over. Channel subscriber count (264,000) was instead obtained directly and reliably via
   yt-dlp's `%(channel_follower_count)s` field.
7. `WebSearch` used for: Vibecode funding/founder details (getlatka.com), channel-stats aggregation
   (developereducators.com), Instagram/TikTok follower cross-checks, and the Creator Science podcast
   appearance.
8. `WebFetch` used successfully on getlatka.com/companies/vibecode and
   podcast.creatorscience.com/riley-brown/ (both returned substantive, checkable content) and on ONE
   specific Instagram reel URL found via WebSearch (instagram.com/reel/DHTiRJHJwjK/), which
   unexpectedly returned apparent engagement metadata (likes/comments/date/caption) despite Instagram's
   general logged-out wall.
9. A calibration test was run: WebFetch was pointed at a deliberately fake/non-existent Instagram reel
   URL to check whether the tool fabricates plausible-looking numbers when it can't access real data.
   It correctly reported it could not extract any metadata from the fake URL (returning only base64
   image placeholders), which supports (but does not fully prove) that the real reel's returned numbers
   were genuinely scraped rather than hallucinated. This is noted explicitly because IG data is held to
   MED-confidence-at-best per QC_PROTOCOL's known constraints regardless.

**What failed / data-access constraints hit (logged per QC_PROTOCOL, not papered over):**
- **YouTube rate-limiting mid-session:** multiple `yt-dlp` calls hit HTTP 429 "Too Many Requests" and
  "Sign in to confirm you're not a bot" errors partway through transcript downloads, requiring three
  rounds of retries with increasing `--sleep-requests` values (0.75s → 1.5-2s) and eventually switching
  `--extractor-args` to `youtube:player_client=android` to complete all 11 transcript downloads
  successfully. This appears attributable in part to OTHER concurrent research-pipeline sessions running
  `yt-dlp` against YouTube from the same environment in parallel (observed via `ps aux` during
  troubleshooting: parallel scratch directories for other creators — nateherk, futurepedia,
  curiousrefuge, liamottley — were actively running yt-dlp at the same time), not solely this dossier's
  own request volume.
- **39-video shorts ceiling:** the `/shorts` tab flat-playlist extraction consistently returned exactly
  39 videos regardless of requested range (tested at both 1:150 and 1:300), while the channel's implied
  total video count (202-204 per two independent sources) minus its ~25 visible long-form videos implies
  a materially larger true shorts catalog exists. This 39-video set should be read as YouTube's
  shelf-exposed sample (likely some blend of recency and evergreen popularity), NOT as the complete
  shorts history, and the computed median (11,363 views) is the median OF THIS SAMPLE, not a verified
  population median. This caveat is carried through every median-relative statistic in this dossier.
- **YouTube channel About tab:** inaccessible to WebFetch (JS-rendered SPA); worked around via yt-dlp's
  structured metadata fields instead, which covered subscriber count but not bio text or listed links.
- **Instagram:** per QC_PROTOCOL's documented baseline, generally blocked to logged-out access; direct
  WebFetch of the @realrileybrown profile page returned no usable bio/follower data. One specific reel
  URL (found via WebSearch, not by browsing the profile directly) did return apparent metadata via
  WebFetch — flagged MED confidence per protocol, not independently re-verified by a second method.
  Follower count (328K) came from a WebSearch result snippet, also MED confidence, not a live profile
  view.
- **TikTok:** not directly fetched; follower count (636.7K) and the "20M-view first video" origin-story
  claim both come from WebSearch result summaries only, MED confidence, `[REPORTED]`, no primary TikTok
  page or press article was independently opened and read in full.
- **"chorus.com/skills" and "NAND agent" / "Nan and Zapier":** auto-caption transcription artifacts
  flagged throughout the post-mortems as likely ASR mis-hearings (most plausibly "n8n," a real
  workflow-automation tool, in both cases) rather than verified real terms — presented as `[INFERRED]`,
  never as confirmed fact.
- **Video frame content (text overlays, exact on-screen UI):** this dossier is transcript-and-metadata-
  based; no video frames were visually inspected (no browser-based video playback was used). Every
  section 1 "text overlay on frame 1" and similar visual-only claims are marked DATA GAP or `[INFERRED]`
  from audio-transcript context rather than presented as directly observed.
- **Part-1 of "Openclaw Blender"** and other series predecessors referenced in-video were not
  independently located or pulled — DATA GAP, noted in Video 3's section D architecture discussion.

**Sourcing summary for the Method log itself:** every fetch/search command described above was actually
executed in this session (scratch working directory:
`/private/tmp/claude-501/-Users-sparsh-Documents-Projects-Tangent/3f21975f-6df6-481e-9a72-4d4c86b4bb54/scratchpad/yt_rileybrown/`),
not simulated or assumed.
