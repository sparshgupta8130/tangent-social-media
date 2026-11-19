# Make 8 camera-move clips in Google Flow (Veo 3.1): about 20-30 minutes

Use the 9:16 frames in `flow-frames/`.
- **F0** = the row of plinths.
- **F1 to F7** = exhibits 1-7. F7 is the phone with a blank screen.

Each clip **starts on one frame and ends on the next**. I cut them together and add all the text,
the phone chat and the music, so **don't add any text**, and ignore Flow's audio.

## Setup (once)
1. Open Flow (labs.google/flow), signed in with your Google AI Ultra account, and start a new project.
2. Pick **Frames to Video** (first and last frame).
3. Settings:
   - Model: **Veo 3.1 Quality**. Use Fast only for a quick test.
   - Aspect: **9:16** (portrait).
   - Outputs per prompt: **2**, so you can pick the better one.

## The 8 clips
For each row: set the **first frame**, set the **last frame**, paste the prompt plus the STYLE line, then generate.

| Clip | First frame | Last frame | Prompt |
|---|---|---|---|
| C0 | F0-row | F1-exhibit1 | Slow smooth forward dolly down the gallery toward the nearest plinth, settling on the drawer of cables. |
| C1 | F1-exhibit1 | F2-exhibit2 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C2 | F2-exhibit2 | F3-exhibit3 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C3 | F3-exhibit3 | F4-exhibit4 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C4 | F4-exhibit4 | F5-exhibit5 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C5 | F5-exhibit5 | F6-exhibit6 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C6 | F6-exhibit6 | F7-exhibit7 | Smooth lateral camera track to the right along the gallery wall, from one plinth to the next. |
| C7 | F7-exhibit7 | F0-row | Slow smooth pull-back and rise, revealing the whole row of plinths down the gallery. |

**STYLE line (paste after every prompt):**
Calm, premium museum film. Steady gimbal camera, slow eased motion, soft warm gallery spotlights,
no people, no text, no new objects, no flicker, photorealistic.

## Pick and send back
- **Keep a take only if:**
  - objects don't melt, warp or change shape mid-move;
  - the number of plinths stays the same;
  - no text appears;
  - there's no flicker;
  - it ends close to the last frame.
- If both takes fail, regenerate once. If it still fails, skip that clip. I'll fall back to the
  smooth glide we already have for that one transition.
- **Download** each kept clip at the highest resolution offered (1080p if available) and name
  them `C0.mp4` … `C7.mp4`.
- **Upload** them to the `flow-clips` folder next to this guide in Google Drive, then tell me.

From there I do the edit:
- hold each exhibit 3-4 s with its line;
- the phone chat types out on exhibit 7;
- the close line on the row, then the end card;
- the original score;
- the 9:16 cut for YouTube and a 4:5 cut for LinkedIn.

The current video stays as the backup. If this isn't done and good by about **4 pm IST**, post
the backup and keep these clips for a re-cut.
