---
name: repurpose
description: Use when a HERO or WORKHORSE pipeline item reaches READY or PUBLISHED — growth-lead plans a platform-native derivative fan-out, Showrunner creates each approved derivative as a linked child item via `pipeline.py derive`, story-lead writes its derivative-spec.md, then each child runs the normal /produce → G2 → G3 → publish path.
---

## Purpose
Turn one hero/workhorse asset into N platform-native derivatives without ever blind-cross-posting
the source file — each derivative is planned for a specific platform's grammar, gets its own
linked child item, and clears the same G2/G3/SHIP bar as any pipeline item
(SYSTEM_DESIGN_V2_PROPOSAL.md §4 item 2).

## Preconditions
- A HERO or WORKHORSE item is at stage READY or PUBLISHED (verify: `python tools/pipeline.py
  board`). FILLER items are not fan-out candidates — they don't carry the production cost to
  justify one.
- The parent item is not KILLED (`pipeline.py derive` enforces this; don't attempt it on a dead
  item).

## Protocol
1. Confirm the trigger: `python tools/pipeline.py board`, locate the parent item id NNN, confirm
   stage READY or PUBLISHED and pillar HERO/WORKHORSE.
2. Invoke `growth-lead` (Task, subagent_type `growth-lead`) with: the parent's `script.md` and
   `publish.md` (if published), `knowledge/virality/laws.md` law 10 ("platform-native beats
   cross-posting; the lane must fit the genre" — NEVER a blind cross-post), `knowledge/platform/
   instagram.md`, `knowledge/platform/youtube.md`, `strategy/STRATEGY.md` §7 (cadence bands — the
   roadmap-capacity ceiling), and `strategy/BETS.md`.
3. growth-lead writes the fan-out plan per its own contract (`.claude/agents/growth-lead.md`):
   named derivatives, each with a stated platform, the audience it reaches that the hero didn't,
   and a mechanism (category-entry-point or funnel). Candidate shapes per the parent's genre:
   reel → Shorts native re-cut (re-grammar, not a re-upload), stills carousel (IG grid),
   newsletter section (email list). A derivative with no stated mechanism does not go in the plan.
4. planner is consulted on capacity: the total derivatives this fan-out proposes must fit inside
   `strategy/STRATEGY.md` §7's cadence band for the weeks they'd land in — the fan-out is capped
   by roadmap capacity, not by how many ideas growth-lead can generate.
5. Present the plan to Sparsh (INTERACTIVE) or apply high-confidence defaults (AUTONOMOUS) — see
   Interaction checkpoints below.
6. For each approved derivative, Showrunner runs:
   `python tools/pipeline.py derive NNN --title "<derivative title>" --platform <p> [--vertical V] [--pillar P]`
   — pillar/vertical default to the parent's if omitted; override `--vertical` when the
   derivative's container differs (e.g. a newsletter section is vertical `newsletter`, not
   `reels`).
7. Invoke `story-lead` (Task, subagent_type `story-lead`) per new child item to write
   `NNN-slug/derivative-spec.md` (exact filename, item-folder root): source beats used from the
   parent's `script.md`, the platform re-grammar applied (cite the specific law/platform-doc
   section), and the native changes made (recut points, new on-screen text, format-native
   pacing). This is what unlocks SCRIPTED→PRODUCING without a fresh G1 (`ops/pipeline/README.md`
   "Derivative gate policy") — the parent's own G1 already validated the underlying material.
8. Each child then runs the normal path: `/produce` → G2 `/critique` → G3 `/brand-review` → SHIP
   → `/publish`, exactly like any pipeline item. Nothing about G2/G3/SHIP is relaxed for a
   derivative.

## Gates
- Max derivatives per parent is bounded by `strategy/STRATEGY.md` §7 cadence-band capacity for
  the landing weeks (step 4) — planner is consulted before any derivative is created, not after.
- A derivative that is just a re-upload of the parent's exact exported file (no re-grammar, no
  native changes) must be caught before it's created: `derivative-spec.md`'s native-changes
  section having real content to write IS the check — if there's nothing true to put there, it
  isn't a derivative, it's a repost, and it doesn't get created. `hygiene_check.py`'s repost
  guard is a second, independent backstop — identical file hashes are blocked at export/publish
  time regardless of whether this check was skipped.
- `pipeline.py validate` enforces `parent_id` referential integrity (must reference an existing,
  non-self item) on every run.

## Outputs
- growth-lead's fan-out plan, written into the parent's `publish.md` fan-out section (or a
  `consults/`-style memo for a parent that predates this skill).
- One `ops/pipeline/NNN-slug/` child item per approved derivative, `parent_id` set, stage IDEA.
- `NNN-slug/derivative-spec.md` per child (story-lead), unlocking SCRIPTED→PRODUCING.
- `pipeline.py board` shows every child annotated `^PARENT_NNN` on its slug.

## On failure
- growth-lead can't state a mechanism for a candidate derivative: drop it from the plan — don't
  pad the fan-out with undirected reach (growth-lead's own failure-modes discipline).
- Roadmap has no capacity this cycle: queue the plan, don't create the children yet —
  `pipeline.py derive` carries no due-date urgency of its own, so a delayed fan-out costs nothing
  but calendar time.
- `pipeline.py derive` errors (parent not found / parent KILLED / bad platform, pillar, or
  vertical): fix the parent id or the flag; never hand-edit `item.yaml` to fake a parent link.
- story-lead can't write a real native-changes section (the "derivative" would in fact just be
  the same cut relabeled): kill the child item (`pipeline.py kill NNN --reason "..."`) rather
  than forcing a spec that doesn't say anything true.

## Interaction checkpoints (INTERACTIVE mode — RUNBOOK §1)
- **Checkpoint 1 — fan-out plan review:** present growth-lead's named derivatives with mechanism
  and platform for each, plus planner's roadmap-capacity read. Sparsh trims/adds/redirects here —
  the cheap point to say "skip the carousel, do the newsletter section instead."
- **Checkpoint 2 — per-child derivative-spec.md:** before each child leaves this skill for
  `/produce`, a quick look at its derivative-spec.md (source beats, re-grammar, native changes) —
  same spirit as `/script`'s pre-G1 read-through checkpoint.
- From there each child is a normal item: its own `/produce` → G2 → G3 → SHIP checkpoints apply
  unchanged — this skill's interactivity ends once children exist and are specced.
- AUTONOMOUS: growth-lead's plan applies at high confidence, capped by roadmap capacity; children
  are created and specced without a pause; normal per-child interactivity resumes at each child's
  own gates (G2/G3/SHIP are never automated in either mode).
