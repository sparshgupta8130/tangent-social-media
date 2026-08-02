# Structure & Retention — Operational Doctrine

Load-bearing for `/script` and G1/G2 lens 2 (STRUCTURE & RETENTION —
`templates/critique-scorecard.md`). Governs everything between the hook resolving and the
ending landing.

## Loop discipline — the loop-map requirement

Every `script.md` must include a **loop map**: every loop opened (a question, a promise, a
"wait for it") listed against where in the beat sheet it closes (SYSTEM_DESIGN §5 —
`script.md` carries "loop map, every loop opened → where it closes"). An unresolved loop is a
critique-gate fail, not a style note — lens 2 of `templates/critique-scorecard.md`.

**Mechanism:** loop-closing is Loewenstein's curiosity-gap mechanism applied across the whole
runtime, not just the opening [RESEARCH-BACKED: research/03 §2.6.1]. Winners visibly resolve
what the hook promises; the worst flops open questions they never answer
[CORPUS: synthesis/01 Part 1 §4].

**Named unresolved-loop flops:**
- Wes Roth, "can AI sway public opinion?" — abstract, unfalsifiable question, references an
  article never shown, ends mid-thought; 3,190 views, dead last of 44. Engagement among the
  small audience it reached was normal (2.60%) — proof the loop failure is a distribution
  problem downstream of the hook, not a reception problem [CORPUS: pattern-library §5.7].
- Skill Leap AI, "ChatGPT competitor from Google is live" — trails off mid-thought, #30/30,
  lowest in the entire catalog [CORPUS: pattern-library §5.7].
- Nate Herk (YT), "Fake it till you make it" — no loop is ever established because there is no
  framing at all; dead last of 164 [CORPUS: pattern-library §5.1].

## Demo-in-motion grammar (the genre closest to Tangent's pipeline)

The full beat grammar, corpus-wide [CORPUS: synthesis/01 Part 1 §5]:

1. **Already-running system** — drop the viewer into a system already live; never open on setup
   or a build-log preamble. Nate Herk's YT skeleton opens on four named sub-agents already
   working, not "let me show you how I built this" [CORPUS: pattern-library §2.5].
2. **Granular visible state-changes every 5–15s** — not one big reveal. Riley Brown's format:
   escalation in visible stages roughly every 10–20s (new pose, new mechanic, iterative
   refinement) [CORPUS: pattern-library §2.6].
3. **Honest error-and-fix, or "now we wait," beat** — outperforms polished cuts; treated as a
   *stronger* trust-building device than a flawless run, not a blemish to edit out
   [CORPUS: synthesis/01 Part 1 §5; pattern-library §2.6 beat 7].
4. **Fixed-length template discipline** — Devin Huynh's five top videos measured **exactly
   24.13 seconds**, ffprobe-verified to six decimal places, near-certain evidence of a reused
   edit template; both his flops ran 48.42s and 67.19s, 2–2.8x longer, outside the template
   [CORPUS: pattern-library §2.1]. Beat-by-beat:
   - 0–5s hook, full text in frame 1, no build-up, over a deliberately mundane real setting.
   - 5–11s escalation/flex line → first product-mechanic reveal.
   - 11–17s core demo: real UI panel, a recurring stock reaction line, drip reveal of a new
     capability every 3–4s, each with its own micro-caption.
   - 18–24s multi-genre proof (the tool shown on a second, unrelated content type) → CTA over
     the same visual the video opened with (a visual rhyme).
   Pacing inside the template: a hard cut or UI-panel change every 1–2s.

## Escalating listicles — most impressive LAST

For multi-item videos, escalating order (weakest → strongest) beats equal-weight lists
[CORPUS: synthesis/01 Part 1 §4]. Matthew Berman's matched pair: winning version = escalating
7+ use-cases, new item every 3–5s, landing on the single most ambitious case as closer (73s);
losing version (posted 7 days later, same product) = single deep-dive, no escalation, soft
rhetorical close — and the losing version scored a *higher* like-rate among those who watched
(4.56% vs 2.50%), proving this was a discovery/distribution failure caused by structure, not a
quality failure [CORPUS: pattern-library §2.15].

## The one absurd/delight beat

One deliberate absurd or comedic beat inside an otherwise utilitarian demo creates the
quotable, rewatch-worthy share moment — Riley Brown's "dance around the room at 8pm" beat
[CORPUS: synthesis/01 Part 1 §4]. Beat 6 of his 10-beat format: "a comedic/absurd sub-task
inserted among utilitarian ones" [CORPUS: pattern-library §2.6]. For Tangent: reserve this for
one moment per HERO piece — an unexpected critic aside, an absurd micro-edit shown and
discarded — never the whole video's register.

## Endings that land vs. trail off

An ending must close the loop map, not just stop. Cross-device/public-deployment proof (Riley
Brown beat 9 — deploys, opens on a second device) is the strongest documented "landed ending"
device [CORPUS: pattern-library §2.6]. Contrast: Skill Leap's and Wes Roth's worst flops both
end mid-thought with no resolution (above). Operational test: read only the last 3 seconds of
the script — does it resolve the loop map, or does it just run out of runway?

## Length bands — "length earns itself"

`tools/hygiene_check.py` enforces reel duration 15–90s, warning outside 20–45s. Devin Huynh's
fixed template (24.13s) sits inside that healthy band; his two flops (48.42s, 67.19s) both
broke the template *and* the band simultaneously [CORPUS: pattern-library §2.1]. Rule: length
is earned by granular state-changes (above), not spent by default — every additional second
must carry a new visible beat, or it gets cut.

## Pacing — qualitative standard only

Frequent visual change (cuts, camera movement, on-screen graphics) sustains attention better
than long static shots — but **no specific cuts-per-second number is verifiable**. Every
circulating figure ("cuts every 0.5–1s," "3.3x completion," the "University of Florida 38%"
study) is untraceable and explicitly flagged **[UNVERIFIED STAT — DO NOT CITE]**
[RESEARCH-BACKED direction / UNVERIFIED magnitude: research/03 §3.3.2]. Score pacing
qualitatively — "high/medium/low" relative to the account's own prior cuts — never against an
invented threshold. The same discipline applies to trending-audio lift and open-loop retention
lift numbers: direction is credible, magnitude is not [research/03 §2.6.1, §3.3.3].
