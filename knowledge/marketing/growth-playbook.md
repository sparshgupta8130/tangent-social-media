# Growth Playbook — Creator-Brand Growth Economics

**Owner:** growth-lead.
**Load context:** read before any BTS-triggered `/consult` on funnel/monetization
mechanics or platform-portfolio questions; before the growth-lead's G3 Growth
Contribution scoring; before any monetization-readiness discussion (`strategy/BETS.md`
Deferred section).

## Owned-audience value — the platform-risk doctrine

**Claim:** an email/community list the creator directly controls is worth structurally more
than the same-size audience rented from a platform, because platform reach is revocable —
algorithm changes, account actions, or policy shifts can zero out distribution overnight
with no recourse, while an owned list is contactable regardless of any platform's decisions.
This is standard creator-economy risk doctrine, not a single peer-reviewed study — treat the
*direction* (owned > rented, holding audience size constant) as well-established practice
wisdom, and any specific "email subscriber is worth $X of IG follower" multiplier claim as
**[UNVERIFIED STAT]**, per the corpus's own ban-list precedent (`knowledge/INDEX.md`
provenance legend).

**What it means for Tangent:** the four-surface architecture (`positioning-doctrine.md`)
already encodes this — IG reaches, but email owns [REPO: STRATEGY.md §1]. The DM-funnel
mechanic exists specifically to convert rented reach into an owned contact before any
platform-risk event can erase the relationship. Growth accounting should track the funnel
conversion into email as a first-class outcome, not a footnote to follower count — a
week with flat follower growth but rising email signups is a good week by this doctrine, not
a mediocre one.

## Follower-quality-over-count doctrine

**Claim:** raw follower count is a vanity number; a smaller, more responsive audience
outperforms a larger, mismatched one on every metric that actually matters (efficiency,
funnel conversion, sentiment). **Our own corpus's evidence:** handlytech — 989K followers,
1.0% median-views/follower ratio, the worst of 22 ranked accounts in the corpus, because 3
pinned 2023–2025 off-topic phone-security hits kept re-priming visitor expectations against
the account's real 2026 content [REPO: `knowledge/virality/failure-modes.md` §3 —
"Audience-mismatch death"]. This is our own corpus's textbook case for why count without
quality is a liability, not an asset: the audience handlytech "grew" wasn't the audience its
current content needed.

**What it means for Tangent:** never plan or celebrate against follower count alone.
Efficiency (median views ÷ followers, `benchmarks.md` §1) is the account-health metric that
actually says whether the audience is watching; the early-warning triad
(`benchmarks.md` §4) exists precisely to catch a handlytech-style mismatch before it
calcifies. At G3 and weekly review, the growth-lead treats a follower-count milestone
with zero commentary on efficiency as an incomplete report, not a win to log.

## Funnel math — worked example

The full mechanic: views → profile visits → follows → DM keyword request → email signup.
**This is an illustrative arithmetic walkthrough, not a claimed real number** — Tangent has
no published posts yet (all bets UNTESTED, `strategy/BETS.md`), so every figure below is a
hypothetical used to show how the conversions compose, not `[OWN-DATA]`.

| Stage | Definition | What moves it | Measurable per `publishing-ops.md`? |
|---|---|---|---|
| Views | the unified "Views" metric (2026 IG consolidation of impressions/plays/replays) | hook strength, distribution wave (`platform/instagram.md` §1) | Yes — API-confirmed [HIGH, `publishing-ops.md` §3] |
| Profile visits | viewer taps through to the account profile | curiosity the content leaves unresolved, bio-line clarity | **Uncertain.** Historically an in-app Professional Dashboard metric; the discrete `profile_views` Graph API field was deprecated in API v22 in favor of broader `views`/`reach`/`follower_count`/`reposts` fields [VERIFIED-ONLINE: developers.facebook.com/docs/instagram-platform/insights/, 2026-07-31, confirms the v22 deprecation]. Treat account-level profile-visit counts as pullable manually from the in-app dashboard, **not** confirmed as an automatable API field — log as a research gap if the analyst needs it scripted, don't assume the API path exists |
| Follows | profile visit converts to a follow | bio-line + grid first impression (`tangent-voice.md`) | Partially — `follower_count` is a confirmed metric; visit→follow *rate* requires the profile-visits figure above, so inherits its same uncertainty |
| DM keyword request | viewer comments the keyword, opts into the automation | the deliverable's specificity and earned-ness (THE LINE, `platform/instagram.md` §2) | Yes — ManyChat's own dashboard logs trigger events [HIGH, `publishing-ops.md` §4] |
| Email signup | DM deliverable includes a path to the list, viewer opts in | deliverable quality, trust in "will I actually get something real" | Yes, via the email platform's own signup count — not an IG metric, so it lives outside `publishing-ops.md`'s IG/YT scope; whichever ESP is chosen must be confirmed in a future ops-brief update |

**Illustrative composition** (hypothetical inputs, not measured): if a WORKHORSE post
reaches 10,000 views and converts at a hypothetical 5% to profile visits (500), a
hypothetical 15% of visits to follows (75), and the same post's DM funnel draws 50 keyword
comments (a comment:like ratio the analyst would separately check against the ≥0.5
`WORKING` bar, `benchmarks.md`), with 20% of those converting to email per BET-2's own
validation gate [REPO: BETS.md BET-2] — that's 10 new email addresses from one post. The
arithmetic composes multiplicatively (views × visit-rate × follow-rate, independently DM
requests × email-conversion-rate) — each stage's rate is what the growth-lead should
track and try to move, not the raw counts, because rates transfer across posts of different
sizes and raw counts don't.

**What moves each conversion, in priority order:** hook quality moves views (craft/critic
domain, not this file's); bio-line clarity and grid first-impression move profile-visit→
follow; deliverable specificity and THE LINE compliance move DM requests
(`platform/instagram.md` §2); deliverable *actually arriving instantly and being real* moves
DM→email (the trust-ledger promise-keeping rule, `community-trust.md`).

## Monetization-readiness criteria

**Sequencing logic: trust before transaction.** [REPO: strategy/BETS.md Deferred —
"Monetization mechanics (presets, course, prints, SaaS): revisit at 10K followers or first
inbound sponsor interest — the funnel builds the asset meanwhile."] The Brand Office's role is
to check *brand conditions*, not just the follower-count trigger, before endorsing a
monetization mechanic at BTS/G3:

1. **Disclosure consistency has a track record** — not a single well-disclosed post, but a
   pattern across enough posts that a viewer checking the account's history sees consistency
   (`community-trust.md` trust-ledger concept).
2. **The funnel mechanic itself is validated**, not just live — BET-2's own gate (funnel
   posts reach comment:like ≥0.5 median across first 5; DM→email conversion ≥20%) should be
   VALIDATED, not UNTESTED, before adding a paid layer on top of the same mechanic
   [REPO: BETS.md BET-2].
3. **No open trust-ledger debt** — no unresolved public dispute, uncorrected error, or
   backlash-flashpoint adjacency sitting unaddressed (`community-trust.md` crisis protocol)
   at the time a monetization mechanic is proposed; introducing a transaction while trust is
   in question compounds the risk.
4. **The distinctive-asset register has at least reached EMERGING status** on the
   highest-leverage assets (critic-as-character, the sliders visual —
   `distinctive-assets.md`) — monetizing before the brand has a recognizable identity risks
   the transaction becoming the account's most memorable feature instead of the craft.

None of these four is itself a number to hit — they are qualitative gates the Brand Office
checks alongside the quantitative follower/sponsor-interest trigger already in BETS.md; a
BTS≥3 "sponsorship / commercial element" flag routes to `/consult` specifically so this
checklist gets run before a brief is scripted, not after.

## Sponsorship economics for small creators

**Corpus evidence — the sponsor penalty is real and severe:** Varun Mayya's two #ad posts
took a 10–15x organic-engagement penalty on the same account as his organic content; Riley
Brown's CodeRabbit sponsor read abandoned his channel's own demo-in-motion mechanic
entirely, producing the lowest comment rate of his whole sample [REPO:
`knowledge/virality/laws.md` Law 9; `knowledge/virality/failure-modes.md` mode 5]. The
mechanism, per the corpus, is **not** algorithmic tag-demotion (Mosseri denies this on the
record) — it's sends-collapse (people don't forward ads to friends) plus visible
trust-friction in comments when a sponsor brief overrides the creator's own format
[REPO: `virality/laws.md` Law 9 confidence ledger — mechanism partial RESEARCH-BACKED,
corpus-confirmed].

**Fit criteria, derived from the counter-example:** Harper Carroll's on-brand
#ClaudePartner posts sat in her *top 5* — the difference from her ServiceNow flop was that
the sponsored content executed entirely inside her own existing format, not the sponsor's
deck [REPO: `virality/laws.md` Law 9]. Applied to Tangent: (1) a sponsor brief must execute
inside one of our ≤3 owned format skeletons unmodified (`content-architecture.md`), never
restructure beat order to the sponsor's template (`failure-modes.md` mode 2); (2) the
natural-fit category is tools we'd plausibly use anyway and can demonstrate honestly inside
the pipeline (Anthropic/Adobe creator programs are the structurally obvious fits, per
Harper's #ClaudePartner precedent — [REPO: STRATEGY.md §5]); (3) any sponsor brief is a BTS
"sponsorship / collab" flag (+3), mandatory `/consult` before scripting, no exceptions
regardless of follower count.

## Platform-portfolio risk

**IG algorithm dependence:** tangentideas.ai's reach is entirely governed by Instagram's
ranking signals (`platform/instagram.md` §1) — a single-platform account has zero recourse
if Instagram's algorithm, policy, or product direction shifts against the account's format
or niche. This is the general platform-risk doctrine above, applied specifically to the
primary reach surface.

**Diversification sequencing already decided in STRATEGY:** YouTube is the deliberate hedge
— both a demographic hedge (35+ = 51.9% of YT's ad-reachable audience vs. IG's youth
concentration, [REPO: `audience/personas.md` persona (a)]) and a platform hedge (a second
distribution channel with independent ranking mechanics). The gallery (tangent.gallery) is
platform-independent by construction — it's owned infrastructure, not rented reach, and
functions as the brand's standing proof regardless of what any social platform does. Email
is the ultimate hedge, per the owned-audience doctrine above. **TikTok is explicitly
deferred** [REPO: STRATEGY.md §5 ghost-twin warning; BETS.md Deferred — "revisit when IG
efficiency is VALIDATED and cadence has ≥2 spare slots/week"] — the growth-lead's role
at `/consult` is to resist adding a third reach platform before the second (YT) is
functioning, since platform-portfolio risk is reduced by depth on fewer, well-run surfaces
more than by breadth across many thin ones.
