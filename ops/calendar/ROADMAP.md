Tangent Social — Rolling Roadmap

**Owner:** planner. **Rebuilt:** every Monday `/plan` (full refresh) and touched at any standup
that surfaces a delay, a news-response insertion, or a bet-gate need (`ops/RUNBOOK.md` §3, §5).
**Horizon:** rolling 3–4 weeks; older weeks are trimmed once CLOSED, not archived here.

**How to read a week section:** one line per pipeline item, linking its `ops/pipeline/NNN-slug/`
id and current stage (from `python tools/pipeline.py board`) — this file is a view over the
pipeline, not a second source of truth for content state; if it disagrees with the pipeline,
the pipeline wins and this file gets corrected. Each week also carries a cadence-band note:
which STRATEGY §7 band the week is targeting (steady-state 3–5 reels + ≤1 long-form/month,
floor 2/week; or a time-boxed launch surge, ≤30 days, ≤once/quarter) and why, plus a reserved
news-response slot (may sit empty — see `ops/RUNBOOK.md` §5 on what gets bumped to fill it).

Per-week detail (slots table, Sparsh-dependency summary) lives in that week's
`templates/roadmap-week.md` instance if the team chooses to spin one out separately; the table
below is the compact rolling view planner maintains directly in this file.

---

## Replan log

Every `/plan replan` prepends a dated note here (newest first) so the roadmap keeps its own
audit trail of why it moved off the Monday plan — `.claude/skills/plan/SKILL.md` "replan" step 5.

- *(none yet)*

---

## Week of YYYY-MM-DD

**Cadence target:** steady-state | launch-surge — *why this band this week*
**HERO drought check:** days since last HERO publish — flag if >7 (`tools/calendar.py`)

| Day | Pillar | Item (id-slug) | Stage now | Risk |
|---|---|---|---|---|
| Mon | HERO\|WORKHORSE\|FILLER | `NNN-slug` | IDEA\|BRIEFED\|SCRIPTED\|PRODUCING\|CUT\|READY\|PUBLISHED | none / BLOCKED-ON-SPARSH / news-perishable |
| Tue | | | | |
| Wed | | | | |
| Thu | | | | |
| Fri | | | | |
| Sat | | | | |
| Sun | | | | |

**News-response reserve slot:** empty | filled by `NNN-slug` (window: A1, expires YYYY-MM-DD)

**Sparsh-dependency summary:** N items BLOCKED-ON-SPARSH this week — list ids, what's needed,
due dates (consolidated per item, `ops/RUNBOOK.md` §4).

---

*(Add the next `## Week of YYYY-MM-DD` section above this line as weeks roll forward; drop the
oldest week once every item in it reaches CLOSED or KILLED.)*
