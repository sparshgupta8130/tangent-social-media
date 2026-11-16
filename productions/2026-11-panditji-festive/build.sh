#!/usr/bin/env bash
# Rebuild both reels from source. Needs: node + playwright-core (resolvable from render.mjs's folder, or copy it next to
# a node_modules that has it), Chrome, Python with numpy/scipy, and an ffmpeg (FFMPEG=…; imageio-ffmpeg's works).
set -euo pipefail
cd "$(dirname "$0")"
WORK=${WORK:-./_work}
FFMPEG=${FFMPEG:-$(python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")}
mkdir -p "$WORK" out
python -m http.server 8766 --bind 127.0.0.1 >/dev/null 2>&1 & SERVER=$!
trap 'kill $SERVER' EXIT
sleep 1
for name in diwali newyear; do
  secs=9; [ "$name" = newyear ] && secs=13.5   # the New Year reel runs at 80 BPM
  node render.mjs "$name.html" "$WORK/$name" frames "$secs" 30
  python score.py "$name" "$WORK/$name.wav"
  "$FFMPEG" -y -loglevel error -framerate 30 -i "$WORK/$name/f%04d.png" -i "$WORK/$name.wav" \
    -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 \
    -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -movflags +faststart \
    -c:a aac -b:a 192k -shortest "out/panditji-$name-reel.mp4"
  echo "built out/panditji-$name-reel.mp4"
done
