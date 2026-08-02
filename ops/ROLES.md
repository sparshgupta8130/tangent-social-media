Tangent Social — Responsibility Matrix (RACI)

R = Responsible (does the work) · A = Accountable (owns the outcome/decision; exactly one per
row unless marked joint) · C = Consulted (input sought before/during) · I = Informed (told
after, no input required).

Columns — the Studio: **SP** Sparsh · **SR** Showrunner · **CD** creative-director ·
**TS** trend-scout · **SL** story-lead · **PR** producer · **CR** critic · **AN** analyst ·
**PL** planner. The Brand Office (SYSTEM_DESIGN §12): **BC** = the Brand Office collectively
(brand-director chairs; growth-lead, audience-advocate as lenses).

Full agent contracts live in `.claude/agents/`; this table is the cross-agent responsibility
map, not a restatement of any one agent's job description.

**Reading the A column:** Showrunner carries Accountable on most rows because it is the final
internal quality gate (SYSTEM_DESIGN §1) — it doesn't do the work, but a bad ideation, a
missed hygiene fail, or a stalled roadmap is still on it. Two rows break that pattern on
purpose: G1/G2 (critic holds `R,A` together, because SYSTEM_DESIGN §8 makes critic verdicts
binding — nobody, including the Showrunner, overrides a SHIP/FIX/KILL call) and ship approval
(Sparsh holds `R,A` together, because that decision is constitutionally his and only his).

| Activity | SP | SR | CD | TS | SL | PR | CR | AN | PL | BC |
|---|---|---|---|---|---|---|---|---|---|---|
| Ideation (note/trend → scored concepts) | C | A | R | R | I | I | I | C | I | I |
| Briefing (brief.md + selector scorecard) | I | A | R | C | I | I | I | I | I | C¶ |
| Scripting (script.md + assets.md) | I† | A | C | I | R | C | I | I | I | I |
| G1 — script gate | I | C | I | I | R (fixes) | I | R,A | I | I | I |
| Production (capture/gen/assembly) | R† | A | I | I | C | R | I | I | C | I |
| G2 — cut gate | I | C | I | I | I | R (fixes) | R,A | I | I | I |
| Brand consults (`/consult`, BTS-triggered or on demand) | C | A | C | I | I | I | I | I | I | R |
| G3 — brand gate (`/brand-review`) | I (C on HOLD) | C | I | I | I | I | I | I | I | R,A |
| Ship approval | R,A | C | I | I | I | I | I | I | R‡ | C |
| Publishing | I | A | I | I | I | R | I | I | R | I |
| DM-funnel fulfillment setup | I† | A | C | I | R | R | C | I | I | C |
| Postmortem | I | A | I | I | I | I | C | R | I | I |
| Benchmarks (`knowledge/benchmarks.md`) | I | I | I | I | I | I | I | R,A | I | I |
| Roadmap (`ops/calendar/ROADMAP.md`) | C | A | C | C | I | I | I | C | R | C |
| Plane sync | I | I | I | I | I | I | I | I | R,A | I |
| Trend surveillance | I | I | C | R,A | I | I | I | I | C | I |
| Knowledge-bank writes | I | A | C | I | C | C | C | R | I | R‖ |
| Strategy/bet changes (BETS.md, STRATEGY.md) | R,A§ | R,A§ | C | I | I | I | I | R | C | C |
| Revenue strategy (`strategy/REVENUE.md`, `/revenue-review`) | R,A§ | R,A§ | I | I | I | I | I | C | I | R |

† Sparsh's row is I by default on scripting/production/DM-fulfillment; it becomes **C** (or the
sole **R**) only on the specific `[SPARSH]`-tagged lines of that item's assets.md (raw photos,
his face/voice, account logins, a deliverable only he can export) — never for the item as a
whole.
‡ Planner's R on ship approval is administrative only: packaging the consolidated ask and
recording `approved_by_sparsh: <date>` in item.yaml once Sparsh has decided. The decision itself
is Sparsh's alone.
§ Joint accountability, weekly-review only (`ops/RUNBOOK.md` §3) — neither party changes
BETS.md status or STRATEGY.md content outside that session, and never unilaterally.
¶ BC is Consulted at briefing only when the Brand-Touch Score triggers a `/consult`
(SYSTEM_DESIGN §12.3); otherwise Informed via the brief's logged BTS.
‖ BC's R on knowledge-bank writes covers `knowledge/marketing/*` only (brand-director
maintains the distinctive-asset register and marketing files, via weekly review / quarterly
audit — RUNBOOK §9); all other knowledge writes stay with the analyst per (e).

---

## Decision rights

Who can actually pull each trigger — independent of who's merely Responsible/Consulted above:

**(a) Kill a concept (pre-script — IDEA/BRIEFED):** creative-director, on selector-formula
failure (STRATEGY §4's 5-point test). No critic gate required — nothing has been produced yet.

**(b) Kill a scripted or produced item (G1/G2 and later):** critic only, via a KILL verdict on
the 8-lens scorecard, or automatically after 2 failed FIX rounds absent a Sparsh escalation
resolving it. Not the Showrunner, not the authoring agent.

**(c) Approve SHIP:** Sparsh only. No proxy, no default-approve on timeout — an unresolved
READY item stays READY (see the >72h drill, `ops/RUNBOOK.md` §8).

**(d) Change a BETS.md status** (UNTESTED/VALIDATING/VALIDATED/FAILED): decided only inside
`/weekly-review`, only by Sparsh + Showrunner jointly, on evidence the analyst presents. Nobody
edits a bet's status field outside that ritual.

**(e) Edit knowledge files:** `knowledge/benchmarks.md` and any `[OWN-DATA]` entry — analyst
only, only via the postmortem/weekly-review skills (SYSTEM_DESIGN §4 rule 2). Any other
knowledge-file edit that would create an exception to a stated law requires it to be written
down in the item folder AND agreed by the critic (`CLAUDE.md`'s closing rule) before it's
applied; routine craft-file additions still route through analyst → Showrunner approval (the
calibration loop, `ops/RUNBOOK.md` §7).

**(f) Change STRATEGY.md:** only Sparsh + Showrunner, only in the weekly review — same
constraint as (d), and for the same reason: strategy drifts on evidence, not on mid-week
conviction.

**(g) Spend money:** Sparsh only. This includes paid tools, sponsorship commitments, and any
future monetization mechanic (BETS.md deferred list) — never automated, never delegated, no
exceptions.

**(h) HOLD an item at G3:** the brand-director, via the §12.4 verdict math and hard-HOLD
triggers — never on instinct alone (the math wins; instinct goes in notes). Only Sparsh can
override a HOLD, and the override is recorded in a `G3-brand-r2.md`. The Brand Office cannot veto
craft choices (critic's domain) and the critic cannot veto brand-portfolio calls (Brand Office's
domain).

**(i) Edit `knowledge/marketing/` files:** brand-director only, via `/weekly-review` or the
quarterly brand audit (RUNBOOK §9) — same write-discipline pattern as (e).

**(j) Change `strategy/REVENUE.md` (thresholds, stream status, product-pipeline gates):**
only inside `/revenue-review`, only with Sparsh + Showrunner joint sign-off on the
revenue-lead's evidence — same constraint and reason as (d)/(f). Actual spend or pricing
remains (g): Sparsh only, always.
