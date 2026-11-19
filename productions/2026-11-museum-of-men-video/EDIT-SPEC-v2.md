# Edit spec v2: Museum of Men video with Flow (Veo 3.1) clips

Goal: a polished ~60-75 s film. Real Veo camera moves (Sparsh's Flow clips) carry the motion. Our
code adds every piece of text, the phone chat animation, the end card and the original score.
Masters: 9:16 1080x1920 (YouTube Shorts) and 4:5 1080x1350 (LinkedIn), 30 fps, H.264 High CRF
~18, AAC 192k, -14 LUFS, <= -1 dBTP, under 45 MB each.

## Inputs
- `flow-clips/C0.mp4` … `C6.mp4` (720x1280, 24 fps, ~7.9 s each). Read `flow-clips/NOTES.md`.
  - **C0 is used RAW.** No repair of its generated motion; `C0-fixed`, `C0-trim` and
    `C0-cut-preview` are rejected and must not be used.
  - **C2 is cut at ~5.6 s**, before the zoom and lighting snap.
  - Normal editing is allowed on every clip: trims, speed-ramping the empty-wall middles
    (≤1.6x, eased), holds (freeze the last good frame with a very slow push-in).
- Upscale 720p → 1080x1920 with a high-quality scaler (lanczos plus a light unsharp). Add light
  grain to stop banding.
- `gpu-kit/flow-frames/F0-row.jpg` (row still) and `F8-endwall.jpg` (end-card wall).
- Copy: `../2026-11-museum-of-men/carousel.md`, **verbatim**. Typography and colours are as in
  the carousel (`../2026-11-museum-of-men/build_square.mjs`): Fraunces headlines, Inter small-caps
  exhibit label, muted #7a6650, ink #1d1a16.

## Change (Sparsh, 2026-11-19, after a failed C0 retake): DROP C0 ENTIRELY
F0 and F1 show contradictory rooms (a row vs a lone plinth), so no Veo move connects them.
- New opening: the row still (F0) with a subtle push-in plus the title for about 3 s.
- Then a hard cut to exhibit 1 (C1's opening frames), held 3-3.5 s with its label and line.
- Then C1 carries the move to exhibit 2.

## Timeline
1. **Open (~3 s):** C0's opening (the row) with the title fading in and out: "The Museum of Men" /
   "Things men never throw away". Then C0 continues (raw) into exhibit 1.
2. **Exhibits 1-6:** each lands at the end of its clip, then a ~3-3.5 s hold with label + line
   fading in (Exhibit 1 The cable drawer … Exhibit 6 The remote, lines exactly as carousel slides
   2-7). Then the next clip: C1 (1→2), C2 cut at 5.6 s (2→3), C3 (3→4), C4 (4→5), C5 (5→6),
   C6 (6→phone).
3. **Phone (~9-10 s), the turn.** C6 lands on the phone (blank screen). Track/composite a chat UI
   onto the screen; it must stay readable on a phone, so a slow push-in toward it is allowed.
   - Header "Rahul / online". The incoming bubble "How are you, bro? 🙂" appears.
   - In the input box, type out letter by letter: "Honestly bro, I'm not doing good." Hold about
     1 s.
   - Backspace it letter by letter (faster).
   - Type "All good, bro 👍", tap send. It becomes a sent green bubble with ticks.
   - On-screen label "Exhibit 7 · His phone". The headline reads "What he typed." while drafting
     and crossfades to "What he sent." at the send.
   - Chat styling as in carousel slides 8/9 (`build_square.mjs` PHONE_CSS).
4. **Close (~5 s):** hard cut to the row (`F0-row.jpg`) with a slow push-out (still image; the
   Flow pull-back failed). Light text with shadow: "Some things men keep are worth throwing out.
   Start with "All good, bro."", then the small line "Today, ask one how he's really doing."
5. **End card (~5 s):** dissolve to `F8-endwall.jpg`. Wall lettering "Happy International
   Men's Day" plus the maker card ("EXHIBIT 8 · THE MAKER / The man who made this museum, with AI.
   / Follow him for more art, apps and stories." plus the 4 handles). **No "Images made with AI"
   line.** Fade out.

## Audio
Original only: adapt `score.py` (felt piano + pad, ~70 BPM).
- Lift at the phone.
- A soft key-click texture while typing and deleting (synthesised, quiet).
- Space on the cut to the row, resolve on the end card.
- Quiet room tone.

## Safe zones and checks
- Text stays inside the Shorts-safe area (avoid the top 220 px and bottom 380 px in 9:16). Make a
  proper 4:5 re-composite, not a dumb crop.
- Self-review frame by frame at every clip boundary and hold. Check copy against carousel.md
  (typos).
- Save `out/museum-of-men-v2-9x16.mp4`, `out/museum-of-men-v2-4x5.mp4` and
  `out/contact-sheet-v2.jpg`. Keep v1 files.
