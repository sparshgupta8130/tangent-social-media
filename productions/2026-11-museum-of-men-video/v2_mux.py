"""v2 (Flow): mux picture + score into out/, then the contact sheet.

    python v2_mux.py
-> out/museum-of-men-v2-9x16.mp4, out/museum-of-men-v2-4x5.mp4 (H.264 High CRF 18 yuv420p, AAC 192k, +faststart)
-> out/contact-sheet-v2.jpg (24 moments from the final 9:16 file, 3 rows of 8)
"""
import os, subprocess
import cv2, numpy as np
import v2_timeline as T

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W = lambda *p: os.path.join(HERE, 'work', 'v2', *p)

for fmt, name in (('v', 'museum-of-men-v2-9x16.mp4'), ('p', 'museum-of-men-v2-4x5.mp4')):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', W(f'video-{fmt}.mp4'), '-i', W('score.wav'),
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
                    '-shortest', '-movflags', '+faststart', os.path.join(OUT, name)], check=True)
    print('wrote', name, round(os.path.getsize(os.path.join(OUT, name)) / 1e6, 1), 'MB')

L, L7 = T.LAND, T.L7
ts = [1.6, 5.0, L[1] + 1.2, (L[1] + L[2]) / 2 + 2, L[2] + 1.2, L[3] - 1.5, L[3] + 1.2, L[4] + 1.2,
      (L[4] + L[5]) / 2, L[5] + 1.2, L[6] + 1.2, (L[6] + L7) / 2 + 1, L7 + 0.2, L7 + 1.6, L7 + 3.6, L7 + 5.4,
      L7 + 6.4, L7 + 8.2, L7 + 9.6, T.CUT + 1.0, T.CUT + 3.5, T.END0 + 0.6, T.END0 + 2.5, T.TOTAL - 1.4]
cap = cv2.VideoCapture(os.path.join(OUT, 'museum-of-men-v2-9x16.mp4'))
tiles = []
for t in ts:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * T.FPS)))
    ok, f = cap.read()
    f = cv2.resize(f, (270, 480), interpolation=cv2.INTER_AREA)
    cv2.putText(f, f'{t:04.1f}s', (8, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2, cv2.LINE_AA)
    tiles.append(f)
sheet = np.vstack([np.hstack(tiles[i:i + 8]) for i in (0, 8, 16)])
cv2.imwrite(os.path.join(OUT, 'contact-sheet-v2.jpg'), sheet, [cv2.IMWRITE_JPEG_QUALITY, 90])
print('contact sheet done')
