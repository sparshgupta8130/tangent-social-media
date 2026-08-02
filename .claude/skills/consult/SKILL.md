---
name: consult
description: Use when a brief's Brand-Touch Score (BTS) is ≥3 (mandatory, SYSTEM_DESIGN §12.3), when BTS is 1-2 and the Showrunner elects to consult, or whenever a Studio agent or Sparsh has a brand, growth, or audience-trust question mid-item. Routes the question to exactly one Brand Office agent and produces an advisory consult memo — never a decision.
---

## Purpose
Get domain expertise from the Brand Office into a Studio decision without handing the Brand Office
decision rights. The output is always advisory; creative and operational authority stays with the
Studio (SYSTEM_DESIGN §12.1) except at G3.

## Preconditions
- The triggering question exists in writing somewhere already reachable (a brief being written, a
  format decision, a mid-production question) — this skill does not manufacture the question, it
  routes one that already exists.
- BTS has been computed by the Showrunner (§12.3's flag table) and recorded in `brief.md` if this
  is a briefing-time consult. BTS ≥3 makes this skill mandatory before scripting; BTS 1-2 makes it
  the Showrunner's call (recorded either way — a silent skip at BTS ≥3 is an audit failure); BTS 0
  never triggers a consult (the item still reaches the Brand Office at G3).
- Ad hoc consults (a Studio agent or Sparsh has a question outside brief-time) have no BTS
  precondition — any genuine domain question can trigger this skill directly.

## Protocol
1. **Write the question block** — the Showrunner (or the requesting agent) writes: context, the
   specific decision to be made, options already considered, and a deadline. Never dispatch a bare
   "thoughts?" — an underspecified question produces an underspecified memo.
2. **Route by domain to exactly ONE Brand Office agent** (Task, matching `subagent_type`):
   - `brand-director` — identity, naming, positioning, format-vs-brand fit.
   - `growth-lead` — funnel changes, monetization timing, platform expansion, sponsorship
     economics.
   - `audience-advocate` — backlash risk, disclosure edge cases, community moves, comment-response
     strategy.
   Invoke a second agent only when the question genuinely straddles two domains (e.g., a
   monetization mechanic with real backlash exposure) — never all three by default. This is a
   lean bench on purpose; over-consulting defeats it as surely as under-consulting.
3. **Agent answers** via `templates/consult-memo.md`, written to `NNN-slug/consults/
   YYYY-MM-DD-<topic>.md` (item-bound) or `ops/council/consults/YYYY-MM-DD-<topic>.md` (general,
   no specific item). The memo is ADVISORY: POSITION stated first, then EVIDENCE (every point
   cited per §12.5), CONFIDENCE, and WHAT WOULD CHANGE MY MIND.
4. **Showrunner/Studio decides.** Deciding WITH the memo needs no further record beyond the memo
   itself. Deciding AGAINST it is legal but never silent: append one line to the same memo file (or
   a decision log entry alongside it) naming the decision and the reason.
5. **Record in `brief.md`**: the BTS score + which flags fired (§12.3 table), which agent was
   consulted and why, and the one-line outcome (followed / overridden + reason pointer). This is
   what makes a silent skip auditable later.

## Gates
- Zero-hallucination rule (§12.5) on every claim in the memo: knowledge-file citation, a
  `knowledge/SOURCES.md`-whitelisted source (URL + fetch date), or `[OWN-DATA]` — anything else is
  written UNKNOWN with a logged research gap, never estimated or recalled from memory.
- Exactly one agent by default; a two-agent dispatch requires stating which second domain applies
  and why, in the question block itself.

## Outputs
- `NNN-slug/consults/YYYY-MM-DD-<topic>.md` or `ops/council/consults/YYYY-MM-DD-<topic>.md`, from
  `templates/consult-memo.md`.
- `brief.md` updated with BTS + consult routing + outcome (step 5) — this skill does not call
  `tools/pipeline.py` itself; it produces the record a later stage transition can point to.

## On failure
- Consulted agent lacks evidence to answer with confidence: the memo says **UNKNOWN** in the
  relevant EVIDENCE point and logs a research gap — it does not guess. The agent may optionally run
  one bounded WebSearch against the `knowledge/SOURCES.md` whitelist to close the gap before
  finalizing; if the whitelist has no matching tier, the gap stays open and is named as such.
- The question actually belongs to the critic's craft domain (hook strength, pacing, aesthetics,
  differentiation) rather than a brand/growth/audience-trust question: redirect to `/critique`
  instead of answering — a Brand Office agent answering a craft question is a domain violation, not a
  service.
- Routing is ambiguous between two Brand Office agents and doesn't clearly "genuinely overlap": default
  to the single best-fit domain rather than dispatching both; note the ambiguity in the question
  block for whoever reads the memo later.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **INTERACTIVE:** present the memo conversationally alongside the Showrunner's own position
  (agree/disagree, and why) — never a bare memo dump. Sparsh's reaction, if he's in the session,
  folds directly into the decision log written in step 4; his enthusiasm for a position discussed
  earlier never substitutes for a reaction to this specific memo.
- **AUTONOMOUS:** proceed per the memo's POSITION unless it conflicts with a non-negotiable
  (`CLAUDE.md`) or the constitutional never-list (`strategy/STRATEGY.md` §2) — in that case treat it
  as a low-confidence creative call and escalate per `ops/RUNBOOK.md` §5 instead of overriding
  silently. Log everything either way; nothing here is exempt from write-as-you-go.
