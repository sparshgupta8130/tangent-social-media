# The Museum of Men: the video (YouTube Short + LinkedIn native)

**Request, verbatim (Sparsh, 2026-11-19):** "for linkedin and youtube, should we create a full video
(not a slide show of existing slides but a full animated video) of the various exhibits? Maybe we
just open with the image of slide 9 without the text, and just 'travel in' to the image, exhibit
by exhibit where for each exhibit the corresponding text from its standalone slide appears, till
the end after all exhibits have been traversed through and the final frame is basically the last
slide exhibit 8? Note that this should render as a high production quality video." He also asked
whether to post natively on both platforms, or on YouTube with LinkedIn pointing to it.

## Proposed build (waiting on Sparsh: spend approval and two choices)

**Why not just zoom into slide 9:** zooming into one 2K still turns to mush. The far plinths in
that image are tiny, and they don't match the hero images.

**Instead:** Veo 3.1 Frames-to-Video camera moves between our existing stills.
- Start frame = the row (slide 9's image). End frame = exhibit 1's image.
- Then exhibit N → exhibit N+1, as a dolly along the gallery.
- Each move lands exactly on the original still. We hold there 3-4 s with a slow code push-in
  while the line fades in, so the text and the phone chat stay razor-sharp.

**Shot order:**
1. Open on the row, with the label: The Museum of Men / Things men never throw away.
2. Travel in through exhibits 1 to 7, holding longest on the phone (the turn).
3. Pull back out to the full row: "Men keep a lot to themselves. Today, ask one how he's really
   doing."
4. End on the exhibit 8 wall: Happy International Men's Day plus the maker card.

**Specs:**
- Master is 9:16 (YouTube Short). Derive a 4:5 for LinkedIn.
- The 4:5 stills get outpainted to 9:16 (extra wall and floor) before Veo.
- Target length about 60 s.
- Captions are burned in, because most people watch muted.

**Audio:** gallery room tone from Veo, plus an original, quiet score (Lyria if the key allows,
else synthesized in code). Never trending or licensed audio.

**Disclosure:**
- The end card says "made… with AI".
- YouTube's altered/synthetic toggle is on.
- The caption states that the images and video are AI-made.

**Knowledge-law exception (CLAUDE.md last line):** `genvideo-playbook.md` §2 says generated video
is b-roll only. Here it is the subject.
- Why the exception: the piece is AI art presented as AI art. It is disclosed on screen and in the
  caption, uses no real people, and claims no photography or pipeline output it isn't.
- Logged here. Critic agreement is still to be obtained before publish.

## Decision log
- 2026-11-19: Sparsh approved the opening title and the gen-video exception. He asked for
  open-source tools, since he has Google AI Ultra.
  - Showrunner: this container has no GPU, and Hugging Face is blocked here. The Ultra
    subscription covers Veo in **Flow** (the web app). As far as we know it does not cover the
    API key, and the credit details are [UNVERIFIED] in `genvideo-playbook.md`.
  - Decision: build v1 now with **open-source 2.5D** (Depth Anything V2 depth maps, OpenCV
    parallax, Playwright type, ffmpeg, a synthesized score). It runs in a session on "Default
    and Testing" (session_01ETPVMLx25AFBqSuyBf3GjT).
  - Optional upgrade: true Veo camera moves made by Sparsh in Flow on his Ultra credits, from a
    frame-pair kit we prepare, then swapped into the same edit.
- 2026-11-19: Sparsh has an RTX 3060 laptop and asked for a prompt kit for a Claude session there.
  - `gpu-kit/PROMPT.md` written. It covers 8 first/last-frame camera-move clips (C0-C7), a VRAM
    check first, candidate open-weights routes (LTX-Video / Wan via ComfyUI, to be verified on
    the official repos), and hand-back as `clips/C0..C7.mp4` plus a REPORT.
  - Drive: folder Post 6/video-gpu-kit (1HVt1pZwmJ3708Dxg4RrhWMH4lwUYapml) holds PROMPT.md and an
    empty frames/ subfolder.
  - The 8 frame PNGs (3.7-5.2 MB each) were NOT uploaded: they exceed the connector's ~3.1 MB per
    call limit. Waiting on Sparsh. Frame sources in the repo: F0 = museum assets/gen/pick/slide-09,
    F1..F7 = slide-02..slide-08.
