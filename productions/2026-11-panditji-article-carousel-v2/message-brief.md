# Message Brief: Panditji article carousel, v2

Made with `/post` on 2026-11-15. It rebuilds the deleted 6-slide carousel that announced the
article "Let deterministic logic decide and the model explain"
(https://labs.tangentideas.ai/writing/deterministic-logic-first/, also on Medium). This is the
first artifact made under `knowledge/craft/clarity.md` and its test case.

**Request (verbatim):** "tell me what should I post as the carousel, what should be the caption,
and what should be the story". After the first version was deleted, the brief became: rebuild
it so a stranger understands it at a glance.

**One-line message:** I built a free astrology app where the AI can't make up where the planets are.
(Round 1 wording, "isn't allowed to guess", was unclear to persona A: "guess what?". It was
changed after cold read round 1.)

**Primary audience:** A+B two-layer. A gets the whole story from the slides. B gets the
problem and the fix, and a door to the full write-up.
**Why they would care, in their words:**
- A: "So the app actually calculates my chart. The AI doesn't make it up."
- B: "Nice. The model only explains, and the maths is done by code. I want to read how."

**Format:** carousel, 6 slides, 1080x1350 · **Template / arc:** T5 "what went wrong, and the
fix" (arc 4), with T1's first-person builder voice.

**Voice and tone:** Sparsh, to a friend who has never heard of the app · **Tone:** person-direct

## The arc

| # | Beat (one plain sentence) | What the viewer SEES |
|---|---|---|
| Cover | I built an astrology app where the AI isn't allowed to guess. | The app's answer screen on a phone |
| 1 | At first, I let the AI answer on its own, and it put Saturn in two different signs. | Two chat replies side by side, Saturn in neighbouring signs |
| 2 | It was answering from memory and mixing up two zodiacs. | Two zodiac rings, 24 degrees apart, labelled "Western" and "Vedic" |
| 3 | So now a normal program on your phone works out where the planets are, and the AI only explains it. | A simple diagram: phone, then "program does the maths", then "AI explains" |
| 4 | I checked those positions against NASA's own tables, and they match. | A NASA table row next to Panditji's value |
| End | I wrote up how I built it, numbers and all. Link in bio. | The article's cover image |

**Chain device:** story bridges: At first / But / So now / Then / (end). Fixed frame.

**Ending:** one next step, "Link in bio" (the article goes in the bio for launch week).

**Depth path (for B):** the article (bio link). The caption adds the safety tests.

**Jargon this topic tempts us to use, and the plain replacement:**
- deterministic code / algorithms → a normal program
- the model / LLM → the AI
- ephemeris, NASA JPL, arcsecond → NASA's own planet tables; "they match"
- sidereal / tropical → two zodiacs, Western and Vedic, about 24 degrees apart
- red-team suite, crisis recall → 427 tricky questions; every crisis message caught (caption only)

**Facts and numbers used (each with its source and what it counts):**
- "Asked about career timing twice in one session, the model placed Saturn in one zodiac sign
  on the first turn and the neighboring sign on the second." (article, paragraph 1)
- The two zodiacs are about 24 degrees apart. (article, paragraph 2)
- Deterministic algorithms on the phone compute the astronomy, and the model only explains
  the numbers. (article, In short)
- Planetary longitudes matched NASA JPL and the Swiss Ephemeris to within 1 arcsecond.
  (article, verification table)
- 427 test prompts in English, Hinglish and Hindi; 100% of crisis messages caught; 0 of 113
  ordinary questions wrongly blocked. (article, safety section)

## Checks
- [x] I can say the one-line message out loud without notes.
- [x] Cover-only read: "I built an astrology app where the AI isn't allowed to guess" says
  what the post is about.
- [x] Headline-only read: see `carousel.md`.
- [ ] `clarity_lint.py`: zero FAIL. (Result in `carousel.md`.)
- [ ] `/cold-read` on the copy: see `critiques/cold-read-adhoc.md`.
- [ ] `/cold-read` on the rendered post: pending the render.
