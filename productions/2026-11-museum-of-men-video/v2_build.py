"""v2 (Flow): render the picture from the Veo 3.1 clips + code-rendered text, chat, end card.

    node v2_overlays.mjs                       # text + chat PNGs first
    python v2_build.py v                       # 9:16 1080x1920 -> work/v2/video-v.mp4
    python v2_build.py p                       # 4:5 1080x1350  -> work/v2/video-p.mp4
    python v2_build.py v --stills 7.5,62.0 --out DIR   # review stills (PNG, no grain)

Motion comes from the Flow clips. Code only adds: 24->30 fps (DIS optical-flow in-betweens), the eased
speed-ups of empty-wall middles (v2_timeline.py), the holds (freeze of the landed frame + very slow
push-in, eased back out during the next move), the push-in to the phone (switching, at the freeze, to the
registered + colour-matched original still slide-08.png for resolution), the chat (Playwright PNGs warped
onto the screen), the close (F0-row.jpg, slow push-out) and the end card (F8-endwall.jpg).
Single resample per frame: source -> output with Lanczos4, then a light unsharp and light grain.
"""
import os, sys, json, subprocess
from multiprocessing import Pool
import cv2, numpy as np
import v2_timeline as T

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPDIR = os.path.join(HERE, 'flow-clips')
OV = os.path.join(HERE, 'work', 'v2', 'overlays')
S8 = os.path.join(HERE, '..', '2026-11-museum-of-men', 'assets', 'gen', 'pick', 'slide-08.png')
F0 = os.path.join(HERE, 'gpu-kit', 'flow-frames', 'F0-row.jpg')
F8 = os.path.join(HERE, 'gpu-kit', 'flow-frames', 'F8-endwall.jpg')
FMT = {'v': dict(W=1080, H=1920, c0=(540.0, 960.0), scr_w=430, scr_c=(540.0, 1000.0)),
       'p': dict(W=1080, H=1350, c0=(540.0, 1050.0), c0_row=(540.0, 900.0), scr_w=400, scr_c=(540.0, 760.0))}
# F-space = the 1080x1920 frame of a Flow clip upscaled 1.5x. Hold push-in anchor (the exhibit) in F-space:
ANCHOR = (540.0, 1215.0)
HOLD_PUSH = 1.04
# slide-08 -> F-space homography (SIFT + RANSAC against C6's landed frame; see README v2)
H_S8 = None
SCREEN_SRC = (848, 1155, 1008, 1486)   # phone screen in slide-08 px (matches v2_overlays.mjs)
XFADE_HOLD = (1.0, 0.6)
GRAIN = float(os.environ.get('GRAIN', '1.0'))   # light luma grain (anti-banding), px std after blur ~0.55*GRAIN
CRF = os.environ.get('CRF', '18')                # within a hold: landed frame of clip N -> frame 0 of clip N+1 (same framing)

ease = T.smooth


# ---------------------------------------------------------------- sources
class Clips:
    def __init__(self):
        self.cache, self.flow = {}, {}

    def frames(self, c):
        if c not in self.cache:
            if len(self.cache) >= 1:
                old = next(iter(self.cache)); del self.cache[old]
                self.flow = {k: v for k, v in self.flow.items() if k[0] != old}
            cap, fs = cv2.VideoCapture(os.path.join(CLIPDIR, c + '.mp4')), []
            while True:
                ok, f = cap.read()
                if not ok:
                    break
                fs.append(f)
            self.cache[c] = fs
        return self.cache[c]

    def first(self, c):
        """Frame 0 of clip c without caching the whole clip."""
        if c in self.cache:
            return self.cache[c][0]
        if ('first', c) not in self.flow:
            self.flow[('first', c)] = cv2.VideoCapture(os.path.join(CLIPDIR, c + '.mp4')).read()[1]
        return self.flow[('first', c)]

    def _flows(self, c, i):
        k = (c, i)
        if k not in self.flow:
            fs = self.frames(c)
            a, b = [cv2.cvtColor(cv2.resize(x, (360, 640), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)
                    for x in (fs[i], fs[i + 1])]
            dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
            f01, f10 = dis.calc(a, b, None), dis.calc(b, a, None)
            up = lambda f: cv2.resize(f, (720, 1280), interpolation=cv2.INTER_LINEAR) * 2.0
            self.flow[k] = (up(f01), up(f10))
            if len(self.flow) > 12:
                del self.flow[next(iter(self.flow))]
        return self.flow[k]

    def at(self, c, tau):
        """Frame of clip c at src time tau (seconds), flow-interpolated between the 24 fps frames."""
        fs = self.frames(c)
        f = min(tau * T.SRC_FPS, len(fs) - 1)
        i = int(np.floor(f)); a = f - i
        if i >= len(fs) - 1 or a < 0.04:
            return fs[min(i, len(fs) - 1)]
        if a > 0.96:
            return fs[i + 1]
        f01, f10 = self._flows(c, i)
        gx, gy = np.meshgrid(np.arange(720, dtype=np.float32), np.arange(1280, dtype=np.float32))
        w0 = cv2.remap(fs[i], gx - a * f01[..., 0], gy - a * f01[..., 1], cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        w1 = cv2.remap(fs[i + 1], gx - (1 - a) * f10[..., 0], gy - (1 - a) * f10[..., 1], cv2.INTER_LINEAR,
                       borderMode=cv2.BORDER_REPLICATE)
        return cv2.addWeighted(w0, 1 - a, w1, a, 0)


CL = None
G = {}


def init(fmt):
    global CL, H_S8
    CL = Clips()
    G['fmt'] = fmt
    W, H = FMT[fmt]['W'], FMT[fmt]['H']
    G['layers'] = {}
    for f in os.listdir(os.path.join(OV, fmt)):
        if f.endswith('.png'):
            im = cv2.imread(os.path.join(OV, fmt, f), cv2.IMREAD_UNCHANGED)
            assert im.shape[:2] == (H, W), (f, im.shape)
            ys, xs = np.where(im[..., 3] > 0)
            y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
            G['layers'][f[:-4]] = (y0, y1, x0, x1, im[y0:y1, x0:x1].copy())  # uint8 RGBA, cropped
    G['chat'] = {}
    G['f0'] = cv2.imread(F0)
    G['f8'] = cv2.imread(F8)
    H_S8 = np.load(os.path.join(HERE, 'v2_s8_homography.npy'))
    G['c2c3'] = np.load(os.path.join(HERE, 'v2_c2c3.npy'))
    G['s8'] = s8_matched()


def chat_png(name):
    if name not in G['chat']:
        im = cv2.imread(os.path.join(OV, 'chat', name + '.png'), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
        im[..., :3] *= im[..., 3:]
        G['chat'][name] = im
    return G['chat'][name]


def s8_matched():
    """slide-08 colour-matched (low frequencies only) to C6's landed frame, plus a feathered validity mask."""
    s8 = cv2.imread(S8).astype(np.float32)
    h, w = s8.shape[:2]
    c6 = CL.at('C6', T.CLIPS['C6']['src_end'])
    c6F = cv2.resize(c6, (1080, 1920), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    c6_in_s8 = cv2.warpPerspective(c6F, np.linalg.inv(H_S8), (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    d = (c6_in_s8 - s8)
    sm = cv2.resize(d, (w // 8, h // 8), interpolation=cv2.INTER_AREA)
    sm = np.stack([cv2.medianBlur(np.ascontiguousarray(sm[..., k]), 5) for k in range(3)], -1)
    sm = cv2.GaussianBlur(sm, (0, 0), 4)
    corr = cv2.resize(sm, (w, h), interpolation=cv2.INTER_CUBIC)
    m = np.zeros((h, w), np.float32); m[2:-2, 2:-2] = 1
    m = cv2.GaussianBlur(cv2.erode(m, np.ones((61, 61), np.uint8)), (0, 0), 20)
    return np.clip(s8 + corr, 0, 255), m


# ---------------------------------------------------------------- camera
def M_of(z, c, scale_in=1.5):
    """Affine: input image (scale_in px per... input px * scale_in = F-space) -> output px."""
    f = FMT[G['fmt']]
    W, H = f['W'], f['H']
    return np.float32([[z * scale_in, 0, W / 2 - z * c[0]], [0, z * scale_in, H / 2 - z * c[1]]])


def hold_cam(u):
    """u in [0,1] across a hold: very slow eased push-in about the exhibit."""
    c0 = np.array(FMT[G['fmt']]['c0']); A = np.array(ANCHOR)
    z = 1 + (HOLD_PUSH - 1) * ease(u)
    return z, A - (A - c0) / z


def cam_at(t):
    """(z, centre) for the clip/hold part of the film."""
    c0 = np.array(FMT[G['fmt']]['c0'])
    for idx, s in enumerate(T.SEGS):
        if s.t0 <= t < s.t1 or (s is T.SEGS[-1]):
            break
    if s.kind == 'hold':
        return hold_cam((t - s.t0) / (s.t1 - s.t0))
    if s.kind == 'clip' and idx > 0 and T.SEGS[idx - 1].clip == 'C2':
        return 1.0, c0                 # after the matched C2 -> C3 cut the camera is already home
    if s.kind == 'clip' and idx > 0:   # ease the previous hold's push back out across the move
        zh, ch = hold_cam(1.0)
        u = ease((t - s.t0) / (s.t1 - s.t0))
        return zh + (1 - zh) * u, ch + (c0 - ch) * u
    return 1.0, c0


def seg_at(t):
    for s in T.SEGS:
        if s.t0 <= t < s.t1:
            return s
    return T.SEGS[-1]


def warp(img, M, flags=cv2.INTER_LANCZOS4):
    f = FMT[G['fmt']]
    return cv2.warpAffine(img, M, (f['W'], f['H']), flags=flags, borderMode=cv2.BORDER_REPLICATE)


# ---------------------------------------------------------------- the phone
def phone_cam(tr):
    f = FMT[G['fmt']]
    W, H = f['W'], f['H']
    q = cv2.perspectiveTransform(np.float32([[[SCREEN_SRC[0], SCREEN_SRC[1]], [SCREEN_SRC[2], SCREEN_SRC[3]]]]), H_S8)[0]
    S = (q[0] + q[1]) / 2; sw = q[1][0] - q[0][0]
    c0 = np.array(f['c0'])
    zf = f['scr_w'] / sw
    u = T.smoother((tr - T.PUSH[0]) / (T.PUSH[1] - T.PUSH[0]))
    drift = 1 + 0.035 * max(0.0, tr) / (T.CUT - T.L7)
    z = np.exp(np.log(zf) * u) * drift
    P0 = S - c0 + np.array([W / 2, H / 2])
    P = P0 + (np.array(f['scr_c']) - P0) * u
    c = S - (P - np.array([W / 2, H / 2])) / z
    return z, c


def phone_frame(t):
    tr = t - T.L7
    z, c = phone_cam(tr)
    base = warp(CL.at('C6', T.CLIPS['C6']['src_end']), M_of(z, c)).astype(np.float32)
    f = FMT[G['fmt']]
    A = np.float64([[z, 0, f['W'] / 2 - z * c[0]], [0, z, f['H'] / 2 - z * c[1]], [0, 0, 1]]) @ H_S8
    s8, m = G['s8']
    hi = cv2.warpPerspective(s8, A, (f['W'], f['H']), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    mm = cv2.warpPerspective(m, A, (f['W'], f['H']), flags=cv2.INTER_LINEAR)[..., None]
    img = base * (1 - mm) + hi * mm
    # chat
    name, ua = T.chat_state(tr)
    if name and ua > 0:
        ch = chat_png(name)
        if T.BUBBLE_IN <= tr < T.BUBBLE_IN + 0.15:
            k = (tr - T.BUBBLE_IN) / 0.15
            ch = chat_png('a00-1') * (1 - k) + ch * k
        s0 = T.SEND + 0.12
        if s0 <= tr < s0 + T.SENT_FADE:
            k = (tr - s0) / T.SENT_FADE
            ch = chat_png('press') * (1 - k) + ch * k
        x0, y0, x1, y1 = SCREEN_SRC
        tw = (x1 - x0) * np.hypot(A[0, 0], A[1, 0])      # on-screen width of the screen (px)
        ph, pw = ch.shape[:2]
        r = min(1.0, 1.25 * tw / pw)
        if r < 1.0:
            ch = cv2.resize(ch, (int(pw * r), int(ph * r)), interpolation=cv2.INTER_AREA)
            ph, pw = ch.shape[:2]
        Mc = np.float64([[(x1 - x0) / pw, 0, x0], [0, (y1 - y0) / ph, y0], [0, 0, 1]])
        cw = cv2.warpPerspective(ch, A @ Mc, (f['W'], f['H']), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
        cw = np.clip(cw, 0, 1) * ua
        img = img * (1 - cw[..., 3:]) + cw[..., :3] * 255
    return img


# ---------------------------------------------------------------- close + end
def close_frame(t):
    u = (t - T.CUT) / (T.END0 + T.DISSOLVE - T.CUT)
    z = 1.075 - 0.075 * (1 - (1 - min(1, u)) ** 2)
    c = np.array(FMT[G['fmt']].get('c0_row', FMT[G['fmt']]['c0']))   # 4:5 sits lower so the line clears the row
    return warp(G['f0'], M_of(z, c, 1.0)).astype(np.float32)


def end_frame(t):
    return warp(G['f8'], M_of(1.0, FMT[G['fmt']]['c0'], 1.0)).astype(np.float32)


# ---------------------------------------------------------------- compose
def picture(t):
    s = seg_at(t)
    if s.kind == 'clip':
        ts, taus = s.curve
        tau = float(np.interp(t - s.t0, ts, taus))
        z, c = cam_at(t)
        return warp(CL.at(s.clip, tau), M_of(z, c)).astype(np.float32)
    if s.kind == 'hold':
        z, c = cam_at(t)
        src = CL.at(s.clip, T.CLIPS[s.clip]['src_end'])
        nxt = 'C%d' % (int(s.clip[1]) + 1)
        th = t - s.t0
        if s.clip == 'C2':
            return c2_hold(src, th / (s.t1 - s.t0))
        if s.clip != 'C2' and th > XFADE_HOLD[0]:   # C2 -> C3 is a real cut (different framing), not blended
            k = ease((th - XFADE_HOLD[0]) / XFADE_HOLD[1])
            src = cv2.addWeighted(src, 1 - k, CL.first(nxt), k, 0)
        return warp(src, M_of(z, c)).astype(np.float32)
    if s.kind == 'phone':
        return phone_frame(t)
    if s.kind == 'close':
        return close_frame(t)
    # end: dissolve from the row, then the wall
    k = ease((t - T.END0) / T.DISSOLVE)
    if k < 1:
        return close_frame(t) * (1 - k) + end_frame(t) * k
    return end_frame(t)


def c2_hold(src, u):
    """C2 was cut mid-zoom: carry that zoom on (ease-out, starting near C2's own zoom rate) and land on C3's
    opening framing, while the colour eases to C3's, so the cut to C3 matches."""
    sc, px, py, gb, gg, gr = G['c2c3']
    e = 1 - (1 - min(1.0, u * 1.06)) ** 3
    z = np.exp(np.log(sc) * e)
    A2 = np.float32([[z, 0, px * (1 - z)], [0, z, py * (1 - z)]])
    Mo = M_of(1.0, np.array(FMT[G['fmt']]['c0']))
    M = np.hstack([Mo[:, :2] @ A2[:, :2], (Mo[:, :2] @ A2[:, 2] + Mo[:, 2])[:, None]])
    k = T.smooth(u * 1.06)
    gain = np.float32([1 + (gb - 1) * k, 1 + (gg - 1) * k, 1 + (gr - 1) * k])
    return warp(src, M).astype(np.float32) * gain


def text_alpha(t):
    out = []
    for name, ti, fi, to, fo in T.TEXT:
        a = ease((t - ti) / fi) * (1 - ease((t - to) / fo))
        if a > 0:
            out.append((name, a))
    L7, cut = T.L7, T.CUT
    if L7 + T.EX7_TEXT_IN <= t < cut:
        a = ease((t - (L7 + T.EX7_TEXT_IN)) / 0.6)
        x = ease((t - (L7 + T.HEAD_XF[0])) / T.HEAD_XF[1])
        out += [('ex7lbl', a), ('ex7typed', a * (1 - x)), ('ex7sent', a * x)]
    if cut <= t:
        a = ease((t - (cut + 0.45)) / 0.8) * (1 - ease((t - (T.END0 - 0.55)) / 0.55))  # gone before the dissolve
        if a > 0:
            out.append(('close', a))
    if t >= T.END0:
        out.append(('end', ease((t - (T.END0 + 0.75)) / 0.9)))      # arrives once the wall is up
    return [(n, a) for n, a in out if a > 0]


def render(fi, grain=True):
    t = fi / T.FPS
    img = picture(t)
    bl = cv2.GaussianBlur(img, (0, 0), 1.1)
    img = img + 0.35 * (img - bl)                      # light unsharp after the 1.5x upscale
    if grain:
        rng = np.random.default_rng(fi)
        n = rng.normal(0, 1.0, img.shape[:2]).astype(np.float32)
        img = img + cv2.GaussianBlur(n, (0, 0), 0.7)[..., None] * GRAIN
    img = np.clip(img, 0, 255) / 255
    for name, a in text_alpha(t):
        y0, y1, x0, x1, im = G['layers'][name]
        al = im[..., 3:].astype(np.float32) / 255
        pm = im[..., :3].astype(np.float32) / 255 * al
        img[y0:y1, x0:x1] = img[y0:y1, x0:x1] * (1 - al * a) + pm * a
    fo = 1 - ease((t - (T.TOTAL - T.FADE_OUT)) / T.FADE_OUT)
    return np.clip(img * fo * 255 + 0.5, 0, 255).astype(np.uint8)


def _work(fi):
    return render(fi).tobytes()


def main():
    fmt = sys.argv[1]
    args = sys.argv[2:]
    if '--stills' in args:
        ts = [float(x) for x in args[args.index('--stills') + 1].split(',')]
        out = args[args.index('--out') + 1]; os.makedirs(out, exist_ok=True)
        init(fmt)
        for t in ts:
            cv2.imwrite(os.path.join(out, f'{fmt}-{t:06.2f}.png'), render(int(round(t * T.FPS)), grain=False))
        return
    rng = (0, T.NFRAMES)
    if '--range' in args:
        a, b = args[args.index('--range') + 1].split(',')
        rng = (int(float(a) * T.FPS), int(float(b) * T.FPS))
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(HERE, 'work', 'v2', f'video-{fmt}.mp4')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    f = FMT[fmt]
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
                           '-s', f"{f['W']}x{f['H']}", '-r', str(T.FPS), '-i', '-', '-c:v', 'libx264',
                           '-profile:v', 'high', '-preset', 'slow', '-crf', CRF, '-pix_fmt', 'yuv420p',
                           '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    with Pool(3, initializer=init, initargs=(fmt,)) as pool:
        for k, buf in enumerate(pool.imap(_work, range(*rng), chunksize=16)):
            ff.stdin.write(buf)
            if k % 150 == 0:
                print(f'{fmt} frame {rng[0] + k}/{rng[1]}', flush=True)
    ff.stdin.close(); ff.wait()
    print('wrote', out)


if __name__ == '__main__':
    main()
