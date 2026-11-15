# Message Brief: <artifact name>

Mandatory before any copy is written, for EVERY artifact: pipeline items (this section lives at
the top of `brief.md`) and ad-hoc pieces made outside the pipeline (save this file in the
production folder). Rules: `knowledge/craft/clarity.md`.

**One-line message:** <the sentence a viewer would say to a friend afterwards: plain words, at most about 15, no metaphor, no jargon>

**Primary audience:** <A (AI-curious everyday viewer) | B (tech enthusiast) | A+B two-layer>
**Why they would care, in their words:** "<what A would say: 'So my horoscope is actually calculated, not made up.'>"

**Format:** <carousel | single image | reel | short | story | caption-only> · **Template / arc:** <e.g. T1 I built it / arc 1>

**Voice and tone:** <who is talking to whom: "Sparsh, to a friend who has never heard of the app"> · **Tone:** <person-direct | person-warm | person-witty> (logged for the tone test in `strategy/BETS.md`)

## The arc (3 to 5 beats; the beats alone must tell the story to a 12-year-old)

| # | Beat (one plain sentence) | What the viewer SEES |
|---|---|---|
| Cover | <what this post is about, as a label plus a stake> | <the thing itself> |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

**Chain device:** <Before/Then/So/Now | Step N | numbered list | question-answer | fixed frame>

**Ending:** <payoff | answerable question | one next step: "link in bio"> (exactly one)

**Depth path (for B):** <article / long video / caption lines 2+ / none> and the one line that points to it.

**Jargon this topic tempts us to use, and the plain replacement:**
- <ephemeris> → <NASA's planet tables>
- <deterministic code> → <a normal program>

**Facts and numbers used (each with its source and what it counts):**
- <"matched NASA's tables": source, date>

## Checks (fill these in as they pass)
- [ ] I can say the one-line message out loud without notes.
- [ ] Cover-only read: a stranger can say what the post is about from the cover alone.
- [ ] Headline-only read (`tools/clarity_lint.py` prints it): the headlines tell the story.
- [ ] `clarity_lint.py`: zero FAIL (WARNs are notes).
- [ ] One `/cold-read`: PASS (file: <path>). It is a sanity check; don't chase small snags.
