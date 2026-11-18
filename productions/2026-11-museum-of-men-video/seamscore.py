"""Seam score of an outpaint: how visible the photo's rectangle is in the RAW generated image
(median abs step across the border, 8 px out vs 8 px in, on a blurred copy). Lower = better."""
import sys, glob, cv2, numpy as np
CW, OX, OY = 3300, 722, 498
def score(f):
    g = cv2.GaussianBlur(cv2.resize(cv2.imread(f), (CW, CW), interpolation=cv2.INTER_AREA).astype(np.float32), (0, 0), 3)
    x0, x1, y0, y1, o = OX, OX + 1856, OY, OY + 2304, 10
    st = [np.abs(g[y0 - o, x0:x1] - g[y0 + o, x0:x1]), np.abs(g[y1 - o, x0:x1] - g[y1 + o, x0:x1]),
          np.abs(g[y0:y1, x0 - o] - g[y0:y1, x0 + o]), np.abs(g[y0:y1, x1 - o] - g[y0:y1, x1 + o])]
    return float(np.median(np.concatenate([s.mean(1) for s in st])))
if __name__ == '__main__':
    for f in sorted(glob.glob('work/gen/*.jpg')):
        print(f.split('/')[-1], round(score(f), 2))
