# Panditji launch Short (v2, motion piece)

Replaces the slideshow cut (`../carousel/video/panditji-short.mp4`), which Sparsh rejected 2026-11-12:
"slides 3 to 8 have the exact same animation… looks like a slide show". Brief: a polished product-launch
video with a background score.

## What it is
- 1080×1920, 30 fps, 58 s, H.264 + AAC 48 kHz, ~-14 LUFS. Output: `panditji-launch-short.mp4`.
- One continuous phone for the whole film (no slide cuts): it rises in, its screen swipes between real app
  pages, the camera pushes in on the starred day and the Gun Milan score, it turns edge-on to change from the
  Vedic kundli to the Western wheel, drops away for the "it says no" break and comes back tilted.
- Kinetic type: masked word-by-word headline reveals, a rolling "Vedic. / Western." word, a typed URL.
- Score: `score.py`, an original piece synthesised from scratch (tanpura drone, Karplus-Strong santoor in
  Raag Bhupali, pad, sub, kick, shaker, claps, risers, impacts). 96 BPM; every scene change sits on a bar line
  (bar = 2.5 s). No samples, no licensed audio.

## Screens (all real)
- Live captures from a local build of panditji main (Asha + Rohan fixture, API mocked offline):
  `capture.mjs` → today, plan, chart-vedic, chart-western, match (full-length), and the tab bars.
- Labs screenshots (real app, real AI replies): today-labs (the reading), ask-top, ask-limits.
  The Ask screens can't be captured locally because the AI relay is offline here.
- Ask replies are revealed top-to-bottom with a cream mask over the real screenshot (no text is drawn).

## Rebuild
1. `node capture.mjs <dir>` with the panditji build served on :4173 (`npx vite preview --port 4173`).
2. Put the captures, the Labs images, `grain.png`, `icon-512.png` and gsap@3.12.5 (`npm i gsap@3.12.5`) next to `launch.html`.
3. `node render_video.js launch.html frames 30` (frame-accurate: `render(t)` seeks a paused GSAP timeline).
4. `python score.py score_raw.wav`; `ffmpeg -i score_raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=11,volume=-1.2dB score.wav`.
5. `ffmpeg -framerate 30 -i frames/f%05d.png -i score.wav -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4`.

## Limits, stated plainly
- The score was checked by spectrogram and loudness curve, not by ear (no audio playback in this environment).
  It is an original synthesised track, not a produced one; a Lyria/Flow Music pass (workload-router) or a
  track from YouTube's audio library is the upgrade path if it doesn't land.
- Mixed builds: Labs screenshots (Oct, tab named "Timing") and live captures (Nov, tab named "Plan").
