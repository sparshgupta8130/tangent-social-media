# YouTube — Shorts + Long-Form Platform Mechanics

Load this before scripting/critiquing/publishing any YT item. Sources:
`research/03_virality_science.md` §1.2 (tiered [RESEARCH-BACKED]/[INDUSTRY DATA]/
[PRACTITIONER LORE]) and the July-2026 platform-ops research brief (`[ops-brief]` = `research/briefs/platform_ops_2026-07.md`, tiered
[HIGH]/[MED]/[LOW]/[UNVERIFIED]); genre-lane law from the corpus distillation
(`knowledge/pattern-library.md`, `[CORPUS: yt_curiousrefuge]`); AI-disclosure penalty from the
July-2026 production-stack research brief (`[stack-brief]` = `research/briefs/production_stack_2026-07.md`).

## 1. Shorts: the hook metric

**"Viewed vs. Swiped Away" is THE hook-quality metric** [RESEARCH-BACKED]. Unlike long-form,
~99.9% of Shorts views originate from the algorithmic feed, not a deliberate click — so YouTube
built a distinct metric (visible in Shorts Analytics) measuring whether a Short is watched or
immediately swiped. Shorts product lead **Todd Sherman** and creator **Jenny Hoyos** describe
this directly on YouTube's own blog ("YouTube Shorts deep dive," blog.youtube). Direct quotes:
Hoyos — *"you have one second to hook someone, especially on Shorts"*; Sherman — *"On short-form,
people are swiping through a feed, and discovering things as they go. That's one important
difference."* Marker: is there a legible payoff/promise visible in the first frame or first
spoken word — nothing to click, so nothing to sell except the next second?

**Explore→exploit seeding** [INDUSTRY DATA for thresholds, RESEARCH-BACKED for mechanism]:
YouTube seeds a Short to a small topic-affinity test cohort (hundreds to low thousands),
independent of subscriber count, and expands distribution if retention/rewatch/like behavior is
strong. Specific completion-rate cutoffs circulating ("70%+ excellent," "below 30% kills
distribution") are **[INDUSTRY DATA/UNVERIFIED]** — vendor-repeated, no disclosed methodology.
Treat the *direction* as reliable, the *exact cutoffs* as heuristics only.

## 2. Specs [ops-brief §2]

- Max length **3 minutes** (raised from 60s, Oct 2024) [HIGH].
- **9:16, 1080×1920** — same canvas as Reels [HIGH].
- Title/description: no confirmed new Shorts-specific limits found beyond the long-standing
  100-char title / 5,000-char description caps [LOW/UNVERIFIED — not re-confirmed this pass].

## 3. Thumbnails-irrelevant-for-Shorts rule (effort allocation)

**The structural difference**: long-form recommendations are a deliberate choice from a grid
(title/thumbnail drive the click); Shorts recommendations are a continuous swipe feed with no
comparable choice moment — the entire selection burden moves onto the in-video hook
[RESEARCH-BACKED — same Hoyos/Sherman source]. **Action item**: do not spend producer/critic
effort on a Shorts thumbnail — that effort belongs on frame 0 and the first spoken word. Score
this in critique lens 1 (HOOK) and lens 7, never penalize a Short for a "weak thumbnail."

## 4. Related-video link (Shorts→long-form)

Lets a Short surface/link to a related long-form video, livestream, or Short from the same
channel, set in YouTube Studio → Content after upload; linked video must be public/unlisted and
Guidelines-compliant [HIGH — official YouTube Help, "Add a related video to your YouTube
Shorts"]. 2026-06-26 UI change moved the placement under on-screen text and dropped the
"Related Video" label — viewers just see channel/title/song [MED]. **This is the primary
in-platform lever for Shorts→long-form conversion — standard step on every Short's publish
checklist once a paired long-form video exists** (see `publishing-ops.md` §3).

## 5. Long-form: packaging matters here

Unlike Shorts, **title + thumbnail packaging genuinely drives long-form CTR** and top creators
test them as a unit [INDUSTRY DATA for CTR figures / RESEARCH-BACKED for the Shorts-vs-long-form
distinction]. Retention discipline still applies throughout the runtime — front-loaded
non-payoff material (intros, logos, "hey guys," subscribe reminders) measurably costs viewers who
never return, directionally supported by real (non-fabricated) hosted-video retention-curve data
[INDUSTRY DATA — Wistia]. Specific percentage-lift numbers for logo/intro cost are
**[UNVERIFIED STAT] — do not cite.**

## 6. The genre-lane inversion law [CORPUS: yt_curiousrefuge]

Art-spectacle content (finished, polished, wordless side-by-side comparisons, trailer-style
reveals) **wins on long-form** — Curious Refuge's single highest-performing video across the
whole 13-video dossier is a 4.4M-view long-form trailer piece, ~152x the long-form median.
Process-demo content (tool comparisons, quick workflow reveals) performs better as native
**Shorts**. This inverts the naive assumption that "spectacle = short, process = long" — for our
lane specifically: finished-art reveals go long-form, process/workflow reels go Shorts (matches
`STRATEGY.md` §5's lane-fit rule and BET-4).

## 7. Audio licensing [ops-brief §2]

The in-app **Shorts audio library** is licensed **only for videos under 60 seconds** — using
that same audio in a Short 60s-3min (or long-form) risks a Content ID claim, and any claim on a
Short over 60s risks a **global block**, not just demonetization [MED]. Given our pipeline is
API-upload (no live in-app trending-audio picker access anyway), bake in only: YouTube Audio
Library-cleared tracks, Creator Music (revenue-share), or fully-owned/AI-generated audio.

## 8. AI altered-content disclosure

Official policy (March 2024, still current): disclose when content is **"realistic" and could
be mistaken for a real person/place/event** (face replacement, synthesized voice, real place/
event doing something it didn't). **Exempt**: production-assistance AI (scripts, captions,
titles), clearly unrealistic/animated content, minor edits, standard effects
[HIGH — blog.youtube, official]. Disclosure via upload flow → "Altered content" → adds a
"Modified or Synthetic" label; voluntary disclosure does **not** hurt reach, search, or
monetization per YouTube's own statement [HIGH].

**Enforcement escalation — the risk we hedge against**: as of **May 2026**, YouTube rolled out
**automatic AI detection** (SynthID-aware + classifier-based) that can apply the label even
without creator disclosure. First violation of the non-disclosure rule = warning + education;
**second violation = 90-day monetization suspension** [HIGH — `stack-brief` §4, Memeburn/ytzolo
policy summaries]. **Action item: self-disclose every [GEN]-tagged asset (Veo/Flow b-roll, TTS
narration) via the native toggle on every upload** — this is materially cheaper than risking a
suspension from auto-detection catching an undisclosed asset. See
`production/genvideo-playbook.md` for the disclosure-integration mechanics.

## 9. Monetization thresholds (YPP, 2026) [HIGH — ops-brief §2]

- **Standard tier** (full ad revenue): 1,000 subscribers + (4,000 public watch hours/trailing
  12mo **OR** 10M public Shorts views/trailing 90 days).
- **Expanded/early tier** (Fan Funding only): 500 subscribers + (3,000 watch hours **OR** 3M
  Shorts views/90 days).
- Shorts watch-time does **not** count toward the 4,000-hour long-form bucket — separate,
  alternate paths, not additive. Also requires 2-step verification, no active strikes; approval
  review 1-4 weeks after thresholds met.
- **Strategic note**: because Shorts-views and long-form watch-hours are separate qualifying
  tracks, a Shorts-heavy channel can reach monetization via the 3M/10M Shorts-view path alone —
  relevant to our dual Shorts+long-form strategy.

## 10. CTA grammar on YT

Per `STRATEGY.md` §5: **"full build on the channel"** (or equivalent verbal redirect to
long-form/related-video link) — **never** the IG keyword-DM mechanic. YouTube comments lost the
ability to carry clickable links as of the Aug-2025 change [MED — ops-brief §2], so a Short's
CTA must point verbally/on-screen to the related-video link or channel, not a comment-triggered
funnel. Deliverable capture on YT routes through the long-form video's description, not the
Short itself.
