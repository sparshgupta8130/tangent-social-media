# Long-Form Structure & Retention — Operational Doctrine

Craft pack: `longform` (`item.yaml` `vertical: longform`) — BET-4 flagship long-forms ("One
plate, start to finish") and BET-5 PVC web-series episodes (`strategy/BETS.md`). Load-bearing
for `/script` and G1/G2 lens 2. Platform mechanics live in `knowledge/platform/youtube.md`
(§5 packaging, §8 disclosure, §9 monetization) — this file extends, never duplicates. Reels
doctrine (`craft/reels/structure-and-retention.md`) still governs loop hygiene; this file is
what changes at 8–20 minutes.

## The first-30-seconds contract — platform-scored, not folk wisdom

YouTube's own retention report has a named "Intro" key moment: **the percentage of viewers
still watching after the first 30 seconds**, and YouTube's own help text says it "indicates
whether the content in the first 30 seconds matched the viewer's expectation of the video's
thumbnail and title" [VERIFIED-ONLINE: support.google.com/youtube/answer/9314415 "Measure key
moments for audience retention," accessed 2026-08-02 — T1 official]. The contract: **the
packaging writes a check; the first 30 seconds must visibly cash it.** Long-form viewers
arrive by click, not swipe (`platform/youtube.md` §5; research/03 §1.2.3) — they chose a
promise, and the opening's only job is to prove the promise is real.

Operational rules:
- **Cold open on the promise, not toward it.** The thumbnail's subject (the finished plate,
  the battle's stakes, the recipient's name) appears in-frame inside 30s — shown, not
  narrated-about. Front-loaded non-payoff material (logo, "welcome back," channel branding)
  measurably costs viewers who never return; steepest drop is the opening seconds
  [INDUSTRY DATA: Wistia retention curves via research/03 §2.6.2 — direction credible, every
  circulating magnitude is [UNVERIFIED STAT]].
- **Brand card after the first payoff beat, never before** — ≤5s, only once the cold open
  has landed. Anti-pattern: Matthew Berman's credential cold-open, dead last of 200
  [CORPUS: pattern-library §5.6].
- **The 30s test at G1:** read only the script's first 30 seconds against the working
  title+thumbnail. Does a viewer who clicked THAT get proof of THAT? If the proof needs
  minute 2, restructure — the platform scores the mismatch at second 30.

## Act structure — cold open → contract → escalating acts → close

The corpus's two proven long-form skeletons [CORPUS: pattern-library §2.19]:
- **Ottley flagship:** stacked specific credibility/stakes claim → **explicit structure
  preview ("Three Parts of This Video")** → numbered body under one unifying frame, never a
  flat list → close resolving the opening claim. The structure preview is a retention device:
  it converts runtime into a visible, finite commitment.
- **Ottley documentary-series:** aggregate stakes up front → **evenly-paced ~90s numbered
  segments**, each with its own named payoff → **drip-feed payoff evenly, no single dominant
  climax** → close inviting the next loop.

Tangent adaptation (policy, built on the above + the reels escalation law): 3 acts for an
8–20min piece — Act 1 stakes + first real payoff, Act 2 process/complication (the honest
error-and-fix beat lives here — trust device, [CORPUS: synthesis/01 Part 1 §5]), Act 3 the
strongest material. **Escalating order holds at long-form scale: most impressive LAST**
[CORPUS: pattern-library §2.15 — Berman's matched pair]. End on the natural button line of
the material itself, never a re-summary [CORPUS: pattern-library §2.20 — Wes Roth].

**Chapters** (official mechanics): first timestamp 00:00, ≥3 timestamps ascending, ≥10s per
chapter; chapters render as labeled progress-bar segments viewers navigate and rewatch
[VERIFIED-ONLINE: support.google.com/youtube/answer/9884579, accessed 2026-08-02 — T1]. Rule:
chapter titles are mini-hooks written at script time (a promise per chapter, banned-words
list applies), not filenames ("Act 2" fails; "The critic rejects pass four" works). Whether
chapters net-help retention: UNKNOWN — research gap: no T1/T2 study located; treat as a
navigation/expectation device, not a retention lever.

## Loop discipline at long-form scale — nested, with re-hooks

Reels carry one loop map; long-form carries **three depths**, all in `script.md`'s loop map:
1. **Master loop** — the episode question the packaging opened. Closes in Act 3, never
   earlier. Mechanism: Loewenstein's curiosity gap applied across runtime
   [RESEARCH-BACKED: research/03 §2.6.1].
2. **Act loops** — each act opens its own question and closes it before the master loop
   resolves. **Mid-video re-hooks at every act boundary**: re-state what's still unresolved
   the moment a sub-payoff lands ("nested loops, biggest payoff near the end"
   [PRACTITIONER LORE: leaked MrBeast production doc via research/03 §2.6.1 — structure
   corroborated, all lift numbers [UNVERIFIED STAT]]).
3. **Micro loops** — per-beat "watch this next adjustment" tension; inherited unchanged from
   `craft/reels/structure-and-retention.md`.

An unresolved loop at any depth is a lens-2 gate fail, same as reels. Named flop class:
ending mid-thought / question never answered — Wes Roth's worst (3,190 views, dead last of
44), Skill Leap's worst [CORPUS: pattern-library §5.7].

## Pacing bands — retention expectations scale with length

- No whitelisted source publishes an episode-length sweet spot for YouTube long-form.
  **UNKNOWN — research gap: is there a T1/T2 length-vs-performance dataset for 8–20min
  creator video?** What exists, tiered honestly: vidIQ's vendor guidance bands — average %
  viewed targets of 50–70% (<5min), 40–55% (5–15min), 30–45% (15–30min), 25–35% (>30min),
  with one disclosed first-party point (their own channel: 30.3% viewed across 16.5M
  long-form views, Jun 2025–Jun 2026) [INDUSTRY DATA / MED: vidiq.com/blog/post/
  average-view-duration/, accessed 2026-08-02 — T2 vendor, single-channel validation]. Use
  these bands as the "platform-typical for length" reference BET-4/BET-5 gates name, until
  [OWN-DATA] replaces them.
- Wistia's 13M-video 2026 dataset shows engagement declining past ~5 minutes — hosted
  *marketing* video, not YouTube; direction only [INDUSTRY DATA: wistia.com/learn/marketing/
  optimal-video-length, accessed 2026-08-02].
- Duration policy (mirrors `tools/hygiene_check.py` `yt-long`): hard 60–3600s, recommended
  480–1200s (8–20min). Policy pending [OWN-DATA], not a researched sweet spot.
- **Length earns itself** scales up: reels demand a state-change every 5–15s; long-form
  demands a new visible development (adjustment, reveal, complication, verdict) roughly every
  30–60s, and a chapter-scale payoff every ~90s [policy — extrapolated from
  [CORPUS: pattern-library §2.19]'s 90s segments; no verifiable cuts-per-minute number
  exists, same discipline as `craft/reels/structure-and-retention.md` pacing rule].

## Endings and next-episode mechanics

1. **Close the master loop first.** The tease is *after* the resolution, never instead of it
   — a withheld payoff is the §5.7 flop class, not serialization.
2. **Then serialize:** verbal + end-screen tease naming the next episode's concrete promise
   (a named recipient, a named plate — not "more soon"), the series playlist (marks videos
   as an official set; other series videos get featured/recommended alongside
   [VERIFIED-ONLINE: support.google.com/youtube/answer/6084043, accessed 2026-08-02 — T1]),
   and the Shorts related-video link back-path (`platform/youtube.md` §4).
3. Plan ep2's audience on follow-conversion, not view compounding — "the series' power is
   commitment-signaling, not view-compounding" [CORPUS: pattern-library §2.3, verbatim].
   Full serialization doctrine: `craft/longform/series-doctrine.md`.

## The AI-generation constraint layer — where the tools bind structure

- **The shot unit is ~8 seconds.** Veo 3.1 base generation is 8s; Flow's Extend continues a
  clip by generating from its final second/frames [VERIFIED-ONLINE: blog.google
  "Bringing new Veo 3.1 updates into Flow" + support.google.com/flow/answer/16935718,
  accessed 2026-08-02 — T1 official]; Scene Extension chains to ~60s total continuous shot
  [MED: `production/genvideo-playbook.md` §1]. Script consequence: **write generated scenes
  in beats of ≤8s, and never script a continuous action longer than ~60s** — anything longer
  must be constructed as a cut sequence, which is an editing decision made at script time.
- **Continuity degrades across chained clips.** Extend sees only the previous clip's tail,
  not the scene's history; character/prop/light drift compounds per link. Mitigations:
  Ingredients-to-Video reference images for character/style consistency (up to 3,
  `production/genvideo-playbook.md` §1); recurring anchor shots (returning to a stable
  master framing) to absorb drift [policy — no whitelisted study; drift itself is the
  router's own named honest gap]. "Long-form multi-scene character/world consistency at
  scale; real color grading" is an unsolved stack gap — assembly and grade are human/Resolve
  work, not generation work (`production/workload-router.md` §2 row c).
- **The credit ceiling shapes the season, not just the shot:** ~2,300 Quality credits per
  3-min fully-chained episode ≈ **~2.5 episodes/week hard ceiling**; Fast-tier for non-hero
  shots stretches it (`production/workload-router.md` §3 cap 2, §5 — re-verify live before
  any production commitment, per that file's §4 protocol).
- BET-5 scope note: PVC episodes enter the pipeline as `[SPARSH]` masters
  (`strategy/BETS.md` BET-5 notes) — for those items this layer governs the *structure
  review* (are scenes cut-able at the 8s/60s grain? is drift visible at act scale?), not
  generation execution.

## G1/G2 lens adaptations (longform)

- **Lens 1 — HOOK (×2):** scored as the **packaging + first-30s pair** — the thumbnail/title
  unit (`craft/longform/packaging.md`) and the cold open are one promise, graded together
  against the Intro-metric contract above. The reels first-frame test becomes: "does the
  first 30s visibly cash the exact check this packaging writes?" A strong open under
  mismatched packaging scores as a hook fail, not a packaging footnote.
- **Lens 2 — STRUCTURE & RETENTION:** loop map at all three depths, complete; act boundaries
  each carry a re-hook; chapter map present with mini-hook titles; escalating order with the
  strongest material last; ending closes the master loop *before* any serialization tease;
  every generated scene respects the 8s-beat / 60s-shot grain.
- **Lens 5 — CRAFT & AESTHETICS:** adds the **chained-clip continuity bar** — adjacent
  generated shots checked for character/prop/light drift, grade consistency across acts
  (human-graded, per the router's honest gap), and for PVC items the tribute-integrity
  checklist in `craft/longform/series-doctrine.md` is part of this lens's bar at G2.
