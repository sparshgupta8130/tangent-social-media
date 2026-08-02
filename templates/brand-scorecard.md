# Brand Scorecard (G3) — <item title>

Produced by: `brand-director`, via `/brand-review`, synthesizing three independent lens scores.
Item: `ops/pipeline/NNN-slug/`. File: `critiques/G3-brand.md` (round 1) or `G3-brand-r2.md`
(Sparsh override only). Cut version reviewed: <path/version>. BTS at brief: <score> — flags:
<list>. Consult history: <list consult files + one-line outcome each, or "none — BTS 0">.

G3 judges brand trajectory only — it does not re-litigate G2's craft/hook/virality scores
(SYSTEM_DESIGN §12.4 rule 4). Each lens was scored independently, blind to the other two.

---

## Lens 1 — Brand-Equity Impact (`brand-director`)
Checklist: one-line-description test · distinctive-asset usage · positioning-drift check ·
portfolio-balance check (each anchored to `knowledge/marketing/`).
- **Score:** /10
- **Reasoning (3-6 bullets, each cited):**

## Lens 2 — Growth Contribution (`growth-lead`)
Checklist: category entry-point served? · funnel fed? · reach spent on the right audience?
- **Score:** /10
- **Reasoning (3-6 bullets, each cited):**

## Lens 3 — Audience Trust (`audience-advocate`)
Checklist: disclosure adequate? · any persona betrayed? · promise-keeping intact (DM deliverable
real + near-instant)? · backlash-map adjacency mitigated?
- **Score:** /10
- **Reasoning (3-6 bullets, each cited):**

---

## Hard-HOLD trigger checklist
Any **yes** forces HOLD regardless of the scores above.

| Trigger | Yes/No | Evidence |
|---|---|---|
| Never-list violation (`strategy/STRATEGY.md` §2) | | |
| Unmitigated backlash-flashpoint adjacency (`knowledge/audience/positioning.md`) | | |
| Positioning drift — one-line-description test fails | | |
| Distinctive-asset violation (`knowledge/marketing/distinctive-assets.md`) | | |

## Verdict math

```
mean = (Brand-Equity + Growth Contribution + Audience Trust) / 3

Brand-Equity Impact:     __ /10
Growth Contribution:     __ /10
Audience Trust:          __ /10
Mean:                    __

ADVANCE:            all three ≥7  AND  mean ≥7.5  AND  no hard-HOLD trigger
ADVANCE-WITH-NOTES: no lens ≤4    AND  mean ≥6     AND  no hard-HOLD trigger
HOLD:               any lens ≤4  OR   mean <6     OR   any hard-HOLD trigger = yes
```

## VERDICT: ADVANCE | ADVANCE-WITH-NOTES | HOLD

Standalone line below, exact text, case-sensitive — `tools/pipeline.py` greps this before allowing
`READY`→`PUBLISHED`:

VERDICT: <ADVANCE|ADVANCE-WITH-NOTES|HOLD>

<one line stating the reason>

### If HOLD
**Escalated to Sparsh with:** the reasoning above + the Showrunner's own position. Only Sparsh can
override — recorded as `G3-brand-r2.md` with `VERDICT: ADVANCE` + the override note.

### Notes for future items (ADVANCE-WITH-NOTES only)
Each note: what it says + which future item type it binds. Appended verbatim to
`ops/council/notes-ledger.md`; checked again at the next item's G3 and at `/weekly-review`.
-

### What would make this a 10 for the brand
<the specific change(s) that would clear every lens at the top of its band — teaching, not just
gatekeeping, mirroring the critic's own rule (SYSTEM_DESIGN §8) one altitude up.>
