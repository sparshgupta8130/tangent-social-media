# Instagram — Reels Platform Mechanics & Compliance

Load this before scripting, critiquing (lens 8), or filling `publish.md` for any IG item.
Sources: `research/03_virality_science.md` §1.1/§1.3 (mechanics, tiered [RESEARCH-BACKED] /
[PRACTITIONER LORE] / [UNVERIFIED STAT]) and the July-2026 platform-ops research brief
(tiered [HIGH]/[MED]/[LOW]/[UNVERIFIED], cited inline as `[ops-brief]` = `research/briefs/platform_ops_2026-07.md`).

## 1. Ranking signals

**The four official signal families** [RESEARCH-BACKED — Mosseri, "Instagram Ranking
Explained," about.instagram.com/blog/announcements/instagram-ranking-explained]: (1) your own
activity — reels liked/saved/reshared/commented/engaged recently; (2) your history with the
poster; (3) information about the reel — audio/visuals and general popularity; (4) information
about the poster — followers and engagement level. Instagram states the actions it weighs
heaviest are: **likelihood to reshare, likelihood to watch all the way through, likelihood to
like, likelihood to visit the audio page.**

**Watch-through / likes / sends-per-reach as the "big three"** [PRACTITIONER LORE, convergent —
not a single citable Mosseri transcript]: multiple outlets attribute to Mosseri that watch time,
likes-per-reach, and sends-per-reach are the top-weighted 2025-26 factors, with **sends weighted
several times higher than likes for reach among non-followers**, while likes matter more for
reach among existing followers. Treat the *direction* (sends > likes for cold reach) as credible
— it's consistent with the official "likelihood to reshare" emphasis above — but the specific
multiplier claims are **[UNVERIFIED STAT] — do not cite as fact.**

**The audition / test-audience model** [PRACTITIONER LORE, consistent with the official
mechanism]: new Reels go to a small test audience first; strong early watch-time/saves/shares
expand distribution in waves. A commonly cited window is 30-90 minutes — **[UNVERIFIED STAT]**,
no official minute-count found. Operational implication: the hook and caption must convert the
*first* wave (people who already follow similar accounts), since that wave gates the second.

## 2. Official penalty list (verbatim) — binary, lens-8 checks

Instagram's Recommendation Guidelines state it makes certain Reels **less visible**, quoted
directly: *"low-resolution or watermarked reels, reels that are muted or contain borders, reels
that are majority text, or reels that have already been posted on Instagram."*
[RESEARCH-BACKED — about.instagram.com/blog/announcements/instagram-ranking-explained;
help.instagram.com/653964212890722]. Checklist: third-party watermark visible? Below-1080p or
compression artifacts? Black bars/borders? Majority static text over motion? File hash already
published (repost guard, `tools/hygiene_check.py`)?

**Engagement-bait policy** [RESEARCH-BACKED, direct quote]: Recommendation Guidelines list
*"content that users broadly tell us they dislike, including clickbait, engagement bait, or
which promotes a contest or giveaway"* as ineligible for Explore/Reels tab/Suggested Posts.
"Comment YES if you agree" is the named canonical example.

### THE LINE (our compliance doctrine)

Bare engagement bait ("comment YES," "tag 3 friends") has **no standalone content value** — it
is the entire ask. A keyword-CTA gating a **real deliverable** (prompt, preset, process PDF) is
different in kind: the automation delivers something concrete via opt-in DM, not just farmed
vanity engagement. **Caveat, kept visible**: Meta's official transparency doc does **not itself**
carve out this exception — the distinction comes from DM-automation-vendor and marketing sources,
not confirmed policy text [MED/partially UNVERIFIED — ops-brief §5]. Operating rule: every
funnel CTA must be *specific and earned by the content* (tied to a real question/offer the post
raises), never a generic templated ask repeated post after post — repetition risks pattern-match
as bait regardless of whether a DM deliverable exists [MED — ops-brief §5]. Follow/like-gating a
contest is confirmed prohibited; the "low-intent signal suppression" penalty mechanism itself is
[PRACTITIONER LORE].

## 3. Current specs [ops-brief §1]

- Export: **1080×1920, 9:16**, H.264, 30fps, ≤4GB [HIGH/MED].
- Length: in-app camera caps ~3 min; uploaded files can go longer but **content actually pushed
  to non-followers via Explore/Reels tab is effectively capped ~3 min** — treat 3 min as the
  real reach ceiling [MED]. No official hard number for the *ideal* hook-driven length was
  found; 7-15s target / 90s hard cap for algorithmic reach is **[LOW/UNVERIFIED]** inference,
  not an official Meta figure.
- Safe zones: keep critical text/graphics out of **top ~250px / bottom ~350px** (center safe
  ≈1010×1440); leave **right ~10%** clear of the like/comment/share rail [MED]. 2026 grid crop
  moved to ~3:4 rectangular — keep critical cover elements in the middle ~60% [MED].
- Caption: hard limit **2,200 chars**; only the **first ~125 chars** show before "more" — write
  that first line as the real headline [HIGH].
- Hashtags: **≤5**, Meta's own recommendation is 3-5 highly relevant tags; Mosseri: *"hashtags
  are not a way to get more reach"* — they're for searchability, not distribution. What actually
  drives reach: caption keywords, on-screen text, watch time, shares, saves [HIGH].
- Cover: upload a dedicated 1080×1920 cover frame, don't rely on an auto-picked one [MED].

## 4. Trial Reels [ops-brief §1]

Publishes hidden from your own followers, shown first to non-followers via Reels
feed/Explore; after ~72h Instagram decides whether to auto-share to your grid
[HIGH — creators.instagram.com/blog/instagram-trial-reels]. **Eligibility gotcha**: secondary
sources consistently report a **public account with ≥1,000 followers** requirement; the official
post itself doesn't state a number [MED/UNVERIFIED]. **Implication for tangentideas.ai: not
usable pre-1K followers — don't build early strategy around it.**

## 5. Edits app [ops-brief §1]

Meta's own editor: records up to 10 min, 4K, **exports watermark-free** (beta extends to ~15
min) [MED]. **Myth correction**: Instagram does NOT penalize content merely for third-party
editing — the actual trigger is a **visible watermark**. Editing in ffmpeg (our pipeline) or
Edits both avoid the penalty as long as export is watermark-free [MED]. 2026 crackdown targets
**content-aggregator accounts** (reposted content); cosmetic tweaks (watermark removal, speed
change) don't count as "original" — our all-original pipeline is structurally safe here.

## 6. Audio rules [ops-brief §1, §3a]

Trending/native audio **must be selected in-app** — there is no API path to attach Instagram's
music-library audio to a Graph-API-published Reel; audio must already be baked into the exported
file for any API publish [HIGH for cover param / MED for audio limitation]. **Creator accounts**
get full trending-audio library access; **Business accounts** are restricted to the ~14,000-track
Meta Sound Collection with no trending songs — a real reach handicap [MED]. This is why
tangentideas.ai runs Creator, not Business (see `publishing-ops.md` §1).

## 7. AI-labeling on IG

Meta auto-applies an **"AI Info" label** when it detects industry-standard AI indicators (C2PA
metadata) or the creator self-discloses; Meta states its detection "methodology is still
evolving" and may miss undisclosed AI content [HIGH — transparency.meta.com]. 2026 update: **ads**
now carry a mandatory AI-label rule (significant-modification threshold); no equivalent hard
organic-post penalty schedule was found [MED]. **Our stance: disclosure-first regardless** — use
the built-in AI-content disclosure option on every [GEN]-tagged asset per
`knowledge/audience/positioning.md`, rather than risk an automatic flag with unknown downstream
consequences.

## 8. Funnel mechanics — evidence summary

Comment-keyword→DM is Instagram's signature compliant automation pattern **because the trigger
is the user's own opt-in action** (commenting the keyword), not a cold blast [HIGH —
ops-brief §5]. Convergent with Mosseri's sends-signal emphasis (§1 above): a DM funnel generates
both a comment (engagement signal) and a send (top-ranked signal) simultaneously
[RESEARCH-BACKED mechanism / vendor-documented tool, §3.4.3 virality_science]. **ManyChat holds
official Meta Business Partner certification** — connects via approved Graph/Messenger API, not
scraping [HIGH — ops-brief §5]. Compliant setup requirements: (1) trigger must be the user's own
comment/keyword, never cold-DM; (2) deliverable must be real and instant-delivered; (3) no URL
shorteners (bit.ly etc.) — Meta actively deboosts/flags these in 2026 [MED]; (4) start on
ManyChat's free tier (25 active contacts) to validate the mechanic before paying. Full setup
steps live in `publishing-ops.md` §5.
