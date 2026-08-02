# Critique Scorecard — <item title>

Produced by: critic, via `/critique`. Gate: **G1 (script.md)** | **G2 (cut)** — delete one.
Item: `ops/pipeline/NNN-slug/`. File: `critiques/G1-script.md` | `G2-cut.md` (round 1), or
`-r2.md` / `-r3.md` for re-reviews. Round: 1 | 2 | 3 — FIX is a legal verdict only on rounds 1
and 2; round 3 MUST resolve to SHIP or KILL, or escalate to Sparsh if genuinely undecidable
(`ops/RUNBOOK.md` §5). Reviewed artifact: `script.md` | `<cut file/description + stills>`.

The critic is structurally independent (SYSTEM_DESIGN §3): this scorecard is filled without
input from the authoring agent's self-assessment. Every deduction below cites a knowledge file
and, where applicable, a named law — no vibes.

---

## Lenses 1–7 (scored /10 each)

### 1. HOOK (weight ×2)
First-frame test: describe frame 0 — would a cold scroller stop? Payoff named/shown ≤1s (YT) /
≤3s (IG)? Curiosity gap present? Zero preamble?
- **Score:** /10
- **Deductions (cite `knowledge/craft/reels/hooks.md` + law):**
- **Notes:**

### 2. STRUCTURE & RETENTION
Loop map complete (every opened loop closes)? Granular state-changes ≤15s apart? Escalation
order? Ending lands? Length earns itself?
- **Score:** /10
- **Deductions (cite `knowledge/craft/reels/structure-and-retention.md` + law):**
- **Notes:**

### 3. EMOTION & INTENSITY
Target emotion named? High-arousal (awe)? STEPPS intensity, not mere presence? Clears the
payoff-intensity bar?
- **Score:** /10
- **Deductions (cite `knowledge/virality/laws.md` + law):**
- **Notes:**

### 4. CLARITY & ONE-IDEA
Sound-off test (legible from visuals+text alone)? One-sentence takeaway? Jargon scan vs the
35+ tone standard?
- **Score:** /10
- **Deductions (cite `knowledge/craft/reels/scripting-voice.md` + law):**
- **Notes:**

### 5. CRAFT & AESTHETICS
Visual grade vs the gallery-brand bar? Audio mix? Caption typography/safe zones? Cut
cleanliness? (We sell taste; craft slop is brand death.)
- **Score:** /10
- **Deductions (cite `knowledge/brand/tangent-voice.md` + `knowledge/production/assembly-playbook.md`):**
- **Notes:**

### 6. AUDIENCE FIT & SHAREABILITY
"Send this to ___" addressee test. Social currency? Save value? Persona match
(`knowledge/audience/personas.md`)?
- **Score:** /10
- **Deductions (cite `knowledge/audience/personas.md` + law):**
- **Notes:**

### 7. DIFFERENTIATION
Against `knowledge/pattern-library.md`: too-similar (which creator does this ape?) vs
too-niche (who outside the bubble cares?). Does it use OUR unfair advantages
(STRATEGY §8 — the moat)?
- **Score:** /10
- **Deductions (cite `knowledge/pattern-library.md` entry):**
- **Notes:**

---

## Lens 8. HYGIENE & COMPLIANCE (binary — any FAIL blocks SHIP outright)

| Check | PASS/FAIL | Evidence |
|---|---|---|
| Platform penalty list clear (`knowledge/platform/instagram.md` or `.../youtube.md`) | | |
| Engagement-bait line not crossed (`knowledge/platform/instagram.md`) | | |
| Disclosure rules met (`knowledge/audience/positioning.md`) | | |
| Brand non-negotiables clear (own-work only, no bought reach, no IP mashups — CLAUDE.md) | | |

**Lens-8 overall:** ALL-PASS | FAIL (name which check)

---

## Gate math

```
weighted_mean = (2 × HOOK + STRUCTURE + EMOTION + CLARITY + CRAFT + AUDIENCE + DIFFERENTIATION) / 8

HOOK score:            __ /10
Weighted mean:         __  (threshold: ≥ 7.5)
HOOK ≥ 8?              yes/no
Lens-8 ALL-PASS?       yes/no

Eligible for SHIP only if: weighted_mean ≥ 7.5  AND  HOOK ≥ 8  AND  lens-8 ALL-PASS
```

## VERDICT: SHIP | FIX | KILL

**This heading is NOT what `pipeline.py` checks.** Immediately below, write a standalone line
reading exactly one of `VERDICT: SHIP` / `VERDICT: FIX` / `VERDICT: KILL` — no `##`, no
surrounding text, case-sensitive, its own line. `pipeline.py`'s gate check greps for the literal
`VERDICT: SHIP` line before allowing SCRIPTED→PRODUCING (G1) or CUT→READY (G2); writing it when
the gate math in fact fails is a process violation, not a formality.

VERDICT: <SHIP|FIX|KILL>

<one line stating the reason>

### If FIX — ranked fix list (most load-bearing first)
1.
2.
3.

### What would make this a 10
<the standard is teaching, not just gatekeeping — name the specific change(s) that would clear
every lens at the top of its band>

### If KILL
**Reason:** <specific, evidence-cited>
**Salvage note:** <what's reusable — hook idea, asset, angle for a future item>

---

## G2 only — hygiene_check tool output

Paste the full `tools/hygiene_check.py` PASS/FAIL output here (resolution, aspect ratio,
duration band, audio stream, codec, black-border/cropdetect, file-hash-not-in-published-ledger).
Any tool FAIL blocks G2 regardless of the scores above.

```
<paste tools/hygiene_check.py output verbatim>
```
