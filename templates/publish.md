# Publish plan — `NNN-slug`

> Producer + planner fill this at READY, per `knowledge/platform/publishing-ops.md`.
> Precondition: G2 `VERDICT: SHIP` + `approved_by_sparsh` set in item.yaml.
> After posting: `python tools/pipeline.py publish NNN --url <url> --video <final-export-path>`

## Platform targets
| Platform | Variant needed (native re-grammar, never blind cross-post) | Scheduled time (local) |
|---|---|---|
| IG Reels |  |  |
| YT Shorts |  |  |

## Instagram
- **Final caption** (first 125 chars carry the message — they're all that shows):

- **Hashtags** (≤5, per current Mosseri guidance):
- **Cover frame** (1080×1920, chosen from: ______ — legible at grid size?):
- **Audio** (native trending sound must be selected in-app — cannot be set via API; name + link):
- **Audio fallback** (licensed/original if trend expired):
- **Disclosure line** (per `knowledge/audience/positioning.md` — present in caption AND on-screen? quote it):
- **DM funnel** (if funnel post): keyword ______ → deliverable path ______ (real, instant — test the automation before posting)
- **AI-label expectation**: will Meta auto-label this? Is our own disclosure ahead of it?

## YouTube
- **Title** (payoff-first, no "AI" as the promise):
- **Description + related-video link** (long-form tie-in if any):
- **Altered-content disclosure** (required if realistic synthetic media — decision + why):

## Pre-post checklist (all must be checked)
- [ ] `python tools/hygiene_check.py <final-export> --platform ig` → PASS (rerun on the FINAL export, not the G2 cut)
- [ ] Sound-off test on the final export: message legible with captions only
- [ ] Safe zones respected (top ~250px / bottom ~350px / right 10% free of critical text)
- [ ] Disclosure visible in first-scroll caption text, not buried
- [ ] Funnel automation live and tested (if funnel post)
- [ ] Posting time chosen deliberately (note why): ______
- [ ] item.yaml `approved_by_sparsh` date present

## Post-publish (same session)
- [ ] `python tools/pipeline.py publish NNN --url <url> --video <path>` run
- [ ] Planner notified → Plane item moved; postmortem due date set (T+72h): ______
