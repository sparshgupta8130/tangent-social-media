# Creator Dossier: Skill Leap AI (YouTube @SkillLeapAI)

**Prepared:** 2026-07-25 | **Analyst method:** yt-dlp direct fetch (no third-party aggregator) | **Protocol:** QC_PROTOCOL.md, video_postmortem_template.md, 03_virality_science.md

**The puzzle this dossier solves:** Skill Leap AI's single biggest YouTube Short (~1.03M views) is an off-topic iPhone-settings tip, while its best AI-specific Short — the channel's actual subject matter — sits at ~62.5K, a **16.4x gap**. This dossier diagnoses that gap using the channel's full Shorts catalog (30 videos, a full population, not a sample) plus 11 deep-dive post-mortems.

---

## A) Channel header

- **Handle / Channel ID:** @SkillLeapAI / `UCwSozl89jl2zUDzQ4jGJD3g` [OBSERVED, yt-dlp, 2026-07-25, HIGH]
- **Subscribers:** 335,000 [OBSERVED via `channel_follower_count` field, yt-dlp fetch of a channel video, 2026-07-25, HIGH]
- **Channel bio (verbatim, current)** [OBSERVED, yt-dlp `--print description` on channel root, 2026-07-25, HIGH]:
  > "Stay on the cutting edge of AI! I share the latest AI tools, models, and tips with easy tutorials and reviews. Learn AI step by step with Skill Leap by Futurepedia—our full library of AI courses. Start your 7-day free trial: https://bit.ly/skill-leap. Subscribe to keep up with the AI revolution! For sponsorships: saj@skillleap.ai"
- **Total Shorts catalog:** 30 videos — this is the **entire population**, not a sample. Confirmed twice: `--flat-playlist --playlist-items 1:150` returned exactly 30 rows, and an uncapped `--flat-playlist` sweep also returned exactly 30 rows with zero errors. [OBSERVED, yt-dlp, 2026-07-25, HIGH]
- **Total long-form videos:** ≈329 (flat-playlist count of `/videos` tab) [OBSERVED, yt-dlp, 2026-07-25, HIGH]. Long-form is clearly the channel's dominant format by volume (329 vs 30 Shorts, an ~11:1 ratio).

### Median Shorts views — split AI-topic vs general-tech

Of the 30 total Shorts, 24 are AI-topic (ChatGPT, Gemini, Claude, AI agents, AI image/video tools) and 6 are general-tech/off-topic (4 iPhone-tips videos, 1 "new laptop for the AI age" hardware spot, 1 Nvidia CES recap) [OBSERVED, classified from titles across the full 30-video sweep, 2026-07-25, HIGH].

| Segment | n | Median views | Notes |
|---|---|---|---|
| **All 30 Shorts** | 30 | 6,200 | avg of ranks 15–16 (6,400 / 6,000) |
| **AI-topic Shorts** | 24 | 6,400 | avg of ranks 12–13, both exactly 6,400 |
| **General-tech Shorts** | 6 | 5,600 | avg of ranks 3–4 (5,700 / 5,500) |

[OBSERVED — computed directly from the full 30-row view-count sweep, 2026-07-25, HIGH confidence in the arithmetic; classification of "AI-topic" vs "general-tech" is [INFERRED] from title/hashtag content, a low-ambiguity call for all 6 general-tech videos]

**The critical nuance visible here:** the AI-topic median (6,400) and general-tech median (5,600) are *close* — general tech is not a broadly stronger topic class on this channel. The entire "off-topic wins" story is driven by exactly **two outlier videos** (1.03M and 151.6K views), not by general-tech content performing better on average. This reframes the whole diagnosis — see Section C.

### Top/median ratios
- Top video (1,028,157) vs all-Shorts median (6,200): **165.8x**
- Top video (1,028,157) vs best AI-specific Short (62,512): **16.4x** — matches the brief's framing
- Best AI-specific Short (62,512) vs all-Shorts median (6,200): **10.1x** — even the AI ceiling itself is a big outlier over typical AI performance on this channel

### Cadence
- **Long-form:** using two confirmed upload-date anchors within the 25 most recent long-form videos (`WCuwYLVE6j8` = 2026-03-19, `AxRprCFZBU8` = 2026-03-27, both [OBSERVED, yt-dlp, 2026-07-25, HIGH]) and the channel-page ordering (newest-first), 25 videos span roughly 2026-03-19 to 2026-07-25 (~128 days) → **≈1 long-form upload every 5.1 days, roughly 2x/week** [INFERRED from 2 anchor dates + list-order assumption, MED confidence — see Method Log data gap].
- **Shorts:** of the 11 Shorts this dossier dated directly, upload dates cluster into two eras: 2021-11-03 and 2021-12-18 (the two off-topic hits, pre-AI-pivot), then a burst of 7 shorts between 2023-02-06 and 2023-05-29 (right after ChatGPT's Nov 2022 public launch), then near-silence: one Short on 2024-12-26 and one on 2025-10-08. [OBSERVED for these 11 dates, HIGH; the remaining 19 of 30 Shorts could not be individually dated — see data gap in Method Log]. **Shorts are not a sustained format for this channel** — see Section D.

### Funnel map
YouTube (long-form tutorials, 2x/week + occasional Shorts) → channel bio link `bit.ly/skill-leap` → **Skill Leap by Futurepedia** (skillleap.ai / skillleap.futurepedia.io), a subscription AI-course platform with a stated 7-day free trial, month-to-month, cancel-anytime [REPORTED, Futurepedia/Skill Leap marketing copy via WebSearch, 2026-07-25, MED — vendor's own claims, not independently verified]. Secondary funnel branch: sponsorship inbound (`saj@skillleap.ai` in bio) — several catalog videos carry `#ad` or brand-partner hashtags (e.g., `#LTXStudiopartner`, `#nvidiapartner`) [OBSERVED, titles in the 30-video sweep, HIGH]. No Shorts in the analyzed set carry an explicit course/link-in-bio CTA inside the video itself — the funnel lives at the channel level (bio link), not embedded per-Short.

### Channel-identity finding (material to the whole dossier)
Skill Leap AI appears to be a **rebrand of a prior general-tech channel called "Howfinity."** Evidence: (1) [OBSERVED, HIGH] the description of the #1 video (`qI2_v_xWGX4`) — fetched directly via yt-dlp — links to `howfinity.com`, not any Skill Leap/AI property; (2) [REPORTED, MED, via WebSearch] Skill Leap AI's Instagram handle is `@howfinity_tech`; (3) [REPORTED, MED, via WebSearch] a Facebook post from Howfinity's own page reads "Exciting news! Skill Leap AI, our new AI learning platform is live" (facebook.com/howfinity/photos/...). No primary source gave an exact rebrand date; the [OBSERVED] upload-date clustering above (two 2021 general-tech Shorts, then a hard break to AI content starting Feb 2023) is consistent with a pivot occurring sometime between Dec 2021 and Feb 2023. This matters directly for Section C: the two viral outliers were not produced under the same channel identity/strategy as the current AI-tutorial mission — they are a holdover from a different channel.

---

## B) Video post-mortems

Selection logic per QC_PROTOCOL/task brief: top 8 by views (includes both off-topic outliers) + general-tech median representative + 2 flops = 11 videos, drawn from the full 30-video population.

---

### VIDEO 1: "How to Check if iPhone is Refurbished or New or Personalized"

#### 0. Identity & stats
- URL: youtube.com/shorts/qI2_v_xWGX4 | Platform: YouTube Shorts | Posted: 2021-12-18 | Length: 51s
- Views: 1,028,157 | Likes: 34,122 (3.32% of views) | Comments: 374 (0.036% of views) — [OBSERVED, yt-dlp direct fetch, 2026-07-25, HIGH]
- Rank: **#1 of 30** in the channel's full Shorts catalog. 165.8x the all-Shorts median, 16.4x the channel's best AI-specific Short. The single largest outlier on the channel by a wide margin (next-highest is 6.8x smaller).

#### 1. Packaging
- Title: "How to Check if iPhone is Refurbished or New or Personalized" — front-loads the exact payoff and audience (anyone who owns/is buying an iPhone).
- Per rubric §1.2.3, thumbnail/title packaging is largely moot for Shorts (99.9% of views come from the feed, not a click on a title) — so the in-video hook, not this title, is the real selection mechanism. Still worth noting the title itself states the full value proposition with no curiosity-gap withholding, which is consistent with how the in-video hook operates (see below).
- Description [OBSERVED]: explains the settings path and closes "Please share and subscribe... See more, easy to follow how-to videos https://howfinity.com" — confirms this is Howfinity-branded content living on the now-renamed channel.

#### 2. Hook (0–3s)
- Verbatim: **"Here's another iPhone trick you're going to find super useful."** [OBSERVED via transcript, 0:00–0:03]
- Taxonomy: bold-claim / practical-value hook, not a curiosity-withholding hook — it states plainly that a useful trick is coming. The word "another" signals this is part of a recurring iPhone-tricks series (consistent with the Howfinity tips-channel format).
- What the viewer sees: a talking-head/screen-recording hybrid — presenter's phone screen with live narration, no logo or preamble before the hook line starts at 0:00.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:03) → Setup/navigation ("Settings > General > About", 0:03–0:20) → Core reveal: what the model-number first letter means (0:20–0:47) → Close/practical instruction ("make sure it's M and not F, N, or P", 0:47–0:51).
- Open loop: "this actually tells you something very important about your phone" (0:16) is planted early and resolved through a 4-item mini-list (F/M/N/P) — closes cleanly by the end, no dangling threads.
- One idea per video: yes — a single decoded fact (model-number-letter meaning), delivered as a compact 4-item list within that one idea (listicle-within-one-idea, compliant with rubric §3.2).
- Pacing: static screen-recording of Settings app with voiceover, minimal visual cuts — pacing is low-dynamism by rubric §3.3.2 standards, but the content itself (settings navigation) has no need for cuts since it's a single continuous action.
- Loop/rewatch design: none — a factual reference video, not built for rewatch, built for **save/send** instead (see below).

#### 4. Value proposition
- Walk-away value: a specific, checkable fact (interpret iPhone model-number letter codes) with immediate applicability — checks the box on "practical value" hard.
- Value class: pure copyable workflow / reference fact.
- Specificity: high — exact letters (F/M/N/P) and exact meanings given, not vague gesturing. This is the single most "specific and useful" hook in the entire sample.

#### 5. Psychology scoring (against 03_virality_science.md)
- STEPPS: **Practical Value** — very high; this is textbook "news you can use," protects a viewer from being scammed on a used/refurb purchase. **Triggers** — very high; every iPhone buyer eventually checks this, an extremely frequent, evergreen real-world cue (buying/receiving any iPhone, new or used). **Social Currency** — moderate; sharing this before a friend buys a used phone signals helpfulness/savvy. **Emotion** — the register is protective/anxiety-resolving rather than pure awe; moderate arousal (§2.3: anxiety-adjacent content is share-favorable, though weaker than anger/awe).
- Primary emotion + arousal: mild anxiety-resolution / protective utility, moderate arousal.
- Identity-signaling share motive: sharing this makes the sharer look protective/informed ("I'm looking out for you before you get scammed").
- Save/send trigger: extremely high and highly specific — there is a natural, nameable addressee ("send this to my mom before she buys that used iPhone off Marketplace"), exactly the §1.1.2/§2.7 marker for send-worthy content.

#### 6. CTA & funnel mechanics
- No in-video CTA. Description carries a generic "share and subscribe" ask plus a link to howfinity.com (not the current Skill Leap course funnel) — confirming this predates the current funnel design.
- Comment-bait mechanics: none present.
- Funnel position: pure top-of-funnel legacy content; does not feed the current AI-course funnel at all.

#### 7. Replicability verdict
- Extractable template: (1) pick a mainstream device everyone owns, (2) find one specific, checkable, protective fact about it, (3) state the payoff in the title/hook with zero gatekeeping, (4) demonstrate the exact navigation path on-screen, (5) close with an actionable checklist.
- Commodity vs unfair advantage: fully commodity — requires no AI expertise, no proprietary tool access, no unique voice. This is exactly why it's replicable by (and was likely inspired by) countless generic tech-tips channels.
- Difficulty for Tangent: **LOW** to execute mechanically, but **structurally irrelevant** — Tangent's mission is AI-specific; manufacturing an "iPhone trick" short is off-mission even if it would work.

#### 8. Why it won
The single most load-bearing factor is **topic universality colliding with a near-zero curiosity-gap cost**: literally every iPhone owner is in the addressable audience, and the hook requires no prior context to understand the stakes. Secondary factors: (a) this is one of the two oldest Shorts in the entire catalog (posted Dec 2021, within months of YouTube Shorts' broad US rollout), giving it ~4.5 years of algorithmic and organic compounding that no AI-topic Short (all 2023+) has had; (b) it was produced under a different channel identity (Howfinity, a general-tech tips brand) whose format was purpose-built for exactly this kind of universal trick content, not retrofitted AI content. Luck/timing component: posting during Shorts' early-growth period, when the format itself was being aggressively pushed by YouTube to build adoption (per rubric §1.2.2, unknown/small-affinity-cohort content could spike disproportionately in a less saturated feed).

#### Sources
- https://www.youtube.com/shorts/qI2_v_xWGX4 (metadata, description, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 2: "iPhone hidden camera setting camera you should know!"

#### 0. Identity & stats
- URL: youtube.com/shorts/r2PM5Z7ZG5I | Posted: 2021-11-03 | Length: 60s
- Views: 151,634 | Likes: 2,873 (1.89%) | Comments: 33 (0.022%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#2 of 30**. This is the *older* of the two off-topic hits (predates Video 1 by six weeks) — the single oldest Short in the whole catalog.

#### 1. Packaging
- Title promises "three hidden settings almost no one knows about" — insider-knowledge framing baked into the title itself.
- No description text captured [OBSERVED — description field empty on fetch].

#### 2. Hook (0–3s, extends to ~6s here)
- Verbatim: **"Your iPhone's camera has three hidden settings that almost no one knows about, let me show you how they work."** [OBSERVED via transcript, 0:00–0:06]
- Taxonomy: "nobody talks about X" / hidden-secret hook (rubric §3.1) — explicit insider-knowledge framing, a stronger Social Currency lever than Video 1's plainer "here's a trick" framing.
- Viewer sees: presenter's Camera app / Photos app screen recording, live demo starting immediately.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:06) → Setup: enable Live Photos (0:06–0:20) → Payoff 1/3: Loop effect demo (0:20–0:41) → Payoff 2/3: Bounce (0:41–0:47) → Payoff 3/3: Long Exposure (0:47–0:58) → Close: "these are really cool if you use them the right way" (0:58–0:60).
- Listicle-of-3 structure with drip payoff — each of the "three hidden settings" promised in the hook is revealed sequentially, closing all three loops the hook opened. Strong compliance with rubric §2.6.1 (multiple loops opened, all resolved before the end).
- Pacing: low-dynamism (single continuous screen recording, no cuts), same profile as Video 1.

#### 4. Value proposition
- Walk-away value: three specific Live Photo effects (Loop/Bounce/Long Exposure) with a demonstrated use case (Loop = "if you have kids running around it looks pretty cool").
- Value class: tool discovery (native iOS feature most users don't know exists) + creative/aspirational (fun output).
- Specificity: high — three named settings, demonstrated live, not described abstractly.

#### 5. Psychology scoring
- STEPPS: **Social Currency** dominant — "almost no one knows about" is a direct in-video insider-knowledge claim, the strongest §2.2/§2.5 marker in the entire sample. **Practical value** + **aspirational/creative** value both present (functional AND fun). **Triggers**: every iPhone camera user is a plausible trigger-context, extremely broad and frequent.
- Primary emotion: mild amusement/delight ("looks pretty cool") — moderate arousal, positive valence.
- Identity signal: sharer looks tech-savvy/ahead-of-the-curve for surfacing a "hidden" feature.
- Save/send trigger: high — a specific "you have to see this" moment, especially addressable to parents (the Loop-with-kids example gives a built-in addressee).

#### 6. CTA & funnel mechanics
- No CTA present in transcript or description.
- Funnel position: legacy top-of-funnel, disconnected from the current AI-course funnel, same as Video 1.

#### 7. Replicability verdict
- Template: (1) name a specific count of hidden features ("three hidden settings"), (2) claim insider/rare knowledge explicitly in the hook, (3) demonstrate each in sequence with immediate visual payoff, (4) close with a light creative-use suggestion.
- Commodity: fully commodity, no proprietary access needed — Apple's own native feature.
- Difficulty for Tangent: **LOW** mechanically, **off-mission** for the same reason as Video 1.

#### 8. Why it won
Same core mechanism as Video 1 (topic universality + zero-context hook + early-Shorts-era timing, oldest video in the catalog), amplified here by an explicit, stronger Social-Currency claim ("almost no one knows"). It under-performs Video 1 by 6.8x despite being older — the delta is likely explained by Video 1's stronger protective/anxiety-resolving value proposition (avoiding a scam) versus this video's more purely aspirational/fun value proposition; per rubric §2.3, protective/anxiety-adjacent content and pure delight are both share-favorable, but the scam-protection angle in Video 1 may carry a sharper, more specific addressee ("don't get scammed") than "this is a fun camera trick."

#### Sources
- https://www.youtube.com/shorts/r2PM5Z7ZG5I (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 3: "ChatGPT 4 is now live! 3 biggest upgrades" — BEST AI-SPECIFIC SHORT

#### 0. Identity & stats
- URL: youtube.com/shorts/6WVddn7qieU | Posted: 2023-03-14 | Length: 44s
- Views: 62,512 | Likes: 1,286 (2.06%) | Comments: 26 (0.042%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#3 of 30 overall, #1 among the 24 AI-topic Shorts.** This is the channel's on-mission ceiling.
- Note: 2023-03-14 is GPT-4's actual public-launch date — this video was posted the **same day** as the news event it covers. [OBSERVED upload date; GPT-4 launch date is common public knowledge, not separately re-verified here]

#### 1. Packaging
- Title: "ChatGPT 4 is now live! 3 biggest upgrades" — news-drop + listicle framing, both payoff-forward.

#### 2. Hook (0–3s, extends to ~7s)
- Verbatim: **"ChatGPT-4 just rolled out right now and these three upgrades are gonna blow your mind."** [OBSERVED via transcript, 0:00–0:07]
- Taxonomy: bold-claim/breaking-news hook + explicit listicle promise ("three upgrades"). "Blow your mind" is deliberate arousal-seeking language (§2.3 marker).
- Viewer sees: presenter narrating over ChatGPT app screen recordings, live demo of the vision-input feature almost immediately.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:07) → Upgrade 1: vision/image input demo, recipe-from-photo example (0:07–0:22) → Upgrade 2: word-limit jump (3,000 → 25,000 words) + creative-writing claim (0:22–0:35) → Upgrade 3: percentile benchmark stat (90th/99th percentile) (0:35–0:44) → **ends abruptly on the stat, no closing line or CTA.**
- Loop design: none — the video trails off after the third fact rather than landing a closing beat (rubric §2.6.1 marker: "does the ending land, or just stop?" — this one just stops).
- One idea per video: yes, clean listicle-of-3 under one "GPT-4 upgrades" frame.
- Pacing: screen-capture with cuts between the three demo segments — moderately more dynamic than the iPhone-tips videos (each of the 3 upgrades gets its own visual, not one continuous take).

#### 4. Value proposition
- Walk-away value: awareness of 3 concrete GPT-4 capabilities, illustrated with specific numbers (25,000-word limit, 90th/99th percentile).
- Value class: news + light tool-discovery.
- Specificity: good — concrete numbers given, though "screenplays or entire songs" is more aspirational gesture than demonstrated output.

#### 5. Psychology scoring
- STEPPS: **Triggers** — the highest of any AI video in the sample; GPT-4's launch was a major, single-day cultural news event, giving this video a real news-cycle trigger window. **Social Currency** — being an early explainer of a major AI release. **Emotion** — "blow your mind" framing targets awe/FOMO, both high-arousal per §2.3.
- Primary emotion + arousal: awe/FOMO, moderately high arousal — the strongest emotional register of any AI-topic video in the sample.
- Save/send trigger: moderate — informative but more "worth knowing" than "worth sending to one specific person."
- Practical value: moderate — informational rather than a copyable workflow.

#### 6. CTA & funnel mechanics
- No CTA present; no comment-bait mechanics observed.
- Funnel position: pure top-of-funnel awareness content, timed to news-cycle relevance.

#### 7. Replicability verdict
- Template: (1) identify a same-day-or-next-day major model/product launch, (2) frame as an N-item upgrade listicle, (3) demonstrate the single most visually compelling feature first (image input → recipe output is inherently show-able), (4) close each item with a concrete number.
- Commodity vs unfair advantage: the *format* is commodity (any AI channel can do a launch-day explainer), but **speed-to-publish is the unfair advantage** — this is a same-day turnaround, which requires an already-built production pipeline.
- Difficulty for Tangent: **MED** — requires monitoring the AI news cycle closely and having a fast-turnaround production process; content itself is straightforward once the news breaks.

#### 8. Why it won (within its class)
The load-bearing factor is **trend-velocity / news-cycle surfing** (rubric §3.4.1/§4 "velocity of trend response") — this is the single biggest AI story available at the time, and the video was live the same day. Secondary factor: listicle structure with an immediately visual first payoff (image → recipe). Compared to the channel's flops (Videos 10–11 below), the explicit delta is **news-cycle timing**: this video rides an external, massive, one-day-only spike in public search/curiosity; the flops cover either a since-deprecated product (Bard) or an abstract trend statement with no comparable news peg.

#### Sources
- https://www.youtube.com/shorts/6WVddn7qieU (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 4: "Google Ai for Gmail just ended email"

#### 0. Identity & stats
- URL: youtube.com/shorts/x4398W_-QZA | Posted: 2023-05-26 | Length: 36s (shortest in the sample)
- Views: 41,721 | Likes: 777 (1.86%) | Comments: 29 (0.070% — the highest comment rate of all 11 videos analyzed) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#4 of 30.**

#### 1. Packaging
- Title: "Google Ai for Gmail just ended email" — deliberately hyperbolic bold claim (email obviously did not end).

#### 2. Hook (0–3s)
- Verbatim: **"Google's AI update for Gmail is gonna end the need to ever write another email from scratch."** [OBSERVED via transcript, 0:00–0:03]
- Taxonomy: bold/hyperbolic claim hook — the most exaggerated claim-style hook in the sample, which likely explains the elevated comment rate (hyperbole invites pushback/debate comments).
- Viewer sees: Gmail interface inside Google Workspace, "Help me write" button visible almost immediately.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:03) → Demo setup: locate "Help me write" icon (0:03–0:14) → Live prompt example: "ask my boss for a raise" (0:14–0:23) → Result + refine options (formalize/lengthen/shorten) (0:23–0:34) → Close: "insert it into your email and press send" (0:34–0:36).
- One idea, single demo, tight 36-second runtime — the punchiest pacing in the sample by total length.
- Open loop: none really opened beyond the hook's claim; the demo directly and quickly resolves it.

#### 4. Value proposition
- Walk-away value: awareness of Gmail's "Help me write" AI feature + one demonstrated prompt.
- Value class: tool discovery, moderate specificity (one example prompt shown, not a broader prompt list).
- The relatable, mildly funny example prompt ("ask my boss for a raise") is a smart, universal-pain-point choice — everyone has wanted to ask for a raise.

#### 5. Psychology scoring
- STEPPS: **Practical value** high (writing email is a near-universal task). **Emotion**: amusement (the raise example is gently funny/relatable) plus mild practical relief. **Triggers**: writing an email is an extremely frequent daily cue, one of the broadest possible trigger surfaces even among AI-topic content.
- Primary emotion + arousal: amusement + relief, moderate arousal.
- The hyperbolic claim ("ended the need to ever write another email") likely also triggered **skeptical/contrarian comments** — a form of engagement that still counts as a ranking signal even when the sentiment is pushback, consistent with this video's outlier-high comment rate.

#### 6. CTA & funnel mechanics
- No explicit CTA. No comment-bait.
- Funnel position: top-of-funnel awareness, no course tie-in.

#### 7. Replicability verdict
- Template: (1) pick a near-universal task (writing email), (2) pair with an AI feature that automates it, (3) use hyperbolic "this ends X" framing in the hook, (4) demonstrate with a relatable, slightly funny example prompt, (5) keep it under 40 seconds.
- Commodity vs advantage: template is fully commodity; the specific choice of a universally-relatable example prompt is a light creative edge.
- Difficulty for Tangent: **LOW-MED** — straightforward to replicate for any AI feature tied to a universal task (writing, scheduling, etc.).

#### 8. Why it performed mid-pack (not top-tier, not a flop)
The load-bearing factor is **task universality within an AI-feature frame** — "writing email" is a near-universal chore, giving this AI video one of the broadest trigger surfaces of any AI-topic Short in the sample, which is likely why it outperforms most other pure-AI content. It still caps well below the off-topic hits and even below the GPT-4 news video, consistent with the diagnosis in Section C: it needed the viewer to already be curious about "Google AI" as a concept to click the hook's premise, a smaller cold-audience pool than "is my phone new or used."

#### Sources
- https://www.youtube.com/shorts/x4398W_-QZA (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 5: "ChatGPT iPhone App is finally here! And it can hear you!" — AI/iPhone hybrid

#### 0. Identity & stats
- URL: youtube.com/shorts/2701TUDJKnc | Posted: 2023-05-18 | Length: 55s
- Views: 40,141 | Likes: 668 (1.66%) | Comments: 29 (0.072%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#5 of 30.** This video is analytically important: it is AI content, but framed and hash-tagged through the iPhone/App Store lens (`#iphone #iphonehacks`), and it sits well above the pure-AI median (6,400) — nearly matching the GPT-4 news video.

#### 1. Packaging
- Title: "ChatGPT iPhone App is finally here! And it can hear you!" — news-drop + curiosity-gap tail ("and it can hear you" withholds the voice-feature detail).
- Hashtags mix AI and iPhone tags (`#ai #iphone #gpt #chatgpt #iphonehacks`) — a deliberate dual-audience framing.

#### 2. Hook (0–5s)
- Verbatim: **"ChatGPT just released an iPhone app, finally, and you could now talk to it too."** [OBSERVED via transcript, 0:00–0:05]
- Taxonomy: news-drop hook with an embedded curiosity gap ("talk to it too" is stated but not yet demonstrated) — a hybrid of bold-claim and information-gap taxonomy (rubric §2.1.1: partial information stated, gap not yet closed).
- Viewer sees: App Store search results for ChatGPT.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:05) → Install/verification instructions, including a scam-avoidance note ("make sure you find this one... the official app by OpenAI") (0:05–0:24) → Feature walkthrough: GPT-3.5 vs GPT-4 tiers, chat history (0:24–0:46) → Payoff: voice-input demo, closing the "talk to it" loop opened in the hook (0:46–0:55).
- Open loop: "you could now talk to it too" (hook) is explicitly closed at 0:46 with the live voice-demo — clean loop closure per rubric §2.6.1.
- Slight structural drift: this is really two ideas (how to install safely + the voice feature) unified only loosely under "the app is here" — a mild violation of the strict one-idea rule (§3.2), though the throughline holds together reasonably.

#### 4. Value proposition
- Walk-away value: safe-install instructions (protective, addressing a real risk of fake ChatGPT apps in the App Store at the time) + awareness of the voice feature.
- Value class: practical/protective + tool discovery.
- Specificity: good — exact verification cue given ("the one that says OpenAI ChatGPT, the official app").

#### 5. Psychology scoring
- STEPPS: **Practical/protective value** — the scam-app warning is a direct anxiety-resolution moment, similar in kind to Video 1's refurbished-phone protection angle. **Triggers**: "searching the App Store" is a broad, frequent action. **Social currency**: being early to a major app launch.
- Primary emotion: mild protective-anxiety resolution + mild curiosity (voice feature).
- This is the clearest **within-sample evidence that hybridizing AI content with a universal-device frame (iPhone) expands reach**: same era (2023) as the AI-median videos, same production quality, yet nearly matches the news-driven ceiling (62,512) at 40,141 — see Section C.

#### 6. CTA & funnel mechanics
- No explicit CTA; the built-in "verify this is the official app" instruction functions as protective guidance rather than a funnel mechanic.
- Funnel position: top-of-funnel, no course tie-in.

#### 7. Replicability verdict
- Template: (1) take an AI-tool news event, (2) frame the install/access step through a universal device the audience already owns, (3) include a protective/safety angle (avoid the fake version), (4) close by paying off a feature teased in the hook.
- Commodity vs advantage: commodity template; the "device-hybrid framing" insight itself (see Section C) is the more valuable, less commodity takeaway.
- Difficulty for Tangent: **LOW-MED** — directly applicable any time an AI tool ships a mobile app or device-native feature.

#### 8. Why it outperformed most pure-AI content
Load-bearing factor: **borrowed reach via device-universal framing** — by anchoring the AI story to "your iPhone," this video partially accesses the same broad trigger surface that drives the off-topic hits, without abandoning the AI subject matter. This is the strongest single piece of evidence in the sample that the AI-content ceiling is substantially about audience/context framing, not an immovable property of "AI" as a topic.

#### Sources
- https://www.youtube.com/shorts/2701TUDJKnc (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 6: "Using Photoshop Ai to complete famous paintings!"

#### 0. Identity & stats
- URL: youtube.com/shorts/ImZH5cUO4hI | Posted: 2023-05-29 | Length: 57s
- Views: 20,320 | Likes: 603 (2.97%) | Comments: 14 (0.069%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#6 of 30.**

#### 1. Packaging
- Title: "Using Photoshop Ai to complete famous paintings!" — result-first framing, leans on cultural-recognition value of "famous paintings."

#### 2. Hook (0–6s)
- Verbatim: **"I took some of the most famous paintings of all time, expanded and filled out the rest using AI."** [OBSERVED via transcript, 0:00–0:06]
- Taxonomy: result-first / demo-in-motion hook (rubric §3.1) — states the completed premise, then shows the process.
- Viewer sees: a famous painting on-screen with the Photoshop generative-fill tool already visible.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:06) → Demo 1: unnamed painting, generative expand (0:06–0:19) → Demo 2: second painting, multiple output variations (0:19–0:32) → Demo 3: **Mona Lisa specifically named**, before/after reveal (0:32–0:57).
- Escalation structure: saves the most universally recognizable painting (Mona Lisa) for last — a deliberate payoff-escalation choice, landing the biggest "wow" beat at the end (rubric §2.6.1: biggest payoff near the end, not front-loaded).
- Pacing: three distinct visual demos with clear before/after moments — the most dynamic pacing profile of the AI-topic videos in this sample.

#### 4. Value proposition
- Walk-away value: awareness of Photoshop's generative-fill AI tool + an aspirational "wow" reaction; light on exact settings/steps (no click-by-click parameter walkthrough).
- Value class: tool discovery + aspirational/wow value, weaker on step-by-step specificity than Videos 1, 2, or 5.

#### 5. Psychology scoring
- STEPPS: **Emotion (awe)** is the dominant lever here — "how wild is this" is explicit awe-seeking language, a genuinely high-arousal positive emotion per §2.3. **Social currency**: anchoring to universally-recognized cultural touchstones (Mona Lisa) elevates the content above a generic tool demo.
- Primary emotion + arousal: awe/wonder, high arousal, positive valence — per §2.3 this is one of the strongest evidence-backed emotional levers in the whole framework.
- Save/send trigger: moderate — impressive but not urgently protective or personally addressable the way Video 1 is.

#### 6. CTA & funnel mechanics
- No CTA present.
- Funnel position: top-of-funnel awe/awareness content.

#### 7. Replicability verdict
- Template: (1) pick a universally-recognized cultural reference point (not a generic stock example), (2) apply the AI tool to it, (3) sequence multiple examples with escalating recognizability, (4) land the most famous example last with a clean before/after.
- Commodity vs advantage: the "use a culturally universal reference object, not a generic one" insight is a genuinely useful, somewhat under-commoditized tactic — most AI demo videos use arbitrary or generic example content instead.
- Difficulty for Tangent: **LOW** — directly transferable to almost any generative AI tool demo.

#### 8. Why it landed mid-pack
Awe-driven emotion and cultural-touchstone framing gave this video a real edge over purely functional AI demos (compare Video 8, `-KS2NzPP_xc`, similar view count but a flatter, more functional emotional register) even though it under-delivers on exact-specificity. It's capped below the news-cycle and device-hybrid videos because "famous paintings + AI" still requires the cold viewer to already find AI-generated content novel/interesting — a topic-affinity precondition that "is your phone new or used" does not require.

#### Sources
- https://www.youtube.com/shorts/ImZH5cUO4hI (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 7: "Best prompts for chat GPT"

#### 0. Identity & stats
- URL: youtube.com/shorts/duBQKodYN-I | Posted: 2023-02-06 (one of the earliest AI-era Shorts, ~10 weeks after ChatGPT's Nov 2022 launch) | Length: 51s
- Views: 14,309 | Likes: 574 (**4.01% — the highest like-rate of all 11 videos analyzed, including the 1.03M-view hit**) | Comments: 6 (0.042%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#7 of 30.**

#### 1. Packaging
- Title: "Best prompts for chat GPT" — direct value-promise title, though (see below) the content is actually "where to find prompts," a mild title/payoff mismatch.

#### 2. Hook (0–3s)
- Verbatim: **"If you use ChatGPT you need to see this website."** [OBSERVED via transcript, 0:00–0:03]
- Taxonomy: bold-claim/FOMO hook ("you need to see this").
- Viewer sees: browser screen recording of a prompt-marketplace website.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:03) → Tool intro: PromptBase marketplace (0:03–0:11) → Use-case walkthrough: marketing prompts, trending sort (0:11–0:40) → Breadth list: LinkedIn/coaching/blog/SEO use cases (0:40–0:51), **ends without a strong closing line.**
- Payoff-vs-title mismatch: the title promises "best prompts," but the video delivers "a website where you can buy prompts" — the actual best prompts are never shown. This is a real specificity gap relative to the title's promise (rubric marker: specificity level — "exact prompts shown vs vague gesturing" — this leans toward the vague-gesturing end despite naming a specific tool).
- Ending trails off on a breadth list rather than a punchy close — a mild retention-engineering weakness (§2.6.1: does the ending land, or just stop?).

#### 4. Value proposition
- Walk-away value: awareness of a prompt marketplace (PromptBase), moderate specificity (exact site named, sort-by-trending method shown) but not the promised prompts themselves.
- Value class: tool discovery.

#### 5. Psychology scoring
- STEPPS: **Practical value** + **social currency** (marketplace/insider knowledge). The standout finding here is **engagement rate**: at 4.01% likes-per-view, this is the highest resonance-per-viewer of any video in the entire 11-video sample — higher than the 1.03M-view hit's 3.32%. This is the single clearest piece of evidence that **AI content is not underperforming on quality/resonance among the people who actually see it** — it is capped on reach, not on how much viewers who watch it like it. See Section C.
- Primary emotion + arousal: mild FOMO, moderate.

#### 6. CTA & funnel mechanics
- No explicit CTA, no comment-bait mechanics.
- Funnel position: top-of-funnel tool-awareness content.

#### 7. Replicability verdict
- Template: (1) name a specific tool/resource site directly in the hook ("you need to see this"), (2) demonstrate a filtered/sorted view of it, (3) list adjacent use cases for breadth.
- Commodity vs advantage: fully commodity format.
- Difficulty for Tangent: **LOW.**
- Caveat: the title/payoff mismatch (promising "best prompts," delivering "a prompt store") is a replicable anti-pattern to avoid, not to copy.

#### 8. Why it performed as it did
This video is the dossier's strongest proof point that **reach and resonance are separate variables** for this channel. Its content-quality signal (like-rate) is best-in-sample; its reach (14,309 views, rank 7 of 30) is unremarkable. The gap between those two facts is the core evidence for an audience-size/algorithmic-reach ceiling rather than a content-quality ceiling — see Section C for the full argument.

#### Sources
- https://www.youtube.com/shorts/duBQKodYN-I (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 8: "New way to build AI agents"

#### 0. Identity & stats
- URL: youtube.com/shorts/-KS2NzPP_xc | Posted: 2024-12-26 | Length: 54s
- Views: 13,471 | Likes: 505 (3.75%) | Comments: 3 (0.022%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#8 of 30.** Notably, this is nearly 2 years newer than the Feb–May 2023 AI cluster, giving it *less* compounding time than most of the other AI videos in the sample, yet it still lands in the top 8 — evidence the AI ceiling isn't purely a function of video age.

#### 1. Packaging
- Title: "New way to build AI agents #chatbase #chatgpt #aiagent" — bold-claim/news framing, narrower technical vocabulary ("AI agents," "build") than the consumer-facing titles above.

#### 2. Hook (0–4s)
- Verbatim: **"There's a brand new way to build AI agents and add them to your website."** [OBSERVED via transcript, 0:00–0:04]
- Taxonomy: bold-claim/news hook, addressed to a narrower audience (people who have or want a website with a chatbot) than any prior video in the sample.
- Viewer sees: Chatbase dashboard/interface screen recording.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:04) → Tool intro: Chatbase (0:04–0:14) → "Actions" feature explainer (0:14–0:20) → Three example agent capabilities: lead collection, Calendly-integrated appointment booking, live web search (0:20–0:49) → Close: recap of Chatbase's core value proposition (0:49–0:54).
- Listicle-of-3 structure (three agent capabilities), each with a distinct, concrete use case — good structural discipline, comparable to Videos 2 and 6.
- Pacing: continuous dashboard screen-capture, low visual dynamism.

#### 4. Value proposition
- Walk-away value: a specific tool name (Chatbase) + three concrete capabilities with named integrations (Calendly).
- Value class: tool discovery, narrow-audience practical value (website owners / small-business marketers specifically).
- Specificity: good — names the exact tool and exact integration partner.

#### 5. Psychology scoring
- STEPPS: **Practical value** — high but audience-conditional (requires owning/wanting a website chatbot, a real ceiling on addressable audience even within "AI-interested" viewers). **Social currency**: moderate (early access to a "brand new" feature).
- Like-rate (3.75%) is again well above the off-topic hits' engagement rates — reinforcing the Video 7 finding: quality/resonance is not the limiting factor.
- Primary emotion + arousal: mild practical-interest, low-moderate arousal (informational/utility register, not awe or FOMO-driven).

#### 6. CTA & funnel mechanics
- No explicit CTA or comment-bait.
- Funnel position: top-of-funnel tool-awareness, arguably closer to a B2B/prosumer audience segment than the channel's typical consumer viewer.

#### 7. Replicability verdict
- Template: (1) identify a genuinely new feature within a known AI tool, (2) explain the underlying mechanism in one sentence, (3) demonstrate 3 concrete use-cases with named real-world integrations.
- Commodity vs advantage: commodity format; specificity (naming Calendly, naming the "actions" feature precisely) is the differentiator versus vaguer competitor content.
- Difficulty for Tangent: **LOW-MED** — requires genuine familiarity with the tool being covered.

#### 8. Why it performed as it did
This video demonstrates the **audience-narrowing effect within AI content itself**: "AI agents for your website" is a smaller addressable slice even of the AI-interested population than "ChatGPT has a new iPhone app." This is a second-order version of the same ceiling mechanism diagnosed in Section C — audience size caps reach at every level of topic specificity, not just "AI vs non-AI."

#### Sources
- https://www.youtube.com/shorts/-KS2NzPP_xc (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 9: "iPhone setting you should change!" — GENERAL-TECH MEDIAN (same-topic control)

#### 0. Identity & stats
- URL: youtube.com/shorts/ebhi03W6ky8 | Posted: 2023-03-31 | Length: 42s
- Views: 5,500 | Likes: 100 (1.82%) | Comments: 3 (0.055%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#18 of 30** — essentially the general-tech segment's own median (general-tech median = 5,600; this video sits right at it). **This video is the dossier's single most important control case**: same topic class as the #1 video (iPhone settings tutorial), same channel, same era relative to the AI pivot (2023), yet sits **187x below** the #1 hit.

#### 1. Packaging
- Title: "iPhone setting you should change! #iphonetips #ios #iphone" — same hashtag/topic family as Video 1, but the hook (below) is conditional rather than universal.

#### 2. Hook (0–3s)
- Verbatim: **"If you listen to music on your iPhone you should turn on the setting right now."** [OBSERVED via transcript, 0:00–0:03]
- Taxonomy: direct imperative/warning hook — but note the **conditional framing "if you listen to music"**, which immediately narrows the addressable audience versus Video 1's universal "here's a trick you'll find useful" (no precondition) or Video 2's "your iPhone's camera has three hidden settings" (applies to any camera user, i.e., nearly all iPhone owners).
- Viewer sees: Settings app screen recording, same production style as Video 1.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:03) → Navigation: Settings > Sound > Headphone Safety (0:03–0:14) → Demo: decibel slider control (0:14–0:33) → Recommendation + safety framing: "around the 85 decibel point... protect your hearing" (0:33–0:42).
- Structurally almost identical to Video 1 (single continuous settings walkthrough, one clean payoff, protective framing) — the production template is the same.

#### 4. Value proposition
- Walk-away value: a specific setting (Headphone Safety / loud-sound reduction) with a recommended threshold (85dB).
- Value class: practical/protective (hearing-health), same class as Video 1's scam-protection value, but a narrower harm (long-term hearing damage vs. immediate financial scam) and a narrower trigger condition (must already listen to loud music via headphones).

#### 5. Psychology scoring
- STEPPS: **Practical/protective value** present but the **Triggers** surface is meaningfully narrower — this only activates for viewers who already listen to loud music on headphones, versus Video 1's trigger ("anyone about to buy/receive an iPhone") which applies to essentially the entire iPhone-owning population at some point.
- Primary emotion + arousal: mild protective concern, lower arousal than Video 1 — hearing damage is a slower-moving, less urgent/immediate risk than being scammed on a purchase, consistent with rubric §2.3's arousal-drives-sharing mechanism (lower-arousal risk = weaker transmission even at equal "protective" valence).
- Save/send: lower specificity of addressee than Video 1 ("send to a friend who listens to loud music" is a narrower ask than "send to anyone buying a phone").

#### 6. CTA & funnel mechanics
- No CTA present.
- Funnel position: legacy top-of-funnel, same non-AI-funnel disconnect as Videos 1–2.

#### 7. Replicability verdict
- Template: identical mechanical template to Video 1, but the case study here is a **cautionary** one: conditional/narrower hooks within the same topic and same production quality massively underperform universal ones.
- Difficulty for Tangent: N/A (off-mission), but the *lesson* — hook universality matters more than topic category — is directly applicable to AI content hook design.

#### 8. Why it landed at the general-tech median, not near the #1 hit
This is the dossier's cleanest natural experiment: holding topic (iPhone settings), channel, production style, and era roughly constant, the only major variable that changed is **hook universality/conditionality**, and the outcome swings 187x. This proves the ceiling-gap diagnosis cannot be reduced to "iPhone content wins, AI content loses" — most iPhone content on this very channel performs in the same range as most AI content (see Section A's close AI/general-tech medians). The #1 and #2 videos are outliers *within* the general-tech bucket too, not representative of it.

#### Sources
- https://www.youtube.com/shorts/ebhi03W6ky8 (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 10: "ChatGPT competitor from Google is live - Bard Ai" — FLOP (lowest views in catalog)

#### 0. Identity & stats
- URL: youtube.com/shorts/Fqd7KCc5Gug | Posted: 2023-03-21 | Length: 52s
- Views: 1,789 | Likes: 33 (1.84%) | Comments: 1 (0.056%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#30 of 30 — the lowest-viewed Short in the entire catalog.**

#### 1. Packaging
- Title: "ChatGPT competitor from Google is live - Bard Ai #ai #bard #goolgeai #chatgpt" — note the typo "goolgeai" in the hashtags, a minor production-quality lapse.

#### 2. Hook (0–3s, extends to ~7s)
- Verbatim: **"Google just released a competitor to ChatGPT, it's called Bard, let me show you how it works."** [OBSERVED via transcript, 0:00–0:07]
- Taxonomy: news-drop hook, but comparatively flat/expository — "let me show you how it works" is a soft, low-urgency close to the hook rather than a sharp claim or gap, closer to the "preamble" pattern the rubric flags as a retention risk (§2.6.2), even though it's brief here.
- Viewer sees: Bard's web interface.

#### 3. Structure & retention engineering
- Beat map: Hook (0:00–0:07) → Feature 1: voice-input mic (0:07–0:27) → Feature 2: "Google it" integration button (0:27–0:50) → **Ends mid-thought**: "so I could go back and forth between the two using these two different windows" — no closing line, the video simply stops on a logistical detail rather than a punchy takeaway.
- Ending fails to land per §2.6.1's marker ("does the ending land, or just trail off?") — this is the weakest close of any video in the sample.

#### 4. Value proposition
- Walk-away value: awareness of Bard as a ChatGPT alternative + two feature demos (voice input, Google Search integration).
- Value class: tool discovery/news.
- A structural risk specific to this video: Bard was, at the time, a **waitlisted, first-generation product** ("it may have a waiting list right now" is stated in the video itself) — the content was covering an unproven, not-yet-mainstream product, which caps both immediate relevance and long-tail evergreen value (Bard was later rebranded/absorbed into Gemini, further shortening this video's long-term discoverability compared to an evergreen topic like iPhone settings).

#### 5. Psychology scoring
- STEPPS: **Triggers**/news-cycle relevance present but weaker than Video 3's GPT-4 launch-day video — Bard's waitlisted launch was a smaller, less universally-felt event than GPT-4's release.
- Primary emotion + arousal: low — informational/neutral register, no awe, FOMO, or protective framing attempted.
- No clear identity-signaling or save/send hook.

#### 6. CTA & funnel mechanics
- None present.

#### 7. Replicability verdict
- Anti-pattern to avoid: (1) don't cover waitlisted/unproven products as if evergreen, (2) don't let the hook end on a soft "let me show you how it works," (3) don't end on a logistical/administrative detail — always land a closing takeaway.
- Difficulty: N/A — this is a lesson in what not to do.

#### 8. Why it lost — named delta vs. the top performers
Compared to Video 3 (also an AI-competitor/launch news video, but 62,512 views vs. this video's 1,789 — a **35x delta between two structurally similar "AI news" Shorts**), the explicit differences are: (a) GPT-4 was a proven, immediately-usable product; Bard was waitlisted and unproven at time of posting — a real news-magnitude gap, not just a production difference; (b) Video 3's hook uses "gonna blow your mind" (high-arousal language); this video's hook uses "let me show you how it works" (low-arousal, procedural language); (c) Video 3 closes on a concrete stat; this video trails off mid-sentence with no closing beat. Also relevant: this video was posted within the same crowded Feb–May 2023 burst (7 AI shorts in ~4 months) — likely diluting the channel's own audience attention and the algorithm's willingness to test-expand every entry in a fast-fired cluster equally.

#### Sources
- https://www.youtube.com/shorts/Fqd7KCc5Gug (metadata, transcript — yt-dlp, 2026-07-25)

---

### VIDEO 11: "Are you using AI agents yet?" — FLOP (2nd-lowest, most recent Short in catalog)

#### 0. Identity & stats
- URL: youtube.com/shorts/nJIk488lmRE | Posted: 2025-10-08 | Length: 51s
- Views: 1,949 | Likes: 33 (1.69%) | Comments: 1 (0.051%) — [OBSERVED, 2026-07-25, HIGH]
- Rank: **#29 of 30.** This is the single **most recent** Short in the entire 30-video catalog — posted with a 335K-subscriber base behind it (vs. ~far smaller subscriber counts when the 2023 videos were posted), yet it still lands in the bottom two. This is important evidence that the ceiling is structural, not just a function of the channel being smaller in 2023.

#### 1. Packaging
- Title: "Are you using AI agents yet? #aiagents" — a direct question/self-locating hook framing (rubric §3.1 "confronting question" taxonomy) at the title level.

#### 2. Hook (0–3s, extends to ~7s)
- Verbatim (in-video, distinct from the title): **"Some of the very best AI tools are adding AI agents on top of their AI tool."** [OBSERVED via transcript, 0:00–0:07]
- Taxonomy mismatch: the **title** poses a sharp confronting question ("Are you using AI agents yet?"), but the **actual spoken hook** is an abstract trend-statement with no immediate visual payoff, no concrete claim, and no demo shown in the first few seconds. Per rubric §1.2.3, packaging (the title) is largely moot for Shorts — the in-video hook is what the swipe-away decision is based on, and this video's real hook is the weaker of the two.
- Viewer sees: talking-head or generic AI-tool-adjacent visual (no immediate concrete demo) during the abstract opening statement.

#### 3. Structure & retention engineering
- Beat map: Abstract trend intro (0:00–0:13) → Tool intro: Gamma (0:13–0:21) → Demo: agent-mode theme-changing (0:21–0:49) → Ends: "so I could go through and see which one I like" — another soft, non-punchy close.
- The first 13 seconds — nearly a quarter of the video's 51-second runtime — are spent on an abstract, non-visual claim before any concrete tool or demo appears. This is a direct violation of rubric §1.2.1/§2.1.3 (deliver a visible payoff or promise within the first second for Shorts) and is the single clearest hook-construction flaw in the entire 11-video sample.
- Title/content mismatch: the title promises a provocative yes/no self-assessment question; the content delivers a single-tool feature demo (Gamma's agent mode) — the title's implied "listicle of reasons to start using agents" never materializes.

#### 4. Value proposition
- Walk-away value: awareness of one feature (Gamma's agent mode for presentation theming).
- Value class: tool discovery, narrow scope (one feature of one tool).
- Specificity: moderate (a real demo is shown) but arrives late and is preceded by throat-clearing.

#### 5. Psychology scoring
- STEPPS: weak across the board relative to the sample — no strong Triggers (no news peg), no Social Currency claim, no explicit protective or awe framing. **Emotion**: flat/informational, low arousal.
- This is the least emotionally-activated video in the entire 11-video sample by the rubric's own framework.

#### 6. CTA & funnel mechanics
- None present.

#### 7. Replicability verdict
- Anti-pattern to avoid: abstract, trend-statement openings with no first-second visual payoff; title/hook mismatch between the packaged question and the delivered content.
- Difficulty: N/A — a lesson in what not to do, useful precisely because it's recent (2025) and still exhibits the same avoidable flaw seen in older flops.

#### 8. Why it lost, and what its recency proves
The explicit delta versus the channel's strongest AI video (Video 3, GPT-4): no news peg, no concrete first-second payoff (13 seconds of abstract setup vs. Video 3's demo starting at 7 seconds), and no arousal-seeking language. Structurally, this is the same hook-construction failure as Video 10's Bard video (soft/procedural opening, weak close), just five years and 300K subscribers later — **strong evidence that the AI-content ceiling on this channel is a durable structural pattern, not an artifact of the channel being small or new when the AI pivot happened.** It also confirms Shorts have become a genuinely deprioritized, low-repetition format for this channel by 2025 (only one other Short — `-KS2NzPP_xc`, Dec 2024 — was posted in the roughly two years before this one), meaning there's little recent iteration/practice on the format to have improved hook craft.

#### Sources
- https://www.youtube.com/shorts/nJIk488lmRE (metadata, transcript — yt-dlp, 2026-07-25)

---

## C) THE CEILING-GAP DIAGNOSIS

**The question:** why does one off-topic iPhone-tips Short (1,028,157 views) outperform the channel's best AI-specific Short (62,512 views) by 16.4x, on the same channel, same production resources, same presenter?

**The answer is not simply "general tech beats AI on this channel."** Section A's median split already falsifies the naive version of that claim: the AI-topic median (6,400) and general-tech median (5,600) across the full 30-video catalog are close — most general-tech Shorts on this channel perform in the *same range* as most AI Shorts. The entire gap is produced by **two specific outlier videos**, not by a systematic topic-class advantage. Four converging mechanisms, all grounded in the rubric and the observed data, explain those two outliers and the broader AI ceiling:

**1. Timing/compounding (rubric §1.2.2 "test-and-expand," §3.4.1 cadence).** The two off-topic hits are, by [OBSERVED] upload date, the two *oldest* Shorts in the entire 30-video catalog (2021-11-03 and 2021-12-18), posted within months of YouTube Shorts' broad US rollout — a less saturated feed environment per the rubric's explore/exploit seeding logic. They have had ~4.5 years to compound views; the AI-topic videos (mostly 2023, one as late as 2025) have had at most ~3 years, several under 1 year. This is a real, non-trivial contributor but **cannot be the whole story**: Video 9 (`ebhi03W6ky8`, iPhone settings, posted 2023-03-31 — the *same era* as the AI-median videos) still sits 187x below the #1 hit despite matching topic and era. Timing alone doesn't explain a 187x same-topic, same-era gap.

**2. Audience-size ceiling via topic universality (rubric §1.2.2/§1.2.3 — Shorts reach is feed-driven and decoupled from subscriber count).** Because Shorts distribution is not gated by the channel's 335K AI-interested subscriber base, a Short's true ceiling is the platform-wide population that could plausibly be interested — and "owns/is buying an iPhone" is a vastly larger population than "is curious about ChatGPT" was in 2023, or "wants to build AI agents for a website" is at any point. The best evidence for this mechanism specifically (isolated from timing) is **Video 5** (`2701TUDJKnc`, ChatGPT's iPhone app, 2023, same era as the AI-median cluster): by hybridizing AI content through the universal iPhone/App-Store frame, it reaches 40,141 views — nearly matching the news-driven ceiling and dwarfing the pure-AI median of 6,400. Same era, same production, different *frame* → 6x the typical AI outcome.

**3. Hook universality vs. hook conditionality (rubric §2.1.1 Loewenstein information-gap; §1.2.1 "one second to hook").** Within the SAME topic (iPhone settings), the #1 hit's hook ("here's a trick you'll find useful," no precondition) applies to literally any iPhone owner, while Video 9's hook ("if you listen to music on your iPhone...") is conditional and narrower. That single variable — universal vs. conditional framing — tracks the 187x gap between two same-topic, same-era, same-channel videos better than anything else in the dataset. Applied to AI content, this explains why "AI agents for your website" (Video 8, narrower precondition: must want a website chatbot) underperforms "ChatGPT has an iPhone app" (Video 5, near-zero precondition: anyone with an iPhone and vague AI curiosity).

**4. What the data rules out: this is NOT a content-quality problem.** [OBSERVED] engagement rates computed directly from fetched like/view ratios show AI-topic videos matching or *beating* the off-topic hits on a per-viewer basis: Video 7 (`duBQKodYN-I`, "Best prompts for ChatGPT") has a 4.01% like-rate — higher than the #1 hit's 3.32% — while sitting at only 14,309 views. Video 8 (`-KS2NzPP_xc`, AI agents) has a 3.75% like-rate at only 13,471 views. This is the dossier's most important finding for Tangent's own strategy: **the people who see AI-tutorial content on this channel like it at least as much as the people who see the off-topic hits** — the AI content is capped on *reach* (how far the algorithm's explore/exploit test-and-expand cycle extends it, gated by cold-audience topic-affinity size and hook universality), not on *resonance*. This is consistent with, though not separately proven by, the rubric's explore/exploit mechanism (§1.2.2): a smaller topic-affinity seed cohort and a narrower/conditional hook both reduce how far a Short's early-wave success can expand it, even when the content that *does* get seen performs excellently.

**5. Channel-identity/legacy factor** [REPORTED, MED confidence]: the two outliers were produced under the channel's prior general-tech identity ("Howfinity," evidenced by the #1 video's description linking to howfinity.com and the shared `@howfinity_tech` Instagram handle/Facebook rebrand announcement), not the current AI-tutorial mission. They are best understood as **inherited legacy assets from a different content strategy**, still visible in the catalog because the channel kept the same handle through its pivot, rather than as proof that the current strategy should chase general-tech virality.

**Bottom line for Tangent:** the ceiling is real and structural (audience-size + hook-universality + timing, reinforced by algorithmic reach mechanics), but it is not a content-quality verdict against AI/niche tutorial material — it's a reach ceiling. The two actionable levers this channel demonstrably has *not* fully exploited within its own AI content are (a) device/context-hybrid framing (Video 5's approach) and (b) ruthlessly universal, non-conditional hook phrasing (contrast Video 1 vs. Video 9) — both are transferable to Tangent without requiring off-mission content.

---

## D) Content architecture: key vs. filler, cadence, sustainability

- **Long-form (≈329 videos, ~2x/week cadence)** [INFERRED cadence from 2 anchor dates, MED confidence] is the channel's **key content** — 11-to-30-minute deep-dive tutorials/reviews on specific tools and model releases (e.g., "Master 80% of Claude Code in 26 Minutes," "Ultimate Guide To Claude Skills," "ChatGPT 5.5 Is Here: I Tested What It Can Actually Do") [OBSERVED titles, 25-video sweep of `/videos`, 2026-07-25]. This is where the channel's actual value delivery and course-funnel conversion (the `bit.ly/skill-leap` bio link) happens — long-form runtime is what actually supports step-by-step tutorial depth, which the Shorts format structurally cannot (rubric §1.2.3: Shorts packaging/depth tradeoffs favor long-form for anything requiring real instructional depth).
- **News-cycle reactivity is the core long-form template**, carried over from the Shorts era: Video 3 (GPT-4, same-day turnaround) established the pattern in Shorts form in 2023; the same "[Product] is here / I tested it" title structure now dominates the long-form catalog ("Claude Opus 4.8 Review: New Demos You Need to See," "Gemini Spark Is Google's Most Powerful AI Tool Yet") [OBSERVED titles, 2026-07-25]. This is a repeatable, sustainable format precisely because the AI industry supplies a constant stream of launch events to react to — cadence is externally paced by the news cycle, not manufactured from scratch each time.
- **Shorts are filler/legacy, not a sustained pillar.** The full dated picture [OBSERVED for 11 of 30 videos, HIGH; remainder undated — data gap logged below]: 2 general-tech Shorts in late 2021 (pre-pivot), a concentrated burst of AI Shorts in Feb–May 2023 (at least 7 of the 24 AI Shorts fall in this ~4-month window), then near-total abandonment — only 2 further Shorts identified across the following ~2.5 years (Dec 2024, Oct 2025). Combined with only 30 total Shorts ever posted against ≈329 long-form videos, the evidence strongly suggests **Shorts were tried hard once, in the immediate aftermath of ChatGPT's launch, largely failed to clear the reach ceiling diagnosed in Section C, and were subsequently deprioritized** in favor of long-form, where the channel's actual funnel and instructional depth live.
- **Sustainability read:** this is a tutorial/education channel whose durable growth engine is long-form + news-cycle timing + a direct course-platform funnel, not a Shorts-virality engine. The one off-topic Shorts spike, however large, appears to be an inherited anomaly from a prior channel identity rather than a repeatable growth lever the current strategy relies on or has continued to pursue (zero further off-topic Shorts were posted after the 2021 pair, across nearly 5 years and 28 subsequent Shorts).

---

## E) Method log

**Environment:** yt-dlp 2026.07.04, direct fetch, no third-party aggregator, all work in `/private/tmp/.../scratchpad/yt_skillleap/`, `--sleep-requests 0.75` (increased to 1–2s later in the session as rate-limiting increased).

**What was fetched successfully:**
1. Full Shorts catalog sweep: `yt-dlp --flat-playlist --playlist-items 1:150` and an uncapped sweep of `youtube.com/@SkillLeapAI/shorts` — both returned exactly 30 rows with zero errors, establishing 30 as the channel's complete Shorts population (not a sample).
2. Full 30-row view-count table sorted descending; used to compute ranks, medians, and the AI-vs-general-tech split.
3. Per-video metadata (title/views/likes/comments/date/duration) via `yt-dlp --print` against `youtube.com/shorts/<id>` for all 11 selected videos — succeeded for all 11 before rate-limiting set in.
4. Per-video descriptions for all 11 selected videos.
5. Auto-generated English subtitles (`--write-auto-subs --sub-langs "en.*" --sub-format vtt`) for all 11 selected videos, deduplicated via a Python script stripping VTT timing/formatting tags and consecutive-duplicate caption lines; timestamped raw VTT re-extracted separately to build beat maps with real timestamps (not evenly-spaced estimates).
6. Channel-level bio/description text via `yt-dlp -J --flat-playlist` on the channel root (this substituted for the `/about` page, which WebFetch could not render — see failures below).
7. Channel subscriber count (335,000) via the `channel_follower_count` field on a direct video fetch.
8. 25-video sweep of the `/videos` (long-form) tab for content-architecture context.
9. Two upload-date anchors for long-form videos (`WCuwYLVE6j8` = 2026-03-19, `AxRprCFZBU8` = 2026-03-27), used to estimate long-form cadence.
10. WebSearch queries establishing the Howfinity connection ([REPORTED, MED] — Instagram handle overlap + a Howfinity-page Facebook post announcing the Skill Leap AI platform) and the current course-funnel structure (Skill Leap by Futurepedia, 7-day free trial, month-to-month).

**What failed / data gaps (logged per QC_PROTOCOL rule 3, not papered over):**
1. **WebFetch of `youtube.com/@SkillLeapAI/about`** returned only YouTube's static footer navigation — the about page is JS-rendered and not accessible to WebFetch. Substituted with the yt-dlp channel-description field (item 6 above), which captured the same bio text successfully.
2. **YouTube rate-limiting (HTTP 429) and bot-check ("Sign in to confirm you're not a bot")** set in partway through the session, after roughly 25–30 individual watch-page requests in quick succession. This blocked: (a) upload dates for the remaining 19 of 30 Shorts not in the 11-video deep-dive set — these videos' exact post dates are therefore **unknown** and not used anywhere in this dossier as if known; cadence claims for Shorts rely only on the 11 dated videos, explicitly flagged as such; (b) upload dates for 3 of 5 additional long-form videos attempted for cadence triangulation (only 2 of 5 succeeded, used as the sole cadence anchors, MED confidence as a result); (c) top-comment content retrieval (`--write-comments`) for the #1 video and the best AI video — attempted to add qualitative comment-sentiment evidence to the psychology sections, but both calls hit the bot-check before returning data. No comment content is fabricated or invented anywhere in this dossier as a result — comment *counts* (from the successful metadata pulls, item 3 above) are used, comment *content* is not, and this gap is logged rather than papered over.
3. No exact rebrand date (Howfinity → Skill Leap AI) was locatable via WebSearch; the Howfinity connection itself is corroborated by two independent signals (shared Instagram handle, a direct link to howfinity.com in the #1 video's own description) but carries [REPORTED, MED] confidence rather than [OBSERVED, HIGH] for the causal "this channel used to be Howfinity" claim, per QC_PROTOCOL's evidence-tier rules.
4. Total lifetime channel view count was not gathered (not load-bearing for the analysis requested; subscriber count and per-video view counts were prioritized given time/rate-limit constraints).

**Selection rationale (11 videos from a 30-video population):** top 8 by raw views (ranks 1–8, includes both off-topic outliers and all 6 of the channel's best-performing AI Shorts), + 1 general-tech median representative chosen deliberately for its same-topic-class contrast value against the #1 video (rank 18, at the general-tech segment's own median), + 2 flops (ranks 29–30, the two lowest-viewed Shorts in the entire catalog — one from the 2023 AI cluster, one the most recent Short in the catalog, giving both an "old flop" and a "recent flop" data point). The AI-topic median (6,400, ranks 12–13) is reported and used analytically in Sections A and C but was not built into a 12th full post-mortem, to keep the video count within the template's 10–11 target; both AI- and general-tech medians are nonetheless independently computed and cited with sources.