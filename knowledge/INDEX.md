# Knowledge Bank — Index

The map, not the content. Agents' "load lists" (in `.claude/agents/`) name the specific files
each role must read before acting — this index is for orienting a new session or a cross-cutting
question. Per `SYSTEM_DESIGN.md` §4: provenance-or-it-doesn't-exist, living-with-write-control,
this file is the map.

## Files

| File | What's in it | Read before |
|---|---|---|
| `craft/reels/hooks.md` | Hook classes ranked by corpus win-rate, verbatim examples, the 1s/3s gate, first-frame test, anti-patterns | Scripting any hook; G1 critique lens 1 |
| `craft/reels/structure-and-retention.md` | Loop discipline, escalating listicles, pacing, length bands, demo-in-motion beat rules | Scripting the body of any piece; G1 lens 2 |
| `craft/reels/scripting-voice.md` | One-idea rule, sound-off legibility, caption/text rules, jargon bans, 35+ tone standard | Scripting VO/captions; G1 lens 4 |
| `craft/longform/structure-and-retention.md` | First-30s contract, act/chapter structure, nested loops + re-hooks, pacing bands, endings/serialization handoff, the AI-generation constraint layer (8s clips, ~60s shots, credit ceiling) | Scripting any long-form; G1/G2 lens 2 on `vertical: longform` |
| `craft/longform/packaging.md` | Title+thumbnail doctrine (the long-form/Shorts inversion), CTR+retention interplay, Test & compare protocol, sell-the-story title rules, episode numbering, browse-vs-suggested | Packaging any long-form; G1/G2 lens 1 on `vertical: longform` |
| `craft/longform/series-doctrine.md` | Episode/season arcs, serialization mechanics (ep2 doctrine), PVC layer: Gazette-first accuracy workflow, dramatization marking, disclosure placement, family-consultation checkpoint, tribute-integrity G2 checklist | Any series/BET-5 item at ideation, script, or critique |
| `virality/laws.md` | The measurement layer (Law 0.1/0.2) + 11 mechanics laws, each with evidence + operational test | Any critique; any postmortem |
| `virality/failure-modes.md` | The 7-mode failure catalog, named cases, early warnings | Postmortems; weekly-review pivot checks |
| `platform/instagram.md` | Ranking signals w/ evidence tiers, official penalty list, engagement-bait line (THE LINE), specs, funnel mechanics | Any IG script/critique/publish |
| `platform/youtube.md` | Shorts vs. long-form structural differences, specs, genre-lane inversion law, disclosure rules | Any YT script/critique/publish |
| `platform/publishing-ops.md` | How we actually publish/schedule/pull analytics/verify stats/run the DM funnel | `/publish`, `/postmortem` |
| `audience/personas.md` | Who we serve: segments, what they want, what they distrust | Ideation; creative-director briefs |
| `audience/positioning.md` | "Machine craft, human taste": backlash map, disclosure rules, constitutional never-list | Every script with a `[GEN]` asset; every publish |
| `knowledge/brand/tangent-voice.md` | Verbal + visual identity across tangentideas.ai / tangent.gallery | Scripting; captions; cover/thumbnail choices |
| `knowledge/brand/content-architecture.md` | HERO/WORKHORSE/FILLER tiers + concept selector formula | Ideation; roadmap planning |
| `production/adobe-playbook.md` | Driving Lightroom web via Claude-in-Chrome: session protocol, capture-worthy moments, connector vs. browser path | Every `/produce` session with a Lightroom capture |
| `production/assembly-playbook.md` | Capture → cut → captions → export path with exact ffmpeg/OBS settings | Every `/produce` assembly pass |
| `production/genvideo-playbook.md` | Veo/Flow usage: what it's for (b-roll only), what it's never for, prompt patterns, disclosure, TTS | Any script with a `[GEN]`-tagged asset |
| `production/workload-router.md` | Claude-vs-Google job routing, tooling matrix per vertical, the three binding caps, re-verification protocol | Any heavy production run; campaign planning |
| `benchmarks.md` | Metric definitions (matching `tools/metrics.py`), healthy bands, our medians (analyst-owned) | Any postmortem; any weekly-review |
| `pattern-library.md` | Distilled 18-dossier corpus: verbatim hooks, structure templates, archetype cards, funnel evidence, failure catalog | Ideation; differentiation checks (G1/G2 lens 7) |

**Craft packs** (`SYSTEM_DESIGN_V2_PROPOSAL.md` §4.3): per-vertical doctrine lives under
`craft/<vertical>/`; `item.yaml`'s `vertical` field selects which pack the critic and producer
load. Built on lane activation, never speculatively — **existing packs: `craft/reels/`
(corpus-built, 2026-07) and `craft/longform/` (BET-4/BET-5 activation, 2026-08-02)**; podcast/
music/games-apps packs do not exist yet. `brand/kit.yaml` `per_vertical` mirrors pack status.

### Brand Office domain (`SYSTEM_DESIGN.md` §12.2)

| File | What's in it | Read before |
|---|---|---|
| `marketing/brand-science.md` | Mental availability, distinctive assets vs differentiation ([CONTESTED] handled honestly), double jeopardy, 95-5 ([EXTRAPOLATION]-tagged), CBBE/Aaker vocabulary, 60/40 | Any consult; every G3 |
| `marketing/distinctive-assets.md` | TANGENT'S asset register: status, build/protect rules, fame×uniqueness measurement, the G3 asset-usage checklist | Every G3; identity decisions |
| `marketing/positioning-doctrine.md` | One-line-description test, category-entry-point map, competitive frame, brand architecture across surfaces | Strategist consults; every G3 |
| `marketing/growth-playbook.md` | Creator-brand growth economics: owned-audience value, funnel math, monetization-readiness, sponsorship fit, platform-risk | Scientist consults; G3 growth lens |
| `marketing/community-trust.md` | Trust ledger, comment doctrine, crisis protocol, community sequencing ([EXTRAPOLATION]-tagged where unstudied) | Advocate consults; G3 trust lens |
| `marketing/brand-health-metrics.md` | Brand Office's collectable-only metrics + G3 scorecard bands + weekly brand-health format + explicit "NOT collectable yet" list | Every G3; weekly brand-health |
| `SOURCES.md` | **System-wide** trusted-source whitelist (T1/T2/T3 + disqualified) + the zero-hallucination procedural rule (§12.5) — binds BOTH teams | Any claim not already in the bank |

## Provenance-tier legend

- **`[RESEARCH-BACKED]`** — peer-reviewed study, official platform documentation, or an
  on-record platform-executive statement.
- **`[INDUSTRY DATA]`** — a large real dataset from a commercial vendor; directionally
  trustworthy, not peer-reviewed, methodology usually disclosed but not independently audited.
- **`[PRACTITIONER LORE]`** — folk wisdom repeated across creator-economy sources, no traceable
  primary source. Plausible, never scored as proven.
- **`[CORPUS: <file>]`** — from our own 18-dossier creator study; cite the specific dossier.
- **`[OWN-DATA]`** — from our own published posts' postmortems.
- **`[UNVERIFIED STAT]`** — a specific-sounding number untraceable to any named source; kept
  visible so it's recognized and discounted, never used as a scoring threshold.

Six files — all three `platform/` and all three `production/` files (built from the July-2026
research briefs, fresher than the main corpus) — instead carry the briefs' own tags —
**`[HIGH]`/`[MED]`/`[LOW]`/`[UNVERIFIED]`** — preserved as-is rather than force-converted;
treat them as equivalent in spirit to `[RESEARCH-BACKED]`→`[UNVERIFIED STAT]` above. The
briefs themselves are committed at `research/briefs/production_stack_2026-07.md` (cited as
`[stack-brief]`) and `research/briefs/platform_ops_2026-07.md` (cited as `[ops-brief]`) —
every brief-tagged claim resolves there, with the briefs' own source URLs. **Retraction discipline applies everywhere**: a
corrected claim is marked `CORRECTED`/`RETRACTED` in place, never silently deleted.

## Write-control rules

1. `benchmarks.md` is written **only** by the analyst, **only** via `/postmortem` and
   `/weekly-review`. No other session edits it.
2. `craft/`, `virality/`, `platform/`, `production/` files gain `[OWN-DATA]` additions the same
   way — through the postmortem/weekly-review skills, never mid-task to win an argument
   (`SYSTEM_DESIGN.md` §4 rule 2).
3. `pattern-library.md` is a frozen verbatim copy — updated only by re-distillation of the
   corpus, never hand-edited.
3b. `marketing/` files are written **only** by the brand-director, **only** via
   `/weekly-review` or the quarterly brand audit (`ops/ROLES.md` decision right (i);
   `ops/RUNBOOK.md` §9). `SOURCES.md` whitelist changes happen at the quarterly audit.
4. **Quarterly stale-claim sweep** (`ops/RUNBOOK.md` §7): every `knowledge/` file is checked each
   new quarter's first `/weekly-review` for claims whose evidence tier or currency has aged out.
   Owned by the analyst, approved by the Showrunner. Correct and mark — never silently delete.
