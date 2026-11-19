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
**SHIP approved by Sparsh, 2026-11-19.** Post `ready-to-post/` (10 square slides, in order) with `ready-to-post/caption.txt`. Tick Instagram's AI label at upload. Waiting on the post time and URL.
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
- 2026-11-19: Sparsh's edits, applied to both builds:
  - removed the "The Museum of Men" / "n/10" header from every slide;
  - removed the "Images made with AI…" line from the end card;
  - removed the "Images made with AI" cover footer;
  - lifted the slide 9 headline clear of the exhibits.
- Disclosure check (CLAUDE.md #2): AI is still stated on-screen on the end card ("The man who
  made this museum, with AI") and in the caption ("Images made with AI"). Also tick Instagram's
  AI label at upload, which also covers India's IT Rules 2026 labelling for realistic synthetic
  media. Do not remove the end-card line without adding another on-screen statement.
- 2026-11-19: **SHIP** (Sparsh). Plan for the day:
  - this carousel goes first, in the morning;
  - the GTA 6 x Men's Day carousel goes 6-8 h later (`productions/2026-11-gta6-mens-day/`);
  - both sets drip as Stories through the day.
- 2026-11-19: Sparsh kept the end card as it is. SHIP reconfirmed.
- 2026-11-19: uploaded to Google Drive folder "Post 6" (1ZVuaqY1jfNxs3Ei7RInOgJmEbe-Erj_7):
  slide-01..10.png (square; byte sizes match the local files) and caption.txt.
- 2026-11-19: Sparsh's edits:
  - cover: the "An exhibition for International Men's Day, 19 November" subtitle is removed;
  - end card: "Happy International Men's Day" added as Fraunces wall lettering above the label
    card.
  Both builds re-rendered.
  - Drive "Post 6": the old slide-01/slide-10 were moved to Drive trash (recoverable) and the new
    ones uploaded. Sizes match: 1651671 and 880977 bytes.
- 2026-11-19 (after SHIP, before posting): Sparsh's changes.
  - Chat messages in English only (global audience). Rahul's message is now "How are you, bro? 🙂".
  - The phone exhibit is now two slides: 8 "What he typed." (draft "Honestly bro, I'm not doing
    good.") and 9 "What he sent." (sent bubble "All good, bro 👍"). The swipe plays the delete. 11
    slides total.
  - His wife: the closing line ties only to the phone and drops the humour. Options offered; the
    Showrunner's pick is "Let him keep the chargers. Just don't let him keep everything to
    himself." Waiting on Sparsh.
  - Drive Post 6 is NOT yet updated; it waits for the closing-line decision.
- 2026-11-19: Sparsh chose the closing line **"Some things men keep are worth throwing out. Start
  with "All good, bro.""**, with a small line "Today, ask one how he's really doing." (slide 10).
  - Caption: "send that message" became "send the real message, not "all good."".
  - Drive Post 6 now holds 11 slides:
    - old slide-08 and 09 and the old caption moved to trash;
    - new slide-08 (typed), 09 (sent) and 10 (close) uploaded;
    - the end card was renamed from slide-10 to slide-11;
    - new caption.txt uploaded.
  - `ready-to-post/` refreshed to match.
- 2026-11-19: Sparsh caught that the row image (slide 10 in the carousel; the video's opening and
  closing row shots) shows objects that don't match the individual exhibits. It was generated on
  its own, and the Showrunner missed it in review.
  - The fix is running: session_01ETPVMMMxjR4p8A7NSyhkYB regenerates the row with Nano Banana Pro,
    using the 7 exhibit images as references. Outputs: `assets/gen/row-v2/` (4:5 and 9:16), plus a
    new 9:16 `F0-row.jpg` for the video.
  - The video edit session was told to swap it in.
  - Drive slide-10 gets replaced after review.
- 2026-11-19: row-v2 landed (same objects, order and colours). Showrunner review against the
  comparison:
  - still not identical: phone box (clean vs scuffed), T-shirt print, keys count, drawer density;
  - in the square crop, the far plinths (phone, remote) collide with the headline.
  - Asked for row-v3: a 1:1 version with headroom, plus closer object fidelity in all versions.
  - Slide 10 is not changed in Drive yet.
