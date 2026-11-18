# The Museum of Men (International Men's Day, 19 Nov 2026)

**Request, verbatim (Sparsh, 2026-11-18):** "let's do the Museum of Men"

It follows the research and idea slate in `research/mens-day-2026-11/` (`IDEAS.md` idea #1,
evidence in `FINDINGS.md`). Made with `/post`, in INTERACTIVE mode.

**Concept:** a gallery exhibition of the everyday things Indian men (dads first) keep, each
shot like a museum piece with a plain label line. It opens funny and recognisable, and the
last two exhibits turn warm: what he gives up, and his phone, so call him.

| File | What |
|---|---|
| `message-brief.md` | First Message Brief. Its arc and exhibits are superseded by `carousel.md` (see the log) |
| `carousel.md` | The copy: 10 slides, picture notes, caption |
| `lint.txt` | `clarity_lint` output |
| `critiques/` | Cold-read packet and reports (copy phase: PASS) |
| `image-prompts.md` | Nano Banana prompts for the 9 image slides |
| `assets/gen/` | Generated images, picks, contact sheet, provenance README |
| `build.mjs` → `slides/` | Renders the 10 final slides (1080×1350) |

## Decision log
- 2026-11-18: Sparsh picked idea #1 (Museum of Men) from the slate.
- 2026-11-18: Sparsh: "He'll ask if you've eaten" is not true for Indian dads, so the line is
  cut. Proposed replacement: "He'll say 'call when you reach'". Better still, a line his own
  dad actually said.
- 2026-11-18: Sparsh's dad passed away a few years ago. He asked whether a second-last slide
  "in memory of my dad" is appropriate. Showrunner view: yes, under conditions:
  - it is one quiet slide, never the cover or the hook;
  - no AI image of his dad;
  - his family is okay with it.
  Waiting on Sparsh.
- 2026-11-18: the last slide is the standard "follow us" channels slide (Sparsh).

## Status
Copy: lint 0 FAIL, cold read PASS. All 10 slides rendered in `slides/`. Waiting on Sparsh's review and SHIP.
- 2026-11-18: Sparsh: with the dad anchor and the memory slide, the post reads like Father's
  Day, not Men's Day. Showrunner agrees. Proposed fix, waiting on Sparsh:
  - exhibits come from different men (dad, brother, nana, best friend, husband, colleague);
  - the turn becomes the "all good 👍" text (men's wellbeing, from idea #5);
  - the memory slide stays, as one man among them, and its call to action widens to
    "check on the men in your life".
- 2026-11-18: Sparsh: the exhibits felt disconnected, with no end-to-end story. Showrunner
  proposed a "what men say vs what they mean" thread.
- 2026-11-18: Sparsh rejected "say vs mean" as an old idea. Objects stay as the exhibits. Drop
  his dad's angle if it overfits; Showrunner recommends dropping it from this post.
  - New proposal: one thread, "things men never throw away". It escalates from silly keeping to
    what he keeps inside (an empty plinth). Waiting on Sparsh.
- 2026-11-18: Sparsh: use AI images. The empty plinth is not clear without text, so find another
  visual for "men hiding something inside".
  - Showrunner picked: his phone, with a message typed but never sent ("Honestly bro, I'm not
    doing okay").
  - Considered: a sealed, unsent letter (less current) and a pressure cooker (reads as men
    exploding).
  - The almirah line was made plain ("always locked") so the phone carries the turn alone.
  - New one-line message: "Men keep everything, even how they really feel. Ask them."
- 2026-11-18: cold read PASS. Both readers flagged the almirah (no joke, repeats the keys), so it
  was swapped for the TV remote in its plastic cover. Both said the end slide gives no reason to
  follow; that is optional polish for Sparsh.
- 2026-11-18: images are generated in a separate cloud session on the "Default and Testing"
  environment, which has a Gemini key (session_01ETPVMQJ5AeMPPkRDQ271nH). Output goes to
  `assets/gen/`, with a provenance README.
- 2026-11-18: Sparsh wants an end-slide line that links Men's Day to what he builds with AI.
  Options proposed; waiting on his pick.
- 2026-11-18: end slide: Sparsh picked option 1, as a label card only with no photo. The card
  reads "Exhibit 8 · The maker: The man who made this museum, with AI. Follow him for more art,
  apps and stories", with a disclosure line.
- 2026-11-18: slides built. Slide 8 is a zoomed crop so the chat is readable. A small added detail:
  Rahul's incoming "Kaisa hai bhai? 🙂" gives the unsent draft its context. Disclosure
  "Images made with AI" is on the cover and the end card, and in the caption.
- 2026-11-19: Sparsh asked for a 1:1 version. `build_square.mjs` renders it to `slides-square/`
  (1080×1080): a per-slide square crop of the same images, with type scaled down. The 4:5 set in
  `slides/` is kept.
- 2026-11-19: GTA 6 tie-in: Sparsh doesn't want "Exhibit 9" framing in the feed, because the
  order of feed posts isn't fixed. It works only in Stories. He liked the leave application and
  the calendar; more ideas were requested. It will be a separate production.
