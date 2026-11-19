"""Export the 9:16 stage frames for Google Flow (Veo 3.1 Frames-to-Video), no text, no grain.

    python export_flow.py   -> gpu-kit/flow-frames/F0-row.jpg ... F8-endwall.jpg (1080x1920, JPEG q92)
Framing = the video's own: F0 = the row's opening frame; F1..F7 = each exhibit's landed frame
(F7 = the phone at gallery framing, screen blank, no chat overlay); F8 = the end-card wall without the card.
Parallax is zeroed, so these are the outpainted canvases exactly as staged.
"""
import os
import cv2, numpy as np
import build as B

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'gpu-kit', 'flow-frames'); os.makedirs(OUT, exist_ok=True)
B.load('v')


def still(cam):
    cam.pz = cam.tx = cam.sx = 0.0
    n, cam.n = cam.n, cam.n
    if n == 8:  # no chat overlay: blank screen
        cam.n = -8
        B.A['canvas'][-8], B.A['depth'][-8] = B.A['canvas'][8], B.A['depth'][8]
    return np.clip(B.render_cam(cam) + 0.5, 0, 255).astype(np.uint8)


shots = [('F0-row', B.row_intro_cam('v', 0.0))]
for i in range(1, 8):
    shots.append((f'F{i}-exhibit{i}', B.ex_cam('v', i, B.ARR[i - 1])))
shots.append(('F8-endwall', B.end_cam('v', B.END_D1)))
for name, cam in shots:
    f = os.path.join(OUT, name + '.jpg')
    cv2.imwrite(f, still(cam), [cv2.IMWRITE_JPEG_QUALITY, 92])
    print(name, round(os.path.getsize(f) / 1e6, 2), 'MB')
