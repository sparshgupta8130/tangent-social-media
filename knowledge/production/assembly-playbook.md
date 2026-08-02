# Assembly Playbook — Capture → Cut → Export

Load before any `/produce` assembly pass. Source: July-2026 production-stack research brief
(`[stack-brief]` = `research/briefs/production_stack_2026-07.md`, tiered `[HIGH]`/`[MED]`/`[LOW]`/`[UNVERIFIED]`) plus safe-zone specs from
`knowledge/platform/instagram.md` §3.

## 1. Capture: OBS Studio + obs-websocket

**Programmatic start/stop**: OBS v28+ ships **obs-websocket natively** — no plugin install.
Connect over `localhost:4455`, authenticate, call `start_record()`/`stop_record()` (e.g. the
`obsws-python` library) from a Bash/Python step in the pipeline, tied to "Claude is about to
begin editing" [HIGH — OBS Forums]. This is deterministic and headless, unlike Xbox Game Bar,
which has **no CLI/API for programmatic start-stop** and is not recommended [MED, absence of any
scripting-interface documentation].

**Concrete settings**:
- Source: **Window Capture** on the Chrome/lightroom.adobe.com window (more stable than Display
  Capture — avoids capturing unrelated desktop chrome).
- Resolution: capture **native landscape** (1920×1080, or **1440p** if the operator's display
  runs 1440p) — **do not pre-crop to vertical at capture time**; reframe to 1080×1920 in post,
  since the Lightroom UI is laid out horizontally and cropping flexibility (picture-in-picture,
  panel zoom-ins) is needed for reel composition [HIGH].
- Frame rate: **30fps** — sufficient for UI/slider/cursor motion; 60fps only if a slow-motion
  speed-ramp on the screen-capture itself is planned.
- Encoder: **NVENC (h264_nvenc)** if an NVIDIA GPU is present, high bitrate (CQP ~18-20 or
  ≥20 Mbps for 1080p) for near-lossless quality, low CPU overhead [HIGH]. Fallback: raw ffmpeg
  `-f ddagrab -framerate 30 -i desktop -c:v h264_nvenc -b:v 20M output.mp4` (`ddagrab`/Desktop
  Duplication API handles high framerates more reliably than the older `gdigrab`, which cannot
  hold true 60fps) if avoiding the OBS dependency.
- **Audio off** during capture — the session's screen audio is not used in the final mix; VO/
  music are added in the assembly pass (§3).

## 2. Reframe-to-vertical strategy

Reframe in post, never at capture time. For each kept segment: identify where the *action* sits
(cursor position, the slider being dragged, the mask overlay rendering) and crop/pan the 1080-
wide window to follow it — the vertical frame should feel intentionally composed, not like a
cropped screenshot. Where the action moves across the frame (e.g., dragging from the Basic panel
to a mask), use a **pan** (`crop` with animated `x`/`y` via expressions) rather than a static
crop, so the 9:16 viewer's eye is led rather than left waiting outside the safe zone. Keep
critical UI/text out of the safe zones defined in `knowledge/platform/instagram.md` §3
(top ~250px / bottom ~350px / right ~10%) — that includes the reframed crop, not just caption
placement.

## 3. ffmpeg assembly — the primary path

**Why ffmpeg over the alternatives** [stack-brief §3]: fully CLI-scriptable, watermark-free, zero
extra subscription cost, and the fundamentals (concat, `setpts`/`atempo` speed-ramps, `ass`/
`drawtext` burned captions, `amix` for music, `libx264`/`h264_nvenc` export) are mature and
unchanged. DaVinci Resolve's scripting API is **Studio-edition-gated since v19.1 — the Free
edition cannot be scripted** [HIGH]; Premiere's ExtendScript is **frozen** (no further changes
planned, support only through ~Sept 2026) and its UXP replacement has real gaps (e.g., Time
Remapping reportedly inaccessible from both ExtendScript and UXP as of Premiere 26.3)
[MED/HIGH]. **Neither is our path** — noted for completeness only.

### Worked example: a typical 30s reel, 4 segments + captions + music

Assume four capture-derived source clips already trimmed to their in/out points:
`seg1.mp4` (0-9s, global adjustments), `seg2.mp4` (0-8s, mask draw-in, speed-ramped),
`seg3.mp4` (0-8s, before/after toggle), `seg4.mp4` (0-7s, critic-loop reject + fix), each
1920×1080 landscape source with the reframe-to-vertical crop already baked in via per-segment
`-vf "crop=1080:1920:x:y"` during trim (§2).

```bash
# 1. Speed-ramp seg2 (2x through the mask-draw, using setpts — no audio to time-stretch since
#    capture audio is off)
ffmpeg -i seg2_raw.mp4 -vf "setpts=0.5*PTS" -an seg2.mp4

# 2. Crossfade-concat all four segments (xfade, since the concat demuxer can't crossfade;
#    chained pairwise, 0.4s transition each, offsets computed from each clip's trimmed duration)
ffmpeg -i seg1.mp4 -i seg2.mp4 -i seg3.mp4 -i seg4.mp4 -filter_complex \
 "[0][1]xfade=transition=fade:duration=0.4:offset=8.6[v01]; \
  [v01][2]xfade=transition=fade:duration=0.4:offset=12.6[v012]; \
  [v012][3]xfade=transition=fade:duration=0.4:offset=19.6[vout]" \
 -map "[vout]" -c:v libx264 -crf 18 assembled_silent.mp4

# 3. Burn captions (pre-authored captions.ass, word-highlight style, positioned inside the
#    safe-zone margins from instagram.md §3 — top ~250px/bottom ~350px/right ~10% excluded)
ffmpeg -i assembled_silent.mp4 -vf "ass=captions.ass" -c:v libx264 -crf 18 captioned.mp4

# 4. Mix VO (if any) + music bed under it, duck music under VO with sidechaincompress, then
#    loudness-normalize the mixed track to -14 LUFS (social-platform loudness convention)
ffmpeg -i vo.wav -i music.mp3 -filter_complex \
 "[1:a]volume=0.3[music_low]; \
  [0:a][music_low]amix=inputs=2:duration=first:dropout_transition=2[premix]; \
  [premix]loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
 -map "[aout]" -c:a pcm_s16le mix.wav

# 5. Final mux + export: 1080x1920, H.264 High@4.2, yuv420p, CRF 18-20, AAC 192k
ffmpeg -i captioned.mp4 -i mix.wav -map 0:v -map 1:a \
 -vf "scale=1080:1920" -c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p -crf 19 \
 -c:a aac -b:a 192k -movflags +faststart \
 ops/pipeline/NNN-slug/exports/NNN-slug_v1.mp4
```

Adjust CRF within 18-20 (lower = higher quality/larger file) per shot content; `-movflags
+faststart` keeps the file streamable for upload. The `-14 LUFS` target is a social-platform
loudness convention, not a platform-documented hard requirement — treat as **[MED, practitioner
convention]**, not an official spec.

## 4. Final-export rule

**`tools/hygiene_check.py` must PASS on the FINAL export before it can reach G2 or `publish.md`**
— `python tools/hygiene_check.py <final-export> --platform ig|yt|yt-long`. Checks: resolution
≥1080×1920 and 9:16 aspect for `ig`/`yt` (≥1920×1080 and 16:9 for `yt-long`), H.264/AAC,
yuv420p, duration in-band per platform, audio stream present, black-border detection
(cropdetect), and the repost guard (SHA256 not already in
`ops/pipeline/.published_hashes.json`). Any FAIL blocks G2 — rerun after every re-export, not
just once. This is a hard gate per `SYSTEM_DESIGN.md` §5, not a suggestion.

## 5. File naming + export location

Exports live at `ops/pipeline/NNN-slug/exports/`. Name each export `NNN-slug_vN.mp4`
(incrementing `vN` per re-export/fix round — never overwrite a prior version in place, since the
repost-guard hash and any critic notes reference a specific file). The file passed to
`tools/pipeline.py publish NNN --url <url> --video <path>` must be the exact final-export path
that passed hygiene_check, so the repost-guard hash matches what's actually live.
