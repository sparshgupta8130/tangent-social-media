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
- Score: `score_v3.py` (v2.3, 2026-11-12): upbeat but smooth. v2 was rejected as "too jarring". Measured vs v1/v2:
  beat-pulse depth 14.2 dB (v1 2.8, v2 15.0); 3-10 kHz share 0.2% (v1 0.2, v2 1.0). Santoor hook + 16th arpeggio,
  rounded kick, soft snaps, pumping pad, 8th bass, gentle limiting. Previous, `score_v2.py`: upbeat bhangra-pop, dhol chaal + tumbi riff from frame 0, four-on-the-floor
  kick, offbeat bass and stabs from the phone landing, half-time break, final hit on bar 22. v1 (`score.py`) was rejected as
  too mellow. v1 was an original piece synthesised from scratch (tanpura drone, Karplus-Strong santoor in
  Raag Bhupali, pad, sub, kick, shaker, claps, risers, impacts). 96 BPM; every scene change sits on a bar line
  (bar = 2.5 s). No samples, no licensed audio.

## Screens (all real)
- Live captures from a local build of panditji main (Asha + Rohan fixture, API mocked offline):
  `capture.mjs` → today, plan, chart-vedic, chart-western, match (full-length), and the tab bars.
- Labs screenshot (real app, real AI reply): today-labs (the daily reading).
- Ask (v2.1, Sparsh 2026-11-12: "just mock it up with a sample"): `capture_ask.mjs` runs the live build with
  `/api/agent` mocked. The career answer is a written SAMPLE (the on-screen kicker says "Ask · sample
  conversation", as the Labs page labels its own); its first turn calls the real engine tools (get_dasha_at,
  get_chart), so the app computes Asha's actual values and draws its own "How I worked this out" row. Facts in
  the sample match those values (Saturn Mahadasha, Jupiter antardasha to Mar 2029, Saturn in own sign).
  The two refusals use the server's real canned replies from api/_lib/guard.ts, sent as `deflected` events.
- Replies are revealed top-to-bottom with a mask over the real screenshot (no text is drawn).

## Rebuild
1. `node capture.mjs <dir>` with the panditji build served on :4173 (`npx vite preview --port 4173`).
2. Put the captures, the Labs images, `grain.png`, `icon-512.png` and gsap@3.12.5 (`npm i gsap@3.12.5`) next to `launch.html`.
3. `node render_video.js launch.html frames 30` (frame-accurate: `render(t)` seeks a paused GSAP timeline).
4. `python score_v3.py score_raw.wav`; `ffmpeg -i score_raw.wav -af loudnorm=I=-14:TP=-1.0:LRA=9 score.wav` (lands at about -13.3 LUFS).
5. `ffmpeg -framerate 30 -i frames/f%05d.png -i score.wav -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4`.

## Limits, stated plainly
- The score was checked by spectrogram and loudness curve, not by ear (no audio playback in this environment).
  It is an original synthesised track, not a produced one; a Lyria/Flow Music pass (workload-router) or a
  track from YouTube's audio library is the upgrade path if it doesn't land.
- One Labs screenshot remains (Today's reading, Oct build, tab named "Timing"); everything else is the Nov build ("Plan").
