Tangent Social — Pipeline Folder Contract

One folder per content item under `ops/pipeline/`. This is the source of truth for content
artifacts (Plane mirrors it for humans, `ops/RUNBOOK.md` §6). Lifecycle narrative:
`ops/RUNBOOK.md` §2. Agent responsibilities: `ops/ROLES.md`. Schema and transitions below
mirror `tools/pipeline.py`/`tools/_common.py` exactly — if this file and the tool ever disagree,
the tool is ground truth and this file is wrong.

## The rule

**All state changes go through `tools/pipeline.py`.** Nobody hand-edits `stage:` in item.yaml.
`pipeline.py stage NNN <STAGE>` only allows moving to the immediate next stage in the fixed
sequence below, and blocks the two gated transitions until the matching critique file carries a
`VERDICT: SHIP` line. `pipeline.py validate` schema-checks every item.yaml.

## State machine

`G1`/`G2`/`G3`/`SHIP` are **gate checks on a transition, not stage values** — item.yaml's
`stage` field only ever holds one of the 9 sequence values below, or `KILLED`.

```
IDEA -/ideate-> BRIEFED -/script-> SCRIPTED -/produce-> PRODUCING -> CUT -> READY -/publish-> PUBLISHED -/postmortem-> POSTMORTEM -> CLOSED
                                       ^                                     ^          ^
                                  [G1 gate]                             [G2 gate]  [G3 + SHIP]
                        needs critiques/G1-script.md              needs a critiques/G2-cut*.md
                        with a "VERDICT: SHIP" line                file with "VERDICT: SHIP"
                        before SCRIPTED->PRODUCING is legal        before CUT->READY is legal

READY -> PUBLISHED requires BOTH (checked in this order):
  [G3 brand gate]  a critiques/G3-brand*.md with a "VERDICT: ADVANCE" or
                   "VERDICT: ADVANCE-WITH-NOTES" line (written by /brand-review; a HOLD only
                   clears via Sparsh's override recorded as G3-brand-r2.md — SYSTEM_DESIGN §12.4)
  [SHIP gate]      approved_by_sparsh set, via
                   `pipeline.py stage NNN READY --approved-by-sparsh` (same-stage field update)
Both are enforced by `pipeline.py publish --url <url> [--video <path>]`, which also records the
URL/date into `published` and (with --video) SHA256-hashes the file into
`.published_hashes.json`, erroring on a repeat hash (repost guard).

Any stage above -> KILLED at any time via `pipeline.py kill NNN --reason "..."` (sets
`kill_reason`; a bare `stage NNN KILLED` is rejected — kill always records why). FIX verdicts on
either gate leave the item at SCRIPTED or CUT respectively; 2 failed FIX rounds force
KILL-or-Sparsh-escalation (`ops/RUNBOOK.md` §5) — the tool doesn't count rounds, that discipline
is a process rule, tracked by the `critiques/G2-cut-r2.md`-style filenames.
```

## Derivative gate policy (Repurposing Engine — SYSTEM_DESIGN_V2_PROPOSAL.md §4 item 2)

A **derivative** is a child item created by `pipeline.py derive PARENT_NNN --title "..."
--platform ig,yt [--vertical V] [--pillar P]` (`/repurpose` skill): it gets its own
`NNN-slug/` folder like any item, but `item.yaml`'s `parent_id` points at the hero/workhorse
item it fans out from. `pillar`/`vertical` default to the parent's when not given explicitly.

**Derivatives SKIP G1, but face FULL G2 and FULL G3 + SHIP like any item.** The rationale: the
parent's own brief/script already passed G1 — re-litigating hook/structure/craft on material
that already cleared that bar is redundant. What a derivative must show instead is that it's a
genuine platform-native re-grammar of the parent, not a re-upload: a `derivative-spec.md` file
(exact filename, item-folder root — a sibling of `script.md`, not a file under `critiques/`)
containing:
- **Source beats used** — which beats/assets from the parent's `script.md` this derivative pulls
  from.
- **Platform re-grammar applied** — the specific law/platform-doc section driving the change
  (`knowledge/virality/laws.md` law 10, "platform-native beats cross-posting"; the matching
  `knowledge/platform/instagram.md` / `youtube.md` section).
- **Native changes** — what's actually different from the parent: recut points, new on-screen
  text, format-native pacing/length. If there's nothing true to write here, it isn't a
  derivative — it's a repost, and it should not exist as a pipeline item.

`pipeline.py`'s SCRIPTED→PRODUCING gate check (`_gate_check`) accepts **EITHER** of these for an
item with `parent_id` set:
1. `critiques/G1-script.md` with a `VERDICT: SHIP` line (the full G1 path — still legal if a
   derivative's script genuinely needs fresh scrutiny), **OR**
2. `derivative-spec.md` present in the item folder (no verdict line required — its mere
   presence, written by story-lead per `/repurpose`, is the unlock).

A non-derivative item (`parent_id` is `null`) always needs the full G1 SHIP verdict; the
alternate path never applies to it. From CUT onward (G2, G3, SHIP, publish) a derivative is
indistinguishable from any other item — same hygiene checks, same critic scorecard, same brand
gate, same repost-guard hash check on export (a derivative that's actually just the parent's
exported file re-saved gets caught there even if `derivative-spec.md` was written carelessly).

`pipeline.py board` annotates every child with its parent id as a `^NNN` suffix on the slug
column (e.g. `hero-shorts-cut ^003`), so the fan-out relationship is visible without opening
`item.yaml`. `pipeline.py validate` checks `parent_id` referential integrity on every run: it
must be `null` or reference an existing item, and never reference itself.

## Folder layout

```
NNN-slug/
  item.yaml     # state + metadata — field meanings below
  brief.md      # concept, selector scores, target emotion, payoff, references          [BRIEFED]
  script.md     # hook variants (>=3), beat sheet, on-screen text, VO, audio, loop map   [SCRIPTED]
  derivative-spec.md # DERIVATIVE ITEMS ONLY (parent_id set): source beats used,
                # platform re-grammar applied, native changes — alternate G1 unlock,
                # see "Derivative gate policy" below                                    [SCRIPTED]
  assets.md     # manifest: asset, provider tag ([AGENT]/[GEN]/[SPARSH]), status, path   [SCRIPTED]
  critiques/    # G1-script.md, G2-cut.md (+ fix rounds: -r2, ...), G3-brand.md          [gates]
  consults/     # Brand Office consult memos for this item (BTS-triggered or ad hoc)   [any]
  publish.md    # caption, cover, audio credit, hashtags, DM keyword+deliverable,
                # posting time, platform variants, disclosure line                      [READY]
  postmortem.md # 9-section postmortem (analyst, T+72h minimum)                         [CLOSED]
```
Bracketed tag = earliest stage/event the file appears at. Templates exist for brief.md,
script.md, assets.md, publish.md, postmortem.md (plus the critique scorecard the critiques/
files use) under `templates/`; item.yaml is built programmatically by `pipeline.py new`,
which also seeds stub `brief.md`/`script.md` from `templates/` automatically.

## Naming

`NNN-slug/` — `NNN` zero-padded 3-digit sequence (001…999), monotonic across the whole
pipeline, never reused (even for KILLED items). `slug` is short kebab-case, auto-derived by
`pipeline.py new` from the title (lowercased, non-alphanumeric runs collapsed to single
hyphens). `pipeline.py new` assigns `NNN` automatically — don't hand-pick one.

## item.yaml field meanings

| Field | Meaning |
|---|---|
| `id` | `NNN` (int), matching the folder name. |
| `slug` | Kebab-case slug, matching the folder name. |
| `title` | Human-readable title. |
| `pillar` | Exactly one of `HERO`\|`WORKHORSE`\|`FILLER` (STRATEGY §4) — drives the Plane label. |
| `platforms` | List of targets from `ig`\|`yt`\|`yt-long` (e.g. `[ig]`, `[ig, yt]`). |
| `vertical` | one of: reels, longform, podcast, music, app, image, newsletter — selects the craft pack the critic/producer load (SYSTEM_DESIGN V2 §4.3); default `reels` |
| `parent_id` | `int` \| `null` — set by `pipeline.py derive` when this item is a repurposed derivative of another item; `null` for everything created by `pipeline.py new`. Drives the derivative gate policy below and the `^NNN` annotation on `board`. |
| `stage` | One of the 9 sequence values above, or `KILLED`. |
| `created` | Date item entered IDEA. |
| `due` | Due date for `next_action`, or null; drives the OVERDUE flag on `board`/`blocked`. |
| `next_action` | One-line description of what's next. |
| `next_action_owner` | One of: `creative-director`\|`trend-scout`\|`story-lead`\|`producer`\|`critic`\|`analyst`\|`planner`\|`showrunner`\|`sparsh`. `board`/`blocked` compute the **BLOCKED-ON-SPARSH** flag whenever this is `sparsh` — it is a derived label, not a stored value. |
| `plane_issue` | Plane work-item id, set at BRIEFED (`ops/RUNBOOK.md` §6), or null. |
| `approved_by_sparsh` | Null until SHIP approval; then the date. Must be set before `READY`→`PUBLISHED`. |
| `published` | Dict of `{url: date}` — one entry per platform if cross-posted; empty `{}` until published. |
| `kill_reason` | Null unless `stage: KILLED`; the reason `pipeline.py kill` recorded. Fold the salvage note (what's reusable) into this same string — there is no separate schema field for it. |

`validate` also requires: `stage: KILLED` items have a non-empty `kill_reason`; `PUBLISHED`/
`POSTMORTEM`/`CLOSED` items have `approved_by_sparsh` set and a non-empty `published` dict;
`parent_id`, if not `null`, is an int referencing an existing item and never the item's own id.
