---
name: post
description: Use whenever Sparsh asks directly for a social asset outside the full pipeline, such as a carousel announcing an article, a festive reel, a Story, a caption, or a quick photo post. It is the fast path, with light clarity checks. It runs a Message Brief, plain copy, clarity_lint, and one quick /cold-read before Sparsh sees anything to post.
---

## Why this exists
Most real requests skip `/ideate` and arrive as "make me a post about X". Those pieces had no
check at all; the deleted Panditji article carousel was one of them. This skill gives an ad-hoc
piece the essentials of `knowledge/craft/clarity.md` without ceremony. Keep it quick. The goal
is a post a stranger gets and would share, not a perfect score.

## Protocol
1. **Make a production folder** at `productions/YYYY-MM-<slug>/`, with a `README.md` that
   records the request verbatim.
2. **Write the Message Brief** (`templates/message-brief.md`): the one-line message, the
   audience, the beats and the tone. In INTERACTIVE mode, show Sparsh the message and the beats
   before writing copy.
3. **Say it out loud first.** Write the 4-to-6 sentence version Sparsh would say to a friend,
   then cut it into beats.
4. **Write the copy** in `carousel.md`, or in script beat blocks for video.
5. **Lint it** with `python tools/clarity_lint.py check <copy file>`. Fix the FAILs. Use the
   WARNs only where they help.
6. **Cold read, once.** Run `/cold-read` on the copy, or on the render if you have already
   made it. If it fails, fix the real problem and read once more. If it still fails, show
   Sparsh. Don't grind on small snags.
7. **Produce** the slides or video, following the visual rules in
   `knowledge/craft/carousels/structure.md`.
8. **Show Sparsh** the one-line message, the headline-only read, the two readers' RESTATED
   lines, the post and the caption.
9. **Record** what was posted, and when, in the folder README.

## Rules
- Facts from an article or app are cited in the Message Brief. No number appears without its
  noun.
- Disclosure follows CLAUDE.md non-negotiable #2, in plain words.
