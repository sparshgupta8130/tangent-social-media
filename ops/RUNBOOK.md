Tangent Social — Operating Runbook

The complete operating protocol for the Showrunner and the three offices (SYSTEM_DESIGN_V2
— approved 2026-08-02): the Studio (4 agents), the Brand Office (4 agents, §9), and
Operations (3 agents). `CLAUDE.md` is the
constitution (loaded every session, ≤150 lines, non-negotiables); this file is the protocol —
how a session actually runs, stage by stage, week by week. `SYSTEM_DESIGN.md` is authoritative
architecture; if this file and `SYSTEM_DESIGN.md` disagree, `SYSTEM_DESIGN.md` wins and this
file is wrong and should be fixed.

---

## 1. The session — modes and rhythm

**Two operating modes** (constitution: `CLAUDE.md`). **INTERACTIVE is the default**: the
Showrunner session is a long-running creative working session with Sparsh in the loop —
think writers'-room, not ticket queue. **AUTONOMOUS** applies only when Sparsh explicitly
says so ("run ahead", "autonomous mode") or in scheduled/headless runs. Mode changes how
stage boundaries are handled (checkpoint conversation vs. high-confidence default + log);
it never changes the gates themselves — the critic grades cold in both modes and never
reads the session conversation; hygiene FAILs and the SHIP approval are mode-independent.

**The interactive loop** (per stage of the item being worked):
1. **Set up** — one short message: what stage we're at, what the skill is about to do, any
   choice worth making before work starts (e.g. which concept to pull, capture-plan scope).
2. **Work** — run the skill/agents as specced. Long agent work runs in background while the
   conversation continues on other items or decisions.
3. **Present** — show the actual work product (concepts + kill list, hook variants + beat
   sheet, critique verdict + ranked fixes, cut + hygiene output), with the Showrunner's own
   recommendation. Never present a menu without a recommendation.
4. **Iterate** — fold Sparsh's reactions in: respin with the relevant agent inline, as many
   rounds as the conversation wants. Small edits (retitle, hook tweak, beat reorder) are
   done directly; substantive redos go back through the owning agent.
5. **Record & advance** — write the outcome into the item folder (brief/script/critiques/
   notes), then `pipeline.py stage`. **Write-as-you-go is mandatory**: the session may run
   for days and be context-compressed at any point — after a compression, state is rebuilt
   ONLY from `pipeline.py board` + item folders + this runbook, never from chat memory. A
   decision that exists only in conversation does not exist.

Each skill's file ends with an **Interaction checkpoints** section naming its stage-specific
presentation and iteration points; those are the authoritative per-stage protocol.

**Session start, both modes** (verbatim from `CLAUDE.md`):
   1. `python tools/pipeline.py board` — full status of every open item (stage, next_action,
      owner, due, overdue flag).
   2. Read `ops/calendar/ROADMAP.md` for this week's plan and `strategy/BETS.md` for live gates.
   3. Check the top entry date in `ops/calendar/trends-log.md`; if >24h old, run `/trend-sweep`
      before anything else — trend windows decay in days, not weeks.
   4. `python tools/pipeline.py blocked` — surface BLOCKED-ON-SPARSH and overdue items. Any
      overdue item, or any BLOCKED-ON-SPARSH item past its due date, is itself a trigger for a
      standup note (§3) even outside the Monday/Friday rituals.
   5. INTERACTIVE: open with "where we are" (3–6 lines: items in flight, blocked, proposed
      next move) and follow Sparsh's lead. AUTONOMOUS: do what the session was opened for.
      Never freelance a workflow that a skill already covers; invoke the skill.

### What a working session looks like

- **Ritual day?** Monday → `/plan` (roadmap refresh). Friday → `/weekly-review`. Run the ritual
  first; it re-prioritizes everything after it.
- **Otherwise, pipeline work:** take the highest-priority non-blocked item from
  `pipeline.py board`, identify its current stage, and invoke the one skill that advances it
  (table in §2). Work HERO items before WORKHORSE before FILLER when several are ready at once,
  unless a news window (§5) or a due date says otherwise.
- **Nothing ready to advance?** Do not idle. Pull the next IDEA-stage note through `/ideate`, or
  clear a BLOCKED-ON-SPARSH item's non-Sparsh sub-tasks (asset prep that doesn't need him,
  differentiation research, draft captions), or run `/trend-sweep` early.
- **Trend-sweep cadence:** daily-ish, minimum once per 24h wall-clock. `trend-scout` also runs
  it ad hoc mid-session on a hot signal (a competitor post, an Adobe/Anthropic announcement) —
  it does not wait for the next scheduled sweep to log a 0–4-day window.

---

## 2. The content lifecycle, end to end

One folder per item (`ops/pipeline/NNN-slug/`, contract in `ops/pipeline/README.md`). All
stage changes go through `tools/pipeline.py` — nobody hand-edits `item.yaml`'s `stage` field.
The tool's stage sequence is fixed: IDEA → BRIEFED → SCRIPTED → PRODUCING → CUT → READY →
PUBLISHED → POSTMORTEM → CLOSED (or KILLED from anywhere). **G1, G2, G3, and SHIP are gate checks
on a specific transition, not stage values** — see the callout below the table.

| Transition | Skill | Primary agent(s) | Gate / requirement | Target turnaround |
|---|---|---|---|---|
| — → IDEA | `pipeline.py new` | Showrunner or planner | none — entry point | instant |
| IDEA → BRIEFED | `/ideate` | trend-scout → creative-director | concept passes all 5 selector points (STRATEGY §4) or it dies here, uncosted | same session, ≤2h agent-time |
| BRIEFED → SCRIPTED | `/script` | story-lead | brief.md complete, ≥3 hook variants drafted | same session, ≤2h agent-time |
| SCRIPTED → PRODUCING (**G1 gate**) | `/critique` (script) → `/produce` | critic, then producer | 8-lens scorecard on script.md; weighted mean (HOOK×2) ≥7.5 AND HOOK≥8 AND hygiene lens all-PASS ⇒ `critiques/G1-script.md` gets a `VERDICT: SHIP` line, which is what `pipeline.py` checks before allowing SCRIPTED→PRODUCING | ≤1h after script.md lands for the verdict |
| G1 FIX loop | `/script` (revise) → `/critique` | story-lead, critic | ranked fix list from critique; re-score; item stays at `SCRIPTED` | ≤1 session/round, max 2 rounds |
| PRODUCING → CUT | `/produce` | producer | executes assets.md ([AGENT]/[GEN] first, [SPARSH] chased in parallel); assembly per `knowledge/production/assembly-playbook.md` | 1–3 days (asset-bound; [SPARSH] items are the variable — see §4) |
| CUT → READY (**G2 gate**) | `/critique` (cut) | critic | `tools/hygiene_check.py` runs FIRST; on any hygiene FAIL the gate stops before the critic is invoked — no critique file is written, no fix round is consumed, the cut goes straight back to `/produce` for re-export. Only a hygiene-PASS cut reaches the critic's 8-lens scorecard; a `critiques/G2-cut*.md` file with `VERDICT: SHIP` is what `pipeline.py` checks before allowing CUT→READY | ≤1h after cut + hygiene_check.py run |
| G2 FIX loop | `/produce` (re-cut) → `/critique` | producer, critic | same ranked-fix discipline; item stays at `CUT`; re-critique files use `-r2` suffixes | ≤1 day/round, max 2 rounds |
| at READY (**G3 brand gate**) | `/brand-review` | Brand Office (3 lenses, brand-director chairs) | three lens scores (Brand-Equity / Growth / Audience Trust) → `critiques/G3-brand.md` with `VERDICT: ADVANCE` / `ADVANCE-WITH-NOTES` / `HOLD` per SYSTEM_DESIGN §12.4; `pipeline.py` blocks READY→PUBLISHED without an ADVANCE-class verdict; HOLD escalates to Sparsh (override recorded as `-r2`) | ≤1h after entering READY; run before requesting SHIP approval so one Sparsh conversation covers both |
| READY → PUBLISHED (**SHIP gate**) | Sparsh approval, then `/publish` | Sparsh, then producer + planner | `pipeline.py stage NNN READY --approved-by-sparsh` records the date; `pipeline.py publish --url <url>` then checks the G3 verdict AND `approved_by_sparsh` before transitioning and recording the URL | target ≤48h from entering READY for the approval (consolidated ask, §4); publish itself same day |
| PUBLISHED → POSTMORTEM → CLOSED | `/postmortem` | analyst | verify_stats.py second-source check, 9-section postmortem, views×LR decomposition, knowledge-bank updates | T+72h minimum, complete by T+96h |

**G1/G2/SHIP are gates, not stages.** `item.yaml`'s `stage` field only ever holds one of the 9
sequence values above, or `KILLED` — never literally `G1`, `G2`, or `SHIP`. What SYSTEM_DESIGN
§5's `SCRIPTED → G1 ⟶ PRODUCING` notation means operationally: `pipeline.py` blocks
SCRIPTED→PRODUCING until `critiques/G1-script.md` carries a `VERDICT: SHIP` line, and blocks
CUT→READY until a `critiques/G2-cut*.md` file does the same (`tools/pipeline.py`'s
`_gate_check`). A FIX verdict does not advance the stage at all — the item stays at `SCRIPTED`
(or `CUT`) through the fix round.

**Who does what, in prose:** creative-director owns the concept and the brief and makes the
creative kill/ship recommendation at ideation; story-lead turns an approved brief into a
shot-by-shot script and minimizes `[SPARSH]` tags; producer executes the asset manifest and
assembles the cut; critic is structurally independent at both gates — it never fixes what it
grades, and skills pass it the work product without the authoring agent's self-assessment;
planner tracks the board, Plane, and the Sparsh queue; the Showrunner orchestrates all of it via
skills and is the last internal check before anything reaches Sparsh.

### The KILLED path

Any stage can end in KILLED via `pipeline.py kill NNN --reason "..."`, which sets
`stage: KILLED` and records the reason in `kill_reason` (a bare `pipeline.py stage NNN KILLED`
is rejected — kill always goes through this command so a reason is never skipped). Item.yaml
has no separate field for the salvage note, so write it into the same `--reason` string (what,
if anything, is reusable — a hook idea, an asset, an angle for later). Who can trigger it:

- **Pre-script (IDEA/BRIEFED):** creative-director, when a concept fails the 5-point selector.
  No critic gate needed — nothing has cost effort yet.
- **Post-script (G1) or post-cut (G2):** critic only, via a KILL verdict, or automatically after
  2 failed FIX rounds without a Sparsh escalation resolving it (§5).
- **At READY:** Sparsh, by declining SHIP with a reason — this is not silent; the reason is
  logged the same way.
- **News-perishable items:** planner, when a news-response item's window closes before
  production can finish (§5).

---

## 3. Weekly rhythm

- **Monday `/plan`:** roadmap refresh. Planner rebuilds/updates the rolling 3–4-week
  `ops/calendar/ROADMAP.md` from pipeline state, BETS.md validation needs, and Sparsh
  availability; reconciles Plane against `pipeline.py board`.
- **Standups:** not a fixed time slot — triggered by **any session start that surfaces an
  overdue item or a BLOCKED-ON-SPARSH item past due** (step 4 of the session-start protocol).
  When triggered, planner produces the cheap standup report: board snapshot, overdue list,
  blockers list, next actions. This can fire multiple times a day; it is intentionally cheap.
- **Friday `/weekly-review`:** the full ritual, in this exact order (analyst → planner →
  creative-director), written to `ops/calendar/review-YYYY-WW.md` from
  `templates/weekly-review.md`:
  1. **Metrics report** — analyst runs `tools/metrics.py report --csv ops/calendar/posts.csv
     --followers N --json` (the rolling stats CSV the analyst appends to on every postmortem):
     per-post decomposition, account medians, efficiency, funnel ratios, early-warning triad
     check.
  2. **Bet gates** — analyst checks each live bet in `strategy/BETS.md` against its validation
     gate and kill/pivot trigger with this week's numbers; proposes UNTESTED/VALIDATING/
     VALIDATED/FAILED status changes with evidence.
  3. **Pillar accounting** — medians per tier (HERO/WORKHORSE/FILLER) vs account median
     (STRATEGY §6.1); HERO-drought check (`tools/calendar.py` flags >7 days with no HERO).
  4. **Format kill/keep** — creative-director reviews the ≤3 owned formats (STRATEGY §4)
     against this week's evidence; kill/replace decisions happen ONLY here, never mid-week. Any
     change appends a dated `[OWN-DATA]` line to `knowledge/brand/content-architecture.md`'s
     format list.
  5. **Next-week roadmap** — planner picks next week's cadence inside the STRATEGY §7 bands and
     hands the updated roadmap to `ops/calendar/ROADMAP.md`.
  - This is the only session in which `strategy/BETS.md` status fields and
    `strategy/STRATEGY.md` itself may be edited, and only jointly by Sparsh + Showrunner
    (`ops/ROLES.md` decision rights).

---

## 4. The Sparsh interface

- **INTERACTIVE mode (default): the conversation IS the interface.** His taste enters live at
  the skills' interaction checkpoints (concept review, hook/beat review, post-critique
  walkthrough, cut review). The Showrunner behaves as a creative partner with a spine:
  always a recommendation, never a bare menu; disagree with reasons and knowledge-bank
  citations; never yes-and a weak idea. He can overrule anything except a hygiene FAIL — an
  overruled critic verdict is logged in the item folder as a knowledge-law exception
  (`CLAUDE.md` final paragraph). `[SPARSH]` asset needs can be asked for in-conversation the
  moment they're identified — but still get recorded as the item's `BLOCKED-ON-SPARSH`
  next-action until delivered, so a context reset never loses the ask.
- **Notes in:** Sparsh drops short notes (a line, a link, a voice memo transcript) anywhere;
  the next `/ideate` run is what turns them into scored concepts and briefs. Notes are never
  acted on directly outside `/ideate` — that skill is where the selector formula and kill
  discipline apply.
- **Consolidated-ask rule (AUTONOMOUS mode, and any need that outlives the session):** every
  `[SPARSH]`-tagged need becomes exactly one `BLOCKED-ON-SPARSH` next-action per item, with
  a due date, surfaced on the board. The team never drips individual asks to him — if an
  item needs three things from Sparsh, that's one next-action listing all three, not three
  pings. Stale BLOCKED-ON-SPARSH items (past due) surface in every standup (§3) until
  resolved.
- **His three approval points (never automated, never delegated):**
  1. **SHIP** — final publish approval on every item, recorded as `approved_by_sparsh: <date>`.
  2. **Money** — anything involving spend (sponsorship terms, paid tools, presets/courses once
     monetization is revisited per BETS.md deferred list).
  3. **Face/voice** — any post that shows him on camera or uses his voice.
- **Response-time expectations:** target ≤48h from an item entering READY, or from a
  BLOCKED-ON-SPARSH item's due date, before it counts as overdue on the board. This is a
  target, not a gate that stalls the pipeline — see the >72h failure drill (§8).
- **Consolidated ask, worked example:** wrong — three separate pings ("need the raw for
  042-golden-hour-restore", "need the raw for 043-portrait-series-ep2", "confirm the DM preset
  file for 041-desert-preset"). Right — one next-action on the board:
  `BLOCKED-ON-SPARSH: 3 items need input (raws: 042, 043; preset file: 041) — due 2026-08-02`,
  linking all three item folders. One ask, one due date, one place to answer.
- **What the team does while blocked: never idle.** A BLOCKED-ON-SPARSH item does not pause the
  session. Work the next item in the pipeline — another item's ideation, scripting, production,
  or critique — while the blocked item waits. Non-Sparsh sub-tasks on the blocked item itself
  (asset prep, caption drafts, differentiation checks) continue in parallel where possible.

---

## 5. Escalation & exception protocol

- **Low-confidence creative calls:** when confidence is genuinely low (not just a hard
  decision — an actually uncertain one), the deciding agent writes the question, the team's
  best two options, and a recommendation into the item folder (a note alongside brief.md or
  script.md) and flags planner to surface it at the next standup or, if urgent, immediately.
  This is Sparsh's "creative gate of last resort" role in practice — used sparingly, not as a
  default escape hatch.
- **Critic deadlocks:** a script or cut that fails FIX twice (2 rounds, per §2) cannot go a
  third round silently. The Showrunner must either (a) kill it via `pipeline.py kill`, logging
  why 2 rounds weren't enough, or (b) escalate to Sparsh with the same two-options-plus-
  recommendation format as above. There is no third autonomous fix round.
- **Knowledge-law exceptions:** per `CLAUDE.md`'s closing line — when judgment conflicts with a
  knowledge-bank law, the law wins unless the exception is written down in the item folder AND
  the critic agrees. An unwritten exception, or one the critic hasn't signed off on, is not an
  exception; it's a violation. This applies to every law in `knowledge/virality/laws.md` and
  every non-negotiable in `CLAUDE.md`.
- **News-window interrupts:** when `trend-scout` logs an A1 (0–4-day window) entry in
  `ops/calendar/trends-log.md`, it pings planner immediately (does not wait for the next
  standup). Planner inserts a news-response item into the current week's roadmap as FILLER
  (STRATEGY §4), reserving the news-response slot the roadmap already carries
  (`templates/roadmap-week.md`). What gets bumped: the lowest-priority FILLER or WORKHORSE item
  not yet past SCRIPTED this week — never a HERO item, and never an item already at G2 or later.
  If no bumpable slot exists, the news item queues for the next sweep and the window is logged
  as missed with the reason.

---

## 6. Plane operations

- **Bootstrap:** first `/plan` run in a fresh workspace creates the Plane project
  **"Tangent Social"** (identifier `TANSOC`) with states Backlog/Planned/In Progress/
  Blocked-on-Sparsh/In Review/Done/Killed and labels `hero`, `workhorse`, `filler`, `series`,
  `news`, `ops`, `sparsh-input` (SYSTEM_DESIGN §9). Idempotent — re-running `/plan` checks for
  the project before creating it.
- **Item lifecycle mirroring:** a pipeline item gets its Plane work item the moment it reaches
  BRIEFED; the id is recorded in `item.yaml`'s `plane_issue` field. Labels map straight from
  item metadata: `hero`/`workhorse`/`filler` from item.yaml's `pillar` field (always exactly
  one), `series` added when the item belongs to a numbered wrapper, `news` added for
  news-response insertions (§5), `ops` for non-content pipeline work (tooling, knowledge-bank
  maintenance), `sparsh-input` added the moment an item first goes BLOCKED-ON-SPARSH and left on
  even after it clears (a historical marker of what needed him). From there planner keeps
  Plane state in step with pipeline stage on every session touching that item (SCRIPTED/G1 →
  In Progress or Blocked-on-Sparsh as applicable; READY → In Review; CLOSED → Done; KILLED →
  Killed). Plane is the roadmap/accountability view for humans; **the repo (`ops/pipeline/`) is
  the source of truth for content artifacts** — if the two ever disagree, the repo wins and
  Plane gets corrected, not the other way round.
- **Fallback:** if the Plane MCP is unavailable in a session, planner does not block content
  work on it. `ops/calendar/ROADMAP.md` becomes the sole truth for that session, and planner
  queues a sync note (a line in the roadmap or standup output naming which items need their
  Plane state reconciled) to run the next time Plane is reachable.

---

## 7. Calibration & learning loops

- **Postmortem → knowledge-bank updates:** every `/postmortem` run that surfaces a durable
  finding (not a one-off) writes an `[OWN-DATA]`-tagged entry into the relevant craft/platform
  knowledge file, per SYSTEM_DESIGN §4's provenance rule. Only the analyst writes these, only
  through the postmortem/weekly-review skills — never mid-task to win an argument. The
  completed `postmortem.md` is also appended under `research/own/` (SYSTEM_DESIGN §2) — the one
  sanctioned write path into the otherwise read-only research archive, growing our own evidence
  corpus alongside the external one.
- **Critic-score-vs-outcome calibration:** part of every postmortem (`templates/postmortem.md`'s
  critic-calibration block) — G2 scores are compared against actual performance. When a pattern
  of systematic misses emerges (not a single data point), the analyst proposes a specific
  critic-prompt update (which lens, what evidence, what the prompt should say instead) and the
  Showrunner approves or rejects it before it's applied to `.claude/agents/critic.md`.
- **Quarterly knowledge-bank review:** a stale-claim sweep — every file in `knowledge/` is
  checked for claims whose evidence tier or currency has aged out (a `[PRACTITIONER LORE]`
  claim later contradicted by `[OWN-DATA]`, a platform spec that's changed). Retraction
  discipline applies: correct and mark, never silently delete. Scheduled at the first
  `/weekly-review` of each new quarter; owned by the analyst, approved by the Showrunner.

---

## 8. Failure drills

- **A published post dies (<0.5x median):** run the views×LR decomposition
  (`tools/metrics.py decompose`) to classify hook/discovery failure vs craft failure, log it in
  that item's postmortem, and move on. No panic pivots off a single data point — STRATEGY §6.1
  ("plan on medians; treat spikes as windfalls") applies symmetrically to flops. One flop is a
  data point; a pattern is what changes the roadmap, and patterns are Friday's business (§3),
  not same-day reactions.
- **A post spikes off-pillar:** windfall discipline per STRATEGY §6.7 — enjoy it, capture it
  with a wrapper/series if one fits naturally, and never rebuild the roadmap or the format
  portfolio around it. Log it as a data point for the audience-mismatch triad (below), nothing
  more, unless the triad actually fires.
- **An account-level warning triad fires** (STRATEGY §6.6: efficiency sliding under ~5%; hits
  coming only from off-pillar content; flat non-pinned spread — checked monthly): **2 of 3** is
  the trigger. Planner schedules a strategy review session (not the regular weekly review — an
  additional one) with Sparsh + Showrunner + analyst before the next normal `/weekly-review`.
- **Sparsh unavailable >72h:** the pipeline does not stall. Every item keeps advancing through
  its stages up to READY and holds there — READY items accumulate into a queue rather than
  publishing without approval (SHIP is never automated, non-negotiable #7 in `CLAUDE.md`).
  Planner logs each item's READY-entry timestamp so queue age is visible on the board, and when
  Sparsh returns he reviews the queue as one batched ask, not N separate ones (§4's
  consolidated-ask rule applied to a backlog).

---

## 9. Brand Office operations (SYSTEM_DESIGN §12)

The Brand Office (brand-director chair, growth-lead, audience-advocate) shares the
pipeline but never makes content. Three entry points:

- **The consult decision node — Brand-Touch Score.** At the end of every `/ideate` (and at
  any format/strategy decision), the Showrunner computes the BTS from the §12.3 flag table
  (new-format +3, identity-surface change +3, commercial element +3, backlash-adjacent +2,
  funnel-mechanic change +2, new platform +1, format/tone stretch +1) and writes score +
  flags into `brief.md`. **BTS ≥ 3 → `/consult` is mandatory before `/script`.** 1–2 →
  Showrunner judgment, decision noted in the brief. 0 → straight through (the Brand Office still
  sees the item at G3). A missing BTS in a brief is an audit failure.
- **Consults are routed, not broadcast:** one Brand Office agent by domain (strategist:
  identity/positioning/format-brand fit · scientist: funnel/monetization/platform/sponsor
  economics · advocate: trust/backlash/disclosure/community); two only on genuine overlap,
  never all three by default. Memos are advisory — the Studio may decide against one, but
  the decision + reason is logged in the same consults/ folder. Non-item consults live in
  `ops/council/consults/`.
- **G3 is not advisory.** Every item gets `/brand-review` at READY; `pipeline.py` will not
  publish without an ADVANCE-class verdict. HOLD goes to Sparsh with the strategist's
  reasoning and the Showrunner's own position; his override is recorded in a `-r2` review.
  ADVANCE-WITH-NOTES notes accrue in `ops/council/notes-ledger.md` and are checked at the
  next G3 and at weekly review — notes that never get honored are an audit failure.

**Rhythms:** monthly — `/revenue-review` (revenue-lead + Showrunner + Sparsh; the only
place `strategy/REVENUE.md` thresholds/status change). Weekly — brand-director's
brand-health section inside `/weekly-review`
(drift, asset consistency, portfolio balance, notes-ledger themes, sentiment summary from
audience-advocate). Quarterly — full brand audit: distinctive-asset register refresh,
positioning-doctrine review against accumulated [OWN-DATA], `knowledge/SOURCES.md`
whitelist refresh, citation-audit of a sample of the quarter's memos/verdicts.

**Boundary discipline (both directions):** the Brand Office never scores hooks, pacing, or craft
(the critic's domain, G1/G2); the critic never blocks on brand-portfolio grounds (the
Brand Office's domain, G3). A question that arrives at the wrong bench gets redirected, not
answered.
