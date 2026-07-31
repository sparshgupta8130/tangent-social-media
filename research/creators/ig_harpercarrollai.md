# Creator Dossier: Harper Carroll (Instagram @harpercarrollai)

**Assignment status:** Deep-dive nominee, centerpiece cold-start case study — this is the corpus's
only documented 0→600K-in-under-2-years account with independent press verification of the growth
mechanics (The Ankler). **Analyst method:** primary data is the already-harvested
`ig_harvest/harpercarrollai.md` (live Instagram pull, read-only, dated 2026-07-25). This session did
**not** re-scrape Instagram directly with a browser (claude-in-chrome reserved by another agent) —
instead it re-verified and materially extended the harvest using `yt-dlp` fetched directly against
individual `instagram.com/reel/<code>/` URLs (Instagram's public GraphQL responses are reachable this
way without login for most posts), plus a matched YouTube Shorts cross-post channel
(`youtube.com/@harpercarrollai`, 266 Shorts, full population pulled via `--flat-playlist`) for
verbatim transcripts, and `WebSearch`/`WebFetch` for the press coverage, interviews, and funnel/business
pages. Every substantive claim below is tagged `[OBSERVED]` / `[REPORTED]` / `[INFERRED]` per the
mandatory template, with source + as-of date + confidence.

**Correction to the prior harvest (logged, not silently fixed):** the original harvest flagged 2
reels in the 48-tile grid as `@oreillymedia` collab-posts (not Harper's own content) and estimated her
"true organic floor" at ~45–50K. Direct `yt-dlp` re-verification of every reel below the 50K line in
this session found **5 non-owner tiles in the grid, not 2**: 4 confirmed `@oreillymedia` collab-posts
(uploader_id `224832541`) and **1 previously-unflagged repost by a third-party fan/clips account,
`@harpercarroll_clips`** (uploader_id `28561678480`, a different account from `@harpercarrollai`'s
own `5787807072`). Excluding all 5, this session's directly-verified true organic floor in the
48-tile sample is **36.2K** (one tile lower than the prior estimate), not ~45–50K. See Section B,
Videos 6–7 and the Sidebar, and the Method log.

---

## A. Account header + funnel map

| Metric | Value | Source | As-of | Confidence |
|---|---|---|---|---|
| Followers | **605K** (og:description) / 610K (page header, minor cache-lag) | `ig_harvest/harpercarrollai.md` | 2026-07-25 | HIGH |
| Following | 1,051 (og:desc) / 1,043 (header) | same | 2026-07-25 | HIGH |
| Posts | 232 | same | 2026-07-25 | HIGH |
| Bio | "Taught AI at @Stanford · built it at @Meta · MS+BS in AI / Weekly explAIned episodes · AI is less scary under the hood" | same | 2026-07-25 | HIGH |
| Median reel views (30 most recent tiles) | **92.85K** | same, computed | 2026-07-25 | HIGH |
| Top 5, non-pinned | DZfgPtFObU1 1.8M, DVbM3sBjl26 1.8M, DbD8-40Owbv 866K, Dan0IIuJP7K 794K, DYPXSQ4hPdF 615K | same + this session's yt-dlp re-pull | 2026-07-25 | HIGH |
| Pinned tile (excluded from top-5) | DCWW2EnA_sm, 2.1M, dated 2024-11-13 (confirmed by date) | same | 2026-07-25 | HIGH |
| True organic floor (genuine own-content, this session) | **36.2K** (DX9nDB_pdBF), 44.5K (DW9gguSDgRM) second-lowest | this session, `yt-dlp` re-verified by `uploader_id` | 2026-07-25 | HIGH |
| Non-owner tiles in the 48-tile grid | 5 of 48 (4 `@oreillymedia` + 1 `@harpercarroll_clips`) | this session, `yt-dlp` `uploader_id`/`channel` field on each | 2026-07-25 | HIGH |
| Top/median ratio (non-pinned) | 1.8M / 92.85K ≈ **19.4x** | computed | 2026-07-25 | HIGH |
| Median/follower ratio | 92.85K / 605K ≈ **15.3%** | computed | 2026-07-25 | HIGH |

### Cross-platform footprint
- **Instagram @harpercarrollai** — primary platform, this dossier. 605K followers `[OBSERVED]`.
- **TikTok @harpercarrollai** — confirmed to exist and to carry the *identical* "10 Days of AI Basics"
  content (same captions, verified by direct text match) `[OBSERVED via WebSearch-indexed TikTok post
  text, 2026-07-25, HIGH on content-match, DATA GAP on exact follower count — not independently
  obtained this session]`.
- **YouTube @harpercarrollai** — 46,500 subscribers `[OBSERVED, yt-dlp `channel_follower_count`,
  2026-07-25, HIGH]`. 266 Shorts (confirmed full population via `--flat-playlist`) plus a long-form
  companion series (the "10 Days of AI Basics" deep-dive videos, 16–34 min each) `[OBSERVED, yt-dlp,
  2026-07-25]`. **YouTube is a materially smaller, later-added platform** — see Section C.
- **Substack** (`harpercarrollai.substack.com`) — newsletter, "AI Explanations & Weekly AI News,"
  free + paid tiers, paid unlocks full archive/community/ad-free app `[OBSERVED, WebFetch, 2026-07-25]`.
- **Podcast "The Polymath Pod"** co-hosted with longevity expert Kayla Barnes-Lentz (AI, longevity,
  science, relationships, faith) `[REPORTED, WebSearch summary, MED]`.
- **Personal/business site** `harpercarroll.ai` (redirects from `harpercarrollai.com`, 301) `[OBSERVED,
  WebFetch, 2026-07-25]`.

### Funnel map
1. **Top-of-funnel:** Reels/Shorts/TikToks — numbered educational series + real-time AI-news
   explainers + brand-partner "explAIner" mini-series `[OBSERVED, this session's 7 post-mortems]`.
2. **In-video comment-keyword capture (dominant CTA mechanic):** "Comment GUIDE / FREE / START /
   BUILD and I'll DM you [the guide/link/commands]" appears on the majority of top performers
   `[OBSERVED, captions + top comments pulled directly, this session]` — functionally the ManyChat-style
   comment→DM funnel described in `03_virality_science.md` §3.4.3, driving the high comment-to-like
   ratios seen throughout (e.g., DYPXSQ4hPdF: 6,402 comments vs 13,267 likes, a 48% comment/like ratio,
   dominated by "Free, thank you" replies). **Whether an automated tool (ManyChat) or manual DM
   execution fulfills the promise was not independently confirmed** — DATA GAP, logged.
3. **Free lead magnet:** an 11-module "free video walkthrough guide" stitched from her existing
   IG/YouTube catalog, plus a "gamified web app" to track progress, delivered via DM `[OBSERVED,
   caption text, DYPXSQ4hPdF and DbD8-40Owbv]`.
4. **Substack newsletter** (free + paid) — mid-funnel nurture layer `[OBSERVED]`.
5. **Harper's AI Academy** (`academy.harpercarroll.ai`) — 162 bite-sized lessons `[REPORTED,
   WebSearch-summarized, MED — the page itself is JS-rendered and returned no body content to WebFetch,
   so this figure could not be independently re-verified against primary text this session]`.
6. **Four standalone on-demand courses** — "The Engine" (LLM mechanics), "The Prompter" (prompt
   engineering), "The Builder" (AI coding agents/CLAUDE.md architecture), "The Automation Layer"
   (Claude skills/Supabase backend integration) — 44 lessons, ~6 hours total, lifetime access, bundled
   Discord community with per-course channels, weekly office hours `[OBSERVED, WebFetch of
   `harpercarroll.ai/course`, 2026-07-25]`. **Pricing discrepancy, logged honestly:** a general
   WebSearch summary (source page unclear) reported "$129 each / $399 bundle," but the live course
   page fetched this session shows the courses as **pre-launch, waitlist-only, price undisclosed**
   `[OBSERVED, live page, 2026-07-25, HIGH — supersedes the unsourced $129/$399 figure, which is
   carried here only as a flagged, unconfirmed prior data point, LOW confidence]`.
7. **Brand/paid partnerships** — explicitly tagged `#ClaudePartner` (Anthropic), `#ChatGPT_Partner`
   (OpenAI), `#ServiceNowPartner`, `#RovoPartner` (Atlassian) posts sit **directly inside her own
   organic top-5**, not in a separate underperforming sponsored bucket — a notable divergence from the
   sponsored-content-underperforms pattern seen elsewhere in this corpus (see Section B, Videos 3–4).
   Site also displays partner logos for NVIDIA, Dell, Microsoft Research, Meta, Nebius, Perplexity, and
   Workday `[OBSERVED, WebFetch `harpercarroll.ai`, 2026-07-25]`.
8. **Speaking engagements** — Stanford HAI Advanced AI Leadership Executive Education, an AI
   Masterclass with Dell, SXSW 2026 `[REPORTED, WebSearch summary, MED]`.
9. **Professional representation** — brand/speaking contact routes to `harper@rangemp.com`
   `[OBSERVED, WebFetch `harpercarroll.ai`, 2026-07-25]`, i.e., she appears to have management/agency
   representation for deals, consistent with a fully professionalized creator-economy operation rather
   than a solo-founder side hustle.

**Funnel shape, in one line:** numbered/news-hook Reel (credential-forward, comment-CTA) → DM lead
magnet or Substack → Academy/courses (mid-ticket, self-serve) + brand partnerships and speaking
(high-ticket, agency-brokered) — a **three-tier ladder** (free content → mid-ticket
course/community → high-ticket brand/speaking), distinct from single-hop "comment-for-link" creators
elsewhere in this corpus.

---

## B. Video post-mortems

Selection per QC_PROTOCOL/task brief: top 5 by views (non-pinned) + 2 lowest genuine own-content
performers (verified by `uploader_id`, **not** the O'Reilly collabs) + 1 O'Reilly collab analyzed
briefly as a sidebar on why guest/collab-hosted content underperforms here.

---

### VIDEO 1 (TOP #1, 1.8M views): "Comment BUILD" — AI content-repurposing tool demo

#### 0. Identity & stats
- URL: instagram.com/reel/DZfgPtFObU1/ | Platform: Instagram Reels | Posted: 2026-06-12 | Length:
  unknown — **DATA GAP**: no matching YouTube cross-post was found for this video (checked by title/
  theme against the full 266-Short catalog), and Instagram's API does not expose duration to `yt-dlp`
  without downloading the video file, which was not done.
- Views: 1.8M `[OBSERVED, ig_harvest grid]`. Likes: **33,065** (1.84% of views) `[OBSERVED, yt-dlp
  direct re-pull, 2026-07-25, HIGH]` — note this **conflicts with the original harvest's recorded
  figure of 904 likes** for this same reel. Comments: 1,741, which **matches the harvest exactly**.
  Given the comment count independently agrees across two different fetch methods (browser scrape vs.
  API pull) while the like count does not, the most likely explanation is a transcription slip in the
  original browser-based harvest (large numbers are easy to misread while scrolling a grid quickly),
  not a genuine change in either direction — this dossier uses the yt-dlp figure (33,065) as primary,
  flagging the discrepancy rather than silently overwriting it.
- Rank: **#1 of 42** genuine (non-owner-excluded) reels in the 48-tile sample, tied with Video 2.

#### 1. Packaging
- Caption opens with the CTA itself, not a teaser: "Comment BUILD and I'll send you the public app
  link & the prompt to make your own!" — payoff and mechanism both stated up front, no curiosity
  withholding on the *offer*, though the tool's actual output is not shown in the caption text (only
  in-video, unobserved — DATA GAP on visual content, caption/comments used as the evidence base).
- Standing credential-forward signature block present at the end of the caption (see Section C) —
  this exact boilerplate paragraph recurs across nearly every post in this sample.

#### 2. Hook (0–3s)
- No verbatim transcript available (DATA GAP — no YouTube proxy, Instagram exposes no subtitle track
  for this post). Best evidence is the caption's opening line, which functions as the written
  equivalent of the spoken hook in her format (her other videos where transcript IS available show the
  spoken hook and the caption's first line are near-identical — see Video 3, 4, 6 below): "Comment
  BUILD and I'll send you the public app link & the prompt to make your own!"
- Taxonomy: **result-first / practical-value hook** combined with an explicit comment-gated CTA —
  per rubric §1.3.2, a bare "comment X" ask with no standalone value would be penalized as engagement
  bait, but here the ask is attached to a fully-described, genuinely useful offer (a working app +
  prompt), which the rubric explicitly distinguishes as compliant, not bait.
- What the viewer sees: [INFERRED from caption's described content, not directly observed] a
  dashboard/workflow screen-recording of the described content-repurposing tool, per the caption's "I
  can review, edit & schedule posts from the dashboard" description.

#### 3. Structure & retention engineering
- DATA GAP on shot-level beat map (no transcript/video observed). Caption-level structure: CTA hook →
  personal-authority framing ("As someone who's been teaching how AI works in video format for years,
  I have *tons* of content to repurpose...") → tool description → credential-forward signature close.
- Open loop: the "comment BUILD" promise is the loop; it resolves off-platform (via DM), not within
  the video itself — a structural pattern distinct from the in-video loop-closure the rubric (§2.6.1)
  describes for pure-content videos. This is a funnel-video, not a pure-education video.

#### 4. Value proposition
- Walk-away value: awareness of a specific, working AI-content-repurposing workflow (video → tweets/
  threads), obtainable via DM.
- Value class: tool discovery + copyable workflow (gated, not directly shown in full).
- Specificity: high on the *offer* (a real system, reviewable/editable dashboard, continuously
  learning from her edits), lower on *in-caption* specificity since the actual prompt/build steps are
  gated behind the comment-CTA rather than shown.

#### 5. Psychology scoring
- STEPPS: **Practical value** (a genuinely useful, described workflow) + **Social currency** (getting
  early/exclusive access to "the public app link" by commenting, a mild insider-access framing).
  **Triggers**: content creators/anyone who repurposes video into text is a broad, recurring-task
  audience.
- Primary emotion + arousal: mild practical-interest, moderate arousal (a genuinely time-saving
  workflow claim).
- Save/send trigger: high — "someone who makes a lot of video content and needs to repurpose it" is a
  specific, nameable addressee.
- Top comments are **overwhelmingly single-word "Build"** repeats `[OBSERVED, yt-dlp comments field]`
  — direct evidence the comment-CTA mechanic is working exactly as designed, converting viewers into a
  comment action at scale (1,741 comments on 1.8M views, a 0.097% comment rate, itself a healthy
  outlier — compare Video 4's 0.007% comment rate on a similar view count).

#### 6. CTA & funnel mechanics
- Explicit, primary CTA: "Comment BUILD and I'll send you the public app link & the prompt."
- Comment-bait mechanics: compliant per rubric §1.3.2 (attached to real, described value, not a bare
  ask) — see Section 2 above.
- Funnel position: pure top-of-funnel lead capture, feeding the DM/lead-magnet layer of the funnel map
  (Section A).

#### 7. Replicability verdict
- Template: (1) build or find a genuinely useful, narrow AI workflow, (2) lead the caption with the
  exact CTA mechanic and payoff in one sentence, (3) attach the standing credential signature so cold
  viewers get an instant trust anchor, (4) let comments do the funnel work rather than a bio link.
- Commodity vs. unfair advantage: the CTA mechanic is fully commodity (any creator can run
  "comment X"); the unfair advantage is having actually built a working, demoable tool to give away —
  this requires real technical capability, which is exactly Harper's claimed differentiator.
- Difficulty for Tangent: **MED** — the comment-CTA mechanic itself is low-difficulty, but it is only
  as credible as the thing being given away; a fine-art/gallery brand would need an equivalently real,
  specific giveaway (e.g., an actual edit recipe/preset, not a vague "tips" PDF) to reproduce this
  pattern's credibility.

#### 8. Why it won
The load-bearing factor is a **credible, specific give-away wrapped in a comment-gated CTA**, which
converts Instagram's comment-count ranking signal (weighted higher than likes for cold reach, per
rubric §1.1.2) into a self-reinforcing loop: every comment is itself a public testimonial visible to
the next scroller ("look how many people want this"), a Social Currency/Public-proof mechanism (rubric
§2.2). Secondary factor: the credential-forward signature is present, giving cold viewers (most of
1.8M views, on a 605K-follower account) a reason to trust that "BUILD" is worth commenting for. No
clear luck/timing component was identified — this reads as a repeatable format, not a news-cycle
spike (contrast Video 4).

#### Sources
- https://www.instagram.com/reel/DZfgPtFObU1/ (metadata, caption, comments — yt-dlp, 2026-07-25)
- `ig_harvest/harpercarrollai.md` (original grid position, view count)

---

### VIDEO 2 (TOP #2, 1.8M views, tied with Video 1): "If you watch one video about AI, let it be this one" — Claude Code install tutorial

#### 0. Identity & stats
- URL: instagram.com/reel/DVbM3sBjl26/ | Posted: 2026-03-03 | Length: unknown — **DATA GAP**, same
  reason as Video 1 (no YouTube cross-post found).
- Views: 1.8M. Likes: **7,171** `[OBSERVED, yt-dlp, 2026-07-25]` — again **conflicts with the harvest's
  recorded 5,358**; comments **904 match exactly** across both methods, same discrepancy-resolution
  logic as Video 1 applied here (yt-dlp figure used as primary, discrepancy flagged, not fabricated
  away).
- Rank: **#1 of 42**, tied with Video 1.

#### 1. Packaging
- Caption opens with a maximal-stakes claim: "If you watch one video about AI, let it be this one." —
  a bold, singular-importance framing (rubric §3.1 "bold claim" taxonomy), immediately followed by the
  actual payoff: exact terminal install commands for Claude Code.
- Tagged `@claudeai #ClaudePartner` — this is **sponsored/partner content sitting at the very top of
  her organic catalog**, tied for the #1 spot.

#### 2. Hook (0–3s)
- No verbatim transcript (DATA GAP, same reason as Video 1). Caption stands in: "If you watch one
  video about AI, let it be this one." followed immediately by the literal copy-paste command: `curl
  -fsSL https://claude.ai/install.sh | bash`.
- Taxonomy: bold-claim hook, escalated by giving the actual payoff (the install command) directly in
  the caption rather than gating it — a lower-friction variant than Video 1's DM-gated approach,
  running an "OR comment START and I'll DM you the commands" as a *secondary*, not primary, path.
- What the viewer sees: [INFERRED] a terminal window installation walkthrough, consistent with the
  caption's step-by-step Mac/Windows commands.

#### 3. Structure & retention engineering
- Caption-level structure: maximal-stakes hook → exact copy-paste commands (Mac AND Windows given,
  removing a common friction point) → alternate DM path for less technical viewers → credential-forward
  signature, explicitly framed around **counter-misinformation** positioning ("It's hard for me to see
  so much misinformation about AI online, so I'm here to provide trustworthy AI education").
- One-idea discipline: yes — a single action (install Claude Code) is the entire payoff, no scope
  creep into other topics.

#### 4. Value proposition
- Walk-away value: a working, immediately-executable install command for a genuinely useful
  developer tool — one of the highest-specificity payoffs in this entire sample (exact command,
  copy-pasteable, platform-branching for Mac/Windows).
- Value class: pure copyable workflow.
- Specificity: very high — this is a "send this to my technical friend who hasn't tried Claude Code
  yet" video almost by design.

#### 5. Psychology scoring
- STEPPS: **Practical value** dominant (a genuinely useful, zero-ambiguity technical payoff).
  **Social currency**: being seen as the early adopter/explainer of a hot developer tool. **Triggers**:
  moderate — "wanting to try Claude Code" is a narrower, more technical trigger than Video 1's broader
  content-creator audience.
- Top comments `[OBSERVED, yt-dlp]`: "Start," "Start," "🔥," "Absolutely love Claude" — short,
  low-effort but directionally positive/action-taking comments, consistent with a technical,
  low-controversy topic.
- Save/send trigger: very high specificity — a copy-paste command is inherently the kind of content
  people bookmark or forward directly.

#### 6. CTA & funnel mechanics
- Dual-path CTA: primary path is self-serve (copy the command directly from the caption, no DM
  needed); secondary path is "comment START" for viewers who want it DM'd.
- This dual-path design is notable: it doesn't force a funnel step for viewers who don't need one,
  while still capturing a comment-based engagement signal from viewers who do — arguably a more
  sophisticated CTA design than Video 1's single DM-gated path.
- Funnel position: **branded partner content** (`#ClaudePartner`) functioning simultaneously as
  organic top-of-funnel content — see Section 8.

#### 7. Replicability verdict
- Template: (1) pick a tool with a genuinely simple, copy-pasteable onboarding step, (2) put the
  exact command directly in the caption (remove the DM-gate friction entirely for technical content),
  (3) offer a DM-path fallback for less technical viewers, (4) close with a mission-driven
  (anti-misinformation) credential signature.
- Commodity vs. unfair advantage: the format is commodity; the unfair advantage is an actual brand
  partnership with the tool vendor (Anthropic), giving legitimacy and likely coordinated
  amplification that a non-partnered creator covering the same tool would lack.
- Difficulty for Tangent: **LOW** mechanically (any tool with a simple install step could be covered
  this way) but **HIGH** to replicate the partnership legitimacy specifically.

#### 8. Why it won
This is the dossier's clearest evidence that **partner/sponsored content is not inherently a
reach-suppressed category on this account** — unlike the ad-boosted-view/near-zero-engagement pattern
documented elsewhere in this corpus (tiffintech, networkchuck), this `#ClaudePartner` post ties for
the single highest view count in the entire 42-video genuine sample, with a real engagement profile
(0.40% like rate, 0.05% comment rate — modest but not anomalous). The load-bearing factor is topic
selection: Claude Code was, at time of posting (Mar 2026), a high-interest, high-utility developer
tool, and the video removes every possible friction point (exact commands, both OSes, DM fallback) —
a "zero-excuse-not-to-try-it" design. Secondary factor: partner-brand amplification/promotion cannot
be ruled out as contributing to reach, though it was not independently confirmable from this session's
data (DATA GAP on whether Anthropic cross-promoted this specific post).

#### Sources
- https://www.instagram.com/reel/DVbM3sBjl26/ (metadata, caption, comments — yt-dlp, 2026-07-25)

---

### VIDEO 3 (TOP #3, 866K views): "How does AI actually work?" — Anthropic/Claude partner series launch, Ep. 1

#### 0. Identity & stats
- URL: instagram.com/reel/DbD8-40Owbv/ | Posted: 2026-07-21 | Length: **119s** `[OBSERVED via
  YouTube cross-post proxy, w3SLz6carLw, posted the same calendar day (2026-07-21) on
  youtube.com/@harpercarrollai, HIGH confidence this is the same script given the exact date match]`.
- Views: 866K `[OBSERVED, ig_harvest]`. Likes: **3** — a clear anomaly, not a real count; comments:
  **532** `[OBSERVED, yt-dlp]`. See discussion below — this dossier does **not** report "3 likes" as a
  real figure.
- Rank: **#3 of 42.**

#### 1. Packaging
- Caption: "How does AI actually work? Let's talk about what's happening under the hood of chatbot
  models like Claude... Thrilled about this new series with @claudeai. Stay tuned for episode 2."
- This is an explicit **series launch**, tagged `@claudeai #ClaudePartner` — episode 1 of a new
  branded numbered-series format, structurally identical in spirit to "10 Days of AI Basics" (see
  Section C) but this time as paid brand content rather than organic.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via transcript]`: **"I'm confident that this might be the most important video
  that you'll see in a while. Let's talk about how AI actually works because it will shape how you use
  it, how you think about it, and make informed decisions about it."**
- Taxonomy: maximal-stakes bold claim, immediately followed (0:10) by the credential-forward line:
  "I'm a Stanford computer scientist for AI who's been building AI systems for over a decade," then
  the partner framing: "I'm teaming up with Anthropic, the team behind Claude, for a series, and for
  day one, we're looking under the hood."
- What the viewer sees: [INFERRED from transcript content — visual not directly observed] a
  probability-distribution/token-prediction visual demo, given the transcript's detailed walk-through
  of an example ("cat"/"hat" completion, shifted by adding "Dr. Seuss" to the prompt).

#### 3. Structure & retention engineering
- Beat map (from transcript, no exact in-video timestamps beyond auto-caption chunks): Hook + stakes
  claim (0:00–0:10) → credential + partner framing (0:10–0:19) → core concept: LLMs as "word/token
  generators" producing a probability distribution (0:19–0:48) → worked example: cat/hat with
  Dr.-Seuss-shifted probabilities (0:48–1:32) → payoff: "everything Claude... knows about you is just
  added info into its prompt behind the scenes" (1:32–1:53) → close: "follow for the next episode in
  my series with Anthropic."
- Open loop: "we're looking under the hood" (hook) is closed by the probability-machine explanation;
  a second-order loop ("episode 2") is deliberately left open at the close — an explicit
  series/appointment-viewing hook (rubric §3.4.2).
- One idea per video: yes — a single mental model (LLMs as probabilistic token generators) delivered
  with one worked example, textbook rubric §3.2 compliance.
- Pacing: [INFERRED] moderate — the transcript implies at least one screen/visual change (the cat/hat
  example) mid-video, consistent with her other tutorial-style content.

#### 4. Value proposition
- Walk-away value: a genuinely correct, simplified mental model for how LLMs generate text
  (probability distribution over tokens, sampling, prompt-conditioning) — this is real technical
  content, not marketing fluff, despite being sponsored.
- Value class: conceptual/foundational education.
- Specificity: high — a concrete worked example (cat/hat/Dr. Seuss) rather than pure abstraction.

#### 5. Psychology scoring
- STEPPS: **Practical value** (genuinely useful mental model) + **Social currency** (being early to a
  new Anthropic-partnered series, a "before everyone else" positioning). **Triggers**: "how does my
  chatbot actually work" is a broad, frequently-recurring curiosity trigger given near-universal
  chatbot use.
- Primary emotion + arousal: intellectual curiosity/clarity-seeking, moderate arousal — this is
  calm-useful register (per the user's own memory of Harper's brand: "her calm, research-based
  teaching style"), not awe or outrage-driven.
- Top comments `[OBSERVED, yt-dlp]` are dominated by single-word "Guide" replies (14 of 15 sampled
  comments), confirming the comment-CTA funnel ("comment GUIDE") is the primary engagement driver
  here, similar to Video 1's "Build" pattern — genuine topical engagement (e.g., "Markov Chains?" from
  one commenter) is present but a minority.
- **Like-count anomaly**: like_count returns as "3" via `yt-dlp`, which is not credible on an 866K-view
  post with 532 real comments. The most likely explanation `[INFERRED, MED confidence]` is that this
  specific post has Instagram's per-post "hide like count" setting enabled (a real, user-facing IG
  feature), causing the API to return a placeholder/sample value rather than the true total — this
  pattern recurs on 3 other posts in this sample (Videos 4, and two flop candidates checked but not
  selected), all with otherwise-plausible comment counts, and does **not** correlate cleanly with post
  date, ruling out a simple platform-wide API change as the explanation. This is flagged, not
  resolved — DATA GAP on true like count for this video.

#### 6. CTA & funnel mechanics
- CTA: "comment GUIDE and I'll share my (free) video walkthrough guide."
- Funnel position: simultaneously top-of-funnel (new series launch, follow-for-episode-2) and branded
  content (Anthropic partnership) — a dual-purpose video.

#### 7. Replicability verdict
- Template: (1) launch a numbered series with a brand partner, (2) open with a maximal-stakes claim,
  (3) state the credential + partner framing back-to-back, (4) deliver one genuinely correct,
  simplified concept with a concrete worked example, (5) close with both a lead-magnet CTA and a
  "follow for episode 2" appointment-viewing hook.
- Commodity vs. unfair advantage: the structural template is commodity; the unfair advantage is
  having an actual brand partnership with the subject-matter company (Anthropic explaining Anthropic's
  own product category) plus genuine technical fluency to explain it correctly.
- Difficulty for Tangent: **N/A/HIGH** — this specific mechanic requires both a technical-authority
  positioning and a brand relationship with an AI company, neither of which map onto a fine-art
  gallery brand; the *transferable* lesson is narrower: pairing a numbered-series commitment with a
  named external partner for credibility.

#### 8. Why it won
Load-bearing factor: **the credential-forward hook plus a named, verifiable brand partnership
(Anthropic) compound into an unusually strong trust signal for a cold, algorithmically-served
audience** — this reproduces the exact mechanism Video 2 demonstrated (partner content outperforming
the "sponsored content underperforms" prior from elsewhere in this corpus). Secondary factor: the
content genuinely teaches something correct and useful rather than being disguised advertising,
which likely protects it from the anti-clickbait/engagement-bait penalties the rubric describes
(§1.3.2) — the comment-CTA is attached to a real 2-minute lesson, not a bare ask. No clear luck/timing
component beyond general AI-topic tailwind.

#### Sources
- https://www.instagram.com/reel/DbD8-40Owbv/ (metadata, caption, comments — yt-dlp, 2026-07-25)
- https://www.youtube.com/shorts/w3SLz6carLw (verbatim transcript proxy — yt-dlp auto-subs, 2026-07-25)

---

### VIDEO 4 (TOP #4, 794K views): "ChatGPT Work is here!!" — launch-day explainer, OpenAI partner

#### 0. Identity & stats
- URL: instagram.com/reel/Dan0IIuJP7K/ | Posted: 2026-07-10 | Length: **70s** `[OBSERVED via YouTube
  cross-post proxy, VIWI4nilOcw, same-day match, HIGH confidence]`.
- Views: 794K. Likes: **3** (same hide-like-count anomaly as Video 3 — DATA GAP, not reported as
  real). Comments: **58** — a notably **low** comment rate (0.0073%) for a top-5 video, well below
  Video 1's 0.097% or Video 3's 0.061%.
- Rank: **#4 of 42.**

#### 1. Packaging
- Caption: "ChatGPT Work is here!! Along with GPT 5.6, which both launched today." — a same-day
  news-drop, tagged `@ChatGPT #ChatGPT_Partner`.
- This is the account's clearest **trend-velocity / news-cycle-surfing** post in the sample (rubric
  §3.4.1/§4): posted the literal day of the product launch.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via transcript]`: **"ChatGPT Work was just released, which brings the power of
  agents directly into ChatGPT. This means you can now turn an idea into a finished output directly in
  the desktop app."**
- Taxonomy: breaking-news/bold-claim hook, immediately followed by a concrete "what changed" framing
  (three ChatGPT desktop modes: Chat, Codex, now Work).
- What the viewer sees: [INFERRED] ChatGPT desktop app screen-recording, per the transcript's direct
  reference to "the Work section in the ChatGPT desktop app."

#### 3. Structure & retention engineering
- Beat map: Hook/news-drop (0:00–0:11) → context: prior two modes vs. new third mode (0:11–0:25) →
  concrete use-case walkthrough: building a product from customer feedback, connecting tools, scanning
  interviews, sourcing suppliers, building a store (0:25–0:46) → capability callout: GPT-5.6 "designed
  to be good at design" (0:46–0:59) → close: availability details + soft CTA ("try Chat GPT Work in
  the Chat GPT desktop app") (0:59–1:10).
- No explicit open-loop/cliffhanger structure — this is a single-payoff news explainer, not a
  series-building video (contrast Video 3).
- One idea per video: borderline — the "three modes now four things to know" (Work launch + GPT-5.6
  design capability) is really two adjacent facts bundled under one launch-day frame, a mild rubric
  §3.2 drift similar to patterns noted in sibling dossiers.

#### 4. Value proposition
- Walk-away value: awareness of a new product tier and one illustrative use case; no exact prompt or
  step-by-step shown (softer specificity than Video 1 or 2).
- Value class: pure news/awareness, lower on copyable-workflow specificity than the account's top-2.

#### 5. Psychology scoring
- STEPPS: **Triggers** — the single strongest news-cycle trigger in this sample (same-day major
  product launch). **Social currency**: being an early, credentialed explainer of a major release.
  **Emotion**: informational/awe-adjacent but restrained — no explicit "blow your mind"-style language
  in the transcript, consistent with her calm-register brand.
- Top comments `[OBSERVED, yt-dlp]` are unusually **substantive and mixed/critical** for this
  account: "gpt 5.6 is good at coding but in design, it's nothing complicated to Kimi or claude,"
  "5.6 is worse than 5.5 at image generation. It takes me many iterations where as 5.5 it took me just
  [one]" — genuine product-quality debate, not comment-bait keyword replies. This is qualitatively
  different from Videos 1 and 3's "Build"/"Guide" comment floods.
- This directly explains the low comment RATE relative to peers: the CTA here is soft ("try it in the
  app," no comment-keyword mechanic), so comments reflect organic reaction rather than a manufactured
  funnel action — a useful natural-experiment contrast within this account's own catalog.

#### 6. CTA & funnel mechanics
- No comment-keyword CTA — the only call to action is "try Chat GPT Work in the Chat GPT desktop
  app," i.e., driving usage of the partner's product directly rather than Harper's own funnel.
- Funnel position: this video's is the only one of the top-5 that does **not** feed Harper's own
  lead-magnet/DM funnel — it is closer to pure sponsored-brand-awareness content, consistent with its
  comparatively low (though still real) comment engagement.

#### 7. Replicability verdict
- Template: (1) monitor major AI product launches closely, (2) publish same-day, (3) name the exact
  new capability/mode in the first sentence, (4) walk through one concrete use case, (5) skip the
  comment-CTA funnel mechanic when the goal is pure brand-awareness content for a partner.
- Commodity vs. unfair advantage: the news-reactive format is commodity (any AI creator can do
  launch-day explainers); the unfair advantage is speed-to-publish (same-day) plus an existing partner
  relationship with OpenAI specifically.
- Difficulty for Tangent: **N/A** for the AI-news angle (off-mission for a gallery brand), but the
  *transferable* lesson — a fast-turnaround, same-day reaction format to a relevant industry event —
  is a viable, low-cost content lane in any niche with a real news cycle (e.g., major photography-gear
  launches, gallery-world events).

#### 8. Why it won
Load-bearing factor: **trend-velocity** (rubric §3.4.1/§4) — this is a major, single-day news event
covered same-day by a credentialed, partnered source, which the algorithm's early-velocity "audition"
window (rubric §1.1.3) likely rewards heavily given a same-day burst of searches/curiosity around the
exact product named. Secondary factor: the OpenAI partnership itself likely provided some
amplification (unconfirmed, DATA GAP). The comparatively low comment rate versus Videos 1 and 3
is best explained by CTA design (no comment-keyword mechanic here), not by weaker underlying interest
— view count remained high because reach here is news-driven, not comment-loop-driven.

#### Sources
- https://www.instagram.com/reel/Dan0IIuJP7K/ (metadata, caption, comments — yt-dlp, 2026-07-25)
- https://www.youtube.com/shorts/VIWI4nilOcw (verbatim transcript proxy — yt-dlp auto-subs, 2026-07-25)

---

### VIDEO 5 (TOP #5, 615K views): "Sending you love. You got this!!" — reassurance/comfort post + free-course funnel

#### 0. Identity & stats
- URL: instagram.com/reel/DYPXSQ4hPdF/ | Posted: 2026-05-12 | Length: **~175s if the YouTube proxy
  match is correct** `[MED confidence — the best-matching YouTube video by title/theme,
  QJ6dyST-WuE ("A message about what's coming with AI - sending you love. You got this!"), is dated
  2026-05-19, seven days after the Instagram post, not the same day. This is treated as a probable but
  not confirmed same-script match — duration and any transcript-level claims from this proxy are
  logged as MED confidence, not HIGH, unlike Videos 3, 4, and 6's exact-date matches.]`
- Views: 615K. Likes: **13,267** (2.16%) `[OBSERVED, yt-dlp, no anomaly on this one]`. Comments:
  **6,402** (1.04% of views) — by far the **highest comment rate of any video in this sample**,
  roughly 10–14x the rate seen on Videos 3–4.
- Rank: **#5 of 42.**

#### 1. Packaging
- Caption: "Sending you love. You got this!! And I'm here to help." — an emotionally-toned,
  non-technical opener, unusual for this account's typical bold-claim/news-drop register.
- No specific topic/product named in the caption — this is a reassurance/community-tone post, not an
  educational or news post.

#### 2. Hook
- Caption-level hook only (no confirmed verbatim transcript — see duration caveat above): "Sending
  you love. You got this!!"
- Taxonomy: an outlier in this account's catalog — closer to **emotional/parasocial-bonding content**
  (rubric §2.4.1) than any of the bold-claim/news/tool-demo hooks seen in Videos 1–4. Functions as a
  direct-address, self-disclosure-adjacent moment that likely strengthens the parasocial bond
  independent of new information delivered.

#### 3. Structure & retention engineering
- Caption structure: emotional opener → credential-forward signature ("I'm here to answer your
  questions about AI... You've got this!") → the actual funnel offer: "If you want a complete free AI
  course, comment FREE and I'll send you the free video walkthrough guide... 11 modules... gamified
  web app."
- This video pairs **emotional reassurance content with the account's most fully-built lead magnet**
  (an 11-module guide + a gamified tracking app), a notably more developed funnel offer than the
  single-tool giveaways in Videos 1–2.

#### 4. Value proposition
- Walk-away value: emotional reassurance ("AI isn't something to be scared of, I'm here to help") +
  access to a structured, multi-module free course if the viewer takes the CTA action.
- Value class: identity/emotional + gated structured-learning value — a different value class than any
  other video in this sample.

#### 5. Psychology scoring
- STEPPS: **Emotion** is the dominant, near-exclusive lever here (contrast every other video in this
  sample, where Practical Value dominates) — directly targets AI-anxiety, an emotionally-charged,
  moderate-to-high-arousal negative state per rubric §2.3, and offers resolution/reassurance rather
  than information. **Parasocial bonding** (§2.4.1) is unusually explicit — direct second-person
  address, no new facts, pure relationship-affirming content.
- The **1.04% comment rate is the single strongest engagement-rate data point in this entire
  dossier**, driven almost entirely by "Free, thank you" replies to the comment-FREE CTA `[OBSERVED,
  yt-dlp comments sample: "Free, thank you" appears 3 of the first 6 sampled comments]`.
- One top comment is worth flagging for the credential-authority analysis: **"Who is using wired
  headphones now a DAYS? Specially with two AI degrees from Stanford 😂😂😂😂"** `[OBSERVED, yt-dlp]`
  — even a mocking/pushback comment routes its joke through her Stanford credential, evidence the
  credential-branding has fully saturated audience perception (see Section C).

#### 6. CTA & funnel mechanics
- CTA: "comment FREE and I'll send you the free video walkthrough guide."
- This is the account's most fully-articulated lead-magnet offer in the sample (11 modules + gamified
  progress app vs. Video 1's single app link or Video 3's unspecified "guide").
- Funnel position: explicitly top-of-funnel-to-mid-funnel bridge — converts an emotional/parasocial
  moment directly into a structured-course opt-in.

#### 7. Replicability verdict
- Template: (1) periodically post pure emotional/reassurance content unconnected to any specific news
  or tool, (2) use it as the vehicle for the account's most-developed lead magnet (not the newest
  content), (3) keep the ask simple (one keyword).
- Commodity vs. unfair advantage: fully commodity emotionally, but only works if the account has
  already built enough parasocial trust (via the credential-forward, calm-teaching brand) for
  "sending you love" not to feel hollow/incongruous — this depends on everything else in the account's
  positioning being consistent first.
- Difficulty for Tangent: **LOW-MED** — directly transferable to a gallery brand ("this is your sign to
  finally hang real art in your home, you've got this") paired with a comparably well-built lead
  magnet, provided the account has already established enough of a trusted voice for it to land.

#### 8. Why it won
Load-bearing factor: **emotional/parasocial content, novel relative to the account's typical
register, paired with the single best-developed lead magnet in the sample** — the highest-ever
comment rate in this dossier is best explained by the CTA's simplicity (one keyword, "FREE") combined
with an audience primed to reciprocate warmth after a direct emotional address, a mechanism distinct
from the practical-value/news-hook mechanisms driving Videos 1–4. This is the strongest single-video
evidence that this account's engine is not purely "credential + information" — an emotional,
non-informational register, deployed occasionally, outperforms most of the account's median content
on both views (615K, top-5) and by far on comment rate.

#### Sources
- https://www.instagram.com/reel/DYPXSQ4hPdF/ (metadata, caption, comments — yt-dlp, 2026-07-25)
- https://www.youtube.com/shorts/QJ6dyST-WuE (probable, date-uncertain proxy — yt-dlp, 2026-07-25, MED confidence)

---

### VIDEO 6 (FLOP, 2nd-lowest of 2, 44.5K views): Meta Superintelligence Labs model explainer

#### 0. Identity & stats
- URL: instagram.com/reel/DW9gguSDgRM/ | Posted: 2026-04-10 | Length: **84s** `[OBSERVED via YouTube
  cross-post proxy, nALGUsjwqNk, same-day match, HIGH confidence]`.
- Views: 44.5K `[OBSERVED, ig_harvest]`. Likes: 685 (1.54%). Comments: 32 (0.072%) `[OBSERVED,
  yt-dlp, no like-count anomaly on this one]`.
- Rank: **#41 of 42** genuine (second-lowest), confirmed genuinely her own content via `uploader_id
  5787807072` (not a collab) `[OBSERVED, yt-dlp, this session]`. 794K/615K-view posts in the same
  sample were 14–18x this video's views.

#### 1. Packaging
- Caption: "The innovations of @Meta's new groundbreaking frontier model, the first out of its
  @Meta.AI Superintelligence Labs" — a corporate/technical framing, no bold personal-stakes claim, no
  news-drop urgency phrasing (contrast Video 4's "is here!!").
- No brand-partner tag — this is unsponsored, standard educational content.

#### 2. Hook (0–3s)
- Verbatim `[OBSERVED via transcript]`: **"Meta's stock recently rose because it just released its
  first super intelligence model, which kind of made waves because the model outperforms almost every
  frontier model like Claude and ChatGPT on major benchmarks."**
- Taxonomy: news/context-setting hook, but softer than Video 4's — leads with the STOCK PRICE
  reaction rather than a direct claim about what the viewer will learn, and the phrase "kind of made
  waves" is hedged language, weaker than Video 4's unhedged "is here!!" or Video 3's "most important
  video you'll see in a while."
- What the viewer sees: [INFERRED, transcript references "on this graph, we can see..."] a benchmark
  chart showing accuracy scaling with number of parallel "thinking agents" (1, 2, 4, 16).

#### 3. Structure & retention engineering
- Beat map: Hook/context (0:00–0:13) → tie-back to Meta's earlier high-profile hires and the Scale AI
  acquisition, cross-referencing a prior video (0:13–0:25) → technical innovation #1: parallel-agent
  reasoning to reduce latency (0:25–0:57) → graph evidence: accuracy vs. number of agents (0:57–1:09)
  → close: "there are more technological innovations I want to talk about... give me a follow, share
  this to someone" (1:09–1:24).
- Open loop: explicitly promises "more technological innovations... in this series that I'm going to
  make" but the loop is deferred to a future, unnamed video, not resolved within this one — a weaker
  version of Video 3's explicit "episode 2" framing (no series name, no numbering).
- One idea per video: mostly yes (parallel-agent reasoning), though the Scale-AI-acquisition tie-back
  is a mild digression into adjacent content.

#### 4. Value proposition
- Walk-away value: one specific technical fact (Meta's model uses parallel agent reasoning to cut
  latency while preserving accuracy gains from "thinking"), illustrated with a real benchmark graph
  reference.
- Value class: technical news + light educational content — genuinely substantive, comparable in
  rigor to Video 3, just without partner backing or a defined series identity.
- Specificity: good — names the specific mechanism (parallel agents) and references concrete
  benchmark behavior (1/2/4/16 agent scaling).

#### 5. Psychology scoring
- STEPPS: **Practical/informational value** present but narrower-audience than the top-5 (requires
  pre-existing interest in frontier-model internals, a more technical sub-slice of her audience than
  "how does AI work" or "install this tool"). **Triggers**: weaker — no near-universal recurring
  trigger comparable to Video 2's "you have Claude Code" or Video 1's "you make content."
- Top comments `[OBSERVED, yt-dlp]` are unusually **substantive and skeptical/critical** for this
  account: "Zuck is literally in court for pushing tech that knowingly harmed kids. It's not the time
  to be pushing..."; "Are we still trusting meta?"; "Harper's vibe conveys enthusiasm and optimism. I
  find this disconcerting. AI used to be 'fun', but..." — a materially more critical comment
  environment than any top-5 video, suggesting some audience friction specifically around
  Meta-positive framing, independent of the video's technical quality.
- No comment-keyword CTA present — comments here are unprompted, organic reactions (like Video 4),
  which likely explains both the lower volume and the more substantive/critical content.

#### 6. CTA & funnel mechanics
- Soft CTA only: "give me a follow, share this to someone who might find it interesting."
- No lead-magnet/DM funnel attached — this video does not feed the course/guide funnel at all.

#### 7. Replicability verdict
- Template: technical-innovation explainer tied to a stock-price/business hook, with a benchmark
  graph as evidence and a soft follow/share CTA.
- Anti-pattern to note: hedged hook language ("kind of made waves") and a company (Meta) that appears
  to generate above-average audience skepticism/friction in the comments are both worth avoiding if
  the goal is view count, even though the content itself is technically solid.
- Difficulty for Tangent: **N/A** (off-mission), but the lesson — a genuinely well-made, technically
  correct video can still underperform if (a) the hook is hedged rather than declarative and (b) the
  subject matter carries audience-trust friction — is transferable.

#### 8. Why it lost (delta vs. top-5)
The explicit delta versus Videos 1–4: **no comment-keyword CTA** (removing the account's most reliable
engagement-volume driver), a **hedged rather than declarative hook** ("kind of made waves" vs. "is
here!!" / "most important video you'll see"), **no brand-partner backing/amplification**, and a
**narrower, more technical trigger surface** (frontier-model internals vs. "everyone who makes
content" or "everyone with a chatbot"). The substantive-but-critical comment tenor also suggests some
topic-specific (Meta-related) audience friction that is independent of production quality — this is a
well-made video whose underperformance is best explained by CTA/hook-design choices and topic-trust
dynamics, not a quality gap versus the top-5.

#### Sources
- https://www.instagram.com/reel/DW9gguSDgRM/ (metadata, caption, comments — yt-dlp, 2026-07-25)
- https://www.youtube.com/shorts/nALGUsjwqNk (verbatim transcript proxy — yt-dlp auto-subs, 2026-07-25)

---

### VIDEO 7 (FLOP, lowest of 2, 36.2K views — lowest genuine post in the sample): "My festival story" — ServiceNow-partner post

#### 0. Identity & stats
- URL: instagram.com/reel/DX9nDB_pdBF/ | Posted: 2026-05-05 | Length: unknown — **DATA GAP**, no
  YouTube cross-post match found.
- Views: 36.2K `[OBSERVED, ig_harvest]` — the **lowest-viewed genuinely-own-content post in the
  48-tile sample**, confirmed via `uploader_id 5787807072` `[OBSERVED, yt-dlp, this session]`, one
  tile below the previous harvest's estimated floor.
- Likes: 492 (1.36%). Comments: 31 (0.086%) `[OBSERVED, yt-dlp]`.
- Rank: **#42 of 42** — dead last among genuine posts in this sample.

#### 1. Packaging
- Caption, in full: **"My festival story 🥲 #Know26 #ServiceNowPartner"** — by a wide margin the
  **shortest caption of any video analyzed in this dossier** (a handful of words vs. multiple
  paragraphs on every other post). Critically, it **omits the standing credential-forward signature
  block** ("If we haven't met yet, I'm Harper...") that appears on every other post in this sample —
  the one structural element this account almost never skips.
- No stated topic, no promise, no visible payoff description — the caption alone gives a cold viewer
  no reason to click beyond curiosity about an emoji ("🥲").
- Tagged `#ServiceNowPartner` and `#Know26` (a conference/event hashtag) — this is **sponsored
  content, self-posted** (unlike the O'Reilly sidebar below, this one lives on Harper's own account),
  making it a useful middle case between fully-organic and fully-guest-hosted content.

#### 2. Hook (0–3s)
- No transcript available (DATA GAP). Best evidence is the caption itself, which is unusually
  vague/personal ("story," "🥲") compared to every other video's declarative, payoff-forward opening.
- Taxonomy: [INFERRED from caption tone] appears to be personal-narrative/anecdote framing rather
  than any of the bold-claim/news/tool-demo taxonomies that dominate her top performers — an outlier
  register for this account, though not the warm "sending you love" register of Video 5 either
  (the 🥲 emoji suggests a bittersweet/nostalgic tone, distinct from Video 5's affirming warmth).

#### 3. Structure & retention engineering
- DATA GAP — no transcript or shot-level detail available; caption gives essentially no structural
  information to analyze, itself a notable finding (see Section 8).

#### 4. Value proposition
- Walk-away value: unclear from available evidence — likely a personal/behind-the-scenes moment tied
  to a ServiceNow conference (Know26), not a teachable AI concept or tool.
- Value class: [INFERRED] personal/relatability content, the weakest-specified value proposition of
  any video in this dossier.

#### 5. Psychology scoring
- STEPPS: none of the six levers are clearly activated by the caption alone — no stated practical
  value, no explicit emotional hook (beyond a single ambiguous emoji), no social currency framing, no
  trigger, no story structure visible in text, no public/observable-popularity element.
- Top comments `[OBSERVED, yt-dlp]` are notably **generic and topic-mismatched** relative to a
  "festival story" theme — e.g., "Please report back re your opinions gleaned from the conference!"
  (the only comment actually engaging with the stated Know26/conference context), alongside unrelated
  reactions like "Perfect use case for automation, not even AI" and "It's not a lack of
  capacity/capabilities, it's a monopoly problem" — suggesting the small comment pool skews toward
  generic AI-adjacent chatter rather than reactions to the specific content, consistent with a video
  that gave viewers little specific to respond to.

#### 6. CTA & funnel mechanics
- No CTA of any kind identified in the caption — no comment-keyword mechanic, no follow ask, no link
  reference.
- Funnel position: does not feed any part of the funnel map in Section A — appears to be pure
  brand-partnership-obligation content (a "we were at your event" acknowledgment post) rather than a
  designed-to-perform video.

#### 7. Replicability verdict
- Anti-pattern to avoid, not a template to copy: omitting the credential-forward trust anchor, giving
  no specific payoff or promise, and using an ambiguous personal-narrative hook all run directly
  counter to every mechanism that makes this account's top-5 work.
- Difficulty for Tangent: **N/A** — this is a lesson in what not to do (brand-obligation posts that
  skip the account's own proven structural elements), not a replicable format.

#### 8. Why it lost (delta vs. top-5)
This is the dossier's cleanest single-video case for **structural discipline mattering more than
topic**: this video breaks nearly every pattern the top-5 share — no credential signature, no stated
payoff, no CTA, no declarative hook, minimal caption effort — and lands dead last in the 42-video
genuine sample despite being posted by the same account, same follower base, same general era (May
2026, squarely inside the window of the other top/flop videos analyzed here). The explicit delta
versus Video 6 (the second-lowest performer, which at least retains a real technical hook and
substantive content) is **caption/structural effort itself**: Video 6 still followed the account's
playbook and landed at 44.5K; this video abandoned nearly all of it and landed at 36.2K, the sample's
floor. Notably, like the O'Reilly sidebar below, this is *also* branded/sponsored content
(`#ServiceNowPartner`) — but unlike Videos 2–3's partner posts (which retained the full credential +
declarative-hook + CTA structure and landed in the top-5), this one dropped the structure and
underperformed, suggesting the earlier finding ("partner content isn't inherently suppressed here")
has a boundary condition: **partner content only performs at Harper-typical levels when it keeps
Harper's own structural playbook intact.**

#### Sources
- https://www.instagram.com/reel/DX9nDB_pdBF/ (metadata, caption, comments — yt-dlp, 2026-07-25)

---

### SIDEBAR: the @oreillymedia collab, and why guest/collab-hosted posts underperform here

**One collab analyzed briefly, per the task brief**, plus a scope correction: this session found
**4 O'Reilly collab posts in the 48-tile grid, not the 2 the original harvest flagged** — `DZ-xwWgAqox`
(17.9K views, analyzed below), `DaBLNlJCiVE` (19.6K), and two more this session identified via direct
`uploader_id` verification, `DZ-XqZoiF4N` (22.5K) and `DaDaYSBEoZy` (23.7K) — all four posted by
`@oreillymedia` (`uploader_id 224832541`), not `@harpercarrollai` (`5787807072`) `[OBSERVED, yt-dlp,
this session, HIGH confidence]`.

**DZ-xwWgAqox** ("How do AI models actually learn?"), posted 2026-06-24: 17.9K views, 203 likes
(1.13% — a perfectly healthy engagement *rate*), 7 comments `[OBSERVED, yt-dlp]`. Caption is written
in **third-person** ("Harper Carroll breaks down the math behind the process...") rather than her own
first-person voice — direct evidence this is O'Reilly-produced editorial content featuring her as a
guest expert, not her own optimized format. `@oreillymedia` itself has only **4,805 Instagram
followers** `[REPORTED, WebSearch, 2026-07-25, MED]` — two orders of magnitude smaller than Harper's
605K.

**Why these underperform, mechanistically:** this is a **different failure mode than the
ad-boosted-sponsored-post pattern documented elsewhere in this corpus** (tiffintech, networkchuck,
where inflated view counts pair with near-zero engagement rates). Here, engagement *rate* is fine
(1.13% likes is comparable to several of Harper's own top-5) — the ceiling is purely **reach**,
because the post lives on a different, much smaller account. Per rubric §1.1.1, Instagram's ranking
weighs "your history with the poster" and the poster's own follower/engagement level — none of
Harper's 605K-follower relationship equity transfers to a post that never touches her own feed or
follower graph. Combined with the loss of her own first-person hook/CTA structure (no credential
signature, no comment-keyword funnel, third-party editorial voice), a collab-guest appearance forfeits
essentially every mechanism identified in Sections B1–B5 above as load-bearing for her own top
performers. **Lesson for Tangent:** a guest feature on a small partner's own channel can be worth
doing for relationship/credibility reasons, but should not be budgeted for reach — reach requires the
content to live on the creator's own, larger, warmed-up audience graph.

---

## C. THE COLD-START PLAYBOOK RECONSTRUCTION (centerpiece)

### C1. The growth timeline, triangulated across sources
- **Pre-launch state:** ~2,000 Instagram followers `[REPORTED, The Ankler, theankler.com/
  creator-spotlight-harper-carroll-instagram-ai-expert-teaching/, accessed 2026-07-25, MED-HIGH — a
  named trade-press profile, the strongest single source in this dossier]`.
- **The sprint:** the "10 Days of AI Basics" series took the account from ~2,000 to **200,000+
  followers in roughly three weeks** `[REPORTED, The Ankler, same source]`.
- **Day 1, directly verified:** the actual originating post, `instagram.com/reel/C4eNPF3PdpG/`, is
  dated **2024-03-13** and currently shows **111,083 likes and 863 comments** (as of this session,
  ~2.4 years post-publication) `[OBSERVED, yt-dlp direct fetch, 2026-07-25, HIGH]` — direct,
  independent confirmation that this specific post was a genuine outlier hit, not merely a press
  characterization.
- **Self-reported scale claim (found via multiple independent WebSearch summaries of her own site's
  marketing copy, primary text not independently re-verifiable this session — academy.harpercarroll.ai
  is JS-rendered and returned no body text to WebFetch):** the Day-1 reel specifically is credited with
  **5 million views and 250,000 "learners" recruited** `[REPORTED, self-source via WebSearch summary,
  LOW-MED confidence — this is her own marketing claim, convergent across two independent search
  results but neither traceable to a directly-fetched primary page this session]`. Taken together with
  the directly-verified 111K-like figure, a 5M-view / ~2.2% like-rate is internally plausible, not
  contradicted by the [OBSERVED] data — but it remains unverified beyond her own claim.
- **13-month milestone:** a podcast episode title states she won **"400K Instagram followers in 13
  months"** `[REPORTED, podcast title, Unicorn Bakery, accessed 2026-07-25, MED — a title is weaker
  evidence than in-episode text, but consistent with the trajectory]`.
- **Current state:** 605K followers as of this session `[OBSERVED, ig_harvest, 2026-07-25]`, roughly
  28 months after the March 2024 launch.
- **The shape of the curve, reconstructed:** 2K (pre) → 200K (+3 weeks) → 400K (+13 months) → 605K
  (+28 months). This is a **front-loaded sprint followed by steady deceleration** — the growth *rate*
  in the first three weeks (~6,600%+ in 21 days) dwarfs the growth rate in every subsequent period
  (roughly 2x over the next ~12 months, then ~1.5x over the ~15 months after that). **The cold-start
  mechanics that matter most are concentrated almost entirely in the first three weeks.**

### C2. The credential-forward hook, verbatim and cross-platform-identical
The exact opening script was independently recovered from **three separate platforms** — an Instagram
caption `[OBSERVED, yt-dlp on C4eNPF3PdpG]`, a TikTok caption `[OBSERVED, WebSearch-indexed TikTok
post text, video ID 7345991798050786603]`, and a YouTube spoken transcript posted nearly a year later
`[OBSERVED, yt-dlp auto-subs on VJoVEMYOW-o]` — and the wording is copy-identical or near-identical
across all three:

> "If you don't know me, I'm Harper, and I received my Bachelor's and Master's degrees from Stanford
> University in computer science in artificial intelligence. I have always loved to teach, and at
> Stanford I TA'd multiple computer science courses, including a PhD-level core AI course, Decision
> Making Under Uncertainty. I was also at Facebook/Meta for 4 years doing AI/ML engineering..."

This is not a one-off flourish — it is a **standing, reusable script block**, reused verbatim across
platforms and, in abbreviated form, across nearly every subsequent post in this account's history (see
Section B's recurring "If we haven't met yet, I'm Harper — a computer scientist for AI who's been
building AI models for over a decade" signature, present in Videos 1, 2, 3, 5, and the original Day-1
post, and its *conspicuous absence* being the single most notable structural feature of the account's
single worst-performing post, Video 7). **The credential is not stated once and assumed to stick — it
is re-stated as a standing module on nearly every piece of content, because Reels/Shorts distribution
is feed-driven and cold (rubric §1.2.3), meaning a meaningful fraction of any given post's audience has
never seen her before and needs the trust-anchor restated from zero.**

### C3. Series architecture as the structural container
The Day-1 post itself explicitly frames the format choice: **"I'm going to come out with 10 videos
going over the 10 basic categories that you should know as fundamentals for AI... The videos here on
Instagram will be short and bite-sized, but I will be coming out with a YouTube series to go more
in-depth."** `[OBSERVED, yt-dlp transcript, VJoVEMYOW-o]` This does three things simultaneously:
1. **Lowers perceived commitment** — "only 10, and they're short" is an explicit scope promise, a
   different psychological ask than an open-ended "follow me for AI content."
2. **Manufactures a "Day 2" reason to follow** — an implicit appointment-viewing mechanic (rubric
   §3.4.2), converting Day-1's one-time viral spike into a standing reason to hit "follow" rather than
   just liking and moving on.
3. **Splits platform roles from day one** — short-form (IG/TikTok) as the discovery/breadth layer,
   long-form (YouTube) as the depth layer for the subset of viewers who want more — a two-tier content
   architecture designed in from the start, not bolted on later.

**This format was not a one-off — it became a reusable owned template.** The full 266-video YouTube
Shorts catalog `[OBSERVED, yt-dlp `--flat-playlist`, full population, 2026-07-25]` shows the numbered
"Day N of X" structure reused at least twice more: a second, **sponsored** 10-part series, "AI x
Nuclear Electricity, Day N/10" with partner `@isodope`, and recurring shorter numbered mini-arcs (e.g.,
a 3-part "NVIDIA's value explained, Part I/II/III," a "ChatGPT Series #1"). The numbered-series
structure functions as a **standing, repeatable production template** she returns to, not a single
lightning-in-a-bottle event.

### C4. Does the numbered series show compounding/retention effects in the view data? (central question 3)
**Directly observable answer, with an important caveat.** On YouTube — the only platform where
per-episode view data for the original "10 Days of AI Basics" series is available to this
session — the pattern is **front-loaded and declining, not compounding**:

| Episode | YouTube views `[OBSERVED, yt-dlp]` |
|---|---|
| Day 1 (original) | 34,541 |
| Day 1 (later repost) | 1,337 |
| Day 2 | 3,700 |
| Day 3 | 3,100 |
| Day 4 | 2,600 |
| Day 5 | 1,700 |
| Day 6 | 5,500 |
| Day 7 | 1,400 |
| Day 8 | 944 |
| Day 9 | 1,700 |
| Day 10 | 1,600 |

Views drop sharply after Day 1 and never recover to Day-1 levels (a small Day-6 bump aside). The
sponsored "AI x Nuclear Electricity" 10-part series shows the same shape (Day 1: 247 views, peaking
mid-series around 1,000, no late-series climb). **This directly falsifies a naive "each episode
compounds on the last" reading of the series-retention theory (rubric §3.4.2) — at least on YouTube.**

**DATA GAP, explicitly logged:** the actual growth explosion (2K→200K) happened on Instagram/TikTok,
not YouTube — the original Days 2–10 Instagram posts predate this session's 48-tile harvest window by
roughly two years and were not independently recoverable. It is **not established** whether the
Instagram version showed the same declining shape or something different (e.g., a platform actively
pushing a recognized, in-progress series to an expanding cohort, consistent with the "audition"/
explore-exploit mechanism in rubric §1.1.3 and §1.2.2).

**Best-supported synthesis, given both the observed YouTube shape and the Ankler's three-week
timeline:** the series' function was very likely **not** "each episode goes more viral than the last."
It was closer to: (1) Day 1 achieves an outlier breakout (via the credential-forward hook + a
genuinely under-served topic + favorable timing), (2) the explicit "10 videos, short, here's the plan"
framing converts a meaningful share of that one-time audience into **followers** rather than one-time
viewers, and (3) the *existence* of a recognizable, numbered, in-progress series — visible as a
pattern to both the algorithm and returning viewers — sustains elevated distribution for the
follow-up episodes even if no single subsequent episode independently re-achieves Day 1's peak. This
is consistent with, but not fully provable from, the mere-exposure mechanism (rubric §2.4.2,
RESEARCH-BACKED) and the platform's stated preference for content with "history with the poster"
signal (§1.1.1) — a recognized returning creator/series should out-distribute an equivalent one-off
from a stranger, even without literal view-count compounding.

### C5. Topic selection during the sprint vs. now
The Day-1 caption states the topic was **audience-demand-driven**: "This is, by far, the most
requested series" `[OBSERVED]`. The 2024 sprint content was a **structured, definitional curriculum**
(What is AI vs. ML → Data → Model Architecture → Training → Training Processes → Evaluation Metrics →
Error Analysis → Ethics & Fairness → Deployment → Open vs. Closed Source) — foundational literacy, not
news reactions. This is a **materially different topic strategy from her current (2026) top-performing
content**, which (per Section B) is dominated by same-day product-launch reactions (Videos 3, 4) and
branded partner series. **The reconstructed arc: foundational-curriculum creator at cold-start →
news-reactive/tools-authority + brand-partner creator at steady-state.** This progression itself is a
transferable lesson: a structured, promise-bounded curriculum is a plausible cold-start format
precisely because it gives a stranger a reason to follow (see C3), whereas news-reactive content
(which requires an existing, warmed-up audience checking in regularly) is a better steady-state format
once a following exists to receive it quickly.

### C6. Cadence during the sprint
**DATA GAP, honestly logged:** only Day 1's exact date (2024-03-13) is independently confirmed; exact
posting dates for Days 2–10 were not recoverable this session (YouTube versions of Days 2–10 are dated
nearly a year later, in 2025, and cannot be used as a dating proxy for the original 2024 Instagram
posts). **What can be said with confidence:** the format's own name ("10 Days of AI Basics") states an
intended daily cadence, and this is directionally consistent with the Ankler's "three weeks" framing
for the whole growth event (10 daily posts plus roughly another 1–2 weeks of algorithmic
follow-through/cascade after the last episode is a plausible reading, though not confirmed by exact
dates).

### C7. Credential-authority dynamics — how much of this is credibility-badging, and what a non-credentialed creator can substitute (central question 2)
- **The credential is doing real, measurable work, not just decoration.** It appears as a standing
  signature block on nearly every video in this sample (Videos 1, 2, 3, 5, plus the Day-1 original),
  and its **absence is the single most notable feature of the account's worst-performing post** (Video
  7, Section B) — a naturally-occurring, within-account A/B signal, not a controlled experiment, but
  suggestive. Her own site tagline states this positioning directly: **"Learn AI from a practitioner,
  not a pundit"** `[REPORTED, WebSearch summary of harpercarroll.ai marketing copy, MED]` — an
  explicit differentiation move against the broader "AI influencer" category, implying she frames many
  competitors as pundits and herself as the credentialed exception.
- **The credential has fully saturated audience perception, including in pushback.** The mocking
  comment on Video 5 — "who is using wired headphones now a days? Specially with two AI degrees from
  Stanford 😂😂😂😂" `[OBSERVED, yt-dlp]` — routes its joke through her Stanford identity even when the
  actual point has nothing to do with AI credentials. This is strong evidence the credential-branding
  has become inseparable from her audience's mental model of the account, for better (default trust)
  and worse (any critique gets filtered through "but she went to Stanford," which can read as either
  reinforcing or slightly mocking depending on the commenter).
- **Mechanism, per the rubric:** the credential functions as an instant trust-transfer for a
  structurally cold audience (rubric §1.2.3 — Shorts/Reels selection burden falls entirely on the first
  few seconds, with no click-through moment to build context first) — it substitutes for the
  slow-built trust a subscribed newsletter or established personal blog would otherwise require,
  compressing "why should I believe this stranger" into one sentence.
- **Substitution advice for a non-credentialed creator** `[INFERRED, this analyst's synthesis, labeled
  as inference per QC_PROTOCOL]`: the credential's functional job is not "prove you went to a
  prestigious school" — it is "give a cold viewer, in the first few seconds, a falsifiable reason to
  trust what follows." A non-credentialed creator's substitute needs to do the same job through a
  different, still-falsifiable channel:
  - **Show a verifiable, working artifact in the first seconds** (a finished piece, a before/after, a
    shipped result) rather than describing credentials — "here's what I made" is the demo-in-motion
    hook taxonomy (rubric §3.1) functioning as proof-of-work.
  - **State a specific, checkable track record** ("I've done this 200 times," "I've sold N pieces," "I
    apprenticed under X for N years") — quantified, falsifiable claims carry some of the same
    trust-transfer weight as an institutional name, per the same underlying psychological mechanism
    (both are shortcuts that let a cold viewer skip re-deriving trust from scratch).
  - **Repeat it as a standing signature, not a one-time bio line** — the load-bearing finding from this
    account is repetition and consistency (present on nearly every video) rather than a single
    "about me" post; a non-credentialed creator's proof-of-work statement needs the same "restated on
    every cold-audience touchpoint" treatment, not a one-time pinned post.
  - This substitution is consistent with the rubric's parasocial-bonding mechanism (§2.4.1, which
    identifies self-disclosure — not institutional pedigree specifically — as the trust-building
    lever) and Social Currency (§2.2 — a specific, checkable claim of unusual competence works the same
    "in the know" mechanism as a name-brand credential).

---

## D. Content architecture: key vs. filler, cadence, sustainability

- **Key content (drives reach + funnel):** (1) **same-day/near-same-day AI product-launch
  explainers** (Video 4, and per the wider YouTube catalog sweep, a recurring "[Product] is here /
  just launched" title pattern — "LLAMA 3.1 IS LAUNCHED," "NEW, FREE LLM OUT NOW," "Meta's release of
  Llama 3.3") — externally-paced, sustainable precisely because the AI industry supplies a constant
  news stream `[OBSERVED, title sweep of the 266-video YouTube catalog, 2026-07-25]`; (2) **branded
  "explAIner" partner mini-series** (Videos 2, 3) that retain her full structural playbook
  (credential + declarative hook + CTA) and land in the top-5 despite being sponsored; (3) **specific,
  demoable tool/workflow giveaways gated behind a comment-keyword CTA** (Video 1, and the "POV: You
  taught an AI to tweet exactly like you" pattern recurring elsewhere in the catalog) — this is the
  account's most direct funnel-feeding format.
- **Filler/lower-priority content:** (1) **personal-narrative/brand-obligation posts that drop the
  standing structural playbook** (Video 7 — the account's floor); (2) **pure technical-explainer
  content on lower-trigger-surface, higher-audience-friction topics** (Video 6 — Meta-related content
  drew unusually skeptical/critical comments relative to the rest of the sample); (3) occasional
  **emotional/parasocial-only posts** (Video 5) that, notably, are NOT filler by performance — they are
  a deliberately-used, high-performing register, just a structurally different one from her
  educational core.
- **Numbered-series format as a recurring production template, not a single event** — reused at
  least three times across the account's history (10 Days of AI Basics; AI x Nuclear Electricity x
  10; smaller Part I/II/III and #1-style micro-series) `[OBSERVED, 266-video catalog sweep]` —
  functioning as a repeatable "own IP" content structure the account returns to whenever it wants an
  appointment-viewing/follow-conversion push, distinct from the news-reactive one-offs that make up
  the bulk of current-era key content.
- **Cadence:** exact native Instagram posting cadence could not be established with confidence from
  the available dated sample (7 detail-pulled reels spanning 2026-03-03 to 2026-07-21, too sparse and
  selection-biased — chosen for top/flop relevance, not cadence sampling — to compute a reliable rate).
  **DATA GAP.** A rough lifetime-average proxy: 232 total posts over ~28 months since the March 2024
  launch ≈ **8.3 posts/month, roughly 1.9/week** `[INFERRED, simple division, MED-LOW confidence — a
  lifetime average smooths over the sprint-vs-steady-state distinction established in Section C1, and
  should not be read as her current weekly rate]`. Her bio's own claim of "Weekly explAIned episodes"
  `[OBSERVED, bio text]` suggests a current cadence target of roughly once/week for the flagship
  explainer format specifically, on top of other content types.
- **Sustainability read:** this account's durable growth engine, post-sprint, is a **three-legged
  structure** — (a) a fast-turnaround news-reactive lane (externally paced, low manufacturing cost per
  video since the news supplies the hook), (b) a standing brand-partnership pipeline (Anthropic,
  OpenAI, ServiceNow, and others per the site's logo wall) that keeps sponsored content inside her own
  proven structural playbook rather than as detached ad-reads, and (c) an occasional, deliberately-used
  emotional/parasocial register that appears to outperform the educational median when deployed. The
  one-time cold-start mechanism (a bounded, numbered curriculum series from a near-zero base) does not
  appear to be a format she still relies on for growth at 605K followers — it was a launch-phase
  tool, since substituted by news-cycle velocity and partnership credibility at scale.

---

## E. Method log

**Environment:** `yt-dlp 2026.07.04`, direct fetch against `instagram.com/reel/<code>/` and
`youtube.com/shorts/<id>` URLs, no third-party aggregator, no browser automation (claude-in-chrome
reserved this session). All work in
`/private/tmp/.../scratchpad/harpercarrollai/`. `--socket-timeout 20` throughout; `--skip-download`
used for every Instagram call (metadata/captions/comments only — no video/audio files were downloaded
at any point in this session).

**What was fetched successfully:**
1. Primary data source: `ig_harvest/harpercarrollai.md` (already-harvested grid of 48 tiles + 7
   detail pulls + `00_INDEX.md` cross-account context) — read in full before any new fetching began.
2. Direct `yt-dlp` metadata pulls (uploader_id, channel, upload_date, like_count, comment_count,
   description, up to 15 top comments) against **19 distinct Instagram reel URLs**: the 7 originally
   flagged in the harvest, plus 6 additional low-view candidates fetched specifically to verify
   genuine-vs-collab attribution before finalizing the flop selection (`DZ-XqZoiF4N`, `DaDaYSBEoZy`,
   `DX9nDB_pdBF`, `DW9gguSDgRM`, `DZscGjFuBhd`, `DaWMgm_Ssq-`), plus a targeted verification fetch on
   `DXbNw7JDRSW` (revealed the previously-unflagged `@harpercarroll_clips` repost) and the actual Day-1
   growth-catalyst post `C4eNPF3PdpG` (succeeded) and its apparent duplicate `DD68xjHO_RT` (failed,
   Instagram API returned an empty response — logged, not retried with cookies/login per the
   read-only, no-authentication constraint implied by the task's data-access rules).
3. Full YouTube Shorts population for `@harpercarrollai`: `yt-dlp --flat-playlist` on
   `youtube.com/@harpercarrollai/shorts` returned **266 rows** (title + view count for each),
   confirmed as the full catalog by the flat-playlist call completing without pagination errors —
   used for series/cadence/topic-evolution analysis in Sections C and D.
4. Six YouTube cross-post matches identified by exact same-calendar-day `upload_date` agreement with
   Instagram posts (`w3SLz6carLw`, `UzIzRyvkAdc`, `A0C8qs4Qmi4`, `VIWI4nilOcw`, `nALGUsjwqNk`, plus the
   Day-4 short `R17q8H1ZSTI` and Day-1 long-form original `VJoVEMYOW-o`), each fetched for full
   metadata and auto-generated English subtitles (`--write-auto-subs --sub-langs "en.*" --sub-format
   vtt`), then de-duplicated/cleaned via a Python script stripping VTT timing tags and consecutive
   duplicate caption lines to produce readable, timestamped transcripts.
5. One additional YouTube match (`QJ6dyST-WuE` for `DYPXSQ4hPdF`) was identified by title/theme but
   its `upload_date` (2026-05-19) did **not** exactly match the Instagram post's date (2026-05-12) —
   used cautiously, flagged as MED not HIGH confidence, in Video 5's post-mortem.
6. `yt-dlp --flat-playlist -J` on the "10 Days of AI Basics" YouTube playlist (long-form companion
   series) for episode-level view counts, used in Section C4's compounding analysis.
7. `WebSearch` (10 queries) covering: the Ankler growth-story feature, her Stanford/Meta bio, podcast/
   interview appearances, course/consulting/speaking details, the "5M views/250K learners" claim, the
   Academy/learner-count claims, and credential-authority framing/quotes.
8. `WebFetch` on: the Ankler article (full extraction), her Substack `/about` page, a German-language
   podcast site (Unicorn Bakery, English-summarized), `harpercarroll.ai/course`, `harpercarroll.ai/`
   (homepage), `rewritingthecode.org` (an interview page, limited direct relevance to the credential-
   authority question specifically).

**What failed / data gaps (logged per QC_PROTOCOL rule 3, not papered over):**
1. **`academy.harpercarroll.ai`** returned only header/navigation text to WebFetch (JS-rendered SPA,
   no server-side content) — the "162 lessons"/"250K learners"/"700K learners" figures could not be
   independently re-verified against this primary page; they are carried forward as [REPORTED] from
   WebSearch-summarized secondary text only.
2. **`harpercarroll.ai/enroll`** returned HTTP 404 — this URL, referenced in one search result, no
   longer resolves; not used as a source.
3. **No verbatim spoken transcript** for 3 of the 7 primary post-mortem videos (`DZfgPtFObU1`,
   `DVbM3sBjl26`, `DX9nDB_pdBF`) — no matching YouTube cross-post was found by title/theme search
   against the full 266-video catalog, and Instagram itself exposes no subtitle track for these posts
   (`yt-dlp --list-subs` confirmed "has no subtitles" on a test call). Caption text and top comments
   were used as the evidence base for these three instead, explicitly flagged wherever a claim would
   otherwise imply a watched transcript.
4. **Like-count anomaly, unresolved:** `like_count` returned as a clearly-wrong placeholder value (`3`)
   for 4 of the ~19 posts fetched this session (`DbD8-40Owbv`, `Dan0IIuJP7K`, `DZscGjFuBhd`,
   `DaWMgm_Ssq-`), while `comment_count` remained plausible on all of them. The leading hypothesis
   (Instagram's per-post "hide like count" creator setting) is stated as [INFERRED, MED confidence] in
   the relevant post-mortems, not asserted as fact — true like counts for these 4 posts are a logged
   DATA GAP.
5. **Like-count discrepancy between this session's yt-dlp pulls and the original harvest's browser-
   scraped figures** on 2 posts (`DZfgPtFObU1`: 33,065 vs. 904; `DVbM3sBjl26`: 7,171 vs. 5,358), while
   comment counts matched exactly on both — flagged and resolved in favor of the yt-dlp figures (with
   reasoning given) in each affected post-mortem, not silently overwritten.
6. **No exact IG posting dates for "10 Days of AI Basics" Days 2–10** (the original 2024 Instagram
   posts) — these predate the 48-tile harvest window by roughly two years and were not independently
   locatable via WebSearch. Section C6's cadence claim is explicitly qualified as inferred from the
   series' own naming convention plus the Ankler's three-week framing, not confirmed dates.
7. **No exact duration** for `DZfgPtFObU1`, `DVbM3sBjl26`, and `DX9nDB_pdBF` (no YouTube proxy found,
   and Instagram's metadata API does not expose a duration field to `yt-dlp` without downloading the
   underlying video file, which this session did not do).
8. **TikTok follower count** for `@harpercarrollai` was not independently obtained this session
   (content-match to the Day-1 script was confirmed via a WebSearch-indexed post, but the account's
   own follower count was not fetched) — logged as a DATA GAP rather than estimated.
9. **Course pricing** shows a live-page-vs-cached-summary discrepancy (waitlist/undisclosed on the
   directly-fetched live page vs. a "$129/$399" figure from an unsourced WebSearch summary) — resolved
   in Section A by treating the directly-fetched live page as authoritative and flagging the other
   figure as unconfirmed, not deleting it outright since QC_PROTOCOL rule 1 only requires deletion of
   *unsourced* stats, and this one does carry a (weak, LOW-confidence) source.
10. **`DD68xjHO_RT`** (an apparent duplicate/alternate reference to the Day-1 post found via
    WebSearch) failed to fetch — Instagram's API returned an empty media response for this specific
    shortcode. Not retried with authentication per the read-only constraint; `C4eNPF3PdpG` (which did
    fetch successfully and carries a matching caption and a plausible 2024-03-13 date) was used as the
    verified Day-1 post instead.
