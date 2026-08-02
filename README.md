# tangent-social-media

The autonomous social media & brand operation for **Tangent** — instagram.com/tangentideas.ai,
tangent.gallery, and YouTube. Three Claude Code agent offices under one **Showrunner** (the main
session, per `CLAUDE.md`), with Sparsh as supervisor and creative gate of last resort:

- **The Studio** (4 agents) — creates across every vertical (reels, long-form, podcast,
  music, apps, images) via per-vertical craft packs, gated by the brutal critic at G1/G2.
- **The Brand Office** (4 agents) — manages, promotes, and monetizes the brand: brand kit
  + positioning, repurposing/distribution/funnel ops, audience trust, and the revenue
  office (`strategy/REVENUE.md`) — judging every final output at the enforced G3 gate.
- **Operations** (3 agents) — the shared spine: roadmaps + Plane, verified measurement,
  trend surveillance.

V2 ("The Label", approved 2026-08-02): Sparsh is the artist; the offices are the label
around him — see `SYSTEM_DESIGN_V2_PROPOSAL.md` and the four evidence briefs in
`research/briefs/revamp-2026-08/`.

## Quick start

```
pip install -r tools/requirements.txt      # pyyaml (+ yt-dlp for stat verification)
winget install Gyan.FFmpeg                 # for hygiene_check + assembly
python tools/tests/smoke.py                # verify the toolchain: expect ALL PASS
```

Then open a Claude Code session here (run it on your top model — the Showrunner is your
creative partner) and just start talking: *"reel idea — the critic rejects my favorite edit
three times."* **The session is the interface**: you and the Showrunner walk each stage
together — concept slate, hook variants, critique verdicts, cut review — iterating as you
go, while the agent team does the work underneath. Say "run ahead" for autonomous mode
(high-confidence defaults, consolidated asks). Every decision is written to the item
folders as it's made, so the session can run for days — or die and restart — losing nothing.

## How it works

```
/ideate (Brand-Touch Score → /consult if triggered) → brief → /script → G1 critic gate
   → /produce → G2 critic gate → /brand-review (G3 brand gate) → Sparsh SHIP approval
   → /publish → /postmortem → knowledge bank learns
```

- **`CLAUDE.md`** — the constitution: non-negotiables, roster, session protocol.
- **`SYSTEM_DESIGN.md`** — full architecture.
- **`strategy/`** — principles + live bets with validation gates (no prescriptions).
- **`knowledge/`** — the evidence-tagged knowledge bank (craft, virality laws, platform
  playbooks, production playbooks, brand, audience). Start at `knowledge/INDEX.md`.
- **`ops/`** — `RUNBOOK.md` (protocols), `ROLES.md` (RACI), `pipeline/` (content in
  flight), `calendar/` (roadmap, trends log).
- **`tools/`** — deterministic scripts: pipeline state machine, metrics math,
  second-source stat verification, export hygiene checks, calendar rendering.
- **`.claude/agents/`** — 10 specialists. Studio: creative-director, trend-scout,
  story-lead, producer, critic, analyst, planner. Brand Office: brand-director,
  growth-lead, audience-advocate.
- **`.claude/skills/`** — 12 workflows: the lifecycle skills diagrammed above (incl.
  `/consult` and `/brand-review`) plus `/plan`, `/trend-sweep`, `/weekly-review`,
  `/revenue-review` (monthly).
- **`research/` + `synthesis/`** — the frozen evidence corpus (18 creator dossiers,
  virality science rubric, whitespace analysis). Read-only; the knowledge bank cites it.

## Operating rituals

Monday `/plan` · near-daily `/trend-sweep` · Friday `/weekly-review` (the only place bet
statuses and format kill/keep decisions change).
