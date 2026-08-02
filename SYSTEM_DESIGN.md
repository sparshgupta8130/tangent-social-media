# SYSTEM DESIGN — The Tangent Social Media Team (V1 reference)

> **V2 NOTICE (2026-08-02):** `SYSTEM_DESIGN_V2_PROPOSAL.md` ("The Label") was approved and
> amends this document: three offices (Studio / Brand Office / Operations), renames
> (scriptwriter→story-lead, brand-strategist→brand-director, growth-scientist→growth-lead),
> `revenue-lead` added, craft packs (`knowledge/craft/<vertical>/`, `item.yaml.vertical`),
> `brand/kit.yaml` + `tools/brandkit_check.py`, the revenue layer (`strategy/REVENUE.md`,
> `/revenue-review`), and the workload router. **Where the two disagree, V2 wins.** This
> file remains the detailed reference for everything V2 doesn't amend.

Authoritative architecture for the agent team that runs Tangent's social presence
(instagram: **tangentideas.ai**, site: **tangent.gallery**, plus YouTube). Every file in this
repo is built to this spec. If a file contradicts this spec, the file is wrong.

Owner (human): **Sparsh** — supervisor and creative gate of last resort. The design goal is
that Sparsh interacts through short notes and approvals; the team does everything else, and
asks for creative input only when it cannot resolve a question with high confidence itself.

---

## 1. Operating model

The team runs inside Claude Code sessions opened in this repo.

- **The Showrunner** = the main session model (highest-capability model available — Sparsh
  runs it as a long-lived Opus-class interactive session). It is the orchestrator, the
  cognitive engine, a creative partner, and the final internal quality gate. It reads
  `CLAUDE.md` (the constitution) on session start, checks pipeline state, and drives work by
  invoking skills, which delegate to the specialist agents below.
- **Two operating modes.** **INTERACTIVE (default):** Sparsh works the pipeline WITH the
  Showrunner, stage by stage — at every stage boundary the Showrunner presents the work
  product with a recommendation, iterates on his reactions (inline for small edits, via the
  owning agent for substantive redos), and advances only on his nod or an explicit "your
  call." **AUTONOMOUS:** only on explicit instruction or in scheduled/headless runs — the
  original high-confidence-defaults + consolidated-asks behavior. Modes change checkpoint
  behavior, never gates: the critic grades cold in both (it never reads the session
  conversation), hygiene FAILs are non-negotiable, SHIP always requires explicit approval.
  Write-as-you-go is constitutional in both modes: decisions live in item folders, not chat
  (long sessions get context-compressed; the repo is the memory). Per-skill checkpoint
  protocols live in each skill's "Interaction checkpoints" section; RUNBOOK §1 has the
  session loop.
- **Specialist agents** live in `.claude/agents/`. Each has one job, a bounded context, and a
  written contract (below). They communicate exclusively through **files in the repo** —
  briefs, scripts, scorecards, logs — never through unrecorded chat. If it isn't written to
  the pipeline, it didn't happen.
- **Skills** in `.claude/skills/` are the workflows — each one is a protocol that names its
  inputs, the agents it invokes, the tools it runs, the gates it must pass, and the files it
  must produce.
- **Tools** in `tools/` are deterministic Python scripts. Anything that must be exact
  (metrics math, state transitions, file hygiene checks, stat verification) is a tool, never
  a model's mental arithmetic.

### Human-input protocol (the autonomy contract)

Every content item carries an **asset manifest** (`assets.md`) in which every asset line is
tagged with exactly one provider:

- `[AGENT]` — the team produces it autonomously (screen captures of Claude driving Lightroom,
  ffmpeg assembly, text overlays, thumbnails, captions).
- `[GEN]` — generative tooling produces it (Veo/Flow b-roll, TTS narration) **subject to the
  disclosure rules** in `knowledge/audience/positioning.md`.
- `[SPARSH]` — only the human can provide it (raw photos, on-camera face/voice, account
  logins, final ship approval). The system MINIMIZES these: before tagging anything
  `[SPARSH]`, the story-lead must record why no `[AGENT]`/`[GEN]` substitute reaches the
  quality bar.

The planner chases `[SPARSH]` items like any other dependency: they appear in the status
board as `BLOCKED-ON-SPARSH` with a due date, and stale ones surface in every standup.

Sparsh's hard approval points (never automated): final SHIP approval before anything is
published, anything involving money, and any post that shows his face/voice.

---

## 2. Repository layout

```
tangent-social-media/
  CLAUDE.md                  # constitution — loaded every session; ≤150 lines
  SYSTEM_DESIGN.md           # this file
  strategy/
    STRATEGY.md              # principles + decision frameworks (NOT prescriptions)
    BETS.md                  # live register of strategic bets with validation gates
  knowledge/                 # the knowledge bank (see §4)
  ops/
    RUNBOOK.md               # operating protocols (see §6)
    ROLES.md                 # responsibility matrix: 7 agents + Showrunner + Sparsh
    pipeline/                # content items in flight (see §5)
      README.md
    calendar/
      ROADMAP.md             # rolling 3-4 week roadmap (planner-owned)
      trends-log.md          # trend-scout's running log
  tools/                     # deterministic scripts (see §7)
  templates/                 # brief.md, script.md, assets.md, critique-scorecard.md,
                             # publish.md, postmortem.md, weekly-review.md, roadmap-week.md
  research/                  # RAW research corpus (read-only; never edited by the team)
  synthesis/                 # frozen research syntheses (read-only)
  .claude/
    agents/                  # 7 agent definitions (see §3)
    skills/                  # 9 workflow skills (see §6)
```

`research/` and `synthesis/` are the evidence archive. The knowledge bank cites into them;
agents read them when they need primary evidence; nobody writes to them except through the
postmortem process (which appends new postmortems under `research/own/`).

---

## 3. The agent roster (`.claude/agents/`)

Seven agents. Frontmatter: `name`, `description` (when to invoke), `tools` (least
privilege), `model`. Body: role, contract (inputs → outputs), the knowledge files it must
read first, its quality bar, and its failure modes to avoid.

| Agent | Model | One-line contract |
|---|---|---|
| `creative-director` | inherit | Turns notes/opportunities into scored concepts and briefs; owns creative kill/ship recommendations. |
| `trend-scout` | sonnet | Watches the niche (Adobe/Anthropic/AI-imaging news, trending audio/formats, competitor moves); maintains `ops/calendar/trends-log.md`; flags 0–4-day windows. |
| `story-lead` | sonnet | Turns a brief into a shot-by-shot script + asset manifest with provider tags and hook variants. |
| `producer` | sonnet | Executes asset manifests: drives Lightroom-via-Chrome capture sessions, gen-video prompts, ffmpeg assembly, export QC. |
| `critic` | inherit | The brutal panel: scores scripts and cuts on 8 lenses against the scorecard; verdicts SHIP/FIX/KILL. No stake in the work; never softens. |
| `analyst` | sonnet | Post-publish measurement: verified stats, views×LR decomposition, benchmark medians, pivot signals, postmortems. |
| `planner` | sonnet | TPM/PM: roadmap, Plane work items, dependencies, standups, accountability, replanning on delays/news. |

Design rules:
- `creative-director` and `critic` inherit the session's top model — creative judgment and
  judgment-of-judgment are the two places intelligence is worth paying for.
- The critic is **structurally independent**: it is never asked to fix what it grades, and
  skills must pass it the work product without the authoring agent's self-assessment.
- Every agent definition names the knowledge files it MUST read before acting (its "load
  list") so knowledge actually reaches decisions.

---

## 4. The knowledge bank (`knowledge/`)

The creative-judgment substrate. Rules:

1. **Provenance or it doesn't exist.** Every substantive claim carries an evidence tier
   inherited from the research corpus — `[RESEARCH-BACKED]`, `[INDUSTRY DATA]`,
   `[PRACTITIONER LORE]`, `[CORPUS]` (from our 18-dossier study, cite the dossier), or
   `[OWN-DATA]` (from our published posts' postmortems) — plus retraction discipline: a
   corrected claim is marked, not silently kept.
2. **Living, but with write control.** `benchmarks.md` is written ONLY by the analyst via
   the postmortem/weekly-review skills. Craft files gain `[OWN-DATA]` entries the same way.
   Nobody edits knowledge mid-task to win an argument.
3. **INDEX.md is the map**: one line per file — what's in it, when to read it.

Files (builder fills them from `research/`, `synthesis/`, and the three research briefs in
the build scratchpad):

```
knowledge/
  INDEX.md
  craft/
    hooks.md                   # hook classes ranked by corpus win-rate; verbatim examples;
                               # the 1s/3s gate; first-frame test; anti-patterns
    structure-and-retention.md # loop discipline, escalating listicles, pacing, length bands,
                               # demo-in-motion grammar (the genre's beat rules)
    scripting-voice.md         # one-idea rule, sound-off legibility, caption/text rules,
                               # jargon bans, the 35+ tone standard, quotable-beat engineering
  virality/
    laws.md                    # the measurement layer (Law 0.1/0.2) + the 11 mechanics laws,
                               # each with its evidence and its operational test
    failure-modes.md           # the 7-mode failure catalog with named cases + early warnings
  platform/
    instagram.md               # ranking signals w/ evidence tiers, penalty list, specs,
                               # funnel mechanics, engagement-bait line, AI-labeling rules
    youtube.md                 # Shorts vs long-form structural differences, specs, lane rules
    publishing-ops.md          # HOW we publish/schedule/export analytics (from R3 research)
  audience/
    personas.md                # who we serve: segments, what they want, what they distrust
    positioning.md             # "machine craft, human taste": backlash map, disclosure rules,
                               # what we never do (IP mashups, undisclosed gen, bought reach)
  brand/
    tangent-voice.md           # verbal+visual identity across tangentideas.ai / tangent.gallery
    content-architecture.md    # HERO/WORKHORSE/FILLER tiers + concept selector formula
  production/
    adobe-playbook.md          # driving Lightroom web via Claude-in-Chrome: session protocol,
                               # capture-worthy moments, edit vocabulary (from R2 research)
    assembly-playbook.md       # capture → cut → captions → export path with exact settings
    genvideo-playbook.md       # Veo/Flow usage: what it's for, prompt patterns, disclosure
  benchmarks.md                # metric definitions, healthy bands, OUR medians (analyst-owned)
  pattern-library.md           # distilled corpus: verbatim hooks, templates, archetype cards,
                               # funnel evidence, failure catalog (from R1 distillation)
```

---

## 5. The content pipeline (`ops/pipeline/`)

One folder per content item: `NNN-slug/` (zero-padded sequence). State machine, enforced by
`tools/pipeline.py`:

```
IDEA → BRIEFED → SCRIPTED → G1 ⟶ PRODUCING → CUT → G2 ⟶ READY → SHIP ⟶ PUBLISHED
                                                                → POSTMORTEM → CLOSED
   (any stage) → KILLED (reason logged, salvage note)
```

- **G1 — script gate**: critic reviews `script.md` BEFORE production spends effort.
  Cheap kills happen here.
- **G2 — cut gate**: critic reviews the actual cut (or its full description + stills when
  video can't be attached). Hygiene checks (`tools/hygiene_check.py`) must PASS.
- **SHIP** : Sparsh's approval, recorded in `item.yaml` (`approved_by_sparsh: date`).

Item folder contents (templates in `templates/`):

```
NNN-slug/
  item.yaml          # id, title, pillar (HERO/WORKHORSE/FILLER), platform(s), stage,
                     # created, due, next_action, next_action_owner, plane_issue,
                     # approved_by_sparsh, published_url(s)
  brief.md           # concept, selector-formula scores, target emotion, payoff, references
  script.md          # hook variants (≥3), beat sheet w/ timestamps, on-screen text, VO,
                     # audio plan, loop map (every loop opened → where it closes)
  assets.md          # manifest: every asset, provider tag, status, path/source
  critiques/         # G1-script.md, G2-cut.md (+ rounds: G2-cut-r2.md ...)
  publish.md         # final caption, cover, audio credit, hashtags, DM keyword+deliverable,
                     # posting time, platform variants, disclosure line
  postmortem.md      # 9-section postmortem (analyst, T+72h minimum)
```

---

## 6. Skills — the workflows (`.claude/skills/<name>/SKILL.md`)

Each SKILL.md: frontmatter (`name`, `description`), then: purpose, preconditions, exact
step-by-step protocol (agents to invoke and with what inputs, tools to run with exact CLI),
gates, outputs, and failure handling. Nine skills:

| Skill | Invokes | Purpose |
|---|---|---|
| `ideate` | trend-scout → creative-director | Note/opportunity → 5–10 scored concepts → top briefs written to pipeline as BRIEFED items. Applies the concept selector formula; kills weak concepts before they cost anything. |
| `script` | story-lead | BRIEFED → SCRIPTED: script.md + assets.md (provider-tagged, [SPARSH] minimized). |
| `critique` | critic | Runs G1 (script) or G2 (cut) with the 8-lens scorecard. Writes `critiques/`. Enforces gate math; verdict SHIP/FIX/KILL with ranked fixes and "what would make this a 10". |
| `produce` | producer | SCRIPTED+G1 → CUT: executes/queues [AGENT] and [GEN] assets, Lightroom capture protocol, assembly per playbook, runs hygiene_check, updates assets.md. |
| `publish` | producer + planner | READY+SHIP → PUBLISHED: publish.md finalized per platform playbooks, checklist run, schedule set, `pipeline.py publish` records URL + file hash. |
| `postmortem` | analyst | PUBLISHED → CLOSED: T+72h stats via verify_stats + metrics tools, 9-section postmortem, views×LR decomposition, knowledge-bank updates ([OWN-DATA]), benchmarks refresh. |
| `plan` | planner | Roadmap CRUD: builds/updates 3–4-week ROADMAP.md, syncs Plane work items, standup report (overdue, blocked-on-Sparsh, next actions), replans on delays/news. Includes first-run bootstrap: create Plane project "Tangent Social" (identifier TANSOC) with states/labels. |
| `trend-sweep` | trend-scout | Daily/weekly sweep → trends-log.md entries with actionability rating; hot items (0–4-day windows) trigger a planner ping to insert a news-response item. |
| `weekly-review` | analyst → planner → creative-director | The Friday ritual: growth accounting vs medians, bet-gate checks against BETS.md, pillar performance, pivot-on-signal decisions, next week's plan. Produces `ops/calendar/review-YYYY-WW.md`. |

Skill-authoring rules: concrete over abstract (exact file paths, exact tool commands); every
skill ends by updating `item.yaml`/state via `pipeline.py` (no silent state); every skill
says what to do when a gate FAILS, not just when it passes.

---

## 7. Tools (`tools/`)

Python 3.13, stdlib + minimal deps (`requirements.txt`; yt-dlp optional, ffmpeg external —
every tool checks its deps and prints an actionable install hint). All tools: `--help`,
non-zero exit on failure, machine-parseable output (`--json` flag where useful). Windows
paths handled. Smoke-testable without network except verify_stats.

1. **`pipeline.py`** — state machine CRUD.
   - `new "<title>" --pillar HERO|WORKHORSE|FILLER --platform ig,yt` → creates NNN-slug/ from
     templates, stage=IDEA
   - `stage NNN <STAGE>` → validates legal transition (gate stages require critique file /
     approval field present), updates item.yaml
   - `board` → status table of all open items (stage, next_action, owner, due, overdue flag)
   - `blocked` → only BLOCKED-ON-SPARSH + overdue items
   - `kill NNN --reason "..."`
   - `publish NNN --url <url>` → records URL, hashes the video file into
     `ops/pipeline/.published_hashes.json` (repost-penalty guard)
   - `validate` → schema-checks all item.yaml files
2. **`metrics.py`** — the measurement constitution, as code.
   - `likerate --views N --likes N` → LR + verdict vs the 1–10% organic sanity band
   - `decompose --views N --likes N --median-views N --median-lr X` → quadrant verdict:
     hook/discovery failure vs craft failure vs healthy vs boosted-suspect
   - `efficiency --csv posts.csv --followers N` → median views/follower efficiency + trend
   - `funnel --comments N --likes N` → comment:like ratio vs the ≥0.5 working-funnel bar
   - `report --csv posts.csv --followers N --json` → all of the above for every row +
     account-level summary (medians, spread, efficiency, early-warning triad check)
   - CSV schema documented in `tools/README.md` (date,platform,url,pillar,views,likes,
     comments,shares,saves,funnel,followers_at_post)
3. **`verify_stats.py`** — the second-source rule, as code: given a public post URL, pulls
   independent metadata via yt-dlp and diffs against claimed numbers; flags >10% divergence.
   (Corpus finding: browser-scraped likes were wrong 15.5% of the time — no number enters a
   postmortem single-sourced.)
4. **`hygiene_check.py`** — pre-publish hygiene via ffprobe: ≥1080×1920, 9:16, duration in
   band (reel: 15–90s warn outside 20–45), audio stream present, H.264/AAC, black-border
   detection (cropdetect), file-hash not in published ledger. Output: PASS/FAIL per check +
   overall; FAIL blocks G2.
5. **`calendar.py`** — renders ROADMAP.md's item table + pipeline state into a week-grid
   markdown view; flags cadence-band violations (floor/ceiling from STRATEGY.md) and
   HERO-drought (no HERO in >7 days).

---

## 8. The critique system (the make-or-break layer)

Scorecard (`templates/critique-scorecard.md`), 8 lenses, each scored 1–10 **with cited
evidence** (knowledge file + law for every deduction — no vibes):

1. **HOOK** — first-frame test (describe frame 0; would a cold scroller stop?), payoff
   named/shown ≤1s (YT) / ≤3s (IG), curiosity gap present, zero preamble. Weight ×2.
2. **STRUCTURE & RETENTION** — loop map complete (every opened loop closes), granular
   state-changes ≤15s apart, escalation order, ending lands, length earns itself.
3. **EMOTION & INTENSITY** — target emotion named; is it high-arousal (awe)? STEPPS
   intensity not presence; the payoff-intensity bar.
4. **CLARITY & ONE-IDEA** — sound-off test (message legible from visuals+text alone),
   one-sentence takeaway, jargon scan vs the 35+ tone standard.
5. **CRAFT & AESTHETICS** — visual grade to gallery-brand bar, audio mix, caption
   typography/safe zones, cut cleanliness. (We sell taste; craft slop is brand death.)
6. **AUDIENCE FIT & SHAREABILITY** — "send this to ___" addressee test, social currency,
   save value, persona match.
7. **DIFFERENTIATION** — against pattern-library: too-similar (which creator does this
   ape?) vs too-niche (who outside the bubble cares?); does it use OUR unfair advantages?
8. **HYGIENE & COMPLIANCE** — binary: platform penalty list, engagement-bait line,
   disclosure rules, brand non-negotiables. Any FAIL ⇒ verdict cannot be SHIP.

Gate math: lenses 1–7 are numeric; lens 8 is binary and never enters the mean. Weighted
mean = (HOOK×2 + lenses 2–7) ÷ 8. SHIP eligibility: weighted mean ≥ 7.5 AND HOOK ≥ 8 AND
lens-8 all-PASS. Verdicts: **SHIP** / **FIX** (ranked, concrete fixes; max 2 fix rounds before
mandatory KILL-or-escalate-to-Sparsh) / **KILL** (reason + salvage note). The critic must
also write "what would make this a 10" — the standard is teaching, not just gatekeeping.

Calibration loop: every postmortem compares the critic's pre-publish scores against actual
performance; systematic misses become critic-prompt updates (analyst proposes, Showrunner
approves).

---

## 9. Planner integration (Plane)

- Plane MCP is connected in this environment. First `/plan` run bootstraps project
  **"Tangent Social"** (identifier `TANSOC`) — states: Backlog/Planned/In Progress/
  Blocked-on-Sparsh/In Review/Done/Killed; labels: `hero`, `workhorse`, `filler`,
  `series`, `news`, `ops`, `sparsh-input`.
- Every pipeline item gets a Plane work item at BRIEFED (`plane_issue` recorded in
  item.yaml). Planner keeps Plane and `pipeline.py board` consistent — Plane is the
  roadmap/accountability view; the repo is the source of truth for content artifacts.
- Weekly cycle: Monday `/plan` (roadmap refresh), daily `/plan standup` (cheap: board +
  overdue + blockers note), Friday `/weekly-review`.
- Fallback: if Plane MCP is unavailable in a session, planner operates on ROADMAP.md alone
  and queues a sync note — never blocks content work on tooling.

## 10. Cadence & capacity (bands, not prescriptions)

STRATEGY.md sets bands (sustainable solo+agents floor/ceiling); the planner picks each
week's actual cadence inside the bands based on: pipeline health, Sparsh availability
(blocked-item count), news windows, and bet-validation needs. Hard rule from the corpus:
filler exists to protect hero quality, never to replace it; volume raises the floor, not
the ceiling.

## 11. Build-phase source material

Builders drew from: `research/` + `synthesis/` (primary corpus), the corpus distillation
(committed as `knowledge/pattern-library.md`), and two July-2026 research briefs (committed
as `research/briefs/production_stack_2026-07.md` and `research/briefs/platform_ops_2026-07.md`,
cited in knowledge files as `[stack-brief]`/`[ops-brief]`). Where a brief contradicts the
corpus, the corpus wins for psychology/mechanics; the brief wins for current platform
specs/tooling facts (it's fresher). Uncertainty is kept visible with tier tags — never
silently resolved.

---

## 12. The two-team architecture: Studio + Brand Office

The system comprises two named teams sharing one pipeline, one Showrunner, one repo:

- **The Studio** (§3's seven agents) — makes the content: ideation → script → production →
  craft/virality gates → publish → postmortem. Owns creative execution.
- **The Brand Office** — a lean three-expert consulting bench. It does NOT make content.
  It (a) consults on demand wherever the Studio needs domain expertise, (b) is pulled in
  automatically by the Brand-Touch Score decision node (§12.3), and (c) critically judges
  every final output at the G3 brand gate (§12.4) in one context only: **does this compound
  the Tangent brand?** Different altitude from the critic: the critic judges the video
  (craft, hook, virality); the Brand Office judges the brand trajectory the video creates.

### 12.1 Brand Office roster (`.claude/agents/`)

| Agent | Model | Lens | One-line contract |
|---|---|---|---|
| `brand-director` | inherit | Brand equity | Chairs the Brand Office. Positioning integrity, distinctive-asset discipline, brand architecture across surfaces, portfolio coherence. Synthesizes G3 verdicts. |
| `growth-lead` | sonnet | Growth contribution | Marketing-effectiveness evidence: mental/physical availability, reach economics, funnel & monetization sequencing, platform-portfolio risk. |
| `audience-advocate` | sonnet | Audience trust | Represents the audience: trust, sentiment, community health, backlash exposure, parasocial-relationship stewardship, disclosure adequacy. |

Brand Office agents are ADVISORY everywhere except G3. A Studio decision made against a consult
memo's advice is legal but must be logged (in the item folder) with the reason — creative
authority stays with the Studio; brand authority peaks at G3.

### 12.2 Brand Office knowledge bank (`knowledge/marketing/` + `knowledge/SOURCES.md`)

Same provenance constitution as §4, plus the marketing-science domain:
```
knowledge/marketing/
  brand-science.md        # mental & physical availability, distinctive assets vs
                          # differentiation, 95-5, double jeopardy, CBBE/equity models —
                          # each: claim, evidence base, applicability-to-a-creator-brand note
  distinctive-assets.md   # TANGENT'S OWN asset register (name/wordmark, gallery-white +
                          # Fraunces aesthetic, "machine craft, human taste", the critic-as-
                          # character, before/after snap) + build/measure/protect rules
  positioning-doctrine.md # category entry points, competitive frame, one-line-description
                          # test, brand architecture (gallery ↔ tangentideas.ai ↔ YT ↔ email)
  growth-playbook.md      # creator-brand growth economics: owned-audience value, funnel
                          # math, monetization-readiness criteria, platform-risk spread
  community-trust.md      # trust/community mechanics, backlash & crisis protocol (extends
                          # audience/positioning.md), consistency-of-voice stewardship
  brand-health-metrics.md # Brand Office's measurable proxies + bands: follower quality,
                          # profile-visit & follow-through rates, returning-viewer %,
                          # branded-search/mention proxies, comment-sentiment share, DM→email
                          # conversion; scorecard definitions used at G3 and weekly review
knowledge/SOURCES.md      # SYSTEM-WIDE trusted-source whitelist + zero-hallucination rule
                          # (§12.5); applies to BOTH teams
```

### 12.3 The consult decision node — Brand-Touch Score (BTS)

Computed by the Showrunner at two moments: when a brief is written (end of `/ideate`) and at
any format/strategy decision. Sum the flags:

| Flag | +Score |
|---|---|
| First-of-kind content: new format/series/pillar audition | +3 |
| Public identity surface change (bio, name, tagline, cover-grid style, channel art) | +3 |
| Sponsorship / collab / any commercial element | +3 |
| Backlash-adjacent subject or disclosure edge case (per positioning.md map) | +2 |
| Funnel/monetization mechanic change (new deliverable class, new CTA type) | +2 |
| New platform surface or cross-posting change | +1 |
| Stretches an owned format or the tone standard | +1 |

**BTS ≥ 3 → mandatory `/consult` before scripting** (recorded in the brief). BTS 1–2 →
Showrunner judgment, decision noted in the brief. BTS 0 → no consult; the Brand Office still
sees the item at G3. The BTS and its flags are written into `brief.md` — silent skips are
audit failures.

### 12.4 The G3 brand gate (READY → PUBLISHED, enforced by `tools/pipeline.py`)

After G2 (craft) and before Sparsh's SHIP approval, every item gets `/brand-review`:
1. The three Brand Office agents score their lenses independently, 1–10, evidence-cited
   (knowledge/marketing/ + the item's consult history + `strategy/BETS.md`):
   **Brand-Equity Impact** (strategist) · **Growth Contribution** (scientist) ·
   **Audience Trust** (advocate).
2. `brand-director` synthesizes `critiques/G3-brand.md` (template
   `templates/brand-scorecard.md`) with the verdict:
   - **ADVANCE** — all lenses ≥ 7 AND mean ≥ 7.5, no hard-HOLD trigger.
   - **ADVANCE-WITH-NOTES** — no lens ≤ 4, mean ≥ 6, no hard-HOLD trigger; notes are
     binding considerations for FUTURE items (logged), not blockers for this one.
   - **HOLD** — any lens ≤ 4, or mean < 6, or a hard-HOLD trigger: never-list violation,
     unmitigated backlash-flashpoint adjacency, positioning drift (the one-line-description
     test fails), or distinctive-asset violation. HOLD escalates to Sparsh; only he can
     override (logged in a `-r2` review recording the override + reason).
3. `pipeline.py` enforces: READY → PUBLISHED requires BOTH `approved_by_sparsh` AND a
   `critiques/G3-brand*.md` whose verdict line is `VERDICT: ADVANCE` or
   `VERDICT: ADVANCE-WITH-NOTES` (exact line, same grep contract as G1/G2).
4. G3 does not re-litigate G2: craft/hook/virality scores are the critic's; the Brand Office
   cites brand-level evidence only. One G3 per item unless the cut materially changes.

### 12.5 The zero-hallucination provenance rule (both teams, constitutional)

Every factual claim in any brief, memo, critique, verdict, or knowledge write must carry
one of: (a) a knowledge-bank citation (file + section), (b) a live citation to a
`knowledge/SOURCES.md`-whitelisted source (URL + date fetched), or (c) an explicit
`[OWN-DATA]` reference to our verified metrics. A claim with none of these is written as
**UNKNOWN** with a logged research gap — never estimated, never "probably." Numbers are
never invented, interpolated, or recalled from memory without a source. `knowledge/SOURCES.md`
defines the whitelist tiers and the disqualified-source list; the weekly review audits a
sample of the week's citations.

### 12.6 Brand Office rhythms

- **Per item:** BTS at brief; consult if triggered; G3 at READY.
- **Weekly:** `brand-director` contributes a brand-health section to `/weekly-review`
  (drift check, distinctive-asset consistency, portfolio balance, ADVANCE-WITH-NOTES themes).
- **Quarterly:** full brand audit (RUNBOOK §9): asset register refresh, positioning-doctrine
  review against accumulated [OWN-DATA], SOURCES.md whitelist refresh.
