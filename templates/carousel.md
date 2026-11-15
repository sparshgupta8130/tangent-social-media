# Carousel copy: <title>

Produced by: story-lead via `/script` (pipeline) or the Showrunner via `/post` (ad-hoc). Rules:
`knowledge/craft/clarity.md` and `knowledge/craft/carousels/structure.md`. The Message Brief
comes first (`templates/message-brief.md`).

This file is ALSO the input to `python tools/clarity_lint.py check <this file>`. Keep the
format exactly:
- `### Slide N`, then `H:` for the headline (the slide's whole point as one plain sentence),
- `B:` for the optional body (1-2 short sentences of depth),
- `V:` for what the picture shows (not linted).
- A line ending `<!-- lint-ok: reason -->` is exempt from the FAIL patterns. Use it rarely,
  and the critic sees every one.

**One-line message:** <copied from the Message Brief>
**Audience:** <A | B | A+B> · **Template:** <T1-T6> · **Tone:** <person-direct | person-warm | person-witty>

## Slides

### Slide 1
H: <the cover: what this post is about, as a label plus a stake, 6-14 words>
V: <the thing itself: the app on a phone, the photograph, Sparsh>

### Slide 2
H: <one plain sentence; slide 2 must stand alone, so name the subject again>
B: <optional>
V: <the picture of what the headline names, with labels on it>

### Slide 3
H:
B:
V:

### Slide 4
H:
B:
V:

### Slide 5
H: <the ending: the payoff, a real question, or one next step>
V:

## Caption
<Line 1: the one-line message or the plain question, under ~125 characters.>

<2-4 short lines: the "more" layer, as Sparsh talking. The AI disclosure in plain words. "Link in bio" if there is depth. No URLs.>

<0-5 specific hashtags>

## Lint result
```
<paste the output of: python tools/clarity_lint.py check <this file>>
```
