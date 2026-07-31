# Creator Dossier: Vaibhav Sisinty (Instagram @vaibhavsisinty)

**Status:** Prototype/roster account per the harvest index (`ig_harvest/00_INDEX.md`), NOT flagged a
formal "deep-dive" — but assigned here for a full forensic pass per direct brief. Held to the same
template-compliance and evidence-tier standard as every other dossier in this project
(`QC_PROTOCOL.md`).

**Analyst method:** Context research (WebSearch/WebFetch) done first, per the brief's sequencing
instruction, before re-reading the primary IG harvest file. The primary harvest file's "Detail pulls
(supplementary harvest)" section (top-5 + 2 flops, browser-agent-sourced) had landed by the time this
dossier's video-level work began, and is used as the primary source for all 7 post-mortems below. This
dossier independently re-fetched all 7 reel URLs via `WebFetch` as a cross-check (see Method log,
Section E) — the two independent pulls agreed within normal likes-count rounding tolerance on every
video, which is reported per-video as corroboration.

No claude-in-chrome browser tools were used (reserved per instructions). All web research used
WebSearch/WebFetch; all video-file-level work (YouTube cross-posts, transcripts, thumbnails) used
`yt-dlp` directly against public YouTube URLs.

---

## A. Account header + funnel map

| Metric | Value | Source | As-of | Confidence |
|---|---|---|---|---|
| IG followers | **2M** | `[OBSERVED]` og:description carried in `ig_harvest/vaibhavsisinty.md` ("2M Followers, 991 Following, 3,956 Posts"), reused from an earlier prototype pull, not re-verified this session | dated to the earlier prototype pull, exact date not logged in that file | MED (not re-verified by this dossier) |
| IG total posts | 3,956 | same source as above — note this is **all post types** (reels + photos/carousels), not a reel-specific count, so it over-states reel volume specifically | same | MED |
| Median reel views (60-tile sample) | **465.5K** | `[OBSERVED]` `ig_harvest/vaibhavsisinty.md` | 2026-07-25 | HIGH |
| Top reel views (60-tile sample) | **1.7M** (`DZK-XJ-AIZK`) | `[OBSERVED]` same | 2026-07-25 | HIGH |
| Median/follower ratio | **23.3%** — tied with `nick_saraev` for the **2nd-highest ratio among all 10 "deep-dive"-tier accounts** in this study, and top-5 overall across all 24 accounts harvested (see `00_INDEX.md` quick-ranking) | `[OBSERVED]`, computed | 2026-07-25 | HIGH |
| Pinning | **None detected** — position 1 (newest) is the single lowest-view tile in the whole 60-tile sample, the opposite of a pin-shape | `[OBSERVED]`, per-tile view sweep | 2026-07-25 | HIGH |
| YouTube (`@vaibhavsisinty`) | ~231K subscribers (per secondary press, not independently re-verified) | `[REPORTED]` sigmastory.in profile piece, citing "late 2025" figure | accessed 2026-07-25, figure dated late-2025 | MED |
| YouTube Shorts catalog size | **≥450** shorts confirmed to exist via flat-playlist sweep (this dossier stopped sweeping at 450 for time-budget reasons — catalog may be larger) | `[OBSERVED]` yt-dlp, this session | 2026-07-25 | HIGH (as a floor, not an exact total) |
| LinkedIn | ~398K followers | `[REPORTED]` Taplio lookup page surfaced via WebSearch snippet | 2026-07-25 | MED |
| X/Twitter | Active (`@VaibhavSisinty`), posts similar AI-news-roundup content in text form | `[OBSERVED]` via WebSearch result snippets showing live post text | 2026-07-25 | MED |

**Business entity & scale** `[REPORTED]`:
- Legal entity **Sisinty Private Limited** — parent of GrowthSchool, OutSkill, and "Build School" —
  generated **₹50–100 Cr revenue** (~US $6–12M) for FY ending 2025-03-31. Source: Tracxn company/legal-
  entity profile, accessed 2026-07-25. MED confidence (Tracxn aggregates filed-financials data; the
  dossier did not independently pull the underlying MCA filing).
- **GrowthSchool**: founded 2021 by Vaibhav Sisinty (ex-Uber, ex-Klook growth roles). Raised **$5M seed**
  in 2021 from Sequoia India, Owl Ventures, and 80+ angels (sources disagree slightly on the exact
  investor list — Tracxn says "Owl Ventures and Peak XV Partners," a separate WebSearch summary says
  "Sequoia India, Owl Ventures" — Sequoia India rebranded to Peak XV in 2022, so these likely describe
  the same round under old/new naming; flagged as a minor sourcing inconsistency, not resolved).
  Self-reported: 10M+ learners, 150+ countries, 400% YoY revenue growth (self-reported PR-style figures,
  **not independently audited** — treat as MED-LOW confidence, standard-issue founder-PR inflation risk).
  Broad-curriculum cohort courses (marketing, product, design, business), practitioner-instructor model.
- **OutSkill**: `[REPORTED]` a **sister brand, not a separate funded company** — Tracxn lists it as
  "unfunded," under the same Sisinty Private Limited umbrella. AI/tech-specific vertical (the actual
  product line his AI-content Instagram funnel is most likely to feed, distinct from GrowthSchool's
  broader catalog). Runs a recurring **"2-Day AI Mastermind" workshop**, nominally priced ~₹4,999–5,000,
  distributed as **free via referral-link promotions** (10,000+ reported participants per WebSearch
  aggregation of Medium/Trustpilot mentions, MED-LOW confidence, self-reported/participant-blog sourced).

**Funnel map — what the CONTENT actually says, observed directly, vs. what the business PRESS says**
`[OBSERVED]` (from the 7 reel captions pulled for this dossier, Section B below) vs `[REPORTED]`
(from press about GrowthSchool/OutSkill):
- **The observed, in-reel CTA is uniform and narrow**: all 7 analyzed reels (5 top + 2 flops) end on
  some variant of *"join my free WhatsApp community — link in bio"*, funneling through a third-party
  WhatsApp-broadcast tool (`join.switchit.app/YT`, confirmed in a cross-posted YouTube video's
  description, Section E). **Not one of the 7 reels directly names GrowthSchool, OutSkill, a course, or
  a price** — the paid-product pitch, if any, happens downstream of the WhatsApp opt-in, outside this
  dossier's visibility. This is a **three-hop funnel**: Reel (discovery) → WhatsApp community (owned,
  daily-AI-news nurture channel) → [`INFERRED`, not observed in this sample] eventual OutSkill/
  GrowthSchool pitch inside that community or via subsequent DM/email. The `[INFERRED]` hop is a
  reasonable read given his overall business (an ed-tech founder building a free daily-AI-news list has
  an obvious reason to do so) but this dossier did not obtain access to the WhatsApp community itself to
  confirm what happens after opt-in — logged as a DATA GAP, not invented.
- One video (`DZK-XJ-AIZK`, the #1 reel) sharpens the loop further: *"Full list dropping in my WhatsApp
  community"* — explicitly withholding part of the content itself (not just "more content," but *this
  video's own promised payoff*) behind the opt-in, a stronger curiosity-gap/practical-value combination
  than the other 6 reels' softer "I share updates like these" framing.
- **Self-reported production-system claim, directly germane to the funnel**: a 2026 Instagram post
  (`instagram.com/p/DNGh28v0Tof/`, not one of the 7 analyzed reels, `[OBSERVED via WebFetch]` of the live
  caption) states: *"800K followers in 8 months. 99% of my content in this journey? AI-generated. The
  voice. The videos. My AI clone. But the perspective? 100% me. Always."* This post is itself explicitly
  framed as a **case-study-as-marketing** move ("the biggest announcement yet," swipe-through carousel) —
  i.e., the growth-hacking demonstration IS the funnel content, modeling the exact skill (AI-content
  production) that OutSkill's paid AI workshops teach. A separate LinkedIn post
  (`[OBSERVED via WebFetch]`, `linkedin.com/posts/vaibhavsisinty_using-my-ai-clone-to-ship-long-form-...`)
  states he is *"Using my AI clone to ship long form videos on AI updates every week on YouTube"* and
  that *"the effort to make it happen is a lot right now."* Both are self-reports from the subject
  himself, not independently verified production-log evidence — treated as `[REPORTED, self-source]`,
  the strongest tier available for a claim about someone's own private production process, but not
  equivalent to `[OBSERVED]` forensic proof.

---

## B. Video post-mortems (7 videos: top 5 by views + 2 flops)

Selection method: identical to the primary harvest file's own selection — top 5 and bottom 2 of the
60-tile grid sample, with the 3 most-recently-posted tiles excluded from the flop pool (still accruing
views, would unfairly rank as flops). Both this dossier's independent `WebFetch` re-pull of each reel URL
and the primary harvest's browser-agent detail-pull agree on caption text and dates; likes/comments agree
within normal K-rounding (e.g. this dossier's WebFetch read "27.4K" likes where the harvest file's browser
pull read "27K" — same underlying number, different rounding granularity of the same UI element).

---

### VIDEO 1 (TOP, rank 1/60 sampled — 3.65x channel median): "Microsoft just made 7 moves at once"

#### 0. Identity & stats
- URL: instagram.com/reel/DZK-XJ-AIZK/. Platform: Instagram Reels. Posted **2026-06-04**
  `[OBSERVED]` (both pulls agree). Length: not directly observed — DATA GAP (Instagram does not expose
  duration in either the grid pull or the WebFetch caption pull; Reels are capped at 90s and this genre
  typically runs 45–75s per the one proxy this dossier could time, see Video 7).
- Views: **1.7M** `[OBSERVED, ig_harvest grid pull, 2026-07-25, HIGH]`. Likes: **27K** `[OBSERVED,
  ig_harvest detail-pull, HIGH]` (this dossier's own WebFetch read 27.4K — same figure, finer rounding).
  Comments: **80** `[OBSERVED, HIGH]`. Shares/saves: not exposed by either pull method — DATA GAP,
  structural (Instagram does not surface these publicly without the poster's own Insights access).
- Rank: **#1 of the 60-tile sample**, **3.65x the channel median** (465.5K). The single best-performing
  reel in the sampled catalog.

#### 1. Packaging
- Caption/first line `[OBSERVED]`: "Microsoft just made 7 moves at once. The last one shot at NVIDIA."
  — a **listicle promise** (7 moves) combined with a **withheld-detail curiosity gap** (which one, and
  how does it "shoot at NVIDIA"?) that is not resolved until deep into the caption/video.
- Thumbnail/first-frame: DATA GAP — this dossier did not obtain a frame-level capture of this specific
  reel (Instagram media files were not downloadable via the tools available; see Method log). A
  visually-comparable YouTube-catalog thumbnail from the same creator, checked for a different video
  (Section D), shows a consistent direct-to-camera persona with stylized burned-in captions — offered as
  a plausible analog for this account's general visual template, **not** as observed evidence for this
  specific video.
- Curiosity gap: strong — "7 moves" sets a concrete, countable promise (list format primes completionist
  motivation); "shot at NVIDIA" is an unexplained claim requiring payoff.

#### 2. Hook (0–3s)
- Caption-implied opening line (the caption itself functions as a near-verbatim hook script in this
  genre, per this dossier's one confirmed proxy transcript in Video 7 — but for this video specifically,
  the exact spoken opening was not independently confirmed against audio; flagged as `[INFERRED from
  caption]`, not `[OBSERVED via transcript]`): "Microsoft just made 7 moves at once."
- Hook taxonomy: **Bold claim** + **listicle/roundup framing**, per 03_virality_science.md §3.1. The
  "shot at NVIDIA" clause additionally functions as a **confronting-question-adjacent** tease (implicitly
  asks "how would a software company move against a hardware giant?").
- What the viewer sees: DATA GAP (no frame-level capture for this video specifically).

#### 3. Structure & retention engineering
- Beat map (`[INFERRED from caption sequencing]`, not a confirmed transcript — the caption lists, in
  order: reasoning model → always-on agent → 15-language voice cloning → 43-language transcription incl.
  Hindi → small coding model beating larger ones → in-house "Maia 200" AI chip, closing with "Microsoft
  is no longer renting anyone else's brain or hardware. It just built the whole stack itself.") This
  reads as a **drip-fed listicle structure**: six items enumerated in the body, with the actual
  "shot at NVIDIA" payoff (the in-house Maia chip = no longer needing NVIDIA's silicon) landing on item 6
  of 7 — a late-loop-close consistent with §2.6.1.
- One-idea-per-video: arguably a **listicle exception to strict one-idea discipline** (§3.2 explicitly
  carves this out as valid when unified under one frame — here, "Microsoft going fully vertical").
- Open loop: "what's the move that shoots at NVIDIA?" opened in the hook, closed at the Maia-chip
  reveal — classic curiosity-gap payoff placement.
- Pacing/captions: DATA GAP, no frame-level access.

#### 4. Value proposition
- Walk-away value: **news awareness** (a competitive-landscape update) with a light **identity-boost**
  angle (being "ahead" on an under-discussed strategic story). Not a copyable workflow — this is the
  news/analysis category, not the tool-tutorial category some of his other content (Video 7) falls into.
- Practical value class: **news** (primary), light **social currency** (secondary — "I clocked what
  Microsoft is really doing" is a smart-and-ahead framing).
- Specificity: HIGH — six named, concrete product moves (reasoning model, agent, voice-cloning language
  count, transcription language count incl. Hindi specifically, coding-model claim, named chip "Maia
  200") rather than vague "Microsoft is doing AI stuff" gesturing.

#### 5. Psychology scoring
- STEPPS: **Social Currency** (being the one who "gets" the real strategic story, not just the headline)
  and **Practical Value** (a genuine competitive-landscape update, "news you can use" for anyone tracking
  the AI infrastructure race) are the dominant pillars. **Triggers** present but weak (Microsoft/NVIDIA
  are frequent-enough names in this audience's feed to re-cue recall). **Story**: mild narrative arc
  (independence-from-NVIDIA as the throughline), not a strong character-driven story.
- Primary emotion: **awe/mild anxiety** (a dominant tech player consolidating power) — high-arousal per
  Berger & Milkman §2.3, consistent with this being the top-performing video of the sample.
- Identity-signaling: strong — sharing this says "I track the infrastructure layer of the AI race, not
  just the consumer-app headlines," a more sophisticated-reader identity than most AI-news content.
- Save/send trigger: MED — the "Hindi specifically" detail inside the transcription-language item is a
  small but real India-audience-specific hook (see Section D, central question 4) that could prompt a
  "this is relevant to me specifically" send among Indian-professional followers.

#### 6. CTA & funnel mechanics
- Explicit CTA: "Full list dropping in my WhatsApp community. Link in bio." — this is the
  **strongest funnel mechanic of the 7 analyzed reels**: it withholds part of THIS video's own promised
  content (not just generic "more content"), a sharper curiosity-gap-to-opt-in bridge than the other 6.
- Comment-bait check: no bare "comment X" ask on this video — the CTA is content-attached (a genuine
  extended list, not an empty engagement request), compliant with §1.3.2's anti-bait standard.
- Funnel position: top-of-funnel discovery bait feeding directly into the account's one and only observed
  funnel step (WhatsApp opt-in) — see Section A funnel map.

#### 7. Replicability verdict
- Extractable template: (1) pick a single dominant news subject with 5+ concrete sub-facts, (2) frame as
  a countable list with one held-back "biggest" item, (3) close the loop with a one-line strategic
  reframe ("no longer renting anyone else's brain"), (4) CTA = "rest of the list is in my [owned channel]."
- Commodity vs. unfair advantage: the news-roundup format itself is commodity (any AI-news account can
  do it); the account's advantage is **research/writing velocity at near-daily cadence** (Section D) and
  an **established owned-audience nurture channel** (WhatsApp community) to withhold payoff into.
- Difficulty for Tangent: **HIGH** for direct format replication (Tangent is a visual-art gallery, not a
  tech-news beat — there is no equivalent "breaking news" cycle to surf) but **LOW-MED** for the
  structural mechanics (list-format curiosity gap + owned-channel payoff-withholding is a genre-agnostic
  retention/funnel technique).

#### 8. Why it won
- The single most load-bearing factor is **topical newsworthiness of a major-platform story** (Microsoft
  vertically integrating its AI stack) landing on an audience that already follows AI infrastructure
  news — this is "news you can use" for a sophisticated audience, not a generic tips video, which likely
  explains both the #1 view rank AND a comparatively modest like-rate (1.59%, mid-pack among the top 5 —
  see Section C) since news-consumption behavior skews toward passive viewing/sharing over active liking.
  Secondary factor: the "shot at NVIDIA" curiosity-gap framing and the India-relevant "Hindi" detail
  (Section D). No obvious luck/trend-surfing component beyond the underlying news event's own timing,
  which this dossier cannot independently confirm as accurately reported (see Section D's honesty note on
  unverified AI-hype claims in this genre generally).

#### Sources
- instagram.com/reel/DZK-XJ-AIZK/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md (detail-pull table + grid, 2026-07-25)

---

### VIDEO 2 (TOP, tied rank 2/60 — 2.79x median): "Google just killed your portfolio tracker"

#### 0. Identity & stats
- URL: instagram.com/reel/DaNu_sMAVD_/. Posted **2026-06-30** `[OBSERVED]`. Length: DATA GAP (same
  structural reason as Video 1).
- Views: **1.3M** `[OBSERVED, HIGH]`. Likes: **10K** `[OBSERVED, HIGH]` (WebFetch read 10.4K, same
  figure). Comments: **51** `[OBSERVED, HIGH]`. Shares/saves: DATA GAP.
- Rank: **tied #2/#3 of 60** (1.3M, alongside `DZEpQ9cgEik` below), **2.79x median**.

#### 1. Packaging
- Caption/hook: "Google just killed your portfolio tracker." — a **bold, hyperbolic claim** (a feature
  upgrade framed as an act of destruction of the status quo) aimed at a specific reader identity
  (people who track a stock/investment portfolio).
- Curiosity gap: MED — the claim is bold but the payoff (screenshot-to-portfolio-tracking) is
  substantially explained within the caption itself, leaving less unresolved than Video 1's list-based
  gap.

#### 2. Hook (0–3s)
- `[INFERRED from caption]`: "Google just killed your portfolio tracker."
- Hook taxonomy: **Bold claim**, single-subject (not a listicle like Video 1) — a direct tool-upgrade
  announcement.
- What the viewer sees: DATA GAP, no frame-level capture obtained.

#### 3. Structure & retention engineering
- Beat map `[INFERRED from caption]`: claim → mechanism (screenshot a brokerage account → AI reads
  holdings, builds portfolio) → format flexibility (CSV/PDF/plain English all work) → conversational
  payoff (ask what sectors you're overexposed to, get daily pre-market briefings) → CTA.
- One-idea-per-video: yes — a single tool feature (Google Finance's AI portfolio ingestion), explained
  end-to-end.
- Open loop: weaker than Video 1 — "killed your portfolio tracker" is largely resolved by the caption's
  own explanation rather than held open for the WhatsApp community.
- Pacing/captions: DATA GAP.

#### 4. Value proposition
- Walk-away value: **tool discovery** — a specific, named, immediately-usable feature (Google Finance)
  most viewers with any brokerage account can try today.
- Practical value class: **tool discovery + copyable workflow** (a literal step: "drop in a screenshot").
- Specificity: HIGH — names the exact input formats accepted (CSV, PDF, plain English) and two concrete
  use cases (sector-overexposure check, pre-market briefing).

#### 5. Psychology scoring
- STEPPS: **Practical Value** is overwhelmingly dominant — this is close to a pure utility video with
  minimal narrative or social-currency framing. **Triggers**: MED — "portfolio," "brokerage account" are
  recurring personal-finance touchpoints for the audience segment that has one.
- Primary emotion: **low-arousal, utility-calm** rather than awe/anxiety/amusement — per §2.3 this
  predicts weaker viral transmission relative to high-arousal content, which is consistent with this
  video having the **lowest like-rate of the entire 7-video sample (0.77%)** despite being tied for the
  2nd-highest view count — a concrete data point supporting the arousal-vs-shares theory rather than a
  simple views-track-likes assumption.
- Identity-signaling: LOW-MED — useful but not a "smart/ahead" flex in the way Video 1's infrastructure-
  race read is; more purely transactional ("this will help me," not "this makes me look sharp").
- Save/send trigger: HIGH despite the low like-rate — this is exactly the kind of narrow, personally-
  addressable "you specifically have a portfolio, you'd want this" content §2.7 identifies as save/send-
  favorable even when it under-performs on likes. `[INFERRED]`: the view/like divergence on this video is
  the clearest single piece of evidence in this sample for saves/sends outperforming likes as the actual
  distribution driver, though this dossier cannot directly observe save/send counts to confirm (DATA GAP,
  reasoning stated).

#### 6. CTA & funnel mechanics
- "Full breakdowns in my WhatsApp community. Link in bio." — softer than Video 1 (no specific withheld
  fact, just "more depth").
- No comment-bait mechanic present.
- Funnel position: same top-of-funnel WhatsApp opt-in as all 7 videos.

#### 7. Replicability verdict
- Template: pick a widely-used consumer tool, name one dramatic new AI-native capability, walk through
  2-3 concrete input formats and 2 concrete use cases, close on "more depth in my [channel]."
- Commodity vs. advantage: fully commodity format — any creator covering a real product update can do
  this; no unique advantage visible in this specific video beyond being fast to publish once the feature
  shipped.
- Difficulty for Tangent: **HIGH** — Tangent has no equivalent "new feature just shipped" news cycle to
  cover; the tool-tutorial genre itself doesn't transfer to a fine-art gallery brand.

#### 8. Why it won
- Most load-bearing factor: **broad relevance of the underlying trigger** (many professionals have a
  brokerage account) combined with **topical timeliness** (a real, recent Google Finance feature).
  Secondary: high specificity (named exact input formats) which makes the practical value concrete rather
  than vague. The notably low like-rate relative to its view count is this dossier's strongest evidence
  that **view distribution and on-post engagement-rate are not the same signal** for this account — a
  point directly relevant to Section C's decomposition of the account's headline ratio.

#### Sources
- instagram.com/reel/DaNu_sMAVD_/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md

---

### VIDEO 3 (TOP, tied rank 2/60 — 2.79x median): "A 4000 rupee filter and 74% cleaner exhaust"

#### 0. Identity & stats
- URL: instagram.com/reel/DZEpQ9cgEik/. Posted **2026-06-01** `[OBSERVED]`. Length: DATA GAP.
- Views: **1.3M** `[OBSERVED, HIGH]`. Likes: **47K** `[OBSERVED, HIGH]` (WebFetch read 46.8K). Comments:
  **197** `[OBSERVED, HIGH]` — the **highest raw comment count of the entire 7-video sample**.
  Shares/saves: DATA GAP.
- Rank: tied #2/#3 of 60, **2.79x median**.

#### 1. Packaging
- Caption/hook: "A 4000 rupee filter and 74 percent cleaner exhaust." — **result-first**, two hard
  numbers stated before any context is given (no subject named yet).
- Curiosity gap: HIGH — the numbers are legible but the "who/what" is completely withheld for the first
  clause, a clean information-gap per §2.1.1 (partial info: a concrete result; missing info: the actor
  and mechanism).

#### 2. Hook (0–3s)
- `[INFERRED from caption]`: "A 4000 rupee filter and 74 percent cleaner exhaust."
- Hook taxonomy: **Result-first / demo-in-motion** — the outcome is stated before the story, per
  §3.1's "shows the payoff before the process" pattern, distinct from the bold-claim hooks of Videos 1–2.
- What the viewer sees: DATA GAP.

#### 3. Structure & retention engineering
- Beat map `[INFERRED from caption]`: result stated → protagonist reveal ("Two high school students got
  tired of waiting for a perfect climate solution") → mechanism (3D-printed filter, algae that feeds on
  exhaust CO2, releases oxygen) → proof/scale ("already on 500 bikes in Indonesia") → credibility markers
  ("won a major American innovation prize," "built their own company," "all before graduation") → CTA.
- One-idea-per-video: yes, a single human-interest/invention story with a clear narrative arc (classic
  underdog-builds-something structure).
- Open loop: "who built this and how" opened at the hook, resolved progressively through the beat map —
  a well-constructed drip-reveal.
- Pacing/captions: DATA GAP.

#### 4. Value proposition
- Walk-away value: **aspiration/emotion** (inspiration from young builders) primarily, with secondary
  **news/awareness** value (a real climate-tech data point). Not a copyable workflow — this is the one
  video of the 7 that is pure story, not tool/tutorial content.
- Practical value class: **aspiration** (dominant) + light **news**.
- Specificity: HIGH — precise numbers throughout (₹4,000, 74%, 500 bikes, Indonesia, "major American
  innovation prize" — though the prize is not named, a minor specificity gap).

#### 5. Psychology scoring
- STEPPS: **Story** and **Emotion** are dominant here — the only video in this sample built as a genuine
  narrative (protagonist, obstacle, achievement) rather than a news/tool roundup. **Social Currency**:
  MED (sharing an inspiring underdog story is a mild "look what's possible" flex, but a gentler one than
  Videos 1/5's insider-knowledge framing).
- Primary emotion: **awe/admiration** — high-arousal positive per Berger & Milkman §2.3, and this video
  has the **highest like-rate of the entire sample (3.62%)**, roughly double the sample's top-5 average
  (1.8%) and 4x the two flops' average (0.94%) — the cleanest single data point in this dossier for the
  arousal-drives-sharing thesis.
- Identity-signaling: MED — sharing this signals optimism/appreciation for youth innovation more than
  personal expertise-signaling.
- Save/send trigger: MED — inspirational but not a reference tool most people would return to; more of a
  one-time emotional watch-and-share than a save-for-later utility piece (contrast with Video 2).

#### 6. CTA & funnel mechanics
- "I share updates like these in my free WhatsApp community. Link in bio." — the softest, most generic
  of the 7 CTAs (no withheld content, no specific promise, just a category description).
- No comment-bait mechanic — yet this video still pulled the highest raw comment count (197) of the
  sample, consistent with high-arousal-emotion content generating more spontaneous commentary even with
  a weak explicit CTA (an `[INFERRED]` read, reasoning stated).

#### 7. Replicability verdict
- Template: find a small-scale, verifiable human-interest invention/achievement story with 3+ hard
  numbers, open on the result, reveal the protagonist second, close on credibility markers, CTA is
  generic ("I share stories like this").
- Commodity vs. advantage: the "young inventor" story genre is commodity in the broader creator economy,
  but sourcing a *genuinely good, verifiable* one at this cadence (near-daily, see Section D) is real
  editorial/research work, not automatable in the same way the news-roundup format is.
- Difficulty for Tangent: **MED** — Tangent could plausibly run an analogous "artist/technique origin
  story" format (a specific painter's unusual materials, a restoration story, a young/emerging artist
  breakthrough) using the same result-first + protagonist-reveal + credibility-marker structure; this is
  the most directly portable format of the 7 videos in this sample, since it doesn't depend on the AI/
  tech news cycle specifically — it depends on narrative craft, which transfers across niches.

#### 8. Why it won
- Most load-bearing factor: **high-arousal positive emotion** (awe at a genuinely impressive youth
  achievement) delivered through a well-built narrative arc, which produced this sample's best like-rate
  by a wide margin and its highest comment count. Secondary: result-first hook with hard numbers creates
  an unusually tight information gap. This is the one video in the sample where views AND engagement rate
  both spiked together (unlike Video 2's views/likes divergence), suggesting the emotional-story format
  may be a stronger all-around performer per-video than the news-roundup format, even though the latter
  produced this sample's single highest view count (Video 1) — a nuance worth flagging for Section C.

#### Sources
- instagram.com/reel/DZEpQ9cgEik/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md

---

### VIDEO 4 (TOP, rank 4/60 — 2.15x median): "The most powerful AI ever made public"

#### 0. Identity & stats
- URL: instagram.com/reel/DZaRmD9A9eF/. Posted **2026-06-10** `[OBSERVED]`. Length: DATA GAP.
- Views: **1M** `[OBSERVED, HIGH]`. Likes: **14K** `[OBSERVED, HIGH]` (WebFetch read 14.4K). Comments:
  **109** `[OBSERVED, HIGH]`. Shares/saves: DATA GAP.
- Rank: **#4 of 60**, **2.15x median**.

#### 1. Packaging
- Caption/hook: "The most powerful AI ever made public." — an **unqualified superlative claim**, the
  same rhetorical move as the nateherk "Ultimate" case documented elsewhere in this project (see
  `creators/yt_nateherk.md`), applied to a model-release story rather than a workflow build.
- Curiosity gap: MED — the claim is bold but generic until the specific model/benchmark is named a beat
  later.

#### 2. Hook (0–3s)
- `[INFERRED from caption]`: "The most powerful AI ever made public."
- Hook taxonomy: **Bold claim / superlative**, per §3.1.
- What the viewer sees: DATA GAP.

#### 3. Structure & retention engineering
- Beat map `[INFERRED from caption]`: superlative claim → named benchmark comparison (a named model
  scoring 80% on "the hardest coding test" vs. a rival's 58%) → capability montage (plays Pokemon by
  sight, composes unheard music, "refuses to become a weapon") → time-boxed availability ("Free on Pro,
  Max and Team till June 22, then paid") → CTA (free prompt playbook).
- One-idea-per-video: yes, a single model-release announcement with a capability-montage structure
  (closer to a listicle-of-capabilities than a single demo).
- Open loop: "how powerful, exactly?" opened by the superlative, partially closed by the benchmark
  number, reinforced by the capability montage — a reasonably tight structure.
- Pacing/captions: DATA GAP.

#### 4. Value proposition
- Walk-away value: **news/awareness** of a frontier-model release plus a **time-sensitive practical
  incentive** (free-until-a-date framing creates urgency distinct from the other 6 videos).
- Practical value class: **news** (primary) + **urgency-driven tool discovery** (the free-until-June-22
  window is the only explicit deadline/urgency mechanic in this 7-video sample).
- Specificity: HIGH — a concrete benchmark score comparison (80% vs. 58%) and a concrete deadline date.

#### 5. Psychology scoring
- STEPPS: **Triggers** (frontier-model releases are a recurring, frequently-discussed topic for this
  audience) and **Practical Value** (a real, time-boxed free-access window) are dominant. **Social
  Currency**: MED (being early to a major release is a mild flex).
- Primary emotion: **awe + mild urgency/FOMO** — the deadline framing adds an urgency component distinct
  from the other reels' more evergreen framings, both high-arousal per §2.3.
- Identity-signaling: MED — "I know about the newest, most powerful model" is a competence-signal but a
  commonly-available one in this niche (many AI accounts cover every major release), so less distinctive
  than Video 1's infrastructure-strategy angle.
- Save/send trigger: HIGH for the specific "free until June 22" clause — this is the kind of
  time-boxed, addressable fact (§2.7) a viewer might specifically DM to a colleague who uses the paid
  tier ("use this before it's gone").
- **Honesty note**: this dossier could not verify whether "80% on the hardest coding test" vs. "58%" is
  an accurate benchmark citation (which benchmark, which model, methodology) — noted, not verified,
  consistent with this dossier's scope (virality post-mortem, not a fact-check of AI-industry claims).
  Flagged given the genre's documented susceptibility to unverifiable/exaggerated claims (see Section D).

#### 6. CTA & funnel mechanics
- "Grab my free prompt playbook in the WhatsApp community, link in bio." — content-attached (a specific
  named lead magnet, "prompt playbook"), not bare engagement bait.
- No comment-bait mechanic present.

#### 7. Replicability verdict
- Template: superlative claim → one hard comparative number → capability montage (3 short beats) →
  time-boxed urgency clause → named lead-magnet CTA.
- Commodity vs. advantage: fully commodity in the AI-news space (every major-model-release video across
  every AI creator in this study's roster uses some version of this template); the urgency clause is the
  only differentiated element, and it is time-perishable by nature (only usable while the deadline is
  real).
- Difficulty for Tangent: **HIGH** for the news-cycle-dependent parts; **MED** for the urgency-clause
  mechanic in isolation (a real limited-time offer/exhibit window is a portable retention/CTA device).

#### 8. Why it won
- Most load-bearing factor: **frontier-AI-release newsworthiness** for an audience with high baseline
  interest in model capability races, reinforced by a genuine time-boxed incentive (free access window)
  that both platforms this dossier examined this niche on tend to reward (urgency = a concrete reason to
  act now, not just watch). Secondary: capability-montage structure keeps multiple small payoffs coming
  rather than one flat claim.

#### Sources
- instagram.com/reel/DZaRmD9A9eF/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md

---

### VIDEO 5 (TOP, rank 5/60 — 2.11x median): "China just beat Neuralink. And nobody is talking about it."

#### 0. Identity & stats
- URL: instagram.com/reel/DZfrPXIgXCp/. Posted **2026-06-12** `[OBSERVED]`. Length: DATA GAP.
- Views: **983K** `[OBSERVED, HIGH]`. Likes: **16K** `[OBSERVED, HIGH]` (WebFetch read 15.9K). Comments:
  **144** `[OBSERVED, HIGH]`. Shares/saves: DATA GAP.
- Rank: **#5 of 60**, **2.11x median** — the lowest-ranked of the top-5 pool, but still comfortably above
  the 465.5K median.

#### 1. Packaging
- Caption/hook: "China just beat Neuralink. And nobody is talking about it." — a textbook, near-verbatim
  match to the **"nobody is talking about X"** hook taxonomy entry in §3.1, combined with a **competitive/
  geopolitical bold claim**.
- Curiosity gap: HIGH — "beat Neuralink" at what, exactly, is unresolved; "nobody is talking about it"
  additionally frames the viewer as about-to-be-let-in on overlooked information (Social Currency setup).

#### 2. Hook (0–3s)
- `[INFERRED from caption]`: "China just beat Neuralink. And nobody is talking about it."
- Hook taxonomy: **"Nobody is talking about X"** (explicit, textbook match) + **bold claim**, per §3.1.
- What the viewer sees: DATA GAP.

#### 3. Structure & retention engineering
- Beat map `[INFERRED from caption]`: claim → named actor/product ("NEO," a Shanghai startup's coin-
  sized brain implant) → regulatory fact ("approved... for commercial sale this week," implying
  timeliness) → mechanism/safety detail ("sits on the protective layer outside the brain," "90 minute
  surgery") → proof ("36 people tried it. Many moved their hands again after years of paralysis") → CTA.
- One-idea-per-video: yes, single-subject news story with a clean stakes → mechanism → proof arc.
- Open loop: "beat Neuralink how?" opened at the hook, closed via the regulatory-approval + patient-
  outcome proof beats — resolves cleanly by the end.
- Pacing/captions: DATA GAP.

#### 4. Value proposition
- Walk-away value: **news/awareness** of a specific medical-AI/neurotech milestone, with an emotional
  payoff (real patients regaining hand movement).
- Practical value class: **news** (primary) + light **emotion/human-interest** (the patient-outcome
  detail).
- Specificity: HIGH — named company/product (NEO, Shanghai), named surgery duration (90 minutes), named
  patient count (36), and a concrete outcome description.

#### 5. Psychology scoring
- STEPPS: **Social Currency** is the dominant pillar here, driven directly by the "nobody is talking
  about it" framing — sharing this explicitly positions the sharer as ahead of the broader conversation,
  the single clearest Social-Currency-coded hook in the 7-video sample. **Emotion** is also present and
  genuine (patient outcomes are an emotionally weighted detail, not neutral tech spec).
- Primary emotion: **awe + mild geopolitical anxiety** (China outpacing a marquee US company on a
  medical-AI frontier) — high-arousal, consistent with a top-5 rank.
- Identity-signaling: HIGH — explicitly the strongest of the sample, because the hook itself frames the
  act of knowing/sharing as a status marker, not just the content's inherent interestingness.
- Save/send trigger: MED-HIGH — a specific, addressable "did you see this" moment for anyone following
  either the Neuralink story or China/US tech competition generally.

#### 6. CTA & funnel mechanics
- "I break down stuff like this every day in my WhatsApp community. Link in bio." — notably includes an
  explicit cadence claim ("every day"), the only one of the 7 captions to state posting frequency
  directly inside the CTA itself — directly corroborating this dossier's independently-computed ~1-post/
  day cadence finding in Section D (a nice cross-check: the creator's own self-description matches the
  dossier's date-derived math).
- No comment-bait mechanic.

#### 7. Replicability verdict
- Template: identify a genuine "underdog surprises incumbent" competitive story, open with the explicit
  "nobody is talking about X" framing, name the specific actor/product/regulatory milestone, close on a
  concrete human-outcome proof point.
- Commodity vs. advantage: the underlying story-sourcing (finding a real, verifiable, under-covered
  competitive-tech story) is closer to genuine editorial/research work than the more templated news-
  roundup videos (1, 2, 4) — harder to commodity-automate purely with an LLM prompt.
- Difficulty for Tangent: **MED** — the "nobody is talking about X" + insider-knowledge framing is a
  genre-agnostic Social-Currency device; Tangent could plausibly apply it to an overlooked art-historical
  fact, technique, or under-recognized artist, without needing the tech-news subject matter itself.

#### 8. Why it won
- Most load-bearing factor: the **explicit "nobody is talking about it" Social-Currency hook**, which
  this dossier judges as the single most textbook-perfect STEPPS activation in the 7-video sample,
  combined with a genuinely emotionally-weighted proof point (paralyzed patients regaining hand movement)
  that most of this sample's other pure-news videos lack. Secondary: geopolitical stakes framing (China
  vs. a marquee US brand) taps a recurring Trigger for this audience.

#### Sources
- instagram.com/reel/DZfrPXIgXCp/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md

---

### VIDEO 6 (FLOP, rank 60/60 eligible — 0.43x median): "Your plant can finally talk"

#### 0. Identity & stats
- URL: instagram.com/reel/DbDltYAge31/. Posted **2026-07-21** `[OBSERVED]`. Length: DATA GAP.
- Views: **200K** `[OBSERVED, HIGH]` — the **lowest view count of the eligible (non-3-most-recent) pool**.
  Likes: **1,756** `[OBSERVED, HIGH]` (WebFetch independently read "1.8K," consistent rounding of the same
  figure). Comments: **16** `[OBSERVED, HIGH]` — tied for the lowest raw comment count in the sample.
  Shares/saves: DATA GAP.
- Rank: **bottom of the eligible 60-tile pool**, **0.43x the channel median** — the weakest video in this
  dossier's sample by a wide margin (less than half the median, vs. the next-weakest flop at 0.55x).

#### 1. Packaging
- Caption/hook: "Your plant can finally talk." — a **whimsical bold claim**, playful register distinct
  from the other 6 videos' news/stakes-driven framing.
- Curiosity gap: MED — cute and clear, but low-stakes; the "gap" (how would a plant talk?) is narrower
  and less urgent than "China beat Neuralink" or "Microsoft's 7 moves."

#### 2. Hook (0–3s)
- `[INFERRED from caption]`: "Your plant can finally talk."
- Hook taxonomy: **Bold claim**, but the mildest/lowest-stakes version of that category in the sample —
  more novelty than urgency.
- What the viewer sees: DATA GAP.

#### 3. Structure & retention engineering
- Beat map `[INFERRED from caption]`: claim → tool/provenance (OpenAI built "Plant Talk," open-sourced,
  free) → mechanism (webcam reads leaf color/spots/drooping, AI voices a response) → illustrative demo
  lines ("getting a tad crispy," "asks for humidity") → setup requirement (zero coding, just a webcam) →
  CTA (5-step setup guide).
- One-idea-per-video: yes, single tool demo, clean structure — **the structural quality is comparable to
  the top-5 videos**; this is a case where a well-built video still underperformed, worth flagging
  directly per this dossier's both-tails mandate.
- Open loop: reasonably closed (claim → mechanism → demo → practical next step).
- Pacing/captions: DATA GAP.

#### 4. Value proposition
- Walk-away value: **tool discovery** (a specific, free, named tool) with a **novelty/amusement** layer.
- Practical value class: tool discovery, but for a **narrow use case** (houseplant owners specifically
  interested in AI-diagnosed plant care) — a smaller addressable audience than "anyone with a brokerage
  account" (Video 2) or "anyone who follows AI news" (Videos 1, 4, 5).
- Specificity: MED-HIGH — concrete setup requirement (webcam, zero coding) but the "5-step setup" itself
  is gated behind the WhatsApp CTA, so the caption alone under-delivers relative to its promise more than
  the top-5 videos do.

#### 5. Psychology scoring
- STEPPS: **Practical Value** present but narrow-audience (a structural ceiling, not a psychology
  failure); weak **Social Currency** (a cute plant-tech demo doesn't confer "ahead of the curve" status
  the way an infrastructure-strategy or geopolitical story does); weak **Triggers** (houseplants are not
  a frequent-recurrence topic for this account's likely core audience of professionals/builders).
- Primary emotion: **amusement/whimsy** — technically a high-arousal-positive category per §2.3, but a
  **mild** version of it; the content reads more "cute" than genuinely delight-inducing, and this
  dossier's own read is that the emotional register is closer to low-arousal pleasantness than true
  amusement-as-defined-in-the-literature.
- Identity-signaling: LOW — sharing a plant-talks-to-you gimmick doesn't obviously make the sharer look
  smart, ahead, or plugged-in the way the account's news-driven content does.
- Save/send trigger: LOW-MED — narrow addressee ("send this to a specific plant-owning friend") is
  possible but a smaller slice of any given follower's network than the account's more universally-
  relevant videos.

#### 6. CTA & funnel mechanics
- "Full 5-step setup and link are inside my free WhatsApp community. Link in bio." — content-attached,
  not bare bait, consistent with the other 6 videos.
- No comment-bait mechanic.

#### 7. Replicability verdict
- Template: same tool-demo structure as Video 2, applied to a narrower/quirkier use case.
- Commodity vs. advantage: fully commodity; no unique advantage visible.
- Difficulty for Tangent: **HIGH** (tech-tool-demo genre, no transfer to an art-gallery brand) though the
  underlying lesson — **novelty/whimsy alone, without a broad-relevance trigger or status-signal, is not
  enough to clear this account's own median** — is a directly useful negative lesson for any creator,
  Tangent included: charming/cute content needs a broader hook than charm alone to travel.

#### 8. Why it lost — delta vs. the top 5
- Most load-bearing factor: **narrow addressable relevance**. Every top-5 video in this sample targets
  either a broad professional/finance trigger (Video 2), a broad AI-news-following audience (Videos 1, 4,
  5), or a universally-relatable inspiration story (Video 3, the highest like-rate). This video's subject
  (AI-diagnosed houseplants) is a smaller slice of even this account's own niche audience. Structurally,
  the video is **not obviously worse-built** than the top 5 (clean claim → mechanism → demo → CTA arc,
  same production format implied by the caption) — this is the clearest evidence in this dossier's
  sample that **topic selection/breadth of relevance, not execution quality, is the primary top-vs-flop
  delta** for this account, directly informing Section C's decomposition.

#### Sources
- instagram.com/reel/DbDltYAge31/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md

---

### VIDEO 7 (FLOP, rank 59/60 eligible — 0.55x median): "1.6 billion free tokens monthly" (OmniRoute)

#### 0. Identity & stats
- URL: instagram.com/reel/Dae05TSAK1l/. Posted **2026-07-06** `[OBSERVED]`. Length: DATA GAP for the IG
  original — see proxy note below.
- Views: **255K** `[OBSERVED, HIGH]`. Likes: **2,567** `[OBSERVED, HIGH]` (WebFetch read "2.6K," same
  figure). Comments: **171** `[OBSERVED, HIGH]` — the **2nd-highest raw comment count in the sample**
  despite being a flop by views, and the **highest comment-RATE of any of the 7 videos (0.067%)**, more
  than 4x the sample's next-highest comment-rate. Shares/saves: DATA GAP.
- Rank: **2nd-lowest of the eligible pool**, **0.55x median**.
- **Cross-platform proxy located**: this is the one video in the 7-video sample with a confirmed
  cross-posted equivalent — YouTube Short `Twpn72mPKTY`, "How to Get 1.6 Billion AI Tokens for FREE
  Every Month!" `[OBSERVED via yt-dlp]`, same underlying topic (OmniRoute, 1.6 billion free tokens),
  posted 2026-07-05 (one day before the IG version), 130,979 views / 8,021 likes / 1,500 comments on
  YouTube, 69 seconds long. This dossier obtained the **full auto-caption transcript** of the YouTube
  version and treats it as a proxy for the IG original's likely spoken content, **not as proof the two
  scripts are word-for-word identical** — logged explicitly as a proxy substitution per the assignment's
  instructions on cross-posted-copy hunting.

#### 1. Packaging
- IG caption/hook `[OBSERVED]`: "1.6 billion free tokens monthly. OmniRoute connects to 160+ AI models
  and auto-picks the cheapest one per task."
- YT proxy opening line `[OBSERVED via transcript]`: **"Stop paying for Claude, Cursor, or Codex. This
  one free tool runs all of them."** — note this is a **materially different hook** from the IG caption:
  the YT version leads with a direct pain-point/cost-savings claim naming specific competitor tools
  (Claude, Cursor, Codex), while the IG version leads with the token-count statistic. This is a genuine,
  observed cross-platform packaging difference, not an assumption.
- Curiosity gap: MED — "1.6 billion" is a large, attention-grabbing number but abstract until contextualized (few viewers have an intuitive sense of what a token is worth).

#### 2. Hook (0–3s)
- IG: `[INFERRED from caption]` "1.6 billion free tokens monthly."
- YT proxy `[OBSERVED via transcript]`: "Stop paying for Claude, Cursor, or Codex. This one free tool runs
  all of them. It's called Omni Route, and it's all over the internet right now."
- Hook taxonomy: **Result-first / stat-led** (IG) vs. **bold claim / pain-point-led** (YT) — two distinct
  taxonomy classes for what is likely the same underlying story, a useful illustration that this
  creator's team (or system) A/B-varies hook framing per platform rather than posting identical copy.
- What the viewer sees (YT only, `[OBSERVED]` from the downloaded thumbnail — Section D): direct-to-
  camera talking-head shot, seated, styled two-tier burned-in caption (bold sans-serif word + italic
  serif continuation), consistent branded room background.

#### 3. Structure & retention engineering
- Beat map, YT proxy `[OBSERVED via transcript, full text captured]`: [0:00] pain-point hook (stop paying
  for X/Y/Z) → [0:07] tool name reveal (OmniRoute) + social-proof claim ("all over the internet right
  now") → [0:11] mechanism (200+ models, auto-picks cheapest) → [0:16] key stat (1.6B free tokens/month
  via stacked free tiers) → [0:19–0:26] live A/B demo (same landing-page prompt run through Claude
  directly vs. through OmniRoute, "almost the same page," "75% fewer tokens") → [0:29] failover feature
  (silently switches models when one hits a limit) → [0:33] setup steps (install, connect free API, paste
  one link) → [0:40] value-close ("if you use AI for everything, you must try this") → [0:44] comment-
  bait CTA ("Comment models and I'll share you the complete setup guide") → [0:48] follow CTA → [0:50]
  WhatsApp-community CTA + link-in-bio.
- **Important platform-specific finding**: the **"Comment models and I'll share you the setup guide"**
  line appears in the YouTube proxy transcript but **does NOT appear** in this dossier's own WebFetch pull
  of the actual Instagram caption (which reads only "...I've put the full 3-step setup guide in my
  WhatsApp community. Link in bio" — no comment-keyword ask). If the IG version's spoken audio matches
  its caption (unconfirmed — DATA GAP, no IG transcript obtained), this suggests the **comment-bait
  mechanic may be YouTube-specific** for this story, not deployed identically on Instagram — which would
  make this video's own high IG comment-rate (0.067%, the sample's highest) **not** attributable to an
  explicit ask, but to the content itself (a cost-saving tool a technical audience has specific follow-up
  questions about) — logged as the more likely read given the caption evidence actually observed, with
  the alternative (an audio-only CTA absent from text) flagged as unresolved.
- One-idea-per-video: yes, single tool + live comparison demo, a **tighter demo-in-motion structure**
  than most of the top-5 videos (only Video 3 has comparably concrete
  step-by-step mechanics).
- Open loop: "does the cheaper router actually work as well?" opened early, closed by the live
  side-by-side demo — clean payoff.
- Pacing (YT proxy, `[OBSERVED]`): steady narration, "[music]" cue markers in the caption track
  suggesting cut points roughly every 3-8 seconds, consistent with dynamic pacing per §3.3.2.

#### 4. Value proposition
- Walk-away value: a genuinely **copyable workflow** (specific setup steps: install, connect free API,
  paste link) plus **cost savings** (75% fewer tokens claimed).
- Practical value class: **copyable workflow + tool discovery**, arguably the most concretely actionable
  video in the entire 7-video sample (the only one with a live before/after comparison demo).
- Specificity: HIGH — model count (160+/200+, minor IG-vs-YT discrepancy noted), token count (1.6B),
  cost-reduction percentage (75%), and explicit 3-step setup.

#### 5. Psychology scoring
- STEPPS: **Practical Value** dominant (a genuine cost-saving tool for a technical audience). **Social
  Currency**: LOW — this is niche/technical enough that sharing it signals technical-practitioner
  identity to a narrower audience than the account's broader AI-news content.
- Primary emotion: **low-arousal utility/relief** (cost anxiety resolved) rather than awe or amusement —
  similar emotional register to Video 2 (portfolio tracker), which also under-performed on likes despite
  reasonable views; here the pattern shows up as under-performing on VIEWS specifically.
- Identity-signaling: LOW-MED, narrower than the top-5's broader-appeal stories.
- Save/send trigger: HIGH for the specific technical sub-audience (developers/AI power users who'd want
  to reference the setup steps later) but that sub-audience is a **smaller slice of this account's total
  reach** than "anyone following AI news" — the same narrow-addressable-audience pattern identified in
  Video 6.

#### 6. CTA & funnel mechanics
- IG: "I've put the full 3-step setup guide in my WhatsApp community. Link in bio." — content-attached,
  compliant.
- YT (proxy only): adds an explicit comment-keyword mechanic ("Comment models...") ahead of the
  WhatsApp CTA — a §3.4.3 comment-automation-adjacent tactic, compliant since it's attached to real
  standalone content already delivered in the video, not a bare ask.

#### 7. Replicability verdict
- Template: pain-point hook (stop paying for X) → tool reveal + social proof → mechanism → hard stat →
  live before/after demo → failover/reliability feature → 3-step setup → CTA.
- Commodity vs. advantage: the underlying tool (OmniRoute) is third-party and equally coverable by any
  AI-tools creator; the **live side-by-side demo** is the one element requiring actual production effort
  (running two real prompts and comparing outputs) rather than pure narration — a small but real
  execution-quality edge over Videos 1, 2, 4, 5's caption-only structures.
- Difficulty for Tangent: **HIGH** — AI-developer-tool content has no natural analog for a fine-art
  gallery; the transferable piece is the **live-comparison-demo structure** itself (show A, show B,
  quantify the difference), which could map to, e.g., a before/after restoration or edit comparison in
  Tangent's own content.

#### 8. Why it lost — delta vs. the top 5
- Most load-bearing factor: **narrow addressable audience** (developers/AI-power-users who pay for
  Claude/Cursor/Codex specifically) is a smaller slice of a 2M-follower general-AI-interest audience than
  broad-relevance subjects like frontier-model news or geopolitical tech stories. Despite this, the video
  is **structurally the most rigorous of the sample** (only one with an actual live demo/comparison) and
  produced this sample's **highest comment-rate**, reinforcing Video 6's finding that **topic breadth,
  not execution quality or engagement-rate, is this account's primary top-vs-flop delta**. Secondary
  factor: the topic (an LLM-cost-routing tool) is adjacent to "inside baseball" for people who already
  pay for multiple AI subscriptions — a real but numerically smaller segment than "everyone curious about
  AI news."

#### Sources
- instagram.com/reel/Dae05TSAK1l/ (WebFetch, 2026-07-25)
- ig_harvest/vaibhavsisinty.md
- youtube.com/shorts/Twpn72mPKTY (yt-dlp metadata + transcript + thumbnail, 2026-07-25)

---

## C. Scale-with-efficiency decomposition (Central Question 1: how does 23.3% median/follower hold at 2M?)

This account ties for the **2nd-best median/follower ratio of any 1M+ follower account in this entire
24-account study** (behind only `realrileybrown` at 328K followers and `kallaway`/`tiffintech`, all
substantially smaller accounts — see `00_INDEX.md` quick-ranking). At 2M followers this is a genuine
outlier: most large accounts in this study decay toward single-digit-percent ratios as follower count
grows (e.g. `danmartell` at ~3M followers sits at 3.5%; `chrisdonnellyofficial` at 808K sits at 1.4%).
Decomposing the evidence gathered above into the factors that plausibly explain this:

1. **Near-daily posting cadence, independently computed from real dates, not estimated.** Using the
   7 confirmed post dates from this dossier's own sample (Jun 1 → Jul 21, spanning 51 grid positions
   across 50 calendar days = **0.98 days/position, essentially 1 reel/day**), this is one of the more
   rigorously-cadence-confirmed accounts in the study (see the position→date table in Section D). Video
   5's own caption independently claims "I break down stuff like this every day," `[OBSERVED, self-
   report]`, corroborating the date-derived math. Per §3.4.1 `[INDUSTRY DATA]`, high-and-consistent
   cadence correlates with faster growth, and per §2.4.2 `[RESEARCH-BACKED]` mere-exposure effect, high
   frequency of a consistent format/persona compounds liking/familiarity — both mechanisms this account's
   cadence would activate more than a lower-frequency account.
2. **A template that trades production cost for volume, not quality for volume.** All 7 post-mortems show
   the same underlying beat structure (bold-claim-or-result-first hook → 3-5 concrete facts → CTA),
   regardless of subject matter, letting a small team (or an AI-assisted pipeline, per the creator's own
   claims in Section A) produce daily output without each video requiring bespoke creative development.
   This is the same "cheap-to-produce, reliably-clears-a-floor" dynamic documented for the news-roundup
   hero format in `yt_nateherk.md`'s Section D, here operating at roughly 7x that account's cadence.
3. **Topical timeliness as a built-in Trigger/relevance mechanism.** Every one of the 5 top videos covers
   a recent, real-world news event (a product launch, a regulatory approval, a benchmark release) — this
   means the content is inherently plugged into whatever the audience is already seeing elsewhere that
   week (§2.2 Triggers), without requiring the creator to manufacture novelty from nothing.
4. **A soft, content-attached CTA design that stays compliant.** None of the 7 videos uses bare
   engagement bait (§1.3.2) — every CTA is attached to genuine promised content (a fuller list, a setup
   guide, a prompt playbook). This keeps the account outside Instagram's explicitly-stated "less visible"
   penalty categories (§1.3.1/1.3.2), which several other lower-ratio accounts in this study were NOT
   found to consistently avoid.
5. **The ratio is NOT explained by uniformly-high per-post engagement.** Section B's granular data shows
   real variance: top-5 like-rates ranged from 0.77% to 3.62% (a 4.7x spread) and the two flops (0.88%,
   1.01%) actually **overlap** with the weakest top-5 video rather than sitting in a cleanly separate
   tier — a finding the primary IG harvest file's own detail-pull note flagged and this dossier's
   post-mortems independently corroborate. **The evidence points to topic BREADTH (how large a slice of
   a 2M-strong, heterogeneous audience a given subject is relevant to) as the dominant top-vs-flop lever,
   not execution quality or on-post engagement-rate** — both flops (Section B, Videos 6-7) were
   structurally comparable to or, in Video 7's case, more rigorously built than several top-5 videos, but
   covered narrower-interest subjects (houseplant AI, developer-tool cost routing) vs. the top 5's
   broad-relevance subjects (finance, major-platform strategy, human-interest, frontier-AI, geopolitics).
   `[INFERRED]`, reasoning shown, from the 7-video sample directly.
6. **Caveat on causal certainty**: this decomposition is built from 7 videos, not a full-catalog sweep
   (unlike, e.g., `yt_nateherk.md`'s 164-video census) — the "topic breadth over execution quality" and
   "near-1-post/day cadence" findings are well-evidenced within this sample but not verified against the
   account's full ~60-tile-or-larger catalog. Treat as a strong, evidence-backed hypothesis, not a
   fully-audited causal claim.

---

## D. Content architecture: key vs. filler, cadence, production system

**Cadence (Central Question 1 support, `[OBSERVED]`, computed this session):**

| Grid position | Shortcode | Date | Views |
|---|---|---|---|
| 57 | DZEpQ9cgEik | 2026-06-01 | 1.3M |
| 53 | DZK-XJ-AIZK | 2026-06-04 | 1.7M |
| 46 | DZaRmD9A9eF | 2026-06-10 | 1M |
| 43 | DZfrPXIgXCp | 2026-06-12 | 983K |
| 27 | DaNu_sMAVD_ | 2026-06-30 | 1.3M |
| 21 | Dae05TSAK1l | 2026-07-06 | 255K |
| 6 | DbDltYAge31 | 2026-07-21 | 200K |

Position-to-position deltas range 0.67–1.13 days/position across the sample, averaging **~0.98 days/
position over the full 51-position, 50-day span** — a tighter, more consistent cadence than several other
accounts in this study where cadence had to be estimated from sparse samples (contrast `yt_nateherk.md`,
where 5 of 14 cadence probes hit rate-limits and were never recovered). This account's cadence claim rests
on 7 out of 7 successful date pulls with no gaps, though it should be noted these 7 were selected because
they were the top-5/flop-2 targets, not a random sample — the true across-the-board cadence could vary at
positions between these 7 (a between-samples-interpolation caveat, not a data gap in the pulls themselves).

**Key vs. filler, `[INFERRED]` from the 7-video sample's subject-matter spread:**
- **Key format** (drives the top-5 ranks): broad-relevance AI/tech news — frontier-model releases,
  major-platform strategic moves, geopolitical tech competition — framed with a bold-claim or "nobody's
  talking about it" hook.
- **Secondary/high-ceiling format**: human-interest invention stories (Video 3) — smaller sample size in
  this dossier (n=1) but the single best like-rate and highest raw comment count, suggesting this may be
  an under-leveraged high-ceiling format rather than filler — flagged as a hypothesis for a fuller-catalog
  follow-up, not confirmed at scale here.
- **Filler/floor-risk format**: narrow-audience tool demos (plant diagnostics, AI-router cost tools) —
  both flops in this sample fall here, despite one (Video 7) being the most rigorously-produced video of
  the seven.

**Production system (Central Question 3 — "zero camera days," `[REPORTED, self-source]` + `[OBSERVED]`
visual corroboration):**
- Vaibhav Sisinty's own Instagram post (`DNGh28v0Tof`, `[OBSERVED via WebFetch]`) states 99% of his
  content across an 800K-follower, 8-month growth run was "AI-generated. The voice. The videos. My AI
  clone." A separate LinkedIn post (`[OBSERVED via WebFetch]`) states he uses "my AI clone to ship long
  form videos on AI updates every week on YouTube," describing it as effortful ("a lot right now") but
  functioning.
- This dossier independently downloaded and visually inspected **two YouTube-catalog thumbnails**
  (`Twpn72mPKTY` and `6UR-EXqeNW4`, `[OBSERVED]`, images captured and reviewed directly): both show a
  **consistent recurring on-camera persona** (same face/beard/build) delivering direct-to-camera
  narration, in two different rooms/outfits, with two visually distinct burned-in-caption styles (a
  tighter two-tone bold-sans + italic-serif style in one; a bold all-caps sans style in the other) —
  suggesting either multiple filming sessions/locations, or a versatile avatar system capable of varied
  backgrounds, or some mix of both. **This dossier cannot forensically distinguish a real human recording
  from an AI-generated clone from still frames alone** — flagged explicitly as a DATA GAP rather than
  asserted either way. The recurring-persona-across-varied-settings pattern is consistent with, but does
  not prove, the creator's own "AI clone" claim.
- **Functional read**: whether the on-camera delivery is a real recording or a synthetic clone, the
  **script/structure production is almost certainly heavily systematized** — the near-1/day cadence
  (Section C) combined with the highly consistent beat structure across all 7 post-mortems (hook →
  3-5 facts → CTA, regardless of subject) is difficult to sustain via fully bespoke human scripting at
  this frequency without either a sizable writing team or an LLM-assisted drafting pipeline (or both).
  `[INFERRED]`, reasoning stated, consistent with but not proof of the "zero camera days" framing.
- **Cross-platform CTA infrastructure**: the YouTube proxy video's description names the actual tool
  behind the "WhatsApp community" CTA repeated in every one of the 7 IG captions —
  `join.switchit.app/YT`, a third-party WhatsApp-broadcast/community tool `[OBSERVED]`. This is the same
  link-in-bio destination implied across the IG sample, confirming the funnel infrastructure is shared
  cross-platform, not platform-bespoke.
- **Honesty/credibility context** `[REPORTED]`, LOW-MED confidence, relevant to interpreting all AI-hype
  claims in this genre: consumer-review aggregation (Quora, a review-aggregator site, both surfaced via
  WebSearch, not independently audited by this dossier) includes user complaints that some GrowthSchool/
  Sisinty-branded live workshops were "pre-recorded and advertised as live, with staged fake
  interactions," and that AI-utility claims in some paid-funnel training sessions are "exaggerated."
  This dossier did not verify these specific allegations directly (no workshop was attended), but flags
  them as relevant background for weighing this creator's self-reported production claims and this
  genre's specific benchmark/capability claims (e.g. Video 4's unverified "80% vs 58%" coding-benchmark
  citation) at appropriately calibrated confidence rather than at face value.

**Central Question 4 — India-global positioning:**
- The 7-video sample itself is **globally-framed by subject matter** (Microsoft, Google, OpenAI, China,
  a US-vs-China neurotech story) and delivered in English throughout, targeting a broad international
  AI/tech-interested professional audience rather than an India-specific one.
- However, two concrete India-specific signals surfaced: (1) Video 1's transcription-language list
  specifically calls out "43 languages **including Hindi**" rather than leaving it generic, a small but
  deliberate India-relevant detail inside an otherwise globally-framed story; (2) a broader sweep of this
  creator's ~450-video YouTube Shorts catalog (Section E) surfaced multiple explicitly India-framed
  titles not present in this dossier's 7-video IG sample — e.g. *"Every Indian Phone Brand Died... Except
  This ONE!"*, *"How This Farmer Built a ₹7 Crore Farm Using ChatGPT!"*, *"This 20-Year-Old Indian Boy
  Crushed Jeff Bezos' Big Secret Project!"* `[OBSERVED]`, titles only, not analyzed as full post-mortems
  (out of this dossier's 7-video scope) — establishing that India-specific human-interest content is a
  real, recurring part of this creator's broader catalog, layered on top of (not instead of) the
  globally-framed AI-news core.
- `[INFERRED]` synthesis: the account's core identity is **globally-relevant AI/tech news for an
  English-speaking professional audience**, with India-specific stories used as a **recurring flavor/
  segment within that frame** (national-pride tech achievements, India-relevant product details) rather
  than as the account's primary organizing identity. **Implication for the owner's own audience-targeting
  choices**: this suggests a viable pattern for a niche (art/fine-photography) account is to organize
  around a **globally-portable core topic/format** and use origin/locale-specific stories as periodic,
  not dominant, content — rather than building the entire identity around a single geography, which would
  cap addressable audience size the way this dossier's Section C found narrow-topic videos (plants,
  developer tools) capped view counts even when well-executed.

---

## E. Method log

**Context research (before re-reading the primary harvest file, per the brief's sequencing instruction):**
WebSearch queries run: GrowthSchool business model/funnel, GrowthSchool funding/revenue, "zero camera
days," AI clone/production system, OutSkill funding/scale, India/global positioning signals, LinkedIn
follower count, and a dedicated critical/skeptical-coverage sweep ("scam," "hype," "fake claims") per the
QC protocol's implicit both-sides-of-the-story expectation. WebFetch calls: `inc42.com/company/growth-
school`, `theexecutiveindia.com` (returned empty/blank — logged as a failed fetch, not substituted
silently), `sigmastory.in` (OutSkill/GrowthSchool relationship piece), `home.growthschool.io/mentors/
vaibhav-sisinty` (failed — TLS/SSL error, logged, not retried given a working alternative source already
in hand), the `linkedin.com/pulse/...` GrowthSchool-playbook article, and two `linkedin.com/posts/...`
posts (one on AI-content strategy, one on the "AI clone" claim — both returned readable text via
WebFetch despite LinkedIn's typical login-wall, apparently because these are public posts with
server-rendered preview text).

**Primary data:** `ig_harvest/vaibhavsisinty.md` re-read after context research, per instructions — the
"Detail pulls (supplementary harvest)" section had landed (7-row table, top-5 + 2 flops) by the time this
dossier reached Section B. Used as the primary source for all views/likes/comments/dates in Section B.

**Independent cross-check:** this dossier separately ran `WebFetch` against all 7 individual reel URLs
(`instagram.com/reel/<shortcode>/`) before discovering the primary harvest's detail-pull table had
already landed, and kept both pulls rather than discarding the redundant one — the two independently-
sourced pulls (browser-agent grid tool vs. this dossier's own WebFetch) agreed on every caption and date,
and agreed on likes/comments within normal K-rounding tolerance in every case, which is reported inline
per-video as a genuine corroboration rather than a single-sourced number.

**YouTube cross-post hunt (`[OBSERVED]`, yt-dlp, per the brief's explicit instruction to hunt cross-posts
for transcript-level detail):**
1. `yt-dlp --flat-playlist --playlist-items 1:450 --print "%(id)s | %(view_count)s | %(title)s"
   "youtube.com/@vaibhavsisinty/shorts"` in three batches (1:60, 61:250, 251:450) — all succeeded, no
   rate-limiting encountered, 450 rows collected; a further batch (251:450 confirmed 200 more rows
   existed) indicates the true catalog size exceeds 450 — this dossier stopped the sweep at 450 given
   time-budget constraints, logged as a floor not an exact total.
2. Keyword-swept the full 450-title catalog for topic matches to all 7 of this dossier's target reels
   (Microsoft/NVIDIA, Google Finance/portfolio, algae exhaust filter, "most powerful AI," China/
   Neuralink/NEO, plant-talk/houseplant, and the 1.6-billion-token OmniRoute story). **Exactly one exact
   topic match found**: `Twpn72mPKTY` ("How to Get 1.6 Billion AI Tokens for FREE Every Month!") matching
   Video 7 (`Dae05TSAK1l`). The other 6 target reels had **no confirmed cross-posted YouTube equivalent**
   within the 450-video sweep — logged as a genuine data gap, not silently skipped; it is possible these
   6 stories exist further back in the catalog (beyond position 450) or were IG-exclusive content, neither
   of which this dossier could confirm within its time budget.
3. For the one match: full metadata pull (`--print` for views/likes/comments/date/duration), full
   description pull (surfaced the `join.switchit.app/YT` WhatsApp-tool link, used in Section D), and
   `--write-auto-subs --sub-langs "en.*" --sub-format vtt` — succeeded on the first attempt, transcript
   de-duplicated via a Python script stripping VTT rolling-caption repeats (same technique documented in
   `yt_nateherk.md`), used to build Video 7's full beat map with real timestamps.
4. Thumbnail visual inspection: `yt-dlp --write-thumbnail --skip-download` for `Twpn72mPKTY` and a second,
   unrelated catalog video (`6UR-EXqeNW4`), converted `.webp` → `.png` via macOS `sips`, and read directly
   with the image-reading tool — both confirmed a consistent recurring on-camera persona (Section D).
   This is the one piece of genuinely `[OBSERVED]` (not caption-inferred, not self-reported) visual
   evidence in this dossier about the account's production format.
5. **LinkedIn video-extraction attempt** (per the brief's instruction to also hunt LinkedIn cross-posts):
   `yt-dlp` against the "AI clone" LinkedIn post URL — **failed**: `ERROR: [LinkedIn] ... Unable to
   extract video`. LinkedIn's extractor generally requires an authenticated session for feed video content
   that this dossier did not have; logged as a confirmed, attempted-and-failed data-access constraint
   rather than skipped without trying, consistent with `QC_PROTOCOL.md`'s "known data-access constraints"
   framing for platforms that block unauthenticated access.

**Known data gaps (not fabricated, not silently skipped):**
- **No frame-level visual capture for any of the 7 Instagram reels themselves** — Instagram video files
  were not downloadable via the tools available in this session (no browser tool, no working IG-specific
  yt-dlp path attempted/available); all "what the viewer sees" observations in Section B are marked DATA
  GAP, and the one piece of visual evidence used in Section D comes from two YouTube-catalog videos, not
  the analyzed IG reels — explicitly flagged as an analog, not direct evidence, everywhere it's used.
- **No exact duration for any of the 7 IG reels** — Instagram does not expose this via WebFetch-accessible
  page content; only the one YouTube proxy (Video 7, 69s) has a confirmed duration.
- **Only 1 of 7 target reels has a confirmed cross-posted transcript** (Video 7) — the other 6 videos'
  "beat maps" in Section B are explicitly labeled `[INFERRED from caption]`, since the caption is treated
  as a plausible (not confirmed) proxy for the spoken structure, distinct from `[OBSERVED via transcript]`
  tier claims.
- **Shares/saves counts** were not obtainable for any of the 7 videos by any method available (a
  structural Instagram limitation, not a tooling failure specific to this dossier).
- **GrowthSchool/OutSkill revenue and learner-count figures are founder-self-reported or third-party-
  aggregator-sourced (Tracxn), not independently audited** — flagged at MED/MED-LOW confidence throughout
  Section A rather than treated as verified fact.
- **This dossier's WhatsApp-community-to-paid-product funnel hop is `[INFERRED]`, not observed** — no
  reel in the sample names a specific paid product, and this dossier did not (and could not, without
  entering personal contact information into a WhatsApp opt-in, which is out of scope for a research
  pass) join the community to confirm what happens after opt-in.
- **The account's own follower count (2M) and total-post count (3,956) were carried forward from an
  earlier prototype pull, not re-verified this session** — flagged MED confidence in Section A rather
  than silently treated as this dossier's own fresh observation.

**No-fabrication check:** every numeric claim in Sections B and C traces to either the primary harvest
file's detail-pull table, this dossier's own `WebFetch` re-pulls (cross-checked against the harvest table
value-by-value), a specific `yt-dlp --print` output or downloaded transcript/thumbnail file in this
session's scratch directory, or a specific cited press URL — with `[INFERRED]` reasoning stated inline
everywhere a claim goes beyond directly observed evidence.
