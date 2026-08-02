# Content Architecture — Tiers, Selector, Format Portfolio

Load-bearing for `/ideate` (concept scoring) and `/plan` (pillar tagging in `item.yaml`).
Restates `STRATEGY.md` §4 operationally, with a worksheet an agent can actually run.

## HERO / WORKHORSE / FILLER tiers

| Tier | Definition | Selection criteria | Price of entry |
|---|---|---|---|
| **HERO** | Engineered for reach — the awe demos, the flagship "Claude edits" spectacle. | Passes all 5 selector points at a HIGH bar; target emotion is awe; concrete, dramatic, on-screen payoff. | Expensive, rationed — never rushed, never more than 2/week even in launch surge (`STRATEGY.md` §7). |
| **WORKHORSE** | Identity and cadence — series episodes, workflow-shares with gated deliverables. Sustains the median. | Passes the selector; fits an owned, repeatable format skeleton. | The bulk of weekly output; must be plannable, which is why format ownership matters (below). |
| **FILLER** | News-response within 0–4 days of an Adobe/Anthropic/AI-imaging event, demonstrated on our own raws — never a talking-head recap. | Timeliness is the primary criterion; still passes the never-list. | Cadence insurance only — "filler exists to protect hero quality, never to replace it; volume raises the floor, not the ceiling" (SYSTEM_DESIGN §10, `virality/laws.md` Law 11). |

Consistent three-tier discipline is what separates mega-creators from wannabes in the corpus —
winners know which tier a post belongs to before they make it; wannabes can't tell
[CORPUS: synthesis/02 §5].

## The 5-point concept selector — scoring worksheet

A concept must pass **all five** or it dies at `/ideate` — this is a gate, not a rubric to
average [STRATEGY §4].

1. **Universal premise?** Y/N — a universally relatable premise, or a universal frame wrapped
   around the niche topic (Skill Leap's device/context-hybrid framing, `craft/hooks.md`).
2. **Concrete, verifiable payoff shown (not claimed)?** Y/N — must be visible on screen, not
   asserted in narration.
3. **High-arousal target emotion named in the brief?** Y/N — awe is the default; name it
   explicitly, don't leave it implicit.
4. **Fits an owned format, or is a deliberate, single-slot audition?** Y/N — see
   format-ownership doctrine below.
5. **Provable live — our raws, our pipeline, visible process?** Y/N — the "prove, don't assert"
   test.

**Worksheet rule:** any single N kills the concept at ideation, before it costs production
effort — record the killing criterion in the brief's kill log even for rejected concepts, so
`/weekly-review` can spot patterns in what keeps failing.

**Worked example.** Concept: "Claude re-grades a wedding photo shot in flat midday light to
gallery-grade evening warmth." (1) Universal premise — Y: everyone recognizes "bad light,
saved." (2) Concrete payoff shown — Y: before/after frame, not claimed. (3) High-arousal
emotion — Y: awe, named in brief. (4) Fits owned format — Y: format (a), demo-in-motion reel.
(5) Provable live — Y: Sparsh's own raw, our pipeline, critic visible on-screen. All five Y →
proceeds to `/script`. Contrast a killed concept: "Claude explains what a RAW file is" — fails
(2) (no on-screen payoff, just narration) and (3) (informational, not high-arousal) — killed at
ideation, logged with both failing criteria named.

## Format-ownership doctrine

Converge on **≤3 owned formats** — the median is only plannable when formats repeat
[CORPUS: pattern-library §2.7 tiffintech, §2.1 elevenpercentprod]. **Audition rules:** at most
**1** unproven format in flight at any time, run against the same selector worksheet as
everything else. **Kill/keep decisions on an owned or auditioning format happen ONLY at the
weekly review** (`/weekly-review`) — never mid-week on a single post's performance; a single
flop or hit is not a format verdict, per Law 11 (median over spikes).

## Starting format portfolio

**(a) The "Claude edits" demo-in-motion reel.** Template skeleton: already-running Lightroom
session → granular visible state-changes every 5–15s → one honest error/adjustment-reconsidered
beat → finished-plate reveal as the closing payoff (`craft/structure-and-retention.md`). Bet
dependency: **BET-3** — demo-in-motion transferring from tool-demos to art is explicitly
untested in the corpus; validation gate is HERO median ≥ WORKHORSE median across ≥8 posts
(`strategy/BETS.md` BET-3).

**(b) The numbered cold-start series wrapper.** Template skeleton: consistent numbering
on-screen and in caption, one unifying frame (e.g., "Edit Log"), each episode a complete
standalone payoff. Honest mechanics: front-load + follow-conversion, NOT view compounding —
Harper Carroll's "10 Days" series drove 2K→200K followers in 3 weeks, but per-episode YouTube
views declined from 34,541 (Day 1) to under 2,000 by Day 8–9; "the series' power is
commitment-signaling, not view-compounding" [CORPUS: pattern-library §2.3, verbatim]. Bet
dependency: **BET-2** (Claude for creatives) when the wrapper carries keyword-funnel episodes.

**(c) The workflow-share + keyword deliverable.** Template skeleton: problem/context beat →
mechanism shown → comment-keyword CTA gating a REAL deliverable (prompt, preset, process PDF).
Bet dependency: **BET-1** (the editing lane) and **BET-2** (Claude for creatives) both validate
through this format's funnel data (`tools/metrics.py funnel`, bar comment:like ≥ 0.5).

## Format portfolio → tier mapping

| Format | Typical tier | Notes |
|---|---|---|
| (a) Claude edits demo reel | HERO (flagship instances), WORKHORSE (routine instances) | reach-engineered when the transformation is dramatic; routine otherwise |
| (b) Numbered series wrapper | WORKHORSE | identity/cadence engine, not a reach play — see honest read below |
| (c) Workflow-share + keyword deliverable | WORKHORSE | funnel/capture engine; occasionally HERO if the deliverable itself is the news hook |

A format is not locked to one tier — the same skeleton can carry a HERO or WORKHORSE instance
depending on how dramatic the specific payoff is. What must stay fixed is the *skeleton itself*
(beat order, disclosure moment, on-screen grammar) — tier changes budget and rationing, not
structure.

## Series mechanics — the honest read

Do not plan a series budget on "each episode goes more viral than the last" — the corpus
falsifies this directly on the only platform with per-episode data (YouTube): Harper's series
declined episode-over-episode in views while still growing the account 100x in followers over
the same window [CORPUS: pattern-library §2.3]. Budget series for (1) a strong Day-1 breakout
via a real hook + underserved topic + timing, (2) the numbered-series framing converting
viewers to followers, (3) sustained elevated distribution for follow-ups via the *existence* of
a recognizable in-progress series — not via any individual episode re-achieving Day 1's peak.
