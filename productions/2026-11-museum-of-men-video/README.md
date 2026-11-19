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

## v1 build (open-source 2.5D), 2026-11-19

**Outputs (`out/`, 59.3 s; 9:16 = 25.2 MB, 4:5 = 18.1 MB; re-rendered 2026-11-19 without the "Images made with AI" line):** `museum-of-men-9x16.mp4` (1080x1920 master, YouTube Short),
`museum-of-men-4x5.mp4` (1080x1350, LinkedIn/IG feed, re-composited, not a crop),
`cover-9x16.jpg` (the title frame), `contact-sheet.jpg` (16 moments). 30 fps, H.264 High CRF 18,
yuv420p, AAC 192 kb/s 48 kHz stereo, `+faststart`. The repo's `.gitignore` excludes `*.mp4`, so the two
files were added with `git add -f`.

**Re-render (in order, from this folder):**
1. `python outpaint.py` – Nano Banana Pro (`gemini-3-pro-image`, Gemini API, `GEMINI_API_KEY`)
   extends each 4:5 still (slides 02-09) to a 3300x3300 stage: wall above, floor below, gallery to
   each side (side room is what the lateral glides travel through). Raw returns in `work/gen/`.
2. `python seamscore.py` – scores how visible the photo's rectangle is in each outpaint. 05 and 07
   failed on the first call (score 21 / 17, a visible box); re-rolled, picks are pinned in
   `stage.py` `PICK` (05 → o6, 07 → o2). 13 image calls in all.
3. `python stage.py` – registers each outpaint to the original (ECC affine; all within ±7 px),
   pulls the outpaint's edge onto the original's edge values, pastes the **original pixels 1:1**
   (every exhibit pixel is the approved still), then Depth Anything V2 Small → disparity maps.
4. `node overlays.mjs` – Playwright renders every text layer per format (9:16 `v`, 4:5 `p`) and
   the phone screen (all 34 typing states x cursor on/off) as transparent PNGs, Google Fonts.
5. `python build.py v` / `python build.py p` – renders + encodes the picture (`--check` reports any
   camera that would leave the canvas; `--frames a,b --out DIR` renders stills for review).
6. `python score.py work/score.wav` – the score. 7. `python mux.py` – out/ files.
`work/` is gitignored (canvases, depth, overlays, intermediates); everything regenerates from the
scripts plus the picks in `../2026-11-museum-of-men/assets/gen/pick/`.

**The edit (59.3 s):** 0–5.4 the row (slide 09), slow dolly with depth parallax, title fades in at
0.1 s and out by 4.5 s → 5.4–6.2 match-dissolve into exhibit 1 (the drawer is aligned by size and
position: same frame spot, zoom ratio 704/748 from the measured drawer widths) → exhibits 1–6,
4.2 s holds with a slow parallax push-in, label + line fade in 0.2 s after landing → 1.1 s lateral
glides between them (cubic in-out, 700 px travel, extra depth parallax, 5-sample 180° motion blur,
crossfade only in the middle 26%) → exhibit 7 holds 6.8 s: push-in from the gallery framing to the
phone (3.85x in 9:16, 3.3x in 4:5); the chat is drawn in code and tracked exactly to the screen
rect; the draft types itself out at 2.6 s, then the cursor blinks; send is never pressed → hard
cut to the row, slow pull-back, the close line in light type with shadow → 1.2 s cross-dissolve to
the gallery wall (slide 03's top) with "Happy International Men's Day" and the maker card →
0.5 s fade out. Copy is verbatim from `../2026-11-museum-of-men/carousel.md`; only line breaks
were added (at sentence ends) for the narrow frame. The maker card also carries "Images made with
AI" in v1 (removed 2026-11-19, Sparsh's call, matching the carousel end card). Text sits between y 262 and ~1500 in 9:16 (outside
the top 220 / bottom 380 Shorts UI).

**Audio:** original, synthesised in `score.py` (no samples): felt-piano model + detuned-saw pad,
70 BPM in D (Dmaj9–Bm9–Gmaj7–Aadd4), a lift at the phone (Em9–F#m7–Gadd9–Asus, higher voicing,
pad swell), space on the return to the row, resolve to D on the end card; synthetic-IR reverb;
room tone = filtered noise; a faint air movement under each glide. No footsteps, no meme audio.
Mastered: −14.0 LUFS integrated, −1.3 dBTP (ffmpeg ebur128 confirms).

**Tools and licences:** Python 3, NumPy (BSD), SciPy (BSD), OpenCV (Apache-2.0), PyTorch (BSD),
Hugging Face transformers (Apache-2.0), Depth Anything V2 **Small** weights (Apache-2.0; the Base/
Large weights are CC-BY-NC and were not used), pyloudnorm (MIT), soundfile (BSD), Playwright
(Apache-2.0) + Chromium, FFmpeg/libx264 (GPL; used as a tool, not distributed), Fraunces + Inter
(SIL OFL, Google Fonts). Images: Nano Banana Pro (the original picks + border-only outpaints;
paid API calls, the same pipeline as the carousel, a few calls only). No paid video generation.

**Honest notes on artefacts (self-review, frame by frame at every transition):**
- It is 2.5D, not real camera motion: the depth map is heavily smoothed so nothing tears, which
  means the parallax is gentle and the wall right behind an object moves very slightly with it.
  No tearing, folding or stretched edges were found in the review frames.
- The glides cross-fade two different rooms in their middle third; with motion blur it reads as a
  fast move, but on a paused frame you see a double exposure. That is by design.
- The phone push-in ends at ~2.2x upsampling of the 2K still, so the phone body/stand is soft at
  full zoom; the chat itself is rendered at frame resolution and is sharp.
- The end-card wall is slide 03's wall upscaled ~1.2x: plain wall, soft by nature.
- Outpainted margins are Nano Banana's; they show mostly during glides and at the frame edges.
  Slide 04's side walls have faint specks at full resolution (not noticeable in motion).
- Retouch: the small ceiling downlight in the row image (slide 09) sat exactly between "lot" and
  "to" in the close line and read like a hyphen; it is cloned out of the video canvas
  (`stage.py` `RETOUCH`). The carousel's slide 9 is unchanged.
- Two exhibit lines wrap with a one-word last line in 9:16 ("…throw them / away.") — left as is; it reads fine.
- A light film grain is added to every frame so the wall gradients don't band in H.264.
- Disclosure: on-screen on the end card ("The man who made this museum, with AI."; the small
  "Images made with AI" line was removed on 2026-11-19 to match the carousel); the caption should
  also say the images and the camera moves are AI/code-made; tick YouTube's altered/synthetic toggle.
- File sizes: the first 9:16 encode was 47.8 MB (over the 45 MB cap) because of the grain; grain was
  lowered and `-tune film` dropped, CRF stays 18.
- Not yet done: G2 critique, G3 brand review, cold-read, Sparsh's SHIP. Critic agreement on the
  gen-video exception is still owed (see above).
- 2026-11-19: v1 delivered to Sparsh (`out/museum-of-men-9x16.mp4`, 1080x1920, and
  `out/museum-of-men-4x5.mp4`, 1080x1350; 59.3 s, H.264/AAC, -14 LUFS).
  - The Showrunner reviewed the contact sheet and the artefact notes. One open point: the video
    end card still carries "Images made with AI", which Sparsh removed from the carousel end card.
    Asked whether to match.
- 2026-11-19: Sparsh: remove "Images made with AI" from the video end card. The v1 session was
  asked to re-render both cuts.
- 2026-11-19: Sparsh: v1 feels like "amateur animation over a slide show", not production
  quality. His reference: the Panditji New Year reel (`productions/2026-11-panditji-festive`).
  - Showrunner diagnosis: that reel is native motion graphics, where every element is drawn and
    animated in code and synced to the score. v1 animates flat raster stills in 2.5D, which
    always reads as "moving photos".
  - Options proposed: Veo 3.1 camera moves (Flow on Ultra credits, or the API with a spend cap),
    or a real 3D gallery in code (Three.js; risk: cut-out "cardboard" look). v1 is the backup.
- 2026-11-19: Sparsh chose **option B (Veo 3.1 in Flow on his Ultra credits)**.
  - `gpu-kit/FLOW-GUIDE.md` (8 clips C0-C7, first/last frame, prompts, settings, pick rules) is
    uploaded to Drive Post 6/video-gpu-kit. New subfolders: `flow-frames` (for 9:16 JPEG frames)
    and `flow-clips` (Sparsh drops C0-C7.mp4). The empty `frames` folder was moved to trash.
  - The 9:16 outpainted frames are being exported by the v1 session to `gpu-kit/flow-frames/`,
    then uploaded.
  - Fallback deadline: about 4 pm IST, after which the backup is posted.
- 2026-11-19: Flow start/end frames for Veo 3.1 Frames-to-Video exported to `gpu-kit/flow-frames/`
  by `export_flow.py`: 1080x1920 JPEG q92 (0.14-0.23 MB each), the outpainted 9:16 stage, no text,
  no grain, no parallax. `F0-row` (slide 09, the video's opening framing), `F1-exhibit1` ...
  `F7-exhibit7` (slides 02-08 at each exhibit's landed framing; F7 = phone, screen blank, no chat),
  `F8-endwall` (the end-card wall from slide 03, without the card).
