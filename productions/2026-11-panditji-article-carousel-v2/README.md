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

**Status:** v3 READY FOR REVIEW (supersedes v2).
- `slides-v3/slide-01.png` to `slide-08.png`, built with `python build_v3.py` from
  `carousel-v3.md`.
- Message and arc: `message-brief-v3.md`, approved by Sparsh on 2026-11-16.
- Skim cold read: PASS (`critiques/cold-read-v3.md`).
- Caption: in `carousel-v3.md`.
- Next: a first-time human read, then Sparsh posts.
- The v2 files (`carousel.md`, `slides/`) are kept as the record of what a second reader
  rejected.

Lesson from this run: the first plain rewrite fixed the real problems (the lecture-style
zodiac slide and the unclear cover). The next two rounds chased small snags that no reader
actually got stuck on, and that was overfitting. One read, real fixes, then move on.

**Story for Instagram (when posted):** one frame showing the cover slide with the text "New
post: why my astrology app won't let AI guess. Tap the link." and a Link sticker to the
article.
