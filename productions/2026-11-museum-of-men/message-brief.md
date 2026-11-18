# Message Brief: The Museum of Men (IG carousel, International Men's Day)

**One-line message:** Dads keep the funniest things, and they hide how much they love you.

**Primary audience:** A (everyday viewer, mostly Indian, often reading English as a second
language). B gets nothing extra here; it is not a tech post.
**Why they would care, in their words:** "That's literally my papa. Sending this to him."

**Format:** IG carousel (about 10 slides, 4:5).
- Derivatives come later: a slow-push YT Short / Reel cut, and a LinkedIn document version
  ("The Museum of the Working Man").
- **Template / arc:** a list built on a fixed frame (the museum), then a turn.

**Voice and tone:** Sparsh, showing a friend round his dad's "museum".
- **Tone:** person-witty, with a warm close. Logged for EXP-TONE in `strategy/BETS.md`.

**Look:** gallery-white walls, one object per slide on a plinth or wall, soft spotlight, and a
small museum label card.
- The beat sentence is set large in Fraunces, readable on a phone. It is never tiny plaque text.
- This doubles as an EXP-LIGHT data point: a light background. Sparsh has final call on the look.

## The arc (the beats alone tell the story)

| # | Beat | What the viewer SEES |
|---|---|---|
| Cover | The Museum of Men: things every Indian dad refuses to throw away. | A gallery wall, the first exhibit on a plinth, the title on the wall |
| Exhibits | One object per slide, one plain funny-and-true line each (list below) | The object, museum-lit, with an "Exhibit N" label |
| Turn | His old shirt: he wears it again so you can have new ones. | A folded, faded shirt under a spotlight |
| Ending (proposed) | His phone. He won't say he misses you. He'll say "call when you reach". | An old phone on a plinth |
| In memory (proposed, Sparsh deciding) | This museum is for my papa. He passed away in [year]. If yours is here, call him today. | A real photo of his dad, or one real object of his. Never an AI image of his dad. |
| End slide | Follow along: our channels (the standard end slide, like the Panditji v4 end slides) | Channel handles |

- **Chain device:** a fixed frame. The same museum layout, with "Exhibit 1", "Exhibit 2" and so
  on, in the same place every time.
- **Ending:** one next step, "call him today", on the in-memory slide. Then the standard follow slide.
- **Depth path:** none needed. The caption repeats the message and adds the IMD date.

## Exhibit shortlist (draft lines; Sparsh picks 6 to 7)

| Exhibit | Draft line | Joke type |
|---|---|---|
| His glasses | Usually found on his head, while he searches the house for them. | quirk |
| The cable drawer | A charger for a phone he sold in 2011. Just in case. | quirk |
| The AC remote | Still in the plastic cover it came in. The AC is nine years old. | quirk / care |
| The "important documents" folder | Every bill since 1998. Ask him for any one; he'll find it in a minute. | competence, affectionate |
| His chappals | Twelve years old. "They're still fine." | thrift |
| The yellow duster | The car gets wiped every morning, whether it's dirty or not. | ritual |
| The newspaper pile | Sold to the raddiwala every month. He bargains over every kilo. | thrift |
| The toolbox | He'll fix it himself first. Always. | pride |
| The TV remote | Cricket on, volume 40, news at 9. Nobody else touches it. | territory |

**Rule for every line:** the joke is about his habits and his love, never about him being
useless. That follows the UK ASA 2019 rulings (`research/mens-day-2026-11/FINDINGS.md` §3).

## Open decisions for Sparsh
1. **Photographs or generated images?**
   - (a) Sparsh photographs the real objects at home, and the Claude/Lightroom pipeline edits
     them. This is on-pillar, uses his own raws, and has the strongest disclosure line.
   - (b) Nano Banana Pro generates the still lifes. Faster, and needs a plain "images made
     with AI" line.
   - (c) A mix: real objects where they're at hand, generated for the rest.
2. **Anchor:** "every Indian dad" (sharper, sends to Papa) or "every Indian man" (wider, closer
   to IMD's framing).
3. **Which 6 to 7 exhibits.**

## Jargon this topic tempts us to use, and the plain replacement
- "toxic masculinity", "emotional labour", "men's mental health crisis" → none. The post shows,
  it doesn't lecture.
- "curated", "artefact", "installation" → "exhibit" only, because it is the frame.

## Facts and numbers used
- "19 November is International Men's Day". Source: `research/mens-day-2026-11/FINDINGS.md` §1 [HIGH].
- No statistics. The 2026 IMD theme is unverified, so it is not used.
- "Twelve years old", "since 1998" and "nine years old" are comic details. They must read as
  jokes, not claims. If Sparsh photographs his dad's real things, use the real years.

## Checks (fill these in as they pass)
- [ ] I can say the one-line message out loud without notes.
- [ ] Cover-only read: a stranger can say what the post is about from the cover alone.
- [ ] Headline-only read (`tools/clarity_lint.py`).
- [ ] `clarity_lint.py`: zero FAIL.
- [ ] One `/cold-read`: PASS.
