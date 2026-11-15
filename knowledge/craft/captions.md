# Captions, titles and story text (every format)

Sits under `knowledge/craft/clarity.md`. Covers Instagram captions (carousels, reels, single
images), YouTube titles and descriptions, and Story text. Evidence:
`research/clarity-2026-11/` (caption sections of each harvest file).

## The first line is the message

Only about the first 125 characters of an Instagram caption show before "more". So line 1 is
the one-line message, in plain words, or the plain question the post answers. It must make
sense on its own, as a full sentence.

Strong first lines from the corpus:
- "Jensen Huang just resigned as CEO of Nvidia, effective immediately, after 33 years running
  the company" (1.5M plays)
- "What if computers stopped using electricity and started using light?" (2M plays)
- "Turns out seeing sound is really fun" (1.1M plays)
- "Made your app with AI? Check these 5 things before you share the link."

Weak first lines lead with a sponsor, a link list, a vague teaser, or promo copy that does
not describe the post. A text-free gallery captioned "Unlock the branding secrets behind
7-figure empires!" got 7 likes.

## After line 1

Pick one mode in the Message Brief:
1. **Restate, then extend:** the next 2 to 4 short lines add the story, the context or the
   "more" layer for enthusiasts. This is the default for builder and explainer posts.
2. **A new idea:** the caption adds something the slides do not say (The School of Life).
   Best for reflective posts.
3. **The question:** one question the reader can answer, to invite comments.

Write the caption as Sparsh talking: "I", "you", short paragraphs of 1 to 3 sentences.

## Links

Links in Instagram captions are not clickable. Never paste a URL in a caption, because it
shows as plain text. Say "Link in bio" (and put the link there), and use the Link sticker in
a Story. `tools/clarity_lint.py` fails a caption with a URL in it.

## Calls to action

One per post, and it must fit the post:
- "Link in bio" when there is depth to go to.
- A real question.
- "Save this" for reference posts.
- "Send this to someone who..." only when there is a real someone.

Never "follow for more". Never keyword-DM bait unless it delivers a real deliverable (the
engagement-bait line in `knowledge/platform/instagram.md`).

## Disclosure

AI involvement is stated in plain words inside the visible part of the caption, or the line
right after it (CLAUDE.md non-negotiable #2). Plain beats clever here too. "I built this with
Claude. I don't write code." is better than a stylized disclosure line. The disclosure lines
in `brand/kit.yaml` are the defaults.

## Hashtags

0 to 5, specific to the post, at the end. Most big accounts in the corpus used none.

## YouTube titles

3 to 8 words. Name the thing. No coined words, no riddle. A question only if it is the
question a normal person asks.
- Strong: "Guess How Far The Sun Is", "This can SEE Sound!", "Why Is Everyone Buying Mac
  Minis for AI?"
- Weak: "Use AI as a Sparring Partner for Your Thinking" (3.8K views, against 253K for the
  same creator's plain question)

The description's first line restates the hook.

## Story text

One line per Story frame, 3 to 10 words, large, high contrast. Say what it is and what to tap:
"New post: how I built Panditji. Tap the link."
