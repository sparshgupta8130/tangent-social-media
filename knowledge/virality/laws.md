# Virality Laws — The Measurement Layer + 11 Mechanics Laws

Load-bearing for G1/G2 (laws are cited as evidence for deductions across all numeric lenses)
and for `/postmortem`'s views×LR decomposition. Source: `synthesis/01_VIRAL_MECHANICS.md`,
cross-cited to `pattern-library.md` and `research/03`. Confidence tags are preserved from the
source documents — treat anything not tagged [RESEARCH-BACKED] as a corpus pattern or a bet,
not a proven mechanism.

## Part 0 — The measurement layer (read this before believing any "viral" number)

### Law 0.1 — Leaderboards lie three ways
**LAW:** A raw view/like count is not evidence of organic reach until three failure modes are
ruled out. **EVIDENCE:** (a) paid boosts — sponsor-funded (Wes Roth's HeyGen short, 0.06% LR),
self-funded undisclosed (kallaway's 74.2M/39.5M/35.8M spikes at 0.0107–0.088% corrected LR,
~15–400x below his own organic baseline), or paid reach-amplification with normal engagement
(tiffintech's Lenovo/FIFA post, 73.7M views at a healthy 1.55% LR — real engagement, bought
distribution); (b) pins — date-verified legacy hits pinned above current content (confirmed at
nateherkai, thevarunmayya, handlytech, kallaway); (c) instrument error — our own browser-harvest
like counts were wrong on 15.5% of 110 re-pulled reels, severely (>2x) on 9.1%
[CORPUS: synthesis/01 Part 0; pattern-library §7.1]. **OPERATIONAL TEST:** no exemplar — ours or
a competitor's — is "organic viral" until it clears a like-rate sanity band (~1–10%) via a
second independent tool (`tools/verify_stats.py`) AND a pin/date check.

### Law 0.2 — Views × like-rate decomposition diagnoses WHY, not just whether
**LAW:** High LR + low views = hook/discovery failure. Low LR + low views = craft failure. These
require different fixes. **EVIDENCE:** Berman's OpenClaw flop scored a *higher* LR than his hit
(4.56% vs 2.50%) at 85x fewer views — a pure discovery failure, not a quality one; Berman's
"ways to use ai" flop had a dead 14s preamble and a low LR — a craft failure
[CORPUS: synthesis/01 Part 0]. **OPERATIONAL TEST:** run `tools/metrics.py decompose` on every
postmortem; a hook/discovery-quadrant flop gets a hook/packaging fix, a craft-quadrant flop gets
a structure/production fix — never the same prescription for both.

## Part 1 — The 11 mechanics laws

**1. The one-second, result-first hook.** Zero preamble, payoff named/shown in second 0–1
across every top performer in all 8 YT dossiers. [RESEARCH-BACKED mechanism + CORPUS confirm:
synthesis/01 §1] → Test: does frame 0 pass `craft/hooks.md`'s first-frame test unaided?

**2. Topic selection dominates format execution.** Same template, 180x gap: Nate Herk's #161
flop ("B2B sales-email approval") vs. his #1 hit ("autonomous AI team"), posted 3 days apart.
[CORPUS: synthesis/01 §2, pattern-library §2.5] → Test: does the concept pass selector-formula
criterion 1 — universally relatable premise, or a universal frame around a niche topic — before
any script is written (`knowledge/brand/content-architecture.md`)?

**3. Payoff intensity, not checklist presence.** STEPPS pillars "present" predicts nothing;
their intensity does — AI-capability awe is the highest organic ceiling observed, above
tutorials on tutorial channels. [RESEARCH-BACKED: Berger & Milkman 2012, via research/03 §2.3;
CORPUS confirm synthesis/01 §3] → Test: is the target emotion named in the brief, and is it
high-arousal (awe is our default), not merely "present"?

**4. Close every loop; escalate multi-payoffs.** Winners visibly resolve every promise the hook
makes; escalating listicles (most impressive last) beat equal-weight lists.
[CORPUS: synthesis/01 §4] → Test: is the loop map complete
(`craft/structure-and-retention.md`), and for multi-item pieces, is the order escalating?

**5. Demo-in-motion grammar for "watch AI work" content.** Already-running system, granular
state-changes every 5–15s, an honest error/wait beat, fixed-length template discipline.
[CORPUS: synthesis/01 §5, pattern-library §2.1, §2.6] → Test: does the script open on a live
system (not a build-log), and does it match our owned format's fixed skeleton
(`knowledge/brand/content-architecture.md`)?

**6. The comment-keyword DM funnel is the strongest distribution+capture mechanic in the
corpus.** Devin Huynh: comments exceed likes on 3 of top 5. Nate Herk IG: comment:like
0.95–3.86:1 with the mechanic vs. 0.09–0.28:1 without, same account. [RESEARCH-BACKED mechanism
(sends > likes for cold reach, per Mosseri) + CORPUS: synthesis/01 §6, research/03 §1.1.2] →
Test: does every funnel post gate a REAL, standalone-valuable deliverable, never bare "comment
YES"? `tools/metrics.py funnel` bar: comment:like ≥ 0.5 = mechanic working.

**7. Series packaging is a cold-start weapon, not a compounding engine.** Harper Carroll's "10
Days of AI Basics" powered 2K→200K followers in 3 weeks, but per-episode YT views FRONT-LOAD and
decline (34,541 → 944 by day 8) — power is commitment-signaling and follow-conversion, not view
compounding. [CORPUS: synthesis/01 §7, pattern-library §2.3] → Test: is a series scripted to
convert Day-1 viewers into followers ("N episodes, here's the plan" framing), not budgeted on
the assumption Episode 5 out-views Episode 1?

**8. News velocity is a reliable, engineerable lever.** Wes Roth: 3 of his top-8 shorts hard-
timed 0–4 days to named events. Sisinty's entire top-5 = news hooks. [CORPUS: synthesis/01 §8] →
Test: is there a 0–4-day news window available (`ops/calendar/trends-log.md`), and does the
script hit it inside that window?

**9. Sponsored content survives ONLY inside the creator's own playbook.** Harper's on-brand
#ClaudePartner posts sit in her top 5; her off-format #ServiceNowPartner post flopped.
Mechanism is sends-collapse (people don't forward ads) plus visible trust-friction, NOT
algorithmic tag-demotion (Mosseri denies this on record). [RESEARCH-BACKED mechanism partial,
CORPUS confirm: synthesis/01 §9] → Test: does a sponsored brief still execute inside our owned
format skeleton, unmodified?

**10. Platform-native beats cross-posting; the lane must fit the genre.** Sebastien's IG beat
his 558K-follower TikTok twin by a 182x view gap on the one matched pair. Tool-demo content wins
Shorts/Reels; art-spectacle wins long-form (Curious Refuge: top long-form 228x their top Short).
[CORPUS: synthesis/01 §10] → Test: does this concept's genre match its assigned lane —
process-demo → Reels/Shorts, finished-art spectacle → YT long-form (`STRATEGY.md` §5)?

**11. Volume raises the floor, not the ceiling.** Berman's 200-Short sweep: bottom 75% live in a
tight 3.6–12K band; top 5% capture 52% of all views; outliers are a lottery, not a formula.
[CORPUS: synthesis/01 §11] → Test: is cadence planning done against the MEDIAN
(`tools/metrics.py report`), with any spike logged as a windfall, never as the new baseline?

## Confidence ledger

RESEARCH-BACKED laws (peer-reviewed/platform-official mechanism): 1 (hook gate), 3 (arousal),
6 (sends>likes direction), 9 (no algorithmic tag-demotion). CORPUS-pattern laws (strong,
repeated, not independently peer-reviewed): 2, 4, 5, 7, 8, 10, 11. Nothing in this file is a
bet — bets (BET-1–4, LENS-1) live in `strategy/BETS.md` and get cited separately whenever a law
is being extended into genuinely untested territory for us (e.g., Law 5 applied to fine-art
editing rather than tool-demos is BET-3, not an established law for our genre).
