# Hooks — Operational Doctrine

Load-bearing for `/script` and G1 critique lens 1 (HOOK, weight ×2 —
`templates/critique-scorecard.md`). Every script needs ≥3 hook variants tested against this
doctrine before G1.

## The gate: 1s (YouTube) / 3s (Instagram) — why it's platform-enforced, not folk wisdom

YouTube Shorts is a swipe-continuous feed with no click/thumbnail moment: "you have one second
to hook someone" (Jenny Hoyos, on YouTube's own creator blog) — 99.9% of Shorts views come from
the feed, not a thumbnail click, so hook quality *is* the entire discovery mechanism
[RESEARCH-BACKED: research/03 §1.2.1, §1.2.3]. Instagram's ranking model foregrounds
"likelihood to watch all the way through," and the ad-industry's "hook rate" metric is literally
defined as % of impressions reaching 3 seconds — Meta's own systems treat 3s as a first-class,
separately measured checkpoint [RESEARCH-BACKED: research/03 §2.1.3]. Corpus confirmation: every
top performer across all 8 YT dossiers names or shows the payoff in second 0–1, zero preamble,
zero branding [CORPUS: synthesis/01 Part 1 §1].

## The first-frame test (procedure — run at G1 and every script review)

1. Describe frame 0 in one sentence, with no context from the rest of the script.
2. Ask: "would a cold scroller — no prior exposure to Tangent — stop on this frame alone?"
3. If the answer needs the caption, the audio, or "well, then it explains..." — it fails. The
   frame must carry the stop unaided [RESEARCH-BACKED: research/03 §1.2.1, §2.1.3].
4. Check for non-payoff material before the promise resolves (logo, "hey guys," branding) — any
   of it present is an automatic fail regardless of what follows [RESEARCH-BACKED: research/03
   §2.6.2].

## Hook classes, ranked by corpus win-rate

Frequency-in-tops ranking across all 8 YT + 10 IG dossiers [CORPUS: synthesis/01 Part 1 §1]:
**demo-in-motion/result-first > bold specific claim > news-event framing > confronting question
(only when the video actually resolves it).**

### 1. Demo-in-motion / result-first — the load-bearing class

Show the finished output or the tool actively working before any narration or claim.

| Hook (verbatim) | Creator | Numbers | Cite |
|---|---|---|---|
| "POV: you got tired of editing so you ask claude to edit for you under 2 min" | Devin Huynh | 2.5M views, 2.13% LR, #1 of 60 (~18.8x median) | [CORPUS: pattern-library §1.1] |
| "Breaking the barrier between what's real and what's not" (no dialogue — the clip is the hook) | Sebastien Jefferies | 950K views, 6.41% LR — highest in his sample | [CORPUS: pattern-library §1.1] |
| "I just built the ultimate personal assistant in n8n using absolutely no code." | Nate Herk (YT) | 1,343,016 views, ~3.8% LR — #1 short, 52.7x median | [CORPUS: pattern-library §1.1] |
| "No way. This right here is my OpenClaw AI agent... it can literally control Blender." | Riley Brown | 116,375 views, 4.71% LR — highest in his sample | [CORPUS: pattern-library §1.1] |
| "Comment 'prompt' and I'll send you this entire system" (fully automated podcast agency) | Ankit Arora | 5.5M views, 153,511 likes | [CORPUS: pattern-library §1.1] |

Caution: several headline demo-in-motion numbers in the dossier (e.g. Nate Herk IG's "Comment
SYSTEM," 3.3M views) are **pinned** legacy posts, not fresh organic proof — check
`virality/laws.md` Law 0.1 before citing any of these as "what to expect this week."

### 2. Bold, specific claim

Confronts an expectation or states a superlative/exact figure directly, zero preamble.

| Hook (verbatim) | Creator | Numbers | Cite |
|---|---|---|---|
| "The material that might replace silicon in your computer is diamonds." | Tiffany Janzen | 1.3M views, 6.94% LR — highest verified organic rate in her dossier | [CORPUS: pattern-library §1.2] |
| "The chip that made MacBooks the king of laptops finally has a serious challenger." | Varun Mayya | 1.5M views, 6.02% LR — #1 non-pinned, ~7.3x median | [CORPUS: pattern-library §1.2] |
| "A 4000 rupee filter and 74 percent cleaner exhaust." | Vaibhav Sisinty | 1.3M views, 3.62% LR — highest in sample | [CORPUS: pattern-library §1.2] |
| "i charge my clients $26K/mo for video editing..." | Devin Huynh | 2.1M views, 1.26% LR | [CORPUS: pattern-library §1.2] |

### 3. News-event

Built on a real, timely, named event with a live news cycle — a reliable, engineerable lever,
not luck [CORPUS: synthesis/01 Part 1 §8].

| Hook (verbatim) | Creator | Numbers | Cite |
|---|---|---|---|
| "In the quaintest corner of Middle Earth, embark on an epic journey..." (LOTR trailer) | Curious Refuge | 4,412,573 views — 152x long-form median, the single highest-performing video in the dossier | [CORPUS: pattern-library §1.3] |
| "Claude just dropped Computer Use — and it's a game changer." | Ankit Arora | 793K views, 3.95% LR (highest of his top-3) | [CORPUS: pattern-library §1.3] |
| "I asked a question and it took almost 19 minutes before it was answered." (o3-pro, posted 1 day after release) | Wes Roth | 29,504 views — his best-engineered organic example | [CORPUS: pattern-library §1.3] |

### 4. Confronting question — ONLY when the video resolves it

A question with no payoff is a flop waiting to happen (see anti-patterns below). This class only
wins when the rest of the video visibly answers its own question.

| Hook (verbatim) | Creator | Numbers | Cite |
|---|---|---|---|
| "What happens when you ask ChatGPT to erase your entire digital footprint...?" (then does it) | Sabrina Ramonov | 3.3M views, #2, 139x median | [CORPUS: pattern-library §1.4] |
| "did Chachi PT just take over customer service jobs" (ASR-mangled, resolves w/ live demo) | Futurepedia | 6.6M views — #1/67, 405.8x median | [CORPUS: pattern-library §1.4] |

## Curiosity-gap mechanics (Loewenstein)

Curiosity is a felt gap between what's known and what's wanted — it requires *partial*
knowledge, not zero and not total. Too little context and there's no perceptible gap, just
confusion; too much and the gap is already closed, nothing left to watch for
[RESEARCH-BACKED: research/03 §2.1.1, Loewenstein 1994]. Operational test: does frame 0 give
*just enough* to make a viewer feel a specific gap ("wait, how did that happen") without
resolving it immediately?

## Anti-patterns (named flops)

- **Preamble / credentialing cold-opens**: Matthew Berman's "Hey, I'm Matt. I'm a multi-time
  tech founder..." — 3,603 views, dead last of 200 [CORPUS: pattern-library §5.6]. Harper
  Carroll's worst post (36.2K views) is her only one *missing* her standing credential-forward
  signature block — proof the block works when present, not proof credentialing itself is the
  hook [CORPUS: pattern-library §5.6]. Devin Huynh's Video 7: credential → problem → feature
  list → pricing → CTA after 50+ seconds — "the classic long-form sales-page structure
  compressed into a Reel," the exact inverse of his winning template
  [CORPUS: pattern-library §5.2].
- **Abstract openings**: Skill Leap AI's "Are you using AI agents yet?" — sharp title, abstract
  trend-statement actual hook; 1,949 views, #29/30 [CORPUS: pattern-library §5.1].
- **Hook-coherence breaks** (hook promises a different video than delivered): Nate Herk (YT)'s
  "Fake it till you make it" into fragmented multi-speaker chatter with no context — 4,881
  views, dead last of 164 [CORPUS: pattern-library §5.1]. Riley Brown's Taylor Swift/"Swifties"
  hook delayed the tool demo 20+ seconds — 3,950 views, 0.348x median (comment rate still beat 6
  of his 8 tops, proving this is a reach failure, not a reception failure)
  [CORPUS: pattern-library §5.1].

## Tangent-specific hook guidance

**Sell the image, not the AI** — the Skill Leap reach-ceiling law: pure-AI framing caps *reach*
even when per-viewer resonance is equal or higher (their AI-topic Shorts out-liked their
1M-view general-tech hit, 4.01% vs 3.32%, at a fraction of the views) — the frame, not the
topic, sets the ceiling [CORPUS: pattern-library §3.14a — flagged as the single most important
corpus finding for Tangent's strategy]. Practical rule: the hook leads with the universally
legible payoff (a breathtaking photograph, an impossible transformation, an agent doing
something jaw-dropping); the AI is the twist that lands *after* the scroll-stop, never the
opener [STRATEGY §2].

Our hook surfaces (map a concept to one of these before scripting):
- **Finished-plate reveal** — the graded photograph appears, full-frame, before any process is
  shown (demo-in-motion/result-first class).
- **Sliders-moving-by-themselves** — Lightroom UI with visible, cursor-less adjustment, the
  agent's hand made legible without narration (demo-in-motion class; BET-3, `strategy/BETS.md`).
- **Critic-rejection moment** — the critic's on-screen verdict/one-liner as the cold open
  (bold-claim-adjacent; also brand differentiation — nobody else in the corpus shows a rejection
  on-screen).
- **Before/after snap** — hard cut, no transition, raw vs. graded (bold-claim class; the
  corpus's most portable, lowest-production-cost hook surface).
