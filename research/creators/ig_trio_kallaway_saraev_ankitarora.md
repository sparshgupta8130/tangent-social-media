# IG Trio Dossier: Kallaway, Nick Saraev, Ankit Arora

**SCOPE NOTE (read first):** This is a deliberately-scoped **secondary-tier** dossier: **top-3 depth per
account, not top-5**. It combines three accounts that did not individually warrant full primary-tier
treatment but are analytically valuable as a set (an extreme-variance serial-spike account, a
tool-arbitrage automation educator, and a spike-and-decay case). Each account gets **3 top post-mortems +
1 flop post-mortem = 4 per account, 12 total**, each following the mandatory nine-section template at
40+ substantive lines. Do not read this as a full parity dossier with the primary-tier accounts
(thevarunmayya, handlytech, sabrina_ramonov, 100xengineers, tiffintech, networkchuck, harpercarrollai) —
those got 8-11 videos each; this got 4 each by design.

**Evidence-tier legend:** `[OBSERVED]` = analyst directly fetched it (yt-dlp against the live Instagram
page, or the harvest file's own live pull). `[REPORTED]` = secondary source, URL required. `[INFERRED]` =
analyst reasoning, labeled and justified. Per QC_PROTOCOL.md, every number carries source + as-of date +
confidence.

**Primary tooling for this dossier:** `yt-dlp 2026.07.04` run directly against `instagram.com/reel/<code>`
URLs for each of the 12 target reels — this returns caption/description text, like_count, comment_count,
and upload timestamp without a logged-in session (Instagram does not gate this metadata the way it gates
the full page), plus a cover-thumbnail image (used as a frame-1 proxy — see caveat in Method log). View
counts are NOT exposed by yt-dlp for Instagram (`view_count` returns `NA`) — all view-count figures in
this dossier are carried forward from the `ig_harvest/*.md` grid-scrape files, which pulled them from
Instagram's `og:description` / rendered grid, `[OBSERVED]` 2026-07-25 by the harvest pass. All work done
in `/private/tmp/.../scratchpad/ig_trio/`. No claude-in-chrome browser tools used, per assignment
constraint.

---

# ACCOUNT 1: Kallaway (@kallaway)

## Account header
- 442K followers, 439 following, 530 posts `[OBSERVED, ig_harvest/kallaway.md, 2026-07-25]`. Bio:
  "Entrepreneur / Breaking down new tech & AI / Helping business owners stay ahead in the AI era /
  sandcastles.ai."
- Real name **Kane Kallaway** `[REPORTED, linkedin.com/in/kanekallaway/, MED]` — LinkedIn describes him as
  cofounder of sandcastles.ai with "1M+ followers, 1B+ views" cross-platform, i.e. this IG account is one
  slice of a larger cross-platform footprint. Sandcastles.ai is described in web results as an AI
  "content storytelling agent" that compresses script-writing time "from 60 minutes to 60 seconds," with
  100K+ signups `[REPORTED, sandcastles.ai + search aggregation, MED — could not verify the 100K signup
  figure against a primary dated source]`. This is directly relevant to the central question: Kallaway is
  literally productizing his own packaging/scriptwriting process as a SaaS.
- **Cross-platform check** `[OBSERVED via yt-dlp, 2026-07-25]`: a YouTube channel `@kallaway` exists and
  is active (long-form interviews — Mark Zuckerberg, Daniel Ek — and product-review videos), but its view
  counts (3.3K–130K per video sampled) are an order of magnitude below the IG mid-grid spikes and even
  below the IG account's own 177K median. **IG Reels, not YouTube, is this creator's primary distribution
  engine** — the YT channel functions as a long-form/interview archive, not a Shorts-repurposing pipeline.
- Median reel views 177K, top raw reel 74.2M, median/follower ratio ~40% (3rd-highest of 22 accounts in
  the wider study) `[OBSERVED, ig_harvest/kallaway.md]`. This is the **most extreme-variance account in
  the entire 22-account study**.

## CRITICAL CONTEXT — pin/boost re-verification landed mid-task

The harvest file `ig_harvest/kallaway.md` was originally roster-tier only (grid + computed stats, no
detail pulls, pin status "uncertain"). Per this task's brief, a second agent was independently
date-checking the three mid-grid mega-spikes; that agent's results (`## Pin/date confirmation` section)
landed in the harvest file **before this dossier was finalized** and materially change the account's
story. This dossier incorporates that re-verification. Summary of what changed:

1. **Grid positions 1-2 (4.3M, 14.5M views) ARE genuinely pinned legacy content** — dated **Jun 27, 2024**
   and **Sep 5, 2024** respectively `[OBSERVED, re-verification pull, ig_harvest/kallaway.md]`, both with
   normal-to-strong organic like-rates (1.3% and 4.4%). These are the account's actual highest-engagement
   content, just old and manually kept pinned — same pattern already confirmed on nateherkai/thevarunmayya/
   handlytech elsewhere in the study.
2. **The three mid-grid mega-spikes this dossier's central question is about (74.2M / 39.5M / 35.8M) are
   NOT pinned** (genuinely recent 2026 dates, buried at grid positions 35/27/18) **but show like-rates
   100-1000x below this account's own organic norm**, landing in the same order of magnitude as the
   *confirmed* ad-boosted posts on tiffintech (Lenovo) and networkchuck (Vanta) elsewhere in this study.
   No official "Paid Partnership" label was detected on any of the three, so the leading explanation
   `[INFERRED]` is **self-funded IG ad spend boosting the creator's own organic posts** (inflates
   impressions/views without a proportional lift in likes/comments from cold, ad-served viewers), not a
   disclosed brand deal, and not organic virality.
3. **A numeric discrepancy exists between this dossier's own yt-dlp pull and the harvest file's
   re-verification pull for like counts on all three spikes** (comment counts match exactly across both
   pulls; likes do not — see the table in each post-mortem's §0 and the Method log). Both pulls agree on
   the *qualitative* conclusion (like-rate is anomalously, dramatically low relative to views on all
   three), so the finding is treated as robust even though the exact like-count is unresolved.

**This reframes the central question directly: the spikes do NOT look organic.** The account is a mixed
pattern — genuine pinned-legacy virality (2024) layered with probable paid view-inflation on select 2026
posts — not "a serial organic mega-viral outlier producer" as the pre-verification heuristic read.

---

### VIDEO 1 (TOP #1 by raw views, mid-grid position 35): "Luma Creative Agents — polar bear video"

#### 0. Identity & stats
- URL: instagram.com/reel/DVhB8rMjp1m. Platform: Instagram Reels. Posted **Mar 5, 2026**
  `[OBSERVED via yt-dlp upload_date, 2026-07-25, HIGH]`. Duration: not exposed by yt-dlp for Instagram
  metadata-only extraction — DATA GAP, structural (would require full video download, out of scope).
  Format: 1080×1920 (9:16 vertical) `[OBSERVED via yt-dlp JSON dump]`.
- Views: **74.2M** `[OBSERVED, ig_harvest/kallaway.md grid scrape, 2026-07-25, HIGH]`. Comments: **972**
  `[OBSERVED via yt-dlp, HIGH — matches exactly across both this dossier's pull and the harvest file's
  independent re-verification pull]`. Likes: **DISCREPANT — this dossier's yt-dlp pull returned 64,910;
  the harvest file's independent re-verification pull returned 678** `[OBSERVED, both pulls dated
  2026-07-25, MED confidence on the exact figure, HIGH confidence on the qualitative conclusion — see
  below]`. Like-rate is either ~0.088% (this dossier's number) or ~0.0009% (re-verification's number) —
  **both are far below this account's genuine organic norm** (the confirmed-pinned tiles run 1.3%-4.4%),
  so the anomalous-engagement conclusion holds regardless of which count is correct.
- Rank: **#1 raw-views reel in the account's 48-tile sample**, grid position 35 (mid-grid, unpinned).
  74.2M / 177K median ≈ 419x — the single most extreme outlier multiple in the entire 22-account study.

#### 1. Packaging
- Caption opens: "This is the most insane creative platform I've ever used." `[OBSERVED via yt-dlp
  description]` — bold-claim superlative, names no product yet.
- Cover-thumbnail `[OBSERVED, downloaded via yt-dlp --write-thumbnail]`: a **structured split-frame
  composite**, not a single candid frame — top half is a labeled "Final Output" box showing an AI-generated
  cinematic shot (a man with a bloodied face beside a polar bear on ice, captioned "Final Output"), below
  it a smaller "Input Images" row showing "First Frame" / "Last Frame" reference stills, and at the bottom
  Kallaway himself mid-gesture (open palm to camera) over a bold white "LUMA / CREATIVE AGENTS" wordmark.
  This is a **branded-package template**, not a raw talking-head clip — closer to a mini cable-news
  graphics package than an organic selfie video.
- Curiosity gap: viewer sees a striking, high-production sci-fi/thriller-style image before knowing how it
  was made — classic result-first packaging (§2.1.1: partial information, gap not yet closed).
- Hashtag `#lumapartner` present in the caption `[OBSERVED]` — not Instagram's official "Paid Partnership"
  label (per Instagram's own help-center documentation, that is a distinct on-platform tag, not a
  hashtag), but a self-declared brand-tie-in hashtag `[INFERRED: functionally signals a
  commercial/promotional relationship with Luma AI even though it isn't the formal disclosure mechanism]`.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption, likely mirrors on-screen narration given the
  conversational-script phrasing throughout — not independently confirmed as the literal spoken audio,
  since no transcript/subtitle track was extractable for Instagram via yt-dlp]`: **"This is the most
  insane creative platform I've ever used."**
- Hook taxonomy: **bold claim** ("most insane... I've ever used" — an unqualified superlative) fused with
  **result-first/demo-in-motion** (the thumbnail shows the finished cinematic output before any process
  explanation).
- What the viewer sees first: the finished AI-generated "final output" image (polar bear/bloodied man
  scene) — not Kallaway's face, not a slow build. The payoff is shown before the mechanism, per §2.1.1's
  "partial info, gap not yet closed" curiosity structure.

#### 3. Structure & retention engineering
- Beat map (reconstructed from the full caption, which reads as a tight explainer script) `[OBSERVED via
  caption; timestamps not obtainable without the video itself — DATA GAP, noted not invented]`:
  bold-claim hook → "what you're looking at" context (Luma workspace) → process reveal (drop in one photo,
  describe scenes) → proof-of-craft beat ("these aren't just random sketches... these are super high
  quality reference photos") → mechanism explainer (chat in plain English, no manual prompting) → stakes
  ("this changes everything about the AI creative process") → CTA (comment "LUMA" for the PDF).
- One-idea-per-video: yes — "this AI creative platform turns one photo + a few described scenes into a
  full storyboarded video, with no manual prompting." Payoff is drip-loaded: the "wow" image is shown
  immediately (hook), but the *how* (agentic chat interface, no-prompt-writing) is revealed progressively.
- Open loop: "how did one photo become this entire cinematic sequence?" opened at the hook, resolved
  across the middle beats — classic §2.6.1 loop structure.
- Pacing: caption text implies a demo-heavy screen-capture structure (storyboard grid, scene selection,
  video-clip stitching) — DATA GAP on actual cut frequency without the video file.
- Loop/rewatch bait: not evident from caption; this reads as a single linear explainer, not built for
  rewatching.

#### 4. Value proposition
- Walk-away value: tool discovery (Luma's agentic creative workspace) + an implied identity/aspiration
  boost ("I could make cinematic content like this too") + a documented process via the promised PDF.
- Practical value class: primarily **tool discovery + aspiration**, secondarily **copyable workflow** (the
  PDF, gated behind a comment).
- Specificity: MED — names the platform (Luma), describes the mechanism (chat-based, agentic, no manual
  prompt-writing) at a conceptual level, but the actual prompts/settings are gated behind the "comment
  LUMA" funnel rather than shown in-video — a deliberate value-gating device, not full in-video disclosure.

#### 5. Psychology scoring
- STEPPS: **Social Currency** is strong — sharing "the most insane creative platform" signals the sharer
  is at the frontier of AI creative tools (§2.2, §2.5). **Emotion**: awe at the visual quality of the
  AI-generated cinematic image — high-arousal positive per Berger & Milkman (§2.3). **Practical Value**:
  present via the gated PDF but secondary to the spectacle. **Triggers/Public/Story**: weak — no everyday
  cue, no visible trend-chain, only a mild narrative arc (photo → storyboard → finished film).
- Primary emotion + arousal: **awe**, high arousal.
- Identity-signaling share motive: "I found the AI tool that makes real filmmaking possible for one
  person" — self-presentation as ahead-of-curve (§2.5).
- Save/send trigger: MED — a specific "send to a friend who makes video content" moment exists, but the
  content is more spectacle-driven than reference-utility-driven, so the save motive is weaker than a
  pure how-to.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'LUMA' and I'll send it through" (PDF lead magnet) — a comment-to-DM funnel
  mechanic (§3.4.3), content-backed (the video itself has standalone value), so it is compliant, not bare
  engagement bait per §1.3.2's test.
- Funnel position: top-of-funnel discovery/spectacle content that converts into a DM'd PDF — likely
  feeding an email/DM list that eventually points at sandcastles.ai, though that connection is
  `[INFERRED]`, not directly observed in this caption.
- Given the `#lumapartner` tag, this reel likely also serves as **brand-partnership deliverable content**
  for Luma AI itself `[INFERRED]`, which is directly relevant to why it may have received paid boost (a
  self-funded or partner-funded push to maximize a sponsored asset's reach).

#### 7. Replicability verdict
- TEMPLATE: (1) open on the finished, striking AI-generated result, not the process; (2) narrate in a
  tight explainer-script cadence (short declarative sentences, one idea per line); (3) show the
  input→output transformation visually (before/after or first-frame/last-frame framing); (4) gate the
  step-by-step behind a comment-keyword DM; (5) tag the tool/brand explicitly.
- Commodity vs. unfair advantage: the explainer-script cadence and split-frame packaging template are
  fully commodity/replicable. The unfair advantage is Kallaway's **apparent access to paid distribution**
  (ad-boost, per the re-verification finding) and any direct brand relationship (Luma) that may have
  funded it — neither of which a new account can assume it has.
- Difficulty for Tangent: MED for the packaging/script craft (learnable); the raw-view outcome specifically
  is **not replicable via organic craft alone** if the re-verification's ad-boost read is correct — this
  is the single most important caveat for anyone trying to reverse-engineer this account's top-line
  numbers.

#### 8. Why it won (or lost) — analyst synthesis
The single most load-bearing factor, per the re-verification evidence, is **probable paid distribution**,
not organic packaging craft — the like-rate is 15-100x lower than this account's own confirmed-organic
pinned content, which is the strongest available signal that most of the 74.2M views came from a cold,
largely non-engaging, ad-served audience rather than the algorithm's organic "audition" mechanism (§1.1.3).
That said, the packaging is genuinely well-crafted (split-frame proof-of-process, tight script, branded
partnership hook) and likely explains why the boosted spend converted into *some* real engagement rather
than none — the craft sets a floor, the spend sets the ceiling. Luck/timing: the `#lumapartner` tag
suggests this was timed to a Luma product moment, giving it topical relevance that a purely organic boost
of generic content might lack.

#### Sources
- instagram.com/reel/DVhB8rMjp1m (`[OBSERVED]` via yt-dlp, 2026-07-25)
- /Users/sparsh/Documents/Projects/Tangent/social_launch/research/ig_harvest/kallaway.md (grid scrape +
  re-verification section)
- linkedin.com/in/kanekallaway/ ; sandcastles.ai (`[REPORTED]`, cross-platform/product context)

---

### VIDEO 2 (TOP #2 by raw views, mid-grid position 27): "OpenAI Codex update — Computer Use"

#### 0. Identity & stats
- URL: instagram.com/reel/DXSDF9djpRD. Posted **Apr 18, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP (same structural limitation as Video 1).
- Views: **39.5M** `[OBSERVED, harvest grid scrape]`. Comments: **77** `[OBSERVED via yt-dlp, matches
  exactly across both this dossier's pull and the re-verification pull]`. Likes: **DISCREPANT — this
  dossier's pull: 4,223; re-verification pull: 476** `[OBSERVED, both 2026-07-25]`. Like-rate range
  0.0107% (mine) to 0.0012% (re-verification) — again far below the account's organic norm.
- Rank: #2 raw-views reel, grid position 27 (mid-grid, unpinned). 39.5M / 177K median ≈ 223x.

#### 1. Packaging
- Caption opens: "OpenAI just launched a massive update for Codex." `[OBSERVED]` — a news-anchor-style
  factual lede, not a personal claim.
- Cover-thumbnail `[OBSERVED]`: same branded split-frame template as Video 1 — top half a real screen
  recording (a Codex terminal session building a "BeansTracker" coffee app, code diff visible), a red
  banner mid-frame reading "THE FUTURE OF WORK," Kallaway talking-head at bottom pointing upward, and a
  large "Codex / OPENAI" wordmark. **Confirms the branded-package format is a repeatable, account-level
  signature**, not a one-off for the sponsored Luma post — this is a non-partner-tagged post using the
  identical visual grammar.
- Hashtag `#chatgptpartner` present `[OBSERVED]` — same self-declared brand-tie-in pattern as Video 1's
  `#lumapartner`, this time with OpenAI/ChatGPT.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption, same transcript-fidelity caveat as Video 1]`: **"OpenAI
  just launched a massive update for Codex."**
- Hook taxonomy: **bold claim / news-first** — states a factual claim with an intensifier ("massive") but
  does not yet reveal what changed; the news itself is the curiosity gap.
- What the viewer sees first (per thumbnail): a live coding/preview interface already in motion — a
  result-first visual even though the hook line is spoken-news framing rather than a demonstrated result.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: news-hook → concrete feature list (in-sidebar app/doc/image
  previews) → reframe ("the sneaky most impressive thing... has nothing to do with coding — it's about
  productivity") → named killer-feature (Computer Use: "see, click, and type across any app") → concrete
  use-case (a "Chief of Staff" automation scanning Slack/Notion/Gmail/Calendar) → repeated
  claim-reinforcement ("I'm telling you...") → CTA.
- One-idea-per-video: technically a feature-list (multiple capabilities named), but organized under one
  frame — "this Codex update matters even if you don't code" — consistent with the valid listicle
  exception in §3.2 (one unifying frame).
- Open loop: "why does a coding update matter to non-coders?" opened early, resolved at the reframe beat
  ("actually has nothing to do with coding... it's about productivity").
- Notable rhetorical device (recurs across this account, see mini-architecture below): **the anticipated-
  objection acknowledgment** — the caption pre-empts "why would I care about a coding tool" before the
  viewer thinks it.

#### 4. Value proposition
- Walk-away value: concrete tool-capability knowledge (Codex now has Computer Use, image gen, in-sidebar
  previews) + a specific automation idea (Chief of Staff bot) the viewer could build.
- Practical value class: **tool discovery** (primary) + a seed of a **copyable workflow** (the Chief of
  Staff idea, though not built out step-by-step in-caption).
- Specificity: MED — names the exact new capability set and one concrete use-case, but (as with Video 1)
  gates deeper how-to behind the "comment AI" funnel rather than fully disclosing in-video.

#### 5. Psychology scoring
- STEPPS: **Practical Value** (a real capability update relevant to daily productivity, not just
  developers) is dominant. **Social Currency**: MED — "found out Codex secretly does X" carries mild
  insider-knowledge framing. **Emotion**: closer to **interest/mild awe** than high-arousal awe — a
  product-update video is inherently lower-spectacle than Video 1's cinematic AI-art reveal, which is
  itself a plausible **content-quality** reason (independent of the boost question) this reel might
  organically under-index on shares relative to Video 1.
- Primary emotion + arousal: interest / mild-awe, MED arousal — notably lower-register than Video 1.
- Identity-signaling share motive: "I'm tracking every AI tool update as it lands" — plugged-in framing.
- Save/send trigger: MED-HIGH — a viewer building automations has a concrete reason to save this as a
  feature-reference.

#### 6. CTA & funnel mechanics
- Explicit CTA: "comment 'AI' and I'll send you the link directly" — comment-to-DM funnel, content-backed.
- Funnel position: top-of-funnel tool-awareness content; the `#chatgptpartner` tag again suggests possible
  brand-deliverable status `[INFERRED]`.

#### 7. Replicability verdict
- TEMPLATE: (1) open on a factual "X just launched Y" news-lede; (2) list concrete new capabilities in
  short declarative beats; (3) reframe toward a broader audience than the literal tool's users ("even if
  you don't code"); (4) end on one named concrete use-case; (5) gate follow-through behind a comment.
- Commodity vs. unfair advantage: the news-reaction format itself is highly commodity (any AI account can
  react to a product launch same-day) — Kallaway's advantage is speed-to-post plus the same probable-boost
  distribution advantage flagged in Video 1.
- Difficulty for Tangent: LOW-MED for the format; the outcome (39.5M views) is again **not attributable to
  format alone** given the like-rate anomaly.

#### 8. Why it won (or lost) — analyst synthesis
Same primary driver as Video 1: the like-rate anomaly (0.001%-0.01%, vs. this account's confirmed-organic
1.3%-4.4%) is the strongest evidence that raw reach here is substantially boosted/paid rather than
algorithmically-organic. Secondary factor: this is a lower-arousal, more purely informational topic than
Video 1's cinematic-art reveal, which — if the boost hypothesis is correct — may partly explain why its
(disputed) like counts sit even lower in absolute terms than Video 1's despite a comparable view count;
informational news-reaction content typically converts passive ad-impressions into likes at a lower rate
than visually spectacular content. Timing: news-reaction to a same-week Codex launch is a real
trend-response play (§3.3.3/§4) independent of any paid component.

#### Sources
- instagram.com/reel/DXSDF9djpRD (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/kallaway.md (grid scrape + re-verification section)

---

### VIDEO 3 (TOP #3 by raw views, mid-grid position 18): "OpenAI solves the Unit Distance Problem"

#### 0. Identity & stats
- URL: instagram.com/reel/DY7GAsGuwGr. Posted **May 29, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP.
- Views: **35.8M** `[OBSERVED, harvest grid scrape]`. Comments: **99** `[OBSERVED, matches across both
  pulls]`. Likes: **DISCREPANT — this dossier's pull: 5,188; re-verification pull: 2,850** `[OBSERVED,
  both 2026-07-25]`. Like-rate range 0.0145% (mine) to 0.0080% (re-verification) — the *highest* like-rate
  of the three spikes under either reading, but still ~100x below the account's confirmed-organic norm.
- Rank: #3 raw-views reel, grid position 18. 35.8M / 177K median ≈ 202x.
- **No `#…partner` hashtag detected on this reel** `[OBSERVED]` — the one mega-spike of the three with no
  self-declared brand-tie-in tag, which somewhat weakens the "sponsored-content boost" sub-hypothesis for
  this specific video even though the self-funded-ad-spend hypothesis remains fully consistent.

#### 1. Packaging
- Caption opens: "OpenAI just solved one of the most famous math problems in the world." `[OBSERVED]` —
  bold claim, maximal-stakes framing ("most famous... in the world").
- Cover-thumbnail `[OBSERVED]`: same branded split-frame template — top half a moody, cinematic archival-
  style close-up of a young man's face mid-thought (illustrative/stock-style B-roll, not a literal Codex
  screen recording this time) under a red "OPENAI'S MATH BREAKTHROUGH" banner, Kallaway talking-head below
  with a cursive "OpenAI solves" + bold "MATH" wordmark. Confirms the template generalizes across topic
  types (creative tool demo, product update, pure-research news) with the same visual grammar.
- **Distinctive rhetorical device, present here and in the flop (Video 4) but not the first two spikes**:
  the caption immediately pre-empts audience skepticism about relevance — "And it sounds super nerdy…" —
  before pivoting to stakes ("But this moment will go down as one of the most important breakthroughs in
  the future of humanity"). This objection-naming device is a recurring, extractable hook-architecture
  element for this account (see mini-architecture below).

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: **"OpenAI just solved one of the most famous math
  problems in the world."**
- Hook taxonomy: **bold claim**, maximal-superlative framing, immediately followed (within the first two
  caption lines) by the objection-preempt ("sounds super nerdy") — a two-beat hook rather than a single
  line, distinctive to this account's science/research-news format.
- What the viewer sees first (per thumbnail): an evocative, mysterious face-in-shadow B-roll image rather
  than a literal screen-recorded proof — a more editorial/documentary visual choice than Videos 1-2's
  direct product-demo footage.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: bold claim → objection-preempt ("sounds nerdy, but...") → reframe
  toward the *real* story (not the problem, but *how* the AI solved it) → contrast-setup ("AI models were
  really good at brute force... but not all problems require brute force") → reveal (the model showed
  "raw creativity," a chain of reasoning "humans would have never thought to try") → stakes-escalation
  ("cures for cancer, new materials, brand new physics") → historical-marker close ("this moment, in May
  2026, will be marked in history"). **No comment-keyword CTA** — the caption ends on "Follow @kallaway,"
  a notable structural difference from Videos 1-2.
- One-idea-per-video: yes — "AI demonstrated genuine creative reasoning, not just brute-force search."
  Payoff is end-loaded: the "how" is withheld until roughly two-thirds through the caption.
- Open loop: "what's actually special about *how* it solved this?" opened early, closed at the "raw
  creativity" reveal — strong §2.6.1 late-payoff structure.
- Pacing: caption alone suggests a talking-head-led essay/explainer rather than a screen-recording demo
  (no described UI, no described visual proof-of-output) — DATA GAP on whether any B-roll accompanies the
  narration beyond the thumbnail's single evocative image.

#### 4. Value proposition
- Walk-away value: primarily **news/aspiration/identity** ("I understand what this AI breakthrough
  actually means") rather than a copyable workflow — this is the account's most purely editorial/
  news-commentary entry of the three spikes.
- Practical value class: **news** (primary), secondarily **aspiration** (being early to understand a
  civilizational-scale claim).
- Specificity: LOW-MED — no tool name to try, no workflow, no gated PDF/link; the value is entirely
  narrative/explanatory, not actionable. This is a meaningful contrast with Videos 1-2 and the flop, all
  of which offer at least a gated actionable artifact.

#### 5. Psychology scoring
- STEPPS: **Social Currency** is the dominant pillar — sharing "AI just got creative, here's what that
  means for cancer/physics/everything" is a maximal-stakes, ahead-of-the-curve claim (§2.2). **Emotion**:
  awe, but tilted toward **anxiety/awe blend** given the "everything is on the table" framing touches
  civilizational stakes — both are high-arousal per §2.3. **Practical Value**: weak/absent — no
  actionable takeaway. **Triggers/Public/Story**: weak-to-mild.
- Primary emotion + arousal: awe/wonder with an anxiety undertone, high arousal.
- Identity-signaling share motive: "I understood a genuine scientific breakthrough before most people" —
  strong social-currency motive, arguably the strongest of the three spikes given the "most famous math
  problem... in history" framing.
- Save/send trigger: LOW — no reference-utility (nothing to look up later), so this is a watch-and-share
  video, not a save-for-later one, per §2.7's distinction.

#### 6. CTA & funnel mechanics
- Explicit CTA: **none** beyond "Follow @kallaway for more videos like this" — no comment-keyword funnel,
  unlike Videos 1-2 and the account's typical pattern. This is the account's purest top-of-funnel
  brand-awareness play among the four videos analyzed.
- Funnel position: top-of-funnel only; no lead-magnet or DM funnel attached to this specific video.

#### 7. Replicability verdict
- TEMPLATE: (1) claim a maximal-stakes bold headline; (2) immediately pre-empt the "why should I care"
  objection; (3) reframe from the surface-level fact to the *mechanism* that makes it special; (4) escalate
  stakes to a broad, emotionally resonant set of implications; (5) close on a historical-marker line rather
  than a CTA.
- Commodity vs. unfair advantage: the news-commentary format and objection-preempt device are fully
  learnable/commodity. No brand-partnership tag here, so (if the boost hypothesis holds) the unfair
  advantage is purely **paid distribution capacity**, without even a sponsor subsidizing it — i.e. this
  reads as the account's own marketing/ad budget, not a brand deal.
- Difficulty for Tangent: LOW for the script format; the raw-reach outcome is again not attributable to
  organic craft given the engagement-rate evidence.

#### 8. Why it won (or lost) — analyst synthesis
As with Videos 1-2, the like-rate anomaly (0.008%-0.0145%, vs. 1.3%-4.4% organic norm) is the strongest
available evidence this reel's reach was substantially non-organic. What differs here: no partner hashtag,
no CTA/funnel — this is the "purest" of the three spikes in terms of content (a stakes-driven science
story with no commercial attachment), which somewhat strengthens the self-funded-ad-spend explanation over
a brand-sponsorship explanation for this specific video, since there is no obvious sponsor to attribute a
boost to. The objection-preempt hook device and end-loaded "how it solved it" structure are genuinely
strong craft, consistent with this account's packaging reputation — but per the evidence, craft explains
the *shape* of the content, not the *scale* of its reach.

#### Sources
- instagram.com/reel/DY7GAsGuwGr (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/kallaway.md (grid scrape + re-verification section)

---

### VIDEO 4 (FLOP): "OpenAI solves 18 medical mysteries"

#### 0. Identity & stats
- URL: instagram.com/reel/DaAnAA3O5Sg. Posted **Jun 25, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP.
- Views: **19.6K** `[OBSERVED, harvest grid scrape]` — the account's lowest-viewed reel in the 48-tile
  sample (excluding the most recent tiles). Likes: **638**. Comments: **10** `[OBSERVED via yt-dlp,
  2026-07-25, HIGH — single pull, no discrepancy issue since this video was not part of the
  re-verification batch]`. Like-rate: **~3.25%** — notably **HIGHER** than any of the three "viral" spikes
  under either likes reading, and roughly in line with the account's genuinely-organic pinned tiles
  (1.3%-4.4%).
- Rank: bottom of the 48-tile sample. 19.6K / 177K median ≈ 0.11x (i.e., this flop under-performs the
  account's own median by ~9x).

#### 1. Packaging
- Caption opens: "OpenAI just helped solve 18 medical mysteries." `[OBSERVED]` — same bold-claim template
  as Video 3, slightly softer superlative ("helped solve" vs. "solved").
- Cover-thumbnail `[OBSERVED]`: **identical branded template** to the other three — top half a stock-style
  molecular/DNA-strand B-roll image under a red "OPENAI'S MEDICAL BREAKTHROUGH" banner, Kallaway
  talking-head below with cursive "OpenAI" + bold "MEDICAL" wordmark. **Visually and structurally almost
  indistinguishable from Video 3's packaging** (same color grade, same banner style, same B-roll-style
  cutaway, same talking-head pose) — this is the single strongest piece of evidence in this account's
  entire sample that **packaging format alone does not explain the variance between a 35.8M spike and a
  19.6K flop**, since the two share nearly identical packaging DNA.
- Same objection-preempt device present: "And it sounds super niche…" `[OBSERVED]` — directly parallel to
  Video 3's "sounds super nerdy" line, confirming this is a deliberate, reused rhetorical template, not a
  one-off phrase.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: **"OpenAI just helped solve 18 medical mysteries."**
- Hook taxonomy: bold claim + objection-preempt, identical structural DNA to Video 3.
- What the viewer sees first: a molecular-structure B-roll image, similar register to Video 3's evocative
  face-in-shadow shot.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: bold claim → objection-preempt → stakes ("going to change modern
  medicine and genomics forever") → problem-context (8,000+ rare diseases, no doctor can hold them all in
  memory) → mechanism reveal (OpenAI's o3 re-analyzed 376 unsolved cases, cross-referencing genes/symptoms/
  literature) → concrete proof-point ("spotted a problem in a child's DNA sequencing that wasn't labeled
  anywhere in the data") → verified outcome (18 confirmed new diagnoses) → stakes-close ("faster
  diagnoses... hope for millions"). **Structurally this is a near-perfect twin of Video 3's beat map** —
  same claim→preempt→mechanism→stakes arc, same end-loaded reveal, same no-CTA close ("Follow @kallaway").
- One-idea-per-video: yes, matching Video 3's discipline.
- Open loop/pacing: same pattern as Video 3 — a talking-head-led essay format with one evocative supporting
  image, not a demo-heavy screen recording.

#### 4. Value proposition
- Walk-away value: news/awe, same class as Video 3 — no tool, no workflow, no gated artifact.
- Practical value class: news (primary).
- Specificity: LOW — matches Video 3's register exactly.

#### 5. Psychology scoring
- STEPPS: same profile as Video 3 — Social Currency dominant (being first to know about an AI-medicine
  breakthrough), Emotion (awe/hope rather than anxiety this time — the framing is warmer, "hope for
  millions of patients" vs. Video 3's more ambivalent civilizational-stakes framing).
- Primary emotion + arousal: awe/hope, high arousal in principle — but see §8 for why this likely
  under-delivered in practice.
- Identity-signaling share motive: present in principle (medical-breakthrough news carries real social
  currency), but medical/genetics content may have a narrower addressable "who would I send this to"
  audience than a universal "AI got creative" framing (Video 3) or a practical tool update (Videos 1-2).
- Save/send trigger: LOW, same as Video 3 — no reference utility.

#### 6. CTA & funnel mechanics
- Explicit CTA: none — "Follow @kallaway for more videos like this," matching Video 3's no-funnel pattern.
- Funnel position: top-of-funnel only.

#### 7. Replicability verdict
- TEMPLATE: identical to Video 3's template — this flop is a structurally faithful execution of the
  account's own winning format, which is precisely what makes it analytically valuable as a flop.
- Commodity vs. unfair advantage: N/A — this video demonstrates that even a well-executed instance of the
  account's own proven template does not guarantee reach; something outside the template (topic pull,
  algorithmic luck, and/or absence of a paid boost) determined the outcome here.
- Difficulty for Tangent: the packaging/script skill is clearly replicable (this flop proves the creator
  himself replicated it faithfully); the missing ingredient for reach is not a craft variable this
  post-mortem can fully resolve — see §8.

#### 8. Why it lost — analyst synthesis, explicit delta vs. Video 3
This is the most important comparison pair in the account's sample: **Video 3 and Video 4 share
near-identical packaging (same thumbnail template, same color grade), near-identical hook architecture
(bold claim + "sounds super [nerdy/niche]" objection-preempt), near-identical structure (claim → preempt →
mechanism → stakes → no-CTA close), and near-identical topic domain (OpenAI reasoning-model breakthrough
news) — yet one reached 35.8M views and the other reached 19.6K, a ~1,800x gap.** Two candidate
explanations, both consistent with available evidence: (1) **Topic pull** — "solved a famous math problem"
has a more universal, headline-legible hook than "helped solve 18 rare pediatric genetic diseases,"
which requires more context (rare disease, genomics, pediatric specificity) to land the stakes, even
though the caption works hard to establish them; math-as-metaphor-for-general-intelligence is a more
recognizable narrative than a niche medical-research story. (2) **Absence of paid distribution** — if the
re-verification's ad-boost hypothesis is correct for the spikes, the simplest explanation for this flop is
that it simply wasn't boosted, and its 19.6K views represent this account's actual organic reach for a
well-crafted but niche-adjacent story — notably, this flop's 3.25% like-rate is fully consistent with (and
slightly above) the account's confirmed-organic pinned-tile range, suggesting **this flop is a more
honest read of the account's true organic ceiling than any of the three "spikes."**

#### Sources
- instagram.com/reel/DaAnAA3O5Sg (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/kallaway.md

---

## Kallaway: mini top-vs-flop delta

| Dimension | Top 3 (as originally framed) | Flop | Re-verified reality |
|---|---|---|---|
| Packaging template | Branded split-frame, red banner, talking-head + wordmark | **Identical template** (Video 4 vs. Video 3 especially) | Packaging is a constant, not a differentiator, across this account's sample |
| Hook device | Bold claim (+ objection-preempt on 2 of 3) | Bold claim + objection-preempt | Same device family used on winners and the loser alike |
| Like-rate | 0.0009%-0.09% (disputed range) | **3.25%** | The "flop" has a dramatically HEALTHIER organic engagement signature than any of the three raw-view leaders |
| CTA/funnel | 2 of 3 have comment-keyword funnels; 1 does not | None | No consistent CTA-presence correlation with reach |
| True organic ceiling | Represented by pinned tiles (4.3M/14.5M, 1.3%-4.4% like-rate) and this flop (19.6K, 3.25%) | — | The account's real organic range is closer to 20K-200K-ish with occasional multi-million legacy pins, NOT the 35-74M mid-grid numbers |

**One-paragraph verdict:** The pre-verification framing of this account as "a serial organic mega-viral
outlier producer" does not survive the re-verification pull. The account's genuine organic craft — strong
packaging, a repeatable branded-explainer format, a deliberate hook device (bold claim + objection-preempt)
— is real and visible across all four videos including the flop, and plausibly explains the account's
healthy 40% median/follower ratio and its two legitimately-pinned multi-million-view 2024 hits. But the
three specific mega-spikes this dossier was asked to center on are best explained by probable paid
distribution layered on top of that organic craft, not by the craft alone.

## Kallaway: mini content-architecture

`[INFERRED]` groupings from the 4 analyzed videos plus the wider 48-tile grid's topic pattern (visible in
caption previews during the harvest pass):

1. **AI-news-reaction explainer** (all 4 videos analyzed fit this: Luma tool launch, Codex update, math
   breakthrough, medical breakthrough) — a same-week-or-fresher reaction to an AI industry development,
   delivered in the tight claim→context→mechanism→stakes explainer script format. This appears to be the
   account's dominant, load-bearing format based on this sample.
2. **Branded/partnership deliverables** (Videos 1 and 2, tagged `#lumapartner`/`#chatgptpartner`) — a
   subset of the news-reaction format that doubles as sponsor content, `[INFERRED]` funding a paid-boost
   layer.
3. **Pure editorial/no-CTA science stories** (Videos 3 and 4) — the news-reaction format stripped of any
   commercial funnel, ending on a stakes-close rather than a lead-magnet ask; this pairing is also the
   one pairing in the sample with a confirmed near-identical structural twin (won vs. lost), making it the
   dossier's clearest natural experiment on what does and doesn't predict reach within this account.

**What sustains the account between spikes:** the news-reaction explainer format itself, running at a
177K organic median on a 442K-follower account (40% ratio) — a genuinely strong base-hit rate — with
occasional legitimate multi-million-view organic hits (the 2024 pinned pair) and, per this re-verification,
occasional paid pushes on selected recent posts that produce headline-grabbing but low-engagement-quality
view counts.

---

# ACCOUNT 2: Nick Saraev (@nick_saraev)

## Account header
- 568K followers, 165 following, 376 posts `[OBSERVED, ig_harvest/nick_saraev.md, 2026-07-25]`. Bio:
  "Digital creator / Founder @ Maker School / Helping 2000+ beginners land their First AI client / Get
  your first client in 90 days."
- Founder of **Maker School** (AI-automation-client-acquisition education, 90-day first-client guarantee)
  and **LeftClick** (a B2B AI-automation consultancy founded 2022) `[REPORTED,
  linkedin.com/in/nick-saraev/, nicksaraev.com/maker-school-2/, makerschoolnicksaraev.com/about, MED]`.
  Reported to teach "over 400K people on YouTube and approximately 500K on Instagram"
  `[REPORTED, search aggregation, MED — not independently re-verified against a primary dated source, but
  directionally consistent with this dossier's own YouTube-channel check below]`.
- **Cross-platform check** `[OBSERVED via yt-dlp, 2026-07-25]`: YouTube channel `@NickSaraev` is active
  and substantial — recent long-form video titles include AI-tool benchmarks/tests ("I Spent $400
  Benching Opus-5," "I Tested Kimi K3 So You Don't Have To") and Claude-Code-specific tutorials/courses
  ("How to Use Claude Code for FREE (2026)," "CLAUDE CODE ADVANCED FULL COURSE (3 HOURS)," "Claude Code +
  Nano Banana 2 + Kling = $15K Animated Sites"). **The "free Claude Code" theme repeats on YouTube too**
  — "How to Use Claude Code for FREE (2026)" (27.7 min, posted May 2, 2026) has 189,015 views, 3,457
  likes, 238 comments `[OBSERVED via yt-dlp direct pull, 2026-07-25, HIGH]`, confirming this is a durable
  cross-platform content pillar for Saraev, not an IG-only pattern.
- Separately, Saraev's **YouTube Shorts tab runs a totally different content pillar**: business-mindset/
  agency-operations clips ("Why Saturation Doesn't Matter," "Hiring full-time employees vs. contractors,"
  "Why I like B2B tech as a target niche") at 2.6K-46K views `[OBSERVED via yt-dlp flat-playlist,
  2026-07-25]` — far below both his IG Reels median (132.5K) and his YT long-form tool-content views. **He
  is running two structurally different formats on two different surfaces for two different purposes**:
  IG Reels = viral tool-hack discovery bait; YT Shorts = audience-nurture/credibility content for his
  existing community; YT long-form = deep tutorials/courses (the actual product-adjacent content).
- Median reel views 132.5K, top raw reel 1.7M, median/follower ratio 23.3%, top/median ratio ~12.8x — a
  **much tighter, more consistent distribution than Kallaway's 419x**, i.e. structurally the opposite
  variance profile.

---

### VIDEO 1 (TOP #1): "OmniRoute — free unlimited Claude Code"

#### 0. Identity & stats
- URL: instagram.com/reel/Da8ZthUPK98. Posted **Jul 18, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP.
- Views: **1.7M** `[OBSERVED, ig_harvest/nick_saraev.md]`. Likes: **57,437**. Comments: **32,079**
  `[OBSERVED via yt-dlp, 2026-07-25, HIGH — closely matches the harvest file's independent detail-pull
  (57K/32K), no material discrepancy on this account, unlike Kallaway]`. Like-rate ~3.38%, comment-rate
  ~1.89% — both far above Kallaway's disputed spikes and consistent with genuinely organic, highly-engaged
  reach.
- Rank: **#1 of 48 sampled reels**. 1.7M / 132.5K median ≈ 12.8x — the account's single largest multiple,
  but modest by this study's standards (compare Kallaway's 419x).

#### 1. Packaging
- Caption opens: "Comment 'CLAUDE' to get this AI tool to run Claude Code for free and with almost
  unlimited usage." `[OBSERVED]` — the CTA is placed in the very first caption line, ahead of any context,
  a distinctive structural choice for this account (front-loaded funnel, not end-loaded).
- Cover-thumbnail `[OBSERVED]`: a real selfie of Saraev making a "shush" finger-to-lips gesture, flanked by
  the Claude logo (top) and two app-icon glyphs, over bold white/red-highlight text "GET UNLIMITED CLAUDE
  CODE." The shush gesture is a deliberate **"secret/insider hack" visual cue** reinforcing the
  Social-Currency framing before a single word is read.
- Curiosity gap: minimal — this is a **fully-resolved-promise thumbnail** (the exact benefit is named:
  unlimited Claude Code, for free), trading curiosity-gap tension for immediate, unambiguous relevance to
  anyone who already uses or wants to use Claude Code.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: **"Comment 'CLAUDE' to get this AI tool to run Claude
  Code for free and with almost unlimited usage."**
- Hook taxonomy: **result-first / bold-claim hybrid**, but unusually the "result" stated is literally the
  CTA-and-benefit combined into one line — a compressed hook structure not seen in either of the other two
  accounts in this dossier.
- What the viewer sees first: Saraev's own face (shush gesture) rather than a screen recording or finished
  output — a parasocial/persona-forward opening (§2.4.1) rather than a demo-forward one.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: CTA-first hook → mechanism reveal (a GitHub tool, OmniRoute, routes
  Claude Code through 200+ free providers, auto-switches on rate-limit) → **analogy beat** ("Think of it
  like a relay race... when one runner gets tired, the next one picks up the baton") → second capability
  (prompt compression, "cuts token usage by up to 90%") → competitive-differentiation claim ("that's the
  part most routing tools get wrong") → compatibility list (Claude Code, Cursor, Codex, Copilot) →
  setup-ease claim ("one npm install") → stakes-close ("changes how much you can actually build in a day").
- One-idea-per-video: yes — "a free multi-provider router keeps Claude Code running past its rate limit."
  Payoff (the tool name and mechanism) is front-loaded in the hook itself, then the middle beats build
  credibility/differentiation rather than withholding the payoff — a **front-loaded-payoff, drip-loaded-
  credibility** structure, distinct from Kallaway's end-loaded-payoff pattern.
- Open loop: minimal — because the hook already resolves the core promise, the "loop" here is closer to
  "will this analogy/differentiation convince me it's not just another routing tool" than a classic
  curiosity gap.
- Pacing: caption structure (short punchy lines, an explicit analogy) implies a fast-cut screen-recording
  demo of the setup process — DATA GAP on confirmed visual pacing without the video file.

#### 4. Value proposition
- Walk-away value: a **directly copyable tool + workflow** (OmniRoute, npm install, config file) solving a
  named, felt pain point (hitting Claude Code's usage limits mid-project).
- Practical value class: **copyable workflow / tool discovery**, maximally specific — this is the most
  actionable of any video analyzed in this dossier across all three accounts.
- Specificity: HIGH — names the exact tool, the mechanism (200+ provider routing + prompt compression),
  the compatible tools list, and the setup step (one npm install) in-caption, without gating the core
  information behind the comment CTA (the CTA gates a guide/link, not the concept itself).

#### 5. Psychology scoring
- STEPPS: **Practical Value** is overwhelmingly dominant — this is "news you can use" in the most literal
  sense for a technical audience with a specific, recurring cost/frustration (§2.7). **Social Currency**:
  strong via the shush-gesture insider-hack framing (§2.2, §2.5). **Emotion**: relief/excitement at a
  removed constraint — a milder-arousal, more utilitarian positive emotion than Kallaway's awe-driven
  content, but Berger & Milkman's arousal principle (§2.3) still applies (excitement is high-arousal
  positive). **Triggers**: genuinely present and unusually strong for this niche — hitting a Claude Code
  rate limit is a **frequent, recurring environmental cue** for the exact audience this account targets,
  meaning the content is re-triggered every time a viewer hits that wall again (§2.2's Triggers pillar,
  rarely this well-matched in the wider study).
- Primary emotion + arousal: excitement/relief, high arousal (a real cost/frustration is being removed).
- Identity-signaling share motive: "I found the arbitrage before you did" — classic tool-arbitrage
  social currency, structurally identical to flight-hacking/credit-card-churning content in other niches.
- Save/send trigger: HIGH and highly specific — "send this to the dev friend who complains about hitting
  Claude limits" is about as addressable as a send-trigger gets (§1.1.2, §2.7).

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'CLAUDE'" — front-loaded (first caption line, not last), content-backed (the tool
  and mechanism are explained regardless of whether the viewer comments).
- Comment-bait mechanics: comment count (32,079) is unusually high relative to likes (57,437) — a
  ~56% comment-to-like ratio, far higher than typical organic content, strongly suggesting the comment-CTA
  itself is functioning as the primary engagement engine, converting curiosity into a trackable,
  algorithmically-favorable action (comments, and the DMs they trigger, are both counted engagement AND
  the literal product-delivery mechanism).
- Funnel position: top-of-funnel discovery bait that converts directly into a DM'd guide — likely a
  soft on-ramp toward Maker School, though that link is `[INFERRED]`, not stated in this caption.

#### 7. Replicability verdict
- TEMPLATE: (1) state the CTA and the resolved benefit in the very first line, no curiosity-gap
  withholding; (2) name the exact tool/mechanism immediately; (3) use one concrete analogy to explain a
  technical mechanism in lay terms; (4) list compatibility/differentiation to pre-empt "is this just
  another X" skepticism; (5) close on a stakes statement tied to daily output/productivity.
- Commodity vs. unfair advantage: the format is highly commodity and explicitly teachable (this creator's
  entire business is teaching exactly this kind of content). Saraev's specific advantage is being
  early/fast to surface a genuinely new free tool to an audience that already has the underlying paid-tool
  pain point — an advantage of **information arbitrage speed**, not of production value or platform
  access.
- Difficulty for Tangent: LOW-MED — the format is straightforward, but it requires (a) an audience with a
  shared, specific technical pain point, and (b) genuinely being early to a real solution, which is a
  sourcing/timing skill more than a production skill.

#### 8. Why it won — analyst synthesis
The load-bearing factor is the **direct pairing of a specific, recurring, felt pain point (Claude Code
rate limits) with a specific, verifiable, free fix**, delivered with front-loaded clarity rather than
curiosity-gap withholding — this content type scores exceptionally on Triggers (re-activated every time
the pain recurs), Practical Value, and a maximally addressable Save/Send motive, three of STEPPS' six
pillars simultaneously and unusually strongly matched to this account's specific technical audience.
Secondary factor: the unusually high comment-to-like ratio suggests the comment-CTA mechanic itself is
doing outsized algorithmic work (§1.1.2's sends/comments-weighted-higher-than-likes principle). No luck/
timing component is evident beyond general Claude Code being a currently-hot, currently-rate-limited tool
in mid-2026 — this is squarely a "solve a real, current pain point" win, not a trend-surf or a boosted
post (unlike Kallaway's spikes, this account's engagement-rate profile shows no anomaly).

#### Sources
- instagram.com/reel/Da8ZthUPK98 (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/nick_saraev.md

---

### VIDEO 2 (TOP #2): "Claude Code + Google Stitch — $15K animated websites"

#### 0. Identity & stats
- URL: instagram.com/reel/DXqzDc6j-H_. Posted **Apr 28, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP.
- Views: **1.1M** `[OBSERVED, harvest]`. Likes: **37,780**. Comments: **31,562** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 38K/32K]`. Like-rate ~3.43%, comment-rate ~2.87% — again high and
  organic-consistent.
- Rank: #2 of 48. 1.1M / 132.5K ≈ 8.3x.

#### 1. Packaging
- Caption opens: "Comment 'CODING' to get the full guide on how Build Stunning Animated websites Using
  Claude Code + Google Stitch + MotionSites." `[OBSERVED]` — same front-loaded CTA-first structure as
  Video 1, and same "grammatically loose, punchy fragments" caption voice.
- Cover-thumbnail `[OBSERVED]`: same template family as Video 1 — real smiling selfie, Claude + Stitch +
  Google logos arrayed around his head, bold text "CLAUDE + STITCH = $15K WEBSITES." The **dollar-value
  framing** ("$15K websites") is a distinct escalation from Video 1's "unlimited/free" framing — this
  thumbnail sells income potential, not just cost-avoidance.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: "Claude Code is amazing at coding. But it struggles at
  frontend design. Here's a simple fix."
- Hook taxonomy: **problem-acknowledgment + bold-claim-fix** — names a specific, credible limitation of a
  tool the audience already trusts/uses (building credibility by not overselling Claude Code), then
  promises a fix — a more nuanced hook than a pure bold claim, and one that pre-empts audience skepticism
  by agreeing with a known pain point first.
- What the viewer sees first: Saraev's smiling selfie with tool logos — persona-forward, matching Video 1.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: problem statement (Claude Code's weak frontend design) → fix-intro
  (pair with Google Stitch) → step-by-step walkthrough (describe app idea in plain words → add reference
  images → export via MCP → paste into Claude Code → run a given prompt, quoted verbatim in the caption) →
  payoff description ("Claude builds real code. Screens connect. Animations flow.") → proof-point ("One
  dev built a dashboard. Took 20 minutes. Client said yes.") → **numbered 6-step recap** → CTA-adjacent
  close ("Done and Ship your first app").
- One-idea-per-video: yes, and notably this is the **most step-by-step-explicit** of any video analyzed in
  this entire dossier — it includes a literal copy-paste-ready prompt ("Turn these Stitch designs into
  code. Make all screens. Link them up...") inside the caption itself, plus a clean numbered recap list.
- Open loop: "can Claude Code's weak point actually be fixed with a free pairing?" opened at the hook,
  closed at the "20 minutes, client said yes" proof-point.
- Pacing: caption's short, staccato sentence style ("Like magic. Your rough idea turns pro. Tweak it
  fast.") strongly implies a fast-cut, high-pacing screen-recording demo — consistent with the general
  §3.3.2 principle (dynamic pacing favored) even though exact cut frequency is a DATA GAP.

#### 4. Value proposition
- Walk-away value: a complete, named, copy-pasteable **multi-tool workflow** (Stitch → MCP export → Claude
  Code) with an exact prompt text and a numbered step list, plus an implied income outcome ($15K).
- Practical value class: **copyable workflow** (maximal — includes verbatim prompt text) + **aspiration**
  (the dollar framing).
- Specificity: HIGH — matches Video 1's specificity level, arguably exceeds it by including verbatim
  prompt text in the caption itself rather than gating it behind the comment funnel.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant again (a genuinely complete, reusable workflow). **Social
  Currency**: present via the income-framing ("$15K websites," "client said yes" — signals the sharer
  knows a real monetization path). **Emotion**: excitement/aspiration, high-arousal positive. **Triggers**:
  present but narrower than Video 1's (frontend-design frustration is common among Claude Code users but
  less universally recurring than hitting a hard rate-limit wall).
- Primary emotion + arousal: excitement/aspiration, high arousal.
- Identity-signaling share motive: "I know how to turn a coding-AI limitation into a billable service" —
  a professional-competence signal, appealing to Saraev's specific audience (aspiring AI-service
  freelancers, matching his Maker School positioning).
- Save/send trigger: HIGH — the numbered step-list and verbatim prompt make this genuinely bookmark-worthy
  reference content, arguably the single most "save"-optimized video in this dossier.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'CODING'" for "the full guide" — content-backed (a working prompt and step list
  are already given in-caption, so the gated "full guide" is a bonus, not the only value).
- Comment-bait mechanics: comment-to-like ratio ~84% (31,562/37,780) — even higher relative-comment
  intensity than Video 1, again consistent with the comment-CTA acting as this account's core engagement
  engine.
- Funnel position: top-of-funnel with a direct monetization narrative ("client said yes") that plausibly
  nurtures toward Maker School / LeftClick positioning, `[INFERRED]` from bio context, not stated in-video.

#### 7. Replicability verdict
- TEMPLATE: (1) open by validating a known limitation of a popular tool (credibility-building, not
  oversell); (2) name the exact fix/pairing; (3) give a genuine step-by-step including a copy-pasteable
  prompt; (4) include one concrete social-proof anecdote; (5) close with a numbered recap.
- Commodity vs. unfair advantage: highly teachable format; Saraev's edge is combining two-plus AI tools
  into a single coherent workflow before it's obvious/common knowledge to do so — a synthesis/sequencing
  skill rather than a single-tool discovery.
- Difficulty for Tangent: MED — requires genuine hands-on tool fluency across multiple products to produce
  a credible, specific, tested workflow (not fakeable with a vague gesture at the idea).

#### 8. Why it won — analyst synthesis
This video wins on **maximal specificity plus credibility-first framing** — naming Claude Code's actual
weakness before pitching the fix builds trust with a technically sophisticated audience that would
otherwise be skeptical of an unqualified "Claude Code can do everything" claim, and the inclusion of a
verbatim, ready-to-use prompt converts the video into genuine standalone reference material rather than a
teaser. The income-framing ("$15K websites," "client said yes") adds an aspiration layer on top of the
practical-value core, widening the content's appeal from "developers hitting a wall" to "aspiring
AI-freelancers looking for a billable service" — a slightly broader addressable audience than Video 1's
narrower rate-limit-specific trigger, though still well within Saraev's core niche (consistent with his
somewhat lower rank, #2 vs #1, if broader-but-shallower resonance underperforms narrower-but-sharper pain-
point resonance at the margin).

#### Sources
- instagram.com/reel/DXqzDc6j-H_ (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/nick_saraev.md

---

### VIDEO 3 (TOP #3): "10+ free AI vibe-coding tools by Google"

#### 0. Identity & stats
- URL: instagram.com/reel/DSm-QQ_Dxh3. Posted **Dec 23, 2025** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP.
- Views: **973K** `[OBSERVED, harvest]`. Likes: **34,416**. Comments: **10,062** `[OBSERVED via yt-dlp,
  2026-07-25, matches harvest's 34K/10K]`. Like-rate ~3.54%, comment-rate ~1.03% — the highest like-rate,
  lowest comment-rate of Saraev's top 3, a different engagement shape than Videos 1-2.
- Rank: #3 of 48. 973K / 132.5K ≈ 7.3x. Notably the **oldest** of the top-3 (Dec 2025 vs. Apr/Jul 2026 for
  the other two) — this reel has had the longest window to accumulate views, a relevant caveat for any
  cross-video reach comparison.

#### 1. Packaging
- Caption opens: "Comment 'GOOGLE' to get all these Free AI Vibe Coding Tools by Google." `[OBSERVED]` —
  same front-loaded CTA pattern as Videos 1-2.
- Cover-thumbnail `[OBSERVED]`: same template — smiling selfie, this time flanked by Chrome/Google logo
  glyphs, bold text "10+ FREE AI CODERS BY GOOGLE." This is the account's **listicle-format** entry among
  the top 3 (a numbered roundup rather than a single-tool-pairing demo).

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: "While everyone's been losing their minds over ChatGPT
  and Cursor. Google has been quietly dropping over 10+ free AI coding tools."
- Hook taxonomy: **"nobody's talking about X" / contrarian-attention hook** — explicitly contrasts where
  the audience's attention currently is (ChatGPT, Cursor) against an underrated alternative (Google's
  tool suite), the clearest example of this specific taxonomy bucket (§3.1) across all three accounts in
  this dossier.
- What the viewer sees first: smiling selfie + tool logos, consistent persona-forward opening.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: contrarian-attention hook → tool 1 (Antigravity, code editor, with a
  quoted example prompt and result) → tool 2 (AI Studio, "Lego for prototypes") → tool 3 (Stitch, design
  tool, cross-referencing Video 2's tool) → tool 4 (Opal, no-code n8n-like automation, with a 3-bullet
  mini-list) → tool 5 (Jules, coding agent, with a personal-use anecdote "I tried it on my side project
  last week") → close ("That's five from 12," naming two more tools in passing) → CTA (comment "GOOGLE").
- One-idea-per-video: this is the account's clearest **listicle exception case** per §3.2 — five (of a
  claimed 12) sub-payoffs under one unifying frame ("Google's underrated free AI tool suite"), each with
  its own micro-demo/example, which is the valid listicle structure rather than a rule violation.
- Open loop: "what are all these quiet Google tools?" opened at the hook, partially closed (5 of 12
  detailed) by the end — a deliberately **incomplete close**, which functions as its own soft CTA/curiosity
  hook toward the gated full list.
- Pacing: five distinct tool-segments in one reel implies a fast, high-density cut structure — DATA GAP on
  confirmed visual pacing.

#### 4. Value proposition
- Walk-away value: awareness of 5+ concrete named tools, each with a one-line differentiator and a
  micro-example, plus a gated "all 12" list.
- Practical value class: **tool discovery** (breadth-first) rather than Videos 1-2's depth-first single-
  workflow value — a genuinely different value shape within the same account.
- Specificity: MED-HIGH — each tool gets a real, specific example ("Make a responsive e-commerce page with
  login" for Antigravity) rather than vague description, but breadth necessarily trades off against the
  step-by-step depth of Video 2.

#### 5. Psychology scoring
- STEPPS: **Social Currency** is unusually strong here via the explicit contrarian frame ("while everyone's
  losing their minds over ChatGPT and Cursor...") — sharing this signals the sharer sees past the
  consensus hype cycle (§2.2, §2.5). **Practical Value**: strong (tool discovery, breadth). **Triggers**:
  MED — "free AI coding tools" is a recurring topic in this audience's feed generally, though this video
  doesn't tie to one specific recurring pain point the way Video 1 does.
- Primary emotion + arousal: curiosity/mild-FOMO ("what am I missing"), MED-high arousal.
- Identity-signaling share motive: "I know about tools before they're mainstream" — strong, explicit
  contrarian-insider framing.
- Save/send trigger: HIGH — a numbered tool-roundup is close to a canonical "save for later reference"
  format per §2.7's list-content marker.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'GOOGLE'" for the complete list — content-backed (5 of 12 tools already delivered
  free in-caption).
- Comment-bait mechanics: comment-to-like ratio ~29% (10,062/34,416) — notably lower than Videos 1-2's
  ~56-84%, consistent with a listicle/awareness format generating more passive likes and fewer "give me
  the thing" comments than a single-tool arbitrage hack does.
- Funnel position: top-of-funnel breadth content, same general funnel shape as Videos 1-2.

#### 7. Replicability verdict
- TEMPLATE: (1) open with an explicit contrarian-attention contrast ("everyone's looking at X, but Y is
  quietly better"); (2) deliver several (not all) named tools each with one concrete example; (3)
  deliberately under-deliver the full count to motivate the CTA; (4) close with a comment-gated complete
  list.
- Commodity vs. unfair advantage: highly replicable structurally; requires genuine breadth of hands-on
  tool familiarity to make each micro-example credible and specific rather than generic.
- Difficulty for Tangent: LOW-MED — a roundup format is accessible, but credibility depends on actually
  having tried each tool, which is a research-time cost, not a production-skill barrier.

#### 8. Why it won — analyst synthesis
The contrarian-attention hook ("everyone's watching ChatGPT/Cursor, Google is quietly better") is the
single most distinctive craft element here — it converts a plain tool-roundup into an implicit
insider-knowledge claim, maximizing Social Currency in a way a neutral "here are some Google AI tools"
framing would not. The listicle structure (5 detailed of a promised 12) is a well-executed instance of the
valid listicle exception, using incompleteness itself as a retention/CTA device. Being the account's oldest
top-3 video (posted Dec 2025, ~7 months before this harvest) is a real, disclosed confound — it has had
substantially more time to accumulate views than Videos 1-2, so its rank-3 position may partly reflect
accumulated time rather than a lower per-day velocity; this dossier cannot fully disentangle velocity from
elapsed time without daily view-history data, which was not obtainable — logged as a DATA GAP rather than
papered over.

#### Sources
- instagram.com/reel/DSm-QQ_Dxh3 (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/nick_saraev.md

---

### VIDEO 4 (FLOP): "YouMind — free AI prompt library"

#### 0. Identity & stats
- URL: instagram.com/reel/DbLpxfKPKoN. Posted **Jul 24, 2026** `[OBSERVED via yt-dlp, HIGH]` — **one day
  before this harvest's data-pull date (Jul 25, 2026)**, a material caveat: this reel was likely still in
  its early algorithmic "audition" window (§1.1.3) at time of measurement and its final view total is not
  yet settled.
- Views: **44.2K** `[OBSERVED, harvest]`. Likes: **1,192**. Comments: **1,489** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 1,184/1,471]`. Like-rate ~2.70%, comment-rate ~3.37% — **comment-
  rate here is actually the HIGHEST of any of the four Saraev videos analyzed**, and the like-rate is
  comparable to (not dramatically below) the top-3's 3.4-3.5% range.
- Rank: bottom of the 48-tile sample (tied for lowest with one other reel). 44.2K / 132.5K ≈ 0.33x.

#### 1. Packaging
- Caption opens: "Comment 'PROMPT' to get this free AI prompts library." `[OBSERVED]` — identical
  front-loaded CTA structure to all three top performers.
- Cover-thumbnail `[OBSERVED]`: same template family exactly — smiling selfie, this time flanked by a
  banana emoji (referencing "Nano Banana," a Google image model) and the Google "G" glyph, bold text
  "BIGGEST AI PROMPT LIBRARY." **Visually indistinguishable in production quality/format from the three
  top performers** — same lighting, same graphic treatment, same font/color choices.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: "This website is basically Pinterest, but for AI
  prompts."
- Hook taxonomy: **analogy-first bold claim** — leads with a familiar-brand comparison (Pinterest) to
  instantly convey the product category, a legitimate and common hook device, structurally sound.
- What the viewer sees first: same persona-forward selfie-plus-logos opening as the top 3.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: analogy hook → tool name (YouMind) → scale claim (30,000+ prompts) →
  organization claim (by model/style/use-case) → use-case examples (thumbnails, infographics, cinematic
  shots) → cadence claim (new prompts daily) → workflow benefit ("you're not starting from a blank box
  anymore") → platform-integration claim (runs directly inside YouMind, no tab-switching) → close (repeat
  cadence claim).
- One-idea-per-video: yes — "a searchable, organized library of ready-to-use AI prompts." Structurally
  sound, matching the top 3's discipline.
- Open loop/pacing: same general shape as the top 3 — no structural defect is evident from the caption
  alone.

#### 4. Value proposition
- Walk-away value: tool discovery (a prompt-library site) + implied time-savings ("not starting from a
  blank box").
- Practical value class: tool discovery, MED specificity (names the tool and its scale claim, but — unlike
  Video 2's verbatim workflow — gives no example prompt text in-caption, a comparatively thinner delivery
  than the account's strongest top performer).
- Specificity: MED — lower than Videos 1-2's HIGH bar, closer to Video 3's breadth-over-depth register but
  without Video 3's named concrete per-item examples.

#### 5. Psychology scoring
- STEPPS: Practical Value present (a genuine time-saving resource) but arguably **thinner** than the top
  3 — no specific named prompt, no anecdote, no dollar-value or income framing, no contrarian-attention
  angle. Social Currency: weak-MED — "I found a prompt library" is a milder insider-knowledge claim than
  "I found a way to get unlimited Claude Code for free" or "everyone's missing Google's tools."
- Primary emotion + arousal: mild interest, LOWER arousal than the top 3's excitement/relief/FOMO range —
  `[INFERRED]` this is the most plausible content-level (as opposed to distribution-level) differentiator
  identified in this account's sample.
- Identity-signaling share motive: present but weaker — a prompt library is a generically useful resource
  without a strong "I'm ahead of the curve" framing attached.
- Save/send trigger: MED-HIGH in principle (a prompt library is inherently save-worthy), but the caption
  gives less reason to act *immediately* than the top 3's urgency-coded framings (rate-limit relief,
  income potential, contrarian FOMO).

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'PROMPT'" — identical mechanic to the top 3, content-backed.
- Comment-bait mechanics: comment-to-like ratio ~125% (1,489/1,192) — the **highest relative comment
  intensity of any of the four videos**, meaning the funnel mechanic itself worked at least as well
  per-viewer as on the top 3; the shortfall is in total reach, not in converting the viewers it did reach.

#### 7. Replicability verdict
- TEMPLATE: identical to the top-3 template in every structural respect (front-loaded CTA, persona
  thumbnail, analogy hook, organized beat structure, comment-gated close).
- Commodity vs. unfair advantage: N/A — this flop demonstrates the account's own template executed
  faithfully; nothing in the format execution explains the underperformance.
- Difficulty for Tangent: same as the top 3 — the format itself is not the limiting factor here.

#### 8. Why it lost — analyst synthesis, explicit delta vs. the top 3
Unlike Kallaway's flop (which shared its winning sibling's template AND still under-performed on raw
reach), **this flop's per-viewer engagement quality is fully comparable to — and on comment-rate, better
than — Saraev's own top 3**, which strongly suggests the shortfall here is a **reach/distribution problem,
not a content-quality problem**. Three non-exclusive contributing factors: (1) **Recency** — posted the
day before measurement, plausibly still mid-"audition" (§1.1.3) with its final view count unsettled — the
single largest confound, logged explicitly rather than glossed over; (2) **Content thinness relative to
the account's strongest work** — no verbatim prompt, no dollar-value framing, no contrarian-attention
angle, no specific recurring-pain-point trigger the way Video 1's rate-limit hack has — a real but modest
content-level gap; (3) **Topic novelty/timing** — a general-purpose prompt library lacks the topical
urgency of "OmniRoute just dropped" or "Google quietly shipped 10 tools," both of which carry an implicit
"this is new, act now" signal that a stable, ongoing resource (a prompt library) cannot replicate. Given
the comment-rate evidence, this dossier's confidence-weighted read is that (1) and (3) are more load-
bearing than (2).

#### Sources
- instagram.com/reel/DbLpxfKPKoN (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/nick_saraev.md

---

## Saraev: mini top-vs-flop delta

| Dimension | Top 3 | Flop | Delta |
|---|---|---|---|
| Packaging template | Selfie + tool-logo constellation + bold red/white 2-line caption | **Identical template** | No differentiation — confirms format is a constant for this account too |
| CTA structure | Front-loaded comment-keyword, first caption line | Same | No differentiation |
| Like-rate | 3.38%-3.54% | 2.70% | Modest gap, not dramatic |
| Comment-rate | 1.03%-2.87% | **3.37% (highest of all 4)** | Flop actually converts BEST per-viewer |
| Specificity/depth | HIGH (Videos 1-2 include verbatim prompts/steps) | MED (no verbatim prompt) | Real but modest content-level gap |
| Trigger strength | Strong recurring pain point (Video 1) or explicit contrarian-FOMO (Video 3) | Generic "useful resource," no urgency hook | Most plausible content-level differentiator |
| Recency confound | Videos 1,2 posted 1-7 days before measurement; Video 3 posted ~7 months before | Posted 1 day before measurement | Flop's low view count may partly reflect insufficient elapsed time, not a ceiling |

**One-paragraph verdict:** Unlike Kallaway, Saraev's flop-vs-top delta is NOT explained by an engagement-
rate anomaly (no evidence of paid boosting anywhere in this account's sample) — the flop's engagement
quality is genuinely comparable to the top 3. The likeliest explanation is a combination of insufficient
elapsed time (posted one day before measurement) and a real but modest content-level gap: the flop lacks
the strong recurring-pain-point trigger or explicit contrarian-FOMO framing that anchors the top 3's hooks,
running instead on a generically-useful-but-un-urgent premise.

## Saraev: mini content-architecture

`[INFERRED]` from the 4 analyzed videos plus the wider pattern already flagged in ig_harvest/nick_saraev.md
(a "comment KEYWORD" format used on nearly every reel in the 48-tile sample, top and flop alike):

1. **Single-tool arbitrage/hack** (Video 1: OmniRoute) — solve one specific, recurring, named pain point
   with one specific free tool; front-loaded CTA; analogy-driven explanation. The account's highest-
   converting sub-format by both views and engagement rate in this sample.
2. **Multi-tool workflow synthesis** (Video 2: Claude Code + Stitch) — combine 2+ tools into one coherent,
   step-by-step, income-framed workflow, including verbatim copy-paste prompt text. The account's most
   information-dense/reference-value sub-format.
3. **Contrarian tool-roundup listicle** (Video 3: Google's free tools) — "everyone's looking at X, Y is
   quietly better," 5 of N tools detailed, rest gated. The account's breadth-over-depth sub-format,
   leaning hardest on Social Currency.
4. **Generic resource-discovery** (Video 4/flop: YouMind prompt library) — same shell (selfie thumbnail,
   comment-CTA, analogy hook) applied to a lower-urgency, non-time-sensitive resource; the weakest-
   performing of the four sub-formats in this sample, though not by an engagement-quality margin.

**What sustains the account:** the comment-keyword-to-DM funnel is the load-bearing mechanical constant
across literally every reel in the account's grid (confirmed in ig_harvest/nick_saraev.md's own pattern
note) — this account has industrialized a single funnel mechanic and varies only the tool/topic/urgency
layer on top of it, which plausibly explains its unusually tight variance (12.8x top/median, the tightest
of the three accounts in this dossier) relative to Kallaway's 419x: a consistent mechanic run at high
volume produces consistent-but-rarely-explosive results, rather than occasional massive spikes.

## Saraev vs. Nate Herk — YT-formula contrast (per yt_nateherk.md §C, read for this dossier)

Nate Herk's #1 YouTube Short (1.3M views, 52.7x his channel median) wins, per that dossier's own synthesis,
by pairing "an instantly-legible, universally-relatable premise with a vivid, verifiable payoff... narrated
with specific tool names" — his top performers are built around universal, low-jargon tasks (invoices,
calendars, personal assistants) with a demonstrated real-world result (a sent email read aloud, an exact
dollar figure), and his dossier explicitly found that **topic/payoff selection, not format, is the
dominant performance lever** on his channel (a near-identical-format video, posted 3 days after his #1,
returned only 0.29x the channel median because it picked an abstract B2B topic with a flat payoff).

Saraev's Instagram formula both resembles and diverges from this:
- **Resemblance**: both creators rely on named tools, concrete demonstrated mechanics, and a legible
  premise a cold viewer can grasp in the hook's first line.
- **Divergence 1 — audience specificity**: Nate Herk optimizes for maximal universality (invoices,
  calendars — tasks any small-business viewer recognizes); Saraev optimizes for **depth within a
  narrower, already-self-selected technical audience** (people who already use or want to use Claude
  Code specifically) — trading Nate's broad-relatability lever for Saraev's Triggers-pillar lever
  (a specific, recurring, felt pain point that re-activates the content every time it recurs).
- **Divergence 2 — CTA mechanics**: Nate Herk's top videos point to "the full video on my channel" (an
  on-platform, same-creator funnel); Saraev's every video (top and flop alike) runs an explicit comment-
  keyword-to-DM funnel — a heavier, more industrialized lead-capture mechanic baked into literally every
  post, not reserved for occasional hits.
- **Divergence 3 — cross-platform structure**: Nate Herk's Shorts appear to be his primary discovery
  surface with long-form as the deeper funnel destination (per that dossier's funnel map). Saraev
  **bifurcates by platform entirely**: IG Reels = tool-hack discovery bait (this dossier's subject); YT
  Shorts = a *different* content pillar entirely (business-mindset/nurture clips at far lower views); YT
  long-form = the deep-tutorial destination (confirmed cross-post theme: "How to Use Claude Code for FREE
  (2026)," 189K views). **Neither creator simply reposts the same Short across platforms** — both
  deliberately differentiate format by platform, but Saraev's differentiation is more extreme (two visibly
  different Instagram-vs-YouTube-Shorts content strategies under one persona).
- **On the central "is Claude-tool-arbitrage a reliable outlier engine" question**: the evidence across
  both platforms (IG: 2 of top 5 explicitly "free Claude Code" branded per ig_harvest/nick_saraev.md's own
  pattern note; YT: a dedicated "How to Use Claude Code for FREE (2026)" long-form video) supports **yes,
  specifically for Saraev's audience** — but the mechanism, per this dossier's STEPPS analysis, is not
  "Claude Code" as a magic keyword; it's that Claude Code usage limits are a **frequent, concrete,
  audience-wide recurring frustration**, which is the Triggers-pillar condition Nate Herk's universal-task
  content satisfies via breadth (everyone has invoices) and Saraev's content satisfies via depth-within-
  niche (everyone in HIS audience hits this specific wall). The transferable lesson is the underlying
  mechanism (recurring, specific, audience-matched pain point + a verifiable fix), not the literal phrase
  "free Claude Code."

---

# ACCOUNT 3: Ankit Arora (@ai_ankitarora)

## Account header
- 735K followers, 391 posts `[OBSERVED, ig_harvest/ai_ankitarora.md, 2026-07-25]`. Bio: "AI can't replace
  you if you follow this page." Two accounts exist under this creator's name; @ai_ankitarora (735K) is
  treated as primary per the harvest file's disambiguation call (5.7x the follower count of @aiwithankit,
  130K) `[OBSERVED, ig_harvest/ai_ankitarora.md disambiguation note]`.
- **Cross-platform check** `[OBSERVED via yt-dlp + WebSearch, 2026-07-25]`: a YouTube channel
  `@aiankitarora` (note: handle differs slightly from the IG handle, no underscore) is active, running
  both long-form tutorials/reviews ("I Tried 1000+ AI Tools," "10 Claude AI Hacks That Will Make You
  Unreplaceable in 2026") and a Shorts tab. **Views on YouTube are dramatically lower** than the IG
  account's peak — long-form videos sampled ran 498-23,000 views (one outlier at 794K, "11 Free AI Apps to
  Simplify Your Life in 2024" — an older video, not part of the March 2026 IG spike window), and Shorts
  ran 1,200-17,000 views `[OBSERVED via yt-dlp flat-playlist]`. **No cross-post match was found** for
  either of the two March 2026 IG mega-hits (the "Claude CoWorks podcast automation" reel or "Your AI is
  lying to you" reel) among the YouTube titles sampled — logged as a **negative finding / DATA GAP**, not
  fabricated: searched, no match located, so this dossier proceeds on IG-caption-only evidence for those
  two videos rather than claiming a transcript that doesn't exist. **Confirms Instagram, not YouTube, is
  this creator's primary viral-distribution surface** — the same structural pattern seen with Kallaway.
- Median reel views 65.7K, top raw reel 5.5M, median/follower ratio 8.9% (2nd-lowest of the 22-account
  study, ahead of only godofprompt/danmartell/sabrina_ramonov/chrisdonnellyofficial/handlytech), top/median
  ratio ~83.7x `[OBSERVED, ig_harvest/ai_ankitarora.md]`.

---

### VIDEO 1 (TOP #1): "Claude CoWorks — fully automated podcast agency"

#### 0. Identity & stats
- URL: instagram.com/reel/DV_FSjBCB9O. Posted **Mar 17, 2026** `[OBSERVED via yt-dlp, HIGH]`. Duration:
  DATA GAP. Pin status: **CONFIRMED NOT PINNED** — dated consistently with its chronological grid
  neighbors `[OBSERVED, ig_harvest/ai_ankitarora.md pinned-flag note]`.
- Views: **5.5M** `[OBSERVED, harvest]`. Likes: **153,511**. Comments: **33,707** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 154K/34K, no discrepancy]`. Like-rate ~2.79%, comment-rate
  ~0.613% — solidly organic-consistent engagement, no anomaly.
- Rank: **#1 of 48**, and the account's all-time peak. 5.5M / 65.7K median ≈ 83.7x — the account's single
  largest multiple, one of the largest in the wider 22-account study.

#### 1. Packaging
- Caption opens: "Comment 'prompt' and I'll send you this entire system" `[OBSERVED]` — CTA-first, similar
  structural choice to Saraev's account, though the payoff (what "system") is not yet named in the first
  line.
- Cover-thumbnail `[OBSERVED]`: a **stylized, high-production fashion-editorial portrait** — Ankit Arora in
  a black tuxedo and bow tie against a solid red backdrop, holding an ornate jeweled prop pistol beside his
  face, with bold all-caps white text "COMMENT / PROMPT" stacked above him. This is categorically different
  packaging from either Kallaway (branded news-graphics template) or Saraev (casual selfie + tool logos) —
  a **magazine-cover/movie-poster aesthetic** with elaborate props and styling, pure visual spectacle
  disconnected from any literal representation of the video's software-automation content.
  `[INFERRED, not confirmed]`: the polish and stylization level is consistent with either a professional
  photoshoot or AI-image-generation, and this dossier could not determine which from the thumbnail alone —
  logged as an open question rather than asserted either way, though the irony of an "AI can't replace you"
  bio-line creator potentially using AI-generated self-portraiture is worth flagging as a live possibility.
- Curiosity gap: high — the striking, incongruous visual (jeweled gun, tuxedo) has no obvious connection to
  "podcast automation," creating a pure pattern-interrupt (§2.1.2) independent of any informational gap.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption, no cross-post transcript located — see account-header DATA
  GAP note]`: "Comment 'prompt' and I'll send you this entire system," followed immediately by: "I built a
  fully automated podcast production agency using just one Claude CoWorks prompt."
- Hook taxonomy: **result-first / bold claim** — states a finished, impressive outcome (a full automated
  agency) attributed to a single input (one prompt), maximizing the "how is that possible with just ONE
  prompt" curiosity gap.
- What the viewer sees first (per thumbnail): pure visual spectacle (stylized portrait), disconnected from
  the software content — meaning the *packaging* hooks on spectacle/pattern-interrupt while the *caption*
  hooks on informational curiosity; two different hook mechanisms stacked on top of each other.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption; no timestamp data available — DATA GAP, no transcript/video obtained]`:
  CTA hook → bold claim (one-prompt automated agency) → scope list ("Guest research, outreach, scheduling,
  interview prep — everything handled by AI") → generalization/replicability claim ("plug in any client's
  YouTube link, and run their entire podcast backend") → philosophical close ("Stop trading time for money.
  Start selling automation.").
- One-idea-per-video: yes — "one Claude CoWorks prompt can run an entire client-service backend." The
  caption is notably SHORT relative to Kallaway's and Saraev's dense multi-beat captions — this is a
  terser, punchier structure that leans more on the video content itself (unobserved) than on caption
  exposition.
- Open loop: "what does this one prompt actually contain, and does it really work end-to-end?" — opened by
  the hook, not resolved in the caption (deliberately gated behind the comment CTA) — a stronger gate than
  Saraev's typical "give most value free, gate a bonus" pattern.
- Pacing/loop design: DATA GAP — caption brevity gives little signal on in-video structure without a
  transcript.

#### 4. Value proposition
- Walk-away value: a business-model idea (sell podcast-production-as-a-service using AI automation) plus
  an implied, gated exact prompt.
- Practical value class: **aspiration/business-opportunity** (primary, "stop trading time for money") +
  **copyable workflow** (secondary, gated behind the CTA rather than shown).
- Specificity: LOW-MED in the caption itself (no prompt text shown, unlike Saraev's Video 2) — the caption
  sells the *outcome* and gates the *mechanism* almost entirely, a more aggressive value-gating strategy
  than either other account's top performers.

#### 5. Psychology scoring
- STEPPS: **Social Currency** dominant — "I automated an entire service business with one prompt" is a
  maximal entrepreneurial-flex claim (§2.2). **Emotion**: excitement/aspiration, high-arousal per §2.3.
  **Practical Value**: present but gated, weaker in-caption than Saraev's equivalent content. **Story**:
  a mild personal narrative arc ("I built..."), first-person builder framing.
- Primary emotion + arousal: excitement/ambition, high arousal.
- Identity-signaling share motive: "I know how to turn AI into a sellable service business" — a strong,
  aspirational entrepreneur-identity signal, likely resonant with Ankit's business/AI-tools-for-income-
  oriented audience.
- Save/send trigger: MED — the *idea* (podcast-automation-as-a-service) is send-worthy to a specific
  addressee (someone running or wanting to run an agency), though the caption alone offers less standalone
  reference value than Saraev's step-by-step equivalents.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'prompt'" — content-adjacent but more heavily gated than this dossier's other
  top performers (the caption describes the outcome but withholds the mechanism almost entirely, closer to
  the boundary of, but not crossing into, Instagram's bare-engagement-bait policy per §1.3.2, since a
  genuine described outcome/business-idea is present, not a contentless "comment YES").
- Funnel position: top-of-funnel discovery bait converting to a DM'd prompt — plausibly a soft on-ramp to
  whatever product/service Ankit sells, though no explicit link/offer is named in this caption.

#### 7. Replicability verdict
- TEMPLATE: (1) open with a bold, single-input-to-big-outcome claim; (2) list the scope of what's
  automated in punchy fragments; (3) generalize to "any client" for replicability appeal; (4) close on a
  philosophical/identity reframe ("stop trading time for money"); (5) gate the actual mechanism behind a
  comment.
- Commodity vs. unfair advantage: the caption template is commodity; the unfair advantage (if the video
  content matches the claim) would be having actually built and tested a working Claude CoWorks prompt
  system — an execution/proof asset this dossier could not verify without the video/prompt itself (DATA
  GAP).
- Difficulty for Tangent: MED-HIGH — requires both a working automation build AND the stylized visual
  production values seen in the thumbnail, a higher production bar than either Kallaway's or Saraev's
  formats.

#### 8. Why it won — analyst synthesis
The load-bearing factor is a **stacked double-hook**: a pure visual pattern-interrupt (the stylized
tuxedo/jeweled-gun portrait, disconnected from and unexplained by the content) captures attention before
any informational content is processed, then the caption's bold "one prompt, entire automated agency"
claim supplies a strong Social-Currency/aspiration payoff for a business-and-AI-tools audience. This
landed within a tight 2-day window alongside Video 2 (below) — both released Mar 15-17, 2026 — which is
itself a contributing factor per §8 of Video 2's analysis: mutual audience cross-feed between two
near-simultaneous hits from the same account plausibly amplified both beyond what either would have
achieved in isolation, though this dossier cannot fully separate that effect from independent topic
strength for each video (DATA GAP: no view-velocity/timestamp-level data available).

#### Sources
- instagram.com/reel/DV_FSjBCB9O (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/ai_ankitarora.md

---

### VIDEO 2 (TOP #2): "Your AI is lying to you"

#### 0. Identity & stats
- URL: instagram.com/reel/DV707PciHfD. Posted **Mar 15-16, 2026** `[OBSERVED via yt-dlp: 20260316; harvest
  file's independent pull recorded Mar 15, 2026 — a one-day discrepancy, likely a timezone/rounding
  difference between pull methods, not material to this dossier's analysis; flagged for completeness]`.
  Duration: DATA GAP.
- Views: **1M** `[OBSERVED, harvest]`. Likes: **33,634**. Comments: **86,205** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 34K/86K]`. Like-rate ~3.36%, **comment-rate ~8.62% — comments
  outnumber likes by a 2.56x ratio, the single most extreme comment-over-like skew in this entire
  12-video dossier**, across all three accounts.
- Rank: #2 of 48, posted **2 days before** Video 1 (the account's all-time #1) — the two hits are tightly
  clustered in time.

#### 1. Packaging
- Caption (in full): "Comment 'PROMPT' and I'll send you the link. Your AI is lying to you. Not because
  it's broken — because it's trained to agree with everything you say. Here's how I fixed mine."
  `[OBSERVED]` — notably terse, only 3 sentences of substantive content.
- Cover-thumbnail `[OBSERVED]`: same stylized-portrait family as Video 1 — Ankit in a black blazer and
  large amber/orange sunglasses against a plain light-grey backdrop, a slightly tilted-down camera angle
  (looking up at him), bold stacked text "MASTER / PROMPT." Same fashion-editorial visual register as
  Video 1, different specific styling.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: **"Your AI is lying to you."**
- Hook taxonomy: **bold claim / negative-warning hybrid** — a direct, provocative accusation aimed at the
  viewer's own AI usage, immediately personal ("YOUR AI") rather than abstract, maximizing self-relevance
  from word one.
- What the viewer sees first (per thumbnail): the stylized sunglasses portrait — again a spectacle-driven
  visual hook layered independently on top of the provocative caption hook.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption; no transcript — DATA GAP]`: provocative accusation → reassurance/
  reframe ("not because it's broken") → mechanism/diagnosis ("trained to agree with everything you say" —
  i.e., sycophancy) → personal-fix tease ("here's how I fixed mine") → CTA (comment "PROMPT" for the link).
  This is the **shortest, most compressed caption of any video in this entire dossier** — four short
  sentences carrying the full hook-diagnosis-tease-CTA arc.
- One-idea-per-video: yes — "your AI agrees with you too much (sycophancy), and there's a prompt fix."
- Open loop: "how did he fix it?" opened at "here's how I fixed mine," deliberately left open/gated at the
  CTA rather than resolved in-caption — the strongest value-gating of any top performer in this dossier
  (even more aggressive than Video 1's gating).
- Pacing/structure: DATA GAP, no transcript.

#### 4. Value proposition
- Walk-away value: a diagnosis/framing (AI sycophancy as a named, relatable problem) plus a gated fix.
- Practical value class: **practical value/problem-awareness** (primary, genuinely useful framing even
  before the gated fix) + tool discovery (the gated prompt).
- Specificity: LOW in-caption (no detail on the actual fix mechanism) — this is a pure curiosity-gap-first,
  specificity-last structure, the opposite extreme from Saraev's give-everything-free-then-gate-a-bonus
  approach.

#### 5. Psychology scoring
- STEPPS: **Emotion** is unusually load-bearing here — the accusatory hook ("your AI is lying to you")
  triggers a mild anxiety/concern spike (a AI-trust problem the viewer may not have known they had) before
  pivoting to reassurance, a deliberate emotional arc (concern → relief-via-solution) that is distinct from
  every other video in this dossier's straightforwardly positive-arousal hooks. Per §2.3, anxiety is a
  high-arousal, share-favorable emotion. **Practical Value**: the sycophancy framing itself (independent of
  the gated fix) is genuinely useful, naming a real, under-discussed AI-behavior problem. **Social
  Currency**: strong — "I noticed and fixed a subtle AI trust problem most people haven't clocked" is a
  sophisticated, ahead-of-the-curve claim.
- Primary emotion + arousal: **anxiety/concern → relief**, high arousal — the most emotionally-engineered
  hook of any video in this dossier.
- Identity-signaling share motive: "I understand a subtle AI failure mode most casual users miss" —
  strong technical-sophistication signal.
- Save/send trigger: HIGH in concept (a real, common frustration point — AI over-agreeing — has an
  obvious "send to a friend who complains their AI just tells them what they want to hear" moment), though
  weakened by the caption's total lack of specificity about the actual fix.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'PROMPT' and I'll send you the link" — the MOST heavily-gated of this account's
  top performers (essentially zero standalone value delivered in-caption beyond the diagnosis itself).
- Comment-bait mechanics: **comment count (86,205) is the single largest raw engagement number in this
  entire 12-video dossier across all three accounts** — the comment-to-like ratio (256%) is extreme and
  worth flagging explicitly as the strongest evidence in this dossier that a comment-CTA, when paired with
  a maximally curiosity-gapped, personally-provocative hook, can become the dominant distribution mechanic
  in its own right (consistent with §1.1.2's sends/comments-weighted-higher-than-likes principle) —
  arguably more consistent with genuine viral comment-chain dynamics (people replying to, arguing with, or
  tagging friends under the provocative claim) than with the CTA alone, though this dossier could not
  directly inspect the comment thread content to confirm — DATA GAP, flagged not fabricated.
- Funnel position: aggressive top-of-funnel lead capture.

#### 7. Replicability verdict
- TEMPLATE: (1) open with a short, personal, provocative accusation naming a problem the viewer likely
  didn't know they had; (2) immediately reassure/reframe to avoid alarmism; (3) name the mechanism in one
  line; (4) tease a personal fix without any detail; (5) gate everything behind one comment.
- Commodity vs. unfair advantage: the hook structure is highly replicable; the risk is that maximal
  gating (near-zero in-caption value) trades some Practical-Value/Save-worthiness for pure curiosity-gap
  intensity — a deliberate trade this account made successfully here but which (per §1.3.2) sits closer to
  the engagement-bait boundary than this dossier's other analyzed top performers.
- Difficulty for Tangent: LOW for the caption template; MED for the underlying claim to hold up as
  genuinely valuable rather than clickbait once a viewer follows through on the CTA (unverifiable from
  available evidence — DATA GAP).

#### 8. Why it won — analyst synthesis
This video's win is best explained by an unusually potent **emotion-first hook** (personal accusation →
reassurance arc, engineered anxiety-then-relief) combined with the account's heaviest value-gating,
producing the dossier's most extreme comment-to-like skew — a strong signal that curiosity/provocation,
not delivered practical value, was the primary conversion driver. Timing is a real contributing factor:
this video posted 2 days before the account's all-time #1 (Video 1), and both share the same stylized-
portrait packaging family and comment-gate mechanic, making mutual audience cross-feed between the two a
plausible amplifier for both — this dossier flags but cannot fully isolate that timing effect from each
video's independent hook strength (DATA GAP: no daily view-velocity data available).

#### Sources
- instagram.com/reel/DV707PciHfD (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/ai_ankitarora.md

---

### VIDEO 3 (TOP #3): "Claude Computer Use announcement"

#### 0. Identity & stats
- URL: instagram.com/reel/DWRkb-MiErx. Posted **Mar 24, 2026** `[OBSERVED via yt-dlp, HIGH]` — 7-9 days
  after Videos 1-2, the account's "hot streak" tail end. Duration: DATA GAP.
- Views: **793K** `[OBSERVED, harvest]`. Likes: **31,289**. Comments: **421** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 31K/421]`. Like-rate ~3.95% (the **highest like-rate of the
  account's top 3**), comment-rate a mere ~0.053% (by far the lowest of the top 3, expected given the
  CTA is not comment-based — see below).
- Rank: #3 of 48. 793K / 65.7K ≈ 12.1x.

#### 1. Packaging
- Caption opens: "Share this reel!!!" `[OBSERVED]` — a **share-CTA, not a comment-CTA**, the only video in
  this account's top 3 (and one of only two across this entire dossier, alongside none in Kallaway's or
  Saraev's samples) built around Instagram's own highest-weighted cold-reach signal (§1.1.1-1.1.2: sends/
  shares outweigh likes for reaching unconnected audiences) rather than a comment-to-DM funnel.
- Cover-thumbnail `[OBSERVED]`: same stylized-portrait family — Ankit in an ornate, bejeweled black-and-
  pink couture jacket with elaborate drop earrings, a royal/high-fashion aesthetic, against a solid blue
  backdrop, bold stacked text "COMPUTER / USE." The most elaborate/expensive-looking costuming of the
  account's three top thumbnails.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED via caption]`: "Claude just dropped Computer Use — and it's a game
  changer."
- Hook taxonomy: **bold claim / news-first** — states a factual product-launch claim with an intensifier
  ("game changer"), similar register to Kallaway's news-reaction hooks but on a different platform-CTA
  strategy (share vs. comment).
- What the viewer sees first (per thumbnail): the elaborate couture portrait, once again a pure-spectacle
  visual hook independent of the caption's news content.

#### 3. Structure & retention engineering
- Beat map `[OBSERVED via caption]`: bold-claim hook → capability list ("control your entire computer like
  a real human. Move the mouse, open apps, type, fill spreadsheets, browse the web") → named companion
  feature (Dispatch: "text Claude a task from your phone… and it'll sit at your Mac and get it done while
  you're away") → caveat/disclaimer ("Currently available on macOS only. Windows coming soon") → save-CTA
  ("Save this for later. You'll need it") → share-CTA (repeated from the opening line).
- One-idea-per-video: yes — "Claude's new Computer Use feature can operate your whole computer
  autonomously." Structurally similar to Kallaway's product-update format (capability list + concrete
  use-case) but delivered in this account's terser caption style.
- Open loop: minimal — this is closer to a straightforward news-announcement structure than a curiosity-
  gap-driven one, consistent with its lower comment-rate (less "argue in the comments" provocation, more
  "here's what happened" reporting).

#### 4. Value proposition
- Walk-away value: awareness of a specific, named new AI capability (autonomous computer control) plus a
  companion feature (remote task dispatch).
- Practical value class: **news/tool discovery**, MED specificity (names exact capabilities and the
  platform limitation, a genuinely useful caveat many announcement-reaction videos omit).
- Specificity: MED — more specific and more balanced (includes the macOS-only caveat) than either of the
  account's other two top performers, which is notable given it under-performed both in raw views.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (a genuine capability update with a real caveat, unusually complete/
  honest framing). **Triggers**: MED — "your computer doing tasks for you" is a recurring aspiration for
  this AI-tools audience. **Social Currency**: present via early-adopter framing ("just dropped") but
  milder than Videos 1-2's more provocative/aspirational hooks.
- Primary emotion + arousal: interest/mild-awe, MED-high arousal — a calmer register than Video 2's
  engineered anxiety-relief arc.
- Identity-signaling share motive: "I'm tracking the newest Claude capabilities as they ship" —
  plugged-in framing, reinforced by the explicit "Share this reel!!!" ask (asking directly for the
  highest-value signal per platform mechanics, per §1.1.1-1.1.2).
- Save/send trigger: explicitly invoked in-caption ("Save this for later. You'll need it") — the only
  video in this account's top 3 to directly name the save action, aligning tightly with §2.7's practical-
  value/saveability principle.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Share this reel!!!" (opening) + "Save this for later" (closing) — **no comment-keyword
  funnel at all**, the only top performer in this account's sample without one.
- Comment-bait mechanics: near-zero (421 comments on 793K views, 0.053%) — expected given no comment-CTA
  is present; this is NOT an engagement-quality problem, it's the natural consequence of asking for a
  different action (share/save) instead.
- Funnel position: this reads as **pure brand/credibility content** (reporting a real Anthropic product
  launch) rather than a lead-capture funnel — no DM/link gate at all.

#### 7. Replicability verdict
- TEMPLATE: (1) lead with a bold product-launch claim; (2) list concrete capabilities in short beats; (3)
  name a companion feature; (4) **include an honest limitation/caveat** (a differentiator most
  announcement-reaction content skips); (5) ask directly for shares and saves rather than comments.
- Commodity vs. unfair advantage: highly replicable — this is closest to pure news-reaction journalism of
  the three top performers, requiring speed-to-post more than any unique asset.
- Difficulty for Tangent: LOW — the format and honesty-caveat device are both straightforwardly learnable.

#### 8. Why it under-performed its siblings (though still a genuine top-3 hit) — analyst synthesis
This is the account's most textbook-optimal CTA choice per the virality-science evidence base (asking for
shares/saves, the platform's own highest-weighted signals per §1.1.1-1.1.2) and arguably its most complete,
honest content (the only one of the three to include a real limitation caveat) — yet it produced the
LOWEST view count of the top 3 (793K vs. 1M and 5.5M). The most plausible explanation `[INFERRED]`: a bare
"share this" ask, without a specific reason tied to an addressable "send to ___" moment (§2.7's
addressability marker), may be a structurally weaker share-trigger than a curiosity-gapped, personally-
provocative comment-CTA hook (Video 2) or a bold single-input business-transformation claim (Video 1) —
consistent with this dossier's broader finding that specific, high-stakes, personally-relevant hooks
out-perform even mechanically "correct" CTA choices. Secondary factor: posted 7-9 days after the Mar 15-17
cluster, outside the tight mutual-cross-feed window that plausibly amplified Videos 1-2.

#### Sources
- instagram.com/reel/DWRkb-MiErx (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/ai_ankitarora.md

---

### VIDEO 4 (FLOP): generic "comment CLAUDE" reel

#### 0. Identity & stats
- URL: instagram.com/reel/DZ-c-kEg5WT. Posted **Jun 24, 2026** `[OBSERVED via yt-dlp, HIGH]` — 3 months
  after the March hot streak. Duration: DATA GAP.
- Views: **24.5K** `[OBSERVED, harvest]`. Likes: **384**. Comments: **52** `[OBSERVED via yt-dlp,
  2026-07-25, closely matches harvest's 384/52 exactly]`. Like-rate ~1.57%, comment-rate ~0.212% — the
  LOWEST like-rate of any video analyzed in this account's sample (below even the account's typical
  organic range implied by the top 3's 2.79-3.95%).
- Rank: near-bottom of the 48-tile sample. 24.5K / 65.7K ≈ 0.37x.

#### 1. Packaging
- Caption (in full) `[OBSERVED]`: **"Comment 'CLAUDE' and I'll send you the link"** — this is the ENTIRE
  caption. No claim, no context, no diagnosis, no capability list — nothing beyond the bare CTA. This is
  the textbook example Instagram's own Recommendation Guidelines name as prohibited engagement bait
  (§1.3.2: "content that users broadly tell us they dislike, including... engagement bait"), though this
  dossier notes the video itself (unobserved) may contain standalone value even if the caption does not —
  Instagram's policy language and this study's marker (§1.3.2) test the *content*, and the caption is the
  only artifact available here (DATA GAP on the video itself).
- Cover-thumbnail `[OBSERVED]`: a **dramatic departure from the stylized-portrait family** — a casual,
  plainly-lit webcam-style clip of Ankit in a black shirt at a desk mic, mid-gesture, with a burned-in
  caption overlay reading **"that one AI Prompt bro on my Feed"** — a self-deprecating, meta-humor framing
  that pokes fun at the "generic AI content creator" archetype. Production values (lighting, styling,
  composition) are visibly lower than the top 3's magazine-cover aesthetic — no costume, no prop, no
  dramatic lighting or camera angle.

#### 2. Hook (0-3s)
- Verbatim opening line `[OBSERVED, thumbnail burned-in text — the only text evidence available, since the
  caption carries no content]`: "that one AI Prompt bro on my Feed."
- Hook taxonomy: **self-aware/meta-humor**, a distinct taxonomy not seen in this account's top 3 or
  anywhere else in this dossier — rather than making a claim about the world, it makes a claim about the
  creator's own content-creator archetype, addressed with irony/self-deprecation.
- What the viewer sees first: a plain, low-production talking-head clip — the opposite visual register
  from the top 3's high-fashion spectacle thumbnails.

#### 3. Structure & retention engineering
- Beat map: **DATA GAP** — with no caption content and no located transcript/cross-post, this dossier
  cannot reconstruct a beat map beyond the single burned-in thumbnail line. This is explicitly logged
  as a data gap per QC_PROTOCOL.md §3 rather than invented.
- One-idea-per-video: cannot be assessed beyond the thumbnail's meta-humor framing — DATA GAP.
- Open loop/pacing: DATA GAP.

#### 4. Value proposition
- Walk-away value: cannot be assessed from available evidence — the caption offers nothing, and the
  thumbnail's self-deprecating framing does not itself convey the underlying "CLAUDE"-gated content's
  value. DATA GAP.
- Practical value class: unknown from available evidence (DATA GAP) — the CTA implies SOME gated resource
  exists ("I'll send you the link"), but its nature is entirely unstated.
- Specificity: effectively zero in all observable artifacts — the starkest specificity failure of any
  video in this entire dossier.

#### 5. Psychology scoring
- STEPPS: essentially unscoreable from available evidence beyond the thumbnail's mild Social-Currency-via-
  self-awareness angle ("I know I'm 'that AI prompt guy' and I'm in on the joke") — DATA GAP on the
  video's actual content prevents a full STEPPS pass.
- Primary emotion + arousal: `[INFERRED, LOW confidence]` mild amusement (self-deprecating humor), if
  anything — but this is inference from a single burned-in caption line, not observation of the full video.
- Identity-signaling/save-send: cannot be assessed. DATA GAP.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Comment 'CLAUDE' and I'll send you the link" — bare engagement bait per Instagram's own
  named policy example (§1.3.2), with zero standalone content value in the only artifact available (the
  caption).
- Comment-bait mechanics: comment-to-like ratio ~13.5% (52/384) — notably LOWER than every other video in
  this account's sample (Videos 1-3 ran 0.053%-256%, admittedly a huge range, but this flop's absolute
  comment count (52) is the lowest of any video analyzed across all three accounts in this dossier).

#### 7. Replicability verdict
- TEMPLATE: cannot responsibly be extracted — a bare CTA caption is definitionally not a template worth
  replicating; this post-mortem is included precisely because it is the account's clearest instance of the
  practice §1.3.2 warns against.
- Commodity vs. unfair advantage: N/A.
- Difficulty for Tangent: N/A — this format should not be replicated; the QC protocol's evidence base
  (§1.3.2) explicitly flags this exact caption pattern as platform-penalized.

#### 8. Why it lost — analyst synthesis, explicit delta vs. the top 3
This is the starkest and simplest delta in this entire dossier: **the top 3 all pair a high-production,
spectacle-driven stylized-portrait thumbnail with a substantive caption (a bold claim, a diagnosis, or a
capability list); this flop pairs a low-production, plain-selfie thumbnail with a caption that is nothing
but a bare CTA** — a compounded packaging-AND-content gap, not a single-variable failure. Unlike Saraev's
flop (matched packaging, real content gap only) or Kallaway's flop (matched packaging AND content, gap
unexplained by either), **this is the one flop in the dossier where both packaging and caption-content
visibly regressed from the account's own established winning template simultaneously** — the clearest
"this creator simply phoned this one in" case among all 12 videos analyzed. It is also, not coincidentally,
posted 3 months after the account's March hot streak, consistent with the broader spike-and-decay pattern
covered in the account-level synthesis below.

#### Sources
- instagram.com/reel/DZ-c-kEg5WT (`[OBSERVED]` via yt-dlp, 2026-07-25)
- ig_harvest/ai_ankitarora.md

---

## Ankit Arora: mini top-vs-flop delta

| Dimension | Top 3 | Flop | Delta |
|---|---|---|---|
| Thumbnail production | High-production stylized fashion-editorial portraits (tuxedo+gun, sunglasses, couture jacket) | Plain casual webcam-style selfie with self-deprecating meta caption | **Regressed** — the only account/flop pair in this dossier with a visible packaging-quality gap |
| Caption substance | Bold claim / diagnosis / capability list, 3-8 sentences each | **Zero content** — bare "Comment CLAUDE" CTA only | **Regressed** — matches Instagram's own named engagement-bait example |
| Like-rate | 2.79%-3.95% | 1.57% | Notably lower, though not a 100x-scale anomaly like Kallaway's |
| CTA type | Comment-keyword (2 of 3) or share/save (1 of 3) | Comment-keyword, content-free | Same mechanic family, but stripped of any supporting content |
| Timing | Mar 15-24, 2026 (tight cluster) | Jun 24, 2026 (3 months later, post-decay) | Consistent with account-level spike-and-decay pattern |

**One-paragraph verdict:** Unlike either Kallaway (matched packaging, engagement-rate anomaly explains the
gap) or Saraev (matched packaging, comparable engagement quality, reach/timing explains the gap), Ankit
Arora's flop shows a genuine, visible, compounded regression in both packaging production value and caption
substance relative to his own top 3 — the clearest case in this dossier of a flop that under-performed
because the creator simply invested less in it, not because of an external distribution anomaly or a subtle
content-depth gap.

## Ankit Arora: mini content-architecture

`[INFERRED]` from the 4 analyzed videos:

1. **High-production stylized-portrait spectacle + bold/diagnostic hook** (Videos 1-2: business-
   transformation claim, sycophancy diagnosis) — the account's peak-performing sub-format, pairing
   magazine-cover visual spectacle with either an aspirational business claim or an emotion-engineered
   personal-accusation hook, heavily comment-gated.
2. **Stylized-portrait + honest news-reaction** (Video 3: Computer Use announcement) — same visual
   production tier, but share/save-CTA instead of comment-gate, and a more complete/honest caption
   (including a real limitation caveat) — the account's most "correct-per-platform-mechanics" but
   lowest-reach top performer.
3. **Low-production, content-free CTA-only** (Video 4/flop) — a visible drop-off in both visual and
   caption investment, the account's weakest identified sub-format.

**What sustains/fails to sustain the account:** the March 2026 hot streak (Videos 1-2, two days apart, both
Claude/Anthropic-adjacent, both stylized-portrait-packaged) represents this account's ceiling; nothing in
the following four months (through the Jul 25, 2026 harvest date) matched it, and the identified flop
sits in that post-peak period with visibly reduced production investment — consistent with, though not
proof of, a causal link between investment level and the account's inability to repeat its peak.

## Ankit Arora: anatomy of spike-and-decay, and the Harper Carroll series-compounding contrast

**What the March 2026 hits were, concretely:** Video 1 (5.5M, Mar 17: a Claude CoWorks podcast-automation-
agency prompt, positioned as a business-transformation opportunity) and Video 2 (1M, Mar 15-16: an AI-
sycophancy diagnosis with a gated personal fix) landed **two days apart**, both riding the same visual-
packaging family (stylized portraiture) and the same comment-to-DM funnel mechanic, both substantively
about Claude/Anthropic's product ecosystem. Video 3 (793K, Mar 24, also Claude-adjacent — the Computer Use
launch) extends the cluster to **three of the account's top four sampled hits landing within a ten-day
window in March 2026**, all tied to the same general topic area (Claude/Anthropic capability news and
prompt-based automation) rather than to a personal, ongoing branded format.

**Why it didn't compound**, contrasted directly against Harper Carroll's series-driven pattern
(`ig_harvest/harpercarrollai.md`, read for this comparison): Harper Carroll's bio explicitly names a
**"Weekly explAIned episodes"** cadence — a numbered, recurring, appointment-viewing format — and her
sampled top performers include content **explicitly branded as an ongoing Anthropic partnership series**
("`@claudeai #ClaudePartner`" launch content, per that account's harvest detail-pull), backed by a
credentialed personal brand (Stanford/Meta background stated in her bio) that plausibly compounds trust and
recognition with each recurring installment — the mere-exposure (§2.4.2) and series-effects (§3.4.2)
mechanisms both predict growing, not merely repeating, returns from this structure. **Ankit Arora's March
cluster has no equivalent scaffolding**: none of the three March videos are numbered, titled as a series,
or branded as recurring — they are three topically-adjacent but administratively independent one-off posts
that happen to have landed in the same short window, most plausibly because **March 2026 was a genuinely
hot news cycle for Claude/Anthropic capability launches** (Computer Use, CoWorks, and general Claude Code
momentum all cluster in this window across MULTIPLE accounts in this wider 22-account study, not just
Ankit Arora's), i.e. this reads as **trend-surfing a real news cycle** (§3.3.3, §4's "velocity of trend
response" factor) rather than **format-ownership compounding** (§2.4.2, §3.4.2). Once the March news cycle
cooled, there was no recurring segment identity, no episode numbering, and no standing brand-partnership
relationship to sustain appointment-viewing behavior — consistent with the visible decay: by May 2026 even
a genuine top-5 reel (445K, per ig_harvest/ai_ankitarora.md) shows a markedly lower like-rate (~0.6%, per
that file) than the March hits (2.79%-3.95%), and by June-July 2026 the account's own flop and near-flop
tiles sit at 24-26K views with sub-2% like-rates — a real, multi-month declining-momentum trend, not a
single bad week.

**The transferable lesson for a new account** (relevant to Tangent, per the cross-account synthesis below):
riding a genuine news cycle can produce a real, legitimate multi-million-view peak even for a mid-size
account (735K followers, 65.7K median) — this is not fabricated or boosted, unlike Kallaway's spikes, the
engagement-rate evidence here is fully consistent with organic virality throughout the March cluster — but
a news-cycle spike without a durable format/series wrapper around it decays rather than compounds, which is
the single most important practical difference between Ankit Arora's trajectory and Harper Carroll's.

---

# CROSS-ACCOUNT SYNTHESIS

## Variance profiles compared

| Account | Followers | Median views | Top raw view | Top/median ratio | Median/follower | Variance archetype |
|---|---|---|---|---|---|---|
| **Kallaway** | 442K | 177K | 74.2M | **419x** | 40% | **Serial-spike (probable paid-boosted)** — extreme top/median driven by 2-3 unpinned mid-grid mega-spikes with anomalous (100-1000x-below-norm) engagement rates, layered on top of genuinely strong organic craft (40% median ratio, 2 legitimately-pinned 2024 multi-million hits at 1.3-4.4% like-rate) |
| **Nick Saraev** | 568K | 132.5K | 1.7M | **12.8x** | 23.3% | **Consistent high-floor performer** — the tightest variance of the three, driven by an industrialized, identical funnel mechanic (comment-keyword-to-DM) run at high volume across nearly every post, top and flop alike, with engagement-rate parity between top and flop content |
| **Ankit Arora** | 735K | 65.7K | 5.5M | **83.7x** | 8.9% | **Spike-and-decay** — a genuine, organic (non-anomalous engagement rate), news-cycle-driven 10-day cluster of 3 top-4 hits in Mar 2026, followed by a multi-month decline in both reach and per-video engagement rate through Jul 2026, with no series/format wrapper to sustain the peak |

## What each archetype teaches a new account

**From Kallaway (serial-spike / probable-boosted archetype):** The organic craft is real and worth
studying independent of the boost question — a consistent branded-packaging template (split-frame,
red-banner, talking-head + wordmark), a repeatable claim→objection-preempt→mechanism→stakes script
structure, and news-reaction speed-to-post all plausibly explain the account's genuinely strong 40%
median/follower ratio and its two legitimately organic multi-million pinned hits. **The critical lesson,
though, is a warning, not a formula**: raw view counts alone are not evidence of a replicable organic
technique, and this dossier's central methodological finding — that like-rate, cross-checked against an
account's own confirmed-organic baseline, is a far more reliable signal than view count alone — should be
the standing diagnostic any future account-audit in this pipeline applies before crediting a "packaging
technique" with a view-count outcome. A new account should absolutely study Kallaway's script/hook
architecture (it is genuinely well-crafted and visible even on the flop); it should NOT assume it can
reproduce his top-line view numbers through packaging craft alone.

**From Nick Saraev (consistent-floor archetype):** The lesson is mechanism-matching over magic-keyword-
chasing. "Free Claude Code" content works for this account not because "Claude Code" is an inherently
viral phrase, but because Claude Code rate-limits are a frequent, concrete, audience-wide recurring
frustration for the specific technical audience Saraev has built — satisfying Berger's Triggers pillar in
a way most content never achieves this cleanly. The transferable formula is: **identify your specific
audience's most frequently recurring, concretely-felt frustration with a tool they already pay for or
struggle with, then deliver (not just tease) a specific, verifiable fix, front-loaded rather than gated.**
The industrialized, identical comment-to-DM funnel run on every single post (proven here to produce
engagement-quality parity between the account's best and worst performers) is itself a replicable
operating discipline independent of any single video's topic — consistency of mechanic, not
consistency of virality, is what this account actually demonstrates.

**From Ankit Arora (spike-and-decay archetype):** The lesson is that a genuine, organic, news-cycle-driven
spike (unlike Kallaway's, this account's March cluster shows no engagement-rate red flags) is a real and
valuable but perishable asset unless it is wrapped in a durable format. The direct, evidence-backed contrast
with Harper Carroll (a numbered weekly series + a standing named brand-partnership, both structurally
absent from Ankit Arora's March cluster) is the clearest actionable takeaway in this entire dossier: **when
a piece of content succeeds by riding a real news cycle, the next move should be to fold that success into
a recurring, named, appointment-viewing format (a numbered series, a branded recurring segment, a standing
partnership) rather than treating it as a one-off win to be followed by more one-off, topically-adjacent-
but-administratively-independent posts** — the latter path is what produced this account's visible,
multi-month decay rather than compounding growth.

**Composite recommendation for Tangent:** none of these three archetypes should be copied wholesale.
Kallaway's raw numbers are not safely attributable to organic technique. Saraev's model requires an
already-large, already-technical, pain-point-sharing audience Tangent does not yet have. Ankit Arora's
model shows what NOT to do after a lucky break. The one thread that generalizes cleanly across all three —
and that this dossier's evidence supports independent of the boost/decay/consistency questions — is
**STEPPS-aligned hook engineering matched to a real, specific, addressable pain point or curiosity gap,
delivered through a consistent, repeatable visual/structural packaging template**, with the explicit
caveat that packaging consistency alone (demonstrated identically on hits AND flops across all three
accounts in this dossier) never explains reach variance by itself — something else (a recurring trigger,
a news cycle, or, in Kallaway's case, probable paid spend) always does the marginal work.

---

## Method log

**Tooling:** yt-dlp 2026.07.04 run directly against `instagram.com/reel/<shortcode>` URLs for all 12
target reels (3 top + 1 flop × 3 accounts), no login session, no claude-in-chrome browser tools (per
assignment constraint). All work in `/private/tmp/claude-501/.../scratchpad/ig_trio/`.

**What was fetched, per reel:**
1. `yt-dlp --skip-download --print "TITLE/DATE/LIKES/COMMENTS"` — succeeded for all 12/12 reels, first
   attempt, no rate-limiting encountered (a 3-second `sleep` was inserted between calls as a courtesy
   precaution, not because any 429s were observed).
2. `yt-dlp --skip-download --print "%(description)s"` — succeeded for all 12/12, capturing full caption
   text used for all hook/structure/CTA analysis in this dossier.
3. `yt-dlp --skip-download --write-thumbnail` — succeeded for all 12/12, downloaded as a frame-1 proxy
   (Instagram's chosen cover image, not necessarily the literal 0:00 frame — flagged as a caveat
   throughout rather than treated as a confirmed literal first frame) and visually inspected via the Read
   tool for every Packaging (§1) section in this dossier. This was the single highest-value research
   decision in this pass — it surfaced Kallaway's branded-template consistency, Saraev's identical-shell-
   across-flop finding, and Ankit Arora's stylized-portrait-vs-plain-selfie packaging regression, none of
   which would have been visible from caption text alone.
4. `yt-dlp -j` (single reel, DVhB8rMjp1m) to inspect the full available JSON field set — confirmed
   `view_count` is NOT exposed for Instagram via yt-dlp (`None`), confirmed `duration` is also `None`
   (logged as a structural DATA GAP across all 12 videos' §0 sections), confirmed 1080×1920 dimensions.

**Cross-platform hunting performed:**
- Nick Saraev: `yt-dlp --flat-playlist` against `@NickSaraev/videos` and `@NickSaraev/shorts` — found and
  directly pulled stats for a matching "free Claude Code" long-form video (`U6gg_bi1I70`, 189,015 views),
  confirming the theme is cross-platform, not IG-only; also discovered the YT Shorts tab runs a
  structurally different (mindset/business) content pillar at far lower views — a genuine, useful negative-
  space finding.
- Kallaway: `yt-dlp --flat-playlist` against `@kallaway/videos` — found an active but much-lower-view
  YouTube channel (interviews, product reviews), confirming IG is the primary growth engine.
- Ankit Arora: `yt-dlp --flat-playlist` against `@ai_ankitarora` (404, does not exist as a YT handle) and
  `@aiankitarora` (found, active) — sampled both `/videos` and `/shorts` tabs; **no cross-post match found**
  for either of the two March 2026 IG hit topics (Claude CoWorks podcast automation, "Your AI is lying to
  you") — logged as a negative finding, not fabricated; this dossier's Video 1/2 analysis for this account
  therefore relies on IG caption text only, with no transcript-level detail, consistent with QC_PROTOCOL.md
  §3's allowance for "could not obtain transcript" data gaps.

**WebSearch calls made:** (1) Nick Saraev/Maker School background — confirmed founder bio, LeftClick
agency, cross-platform reach claims; (2) Kallaway/sandcastles.ai background — confirmed real name (Kane
Kallaway), product description; (3) Instagram `#lumapartner`/`#chatgptpartner` tag meaning — confirmed
these are self-declared hashtags, NOT Instagram's official Paid Partnership disclosure label, a distinction
carried through this dossier's Video 1/2 (Kallaway) analysis; (4) Ankit Arora cross-platform presence —
located the `@aiankitarora` YouTube handle used for the cross-post hunt above.

**The Kallaway numeric discrepancy** (this dossier's yt-dlp like-count pulls vs. the harvest file's
independent re-verification agent's pulls, for all three mid-grid mega-spikes) is disclosed in full in
each affected video's §0 rather than silently resolved in favor of one reading — comment counts matched
exactly across both independent pulls in all three cases, which is the basis for this dossier's confidence
that both pulls hit the correct video; only the like-count field diverged, for reasons this dossier could
not determine (possibly a live-changing count between the two pull times, possibly a display-vs-API field
difference — genuinely unresolved, flagged as such).

**Reads performed for required comparative context:** `research/QC_PROTOCOL.md`,
`research/templates/video_postmortem_template.md`, `research/03_virality_science.md` (all mandatory
first-reads); `research/ig_harvest/kallaway.md`, `nick_saraev.md`, `ai_ankitarora.md`, `00_INDEX.md`
(primary data); `research/ig_harvest/harpercarrollai.md` (for the series-compounding contrast, per the
Ankit Arora central question); `research/creators/yt_nateherk.md` §C (for the Nate Herk YouTube-formula
contrast, per the Saraev central question) — re-read in full rather than summarized secondhand.

**What was NOT done / explicit scope limits:** No video files were downloaded or watched frame-by-frame
(cover-thumbnails only); no in-video burned-in captions/subtitles beyond what a single thumbnail frame
could show were inspected; no comment-thread contents were pulled for any of the 12 reels (comment
*counts* only); exact video durations could not be obtained for any of the 12 reels via yt-dlp against
Instagram (a structural tool limitation, not a skipped step). All are logged as DATA GAP at the relevant
template section rather than fabricated, per QC_PROTOCOL.md's hard rules.
