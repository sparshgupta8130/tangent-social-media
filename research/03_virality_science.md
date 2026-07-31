# The Evidence Base for Short-Form Video Post-Mortems

**Scope:** Instagram Reels + YouTube Shorts, 2024–2026. Built for per-video grading, not for general strategy reading.

**How to read this document.** Every principle is tagged:

- **[RESEARCH-BACKED]** — peer-reviewed study, official platform documentation/blog, or a platform executive's on-record statement.
- **[INDUSTRY DATA]** — a large real dataset analyzed by a commercial vendor (creator-tools company, video host, ad platform). Directionally trustworthy, not peer-reviewed, and the vendor has an incentive to produce shareable findings. Methodology is usually disclosed but not independently auditable.
- **[PRACTITIONER LORE]** — folk wisdom repeated across creator-economy blogs/newsletters with no traceable primary source. Often plausible and consistent with (a) and (b) above, but should not be scored as if it were proven.
- **[UNVERIFIED STAT — DO NOT CITE AS FACT]** — a specific-sounding number (e.g., "38% lift," "3.3x completion") that recurs across SEO content-farm articles but could not be traced to any named study, dataset, or methodology after a direct search. These numbers appear to be invented or mutated by content-marketing sites copying each other. They are included here only so analysts recognize and discount them when they see them elsewhere — **never use them as a scoring threshold.**

Each principle gives: **(a) the claim**, **(b) the evidence**, **(c) markers** — what to actually look for in a specific Reel/Short during a post-mortem.

---

## 1. ALGORITHM MECHANICS (2024–2026)

### 1.1 Instagram Reels ranking signals

**1.1.1 The four signal families Instagram states it uses** [RESEARCH-BACKED]

*Claim:* Instagram's official ranking explainer names four categories of signals for Reels, in this order: (1) your own activity — reels you've liked, saved, reshared, commented on, and engaged with recently; (2) your history with the poster; (3) information about the reel itself — audio/visuals and its general popularity; (4) information about the poster — follower count and engagement level. Instagram states the actions it most heavily weighs it predicts are: **likelihood to reshare, likelihood to watch all the way through, likelihood to like, and likelihood to visit the audio page.**

*Evidence:* Meta/Instagram official blog, "Instagram Ranking Explained," about.instagram.com/blog/announcements/instagram-ranking-explained (Adam Mosseri, 2023, still the standing reference Instagram links from its Help Center as of 2025–2026).

*Markers:* Does the video's content make resharing psychologically cheap (see STEPPS §2.2)? Is there a natural "go check out the audio" moment (trending sound, remix-bait)? Does it reward rewatching (loop-friendly ending)?

**1.1.2 Watch time, likes-per-reach, sends-per-reach as the "big three"** [PRACTITIONER LORE, converging from many secondary sources, not from a single citable Meta document]

*Claim:* Multiple creator-marketing outlets independently report that Mosseri named watch time, likes-per-reach, and sends-per-reach as the three ranking factors that matter most as of January 2025, with sends (DM shares) weighted several times higher than likes for reaching *new* (unconnected) audiences, while likes matter more for reach among existing followers.

*Evidence:* Convergent secondary reporting (Torro, DataSlayer, Buffer, Social Media Today, various creator newsletters) attributing the "3-5x" multiplier and the connected/unconnected split to Mosseri's public statements; no single primary transcript was locatable. Treat the *direction* (sends > likes for cold reach) as credible because it is consistent with §1.1.1's official emphasis on "likelihood to reshare," but treat the specific "3-5x" multiplier as **[UNVERIFIED STAT]**.
Independently, multiple 2025-2026 sources (Socialync, David Zucker's newsletter) report Mosseri stating shares are "the strongest signal Instagram has ever had" and that Instagram's internal data shows shares predict long-term retention/satisfaction better than watch time or saves — again convergent secondary reporting, not a located primary transcript.

*Markers:* Would a friend actually send this to one specific other person ("this is so you" / "you'd love this")? Is the content narrow/specific enough to have a addressee in mind, vs. generically "nice" content nobody sends?

**1.1.3 The "audition" model / early-velocity window** [PRACTITIONER LORE + consistent with official mechanism]

*Claim:* New Reels are shown to a small test audience first; if early engagement (watch time, saves, shares) is strong, distribution expands in waves. Commonly cited windows are the first 30–90 minutes.

*Evidence:* This "test-and-expand" mechanism is well-documented for YouTube Shorts (§1.2, official interviews) and is described by multiple secondary sources as also applying to Reels, using Mosseri's own "audition" framing. The specific "90-minute" window is **[UNVERIFIED STAT]** — no official minute-count was locatable for Instagram specifically.

*Markers:* Was the caption/hook designed to convert the *first* wave of viewers (people who already follow similar accounts) into savers/sharers, since that wave determines whether the video ever reaches wave two?

### 1.2 YouTube Shorts ranking signals

**1.2.1 "Viewed vs. Swiped Away" is the primary hook-quality metric** [RESEARCH-BACKED]

*Claim:* Unlike long-form, most Shorts views originate from the algorithmic feed rather than deliberate search/click, so YouTube built a distinct metric — the percentage of times a Short is watched vs. immediately swiped away — visible in Shorts Analytics. YouTube Shorts product lead Todd Sherman has described this directly in on-record interviews (Creator Insider channel, and press coverage of it) as the primary lens for judging whether a hook worked.

*Evidence:* YouTube official blog, "YouTube Shorts deep dive: A conversation with product lead Todd Sherman and creator Jenny Hoyos," blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/ — direct quote from Jenny Hoyos (a creator YouTube chose to feature on its own blog as instructive): **"you have one second to hook someone, especially on Shorts"** and thumbnails are largely irrelevant because "99.9% of the views are coming from the Shorts feed" (not a click on a thumbnail). Corroborating coverage: MediaPost ("YouTube Shorts Product Lead Offers Insights For Creators And Brands"), Search Engine Journal's writeup of the Creator Insider interview describing the swiped-away metric and the algorithmic-feed vs. search distinction in Sherman's own words: *"On short-form, people are swiping through a feed, and discovering things as they go. That's one important difference."*

*Markers:* Is there a legible payoff/promise visible in the first frame or first spoken word (nothing to "click," so nothing to sell except the next second)? Would a cold viewer, with zero context, know within ~1 second whether to keep watching?

**1.2.2 Average % viewed / completion, and the "explore → exploit" seeding model** [INDUSTRY DATA for exact thresholds, RESEARCH-BACKED for the underlying mechanism]

*Claim:* YouTube explicitly uses a small-seed-audience test (a few hundred to a few thousand viewers with topic affinity) and, if that cohort's retention/rewatch/like behavior is strong, expands distribution to progressively larger audiences — independent of subscriber count. This is why unknown creators can spike suddenly.

*Evidence:* This mechanism is described consistently across multiple outlets summarizing Sherman's public comments (vidIQ, Shortimize, TrueFuture Media) and matches the general "test-and-expand" pattern platforms have described for algorithmic feeds. Specific completion-rate thresholds circulating ("70%+ is excellent," "below 30% kills distribution," "80–100%+ triggers rewatch signal") are **[INDUSTRY DATA / UNVERIFIED]** — plausible, repeated by vendors like vidIQ and Shortimize who have access to aggregate creator data, but no disclosed methodology was locatable, so treat the *direction* (higher % viewed → broader push) as reliable and the *exact cutoffs* as heuristics only.

*Markers:* Does completion likely clear the video's own runtime-adjusted bar (a 60-second Short needs a mid-video reason to keep watching, not just a strong first second)? Is there a rewatch trigger (loop, "wait, what?" ending, visual gag that rewards a second pass)?

**1.2.3 Shorts feed vs. long-form recommendations — the core structural difference** [RESEARCH-BACKED]

*Claim:* Long-form YouTube recommendations are built around a viewer's deliberate choice from a grid (so thumbnail/title "packaging" drives the click); Shorts recommendations are a continuous swipe feed with no comparable choice moment, so the entire selection burden moves onto the in-video hook and away from the thumbnail/title.

*Evidence:* Same YouTube-official blog source as 1.2.1 (Jenny Hoyos: thumbnails "not important" for Shorts because 99.9% of views come from the feed) plus Sherman's "swiping through a feed" quote.

*Markers:* Was production effort spent on a thumbnail/title instead of the in-video first second? (Wasted effort for Shorts — misallocated grading signal if the post-mortem penalizes weak thumbnails on a Short.)

### 1.3 What platforms say they penalize

**1.3.1 Instagram's official "less visible" list** [RESEARCH-BACKED — direct quote from official source]

*Claim:* Instagram explicitly states in its Recommendation Guidelines / ranking explainer that it aims to make certain Reels **less visible**, specifically: *"low-resolution or watermarked reels, reels that are muted or contain borders, reels that are majority text, or reels that have already been posted on Instagram."*

*Evidence:* Meta/Instagram official blog, "Instagram Ranking Explained" (about.instagram.com/blog/announcements/instagram-ranking-explained); reiterated at the official Help Center article "Recommendation eligibility on Instagram" (help.instagram.com/653964212890722).

*Markers (binary, checkable per video):* Third-party watermark visible (CapCut/TikTok/other)? Below-1080p export or visible compression artifacts? Black bars/borders present? Is the video majority static text-on-screen rather than motion/visual content? Was this exact file previously posted elsewhere on the account?

**1.3.2 Instagram's official engagement-bait / clickbait policy** [RESEARCH-BACKED — direct quote]

*Claim:* Instagram's Recommendation Guidelines (which Threads also follows) explicitly list *"content that users broadly tell us they dislike, including clickbait, engagement bait, or which promotes a contest or giveaway"* as ineligible for recommendation surfaces (Explore, Reels tab, Suggested Posts). "Comment YES if you agree"-style prompts are named as a canonical example.

*Evidence:* Instagram Recommendation Guidelines, as quoted directly by Buffer's official Threads account (a verified brand account citing the guidelines text) and corroborated by Social Media Today's reporting on Mosseri publicly debunking "always ask people to comment" as a growth hack.

*Markers:* Does the caption or on-screen text contain a bare compliance-bait instruction ("comment X," "like if you agree," "tag a friend or you'll have bad luck") with no informational or entertainment content behind it? Note: a *genuine* CTA embedded in useful content (§3.4) is different from bare engagement bait — the distinguishing test is whether the video has stand-alone value without the bait.

**1.3.3 Follow-gating / like-gating contests devalued as "low-intent"** [PRACTITIONER LORE, plausible extension of 1.3.2]

*Claim:* Updated Instagram promotion rules prohibit mandatory engagement (like/comment/follow) as a contest-entry condition, and several secondary sources claim the algorithm now treats gated actions as "low-intent" signals that can suppress reach even where not technically banned.

*Evidence:* Secondary reporting only (Gainsty, KickoffLabs, TheSocialCat); the "low-intent signal suppression" mechanism specifically was not locatable in an official document. Treat the *policy* (gating is prohibited) as confirmed and the *algorithmic penalty mechanism* as unverified inference.

*Markers:* Does the video require a follow/like/tag as a literal condition of participation (contest, giveaway)?

---

## 2. HUMAN PSYCHOLOGY OF VIRAL SHORT-FORM

### 2.1 Hook mechanics

**2.1.1 The curiosity/information-gap** [RESEARCH-BACKED]

*Claim:* Loewenstein's information-gap theory of curiosity (1994) holds that curiosity arises from a perceived gap between what one knows and what one wants to know — a "cognitive induced deprivation," functioning like a drive state (analogous to hunger). Critically, curiosity requires *partial* knowledge, not total ignorance: a small amount of information ("priming dose") is what makes the gap salient and motivating; too little context and there's no felt gap to close, too much and the gap is already closed (satiation).

*Evidence:* G. Loewenstein, "The psychology of curiosity: A review and reinterpretation," *Psychological Bulletin*, 1994; summarized in a 2015 review, "The psychology and neuroscience of curiosity" (PMC4635443).

*Markers:* Does the opening line/frame establish *just enough* context to make a viewer feel there's a specific gap ("wait, how did that happen," "what's the catch") without immediately resolving it? Does the video open with the gap already closed (no reason to keep watching) or with zero context (no gap perceptible, just confusing)?

**2.1.2 Pattern interrupts / in-medias-res openings** [PRACTITIONER LORE for the specific framing, though the underlying attentional-capture mechanism (novelty/salience drawing reflexive attention) is well established in attention research generally]

*Claim:* Opening on an unexpected, mid-action, or visually discontinuous frame (rather than a slow build-up or setup) captures reflexive attention before the viewer has decided to invest deliberate attention.

*Evidence:* Widely repeated across creator-education content and consistent with the general finding that novel/salient stimuli reflexively capture attention (a long-standing, uncontested finding in attention psychology, though the specific short-form-video framing is practitioner lore, not a dedicated study). Specific lift numbers claimed by SEO content ("+23% retention," "58% vs 41%") are **[UNVERIFIED STAT]**.

*Markers:* Does the video start mid-action/mid-sentence/mid-result, or does it start with a slow establishing shot, logo, or "hey guys" preamble?

**2.1.3 The first-second/first-3-second gate is real and platform-enforced, not just folk wisdom** [RESEARCH-BACKED, converging from platform + ad-industry data]

*Claim:* Both platforms structurally treat the opening moment as a distinct, heavily-weighted checkpoint: Instagram's own ranking post foregrounds "watch it all the way through" and industry hook-rate metrics for Meta video ads are literally defined as % of impressions reaching 3 seconds; YouTube's Shorts lead frames the entire feed-based discovery model around whether the first ~1 second earns a few more seconds (§1.2.1).

*Evidence:* YouTube blog Hoyos quote ("you have one second to hook someone"); Meta ads-industry "hook rate" metric definition (3-second-plays ÷ impressions) reported consistently across ad-tech sources (AdManage, Hawky, Vixen Digital) — note this is an *advertising* metric, not confirmed to be identical to organic Reels ranking, but it demonstrates Meta's own systems treat 3-second retention as a first-class, separately measured checkpoint.

*Markers:* Is there anything resolved, promised, or visually striking within the first ~1 second (Shorts) / ~3 seconds (Reels), or does the video "warm up" first?

### 2.2 Berger's STEPPS [RESEARCH-BACKED — practitioner-academic hybrid; Berger is a Wharton marketing professor and STEPPS synthesizes his own and others' peer-reviewed work, but the STEPPS framework itself, as packaged in *Contagious* (2013), is a trade book, not a single peer-reviewed paper]

| Principle | Claim | Marker in a specific video |
|---|---|---|
| **Social Currency** | People share things that make *them* look good, in-the-know, or ahead of the curve to look at. "The better something makes us look, the more likely we are to share it." | Does watching-then-sharing this confer status ("I found this first," "I'm smart/plugged-in for knowing this")? |
| **Triggers** | Content tied to a frequent environmental cue ("top of mind, tip of tongue") gets talked about more because the cue keeps re-activating the memory. | Is the topic linked to something the viewer encounters often (a common object, situation, or recurring event) vs. a one-off niche reference? |
| **Emotion** | "When we care, we share" — physiological arousal (not just positive/negative valence) drives transmission (expanded in §2.3). | Does the video produce a felt emotional spike, or is it emotionally flat/informational-only? |
| **Public** | Visible social proof ("monkey see, monkey do") — if sharing/using something is observable, others imitate it. | Does the content or format make its own popularity visible (trending sound, visible duet/stitch chain, a challenge format)? |
| **Practical Value** | "News you can use" — people share to help others, i.e., useful information has inherent transmission value (expanded in §2.7). | Does the viewer walk away with something they could apply, or is it consumption-only? |
| **Stories** | Information wrapped in a narrative is more memorable and more retellable than the same information as a list of facts, because the story acts as a "Trojan horse" for the information. | Is there a narrative throughline (setup → complication → resolution) or is it a flat list/data-dump? |

*Evidence:* J. Berger, *Contagious: Why Things Catch On* (2013); summarized consistently across Wharton's own coverage (knowledge.wharton.upenn.edu) and multiple book-review sources. Treat STEPPS as a well-regarded synthesis framework, not as six independently peer-reviewed causal claims — the Emotion pillar (2.3) is the one with the strongest direct peer-reviewed backing.

### 2.3 High-arousal emotion and sharing — Berger & Milkman (2012) [RESEARCH-BACKED]

*Claim:* Content evoking high-arousal emotions — positive (**awe**) or negative (**anger, anxiety**) — is significantly more likely to be shared/go viral. Content evoking low-arousal emotions, even negative ones (**sadness**), is *less* likely to be shared, despite sadness being just as "negative" as anger. Positive content is on net more viral than negative content, but arousal — not valence alone — is the operative mechanism: arousal (physiological activation) drives social transmission.

*Evidence:* J. Berger & K. Milkman, "What Makes Online Content Viral?", *Journal of Marketing Research*, Vol. 49, No. 2 (April 2012), pp. 192–205. Methodology: analyzed roughly three months of *New York Times* articles and their appearance on the paper's "most emailed" list, coding each article's evoked emotion and cross-referencing with actual sharing behavior. (SAGE: journals.sagepub.com/doi/10.1509/jmr.10.0353; SSRN preprint: papers.ssrn.com/sol3/papers.cfm?abstract_id=1528077.)

*Markers:* Which specific emotion does the video target — awe/amazement, anger/outrage, anxiety/urgency, amusement (high-arousal positive, well-established separately as a driver of sharing) — versus sadness/calm/contentment (low-arousal, weaker sharing driver even if the content is "good")? A video can be well-made and still under-perform on shares if its emotional register is low-arousal.

### 2.4 Parasocial bonding, mere exposure, and format/face consistency

**2.4.1 Parasocial relationships** [RESEARCH-BACKED]

*Claim:* Parasocial relationships are nonreciprocal socio-emotional bonds viewers form with media figures, where the viewer feels they personally know the creator despite no real relationship. These bonds are strengthened by perceived dialogue/interactivity (replying to comments, direct address to camera) and by self-disclosure (creators sharing personal information/experiences), and they measurably increase trust and downstream behavior (e.g., purchasing).

*Evidence:* Peer-reviewed and academic-thesis sources: MDPI, *Journal of Theoretical and Applied Electronic Commerce Research* ("Influencers' Persuasive Power and Parasocial Relationships in Digital Consumption," 2025); CUNY Academic Works graduate thesis on influencer marketing and parasocial relationships; SSRN paper on parasocial relationships and consumer trust.

*Markers:* Direct camera address ("you")? Recurring, recognizable face/persona across videos rather than anonymous B-roll/voiceover-only? Any self-disclosure or personality signal, vs. purely generic/faceless information delivery?

**2.4.2 Mere exposure effect** [RESEARCH-BACKED, one of the most replicated findings in social psychology]

*Claim:* Repeated exposure to a stimulus — a face, format, sound, or phrase — increases liking for it, even without conscious recognition of having seen it before. First exposures matter most; returns diminish with additional exposure.

*Evidence:* R. Zajonc, *Journal of Personality and Social Psychology Monograph Supplement* (1968); Kunst-Wilson & Zajonc (1980) showed the effect holds even for subliminally-brief exposures; replicated in 200+ studies per Bornstein's 1989 meta-analysis.

*Markers:* Does this video reuse a recognizable intro beat, catchphrase, visual motif, or the same on-camera person as the creator's other videos (compounding familiarity across a body of work), or does every video look/sound like a one-off with no consistent identity?

### 2.5 Identity signaling — sharing as self-presentation

*Claim:* Sharing "useful AI trick" / life-hack / insider-knowledge content functions as **expressive self-presentation** — a way of signaling to one's own network that the sharer is smart, ahead of the curve, or plugged into something valuable, independent of whether the recipient will actually use the information. This overlaps heavily with Berger's Social Currency pillar (§2.2) but is worth separating for grading: the *object being shared* (a genuinely surprising/useful finding) is what makes the *act of sharing it* self-flattering.

*Evidence:* General self-presentation/impression-management theory is well established in social psychology (documented in the search but not tied to a single canonical study specific to "AI trick" content — this specific application is **[PRACTITIONER LORE]** built on a **[RESEARCH-BACKED]** general theory of self-presentation). No dedicated peer-reviewed study of "AI-tip sharing as status signaling" was located; treat the general identity-signaling mechanism as solid and its specific application to AI-tip content as inference, not direct evidence.

*Markers:* Does the content give the sharer something *specific and novel enough* to look smart for surfacing it (a non-obvious trick, an early/underground finding), or is it generic advice the recipient likely already knows (nothing to signal by forwarding it)?

### 2.6 Retention engineering

**2.6.1 Open loops and payoff placement** [PRACTITIONER LORE, well-corroborated in structure but with unverifiable specific lift numbers]

*Claim:* Structuring a video around an unresolved question/tension opened early and resolved late keeps viewers watching because humans are motivated to close perceived gaps (same mechanism as §2.1.1, applied across the whole runtime rather than just the opening). Strong long-form/Shorts creators repeatedly re-open smaller loops throughout the middle of a video and land the biggest payoff near the end rather than early.

*Evidence:* This is a direct runtime-length application of Loewenstein's information-gap theory (§2.1.1, RESEARCH-BACKED for the underlying mechanism). The specific structural template (multiple nested loops, final large payoff) is corroborated qualitatively by the leaked MrBeast production document (see §3, PRACTITIONER LORE — leaked internal doc, not peer-reviewed) which explicitly instructs writers to "hook people at the start... transition to an amazing story... have no dull moments, and then have a satisfying payoff at the end... with an abrupt ending." Specific numeric claims circulating in SEO content ("open loops increase ADV by 40–60%," "1.2% vs 2.8% drop per minute") are **[UNVERIFIED STAT — do not cite]**.

*Markers:* Is there an unresolved question/tension established early that the video is visibly building toward resolving? Is the biggest reveal/payoff near the end (loop closed late) rather than dumped in the first few seconds (nothing left to watch for)? Does the ending land cleanly (loop closed) or just stop/trail off (loop left open, unsatisfying)?

**2.6.2 Silent retention killers: intros, logos, preambles** [PRACTITIONER LORE, directionally consistent with real retention-curve data]

*Claim:* Any non-payoff material placed before the hook resolves (animated logo, "hey guys welcome back," channel branding, subscribe reminders) measurably costs viewers who never return, because it delays the resolution of the curiosity gap the title/thumbnail/first-frame already created.

*Evidence:* Directionally supported by real (non-fabricated) retention-curve data: Wistia's own hosted-video analytics find the steepest engagement drop occurs in a video's opening seconds, worsening for longer videos (wistia.com/learn/marketing/understanding-audience-retention — **[INDUSTRY DATA]**, Wistia's own dataset, not third-party verified but a legitimate video host analyzing its own hosted traffic, unlike the anonymous SEO-blog stats). The specific claims "-8 to -15% for a 3-second logo" and "35% lost in first 10 seconds never recovers by 5:00" are **[UNVERIFIED STAT]** (untraceable to Wistia or any named source, likely SEO-blog invention) — the *direction* (front-loaded non-payoff content costs retention) is credible; the *magnitude* is not.

*Markers:* Count the seconds before the video delivers on its hook/promise or shows anything new — is there dead air, a logo, or a preamble at the start?

### 2.7 Practical value + saveability → distribution

*Claim:* Content offering "news you can use" (STEPPS' Practical Value pillar) is disproportionately **saved** (bookmarked for later reference) rather than just liked, and both platforms treat saves/sends as stronger buying signals than likes because saving/sending requires the viewer to judge the content worth returning to or worth a specific other person's time — a costlier, higher-intent action than a passive like.

*Evidence:* The *direction* (saves/sends > likes as an intent signal) is RESEARCH-BACKED per Instagram's own framing of "likelihood to reshare" as a top prediction target (§1.1.1) and Mosseri's repeated public statements that shares outweigh likes (§1.1.2, PRACTITIONER LORE via convergent secondary reporting but consistent with the official signal). The specific claim that "list content" (recommendation lists, decision frameworks) benchmarks especially high on saves, and the "2–4% save rate is strong / 2% triggers wider test audience" thresholds, are **[UNVERIFIED STAT]** — plausible but untraceable to a disclosed methodology.

*Markers:* Does the video contain something a viewer would plausibly want to find again later (a list, a step-by-step, a reference fact), or is it purely a one-time watch-and-move-on experience? Is there a natural "send this to [specific person]" moment, or is the content too generic to have an addressee?

---

## 3. SHORT-FORM CONTENT ENGINEERING PRACTICE

*Everything in this section is [PRACTITIONER LORE] unless otherwise marked — this is documented creator/agency practice, not academic research, though much of it is a reasonable operationalization of §1–2.*

### 3.1 Documented hook taxonomies

Common categories that recur consistently across creator-education sources (VidIQ, Chaplin, Postlink, Ridge Films) and the leaked MrBeast document:

| Hook type | Mechanism | Example framing |
|---|---|---|
| Bold claim | Confronts an expectation directly | "Everyone is doing X wrong" |
| Confronting question | Forces the viewer to self-locate | "Why does nobody talk about this?" |
| Result-first / demo-in-motion | Shows the payoff before the process (§2.1.1 curiosity gap on *how*) | "Here's what I built" then explains |
| "Nobody is talking about X" | Frames content as hidden/insider knowledge (Social Currency, §2.2) | — |
| In-medias-res | Opens mid-action (§2.1.2) | Starts on the result of an unseen setup |

*Markers:* Which taxonomy bucket does the opening line/frame fall into? Is it a recognizable, deliberate hook type, or a generic/unstructured opening ("so today I want to talk about...")?

### 3.2 Structure templates

*Claim:* The dominant structural template across creator-education sources is **hook → context/stakes → payoff (single or looped)**, with an explicit "one idea per video" discipline for short-form specifically: cramming multiple takeaways into a 15–60 second video is repeatedly flagged as diluting both clarity and shareability, versus a single clean takeaway. Listicle format (multiple mini-payoffs in sequence) is treated as a distinct, valid alternative to single-payoff structure, not a violation of the one-idea rule, provided the "one idea" is the *list itself* (e.g., "5 mistakes," where each item is a sub-payoff within one coherent frame).

*Evidence:* Convergent practitioner sources (Socialync structure guide, multiple short-form agency blogs); the "one idea" framing is stated as consensus best practice across essentially all sources reviewed but is not itself a study.

*Markers:* Can the video's core takeaway be stated in one sentence? If it's a list, is there one unifying frame, or does it wander across unrelated ideas?

### 3.3 Captions, pacing, and audio

**3.3.1 Captions/text overlay** [RESEARCH-BACKED for the underlying "watched muted" premise]

*Claim:* A large majority of social video is watched with sound off, making burned-in captions/text overlay effectively mandatory for message delivery, not just an accessibility nicety.

*Evidence:* Verizon Media & Publicis Media study (2019, n=5,616 US consumers ages 18–54): 69% watch video with sound off in public, 25% with sound off even in private; 80% said they're more likely to watch to completion if captions are present; 80% of caption users report no hearing impairment (i.e., captions are a viewing-preference choice, not primarily an accessibility accommodation). Reported by Forbes (forbes.com/sites/tjmccue/2019/07/31), 3Play Media, and Digiday's earlier (2016) "85% of Facebook video watched without sound" reporting on internal Meta/agency data.

*Markers:* Is the core message legible from on-screen text/captions alone with sound off? Is essential information conveyed only in narration with no matching on-screen text?

**3.3.2 Pacing / cuts-per-second** [PRACTITIONER LORE — the general principle is plausible and near-universal in practice, but essentially every specific number circulating is unverifiable]

*Claim:* Frequent visual change (cuts, camera movement, on-screen graphics, zooms) sustains attention better than long static shots.

*Evidence:* No credible, traceable study was located for any of the specific numbers commonly cited ("cuts every 0.5–1s," "3.3x completion," "change something every 3–5 seconds," "University of Florida 38% retention study" — this last one could not be traced to any real UF study and is very likely a fabricated/mutated attribution common in SEO content; **do not use it**). The general direction (static long-take content underperforms dynamically-edited content in short-form specifically) is consistent with §2.1.2's pattern-interrupt logic and near-universal practitioner consensus, but should be scored qualitatively, not against an invented numeric threshold.

*Markers:* Rough visual-change frequency — does the frame stay static for extended stretches, or is there regular cutting/movement/on-screen graphics? (Score qualitatively: "high/medium/low pacing," not against a fabricated benchmark.)

**3.3.3 Trending audio** [PRACTITIONER LORE]

*Claim:* Using a currently-trending sound plugs a video into the sound's own discovery surface (a dedicated audio page on Reels; sound-based content clustering on both platforms) and platforms are widely believed to boost early distribution for trend-timely audio use, with the effect concentrated in a narrow early window after a sound starts trending (before saturation).

*Evidence:* Consistent across creator-marketing sources (DashSocial, Sprout Social, Conbersa) and aligned with Instagram's own stated signal "information about the reel: the audio track... as well as popularity" (§1.1.1, RESEARCH-BACKED — Instagram does state audio is a ranking input). The specific multipliers ("68% more views," "48% more reach," "3–5x push within 48 hours") are **[UNVERIFIED STAT]**.

*Markers:* Is the audio original, a trending/popular sound, or generic stock music? If trending, was it used near the start of the trend or well past its peak?

### 3.4 Posting cadence, series effects, and CTA design

**3.4.1 Posting cadence** [INDUSTRY DATA]

*Claim:* Higher and more consistent upload frequency correlates with faster channel growth. A large-scale analysis found channels posting 12+ times/month had roughly 4x the median monthly view-growth rate of channels posting less than once a month, with growth rising at each cadence tier in between; separately, channels with a *predictable* schedule reportedly outgrow channels posting the same total volume on random days.

*Evidence:* vidIQ, "How Often to Post on YouTube? We Analyzed 10 Million Channels" (vidiq.com/blog/post/How-Often-Post-on-Youtube/) — vidIQ states the analysis covered 10,210,278 channels (≥1,000 subscribers) over a 12-month window. This is **[INDUSTRY DATA]**: a real, large, disclosed-sample-size dataset, but from a commercial creator-tools vendor with an interest in promoting consistent posting (they sell tools for it), not independently peer-reviewed, and correlational (frequent posters may simply be more skilled/resourced creators generally — the study does not establish causation).

*Markers:* Is this video part of a channel with an identifiable regular cadence, or a one-off/sporadic post? (Cadence is an account-level property, not gradeable from a single video, but note it for context in the post-mortem.)

**3.4.2 Series/format effects** [PRACTITIONER LORE]

*Claim:* A recurring series format ("Episode N of X") builds appointment-viewing habits and is believed to convert to follows/subscriptions at a higher rate than one-off content, though most series reportedly need several installments (commonly cited: 5–8+) before the algorithm/audience recognizes the recurring pattern and begins compounding.

*Evidence:* Consistent across creator-strategy sources (Social Media Examiner, Deloitte's short-form-video industry predictions, various agency blogs); specific multipliers ("3-5x higher follow rate") are **[UNVERIFIED STAT]**. The general "recognition takes several reps" claim is consistent with mere-exposure logic (§2.4.2, RESEARCH-BACKED) even though the specific episode-count threshold is not independently verified.

*Markers:* Does the video signal it's part of a series (numbering, consistent title format, "part X")? Is this a new series (early, unproven) or an established one (later episodes should show format-recognition payoff)?

**3.4.3 CTA design and comment-automation tools (ManyChat etc.)** [split — mechanism RESEARCH-BACKED via §1.3.2, tool usage PRACTITIONER/VENDOR DOCUMENTATION]

*Claim:* Tools like ManyChat let creators auto-DM anyone who comments a specific keyword ("comment 'GUIDE' for the link"), converting a comment into a lead-capture/DM funnel. This both drives comment volume (an engagement signal) and sends (a top-ranked signal, §1.1.2) simultaneously — but bare, content-free versions of this mechanic ("comment YES") are the literal example Instagram names as prohibited engagement bait (§1.3.2).

*Evidence:* Mechanism/product behavior confirmed directly from ManyChat's own documentation (help.manychat.com, manychat.com/blog — vendor documentation, not independent verification of effectiveness). The bait-penalty risk is confirmed by Instagram's own guidelines (§1.3.2, RESEARCH-BACKED). No independent study on net reach effect (comment-automation lift vs. engagement-bait penalty) was located — this is a real tension the evidence does not resolve either way.

*Markers:* If a comment-keyword CTA is present, is it attached to genuinely valuable content the video already delivers (compliant, likely fine) or is the comment itself the *only* thing being asked for with no standalone value (likely flagged as bait per §1.3.2)?

---

## 4. WHAT SEPARATES MEGA-CREATORS FROM SUB-100K CREATORS

| Factor | Claim | Evidence tier | Markers |
|---|---|---|---|
| **Consistency/cadence** | Regular, predictable posting outperforms sporadic posting at the same total volume; higher-frequency tiers show materially faster growth | [INDUSTRY DATA] §3.4.1 | Channel-level, not single-video — note as context |
| **Format ownership** | A recognizable, repeated format/persona compounds via mere exposure (§2.4.2) and parasocial bonding (§2.4.1), both RESEARCH-BACKED mechanisms, even though "format ownership" as a named practitioner concept is not itself a study | [RESEARCH-BACKED mechanism / PRACTITIONER LORE framing] | Does this creator have a recognizable signature (recurring visual style, catchphrase, persona) distinct from generic genre content? |
| **Niche → broad laddering** | Documented case pattern (Ali Abdaal: narrow niche → adjacent broadening → broad brand, each expansion audience-tested before scaling) vs. MrBeast's alternative path of universal spectacle with no niche phase | [PRACTITIONER LORE — single case studies, not a controlled comparison] | Is this creator/video staying within an established, tested niche, or attempting an untested broad swing? |
| **Packaging discipline (title/thumbnail/first-frame)** | For long-form, thumbnail+title changes are reported to move CTR substantially, and top creators test them as a unit; for Shorts specifically, packaging is largely *moot* — the in-video first-second hook replaces it (§1.2.3, RESEARCH-BACKED distinction) | [INDUSTRY DATA for long-form CTR figures / RESEARCH-BACKED for the Shorts-vs-long-form distinction] | For a Short: judge the first-frame/first-second, not a thumbnail. For long-form or a Reel that also circulates as a link/embed: judge title+thumbnail as a unit |
| **Velocity of trend response** | Widely believed that early adoption of a trending sound/format captures disproportionate algorithmic push before saturation (§3.3.3) | [PRACTITIONER LORE, specific multipliers UNVERIFIED] | Was a trend/sound/format used near its emergence or well after peak/saturation? |

---

## 5. VIRAL POST-MORTEM CHECKLIST

*One page, applicable to any single Reel or Short. Score each item; note evidence tier in parentheses so low-confidence items don't get over-weighted relative to research-backed ones.*

**Hook (0–1s Shorts / 0–3s Reels)**
1. Does the video deliver a visible payoff, promise, or unresolved gap within the first second (Shorts) / three seconds (Reels)? (RESEARCH-BACKED — §1.2.1, §2.1.3)
2. Is the opening frame in-medias-res / a pattern interrupt, rather than a slow build-up or preamble? (PRACTITIONER LORE — §2.1.2)
3. Is there a real information/curiosity gap established (not fully resolved, not totally context-free)? (RESEARCH-BACKED — §2.1.1)
4. Is any non-payoff material (logo, "hey guys," channel branding) placed before the hook resolves? (Penalize if yes — §2.6.2)

**Retention / structure**
5. Can the video's core takeaway be stated in one sentence ("one idea" discipline)? (PRACTITIONER LORE — §3.2)
6. Is there a clear hook → context/stakes → payoff arc, or a coherent list structure? (PRACTITIONER LORE — §3.2)
7. If loops/questions are opened mid-video, are they closed before the video ends? (RESEARCH-BACKED mechanism, PRACTITIONER LORE structure — §2.6.1)
8. Does the ending land (loop closed / satisfying beat) or just stop/trail off?
9. Is pacing dynamic (cuts, movement, on-screen graphics) rather than long static takes, appropriate to the content type? (PRACTITIONER LORE — §3.3.2; score qualitatively, no numeric benchmark)

**Emotional/psychological engine**
10. Which specific emotion is this video primarily targeting: awe, anger/outrage, anxiety/urgency, amusement (all high-arousal, share-favorable) — or sadness/calm/neutral-informational (low-arousal, share-unfavorable)? (RESEARCH-BACKED — §2.3)
11. Does the content confer status/social currency on whoever shares it ("this makes me look smart/ahead/in-the-know")? (RESEARCH-BACKED framework — §2.2, §2.5)
12. Is there a specific, addressable "send this to ___" moment, or is the content too generic to have a mental addressee? (RESEARCH-BACKED direction — §1.1.2, §2.7)
13. Does the video offer standalone practical/reference value (something worth saving), independent of entertainment value? (RESEARCH-BACKED direction — §2.7)

**Format/identity**
14. Does the creator's face, voice, or persona appear consistently enough across videos to build parasocial/mere-exposure compounding, or is this a one-off anonymous piece? (RESEARCH-BACKED mechanism — §2.4)
15. Is this video part of a legible series/recurring format (numbering, consistent structure), or a standalone? (PRACTITIONER LORE — §3.4.2)
16. Is trending/topical audio used, and if so, is the trend fresh or stale? (PRACTITIONER LORE — §3.3.3)

**Platform compliance / hygiene (binary — these are officially documented penalties)**
17. Third-party watermark visible (CapCut/TikTok/other)? (Penalize if yes — RESEARCH-BACKED, §1.3.1)
18. Resolution below platform-native quality, or visible compression artifacts? (Penalize if yes — §1.3.1)
19. Black bars/borders present, or audio muted with no reason? (Penalize if yes — §1.3.1)
20. Is the video majority static on-screen text rather than visual/motion content? (Penalize if yes — §1.3.1)
21. Has this exact file been posted before on this account? (Penalize if yes — §1.3.1)
22. Does the caption/on-screen text contain bare engagement bait ("comment YES," "like if you agree") with no standalone content value behind it? (Penalize if yes — §1.3.2)
23. Captions/text-overlay present and sufficient to convey the core message with sound off? (RESEARCH-BACKED — §3.3.1)

**Packaging (context-dependent — apply #24 only if relevant)**
24. *[Shorts/Reels-in-feed only, skip for embeds/links]:* Is production effort correctly allocated to the in-video hook rather than a thumbnail (thumbnails are largely irrelevant for feed-native Shorts/Reels consumption)? (RESEARCH-BACKED distinction — §1.2.3)
25. CTA present: if so, is it attached to content with standalone value (compliant) or is the comment/follow itself the entire ask (bait risk — cross-reference #22)? (§3.4.3)

---

## Source list (for reference)

**Peer-reviewed / academic**
- Berger, J. & Milkman, K. L. (2012). "What Makes Online Content Viral?" *Journal of Marketing Research*, 49(2), 192–205. journals.sagepub.com/doi/10.1509/jmr.10.0353 ; SSRN: papers.ssrn.com/sol3/papers.cfm?abstract_id=1528077
- Loewenstein, G. (1994). "The psychology of curiosity: A review and reinterpretation." *Psychological Bulletin.* Summarized in: pmc.ncbi.nlm.nih.gov/articles/PMC4635443 ("The psychology and neuroscience of curiosity")
- Zajonc, R. B. (1968). "Attitudinal effects of mere exposure." *Journal of Personality and Social Psychology Monograph Supplement.* psy.lmu.de/allg2/download/audriemmo/ws1011/mere_exposure_effect.pdf ; Kunst-Wilson & Zajonc (1980); Bornstein (1989) meta-analysis, per en.wikipedia.org/wiki/Mere-exposure_effect
- Parasocial relationships: MDPI *JTAER* (2025), "Influencers' Persuasive Power and Parasocial Relationships..."; CUNY Academic Works thesis; SSRN paper on parasocial trust

**Trade book (practitioner-academic hybrid)**
- Berger, J. (2013). *Contagious: Why Things Catch On.* STEPPS framework — summarized via knowledge.wharton.upenn.edu and multiple book reviews.

**Official platform sources**
- Meta/Instagram: "Instagram Ranking Explained," about.instagram.com/blog/announcements/instagram-ranking-explained
- Instagram Help Center: "Recommendation eligibility on Instagram," help.instagram.com/653964212890722
- Instagram Recommendation Guidelines (quoted via Buffer's official Threads post)
- YouTube official blog: "YouTube Shorts deep dive: A conversation with product lead Todd Sherman and creator Jenny Hoyos," blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/

**Industry data (vendor-disclosed datasets, not peer-reviewed)**
- vidIQ, "How Often to Post on YouTube? We Analyzed 10 Million Channels," vidiq.com/blog/post/How-Often-Post-on-Youtube/
- Wistia, "Understanding Audience Retention," wistia.com/learn/marketing/understanding-audience-retention
- Verizon Media & Publicis Media (2019) captions/sound-off study, as reported by Forbes (forbes.com/sites/tjmccue/2019/07/31) and 3Play Media

**Practitioner / secondary (leaked docs, convergent blog reporting)**
- Leaked MrBeast production document, as reported by simonwillison.net/2024/Sep/15/how-to-succeed-in-mrbeast-production/ and alexanderjarvis.com — leaked internal doc, not an official public statement
- Mosseri statements on sends/shares as top signal — convergent secondary reporting only (Torro, DataSlayer, Socialync, David Zucker's newsletter); no primary transcript located
- Ali Abdaal niche-to-broad case study — multiple creator-economy blogs, single-case, not controlled comparison
- ManyChat product documentation — help.manychat.com, manychat.com/blog

**Explicitly flagged as unverifiable — do not cite as fact in grading**
- "University of Florida" 38% editing-retention study (untraceable, likely fabricated/misattributed)
- "3.3 billion Shorts analyzed" study behind the 70–90% viewed-ratio claim (source not named anywhere it's cited)
- Specific percentage lifts for: pattern interrupts, cuts-per-second, logo-animation cost, open-loop retention lift, trending-audio view/reach multipliers, series follow-rate multiplier, save-rate thresholds
