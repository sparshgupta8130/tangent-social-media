# Publishing Operations — The Concrete Ops Manual

Backs `templates/publish.md` and the `/publish` and `/postmortem` skills. Every claim here
carries the July-2026 platform-ops research brief's confidence tag (`[HIGH]`/`[MED]`/`[LOW]`/
`[UNVERIFIED]`, `[ops-brief]` = `research/briefs/platform_ops_2026-07.md`) unless otherwise cited. Read alongside `knowledge/platform/
instagram.md` and `knowledge/platform/youtube.md` (specs/penalties) — this file is HOW we
execute, those are WHAT the platforms reward/punish.

## 1. Account setup decisions

- **Instagram: Creator professional account, not Business.** Both are "professional" (analytics/
  ads/API), free, switchable without losing followers [HIGH]. The dividing line for API access
  is Personal-vs-Professional, not Creator-vs-Business [HIGH — Meta for Developers, resolves
  conflicting secondary claims]. Creator wins because it retains the **full trending-audio
  library**; Business is capped at the ~14,000-track Meta Sound Collection with no trending
  songs — a real reach handicap for a content-first account [HIGH/MED].
- **Link a Facebook Page at setup**, even a minimal unused one. Not strictly mandatory for a
  professional account, but Insights and the full API feature set require it in practice; no
  2026 policy change removes this linkage [MED]. One-time low-cost step, no found downside.
- **ManyChat: start on the free tier** (25 active contacts, 2 channels) to validate the
  comment-keyword→DM mechanic mechanically works before paying [HIGH — official Meta Business
  Partner]. Re-evaluate against Chatfuel only once contact volume outgrows the free tier — cost
  curves diverge by audience size, not features.
- **Skip the "warmup ritual."** Specific day-count warmup schedules ("7-14 days," "10-21 days")
  circulating in creator blogs are **[LOW/UNVERIFIED]**, sourced to no Meta statement. The two
  well-corroborated real restriction triggers are: third-party engagement-automation (auto-like/
  auto-follow/auto-comment — distinct from our compliant ManyChat/API stack) and posting
  duplicate/near-duplicate clips across multiple accounts (fingerprint-detected) [MED].

## 2. Publishing paths — ranked by automation depth

**P1 — Manual in-app posting (trending-audio posts).** Required whenever a post rides native
IG trending audio, because **no API path can attach Instagram's music-library audio to a
Graph-API-published Reel** — audio must already be baked into the file for any API publish
[HIGH for cover param / MED for audio limitation]. Use for HERO/format-audition items where
trend-timeliness matters.

**P2 — IG Graph API standard-access self-publish (non-trend posts).** Requirements: Meta
developer registration, an app in Meta App Dashboard, IG account must be Business or Creator
(professional). **Standard Access (publishing only to our own account) needs NO App Review and
NO Business Verification** — those are Advanced-Access-only requirements for managing other
accounts [HIGH]. Permission: `instagram_business_content_publish` (Business Login for Instagram)
or `instagram_content_publish` (Facebook Login for Business). **Rate limit**: officially
`4,800 × trailing-24h impressions on the account` [HIGH for the formula] — for a low-follower new
account this can functionally cap publishes to a modest handful/day early on, loosening as
impressions grow; flat-number folk-caps (25/50/100 posts/24h) circulating are **[MED]**,
conflicting between sources, treat as directional only. Can set `cover_url` (or `thumb_offset` —
`cover_url` wins if both set) [HIGH]. **Audio must be pre-baked into the render** — this is the
non-trend, non-audio-critical path.

**P3 — Meta Business Suite scheduling.** Free, web + mobile, no third-party app. Scheduling
window and post-count figures conflict between sources (20min-29 days vs. 25 posts/day over 75
days) — likely reflect different surfaces (Stories vs. feed/Reels); treat cautiously [MED]. A
90-second Reel cap noted for Business Suite specifically looks stale against the 3-min Reels
cap [LOW/UNVERIFIED]. Use as the human-reviewable calendar/queue layer on top of P2, not as the
primary automation mechanism. **Recommended default**: P2 (Graph API, Standard Access) with a
free-tier scheduler (Buffer 3 channels/10 posts, or Metricool 50/month) as the queue UI on top
[Synthesis — MED confidence] — reserve P1 for every trend-audio post.

**YT upload path.** Use the **YouTube Data API v3** directly (first-party, well-documented).
**Hard gotcha, must clear before going live**: any video uploaded via `videos.insert` from an
**unverified API project** is automatically locked to **private regardless of requested privacy**
— public visibility requires passing Google's **API Audit** for that project, with no per-video
appeal [HIGH — Google Help Center, "Videos locked as private"]. **Action item: complete the API
Audit / project verification BEFORE any automated upload goes live** — until then, **manual
Studio upload is the default path**, not a fallback. Quota: default project gets 10,000
units/day; `videos.insert` reportedly dropped to ~100 units/call (Dec 2025) with uploads drawing
from a separate ~100-call/day bucket since June 2026 [MED — recent policy changes, not
independently cross-checked against an official Google changelog — **verify against your own
Cloud Console before depending on this figure**].

## 3. Analytics collection protocol

- **IG Insights API**: media-level `impressions`/`reach`/`engagement`, plus (per secondary
  sources) `saves`/`shares`/video views [MED — official overview page not exhaustive]. 2026
  deprecated `Media impressions`/`Reel plays`/`Reel replays`/`Reel initial plays` into a unified
  **"Views"** metric; added `Profile reposts`, `Reposts`, and **`Reels skip rate`** — the
  closest available **retention proxy** (no true retention curve or average-watch-time field
  exists via API) [MED]. **Retention window**: in-app Insights dashboard shows only trailing
  **90 days**; the API/data-connector layer retains **up to 2 years**. Pull and store API data on
  a schedule — don't rely on the app for historical trend data.
- **YT Analytics API**: confirmed fields — `estimatedMinutesWatched`, `averageViewDuration`,
  `averageViewPercentage`, `views`, `engagedViews`, `audienceWatchRatio`,
  `relativeRetentionPerformance`, segment `startedWatching`/`stoppedWatching` [HIGH]. **No
  Shorts-specific "swiped away" field is documented in the API** — that number lives only in the
  **Studio UI's Shorts analytics panel**; pull it manually there, use `averageViewPercentage` +
  segment retention via API as a proxy elsewhere [HIGH for the API gap].
- **Fallback exports**: Meta Business Suite → Ads Reporting → CSV/PNG/PDF; YouTube Studio →
  Analytics → Advanced Mode → CSV. Use for cross-checks or if API pulls lag.
- **Weekly `posts.csv` update procedure**: after each `/postmortem`, append a row to
  `ops/calendar/posts.csv` matching the schema in `tools/README.md` exactly —
  `date,platform,url,pillar,views,likes,comments,shares,saves,funnel,followers_at_post`
  (integers, blank = 0; `funnel` is `0`/`1` for whether the comment-keyword-DM mechanic is live
  on that post). This file feeds `tools/metrics.py efficiency|report` and the weekly-review
  medians in `benchmarks.md`.
- **Second-source verification rule** [`research/QC_PROTOCOL.md` standing rule]: **no number
  enters a postmortem single-sourced.** Every claimed stat runs through
  `python tools/verify_stats.py --url <post_url> --views N --likes N --comments N` before it's
  written down — >10% divergence = `FAILED-VERIFICATION`, must be resolved before the postmortem
  ships. This exists because the corpus's own browser-scraped instrument was wrong on likes
  ~45% of the time (1.8x-453x off) — a documented failure mode, not a hypothetical one.

## 4. DM automation setup

ManyChat comment-keyword→DM flow: user comments the keyword on a live post → ManyChat (Meta
Business Partner, Graph/Messenger API, not scraping) auto-DMs the deliverable link/file
[HIGH — ops-brief §5]. **Opt-in requirement**: the trigger must be the user's own comment/
story-reply/keyword DM — cold DM blasting non-opted-in users is the fastest path to a ban [MED].
**Deliverable hosting**: host the real asset (prompt text, preset file, process PDF) somewhere
stable and directly linkable — never a URL shortener (bit.ly/tinyurl are actively deboosted/
flagged by Meta in 2026) [MED]. Before shipping any funnel post, **test the automation live**
(comment the keyword yourself, confirm instant delivery) — the `publish.md` pre-post checklist
gates on this. See `knowledge/platform/instagram.md` §8 for THE LINE governing what makes a
keyword-CTA compliant vs. bare bait.

## 5. Email capture (week-1, non-negotiable)

Email capture is wired before the first post, and list growth is a first-class weekly metric
from item #1 — not a "someday" feature. Rationale: product/subscription revenue needs 1–2
years of audience-trust lead time, and the measured median email subscriber is worth
$4.40/YEAR (not the "$1/month" folklore) — so the list must start compounding earlier and
scale bigger than a "popup once we have an audience" plan allows
[REPO: research/briefs/revamp-2026-08/monetization_economics.md, design-implications §1].
Sequencing and P&L ownership: `strategy/REVENUE.md` §2 (revenue-lead).

- **Link-in-bio → landing page.** The IG bio link and the YT channel link both point at a
  single capture surface (the ESP-hosted landing page until anything better exists). **ESP
  choice: DEFERRED but shortlisted — Beehiiv or Substack, both on free tiers**
  [REPO: research/briefs/revamp-2026-08/subscription_inventory.md, tooling-matrix row (g)];
  decided by Sparsh at week-1 setup or the first `/revenue-review` (account creation is his;
  free tier means no spend decision, but the platform choice is sticky). Whichever is chosen,
  update this section and the funnel table in `knowledge/marketing/growth-playbook.md` (its
  email-signup row explicitly awaits ESP confirmation).
- **Keyword-DM deliverables are always email-gated AFTER delivery — deliver first, invite
  second.** The DM flow sends the real deliverable link immediately and unconditionally, then
  a one-line invite with the list's concrete promise (e.g. "the full preset pack + one worked
  edit each week — free, on the list"). **Never hold the deliverable hostage behind a signup**
  — a signup-wall converts the funnel's real deliverable into bare bait and breaks THE LINE
  (`knowledge/platform/instagram.md` §2) and the promise-keeping trust rule
  (`knowledge/marketing/community-trust.md`). The email ask rides on delivered value; it never
  gates it.
- **Weekly email-adds KPI.** The analyst pulls the ESP's signup count weekly and reports
  email adds + list size + DM→email conversion % in `/weekly-review` alongside views/followers
  (BET-2's ≥20% DM→email gate lives on this number). These counts live in the ESP dashboard,
  NOT in `ops/calendar/posts.csv` — the CSV's `funnel` column only flags whether the mechanic
  was live on a post. The revenue-lead reads these rows monthly at `/revenue-review`
  (`strategy/REVENUE.md` §5).
