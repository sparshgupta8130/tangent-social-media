"""v2 (Flow): register the original still slide-08.png to C6's landed frame (F-space, 1080x1920).

    python v2_register.py      -> v2_s8_homography.npy (slide-08 px -> F-space px)
SIFT + ratio test + RANSAC homography. Used by v2_build.py for the push-in to the phone: at the freeze, the
picture switches to the registered, colour-matched original (1.6x the resolution of the Flow frame).
"""
import os
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(os.path.join(HERE, 'flow-clips', 'C6.mp4')); cap.set(cv2.CAP_PROP_POS_FRAMES, 165)
c6 = cv2.resize(cap.read()[1], (1080, 1920), interpolation=cv2.INTER_LANCZOS4)
s8 = cv2.imread(os.path.join(HERE, '..', '2026-11-museum-of-men', 'assets', 'gen', 'pick', 'slide-08.png'))
k = 0.62
s8s = cv2.resize(s8, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
sift = cv2.SIFT_create(4000)
ka, da = sift.detectAndCompute(cv2.cvtColor(s8s, cv2.COLOR_BGR2GRAY), None)
kb, db = sift.detectAndCompute(cv2.cvtColor(c6, cv2.COLOR_BGR2GRAY), None)
good = [m for m, n in cv2.BFMatcher().knnMatch(da, db, k=2) if m.distance < 0.75 * n.distance]
pa = np.float32([ka[m.queryIdx].pt for m in good]); pb = np.float32([kb[m.trainIdx].pt for m in good])
H, inl = cv2.findHomography(pa, pb, cv2.RANSAC, 2.0)
H = H @ np.diag([k, k, 1.0])
print(len(good), 'matches,', int(inl.sum()), 'inliers'); print(H.round(5))
np.save(os.path.join(HERE, 'v2_s8_homography.npy'), H)

# C2 is cut at 5.6 s mid-zoom (Sparsh). Its hold continues that zoom in code and lands on C3's opening framing,
# so the cut to C3 matches. Similarity C2 frame 134 (5.58 s) -> C3 frame 0, in 720p clip px.
def frame(c, i):
    cap = cv2.VideoCapture(os.path.join(HERE, 'flow-clips', c + '.mp4')); cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    return cap.read()[1]


a, b = frame('C2', 134), frame('C3', 0)
ka, da = sift.detectAndCompute(cv2.cvtColor(a, cv2.COLOR_BGR2GRAY), None)
kb, db = sift.detectAndCompute(cv2.cvtColor(b, cv2.COLOR_BGR2GRAY), None)
good = [m for m, n in cv2.BFMatcher().knnMatch(da, db, k=2) if m.distance < 0.75 * n.distance]
pa = np.float32([ka[m.queryIdx].pt for m in good]); pb = np.float32([kb[m.trainIdx].pt for m in good])
M, inl = cv2.estimateAffinePartial2D(pa, pb, ransacReprojThreshold=2.0)
s = float(np.hypot(*M[0, :2])); t = M[:, 2]
p = t / (1 - s)                     # zoom about a fixed point p: x' = p + s (x - p)
w = cv2.warpAffine(a, M, (720, 1280), flags=cv2.INTER_LANCZOS4)
reg = (slice(80, 560), slice(80, 640))   # the wall: per-channel gain C2 -> C3
gain = b[reg].reshape(-1, 3).mean(0) / w[reg].reshape(-1, 3).mean(0)
print('C2->C3 scale', round(s, 4), 'fixed point', p.round(1), 'gain BGR', gain.round(3), int(inl.sum()), 'inliers')
np.save(os.path.join(HERE, 'v2_c2c3.npy'), np.array([s, p[0], p[1], *gain]))
