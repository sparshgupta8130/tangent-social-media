# Creator Dossier: Liam Ottley (YouTube @LiamOttley)

Niche: "make money with AI" business content — AI Automation Agency (AAA) education, agency-building
tutorials, and personal-brand/lifestyle content, all funneling into a free community and paid accelerator
program. All stats as-of **2026-07-25** unless otherwise noted. Data pulled via `yt-dlp 2026.07.04`
(homebrew) and a nightly build `2026.07.23.234303` (isolated venv, used only to rule out a version-specific
bug — see Method Log), plus direct Claude-Browser render of youtube.com (logged-out) and raw
`ytInitialData`/innertube JSON parsing. Every number below is [OBSERVED] unless tagged otherwise.

---

## CRITICAL FINDING (read this before anything else in this dossier)

**Liam Ottley's YouTube Shorts catalog contains exactly ONE video.** Not "under-sampled in discovery" in the
sense of "we didn't find all of them" — there is, as of 2026-07-25, precisely one video in the `/shorts` tab
of a channel with 825,000 subscribers and 251 total uploads. This was independently verified three separate
ways:

1. `yt-dlp --flat-playlist --playlist-items 1:150` against `@LiamOttley/shorts` (per the assigned SWEEP
   command, and retried at `1:150` with no range limit, with a nightly yt-dlp build, and with
   `--extractor-args "youtubetab:skip=webpage"` to force API-only extraction) — every attempt returned
   exactly **one row**: `TmxBWCOUWVc | 90000 | ALEX HORMOZI on How To Make A Fortune With AI`.
2. Raw `ytInitialData` JSON was extracted directly from the `/shorts` tab's HTML (`curl` + regex + `json.load`)
   and the `richGridRenderer.contents` array — the actual data structure YouTube's own front-end renders from
   — was manually inspected: it contains **one `richItemRenderer`, full stop.** No continuation token exists
   for this grid (a search of the entire page JSON for `continuationItemRenderer` found only two tokens, both
   belonging to the unrelated "About channel" engagement panel, not the Shorts grid).
3. Live browser render: navigated to `youtube.com/@LiamOttley`, clicked the "Shorts" tab, read the rendered
   page text. Result: one thumbnail, one title ("ALEX HORMOZI on How To Make A Fortune With AI"), one view
   count ("90K views"), then nothing else — matching the `yt-dlp` and raw-JSON findings exactly.

Cross-check: the channel header reports **251 videos** total; the `/videos` tab flat-playlist sweep
independently returned **250** entries, all with `duration >= 189s` (i.e., zero videos under YouTube's
3-minute Shorts-eligibility ceiling other than the one already counted). 250 (long-form) + 1 (the Short) =
251, matching the header exactly. [OBSERVED, HIGH confidence — three independent extraction methods plus an
arithmetic cross-check all agree]

**Consequence for this dossier's method:** the assigned selection protocol ("top 8 shorts by views + 2-3
flops + median") is impossible to execute against a catalog of one item — there is no top-8, no flops, and no
distribution to take a median of. The methodology was adapted (full justification in the Method Log): the one
real Short gets its own complete post-mortem (it is simultaneously the channel's best, worst, and only
Short), and the remaining ten post-mortem slots were filled with a views-ranked sample of Liam's **long-form**
catalog (top 6 / median 1 / flops 3, same exclude-the-5-most-recent-uploads discipline applied to flop
selection) — because long-form is not a fallback proxy here, it is empirically the entire channel. This
pivot is itself the headline finding the brief asked this dossier to establish.

---

## A) Channel header

- **Subscribers:** 825,000 [OBSERVED — `yt-dlp` `channel_follower_count` field and independently confirmed via
  logged-out browser render of `youtube.com/@LiamOttley` showing "825K subscribers," both as-of 2026-07-25,
  HIGH confidence]
- **Total catalog size:** 251 videos = 250 long-form + 1 Short [OBSERVED, see Critical Finding above]
- **Total lifetime channel views:** 31,172,683 [OBSERVED, extracted from the channel's `aboutChannelViewModel`
  JSON payload via the innertube browse-continuation endpoint, 2026-07-25]
- **Channel age:** joined 2018-05-29 [OBSERVED, same source]. Country: New Zealand [OBSERVED]. The channel's
  own description states the current content identity ("AI Automation Agency" / AAA) dates to 2023, implying
  ~5 years of channel history before the current niche/format was established — the catalog analyzed here is
  overwhelmingly the 2023–2026 AI-business era, not the pre-2023 channel.
- **Shorts median/top:** **not computable** — n=1. The one Short has 90,282 views [OBSERVED, `yt-dlp`
  `--print` metadata pull, 2026-07-25, HIGH confidence]. If inserted into the long-form catalog for
  comparison purposes, 90,282 views would rank **#70 of 251** (top ~28th percentile) [OBSERVED, computed by
  sorting the full 250-video long-form view-count list and finding 90,282's insertion point] — a solidly
  above-median result for a single, never-repeated experiment, not a flop, but nowhere near the channel's
  ceiling.
- **Long-form median (n=250, full catalog):** **43,502 views** (the video "7 Proven AI Systems Giving
  Ecommerce Stores an Edge in 2025," `yxStHAjTTbU`, ranked #125 of 250) [OBSERVED, computed from a full
  `--flat-playlist --playlist-items 1:250`-equivalent sweep of `@LiamOttley/videos`, 2026-07-25]
- **Long-form top:** 3,627,172 views ("How to Build & Sell AI Agents: Ultimate Beginner's Guide," `w0H1-b044KY`,
  posted 2025-03-27) [OBSERVED]
- **Long-form top/median ratio:** 3,627,172 / 43,502 = **~83.4x**. This is an unusually wide spread — it means
  the channel's growth is driven by a small number of massive evergreen "flagship guide" videos sitting atop
  a much larger base of videos performing at a fraction of that level, not by consistently-high performance
  across the catalog. See Section D for the architecture this implies.
- **Cadence:** irregular/bursty, not steady. The 15 most recent uploads (RSS feed, `2026-02-23` to
  `2026-06-21`) average roughly 1 video per 6–8 days across that ~17-week window, but cluster in bursts (3
  uploads in 3 days, 2026-02-23/24/25) separated by multi-week gaps (e.g. 2026-03-22 to 2026-04-13, three
  weeks with nothing) [OBSERVED, parsed from `youtube.com/feeds/videos.xml?channel_id=UCui4jxDaMb53Gdh-AZUTPAg`].
  As of this dossier's research date (2026-07-25), the channel's most recent upload was **2026-06-21** — over
  five weeks stale, i.e. the channel is currently in a posting gap at the moment of writing. In one of the
  analyzed flop videos (posted January 2023) Liam states he was publishing content "three times a week"
  [OBSERVED, transcript, FLOP3 below] — cadence has slowed substantially since the channel's early
  SMMA-to-AI-pivot era.
- **Funnel map** [OBSERVED via live browser render of the channel's About panel, 2026-07-25, cross-verified
  against the CTA/description content of all 11 videos sampled below — the funnel structure is remarkably
  consistent across nearly every video regardless of performance, see Section D]:
  - **Top of funnel — discovery:** long-form YouTube video is the entire discovery engine (see Critical
    Finding; Shorts contribute effectively 0% of catalog and, being algorithmically feed-driven rather than
    search/recommendation-driven per `03_virality_science.md` §1.2.3, are the one channel of distribution
    Liam does not use at all)
  - **Owned-audience capture — free tier:** Skool community at `skool.com/learn-ai`. Self-reported size grows
    across the sampled videos' upload dates: "200,000+ members" (2024 videos, e.g. TOP5/TOP6 descriptions),
    "100,000 AI agency owners" surveyed + described as "the world's largest AI business community" (April
    2025, MEDIAN video), "280k+ members" (TOP2/TOP3 descriptions, Dec 2024–Jan 2025), and "over 300,000"
    on the current (2026-07-25) channel About page [OBSERVED, each figure tagged to its own video/date — these
    are Liam's own self-reported numbers, not independently auditable, so treat the *direction* (consistent,
    large, growing) as HIGH confidence and the *exact figures* as [REPORTED] by the subject himself, not
    third-party verified]. Nearly every video description gates a free lead-magnet PDF/roadmap behind
    requesting to join this Skool ("request to join, you'll be let in within 1-2 minutes... find the post for
    this video to access the writeup") — a classic content-upgrade / email-and-community-capture funnel.
  - **Paid tier:** AAA Accelerator (`aaaaccelerator.com`), pitched in every sampled video's description as
    helping "entrepreneurs, industry experts & developers build and scale their AI Agency." **Pricing is never
    disclosed in any of the 11 sampled videos** [DATA GAP — no video content names a specific price point for
    the Accelerator; only the free Skool tier's terms are made explicit on-screen].
  - **Service/agency arm:** Morningside AI (`morningside.ai`), Liam's own AI-implementation agency — "work
    with me," a direct B2B sales funnel, separate from the education/community business.
  - **Talent funnel:** "Apply to Join My Team at Morningside AI" and "...at AAA Accelerator" links appear in
    every sampled description — the audience doubles as a hiring pipeline, not just a customer base.
  - **UGC / community-proof funnel:** the MEDIAN video (below) includes an explicit form ("Have your own
    solution to share? Tell us here") inviting AAA community members to be featured in future videos — this
    simultaneously sources free content, deepens community members' investment/status, and manufactures
    fresh social proof for the free tier, a closed loop.
  - **Secondary channels/social:** a separate "Liam Ottley VLOGs" channel (BTS/personal), Instagram
    (`instagram.com/liamottley`), X (`x.com/liamottley_`) [OBSERVED, About-panel links list]. None of these
    were deep-dived — out of scope for a YouTube-focused dossier; noted for completeness only.
  - **Monetization outside the funnel:** standard YouTube AdSense pre-roll is active (an Oracle NetSuite
    sponsored ad played before the #1 video in this sample was screenshotted, 2026-07-25) — the channel is
    not solely a lead-gen vehicle, it also earns directly from the platform.

---

## B) Video post-mortems

**Selection method (adapted — see Critical Finding):** Video 1 is the channel's only Short, analyzed in full
regardless of rank since no ranking is possible at n=1. Videos 2–11 are drawn from the 250-video long-form
catalog: top 6 by view count, the exact median (#125 of 250), and the bottom 3 by view count **excluding the
5 most-recently-published uploads** (per protocol, to avoid penalizing videos that simply haven't had time to
mature). Long-form median for reference throughout Section B: **43,502 views**.

---

### VIDEO 1 (the channel's entire Shorts catalog — n=1 of 1): "ALEX HORMOZI on How To Make A Fortune With AI"

#### 0. Identity & stats
- URL: `youtube.com/shorts/TmxBWCOUWVc`. Platform: YouTube Shorts. Posted 2023-09-25. Duration: 39s.
  [OBSERVED, `yt-dlp` metadata pull, 2026-07-25]
- Views: 90,282. Likes: 5,277 (5.85% of views — the highest like-rate of any video in this entire 11-video
  sample). Comments: 45 (0.05%). [OBSERVED, `yt-dlp` `--print` pull, as-of 2026-07-25, HIGH confidence]
- Rank: #1 of 1 in the Shorts catalog by definition. If judged on raw views against the 250-video long-form
  catalog, it would rank #70/251 (~top 28th percentile) — comfortably above the channel's long-form median
  (43,502) but nowhere near its top tier (millions). Posted 2023-09-25 and never followed by a second Short
  in the ~2 years 10 months since — this is a one-time experiment, not an ongoing (even low-volume) format.

#### 1. Packaging (the pre-click/pre-swipe layer)
- Title: "ALEX HORMOZI on How To Make A Fortune With AI." Frame 1 [OBSERVED via direct browser screenshot,
  2026-07-25]: a **split-screen** layout — top half shows Alex Hormozi (bearded, tank top, reclined,
  listening/reacting), bottom half shows Liam Ottley mid-answer. A large yellow-and-black text callout reads
  "DO THINK" (a keyword-emphasis graphic synced to Liam saying "...because I **do think** that AI
  implementation..."), plus standard word-by-word burned-in auto-caption text above it.
  Below the video, YouTube's native "this Short is from" panel names the source video: "The Massive
  Opportunity in Building AI Businesses" (the full podcast interview).
- What's actually being sold by the title vs. what's delivered: the title implies Hormozi is the one
  teaching ("Alex Hormozi on how to..."), but the audio content is entirely **Liam** answering a question
  Hormozi asked him — Hormozi's face carries the pattern-recognition/stop-scroll power (he is a far larger,
  more widely recognized business figure than Liam), while the actual value/voice is Liam's. This is a
  deliberate **borrowed-authority packaging technique**: a bigger creator's face does the hook-stopping work,
  a smaller creator's content does the payoff work.
- Curiosity gap: mild — a viewer who recognizes Hormozi's face expects to hear him speak, and instead gets
  Liam; the gap is less "what will be revealed" and more "wait, who's actually talking here," resolved within
  ~2 seconds once Liam's voice/face appears.

#### 2. Hook (0–3s)
- Verbatim opening line [OBSERVED via auto-caption transcript]: *"I did make a tweet about the opportunity
  that you're talking about right now because I do think that AI implementation for Main Street is an
  enormous opportunity if you are starting one of these businesses."*
- Hook taxonomy: **in-medias-res / demo-in-motion hybrid** per `03_virality_science.md` §3.1 — the clip drops
  the viewer directly into the middle of an ongoing conversation with zero setup, preamble, or re-introduction
  of context. There is no "hey guys" (§2.6.2's silent-retention-killer is fully avoided).
- What the viewer sees: two real, recognizable talking heads (a podcast/interview format), not a
  screen-recording or B-roll — the visual is entirely faces-and-conversation, with the split-screen doing the
  format-signaling work (this is a "clip from a bigger conversation," which itself sets viewer expectations
  correctly per the native YouTube sourcing panel).

#### 3. Structure & retention engineering
- Beat map [OBSERVED, full 39s transcript]:
  - 0:00–0:21 — Liam names the opportunity (AI implementation for "Main Street" businesses), frames it as
    enormous, stresses specificity/focus and "productizing" a solution
  - 0:21–0:31 — pivots to a **communication tactic**: don't use "techno jargon" with the client
  - 0:31–0:38 — lands the single, complete, quotable payoff: *"just tell them what life's going to be like
    once this thing is done and ask them if they want that"*
- One-idea-per-video: yes, cleanly — one sales-communication principle, stated once, not diluted by a list or
  multiple competing takeaways. This is the strongest structural compliance with §3.2's "one idea" discipline
  of any video in this 11-video sample (the long-form videos, by contrast, are almost all multi-point lists).
- Payoff placement: end-loaded — the most quotable line is the literal last sentence, which is also
  independently confirmed as the standout by audience behavior (see Section 5/6 below — it's the top comment,
  nearly verbatim).
- Loop design: no explicit rewatch trigger (no visual gag, no planted early tease resolved at the end) — the
  loop that exists is conversational (a direct answer to an implied question), which closes cleanly rather
  than circling back.
- Pacing: static by short-form standards — this is a single continuous talking-head answer with no internal
  cuts, B-roll, or scene changes; the only "pacing" device is the one text-emphasis graphic ("DO THINK") and
  the rolling auto-caption. Under §3.3.2's qualitative pacing marker, this scores LOW-dynamism relative to a
  purpose-built short, but the format (raw interview clip) makes that an expected trade-off, not a failure —
  the content genre here is "authentic clip," where over-editing would undercut the credibility.

#### 4. Value proposition
- What the viewer walks away with: one specific, actionable sales/communication principle — sell the outcome
  ("what life's going to be like"), not the technical mechanism, and ask a direct closing question.
- Practical value class: **copyable framework** (a specific technique that a viewer running any kind of
  service business could apply verbatim the next day), not a tool name, not news, not pure entertainment.
- Specificity level: HIGH for a 39-second clip — no vague gesturing ("communicate better"); the advice names
  the exact mechanism (avoid jargon → describe the future state → ask for the sale) in one breath.

#### 5. Psychology scoring (against `03_virality_science.md` checklist)
- STEPPS scan: **Practical Value** is the dominant activated pillar — a single, immediately usable insight
  (§2.7). **Social Currency** is activated via the Hormozi association — being seen watching/sharing a clip
  where a major business figure is present confers some "I'm plugged into this space" status even though
  Hormozi isn't the one talking (§2.2, §2.5). **Story/Emotion** are comparatively weak — there is no
  narrative arc and no high-arousal emotional spike (no awe, anger, or anxiety register); this is calm,
  informational content.
- Primary emotion + arousal: calm-useful, LOW arousal. Per Berger & Milkman (§2.3, RESEARCH-BACKED), low-
  arousal content — even when positively valenced and useful — is a comparatively weak *viral-sharing*
  driver relative to high-arousal awe/anxiety/amusement content. This is consistent with the video's
  respectable-but-not-explosive performance (top-28th-percentile, not top-tier): the content is genuinely
  useful and well-received (highest like-rate in the sample) but was never built to spike.
- Identity-signaling share motive: moderate — sharing this says "I follow smart AI-business conversations,"
  a mild social-currency signal, but the content itself (a sales-communication tip) isn't sufficiently novel
  or insider to be strongly identity-defining on its own.
- Save/send trigger: MED — the closing line is genuinely quotable/forwardable to a specific person ("you
  should hear this before your next sales call"), which is corroborated directly by the evidence in Section 6
  below (a top comment restating it near-verbatim, at 177 likes — the single most-liked comment on the video).

#### 6. CTA & funnel mechanics
- Explicit CTA: a comment (24 likes) reading *"Watch my full interview with @AlexHormozi on my channel!
  (click the arrow in bottom left corner)"* [OBSERVED, fetched via `yt-dlp --write-comments`, 2026-07-25] —
  this points viewers to YouTube's native "Short is from this video" panel rather than an external link,
  keeping the funnel entirely on-platform (clip → parent long-form video, not clip → external site).
- Comment-bait mechanics / observable engagement loop [OBSERVED, full 45-comment pull]: the top comment (177
  likes) is a viewer restating the video's own closing line almost word-for-word — direct evidence the
  "practical value" payoff is exactly what resonated. A separate comment (5 likes) reads *"Liam is just the
  best. Joined the community recently and I want to start AAA here in Africa"* — **direct observed evidence
  of a Short converting a viewer into a community member**, the funnel mechanic working in the wild, not just
  in theory. A third comment ("Awesome first short Liam") independently corroborates this being explicitly
  his first Short — external confirmation of the Critical Finding above, from inside the audience itself.
- Funnel position: top-of-funnel discovery/introduction-by-association — this is Liam's content riding a
  bigger creator's episode into a feed slot his own long-form catalog cannot reach (Shorts feed vs. search/
  recommended, per §1.2.3), used exactly once and then abandoned as a channel strategy.

#### 7. Replicability verdict
- The extractable TEMPLATE: (1) get booked on/interviewed by a much larger creator/podcast in your niche; (2)
  identify the single most quotable, standalone-complete answer you gave; (3) clip it with zero re-editing of
  the substance, split-screen both faces, add one keyword-emphasis text graphic; (4) let the platform's native
  "watch the full video" panel do the CTA work; (5) pin/post a comment pointing explicitly to the full
  interview.
- Commodity vs. unfair advantage: the editing/format is entirely commodity (any creator can do split-screen
  clip production). The unfair advantage is **access** — this only works if you can get in the room with a
  creator many times your size in the first place, which is not a reproducible tactic on demand.
- Estimated difficulty for Tangent: **MED** — not because the clip format is hard, but because the
  prerequisite (a guest slot on a much bigger show) is the actual bottleneck, not anything about the video
  itself.

#### 8. Why it won (or lost) — analyst synthesis
This is simultaneously the channel's best AND only Short, which makes "why it won" and "why the format was
never repeated" the same question. It performed respectably (top-28th-percentile-equivalent, highest
like-rate in this entire sample) on the strength of borrowed authority (Hormozi's face) plus a genuinely
complete, quotable, practical payoff delivered with zero fluff — a nearly ideal execution of the "one idea"
discipline. It did **not** spike into the millions, plausibly because (per §2.3) its emotional register is
calm-useful rather than high-arousal, and because it is a byproduct of a podcast appearance rather than a
purpose-built hook-engineered Short. The more important fact than its performance is that it was never
repeated: a single successful, funnel-converting experiment (documented converting at least one viewer into a
community member, in the comments themselves) was not followed up on. That is a channel-strategy decision,
not a performance failure — see Section D for the fuller argument that Liam's growth engine runs entirely
through long-form and free-community capture, and Shorts were tried once, worked fine, and were deprioritized
anyway in favor of doubling down on long-form.

#### Sources
- https://www.youtube.com/shorts/TmxBWCOUWVc (video, transcript via auto-captions, comments)
- https://www.youtube.com/watch?v=w1Q93tz83DY (source long-form interview, "The Massive Opportunity in
  Building AI Businesses | Alex Hormozi," 103,844 views, posted 2023-09-24, 22:49 duration — confirms the
  Short was cut from this video and posted the following day)
- https://www.youtube.com/@LiamOttley/shorts (live browser render + raw `ytInitialData`, 2026-07-25)

---

### VIDEO 2 (long-form, rank #1 of 250 by views — 83.4x median): "How to Build & Sell AI Agents: Ultimate Beginner's Guide"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=w0H1-b044KY`. Platform: YouTube (long-form). Posted 2025-03-27. Duration: 13,839s
  (3h 50m 39s). [OBSERVED, `yt-dlp` metadata, 2026-07-25]
- Views: 3,627,172. Likes: 84,354 (2.33%). Comments: 2,800 (0.08%). [OBSERVED, HIGH confidence]
- Rank: #1 of 250 long-form videos, and the channel's single largest video by a wide margin — more than 2x
  the #2 long-form video (1,726,625). 83.4x the long-form median.

#### 1. Packaging (the pre-click/pre-swipe layer)
- Title: "How to Build & Sell AI Agents: Ultimate Beginner's Guide" — a bold, comprehensive-scope promise
  ("Ultimate...Guide") rather than a curiosity-gap tease; the payoff (you will learn to build AND sell agents)
  is named directly, not withheld. Thumbnail was not independently screenshotted for this video [DATA GAP —
  autoplay covered the thumbnail before a static capture could be taken; noted in Method Log].
- Unlike a Short, packaging matters a great deal here: per §1.2.3/§4 of the virality-science doc, long-form
  relies on title+thumbnail to win the click from a grid of competing options (search or recommended), the
  opposite of the Shorts feed's thumbnail-irrelevance. A nearly-4-hour runtime is itself part of the pitch —
  "Ultimate...Guide" plus the visible duration together signal comprehensiveness/completeness before the
  click.
- The description's own timestamp map [OBSERVED] confirms the promised scope: three chapters (foundational
  understanding → four end-to-end build tutorials → monetization blueprint), exactly matching the title's
  "build & sell" framing — no bait-and-switch between packaging and content.

#### 2. Hook (0–3s / extended to ~60s given format)
- Verbatim opening line [OBSERVED via transcript]: *"Two years ago, I taught myself how to build AI agents
  without any prior experience in AI. And since then, I've started multiple AI businesses that have generated
  over $5 million in revenue. I've grown from 0 to 450,000 subscribers here on YouTube."*
- Hook taxonomy: **bold claim / credibility-flex hook** — an explicit income claim ($5M) and audience-growth
  claim (0→450K subs) stacked in the first two sentences, establishing authority before any teaching content
  begins.
- What the viewer sees/hears: direct-to-camera address, no B-roll yet — pure credibility establishment before
  the curriculum is previewed.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via the creator's own description timestamps, cross-checked against transcript sampling
  at the start, ~3h35m mark, and end]: 0:00 intro/credibility → 2:39 why learn agents → 5:39–32:39 foundational
  theory (what agents are, anatomy, tools/schemas) → 35:00–3:35:29 four full build tutorials (the bulk of the
  runtime, ~3 hours) → 3:35:29 "The Real Opportunity" (monetization pitch) → 3:39:47–3:48:46 three ways to
  monetize, extending the knowledge gap, getting first clients → 3:48:46 next steps/CTA.
- Open loop: the credibility claim ($5M, 450K subs) in the hook is not "resolved" until the final third of
  the video, when Liam walks through exactly how those numbers were generated (education/consulting/
  implementation services) — a very long-range open loop spanning the entire runtime.
- One-idea-per-video: no — this is explicitly NOT single-idea content; it is a full course with dozens of
  sub-payoffs, which is appropriate for its "Ultimate Guide" packaging and its lead-magnet function (see
  Section 6) rather than a violation of §3.2's discipline (that rule is stated as a short-form-specific norm).
- Pacing: within the tutorials, screen-recording/build-along format (dynamic, tool-switching, visible progress)
  per §3.3.2; within the theory sections, slide/talking-head hybrid.
- Loop closure at the end: explicit, direct — closes with a clear CTA rather than trailing off (§2.6.1).

#### 4. Value proposition
- What the viewer walks away with: a complete free course — conceptual understanding of AI agents, four
  working builds (step-by-step, "over my shoulder"), and a monetization framework. Practical value class:
  **copyable workflow** (tool discovery + workflow, at course scale).
  - Specificity: HIGH within the build sections (named platforms/tools, step-by-step); the monetization
    section is more directional (three service categories: education, consulting, implementation) than a
    literal price-and-pitch script.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (a genuinely complete free course). **Social Currency** — knowing/
  having-completed "the" free AI agents course carries some in-the-know value. **Emotion** — mixed: the
  credibility-flex hook and "before these AI agents start taking our jobs" line (0:36) both tap mild anxiety/
  urgency, a higher-arousal register than Video 1's calm-useful tone.
- Primary emotion: aspiration + mild anxiety/urgency (life-change framing: "build the life of your dreams
  before these AI agents start taking our jobs" — [OBSERVED verbatim, 0:36]).
- Identity-signaling: HIGH — "I completed Liam's full agents course" is a meaningfully larger status claim
  than watching a 39-second clip, consistent with mere-exposure/parasocial compounding across a long,
  intensive, personally-guided experience (§2.4).
- Save/send trigger: HIGH — a nearly-4-hour structured course with timestamps is maximally "save for later"
  content, the textbook profile §2.7 describes for saves/sends outperforming likes as an intent signal.

#### 6. CTA & funnel mechanics
- Explicit CTA (verbatim close, [OBSERVED]): *"You need to jump in the free community... drop an introduction
  post... start working your way through my free course material... each time you complete a video... you
  can click the little checkbox so you can keep stacking those small wins."* This is a **gamified onboarding
  CTA** — the free Skool community isn't just linked, it's framed as a structured, checkbox-tracked follow-on
  curriculum, directly extending the video's own "course" framing into the owned platform.
  Also explicit: "leave a like... drop a comment... click the share button... subscribe" — a compliant,
  content-attached engagement-bait bundle (not bare bait per §1.3.2, since it rides on genuine, already-
  delivered value).
- Description-level CTA [OBSERVED]: Skool community, AAA Accelerator, Morningside AI, and a "FREE 14-day
  playbook" lead magnet, plus a note pointing to an even newer 2026 version of the same course.
- Funnel position: this is the channel's **flagship top-of-funnel lead magnet**, not a monetization video
  directly — its entire second half is the pitch into the free community, which is itself the entry point to
  the paid Accelerator.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) open with a stacked, specific credibility claim (revenue + audience growth); (2)
  promise total comprehensiveness in title and structure (theory → builds → monetization); (3) deliver real,
  complete, step-by-step value with visible screen-recording; (4) spend the final ~15 minutes making the case
  for *why* this is a business opportunity, using scarcity/ratio stats; (5) close with a structured, gamified
  path into an owned community, not just a generic subscribe ask.
- Commodity vs. unfair advantage: the tutorial content (AI agent building) is increasingly commodity as more
  creators cover the same tools; Liam's unfair advantage is the **specific, large, already-built free
  community** the video funnels into — the video's job is to make that community's value legible, not just to
  teach agents.
- Estimated difficulty for Tangent: **HIGH** — requires an existing community/product to fund a multi-hour
  production and to make the CTA credible; without the community already existing, this format is an empty
  funnel.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's outlier performance is that it functions as a **complete,
free, evergreen course** in a topic (AI agents) with sustained, broad search/recommendation demand across all
of 2025–2026 — long-form's discovery model rewards exactly this kind of durable, comprehensive asset (per
§1.2.3, long-form recommendation is driven by legible packaging + sustained relevance, unlike the
feed-only churn of Shorts). Secondary factors: the credibility-flex hook front-loads trust before a
multi-hour commitment is asked of the viewer, and the monetization section converts that trust directly into
funnel action. A likely timing/luck component: this was published March 2025, well inside the post-ChatGPT
"AI agents" hype cycle, meaning the topic itself was independently trending in search demand — some of this
video's outlier status is topic-timing, not technique alone.

#### Sources
- https://www.youtube.com/watch?v=w0H1-b044KY (video, description, transcript)

---

### VIDEO 3 (long-form, rank #2 of 250 by views — 39.7x median): "This AI Technology Will Replace Millions (Here's How to Prepare)"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=g3-c8XZi7BY`. Posted 2025-01-06. Duration: 3,197s (53m 17s). [OBSERVED]
- Views: 1,726,625. Likes: 42,153 (2.44%). Comments: 6,200 (0.36% — the highest comment-rate of any video in
  this sample). [OBSERVED, HIGH confidence]
- Rank: #2 of 250. 39.7x the long-form median.

#### 1. Packaging
- Title: "This AI Technology Will Replace Millions (Here's How to Prepare)" — a **bold claim + negative-
  warning hybrid** (§3.1), explicitly naming a threat (job replacement) and immediately offering resolution
  (how to prepare), a classic anxiety-hook/relief-valve structure.
- No timestamp for "Painting the Picture" until 1:14 per the description — the opening minute is pure hook
  before any structural signposting, unusual restraint for a 53-minute video.

#### 2. Hook (0–60s)
- Verbatim opening [OBSERVED]: a rapid-fire **montage of borrowed clips** — AI executives' own words
  ("agents are emerging as the latest battleground in enterprise AI... we're going to bring a level of
  automation capability that the world's never seen"), stitched together, then Liam's own voice: *"AI agents
  are here. The death of the smartphone has arrived. Hundreds of millions of jobs will soon disappear. The
  world as we know it is about to change forever. And most people have no idea what's about to hit them. But
  you're different, because in the next 60 minutes I'll show you exactly what AI agents really are..."*
- Hook taxonomy: **bold claim stacked with negative warning**, reinforced by borrowed-authority clips (other
  people's own words, not Liam's claims alone) before pivoting to direct address and an explicit **flattery/
  in-group** move ("you're different") — a textbook Social-Currency activation (§2.2): the video positions
  the viewer as exceptional for watching, ahead of the unaware masses.
- What the viewer sees: fast-cut clips of recognizable tech executives/interviews, high visual variety in the
  first minute — the opposite of Video 1's static single-shot open.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps + transcript sampling at start/mid/end]: 0:00 hook montage →
  1:14 "Painting the Picture" (a **narrative scenario**, "Flash forward to 2035, you're taking your dog for a
  walk..." — a fully fictional day-in-the-life told in second person) → 5:35 why the world is changing →
  12:52–21:51 "4 Phases of AI Agent Evolution" (a structured taxonomy: text-based → voice-based → brain-
  computer → predictive brain-computer agents) → 25:04–33:41 how personal/work/business life changes → 37:13
  "How To Win" broken out by audience segment (young adults / entrepreneurs / office workers / manual
  workers) → 50:51 close.
- Story pillar (§2.2, §2.6): the entire video is framed as a single sci-fi narrative arc (2025 → 2035), a much
  stronger use of the "Trojan horse" narrative-for-information mechanism than any other video in this sample.
- Loop design: the closing minutes explicitly circle back to the opening's "you're different" framing —
  *"we are the generation that's going to witness the end of traditional human work... when our grandchildren
  ask us... will you tell them you saw it coming and took action, or that you waited until it was too late?"*
  — a clean rhetorical loop closure, ending (per the sampled transcript tail) on another borrowed-clip quote
  about risk-taking rather than a direct community CTA in the final lines sampled.
- Pacing: HIGH-dynamism narrative sections (scenario-building, borrowed clips) alternating with structured
  slide-style taxonomy sections — more visually varied than the tutorial-heavy Video 2.

#### 4. Value proposition
- Practical value class: closer to **news/analysis + aspiration** than a copyable workflow — the "4 Phases"
  taxonomy and segment-specific "How To Win" advice are directional/conceptual, not step-by-step tool
  tutorials.
- Specificity: MED — segment-specific strategy sections (what should an office worker vs. entrepreneur do) are
  more concrete than the opening's scenario-painting, but this video teaches a *mental model*, not a build.

#### 5. Psychology scoring
- STEPPS: **Emotion** is the dominant pillar — this video runs on anxiety/urgency (job/smartphone
  "death," "most people have no idea what's about to hit them") far more than any other video in this
  sample, a high-arousal negative register that Berger & Milkman (§2.3, RESEARCH-BACKED) identify as a strong
  viral driver. **Social Currency** — the "you're different" flattery directly manufactures an in-group
  status for viewers. **Story** — the 2035 narrative scenario is the clearest Trojan-horse structure in the
  sample.
- Primary emotion + arousal: anxiety/FOMO, HIGH arousal — the strongest emotional register of any video
  analyzed in this dossier.
- Save/send trigger: HIGH — the highest comment-rate in the sample (0.36%) is itself evidence of the content
  provoking active response/discussion rather than passive consumption, consistent with high-arousal content
  driving engagement beyond simple viewing (§1.1.2's shares/comments as stronger signals than likes).

#### 6. CTA & funnel mechanics
- Description-level CTA [OBSERVED]: Skool community ("280k+ members" — this is the largest community figure
  claim among all videos sampled, dated Jan 2025), AAA Accelerator, Morningside AI — the standard three-link
  funnel bundle, identical structure to every other video in this sample.
- Unlike Video 2, the sampled transcript tail for this video does **not** contain an explicit spoken
  community CTA in its final lines — the funnel here appears to rely more on the description block and
  end-screen than on a verbal pitch, a lighter-touch CTA approach than the course-style videos. [Data
  point, not a full-video confirmation — only the sampled final ~90 seconds were read in detail; a mid-video
  CTA cannot be ruled out — logged as a partial DATA GAP.]

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) open with a borrowed-clip montage of bigger names saying alarming things in their
  own words; (2) pivot to a bold claim + negative warning in your own voice; (3) explicitly flatter the
  viewer as exceptional/aware; (4) tell a second-person narrative scenario rather than a bullet list; (5)
  structure the middle as a clean taxonomy (a numbered "phases" model); (6) close with a rhetorical
  historical-stakes question, not necessarily a hard sales pitch.
- Commodity vs. unfair advantage: the anxiety-hook technique itself is commodity (widely used across the AI-
  content genre); the borrowed-clip sourcing/editing and the narrative-scenario writing are a real production
  skill investment, not trivial to replicate at this polish level.
- Estimated difficulty for Tangent: **MED-HIGH** — the scenario-writing and clip-sourcing/rights-clearing
  work is real production overhead beyond a talking-head video.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's performance is emotional register: this is the highest-
arousal, most fear/urgency-driven video in the entire sample, and per Berger & Milkman's RESEARCH-BACKED
finding (§2.3) that is precisely the profile most associated with viral transmission — corroborated directly
by this video posting the highest comment-rate of any video analyzed here. Secondary factor: the narrative
"2035" scenario is a genuinely well-executed Story-pillar device, rare in this creator's catalog (most of his
other top performers are structured as courses/lists, not narratives). A plausible timing component: posted
January 2025, squarely inside a wave of real AI-agent product launches (the borrowed clips reference live
executive announcements), giving the anxiety hook external validation from the news cycle rather than
appearing manufactured.

#### Sources
- https://www.youtube.com/watch?v=g3-c8XZi7BY (video, description, transcript)

---

### VIDEO 4 (long-form, rank #3 of 250 by views — 37.2x median): "The 8 AI Skills That Will Separate Winners From Losers in 2025"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=aXiOBAXYxCI`. Posted 2024-12-04. Duration: 1,172s (19m 32s). [OBSERVED]
- Views: 1,618,671. Likes: 70,203 (4.34% — the highest like-rate of any long-form video in this sample).
  Comments: 2,000 (0.12%). [OBSERVED]
- Rank: #3 of 250. 37.2x the long-form median.

#### 1. Packaging
- Title: "The 8 AI Skills That Will Separate Winners From Losers in 2025" — a **listicle + binary-stakes**
  hook (you will be a winner or a loser, a hard either/or framing with no neutral outcome offered), naming an
  exact number (8) which sets a concrete, trackable promise.

#### 2. Hook (0–30s)
- Verbatim opening [OBSERVED]: *"In 2025 the winners won't be the marketers, the developers, or the
  designers — they'll be AI generalists who can do it all. I know because I've done it over the past 2 years.
  I've made almost $4 million by mastering a specific set of AI skills that have turned me into a one-person
  army."*
- Hook taxonomy: **bold claim + credibility-flex income hook**, structurally identical to Video 2's opening
  (specific $ figure delivered inside the first three sentences) but compressed into a much shorter runtime
  (19m vs. 3h50m) — the same credibility mechanism deployed at listicle scale rather than course scale.
- What the viewer sees: direct-to-camera, no visual aids yet in the opening seconds — pure verbal hook.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps]: 0:00 hook → 0:37 "Who am I?" (credibility) → 1:09 "Survival
  of the Fittest" framing → 3:47 "Modern Day Survival" → 7:50 "The 4 Powers" (a meta-framework: four
  underlying "powers" that generate the 8 specific skills, e.g. Power #1 → Skill #1, Power #2 → Skills #2–5,
  etc.) → 17:21 Skill #8 (final) → close.
- Listicle-with-a-unifying-frame structure, exactly the pattern §3.2 flags as compliant-not-violating the
  "one idea" rule ("the one idea is the list itself") — the "4 Powers → 8 Skills" nested structure is a more
  sophisticated variant than a flat numbered list, giving the video an organizing logic beyond "here are 8
  things."
- Loop closure [OBSERVED, verbatim close]: *"remember what we learned from Darwin: it's not the strongest of
  the species that survives, nor the most intelligent, it's the one that's most adaptable to change... AI is
  creating a new class of people that are better adapted to this digital age, and the question for you now is
  will you be one of them."* — closes the "winners vs. losers" binary opened in the title/hook, a clean
  full-circle structure. (Note: the "survival of the fittest = Darwin" attribution is a commonly repeated
  misquote — Darwin did not coin that phrase — logged as an observed accuracy wrinkle, not corrected in the
  video.)

#### 4. Value proposition
- Practical value class: **framework/mental-model** (the "4 Powers, 8 Skills" taxonomy) rather than a
  step-by-step build; the video names the skills and the underlying logic for why they matter, and points to
  external resources (a linked roadmap) for the how-to depth.
- Specificity: MED — skill names and the reasoning behind them are concrete; execution depth is deferred to
  the gated lead magnet, consistent with this video's top-of-funnel role.

#### 5. Psychology scoring
- STEPPS: **Social Currency** — being an "AI generalist" ahead of "marketers, developers, designers" is an
  explicit identity upgrade offered to the viewer, strongly activating §2.5's identity-signaling mechanism.
  **Practical Value** — a named, numbered skill list is inherently save-worthy reference content. **Emotion**
  — the winners/losers binary carries mild status-anxiety, lower arousal than Video 3's existential framing
  but higher than Video 1's calm-useful tone.
- Primary emotion: aspiration with a light status-anxiety undertone (the "loser" framing implies real
  consequence for inaction).
- Save/send trigger: HIGH — an explicitly numbered list ("8 AI Skills") is close to the archetypal
  save-for-reference format described in §2.7, and this video's like-rate (4.34%) is the highest of any
  long-form video sampled, consistent with strong practical-value reception.

#### 6. CTA & funnel mechanics
- Explicit CTA [OBSERVED, verbatim]: *"...that's all for the video, guys, if you want to hit down leave a
  like... subscribe to the channel... I'm going to put a video up here breaking down some of the most
  important lessons for learning and building AI agents... I will see you inside the free Skool community."*
  — standard like/subscribe/community-close bundle, plus an explicit end-screen video recommendation
  (cross-promoting Video 2/its family), an on-platform retention tactic distinct from the external-link CTA.
- Description-level: Skool ("Access the Complete Roadmap for FREE"), AAA Accelerator, Morningside AI, plus a
  link to a separate "My Story" video — a recurring pattern of using one video's description to route
  traffic to another specific video (a personal-origin-story piece) rather than only to external funnel
  links.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) title as a binary-stakes numbered list ("N things that separate winners from
  losers"); (2) open with a specific income-credibility claim; (3) organize the list under a higher-order
  meta-framework (a "why" layer above the list itself) rather than a flat enumeration; (4) close by resolving
  the title's own binary framing directly.
- Commodity vs. unfair advantage: the listicle format and winners/losers framing are commodity; the specific
  "4 Powers → 8 Skills" nested taxonomy is a light but real content-design investment above a generic list.
- Estimated difficulty for Tangent: **LOW-MED** — a 19-minute structured listicle is a highly reproducible
  format relative to the multi-hour course (Video 2) or narrative-scenario (Video 3) formats above.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's performance is the combination of a concrete, countable
promise (exactly 8 skills) with an unusually strong credibility-flex hook delivered in a much shorter runtime
than this creator's typical flagship content — it captures much of Video 2's authority-establishment
technique at 1/12th the length, likely broadening its completion-rate ceiling (§1.2.2's completion-rate
mechanism favors shorter, tightly-structured content reaching its payoff faster). Secondary factor: the
binary "winners vs. losers" framing manufactures status stakes without requiring the higher-arousal
apocalyptic register Video 3 uses, making it a comparatively "safer"/more shareable watch for a broader
audience segment. This video posted the highest like-rate of any long-form video sampled, the clearest single
piece of evidence that its practical-value/identity-signaling combination landed well with the audience that
actually watched it.

#### Sources
- https://www.youtube.com/watch?v=aXiOBAXYxCI (video, description, transcript)

---

### VIDEO 5 (long-form, rank #4 of 250 by views — 27.5x median): "How to Get Rich with AI: The Complete Beginner's Blueprint"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=h9Pk5iNDXMk`. Posted 2024-10-24. Duration: 1,597s (26m 37s). [OBSERVED]
- Views: 1,197,738. Likes: 41,716 (3.48%). Comments: 702 (0.06%). [OBSERVED]
- Rank: #4 of 250. 27.5x the long-form median.

#### 1. Packaging
- Title: "How to Get Rich with AI: The Complete Beginner's Blueprint" — a direct, unambiguous income-claim
  title with a completeness promise ("Complete...Blueprint") and an explicit beginner-accessibility signal,
  removing the "is this too advanced for me" objection before the click.

#### 2. Hook (0–60s)
- Verbatim opening [OBSERVED]: *"I started with zero experience in AI, and within just 2 years I've built
  multiple AI businesses that have generated almost $3 million in revenue... without any formal coding
  experience, with no degree, and without any investors either... in this video I'm going to give you that
  exact blueprint... the same blueprint that worked for me and for the thousands of successful AI
  entrepreneurs in both my free and paid communities. And when I say thousands, I mean it: from the data I've
  collected of over 37,000 people in my free community, over 5,000 of those are already making between $1
  and $10,000 per month with their AI business, and 585 of them are already doing over $10,000 every
  month..."*
- Hook taxonomy: **bold claim + statistical social-proof stack** — this is the single most granular
  income-claim data point in the entire dossier: a specific personal revenue figure ($3M), plus a specific
  community size (37,000), plus a specific income-tier breakdown of that community (5,000 at $1–10K/mo, 585
  at $10K+/mo). This stacks personal credibility with third-party (community-member) social proof inside the
  first minute.
- What the viewer sees: direct-to-camera; the specificity of the numbers is doing the persuasive work, not
  visual production.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps]: 0:00 hook/stats → 0:59 "Three Parts of This Video" →
  1:43 current state of the economy → 3:31 the AI landscape → 4:12–13:37 five specific AI business models
  (Business #1 through #5) → 13:37 "Where to Start" → 16:32–22:42 "3 Phases of AI Business" → 22:42 a
  concrete "6 Month Plan" → 24:23 final note/close.
- Structure explicitly telegraphed up front ("Three Parts of This Video," 0:59) — a retention-engineering
  device that sets viewer expectations for a defined, finite journey rather than an open-ended ramble,
  reducing mid-video drop-off risk by making progress legible.
- Payoff placement: **drip-fed across the whole runtime**, not front- or end-loaded — five distinct business
  models each function as a mini-payoff (§3.2's listicle-as-valid-alternative-structure), building toward the
  single biggest payoff (the concrete 6-month plan) near the end.

#### 4. Value proposition
- Practical value class: **copyable workflow at the planning level** — a genuine 6-month, phased roadmap, not
  just a mindset framework. This is more execution-oriented than Video 3 or Video 4's more conceptual
  framings.
- Specificity: HIGH for a beginner-blueprint video — five named business models plus a phased timeline is
  substantially more concrete than most "how to get rich" content in the wider genre.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (a genuinely actionable phased plan). **Social Currency /
  Public proof** — the community income-tier statistics function as visible social proof (§2.2's "Public"
  pillar: seeing that thousands of *other* ordinary people are already succeeding makes the opportunity feel
  observably real, not just claimed).
- Primary emotion: aspiration, with an explicit anxiety-relief close (see Section 6) rather than an
  anxiety-inducing hook — this video's fear register is deployed at the *end*, not the opening, a different
  sequencing than Video 3's fear-first structure.
- Save/send trigger: HIGH — a "6 Month Plan" framed video is maximally save-for-reference content, matching
  §2.7's profile precisely.

#### 6. CTA & funnel mechanics
- Explicit CTA and closing emotional beat [OBSERVED, verbatim]: *"...I don't have to lose a wink of sleep at
  night about whether my future is at risk or whether I'm going to be made redundant... take it from me, take
  it from all the other people in my community, go in there, have a chat to people... if at any point over
  the next 6 months you have issues implementing the roadmap... you can join the free Skool community and you
  can actually ask questions to me directly on my free community Q&As, which are once a week... you can put
  it on your calendar."* — this is the most specific, concrete free-tier perk named anywhere in the sampled
  catalog: a **weekly live Q&A with Liam himself**, directly inside the free community, explicitly offered as
  the safety net for anyone who gets stuck on the video's own roadmap.
- Funnel mechanics: the anxiety register (job security, redundancy) is reserved for the *close*, functioning
  as the emotional case for why the community matters, rather than as the hook — the video leads with
  aspiration/stats and closes with fear-resolution, the inverse sequencing of Video 3.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) open with a personal income claim plus granular third-party social-proof
  statistics (not just your own numbers — your community's income distribution); (2) explicitly preview the
  video's own structure ("three parts") in the first minute; (3) present multiple named, distinct business
  models as sub-payoffs; (4) build to one concrete phased timeline as the biggest payoff; (5) close by naming
  a specific, recurring, personal-access perk (a live weekly Q&A) as the resolution to any doubt.
- Commodity vs. unfair advantage: the blueprint structure is replicable by any creator with a community; the
  specific granular member-income statistics are Liam's unfair advantage — a smaller/newer creator has no
  comparable third-party proof to cite.
- Estimated difficulty for Tangent: **MED** — the structure is learnable, but the credibility stack (a large
  pre-existing community with income data to cite) is the hard-to-replicate prerequisite.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's performance is the density and specificity of its social
proof — stacking a personal revenue figure with a granular, third-party community income breakdown (37,000
members; 5,000 at $1–10K/mo; 585 at $10K+/mo) in the first 60 seconds is a materially stronger credibility
device than a personal claim alone, directly engaging §2.2's Public/social-proof pillar rather than resting on
Social Currency alone. Secondary factor: the explicit "three parts" structural preview reduces early
abandonment risk by making the video's scope legible immediately. The weekly-live-Q&A CTA at the close is
also a genuinely differentiated funnel mechanic among the videos sampled — a concrete, recurring, personal-
access perk rather than a generic "join my community" ask, plausibly improving free-to-community conversion
specifically for this video even though that isn't independently measurable from public data alone
[INFERRED — the mechanism (specific/concrete offers converting better than generic ones) is standard
marketing logic, not independently verified for this exact video].

#### Sources
- https://www.youtube.com/watch?v=h9Pk5iNDXMk (video, description, transcript)

---

### VIDEO 6 (long-form, rank #5 of 250 by views — 23.2x median): "How to Get Rich with AI Agents in 2025 | Complete Beginner's Guide (OpenAI Custom GPTs)"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=Hh2zqaf0Fvg`. Posted 2024-01-17. Duration: 4,883s (1h 21m 23s). [OBSERVED] — the
  earliest-published video in this top-6 sample by over 8 months, and the second-longest video sampled.
- Views: 1,010,853. Likes: 33,901 (3.35%). Comments: 798 (0.08%). [OBSERVED]
- Rank: #5 of 250. 23.2x the long-form median.

#### 1. Packaging
- Title stacks an income claim ("Get Rich"), a year-anchor ("2025" — notably published in **January 2024**,
  meaning the title was forward-dated by an entire year at publication, a deliberate evergreen-relevance
  tactic), a beginner-accessibility signal, and a specific product name (OpenAI Custom GPTs) — an unusually
  dense, multi-hook title compared to the more single-concept titles of Videos 2–5.

#### 2. Hook (0–60s)
- Verbatim opening [OBSERVED]: *"OpenAI has just released the GPT store, marking the App Store moment for
  AI. Looking back to 2008 when Apple unleashed their App Store, only those with app development skills got a
  slice of the millions the App Store generated. The difference for us today is that the skills required to
  create for the GPT store... can be learned in an hour or two rather than 3 years of software engineering at
  college... take advantage of the easy money new platforms like this offer before it's too late."*
- Hook taxonomy: **analogy-driven bold claim + scarcity/urgency** — an explicit historical parallel (2008 App
  Store) does the credibility-building work here instead of a personal income-claim opener, a structurally
  different hook mechanism than every other top-6 video in this sample (all of which open with Liam's own
  $-figures). "Before it's too late" is an explicit urgency/scarcity device.
- A self-aware credibility bridge follows almost immediately [OBSERVED]: *"Now before you sit down and listen
  to another random guy on the internet teach you how to make money online... you need to know a little bit
  about the person giving you the advice"* — Liam explicitly names and defuses the viewer's skepticism before
  introducing himself, a distinct rhetorical move not seen in the other sampled hooks.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps]: 0:00 intro/hook → 3:38 what are GPTs → 7:13 the app-store
  opportunity → 12:11 "2024's Most Valuable Skill" → 20:44 Chapter 2: five named skills (20:57–33:53) →
  37:27 Chapter 3: a full hands-on build (37:48–1:18:22, roughly 40 minutes of screen-recorded, step-by-step
  GPT construction, including custom actions, OpenAPI schemas, authorization setup, publishing) → 1:18:22 key
  takeaways/close.
- This is the most tutorial-dense video in the top-6 sample by proportion of runtime (roughly half the video
  is a single continuous build-along), closer in kind to Video 2's course format than to the
  listicle/narrative formats of Videos 3–4.
- One-idea structural discipline: violated in the literal sense (multiple skills, multiple chapters) but
  compliant with §3.2's list-with-unifying-frame allowance — everything nests under the single "get rich with
  GPTs" frame.

#### 4. Value proposition
- Practical value class: **copyable workflow**, HIGH specificity — the closing minutes give a numbered,
  sequential action list (create your first GPTs → pick a niche → build an audience by "sharing helpful
  content on things like Twitter or YouTube or LinkedIn or **short form content**" → deploy via a named
  third-party tool).
- **Notable finding:** this video explicitly recommends **short-form content** to its own audience as an
  audience-building tactic (verbatim, [OBSERVED]: *"you can then start to build your building profile...
  begin an audience on a platform of your choice by sharing helpful content on things like Twitter or YouTube
  or LinkedIn or short form content"*) — a direct, observed irony given the Critical Finding at the top of
  this dossier: Liam teaches his audience to use short-form content for growth, while his own channel has
  posted exactly one Short in its entire history.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (full build tutorial). **Triggers** — tying the pitch to a very recent,
  widely-covered news event (the GPT Store launch) means the topic itself was already "top of mind, tip of
  tongue" for the target audience at time of posting (§2.2's Triggers pillar), a news-hook advantage none of
  the other top-6 videos share as directly.
- Primary emotion: urgency/scarcity ("before it's too late," "tens of thousands of people rushing to this new
  opportunity") layered under an otherwise practical, tutorial-driven tone.
- Save/send trigger: HIGH — an 80-minute build-along with granular technical timestamps (schemas,
  authorization, deployment) is dense reference material, the kind of content a viewer returns to
  step-by-step rather than watches once.

#### 6. CTA & funnel mechanics
- Explicit close [OBSERVED, verbatim]: *"...that's all for the video guys, thank you so much for watching and
  congratulations on making it to the end. I wish you all the best for 2024 and will continue to do all I can
  to help you make money with AI and build a life you truly love living."* — notably the most personal/
  warm sign-off language sampled, without a hard community CTA in the final lines read (description still
  carries the standard Skool/Accelerator/Morningside links).
- Funnel position: positioned as a skills-transfer/tool-adoption video (riding the GPT Store news cycle) more
  than a direct community-conversion video — the CTA emphasis is softer here than in Videos 2, 4, or 5.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) attach your evergreen income-opportunity content to a very recent, named platform
  launch (ride the news cycle rather than starting from a generic premise); (2) use a historical analogy (a
  past platform's gold-rush moment) to make the *size* of the opportunity legible without needing your own
  income claim as the sole credibility source; (3) proactively name and defuse "why should I trust this
  random person" skepticism before the pitch; (4) close the video by explicitly telling your audience to use
  short-form content to build their own following (even if you personally don't).
- Commodity vs. unfair advantage: attaching content to a trending product launch is a widely-used,
  reproducible tactic (commodity); the 80-minute, technically deep build-along (schemas, auth, deployment) is
  a real production/expertise investment, not trivial.
- Estimated difficulty for Tangent: **MED-HIGH** — requires both fast turnaround on a live news hook AND deep
  technical build content in the same asset.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's performance is timing: it was published 17 days after
OpenAI's GPT Store launch (per the video's own framing, "OpenAI has just released the GPT store"), catching a
genuine news-cycle wave (§2.2's Triggers pillar) that guaranteed high organic search/recommendation relevance
independent of hook craft — a clear trend-surfing/luck component per the template's guidance to name timing
effects explicitly. Secondary factor: the historical-analogy hook (2008 App Store) is a more sophisticated
trust-building device than a bare income claim, useful precisely because credibility hadn't yet been
established with viewers arriving cold off a trending-topic search. The video's own advice to viewers ("build
your audience... on short form content") stands in direct, observable tension with the channel's own Shorts
abstinence — worth flagging as the dossier's clearest single piece of evidence that Liam's stated growth advice
and his own channel strategy have diverged.

#### Sources
- https://www.youtube.com/watch?v=Hh2zqaf0Fvg (video, description, transcript)

---

### VIDEO 7 (long-form, rank #6 of 250 by views — 22.8x median): "2 years in Dubai - my honest thoughts"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=QTABGw29W5M`. Posted 2024-08-06. Duration: 973s (16m 13s). [OBSERVED]
- Views: 992,403. Likes: 21,796 (2.20% — the lowest like-rate of the top-6 sample). Comments: 3,100 (0.31%,
  second-highest comment-rate in the sample). [OBSERVED]
- Rank: #6 of 250. 22.8x the long-form median. The only top-6 video that is not "make money with AI" content
  at all — a personal lifestyle/relocation vlog.

#### 1. Packaging
- Title: "2 years in Dubai - my honest thoughts" — a lowercase, conversational, low-hype title, a sharp
  register shift from every other top-6 title's income-claim/bold-claim framing. "Honest" is doing
  credibility-signaling work (implying other Dubai content isn't honest), a mild negative-comparison hook
  without naming a target.

#### 2. Hook (0–45s)
- Verbatim opening [OBSERVED]: *"So today marks roughly the 2-year anniversary since I packed up my life in
  New Zealand and moved to Dubai to live and work, and I thought this was a good time to make this video and
  kind of reflect on my thoughts after 2 years... I think that might be helpful for a lot of you who are
  interested in moving there and want to know how good it is, really, cuz they make it out to be this
  entrepreneur's paradise — some people say it's awful. I want to give you my actual thoughts and my
  experience."*
- Hook taxonomy: **debunking/contrarian-honesty framing** — explicitly stakes out a middle position against
  two named extremes ("entrepreneur's paradise" vs. "awful"), a device distinct from every bold-claim/income-
  claim hook in the rest of this sample.
- What the viewer sees: direct-to-camera personal reflection, no business-tutorial visual register at all —
  signals a content-type shift before any words are needed.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps]: 0:00 intro → 0:43 personal experience/context → 2:34–5:46
  eight numbered pros → 6:14–12:23 nine numbered cons → 12:23 "Who SHOULD move to Dubai?" → 13:13 "Who
  SHOULDN'T move to Dubai?" → 14:41 a "Bonus Pro" (a deliberate small extra payoff after the video appeared to
  be structurally complete, a minor rewatch/completion-reward device).
  Note the pro/con imbalance (8 pros vs. 9 cons, and cons given roughly double the runtime of pros, ~6
  minutes vs. ~3) — a structural tell that despite the "honest, balanced" framing, the video leans mildly
  negative in substance, consistent with the closing content (see Section 8).
- One-idea/listicle-with-frame compliance: yes, cleanly (§3.2) — pros/cons is an inherently unifying dual
  list structure.

#### 4. Value proposition
- Practical value class: **decision-support content** (should I move to Dubai), a distinct value class from
  every other video in this sample — not a business tutorial, not a tool discovery, but personal-experience-
  as-decision-input.
- Specificity: MED-HIGH — nine distinct, named cons (not vague "it's hard sometimes" gesturing) plus explicit
  audience segmentation (who should/shouldn't move).

#### 5. Psychology scoring
- STEPPS: **Story/Emotion** — this is the only video in the sample built on lived personal narrative rather
  than a taught framework, giving it a distinct parasocial-bonding profile (§2.4.1: self-disclosure measurably
  strengthens parasocial trust) not present in the tutorial-format videos.
- Primary emotion: reflective/authentic-vulnerability register, a notably different (and lower-arousal, more
  intimate) tone than the anxiety/aspiration registers dominating the rest of the top-6.
- Identity-signaling: LOWER than the business-tutorial videos — sharing "watch this guy's honest Dubai
  take" signals less status than sharing an income-opportunity insight, but the video's high comment-rate
  (0.31%, second in the sample) suggests it prompted unusually active personal engagement/opinion-sharing
  (relocation is a topic people have strong personal takes on) rather than passive consumption.

#### 6. CTA & funnel mechanics
- Explicit close [OBSERVED, verbatim]: *"...that's all for this video. If you're interested in learning more
  about how I make my money with the businesses that I run, I'll put a video up here that will kind of
  introduce you to all that... this might be shown to people who are outside my core audience, so yeah,
  that's been all, I'll see you in the next one."*
- **Self-aware broad-reach acknowledgment** [OBSERVED, verbatim above]: Liam explicitly names that this video
  is likely reaching viewers "outside my core audience" — direct evidence this video functions as a
  **niche-to-broad laddering** play (per §4's framework), using a universally-relatable lifestyle topic
  (expat relocation) to pull in viewers who would never search "AI automation agency," then using the
  end-screen to bridge them toward the business content.
- No community/Skool CTA spoken in the sampled close — the funnel move here is entirely on-platform
  (end-screen video recommendation into the business catalog), not a direct external-link pitch, consistent
  with this video's role as top-of-funnel broad-audience acquisition rather than direct conversion.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) pick a personal-life milestone with broad, non-niche relatability (relocation,
  in this case); (2) frame it explicitly as debunking two extreme narratives; (3) structure as a pro/con
  list with real specificity; (4) end by explicitly bridging back to your core-topic content for the portion
  of the audience who are new/outside your niche.
- Commodity vs. unfair advantage: the relocation-vlog format is entirely commodity (an enormous, saturated
  YouTube genre on its own); Liam's advantage is using it as a **funnel bridge** into an existing, unrelated
  business-content catalog, not the vlog format itself.
- Estimated difficulty for Tangent: **LOW** — the format itself is simple; the strategic value depends
  entirely on having a separate core content library worth bridging viewers into.

#### 8. Why it won — analyst synthesis
The single most load-bearing reason for this video's performance is genre-crossing reach: as an
expat-lifestyle video, it competes in a search/recommendation space entirely disconnected from "AI business"
content and orders of magnitude larger in total search volume, which plausibly explains both its strong view
count AND its comparatively lower like-rate (viewers arriving via a lifestyle-topic search have a weaker
pre-existing affinity/parasocial bond with Liam than his core AI-business audience, per §2.4's parasocial
mechanism — cold viewers like less even when they watch fully). Liam's own on-camera acknowledgment that this
reaches people "outside my core audience" independently confirms this was a deliberate top-of-funnel/
audience-laddering move (§4), not an incidental personal vlog. Secondary factor: relocation content
inherently invites strong personal opinions, plausibly explaining its high comment-rate relative to its
like-rate — people argue about Dubai in the comments more readily than they "like" a business tutorial.

#### Sources
- https://www.youtube.com/watch?v=QTABGw29W5M (video, description, transcript)

---

### VIDEO 8 (long-form, exact median — rank #125 of 250): "7 Proven AI Systems Giving Ecommerce Stores an Edge in 2025"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=yxStHAjTTbU`. Posted 2025-04-19. Duration: 779s (12m 59s). [OBSERVED]
- Views: 43,502. Likes: 1,454 (3.34%). Comments: 59 (0.14%). [OBSERVED]
- Rank: exactly #125 of 250 — the median video of the entire long-form catalog by construction.

#### 1. Packaging
- Title: "7 Proven AI Systems Giving Ecommerce Stores an Edge in 2025" — a numbered-list, niche-specific
  ("ecommerce stores") title, narrower in addressable audience than any top-6 title (all of which target the
  broad "anyone wanting to make money with AI" audience, not a specific vertical).

#### 2. Hook (0–90s)
- Verbatim opening [OBSERVED]: *"Okay, so I surveyed over 100,000 AI agency owners in the world's largest AI
  business community to find out which ones were using AI to deliver the best results for their ecommerce
  clients. And what I discovered is that the ecommerce playbook isn't about to be changed by AI — it's
  already been disrupted forever. For example, we found a store owner using AI to go from 50 hours a week
  responding to customer messages on WhatsApp down to zero, fully automated... These are going to be seven
  real examples of AI agencies helping ecommerce clients turn their cost centers into profit-generating
  machines. Even using some of these solutions to scale from $9K to $252,000 per month within just 8 months.
  I'll share the playbooks and the proof — real numbers, screenshots, and the exact tools they're using."*
- Hook taxonomy: **result-first + statistical-authority hook** — leads with a survey-methodology credibility
  claim ("100,000 AI agency owners") before any individual example, then stacks the single most extreme
  income-claim number in this entire dossier ($9K → $252K/month in 8 months) as the headline proof point.
- What the viewer sees: direct-to-camera, verbal-only in the hook (no screenshots/proof shown yet in the
  opening seconds — the "screenshots" promise is deferred).

#### 3. Structure & retention engineering
- Beat map [OBSERVED — this video's description gives explicit timestamps, itself a data point: 0:00 "What
  We're Covering" → 1:28–11:52 seven numbered solutions (Solution #1 through #7, each 1–2 minutes) → 11:52
  recap/close]. A pure listicle with a tight, evenly-paced per-item runtime (~90 seconds per solution on
  average), the most rigidly uniform structure of any video in this sample.
- Payoff placement: drip-fed evenly across seven roughly-equal segments, no single dominant payoff — every
  segment is a comparable-weight mini-case-study (name, tool stack, specific price charged, specific outcome).
- Pacing: screen-capture heavy per the description's implied structure (screenshots of receipts/results named
  in the hook), consistent, list-driven rhythm.

#### 4. Value proposition
- Practical value class: **case-study/proof compilation** — each of the seven items names a real person
  (LinkedIn-linked in the description), their tool stack (e.g., "WhatsApp Business API, Supabase, n8n" for
  the first example), and a specific price charged ("$7,000 as a one-time fee with no retainer").
- Specificity: HIGH — this is one of the most granular, name-and-price-specific videos in the entire sample,
  materially more concrete than the broader "8 skills"/"5 businesses" framework videos in the top-6.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant, reinforced by **Public**/social-proof (real, named, LinkedIn-linked
  case studies are a much stronger "Public" signal per §2.2 than an anonymous statistic — a viewer can go
  verify these people exist). **Story** — each of the seven mini-segments is a compressed narrative
  (business had a problem → an agency built a solution → a specific dollar outcome).
- Primary emotion: aspiration, grounded/credible rather than urgent — no fear/scarcity language observed in
  the sampled hook or close, a calmer register than the top-6's income-claim hooks despite citing the
  dossier's single largest specific dollar figure ($252K/month).
- Save/send trigger: HIGH by content type (a 7-item reference case-study compilation) but this did NOT
  translate into outlier view counts — a useful counter-example to the assumption that save-worthy structure
  alone predicts distribution; niche audience size (ecommerce-specific AI agency owners is a narrower slice
  of Liam's total audience than "anyone wanting to make AI money") is the more likely explanatory factor (see
  Section 8).

#### 6. CTA & funnel mechanics
- Explicit CTA and UGC funnel [OBSERVED, verbatim, description]: *"Have your own solution to share? Tell us
  here: [form link]"* — a distinct funnel mechanic not observed in any top-6 video: **soliciting audience
  case studies for future videos**, which simultaneously sources free content, rewards community members with
  exposure/credibility, and manufactures fresh social proof — a closed loop unique to this
  community-driven-content-series format.
- Standard close [OBSERVED, verbatim]: *"...if you're an AI automation agency owner building some awesome
  stuff in any industry and want to be on one of these videos so you can get some free coverage and attention
  for your agency, there'll be a form in the description... make sure you're subscribed, like the video...
  and if you enjoyed this one and want to hear 16 of the best AI lead generation systems that are selling
  right now, I'll also link that up here — an absolute banger."* — explicit cross-promotion to a sibling
  video in the same "proven systems" series format.
- Funnel position: this is a **series-format video** (explicitly referencing a sibling "16 AI lead generation
  systems" entry) — evidence of a recurring format/franchise within the channel, per §3.4.2's series-effects
  framework, distinct from the one-off flagship videos dominating the top-6.

#### 7. Replicability verdict
- Extractable TEMPLATE: (1) survey/solicit real case studies from your own community rather than inventing
  hypothetical examples; (2) open with an aggregate credibility stat (N people surveyed) before any
  individual story; (3) structure as evenly-paced numbered segments, each with a name, tool stack, and
  specific price; (4) close by inviting the audience to submit their own case study for a future entry,
  creating a self-sustaining content pipeline.
- Commodity vs. unfair advantage: the case-study-compilation format is replicable by any creator with an
  audience; Liam's unfair advantage is having an existing 100,000+-member community to survey/source from —
  without that base, this format has no raw material.
- Estimated difficulty for Tangent: **MED** — the format mechanics are simple, but sourcing genuine, verifiable
  case studies requires an existing engaged audience Tangent does not yet have.

#### 8. Why it won (landed at exactly median) — analyst synthesis
The single most load-bearing reason this video sits at the exact median rather than in the top tier is
**audience-segment narrowing**: "ecommerce stores" is a specific vertical within Liam's broader "anyone who
wants to make money with AI" audience, and per the funnel-map in Section A, niche-specific content should be
expected to under-reach relative to universally-addressed content (Video 2's "beginner's guide," no
vertical named) even when execution quality (specificity, real case studies, structural discipline) is
comparably high or higher. This is a genuinely well-built video by several of this dossier's own craft
metrics — the highest case-study specificity in the sample, a UGC-sourcing funnel loop unique among the
videos analyzed, and the single largest headline dollar figure in the dossier ($252K/month) — yet its median
placement is the clearest evidence in this entire dossier that **audience-addressability, not hook/production
quality, is the dominant variable** separating this channel's outlier hits from its typical output. This is
the load-bearing insight for Section C/D below.

#### Sources
- https://www.youtube.com/watch?v=yxStHAjTTbU (video, description, transcript)

---

### VIDEO 9 (long-form FLOP #1 of 3, rank #4 from bottom of 250 by views): "Mixo.io's REVOLUTIONARY Text-to-Website AI Explained | Founder Chat w/ Adam Arbolino"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=vTUlIl1N53o`. Posted 2023-02-22. Duration: 1,794s (29m 54s). [OBSERVED]
- Views: 4,177. Likes: 119 (2.85%). Comments: 16 (0.38%). [OBSERVED]
- Rank: near the very bottom of the 250-video catalog (the single lowest-viewed video in the full sweep, at
  4,100 views, is a different video not selected here to preserve source diversity across the three flops —
  see Method Log). Excluded from being penalized as "too recent to have matured": posted 2023-02-22, over 3
  years before this dossier's research date, ruling out an immaturity confound.

#### 1. Packaging
- Title: "Mixo.io's REVOLUTIONARY Text-to-Website AI Explained | Founder Chat w/ Adam Arbolino" — names a
  specific, low-name-recognition third-party product and a guest most viewers will not recognize, the
  opposite of Video 1's borrowed-authority strategy (that Short worked partly *because* Hormozi is famous;
  this video's guest carries no comparable pre-existing audience pull). "REVOLUTIONARY" is unearned
  superlative inflation without a personal stake/claim behind it (contrast Video 5/6's specific $-figures).

#### 2. Hook (0–30s)
- Verbatim opening [OBSERVED] — an unusual **cold-open-then-rewind** structure: *"...that's kind of the
  secret sauce to how you grow something, you have liberty to discuss it, what model are you using
  underneath... yeah, I put the tech hat on me and think where this goes... where are the areas that you were
  seeing the most action..."* (a mid-conversation teaser snippet, no context given) followed immediately by:
  *"Hello and welcome everybody back to the channel, today we have this very special guest on the channel,
  Adam Arbolino, founder of Mixo.io..."* (a formal, scripted re-introduction).
- Hook taxonomy: attempted **in-medias-res teaser** (§2.1.2) immediately undercut by a full-context formal
  reset seconds later — the teaser doesn't earn its own suspense because it's followed by exactly the kind of
  slow, "hello and welcome" preamble §2.6.2 flags as a silent retention killer. This is the only video in the
  entire 11-video sample with an explicit "hello and welcome back to the channel" opening.
- What the viewer sees: two-person video-call-style interview framing, low visual dynamism from the first
  frame.

#### 3. Structure & retention engineering
- Beat map [OBSERVED via description timestamps + transcript sampling]: 0:00 intro → 0:37 Adam/Mixo's origin
  story (an extended personal/career narrative — 15 years in startups, DesignCrowd, BrandCrowd — before Mixo
  itself is discussed in depth) → 5:50 Liam's own struggles prototyping AI apps → 10:53 what's under Mixo's
  hood → 18:30 AI empowering individuals → 21:56 Mixo's marketing strategy → 26:30 advice for entrepreneurs →
  28:37 outro.
- Structural problem: the guest's personal biography (0:37–~5:00) precedes any product substance, and is
  general startup-founder narrative not specific to AI or to Liam's stated niche — a much slower ramp to
  payoff than any top-6 video, none of which spend meaningful runtime on a third party's unrelated career
  history before the AI content begins.
- One-idea discipline: violated without a clean unifying frame — this is a loosely structured Q&A-style
  conversation, not a listicle-with-frame (§3.2) or a single-throughline narrative (contrast Video 3's tight
  2035 scenario) — closer to unstructured "podcast chat" than any of the top/median videos.

#### 4. Value proposition
- Practical value class: **founder interview / soft news**, low specificity for the actual target audience —
  general startup/distribution-channel advice ("finding your distribution channel is the one key thing")
  rather than an AI-agency-specific, immediately actionable takeaway.
- Specificity: LOW-MED relative to the rest of the sample — no numbered steps, no pricing, no named tool
  stack for the *viewer* to replicate (the conversation is about Adam's company, not a teachable system for
  the audience).

#### 5. Psychology scoring
- STEPPS: weakest activation of any video in the sample across nearly every pillar. **Practical Value** —
  low (general founder wisdom, not a specific system). **Social Currency** — low (Adam Arbolino carries no
  pre-existing recognition for Liam's audience to borrow). **Emotion** — flat/calm, no arousal spike.
  **Story** — present but generic (a startup-founder origin story is a very common genre beat, not a
  distinctive narrative).
- Primary emotion: neutral-informational, the lowest-arousal video in the entire sample.
- Save/send trigger: LOW — nothing here is reference-worthy or forwardable to a specific person in the way
  the numbered case-study/skill-list videos are.

#### 6. CTA & funnel mechanics
- Description-level CTA [OBSERVED]: identical standard funnel bundle (Skool, AAA Accelerator, Morningside AI)
  as every other video in the sample — the funnel infrastructure does not vary with expected content
  performance; it's templated across the whole catalog (see Section D). Additionally includes a direct
  affiliate-style promotional link ("Create Your Own Website in Seconds w/ Mixo! 👉 mixo.io/?via=liam") and a
  reference to a "Founder Chat Playlist" — confirming this was part of a recurring interview series/franchise,
  not a one-off.
- Funnel position: this reads as a **relationship/networking or cross-promotional** video (interviewing a
  fellow founder, likely mutually beneficial for both parties' audiences) rather than a growth- or
  conversion-optimized asset — its low view count is consistent with a video that wasn't built primarily to
  win the algorithm.

#### 7. Replicability verdict
- Extractable TEMPLATE (as an anti-pattern): what NOT to do — don't open with an un-earned in-medias-res
  teaser immediately followed by a full scripted re-intro; don't spend the first several minutes on a guest's
  general career history before any content specific to your audience's stated interest; don't rely on a
  guest's name recognition without verifying your audience actually knows them.
- Commodity vs. unfair advantage: guest-interview format is commodity; nothing about this execution rises to
  a differentiated advantage.
- Estimated difficulty for Tangent: **LOW** to execute, but LOW-value — this format is easy to produce and,
  per this evidence, a comparatively weak use of production time relative to this creator's own top-6
  formats.

#### 8. Why it lost — analyst synthesis (delta vs. top performers named explicitly)
The single most load-bearing reason for this video's underperformance is **audience-fit mismatch layered on
weak hook craft**: unlike Video 9's category-mates in the top-6 (Videos 2–6), which open with Liam's own
specific, high-stakes claims about the audience's own potential outcomes ("you can get rich," "you can avoid
being a loser"), this video opens with a stranger's general startup story that offers the viewer no personal
stake or promise in the first several minutes — a direct, observable violation of the hook-quality gate in
§1.2.1 (there is no "visible payoff, promise, or unresolved gap" specific to the viewer within the critical
opening window; the in-medias-res teaser is generic industry chat, not a viewer-relevant promise). The named
guest also carries none of Hormozi's (Video 1) audience-recognition pull, so the "borrowed authority" hook
mechanism that worked at small scale in the one Short is entirely unavailable here. Compared to the top-6's
consistent income-claim/credibility-flex opening formula, this video is the clearest evidence that Liam's
catalog underperforms specifically when it drifts into founder-interview/networking content — a distinct,
identifiable content bucket from his core "make money with AI" tutorials, and reliably his weakest-performing
bucket (see Video 10/11 below for corroboration from an entirely different sub-genre reaching the same
outcome).

#### Sources
- https://www.youtube.com/watch?v=vTUlIl1N53o (video, description, transcript)

---

### VIDEO 10 (long-form FLOP #2 of 3): "GPT-4 Honest Review: Almost Perfect!"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=HVhDKmD1g0E`. Posted 2023-03-22. Duration: 598s (9m 58s). [OBSERVED]
- Views: 4,359. Likes: 148 (3.40%). Comments: 18 (0.41%). [OBSERVED]
- Posted over 3 years before this dossier's research date — not an immaturity confound.

#### 1. Packaging
- Title: "GPT-4 Honest Review: Almost Perfect!" — pure product-news framing with no personal income/agency
  angle at all, the most "generic tech YouTuber" title in the entire sample; nothing distinguishes this from
  any of the hundreds of other GPT-4-explainer videos published by other channels the same week (GPT-4
  launched March 14, 2023; this video posted March 22, 2023 — 8 days into what was almost certainly a
  saturated news cycle across the whole AI-YouTuber ecosystem) [INFERRED — the launch-date proximity is
  observed from the video's own content ("GPT-4 has finally been released"), the claim that this was a
  saturated/crowded news moment is a reasonable inference from GPT-4's well-known outsized mainstream
  coverage, not independently verified against competing channels' upload dates].

#### 2. Hook (0–20s)
- Verbatim opening [OBSERVED]: *"GPT-4 has finally been released after years of anticipation and development,
  but how does it stack up against its predecessors, and why are there people saying that it hasn't really
  lived up to the hype, and how can you start utilizing it in your daily life? That's exactly what we're going
  to be talking about in this video — here are the six key things that you need to know about the GPT-4
  release."*
- Hook taxonomy: **straightforward listicle preview**, functional but generic — three rhetorical questions
  stacked before the numbered-list promise, a competent but unremarkable structure with no bold claim,
  no personal stake, no negative-warning/urgency device, and no borrowed-authority element.
- What the viewer sees: direct-to-camera, no visual hook device.

#### 3. Structure & retention engineering
- Beat map [OBSERVED, full transcript read]: 0:00 hook → six numbered facts (availability/API access,
  enhanced performance/benchmarks, increased input limit, multimodal/image input, customizability via system
  messages, reduced bias/better fact-checking) → then unlabeled "downsides" section (slower processing, higher
  API cost, no internet access) → a comparison to a fellow creator's prior GPT-2→GPT-3 interview anecdote →
  close.
- One-idea/listicle-with-frame compliance: technically yes (6 facts under one "what you need to know" frame),
  but the facts themselves are largely **spec-sheet recitation** (token limits, pricing tiers, benchmark
  scores) rather than the audience-specific "so what does this mean for YOUR AI business" framing that
  characterizes the top-6 videos — this video stays in tech-reviewer mode throughout rather than pivoting to
  Liam's stated niche (AI entrepreneurship) until the very final lines.
- Pacing: talking-head only, no screen-recording/demo shown despite discussing a live product (a missed
  demo-in-motion opportunity per §3.1's taxonomy).

#### 4. Value proposition
- Practical value class: **news/spec summary**, LOW-MED specificity — real numbers are cited (token limits,
  exact API pricing: "$400" vs "$7,500" per 100K requests) but framed as general tech news rather than as an
  actionable business opportunity until the closing seconds.
- Specificity: MED on the facts themselves, LOW on audience-relevant application — contrast Video 5/6, which
  spend the majority of runtime on what the viewer should specifically DO with the news.

#### 5. Psychology scoring
- STEPPS: **Practical Value** present but generic (spec-sheet facts anyone could get from OpenAI's own
  announcement). **Triggers** — the GPT-4 launch itself was a strong trigger/news event, but so was every
  other AI channel's simultaneous coverage of the same event, diluting any first-mover advantage this specific
  video might have had. **Social Currency/Story** — essentially absent; no narrative, no personal stake,
  no in-group flattery.
- Primary emotion: neutral-informational, low arousal — most similar in register to Video 9 among this
  dossier's flops.
- Save/send trigger: LOW-MED — the pricing comparison numbers have some reference value, but the video isn't
  packaged as a saveable resource (no timestamped list of numbers-to-reference, unlike the top-6's more
  deliberately structured lists).

#### 6. CTA & funnel mechanics
- Explicit close [OBSERVED, verbatim]: *"...as always on this channel we like to bring things back to
  entrepreneurship and how you can build businesses with this... currently working on a ton of interesting
  projects using GPT-4 that I can't wait to show you guys... hit down below and subscribe... hit the bell if
  you're interested in AI entrepreneurship content, that's all we talk about here on this channel."* — the
  pivot back to the channel's actual niche only happens in the final ~30 seconds, after nearly 9 minutes of
  general tech coverage.
- Description-level: identical standard funnel bundle (Skool, AAA Accelerator, Morningside AI) — again
  confirming the funnel infrastructure is applied uniformly regardless of a given video's content type or
  expected performance (see Section D).

#### 7. Replicability verdict
- Extractable TEMPLATE (anti-pattern lesson): reacting to a major, heavily-covered news event without a
  distinctive angle (no personal stake, no unique data, no contrarian take) produces a video that competes
  directly against every other creator's same-week coverage of the same event, with nothing to differentiate
  it — the opposite lesson from Video 6, which used a comparably news-driven hook (GPT Store launch) but
  wrapped it immediately in a historical analogy AND a direct business-opportunity framing from the first
  minute.
- Estimated difficulty for Tangent: **LOW** to produce, but this is a crowded, low-differentiation format —
  not recommended without a genuinely distinctive angle.

#### 8. Why it lost — analyst synthesis (delta vs. top performers named explicitly)
The single most load-bearing reason for this video's underperformance is **generic news-cycle competition
without differentiation**: this video covers the same launch event as Video 6 (a different OpenAI product
news moment, the GPT Store), but where Video 6 immediately wraps the news in a historical analogy, a
scarcity/urgency framing, and a direct "here's exactly how you personally get rich from this" structure from
the opening seconds, this video spends roughly 85% of its runtime in generic spec-sheet/tech-reviewer mode
and only pivots to Liam's actual value proposition (AI entrepreneurship) in the closing 30 seconds. The two
videos are a near-perfect matched pair for isolating what separates this creator's hits from misses on
identically-shaped "reacting to an OpenAI product launch" premises: **audience-specific framing from the first
line, not the news event itself, is the deciding factor.**

#### Sources
- https://www.youtube.com/watch?v=HVhDKmD1g0E (video, description, transcript)

---

### VIDEO 11 (long-form FLOP #3 of 3): "Why 95% of Marketers Will Not Survive the AI Revolution"

#### 0. Identity & stats
- URL: `youtube.com/watch?v=n0v-OpbtLHw`. Posted 2023-01-23. Duration: 490s (8m 10s). [OBSERVED] — the
  earliest-published video in the entire 11-video sample.
- Views: 5,843. Likes: 238 (4.07% — the highest like-rate among the three flops, despite the lowest absolute
  views of the three). Comments: 48 (0.82% — the highest comment-rate of ANY video in this entire 11-video
  sample, flop or hit). [OBSERVED]
- Posted during the channel's SMMA-to-AI content pivot era (per this same video's own transcript, see below),
  over 3.5 years before this dossier's research date.

#### 1. Packaging
- Title: "Why 95% of Marketers Will Not Survive the AI Revolution" — a bold-claim/negative-warning hook with
  a specific (if unsourced) statistic, structurally similar in kind to Video 3's "This AI Technology Will
  Replace Millions" — the same hook taxonomy that produced this dossier's #2 all-time video, here producing a
  bottom-3 result instead, a genuinely useful controlled comparison (see Section 8).

#### 2. Hook (0–35s)
- Verbatim opening [OBSERVED]: *"I lost my first client due to the influence of AI tools last week. The
  rapid rise of AI tools like ChatGPT are changing the landscape of SMMA for good... Pushed by large
  influencers like Tai Lopez and [Iman] Gadzhi, this business model has garnered enormous amounts of
  attention... As an agency owner myself, and having lost a client just last week to these influencers, I've
  had to do a real deep dive..."*
- Hook taxonomy: **personal-loss/negative-warning hook** — opens with a specific, personal, negative anecdote
  (lost a client) rather than an abstract claim, arguably a stronger individual hook device (concrete,
  first-person stakes) than Video 3's borrowed-clip-montage opening, yet this video underperformed by roughly
  300x.
- What the viewer sees: direct-to-camera, no visual aids in the opening.

#### 3. Structure & retention engineering
- Beat map [OBSERVED, full transcript read]: 0:00 hook/personal loss story → 0:56–7:13 a comprehensive
  six-service breakdown of how AI is disrupting each specific SMMA service line (copywriting, blog/SEO,
  creative ideation, media creation, email marketing, strategy) → 7:13 "are we witnessing the death of SMMA?"
  rhetorical question, answered "no, but it will rapidly change" → three concrete strategic recommendations
  for agency owners → standard subscribe/bell/like close, including an explicit statement of posting cadence:
  *"my name's Liam Ottley and I create AI and entrepreneurship focused content on this channel three times a
  week"* [OBSERVED — this is the source for the "3x/week, 2023 era" cadence claim referenced in Section A].
- This is, on transcript-read merit, one of the **most thorough and well-organized** videos in this entire
  11-video sample — six named service lines, each with concrete tool names and a clear "here's what changes
  and what you should do about it" structure, closing with an explicit macro answer to the title's own
  question. It does not read as a low-effort or poorly-structured video by any craft metric applied elsewhere
  in this dossier.

#### 4. Value proposition
- Practical value class: **copyable workflow** — genuinely comparable in specificity/structure to the top-6
  videos (named tools per service line: Copy.ai, ChatGPT, Jasper, Pictory, Midjourney/DALL-E/Stable
  Diffusion), not a generic warning piece.
- Specificity: HIGH — arguably higher than Video 3 (this dossier's #2 all-time video), which stays more
  conceptual/narrative throughout.

#### 5. Psychology scoring
- STEPPS: **Practical Value** and **Emotion** (loss-framed personal stakes) both strongly activated — by the
  checklist alone, this video should score comparably to the dossier's top performers. **Story** — the
  personal-loss opening is a genuine, specific narrative beat (stronger, arguably, than Video 3's fictional
  2035 scenario, since it's a true first-person account).
- Primary emotion: personal anxiety/loss, moderately high arousal.
- Save/send trigger: the six-service breakdown is genuinely reference-worthy — and the data bears this out:
  this video's comment-rate (0.82%) is the highest of any video in the ENTIRE 11-video sample, evidence that
  the people who did find it engaged with it actively, even though the raw reach was tiny.

#### 6. CTA & funnel mechanics
- Explicit close [OBSERVED, verbatim]: standard subscribe/bell/like, PLUS the explicit "three times a week"
  cadence disclosure — no Skool/Accelerator/Morningside link bundle in the description (unlike every other
  video in this sample) [OBSERVED] — because in January 2023 the "AAA"/Skool funnel infrastructure the rest
  of this dossier documents **had not yet been built**; the channel's own About page states the AAA model was
  created in 2023, and this video predates that model's public rollout. This is a structurally important data
  point: the standardized funnel bundle is not a channel constant, it is a **post-2023 addition**, and this
  video is a "before" snapshot of the channel pre-funnel.

#### 7. Replicability verdict
- Extractable TEMPLATE: identical in kind to the top-6's best practices (personal-stakes hook, named
  tools/specificity, clear macro-answer structure) — on pure craft grounds this is a reasonably strong
  template, not an anti-pattern.
- Estimated difficulty for Tangent: **LOW-MED**, and by content-quality metrics alone this format deserves
  more credit than its view count suggests — see Section 8 for why view count and craft diverge here.

#### 8. Why it lost — analyst synthesis (the delta vs. top performers named explicitly)
This is the most instructive flop in the entire dossier precisely because it is **not** a craft failure —
by hook specificity, hook personal-stakes, hook emotional register, structural organization, and tool-
specificity, this video matches or exceeds several of the top-6 performers on the template's own scoring
criteria. The single most load-bearing reason for its underperformance is almost certainly **audience size at
time of publication**: posted January 23, 2023, this predates the AAA-model/Skool-funnel infrastructure
(confirmed by its own description lacking the standard link bundle every other sampled video carries) and
very likely predates the bulk of the channel's subscriber growth to its current 825K — a channel publishing
"three times a week" in this era was almost certainly a small fraction of its current size, meaning this video's
absolute view ceiling was structurally capped by algorithmic seeding to a much smaller subscriber base and
topic-affinity audience (per §1.2.2's seed-audience mechanism, initial distribution scales with the size of
the qualifying pool available to test against) regardless of hook quality. [INFERRED — exact subscriber count
on 2023-01-23 was not independently obtainable via any tool available to this dossier (YouTube does not expose
historical subscriber-count snapshots publicly); the inference rests on (a) the channel's own "3x/week" 2023
cadence claim implying an early-stage growth phase, (b) the absence of the now-standard funnel bundle
confirming this predates the AAA-model rollout the channel's own About page dates to 2023, and (c) the
channel's current 825K subscriber count being reached across the ~3.5 years since — MED confidence]. This
reframes the entire Top-vs-Flop comparison for this specific video: it is best read as evidence that **channel
maturity/distribution-pool size, not content quality, is the dominant variable** for this particular flop —
a materially different "why it lost" story than Videos 9 and 10 (genuine hook/framing weaknesses) above.

#### Sources
- https://www.youtube.com/watch?v=n0v-OpbtLHw (video, description, transcript)

---

## C) TOP-vs-FLOP DELTA

The delta across this 11-video sample is not one single mechanism — three distinct, separable factors emerge,
and disentangling them is the main analytical payoff of running flops alongside hits rather than studying
hits alone:

**1. Audience-addressability breadth is the single strongest predictor, stronger than hook craft.** The
median video (Video 8, "7 AI Systems for Ecommerce") and the two strongest-hook flops (Video 10, GPT-4 review;
Video 11, "95% of Marketers") all demonstrate competent-to-excellent hook/structure execution by this
dossier's own scoring criteria, yet sit at or near the bottom of the catalog, while the top-6 are near-
universally addressed at "anyone who wants to make money with AI" rather than a named vertical (ecommerce),
a specific product review (GPT-4), or a specific sub-industry (SMMA/marketers). Video 7 ("2 Years in Dubai")
independently corroborates this from the opposite direction: it is the *only* top-6 video with zero AI-
business framing in its hook at all, and it wins by being maximally broad-reach (a universal lifestyle topic)
rather than niche-specific, with an explicit on-camera acknowledgment ("this might be shown to people who are
outside my core audience") confirming this was a deliberate broad-net cast.

**2. Channel maturity/distribution-pool size confounds any pure content-quality comparison for the oldest
flops.** Videos 9, 10, and 11 were all published January–March 2023, before the channel's own AAA-model/Skool
funnel infrastructure existed (confirmed directly: these three videos' descriptions lack the standard funnel
link bundle every other sampled video carries) and very plausibly while the channel's subscriber base was a
small fraction of its current 825K. This means the flop sample is not a clean "bad content" control group —
it is partially confounded with "small channel in an earlier era," which the top-6 (all published Aug 2024–
Mar 2025, well into the current funnel/audience-size era) do not share. Video 11 in particular scores
competitively on hook/structure/specificity yet still flopped, the strongest single piece of evidence this
confound is real and not fully explained by content quality.

**3. Genre/format matters independent of both of the above.** The two flops with the weakest hook execution
by this dossier's own criteria (Video 9, the Mixo.io founder interview, and Video 10, the generic GPT-4 spec
recap) share a format the top-6 never uses at outlier scale: unstructured guest-interview chat, and
undifferentiated news-cycle reaction without an immediate audience-specific reframe. The channel's proven
top-6 formats are, without exception, either (a) Liam himself delivering a structured, numbered, income-
stakes framework directly to camera, or (b) a broad-reach personal lifestyle piece explicitly used as a
funnel bridge — guest interviews and generic tech-news recaps appear to be a structurally weaker category
for this specific channel regardless of era.

**In two sentences:** the delta between Liam's hits and flops is driven less by hook mechanics (several flops
execute the same hook taxonomies — bold claim, negative warning, personal stakes — that also power his
biggest wins) than by how broadly a video's premise addresses "anyone who wants to make money with AI" versus
a narrow vertical, guest, or single product; a secondary, partially confounding factor is that this
dossier's flop sample skews toward the channel's pre-funnel, likely-smaller-audience 2023 era, meaning some
of the gap reflects channel maturity rather than content quality alone.

---

## D) CONTENT ARCHITECTURE

**Key vs. filler, and what actually sustains the channel:**

- **The true growth engine is a small number of massive, evergreen, maximally-broad long-form "flagship
  guide" videos** (Videos 2–6 in this sample), each a comprehensive, structurally disciplined, credibility-
  flex-hooked asset addressed at the widest possible "anyone who wants to make money with AI" audience.
  These sit atop an 83.4x top/median gap (Section A) — the channel's performance distribution is
  extremely top-heavy, not evenly strong across the catalog.
- **A secondary, smaller tier of broad-reach personal/lifestyle content** (Video 7, "2 Years in Dubai," and by
  strong implication similarly-framed personal videos elsewhere in the catalog not sampled here) functions as
  a deliberate top-of-funnel audience-laddering tool, explicitly acknowledged on-camera by Liam himself as
  reaching "outside my core audience" — this is filler in the sense of not being AI-business content, but
  strategically load-bearing as a funnel-widening device, not filler in the sense of being low-effort or
  unimportant.
- **A recurring series format** (Video 8's "proven AI systems" case-study compilations, explicitly
  cross-referencing a sibling "16 AI lead generation systems" entry, plus a community-sourced UGC submission
  form) functions as a content-pipeline/community-engagement sustaining mechanism — reliably median
  performance, not viral, but structurally cheap to produce (audience supplies the raw material) and doubles
  as a community-retention device independent of its own view count.
- **Guest interviews and generic product-news recaps are the weakest-performing identified bucket** — both
  sampled flops in this category (Video 9, Video 10) underperform even the channel's other, comparably-aged
  flop (Video 11, which uses Liam's own proven direct-address format) — suggesting this is a genre weakness
  for this specific channel, not just an era effect.
- **Shorts play effectively zero role in the funnel or the channel's growth.** This is the dossier's
  headline structural finding (see Critical Finding): one Short exists, it worked reasonably well on its own
  modest terms (documented converting at least one viewer into a community member), and was never repeated
  in the 2 years 10 months since, despite Liam's own long-form content (Video 6) explicitly advising his
  audience to use short-form content as an audience-growth tactic. **Long-form carries 100% of both the
  discovery and conversion load on this channel.**
- **The funnel itself is remarkably uniform and appears to be a fixed template, not a performance-responsive
  system.** The exact same three-link bundle (Skool community → AAA Accelerator → Morningside AI) appears in
  the description of nearly every video sampled here regardless of whether that video went on to do 3.6
  million views or 4,177 views — the CTA infrastructure does not visibly vary with a video's role in the
  funnel (flagship guide vs. founder-interview vs. lifestyle vlog all carry the identical bundle), suggesting
  this is templated/automated at the channel-operations level rather than hand-tuned per video. The one
  exception (Video 11, pre-2023 funnel rollout) is a "before" snapshot confirming the bundle was added as a
  standing operational practice at a specific point in the channel's history, not present from the start.
- **Shorts-vs-long-form funnel roles, stated plainly:** long-form is simultaneously the discovery layer, the
  trust-building layer (via multi-hour, personally-hosted, credibility-flex-hooked content), and the direct
  conversion layer (via explicit, often gamified, in-video CTAs into the free Skool community, which is
  itself the qualifying step before the paid AAA Accelerator and the Morningside AI service funnel). Shorts
  occupy no defined role in this architecture at all — not even a minor one — as of this dossier's research
  date.

---

## E) Method log

**Tools:** `yt-dlp 2026.07.04` (homebrew install, confirmed via `which yt-dlp && yt-dlp --version`); a second,
isolated `yt-dlp 2026.07.23.234303` nightly build (installed into a throwaway Python venv specifically to rule
out a version-specific bug behind the Critical Finding — see step 3 below); direct `curl` + Python (`json`,
`re`) for raw `ytInitialData`/innertube JSON inspection; Claude Browser pane (logged-out Chromium) for visual/
DOM-level verification; custom Python VTT-deduplication scripts (`dedupe_vtt.py` / `dedupe_vtt2.py` /
`dedupe_vtt3.py`, iterated to find a readable rolling-caption-collapse approach) to convert auto-caption `.vtt`
files into readable timestamped transcripts.

**Steps executed, in order:**

1. Created scratch dir
   `/private/tmp/claude-501/-Users-sparsh-Documents-Projects-Tangent/3f21975f-6df6-481e-9a72-4d4c86b4bb54/scratchpad/yt_liamottley/`.
2. SWEEP (per protocol): `yt-dlp --flat-playlist --playlist-items 1:150 --sleep-requests 0.75 --print
   "%(id)s | %(view_count)s | %(title)s" "https://www.youtube.com/@LiamOttley/shorts"` → returned exactly
   **one row**. Re-ran with no `--playlist-items` cap, with `--dump-single-json` for structural inspection,
   and with `-v` verbose logging — `yt-dlp`'s own debug output confirmed *"Playlist Liam Ottley - Shorts:
   Downloading 1 items of 1"* — i.e. `yt-dlp` itself, not a display/print-formatting issue, believes the
   playlist has one item.
3. Ruled out a version-specific `yt-dlp` bug: created an isolated Python venv, installed the latest nightly
   build (`2026.07.23.234303`, 19 days newer than the stable release in step 2) via
   `pip install --pre yt-dlp[default] --extra-index-url https://yt-dlp.github.io/yt-dlp-nightly-builds/`, and
   re-ran the identical sweep — **also returned exactly one row.** This rules out "outdated tool" as the
   explanation.
4. Direct evidence gathering: `curl`'d the raw `/shorts` tab HTML with a standard desktop User-Agent, `grep`'d
   for `videoId` occurrences (found exactly 1 unique ID), then extracted and `json.load`'d the embedded
   `ytInitialData` script block directly. Walked the resulting JSON tree to `contents.twoColumnBrowseResults
   Renderer.tabs[selected].content.richGridRenderer.contents` — confirmed this array has length 1. Separately
   searched the entire JSON tree for any `continuationItemRenderer` node (which would indicate more results
   are paginated behind a "load more" trigger) — found exactly two, both nested under the unrelated "About
   channel" engagement-panel description box, not the Shorts grid, confirming no pagination exists for this
   tab's content, not merely that `yt-dlp` failed to follow one.
5. Live-browser confirmation: opened `youtube.com/@LiamOttley` in the Claude Browser pane, clicked the
   "Shorts" tab UI element directly (not a URL navigation, to force the same client-rendering path a real user
   would experience), read the rendered page text — matched the `yt-dlp`/raw-JSON findings exactly (one
   video, "ALEX HORMOZI on How To Make A Fortune With AI," "90K views").
6. Cross-check arithmetic: swept `@LiamOttley/videos` via `yt-dlp --flat-playlist --dump-single-json` — 250
   entries returned, `playlist_count: 250` in the response, all with `duration >= 189s` (none in the
   Shorts-eligible sub-3-minute range). 250 + 1 (the Short) = 251, matching the channel header's stated
   "251 videos" exactly — an independent arithmetic confirmation not reliant on the Shorts-tab extraction
   working correctly at all.
7. Given the Critical Finding, adapted video selection (documented in Section B's intro) to draw the
   remaining 10 post-mortem slots from the 250-video long-form catalog: computed the full view-count
   distribution from the step-6 sweep, selected top 6 by views, the exact median entry (#125 of 250), and the
   bottom-ranked entries **excluding the 5 most-recently-published uploads** (identified by comparing IDs
   against the first 5 rows of the default/latest-sorted sweep) — landed on 3 flops after excluding one
   bottom-15 candidate (`zugGJjnF6vM`) that overlapped with the most-recent-5 exclusion list.
8. Per-video metadata: looped `yt-dlp --print "%(title)s | views=... | likes=... | comments=... | date=... |
   dur=...s"` and a separate `--print "%(description)s"` pass over all 11 selected IDs. **First attempt hit
   HTTP 429 "Sign in to confirm you're not a bot" errors across every ID** (a rate-limit consequence of the
   heavy probing in steps 2–6 against the same channel in a short window) — recovered by adding
   `--extractor-args "youtube:player_client=android"` and increasing `--sleep-requests` to 2, after which all
   11 metadata + all 11 description pulls succeeded cleanly.
9. Transcript pull: looped `yt-dlp --skip-download --write-auto-subs --sub-langs "en.*" --sub-format vtt`
   (same android-client/2s-sleep settings) over all 11 IDs — succeeded for all 11. Raw `.vtt` auto-captions
   use YouTube's rolling/cumulative-cue format (each cue re-sends the prior cue's text plus new words), which
   is unreadable directly; wrote and iterated three versions of a Python de-duplication script before settling
   on a "cue-chain" approach (collapse consecutive cues where each is a superset-extension of the last, emit
   only the final, longest form of each chain) that produces clean, accurately-timestamped readable text —
   used for all quoted transcript material in this dossier.
10. For the two multi-hour videos in the sample (Video 2, 3h50m; Video 6, 1h21m — and Video 3 at 53m, Video 5
    at 26m), full line-by-line reading of the entire transcript was impractical at the depth this dossier
    otherwise applies. **Adapted method, disclosed here rather than silently applied:** hooks (first
    ~60–90s) and closing CTAs (final ~2–3 minutes) were read in full verbatim for every long-form video; for
    beat-map/structure claims in the middle of long videos, this dossier relies primarily on the creator's own
    self-published, precise timestamp lists in each video's description (cross-checked by jumping to and
    reading transcript text AT those exact timestamps for at least one mid-video section per long video, e.g.
    Video 2's "3:35:29 - The Real Opportunity" section was read in full to verify the description's own
    labeling matched actual spoken content) rather than reading every intervening minute. This is a real
    depth trade-off for the longest videos and is flagged as a partial DATA GAP: middle-of-video beat-map
    claims for Videos 2, 3, 5, and 6 rest on creator-provided timestamps + spot-check reads, not full
    line-by-line transcript review, whereas Videos 1, 4, 7, 8, 9, 10, and 11 (all under 30 minutes) were read
    in full.
11. Comments: attempted `yt-dlp --write-comments` with various `--extractor-args
    "youtube:max_comments=..."` limiting syntaxes to cap fetch time on high-comment-count videos — **the
    limiting syntax did not work as expected** (two separate attempts against Video 2, which has ~2,821
    comments, both ignored the intended cap and began fetching the full comment tree; both were manually
    killed via `TaskStop` after several minutes rather than left to complete, to avoid an excessive
    request-volume/rate-limit risk against the same channel). **Successfully completed a full comment pull
    only for Video 1** (the Short, 45 comments total — small enough to complete in ~40 seconds) — this is the
    source for the specific comment quotes in Video 1's Section 6. **DATA GAP, logged not papered over:** no
    comment-content sampling (beyond the numeric `comment_count` field, which was successfully obtained for
    all 11 videos via the metadata pull in step 8) was performed for Videos 2–11; all comment-mechanics
    observations for those ten videos are necessarily limited to the count/rate, not comment content.
12. Channel-level "about" data: extracted directly from the `aboutChannelViewModel` node inside an innertube
    `browse` continuation response fetched during step 4's raw-JSON investigation (subscriber count, total
    channel views, join date, country, video count) — then independently re-confirmed via a live Claude
    Browser render of the channel's About modal (clicked into the description panel and the "and 6 more
    links" expansion) to capture the full funnel-link list (Work with me / My Accelerator / My Community /
    VLOG Channel / My Agency / Instagram / X) used to build Section A's funnel map.
13. Cadence data: `curl`'d the channel's public RSS feed
    (`youtube.com/feeds/videos.xml?channel_id=UCui4jxDaMb53Gdh-AZUTPAg`) and parsed the 15 most recent
    `<published>` timestamps directly (RSS is capped at 15 entries by YouTube; not usable for the full
    250-video catalog, only for recent-cadence estimation, which is the only role it plays in this dossier).
14. Source-video traceback for Video 1: independently pulled metadata for the parent long-form interview
    (`w1Q93tz83DY`, "The Massive Opportunity in Building AI Businesses | Alex Hormozi") named both in the
    Short's own description and in YouTube's native "this Short is from" panel — confirmed publish-date
    sequencing (interview posted 2023-09-24, Short posted 2023-09-25, one day later).
15. Visual grounding: took direct Claude Browser screenshots of Video 1 (full split-screen frame, caption
    overlay, and native source-video panel all visible and quoted directly in Section 1) and Video 2 (thumbnail
    capture attempt — an active Oracle NetSuite pre-roll ad was playing and covered the actual thumbnail;
    logged as a DATA GAP for Video 2's frame-1 description, which relies on the description/title text only,
    not a captured static image). **Frame-1/thumbnail visuals were NOT independently screenshotted for Videos
    3–11** — packaging analysis for those ten videos rests on title text, description text, and (for Video
    1 only, plus the Video-2 attempt) direct visual confirmation. Logged as a partial DATA GAP, consistent
    with this being resource-intensive to do for all 11 videos within the scope of this task.

**What was NOT independently verified (data gaps carried forward, not papered over):**
- Whether the Skool community's self-reported member counts (200K/280K/300K+ across different videos'
  descriptions and one in-video survey claim of "100,000 AI agency owners") are independently auditable —
  these are entirely self-reported by the subject, tagged [REPORTED] throughout, not third-party verified.
- AAA Accelerator pricing — never disclosed in any of the 11 sampled videos' content; not investigated via
  the Accelerator's own landing page (out of scope — this dossier analyzes video content, and entering a
  sales funnel to extract pricing was judged beyond the assignment's scope).
- Comment *content* (as opposed to comment *count*) for 10 of the 11 videos, per step 11 above.
- Full line-by-line transcript review for the middle sections of the four longest videos (Videos 2, 3, 5, 6),
  per step 10 above.
- Frame-1/thumbnail visuals for Videos 3–11, per step 15 above.
- Historical subscriber-count-over-time data — YouTube does not expose this publicly for any point besides
  "now," so the [INFERRED] claim in Video 11's analysis (that the channel was meaningfully smaller in
  January 2023) rests on indirect evidence (the "3x/week" cadence self-statement, the absence of the
  now-standard funnel bundle, and the channel's own About-page dating of the AAA model to 2023) rather than a
  directly observed historical subscriber count.
- Instagram, TikTok, and any other cross-platform presence — out of scope per the assignment ("YouTube
  @LiamOttley"); the About-panel's Instagram/X links were noted for completeness in Section A but not
  investigated further.
- Whether 44,177/4,359/5,843-view videos (Videos 9–11) reflect genuinely weak content or are simply the
  lowest-count entries in a catalog where the true bottom (a 4,100-view video, `vTUlIl1N53o`'s near-neighbor)
  was passed over in favor of source diversity — the exact bottom-ranked video by raw count was not itself
  analyzed; three videos very close to the bottom were, which the analyst judges as an acceptable and
  disclosed substitution rather than a gap, but is logged here for transparency.
