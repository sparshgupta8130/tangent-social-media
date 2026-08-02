# Postmortem — <item title>

Produced by: analyst, via `/postmortem`, **T+72h minimum** after publish. Item:
`ops/pipeline/NNN-slug/`. Adapted from `research/templates/video_postmortem_template.md`'s
9-section structure, applied to OUR OWN published post rather than a corpus creator's video.
Same evidence-tier discipline applies: every substantive claim is tagged `[OBSERVED]` /
`[REPORTED]` / `[INFERRED]`, per `research/QC_PROTOCOL.md`. A section that cannot be filled says
`DATA GAP: <what's missing and what was tried>` — never silently skipped.

---

## POST: <title / first-line hook>

### 0. Identity & stats
- Platform, published URL (from item.yaml's `published` dict — one entry per platform), post
  date, length.
- Views / likes / comments / shares-saves, each with source + as-of date + confidence
  (`[OBSERVED]` from platform insights, `[REPORTED]` from a secondary tool).
- Rank within our own catalog to date (top-N by views? typical? outlier multiple vs our
  account median, `knowledge/benchmarks.md`?).

### 1. Packaging (the pre-click/pre-swipe layer)
- Cover frame / first caption line as actually published.
- What curiosity gap or promise was made? Was the payoff named or teased?
- Text overlay on frame 1 as published (vs what script.md specified — note any drift).

### 2. Hook (0–3s)
- Verbatim opening line as published `[OBSERVED]`.
- Hook taxonomy classification (result-first / bold claim / question / negative warning /
  demo-in-motion / other — `knowledge/craft/reels/hooks.md`).
- What the viewer actually sees in the first seconds, as shipped.

### 3. Structure & retention engineering
- Beat map as published vs script.md's beat sheet (rough timestamps) — note any cut deviations.
- Open loops planted and where they closed (vs the loop map in script.md).
- One-idea or listicle? Payoff placement (front-loaded / end-loaded / drip).
- Pacing markers: cut frequency, b-roll ratio, caption/subtitle style as shipped.
- Retention chart shape if platform insights expose one (`[OBSERVED]`), else
  `DATA GAP`.

### 4. Value proposition
- What the viewer walks away with (skill, tool name, workflow, emotion, identity boost).
- Practical value class: copyable workflow / tool discovery / news / entertainment / aspiration.
- Specificity level actually delivered (exact prompts/settings shown vs vague gesturing).

### 5. Psychology scoring (against `knowledge/virality/laws.md` / synthesis/01_VIRAL_MECHANICS.md)
- STEPPS scan: which of Social currency / Triggers / Emotion / Public / Practical value / Story
  were activated, and HOW (cite the moment).
- Primary emotion + arousal level actually landed (vs brief.md's target — note any gap).
- Identity-signaling share motive: who shared this and what does sharing say about them?
- Save/send trigger: what made this savable or DM-able?

### 6. CTA & funnel mechanics
- Explicit CTA as published (comment-keyword DM / follow-for-part-2 / link-in-bio / none).
- Comment-bait mechanics observed in top comments, if any.
- `tools/metrics.py funnel` result: comment:like ratio vs the ≥0.5 working-funnel bar
  (STRATEGY §6.5), if this was a funnel post.

### 7. Repeatability verdict
- The extractable TEMPLATE: 3–6 bullets another session of ours could reuse as-is.
- What's commodity vs what is OUR unfair advantage in this post (STRATEGY §8).
- Does this become/reinforce an owned format, or was it the one active audition
  (STRATEGY §4)? State the recommendation.

### 8. Why it won (or lost) — analyst synthesis
- 3–6 sentences: the single most load-bearing reason for this outcome, secondary factors, and
  any luck/timing components (news-surfing, platform push).
- If comparing against our own recent flops/hits: name the delta explicitly.

---

## Verified-stats block
Claimed numbers (from platform insights) vs `tools/verify_stats.py` second-source output.
Flag any divergence >10%. No number above may be used single-sourced (CLAUDE.md non-negotiable
#4; corpus finding: browser-scraped likes were wrong 15.5% of the time).

| Metric | Claimed | verify_stats.py | Divergence | Verdict |
|---|---|---|---|---|
| Views | | | | |
| Likes | | | | |
| Comments | | | | |

## Views×LR decomposition verdict
`tools/metrics.py decompose` output and quadrant verdict: hook/discovery failure vs craft
failure vs healthy vs boosted-suspect (STRATEGY §6.3, synthesis/01 Law 0.2).

## Critic-calibration block
G2 scorecard scores (`critiques/G2-cut.md`) vs actual outcome above. Where was the critic
right; where was it wrong; by how much. If a systematic miss (not a one-off), state the specific
critic-prompt change being proposed to the Showrunner (`ops/RUNBOOK.md` §7).

| Lens | G2 score | Outcome evidence | Critic right/wrong | Proposed prompt change (if any) |
|---|---|---|---|---|

## Knowledge-bank update list
Every `[OWN-DATA]` entry written as a result of this postmortem — file + exact line/section
added or corrected (retraction discipline: correct and mark, never silently delete).

- `knowledge/<file>` — <entry added, verbatim or close to it>

## One-line lesson
<the single sentence this postmortem should leave behind for the next similar item>

---

### Sources
Every URL/tool output used for this postmortem's numbers.
