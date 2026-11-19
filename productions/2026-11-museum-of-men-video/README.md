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
- 2026-11-19: 9:16 Flow frames F0-F8 uploaded to Drive video-gpu-kit/flow-frames (sizes match
  local). Sparsh doesn't want to read the guide; the Showrunner walks him through Flow
  step by step in chat.

## v2 (Flow), 2026-11-19

Built to `EDIT-SPEC-v2.md` from Sparsh's Veo 3.1 Frames-to-Video clips C1-C6 (`flow-clips/`, C0 dropped per the spec change;
720x1280, 24 fps). Autonomous run for this task only; no paid APIs, no new generation.

**Outputs (`out/`):** `museum-of-men-v2-9x16.mp4` (1080x1920, YouTube Shorts) and `museum-of-men-v2-4x5.mp4`
(1080x1350, LinkedIn), both 75.84 s, 30 fps, H.264 High CRF 18 yuv420p, AAC 192 kb/s 48 kHz, `+faststart`;
`contact-sheet-v2.jpg` (24 moments). 9:16 = 35.9 MB, 4:5 = 26.3 MB; both −14.0 LUFS integrated, −2.4 dBTP
(ffmpeg ebur128). v1 files are kept. Render time ≈ 7 min (9:16) + 5.5 min (4:5) on 3 CPU workers.

**Re-render (from this folder):**
1. `python v2_register.py` – SIFT+RANSAC: `v2_s8_homography.npy` (slide-08.png -> C6's landed frame) and
   `v2_c2c3.npy` (C2 at 5.58 s -> C3's first frame: zoom 1.216 about (516, 560), per-channel wall gain).
2. `node v2_overlays.mjs` – Playwright: text layers per format (`v`, `p`) + 87 chat-screen states.
3. `python v2_build.py v` / `python v2_build.py p` – picture -> `work/v2/video-{v,p}.mp4`
   (`--stills 12.0,61.5 --out DIR` for review stills; env `GRAIN`, `CRF`).
4. `python v2_score.py work/v2/score.wav` – the score. 5. `python v2_mux.py` – out/ files + contact sheet.
`v2_timeline.py` holds every cue (prints the timeline when run). `work/` is gitignored.

**Spec change applied (Sparsh, 2026-11-19, `EDIT-SPEC-v2.md` "Change"): C0 is dropped entirely.** No C0 frame
appears anywhere. The film opens on the row still and hard-cuts to exhibit 1. Row still = `gpu-kit/flow-frames/F0-row.jpg`
from commit **f2e9053** (row-v3, objects matching the exhibits: dark-wood drawer with black/white chargers, scuffed
phone box with its tray). It is a single swappable input: replace the file and re-run steps 3-5.

**Timeline (s; 72 BPM grid, beat 0 = the cut to exhibit 1; every landing and move start is on an 8th-note):**

| Time | What |
|---|---|
| 0.00–3.33 | Row still, very slow push-in (1.00 → 1.03, about its top edge). Title in 0.30–1.00, out 2.45–3.10 |
| 3.33 | **Hard cut** to exhibit 1 = C1's first frame (on the beat) |
| 3.33–6.67 | Hold, exhibit 1 (label + line in from 3.53) |
| 6.67–13.34 | C1 (middle 1.4–6.0 s src sped up, eased, peak 1.43x) |
| 13.34–16.25 | Hold, exhibit 2 |
| 16.25–21.25 | C2, played to **5.58 s** (frame 134) only, peak 1.32x |
| 21.25–24.17 | Hold, exhibit 3: C2's zoom carried on in code (ease-out) to C3's opening framing; text out before the cut |
| 24.17 | **Hard cut** C2 → C3 (matched framing and wall colour) |
| 24.17–29.17 | C3 (peak 1.54x) · 29.17–32.09 hold, exhibit 4 |
| 32.09–38.34 | C4 (peak 1.60x) · 38.34–41.25 hold, exhibit 5 |
| 41.25–47.09 | C5 (peak 1.31x) · 47.09–50.01 hold, exhibit 6 |
| 50.01–55.84 | C6 (peak 1.49x), lands on the phone |
| 55.84–65.84 | Exhibit 7: push-in 0–3 s to the screen; UI wakes +0.55; "How are you, bro? 🙂" +1.35; types "Honestly bro, I'm not doing good." +2.25–4.71; holds 1 s; backspaces +5.71–6.91 (accelerating, like a held key); types "All good, bro 👍" +7.33–8.50; send +8.92 → green bubble with ticks, "What he typed." crossfades to "What he sent." |
| 65.84 | **Hard cut** to the row still, slow push-out 1.12 → 1.04 (about its top edge); close line in at 66.29 |
| 70.29–70.84 | Close text fades out (it never overlaps the end-card text) |
| 70.84–72.04 | Dissolve to `F8-endwall.jpg`; wall lettering + maker card fade in 71.59–72.49 (no "Images made with AI" line) |
| 74.84–75.84 | Fade to black |

**How the motion is handled (settings):**
- **All camera motion is Veo's.** Code adds only: speed-ups of the empty-wall middles (≤1.6x, 0.6 s eased
  ramps; each clip's factor solved so its length is a whole number of 8th-notes), holds, and the phone push-in.
- **24 → 30 fps:** DIS optical-flow in-betweens (flow at 360x640, bidirectional warp + blend). The jump scan
  over every frame of the 9:16 master finds only the three intended hard cuts (3.33, 24.17, 65.84 s), in both formats. Each move keeps an even frame cadence,
  with no duplicate frames and no judder.
- **Holds:** freeze on the clip's landed frame (Veo's tails are static by then) with a 1.00 → 1.04 eased
  push-in about the exhibit. The push eases back out across the next move, so nothing jumps. Clip N's landed frame and clip N+1's first
  frame are the same framing (mean abs diff 1.3–2.9/255; ). Inside the hold the two
  are blended over 0.6 s while static, so the next move starts from its own first frame. That blend is between
  the same framing, never between camera angles.
- **C2 → C3:** C2 is cut at 5.58 s, mid-zoom (Sparsh's call: before the zoom and the lighting snap). Freezing there would
  stop a fast zoom dead, so the hold continues that zoom in code (ease-out, starting near C2's own rate) and
  lands exactly on C3's opening framing, while the wall colour eases to C3's (gain B 0.975, G 0.944, R 0.924).
  The hard cut then keeps the plinth and keys in place. Only the back wall/floor line shifts.
- **The phone:** at the C6 freeze the picture switches, invisibly, to the original still `slide-08.png`,
  registered to C6's frame (homography) and colour-matched at low frequencies. It has 1.6x the pixels of the
  Flow frame, so the push-in (screen 106 px → 430 px wide in 9:16, 400 px in 4:5) stays clean. The chat
  is rendered by Playwright at 2.2x and warped onto the screen quad every frame, so it is pixel-sharp. Notch redrawn.
- **Scaling:** one Lanczos4 resample per frame (720p → 1080 x camera), unsharp 0.35 @ σ1.1, luma grain
  (σ≈0.4 levels after blur) against banding.
- **4:5** is a re-composite, not a crop of the 9:16: its own text layout and margins, its own vertical window,
  its own phone framing, and the row sits lower in the close so the line clears the far plinths.
- Text safe area (9:16): all text between y 262 and ~1460 (outside the top 220 / bottom 380 px).

**Audio (`v2_score.py`, original, synthesised, no samples):** felt piano + pad, 72 BPM in D, on the
picture's beat grid.
- Each exhibit's chord lands with it (Dmaj9 Bm9 Gmaj7 Aadd4 Dmaj9 Bm9), with a quiet 8th-note arpeggio.
- The lift at the phone: Em9 F#m7 Gadd9 Asus, higher voicing, pad swell. The arpeggio drops out while he
  deletes the draft, leaving one low note.
- Synthesised key clicks under typing and deleting, about 16 dB under the music's peaks, and a soft tap on send.
- Space on the cut to the row; resolves to D on the end card. Room tone throughout, plus faint air under each move.
- Master: −14.0 LUFS integrated, −2.4 dBTP. The Veo clips' own audio tracks are not used.

**Honest notes:**
- **Length is 75.8 s,** a hair over the spec's ~60–75 s. It is set by ~3 s holds, a 10 s phone, a 5 s close
  and a 5 s end, with speed-ups capped at 1.6x in the empty middles.
- **Row layout (new row image):** the row-v3 still has a short wall (the row starts ~y 530 of 1920), so the
  title and close sit high: 9:16 text from y 232/240, inside the 220 px Shorts margin. The row camera zooms
  about the image's top edge, so the row only grows downward, away from the text. In 4:5 the window shows the
  top of the row (phone → keys/box), and the drawer at the front is cropped out of the open and close shots.
- **The opening hard cut** goes from the dark, warm row to the bright exhibit-1 wall. That is a big
  brightness change by design (the spec's hard cut); it lands on beat 4 with the first chord.
- **The C2→C3 cut is the one visible edit inside the gallery.** The keys stay put, but the wall/floor line
  behind them jumps up, because Veo's F3 framing has a different camera height. It reads as a cut, not a glitch, at
  normal speed. During the hold the C2 frame is magnified up to 1.22x (≈1.8x from 720p), so it is
  softer than the C3 shot it cuts to.
- The empty-wall stretches are Veo's soft 720p walls and floor upscaled 1.5x. They are clean, but not 1080-native detail.
- At full zoom the phone and stand are the original still at ~2.6x, slightly soft. The chat is sharp.
- The chat keeps the carousel's styling (grey send button). Additions: a notch, a pressed state on the
  send button, and a cursor that blinks only while idle.
- File-size fix: the first full encode had heavier grain and came out 95 MB / 68 MB, over the 45 MB cap. Grain was lowered after a 6x-contrast
  banding check showed no visible difference; CRF stays 18.
- Not done (out of scope for this task): G2 critique, G3 brand review, cold-read, Sparsh's SHIP.
