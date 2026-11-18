"""Step 6: mux video + score into out/, then make the cover and the contact sheet.

    python mux.py
-> out/museum-of-men-9x16.mp4, out/museum-of-men-4x5.mp4 (H.264 High CRF 18 yuv420p, AAC 192k, +faststart)
-> out/cover-9x16.jpg (frame at 1.6 s: the row with the title), out/contact-sheet.jpg (16 frames, 9:16)
"""
import os, subprocess
import cv2, numpy as np
import build as B

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W = lambda *p: os.path.join(HERE, 'work', *p)
run = lambda *a: subprocess.run(a, check=True)

for fmt, name in (('v', 'museum-of-men-9x16.mp4'), ('p', 'museum-of-men-4x5.mp4')):
    run('ffmpeg', '-y', '-loglevel', 'error', '-i', W(f'video-{fmt}.mp4'), '-i', W('score.wav'),
        '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
        '-shortest', '-movflags', '+faststart', os.path.join(OUT, name))
    print('wrote', name, round(os.path.getsize(os.path.join(OUT, name)) / 1e6, 1), 'MB')

# cover: re-render the title frame losslessly (not from the H.264 stream)
B.load('v')
cv2.imwrite(os.path.join(OUT, 'cover-9x16.jpg'), B.frame(int(1.6 * B.FPS)), [cv2.IMWRITE_JPEG_QUALITY, 93])

# contact sheet: 16 moments across the cut, from the final 9:16 file
ts = [1.6, 4.4, 5.8, 8.5, 10.9, 13.8, 19.0, 24.3, 29.6, 34.9, 38.7, 43.5, 46.6, 50.0, 52.4, 57.0]
tiles = []
cap = cv2.VideoCapture(os.path.join(OUT, 'museum-of-men-9x16.mp4'))
for t in ts:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * B.FPS)))
    ok, f = cap.read()
    f = cv2.resize(f, (270, 480), interpolation=cv2.INTER_AREA)
    cv2.putText(f, f'{t:04.1f}s', (8, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2, cv2.LINE_AA)
    tiles.append(f)
sheet = np.vstack([np.hstack(tiles[i:i + 8]) for i in (0, 8)])
cv2.imwrite(os.path.join(OUT, 'contact-sheet.jpg'), sheet, [cv2.IMWRITE_JPEG_QUALITY, 90])
print('cover + contact sheet done')
