# Failure Modes — The 7-Mode Catalog

Load-bearing for G1/G2 review and `/weekly-review`'s pivot-on-signal checks. Each mode:
definition, named corpus cases, early-warning signs for OUR posts, prescribed response. Source:
`pattern-library.md` §5 (Failure Catalog) and `synthesis/01` Part 2.

## 1. Hook-coherence break
**Definition:** the hook promises a different video than the one delivered, or the hook itself
confuses rather than intrigues. **Cases:** Nate Herk (YT), "Fake it till you make it" into
fragmented chatter with no context — 4,881 views, dead last of 164. Riley Brown's Taylor-Swift-
hook video delayed its own tool demo 20+ seconds — 3,950 views, 0.348x median (comment rate beat
6 of his 8 tops — a reach failure, not a reception failure). Skill Leap's "Are you using AI
agents yet?" — title/hook mismatch, 1,949 views, #29/30 [CORPUS: pattern-library §5.1].
**Early-warning signs:** the critic's G1 note flags "the hook sets up X but the beat sheet pays
off Y"; a script variant needs the caption to explain what the first frame means. **Prescribed
response:** rewrite the hook to match the actual payoff, or restructure the payoff to match the
promised hook — never ship the mismatch; max 2 fix rounds (SYSTEM_DESIGN §8), then KILL.

## 2. Format abandonment
**Definition:** dropping the account's own proven structural discipline — usually for a sponsor
read or an off-brand slideshow. **Cases:** Devin Huynh's Video 7 (infomercial structure,
credential→pricing→CTA after 50s+, 3,285 views) and Video 6 (third-party repost, no Devin on
camera, 2,528 views — "no parasocial continuity"). Ayham Joukhadar's Pippit #ad replaced his
entire screen-record persona with a stock-photo slideshow — the most extreme persona break in
the corpus [CORPUS: pattern-library §5.2]. **Early-warning signs:** a brief that reads like a
sponsor's own deck rather than our format skeleton; `assets.md` shows no `[AGENT]`-captured UI.
**Prescribed response:** any sponsored or guest-brief concept must still execute inside one of
our ≤3 owned format skeletons (`knowledge/brand/content-architecture.md`) — kill briefs that can't.

## 3. Audience-mismatch death
**Definition:** a well-executed video (or account-level pattern) reaching the wrong or too-
narrow slice of the audience; distribution collapses while per-viewer engagement stays healthy.
**Case (the textbook account-level autopsy):** handlytech — 989K followers, 1.0% median/
follower ratio (worst of 22 ranked accounts), driven by 3 pinned 2023–2025 off-topic
phone-security hits still re-priming visitor expectations against the account's real 2026
"AI in 30 seconds" content [CORPUS: pattern-library §5.3, §3.2]. **The handlytech early-warning
triad — check monthly, account level** (`strategy/STRATEGY.md` §6): (a) efficiency (median
views ÷ followers) sliding under ~5%; (b) hits coming only from off-pillar content; (c) flat
non-pinned spread. **Two of three trips a mandatory strategy review** (planner-triggered).
**Prescribed response at video level:** never leave an off-niche hit pinned once the real niche
is committed to; at account level, let off-pillar windfalls pass without rebuilding the channel
around them (Skill Leap explicitly did NOT pivot to iPhone content — `synthesis/02` §8).

## 4. Spike-decay without wrapper
**Definition:** a genuine organic spike, riding a news cycle, that evaporates because no
repeatable format caught the new attention. **Case:** Ankit Arora — 3 of his top-4 hits landed
within a 10-day Claude/Anthropic news window with no numbered/branded series wrapper; two
months later, engagement had decayed into sub-2%-LR flops [CORPUS: pattern-library §5.4].
**Counter-case:** Harper Carroll's numbered "10 Days" series caught a comparable cold-start
spike and converted it into durable followers [CORPUS: synthesis/01 §7]. **Early-warning
signs:** a HERO or FILLER spike posts with no series/wrapper assigned in its brief. **Prescribed
response:** fold any lucky news-cycle win into a named, numbered wrapper within days, not weeks
— Law 7, `virality/laws.md`.

## 5. Sponsor-brief capture
**Definition:** content structurally captured by a paid partner's brief in a way that
suppresses reach, engagement, or format integrity, independent of hook quality. **Cases:**
Varun Mayya's two #ad flops (10–15x organic penalty, same account); Riley Brown's CodeRabbit
sponsor read abandoned his channel's demo-in-motion mechanic entirely — lowest comment rate of
his whole sample, "the cleanest sponsor-brief-capture case in either YouTube dossier"
[CORPUS: pattern-library §5.5]. Mechanism confirmed: NOT algorithmic tag-demotion (Mosseri
denies this on record) but sends-collapse (people don't forward ads) plus visible trust-friction
in comments [CORPUS: synthesis/01 §9]. **Early-warning signs:** a sponsor brief dictating beat
order rather than our own template. **Prescribed response:** Law 9 — sponsors execute inside our
format, never the reverse; kill or renegotiate any brief that can't fit.

## 6. Preamble cold-open
**Definition:** a strong hook immediately undercut by non-payoff material — self-introduction,
credentialing, "hello and welcome." **Cases:** Harper Carroll's worst post omits her usual
credential signature and opens on vague personal narrative (36.2K views, dead last). Curious
Refuge's two podcast flops both follow a genuinely strong cold open with a full, unhurried
guest self-introduction — a "textbook silent retention killer," reproduced identically 8 months
apart [CORPUS: pattern-library §5.6]. **Early-warning signs:** any script beat before the hook
resolves that isn't a visible payoff step. **Prescribed response:** cut everything before the
hook resolves; if credentialing is genuinely needed, fold it into an ongoing on-screen signature
(consistent named characters, `knowledge/brand/tangent-voice.md`), never a spoken intro.

## 7. Unresolved loop
**Definition:** the video opens a curiosity gap or a question and never closes it. **Cases:**
Wes Roth's "can AI sway public opinion?" — abstract, unfalsifiable, ends mid-thought, 3,190
views, dead last of 44 (engagement among the few who saw it was normal — a distribution failure
downstream of the unresolved hook). Skill Leap's "ChatGPT competitor from Google" trails off
mid-thought, #30/30 [CORPUS: pattern-library §5.7]. **Early-warning signs:** the loop map in
`script.md` shows an opened item with no closing beat. **Prescribed response:** G1 hard-fails
any script with an incomplete loop map — this is a lens-2 gate item, not a suggestion
(`templates/critique-scorecard.md`).

## Quick-reference: mode → primary lens affected

| Mode | Primary critique lens hit | Fastest tell |
|---|---|---|
| 1. Hook-coherence break | Lens 1 (HOOK) | caption has to explain the first frame |
| 2. Format abandonment | Lens 7 (DIFFERENTIATION) | brief reads like the sponsor's own deck |
| 3. Audience-mismatch death | Lens 6 (AUDIENCE FIT) | pinned hit off-topic vs. current pillar |
| 4. Spike-decay without wrapper | Lens 2 (STRUCTURE) | news-driven brief has no series field filled in |
| 5. Sponsor-brief capture | Lens 7 (DIFFERENTIATION) | beat order dictated by the brief, not our template |
| 6. Preamble cold-open | Lens 1 (HOOK) | any beat before the hook resolves that isn't payoff |
| 7. Unresolved loop | Lens 2 (STRUCTURE) | loop map has an opened row with an empty close column |

## Account-level alarm vs. video-level failure

Modes 1, 2, 6, and 7 are diagnosed per video, at G1/G2. Mode 3's handlytech triad and mode 4's
wrapper check are diagnosed at the **account level**, monthly, by the planner
(`ops/calendar/ROADMAP.md` cadence review) — a single post tripping one of these is a data
point, not yet a failure; two of the triad's three conditions trip a mandatory strategy review,
per `strategy/STRATEGY.md` §6.
