# Web-Series Doctrine — Episode Arcs, Serialization, and the PVC Operational Layer

Craft pack: `longform`. Load-bearing for `/ideate` (episode/season briefs), `/script`, and
G1/G2 lenses 2 and 5 on any series item — and **constitutionally binding for every BET-5 PVC
item**: this file operationalizes `ops/council/consults/2026-08-01-pvc-ethics.md` (the ethics
memo) and BET-5's standing conditions (`strategy/BETS.md`). Where this file and the memo
could ever read differently, the memo's stricter reading wins.

## Episode arc + season arc

- **Every episode is a complete standalone payoff** — the wrapper rule from
  `knowledge/brand/content-architecture.md` format (b) holds at episode scale: a cold viewer
  landing on ep4 gets a whole story (one recipient, one battle, one act of valor; one plate,
  start to finish). The season arc is carried by escalation and variation across episodes,
  never by withholding an episode's own resolution — a cliffhanger that withholds the
  episode's core payoff is the unresolved-loop flop class
  [CORPUS: pattern-library §5.7; `craft/longform/structure-and-retention.md` endings rule].
- **Vary the container or it decays:** the corpus's only quantified season-scale repetition
  data — Curious Refuge reran one packaging/structure formula three times; engagement rate
  fell 2.08% → 1.94% → 0.82% while absolute views held [CORPUS: pattern-library §2.17,
  "quantified format fatigue"]. Season design rule: hold the identity constants (wrapper
  name, numbering, visual identity, disclosure frame) and vary the promise, structure
  emphasis, and packaging per episode.
- Season length: UNKNOWN — research gap: no T1/T2 evidence on optimal episode count or
  cadence for creator web-series; Harper Carroll's "10 Days" framing shows a *stated finite
  plan* lowers commitment cost and converts follows [CORPUS: pattern-library §2.3] — state
  the season's size up front, as policy.

## Serialization retention — what actually makes ep2 get watched

Plan on the corpus's honest read, not the fantasy: **"the series' power is
commitment-signaling, not view-compounding"** [CORPUS: pattern-library §2.3, verbatim —
Harper's per-episode YT views fell 34,541 → under 2,000 by Day 8–9 while the account grew
100x in followers]. Ep2's audience is built from:
1. **The series playlist** — marks episodes as an official set; sibling episodes get
   featured/recommended while one plays [VERIFIED-ONLINE:
   support.google.com/youtube/answer/6084043, accessed 2026-08-02 — T1].
2. **The end-of-episode tease, after the loop closes** — a concrete named promise (the next
   recipient, the next plate), never "more soon"
   (`craft/longform/structure-and-retention.md`).
3. **Shorts/trailer feeders with the related-video link** — the primary in-platform
   Shorts→long-form lever (`platform/youtube.md` §4); BET-5's IG trailers point the same
   direction cross-platform (`strategy/BETS.md` BET-5 gate).
4. **Numbering + wrapper consistency** — follow-conversion via a legible in-progress series
   (`craft/reels/scripting-voice.md` series rules; mere-exposure mechanism
   [RESEARCH-BACKED: research/03 §2.4.2]). Series-effect folklore beyond this ("5–8 episodes
   before compounding," follow-rate multipliers) is [PRACTITIONER LORE / UNVERIFIED STAT:
   research/03 §3.4.2] — never a planning number.

## The PVC operational layer

### Per-episode accuracy workflow — Gazette-first (ethics memo Q1a)

Every episode brief carries a **fact table** built before scripting, three columns: claim →
source → tier. Rules:
- **T1 for what earned the decoration = the Gazette of India citation text itself.** Nothing
  else carries citation-level weight [ethics memo Q1a; Gazette's constitutive role
  VERIFIED-ONLINE via newsonair.gov.in per the memo, accessed 2026-08-01].
- **T2 (reputable published military histories, regimental accounts) fills color only** —
  unit context, personal life — always tagged, never given citation weight.
- **Conflict rule:** the Gazette is authoritative for the documented act; when secondary
  tellings disagree, the episode never resolves toward "whichever version is more dramatic"
  [memo Q1a]. Depict the agreed core, or mark the divergence as dramatization.
- **No source → the claim is cut or the scene is marked dramatization.** Zero-hallucination
  applies doubly here (BET-5 standing conditions; CLAUDE.md non-negotiable 9). SOURCES.md
  still lacks an India-legal/India-press tier — the memo's flagged gap stands; unlisted
  Indian outlets remain directional-only until the quarterly whitelist refresh addresses it.

### Dramatization-marking conventions (memo Q1b)

- Everything beyond the documented record — dialogue, private moments, interior thought — is
  dramatization **by definition** and carries an on-screen marker in-scene (standing card
  text, set once as a distinctive asset: "Dramatized — the documented act is sourced; this
  scene imagines it"), plus a blanket line in the description naming the sourcing basis.
- **Never synthesize the recipient's actual voice — for any line, documented or invented**
  (the Bourdain failure, [VERIFIED-ONLINE: Variety 2021 via memo Q1 — T2]); actor-performed,
  clearly-fictionalized dialogue only. Platform rule stacks on top: cloning someone else's
  voice requires disclosure AND consent [HIGH: `production/genvideo-playbook.md` §7].
- **Never invented present-tense speech or opinion** attributed to the recipient (the
  Karunanidhi failure mode — memo Q1 evidence, UNLISTED/directional). Likeness recreation is
  lower-risk than voice by available precedent but carries the same dramatization marker.

### Disclosure placement for long-form (memo Q1c + platform layer)

- **Description body, visible without expansion:** the `brand/kit.yaml`
  `youtube_description` disclosure line (Claude + critic named), plus the sourcing basis
  ("every citation detail sourced from the Gazette of India; dramatized scenes are marked").
- **On-screen:** the human-gate beat (kit `on_screen` rule) — for PVC, the C8 making-of
  content carries the *proof* of rigor; the tribute episode itself is never interrupted by a
  process flex [memo Q1c].
- **Platform toggle:** every `[GEN]`-tagged upload self-declares via the Altered-content
  toggle — auto-detection makes non-disclosure strictly more expensive
  (`platform/youtube.md` §8 [HIGH]). India's IT Rules synthetic-content labeling (in force
  Nov 2025) is a floor our doctrine already exceeds [T1 via memo Q1: meity.gov.in].

### Family-consultation checkpoint (memo Q2) — in the episode lifecycle

- **When:** at `/ideate`, the moment a specific named recipient is proposed — outreach
  (regimental associations, National War Memorial, Bharat Ke Veer network) becomes a brief
  checklist item; **status must be recorded in the item folder before `/script` runs.** This
  is the single variable separating every positive precedent found (Shershaah —
  family-as-collaborators, UNLISTED/directional) from every negative one [memo Q2].
- **Episode 1 is close to go/no-go on this:** secured engagement converts the lane from
  "no precedent, build defensively" to holding the strongest available precedent [memo Q2].
- **If a family objects post-publish:** stricter-than-standard crisis protocol — self-audit
  first, acknowledge before defending, Sparsh same-day; "technically accurate" is not
  sufficient; amend or pull [memo Q2; `knowledge/marketing/community-trust.md`].
- Direct precedent for AI content about Indian martyrs: **UNKNOWN — research gap** (memo Q2,
  carried forward, not papered over).

### Monetization and CTA boundary (memo Q3, Q4)

- **No keyword-DM funnel mechanic on or attached to a tribute episode — hard
  incompatibility, not case-by-case.** No in-narrative sponsorship, ever. Charity tie-ins
  only with verifiable pass-through. The pipeline/craft story monetizes via C8 making-of
  content, never via the tribute [memo Q3].
- **Date pegs pass the random-Tuesday test:** the episode must hold up independent of the
  date; no urgency/scarcity language tied to a national day; if a date is a production
  constraint rather than a choice, say so in `publish.md` [memo Q4].
- Audience note for briefs: this lane's target is BET-5's India-first audience — **not** the
  four existing personas; never write defensive "AI can honor heroes too" content at
  persona (d) [memo Q5; `knowledge/audience/personas.md` reading rule].

## Tribute-integrity checklist — the critic's G2 instrument (binary, per episode)

| # | Check | Source |
|---|---|---|
| 1 | Fact table complete; every biographical claim Gazette/T2-sourced or cut | memo Q1a |
| 2 | No dramatized scene presented with citation-level certainty; markers on-screen | memo Q1a/b |
| 3 | No synthesized recipient voice; no invented present-tense speech/opinion | memo Q1b |
| 4 | Disclosure: description line + sourcing basis + Altered-content toggle queued | memo Q1c; yt §8 |
| 5 | Family/regimental consultation status recorded in item folder (not asserted) | memo Q2 |
| 6 | No funnel/sponsor/merch mechanic in or attached to the episode | memo Q3 |
| 7 | Date peg (if any) passes the random-Tuesday test | memo Q4 |
| 8 | Tone: reverent/documentary register; no patriotism-signaling disconnected from the documented story | memo Q4 |

Any FAIL blocks SHIP at G2 exactly like a lens-8 hygiene fail — these are integrity checks,
not taste notes. Row 5's *outcome* can be "declined/no response, proceeding with defensive
posture logged" — but never blank.

## G1/G2 lens adaptations (longform, series items)

- **Lens 1 — HOOK (×2):** the episode's packaging+first-30s pair
  (`craft/longform/packaging.md`) must work for a cold viewer with zero series context —
  serialization never subsidizes a weak standalone promise.
- **Lens 2 — STRUCTURE & RETENTION:** episode closes its own master loop; season arc
  advanced by variation, not withholding; ep-tease present and concrete; series playlist +
  related-video wiring named in `publish.md`'s checklist.
- **Lens 5 — CRAFT & AESTHETICS:** for PVC items the tribute-integrity checklist above is
  part of the craft bar — a technically beautiful episode that blurs the
  documented/dramatized line fails craft, because the sourcing rigor IS the craft claim
  (machine craft, human taste, and the memo's "show the labor" doctrine). Continuity bar
  (chained-clip drift) applies per `craft/longform/structure-and-retention.md`.
