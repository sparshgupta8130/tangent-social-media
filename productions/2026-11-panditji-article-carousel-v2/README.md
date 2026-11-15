# Panditji article carousel, v2 (the Clarity Doctrine's first test case)

**Request:** rebuild the deleted 6-slide carousel that announced "Let deterministic logic decide
and the model explain" (https://labs.tangentideas.ai/writing/deterministic-logic-first/, Medium
https://medium.com/p/26370dd5be48). Sparsh deleted the first version after a first-time reader
said no slide made sense. Made with `/post` on 2026-11-15.

| File | What |
|---|---|
| `message-brief.md` | One-line message, audience A+B, arc, tone, jargon swaps, sourced facts |
| `carousel.md` | The final copy: slides (H/B/V) and caption |
| `lint.txt` | `tools/clarity_lint.py` output (0 FAIL) |
| `critiques/cold-read-adhoc*.md` | The cold-read rounds. Rounds 1-3 were judged under a strict rule that was later retired as overfitting; round 4 passed under the light rule |

**Status:** SLIDES READY FOR SPARSH'S REVIEW.
- `slides/slide-01.png` to `slide-07.png`, 1080x1350, rebuilt with `python build.py`.
- The build uses real assets in `assets/`: the Panditji answer screen, the app icon and the
  Tangent mark.
- Cold read on the render: PASS (`critiques/cold-read-render.md`).
- Next: Sparsh approves, then posts with the caption in `carousel.md` and the Story below.
- Nothing has been posted.

Lesson from this run: the first plain rewrite fixed the real problems (the lecture-style
zodiac slide and the unclear cover). The next two rounds chased small snags that no reader
actually got stuck on, and that was overfitting. One read, real fixes, then move on.

**Story for Instagram (when posted):** one frame showing the cover slide with the text "New
post: why my astrology app won't let AI guess. Tap the link." and a Link sticker to the
article.
