"""Step 4: render "The Museum of Men" video frames (2.5D parallax camera) and encode.

    python build.py v            # 9:16 master 1080x1920 -> work/video-v.mp4 (no audio)
    python build.py p            # 4:5  1080x1350        -> work/video-p.mp4
    python build.py v --frames 0,150,300 --out DIR   # stills for review
Inputs: work/canvas/slide-NN.png + work/depth/slide-NN.npy (stage.py), work/overlays/ (overlays.mjs).
mux.py adds the score and writes out/.

The camera: every shot is a still canvas + a disparity map. A camera is (focal canvas point F,
where F sits in the frame pF, zoom z, extra shift sx, dolly parallax pz, lateral parallax tx).
For each output pixel u we look up canvas point
    X = F + (u - pF - sx) / (k*z*(1 + pz*(d - d0))) - tx*(d - d0)/(k*z)
with d = smoothed disparity at X (2 fixed-point passes) and d0 = disparity at F: things nearer
than the focal object scale/shift more, farther things less (2.5D). Disparity is heavily
smoothed and parallax amounts are kept small, so the warp never folds (no tearing).
Rendering is 2x supersampled, then INTER_AREA down; glides get true motion blur (5 sub-frames).
"""
import os, sys, math, subprocess
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
W_ = lambda *p: os.path.join(HERE, 'work', *p)
FPS = 30
K1 = 1080 / 1856          # frame px per canvas px at z = 1 (full photo width = frame width)
SS = 2                    # supersampling
CANVAS = 3300

FMT = {'v': (1080, 1920), 'p': (1080, 1350)}

# ---------------------------------------------------------------- timeline (seconds)
DISS0, DISS1 = 5.4, 6.2   # row -> exhibit 1 match-dissolve
HOLD, GLIDE, HOLD7 = 4.2, 1.1, 6.8
ARR = [DISS1 + i * (HOLD + GLIDE) for i in range(7)]  # arrival (fully landed) of exhibits 1..7
CUT = ARR[6] + HOLD7      # hard cut back to the row
END_D0, END_D1 = CUT + 7.0, CUT + 8.2  # cross-dissolve row -> end wall
TOTAL = END_D1 + 6.3
NFR = int(round(TOTAL * FPS))

# ---------------------------------------------------------------- per-shot geometry
# focal points (canvas px) measured on the canvases (see README)
FOC = {2: (1655, 1999), 3: (1684, 1999), 4: (1676, 1906), 5: (1659, 2110), 6: (1667, 2033),
       7: (1608, 1999), 8: (1650.5, 1818.5), 9: (1633, 2373)}
DRAWER_W = {2: 704, 9: 748}           # drawer width in canvas px, for the match-dissolve
SCREEN = (847 + 722, 1156 + 498, 163, 329)  # phone screen rect on canvas 08 (x, y, w, h)
KPZ = 0.55                            # dolly parallax per unit ln(zoom)
GL_D = {'v': 700, 'p': 700}           # glide travel (frame px)
GL_P = 85                             # extra lateral parallax in the glide (frame px per unit disparity)


def ease(x):  # cubic in-out
    x = min(max(x, 0.0), 1.0)
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def smooth(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def herm(p0, p1, m0, m1, T, t):  # cubic Hermite over [0, T]
    s = min(max(t / T, 0), 1)
    h00, h10, h01, h11 = 2 * s ** 3 - 3 * s ** 2 + 1, s ** 3 - 2 * s ** 2 + s, -2 * s ** 3 + 3 * s ** 2, s ** 3 - s ** 2
    return h00 * p0 + h10 * T * m0 + h01 * p1 + h11 * T * m1


class Cam:
    def __init__(self, n, F, pF, z, pz=0.0, sx=0.0, tx=0.0):
        self.n, self.F, self.pF, self.z, self.pz, self.sx, self.tx = n, F, pF, z, pz, sx, tx


def geo(fmt):
    Wf, Hf = FMT[fmt]
    g = {}
    if fmt == 'v':
        g['ex_pf'] = (Wf / 2, 1150); g['ex1_pf'] = (Wf / 2, 1250)
        g['ex_z'] = (1.08, 1.17); g['ex1_z0'] = 1.36
        g['ph_z1'], g['ph_pf1'] = 3.85, (Wf / 2, 1125)
        g['row_pf0'] = None; g['close_z'] = (1.17, 1.0); g['close_c'] = (1650, 1650)
        g['end_F'], g['end_z'] = (1650, 1000), (2.1, 2.17)
    else:
        g['ex_pf'] = (Wf / 2, 885); g['ex1_pf'] = (Wf / 2, 900)
        g['ex_z'] = (1.04, 1.12); g['ex1_z0'] = 1.30
        g['ph_z1'], g['ph_pf1'] = 3.3, (Wf / 2, 815)
        g['row_pf0'] = None; g['close_z'] = (1.15, 1.0); g['close_c'] = (1650, 1600)
        g['end_F'], g['end_z'] = (1650, 1040), (1.6, 1.66)
    return g


def ex_span(i):  # exhibit index 1..7 -> (start, end) of its camera
    a = ARR[i - 1]
    s = DISS0 if i == 1 else a - GLIDE
    e = a + HOLD7 if i == 7 else a + HOLD + GLIDE
    return s, e


def ex_zoom(fmt, i, t):
    g = geo(fmt)
    s, e = ex_span(i)
    if i == 1:
        z0 = g['ex1_z0']; z1 = z0 * 1.085
    else:
        z0, z1 = g['ex_z']
    return math.exp(math.log(z0) + (math.log(z1) - math.log(z0)) * (t - s) / (e - s)), z0, z1


def ex_cam(fmt, i, t):
    g, Wf = geo(fmt), FMT[fmt][0]
    n = i + 1
    s, e = ex_span(i)
    a = ARR[i - 1]
    z, z0, z1 = ex_zoom(fmt, i, t)
    zref = math.sqrt(z0 * z1)
    pF = g['ex1_pf'] if i == 1 else g['ex_pf']
    if fmt == 'v' and n == 5:  # chappals sit low on their canvas: lift the frame so it stays on canvas
        pF = (pF[0], 1195)
    if i == 7:  # the phone: slow push from gallery framing to a readable screen
        p = ease((t - (a + 0.3)) / 4.3)
        zA, zB = g['ex_z'][0] * (1 + 0.04 * max(0, (t - s)) / GLIDE) if t < a else g['ex_z'][0] * 1.04, g['ph_z1']
        z = math.exp(math.log(zA) + (math.log(zB) - math.log(zA)) * p)
        pF = (pF[0] + (g['ph_pf1'][0] - pF[0]) * p, pF[1] + (g['ph_pf1'][1] - pF[1]) * p)
        zref = g['ex_z'][0] * 1.04
    pz = KPZ * math.log(z / zref)
    if i == 7:
        pz = KPZ * math.log(min(z, zref * 1.15) / zref)  # parallax stops growing on the big push
    sx = tx = 0.0
    if t < a and i > 1:  # gliding in from the right
        q = 1 - ease((t - (a - GLIDE)) / GLIDE); sx, tx = q * GL_D[fmt], q * GL_P
    if i < 7 and t > a + HOLD:  # gliding out to the left
        q = ease((t - (a + HOLD)) / GLIDE); sx, tx = -q * GL_D[fmt], -q * GL_P
    return Cam(n, FOC[n], pF, z, pz, sx, tx)


def row_intro_cam(fmt, t):
    """The row: dolly toward the nearest plinth, landing on exhibit 1's framing at the dissolve midpoint."""
    Wf, Hf = FMT[fmt]
    F = FOC[9]
    tm = (DISS0 + DISS1) / 2
    pf0 = (Wf / 2 + (F[0] - 1650) * K1, Hf / 2 + (F[1] - (1650 if fmt == 'v' else 1700)) * K1)
    z_ex1_m, z0, z1 = ex_zoom(fmt, 1, tm)
    rate = (math.log(z1) - math.log(z0)) / (ex_span(1)[1] - ex_span(1)[0])
    zm = z_ex1_m * DRAWER_W[2] / DRAWER_W[9]
    pf1 = geo(fmt)['ex1_pf']
    lz = herm(0.0, math.log(zm), 0.0, rate, tm, t) if t <= tm else math.log(zm) + rate * (t - tm)
    q = ease(t / tm)
    pF = (pf0[0] + (pf1[0] - pf0[0]) * q, pf0[1] + (pf1[1] - pf0[1]) * q)
    z = math.exp(lz)
    lo = Hf - (CANVAS - 6 - F[1]) * K1 * z  # keep the frame's bottom edge on the canvas
    pF = (pF[0], max(pF[1], lo))
    return Cam(9, F, pF, z, KPZ * 1.2 * lz)


def row_close_cam(fmt, t):
    Wf, Hf = FMT[fmt]
    g = geo(fmt)
    p = (t - CUT) / (END_D1 - CUT)
    za, zb = g['close_z']
    z = math.exp(math.log(za) + (math.log(zb) - math.log(za)) * (1 - (1 - p) ** 1.6))
    return Cam(9, g['close_c'], (Wf / 2, Hf / 2), z, KPZ * 1.2 * math.log(z / zb))


def end_cam(fmt, t):
    Wf, Hf = FMT[fmt]
    g = geo(fmt)
    p = (t - END_D0) / (TOTAL - END_D0)
    za, zb = g['end_z']
    return Cam(3, g['end_F'], (Wf / 2, Hf / 2), za + (zb - za) * p, 0.0)


def layers_at(fmt, t):
    """[(alpha, [cams sampled across the shutter])] for time t."""
    def mb(fn):  # 5 sub-frames over a 180-degree shutter
        return [fn(t + (j / 4 - 0.5) * 0.5 / FPS) for j in range(5)]
    if t < DISS0:
        return [(1.0, [row_intro_cam(fmt, t)])]
    if t < DISS1:
        a = smooth((t - DISS0) / (DISS1 - DISS0))
        return [(1 - a, [row_intro_cam(fmt, t)]), (a, [ex_cam(fmt, 1, t)])]
    if t < CUT:
        for i in range(1, 8):
            a = ARR[i - 1]
            if i < 7 and a + HOLD <= t < a + HOLD + GLIDE:  # glide i -> i+1
                p = (t - (a + HOLD)) / GLIDE
                w = smooth((p - 0.37) / 0.26)
                return [(1 - w, mb(lambda tt: ex_cam(fmt, i, tt))), (w, mb(lambda tt: ex_cam(fmt, i + 1, tt)))]
            if a <= t < (a + HOLD if i < 7 else CUT):
                return [(1.0, [ex_cam(fmt, i, t)])]
    if t < END_D0:
        return [(1.0, [row_close_cam(fmt, t)])]
    if t < END_D1:
        a = smooth((t - END_D0) / (END_D1 - END_D0))
        return [(1 - a, [row_close_cam(fmt, t)]), (a, [end_cam(fmt, t)])]
    return [(1.0, [end_cam(fmt, t)])]


# ---------------------------------------------------------------- assets (loaded per worker)
A = {}


def load(fmt):
    A['fmt'] = fmt
    A['canvas'] = {n: cv2.imread(W_('canvas', f'slide-{n:02d}.png')) for n in range(2, 10)}
    A['depth'] = {}
    for n in range(2, 10):
        d = np.load(W_('depth', f'slide-{n:02d}.npy'))
        A['depth'][n] = cv2.GaussianBlur(d, (0, 0), 20)  # ~60 canvas px: soft enough that nothing folds
    Wf, Hf = FMT[fmt]
    u, v = np.meshgrid((np.arange(Wf * SS, dtype=np.float32) + 0.5) / SS - 0.5,
                       (np.arange(Hf * SS, dtype=np.float32) + 0.5) / SS - 0.5)
    A['u'], A['v'] = u, v
    rd = lambda p: cv2.imread(p, cv2.IMREAD_UNCHANGED)
    A['txt'] = {k: rd(W_('overlays', fmt, f'{k}.png')) for k in
                ['title', 'close', 'end'] + [f'ex{i}' for i in range(1, 8)]}
    nch = int(open(W_('overlays', 'screen', 'n.txt')).read())
    A['nch'] = nch
    A['scr'] = {}
    for c in range(nch + 1):
        for b in (0, 1):
            im = rd(W_('overlays', 'screen', f's{c:02d}-{b}.png')).astype(np.float32)
            im[..., :3] *= im[..., 3:] / 255.0  # premultiply
            pyr = [im]
            for _ in range(4):
                pyr.append(cv2.pyrDown(pyr[-1]))
            A['scr'][(c, b)] = pyr


def dsample(n, X, Y):
    return cv2.remap(A['depth'][n], X / 3.0, Y / 3.0, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def render_cam(cam):
    Wf, Hf = FMT[A['fmt']]
    k = K1 * cam.z
    Fx, Fy = cam.F
    d0 = float(dsample(cam.n, np.float32([[Fx]]), np.float32([[Fy]]))[0, 0])
    du = A['u'] - (cam.pF[0] + cam.sx)
    dv = A['v'] - cam.pF[1]
    X = Fx + du / k; Y = Fy + dv / k
    for _ in range(2):
        dd = dsample(cam.n, X, Y) - d0
        s = k * (1 + cam.pz * dd)
        X = Fx + du / s - cam.tx * dd / k
        Y = Fy + dv / s
    img = cv2.remap(A['canvas'][cam.n], X, Y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    img = cv2.resize(img, (Wf, Hf), interpolation=cv2.INTER_AREA).astype(np.float32)
    if cam.n == 8:
        img = phone(img, cam, k)
    return img


def screen_state(t):
    a7 = ARR[6]
    t0, cps = a7 + 2.6, 13.0
    c = int(np.clip((t - t0) * cps, 0, A['nch']))
    typing = t0 <= t < t0 + A['nch'] / cps + 0.25
    blink = typing or (int((t - t0) / 0.53) % 2 == 0) or t < t0 - 0.0
    return c, 1 if blink else 0


def phone(img, cam, k):
    """Composite the code-drawn chat screen, tracked exactly to the phone's screen rect."""
    Wf, Hf = FMT[A['fmt']]
    sx0, sy0, sw, sh = SCREEN
    scale = k / 4.0  # overlay is 4 px per canvas px
    lvl = 0
    while scale * (2 ** (lvl + 1)) <= 1.0 and lvl < 4:
        lvl += 1
    ov = A['scr'][screen_state(A['t'])][lvl]
    sc = scale * (2 ** lvl)
    ox = cam.pF[0] + cam.sx + (sx0 - cam.F[0]) * k
    oy = cam.pF[1] + (sy0 - cam.F[1]) * k
    # sx0 refers to the screen's left edge = pixel edge; overlay pixel centres at +0.5
    M = np.float32([[sc, 0, ox + 0.5 * sc - 0.5], [0, sc, oy + 0.5 * sc - 0.5]])
    w = cv2.warpAffine(ov, M, (Wf, Hf), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    a = w[..., 3:] / 255.0
    return img * (1 - a) + w[..., :3]


def put_text(img, key, alpha, dx=0.0, dy=0.0):
    if alpha <= 0.002:
        return img
    ov = A['txt'][key]
    if dx or dy:
        ov = cv2.warpAffine(ov, np.float32([[1, 0, dx], [0, 1, dy]]), (ov.shape[1], ov.shape[0]),
                            flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    a = ov[..., 3:].astype(np.float32) / 255.0 * alpha
    return img * (1 - a) + ov[..., :3].astype(np.float32) * a


def texts(fmt, t):
    """[(key, alpha, dx, dy)]"""
    out = []
    fin = lambda t0, d=0.8: smooth((t - t0) / d)
    rise = lambda t0, d=0.8: 16 * (1 - ease((t - t0) / d))
    # title over the row
    if t < 4.6:
        a = fin(0.1, 0.7) * (1 - fin(3.6, 0.9))
        out.append(('title', a, 0, rise(0.1, 0.7)))
    for i in range(1, 8):
        a0 = ARR[i - 1]
        tin = a0 + 0.2
        if not (a0 - 0.1 <= t < (CUT if i == 7 else a0 + HOLD + GLIDE)):
            continue
        a = fin(tin, 0.8)
        dx = 0.0
        if i < 7 and t > a0 + HOLD:  # rides with the wall as the gallery glides, fades early
            q = ease((t - (a0 + HOLD)) / GLIDE)
            dx = -q * GL_D[fmt] * 0.92
            a *= 1 - smooth((t - (a0 + HOLD)) / (GLIDE * 0.42))
        out.append((f'ex{i}', a, dx, rise(tin)))
    if CUT <= t < END_D1:
        a = fin(CUT + 0.7, 1.0) * (1 - fin(END_D0 - 0.2, 0.7))
        out.append(('close', a, 0, rise(CUT + 0.7, 1.0)))
    if t >= END_D1 - 0.3:
        out.append(('end', fin(END_D1 - 0.3, 1.0), 0, rise(END_D1 - 0.3, 1.0) * 0.6))
    return out


GRAIN_RNG = None


def frame(fi):
    t = fi / FPS
    A['t'] = t
    fmt = A['fmt']
    Wf, Hf = FMT[fmt]
    img = np.zeros((Hf, Wf, 3), np.float32)
    for alpha, cams in layers_at(fmt, t):
        if alpha <= 0.001:
            continue
        acc = np.zeros_like(img)
        for c in cams:
            if len(cams) > 1:
                A['t'] = t  # screen state follows the frame time
            acc += render_cam(c)
        img += alpha * acc / len(cams)
    for key, a, dx, dy in texts(fmt, t):
        img = put_text(img, key, a, dx, dy)
    # fade to black over the last 0.5 s (frame 0 is a full picture: it is the Shorts first frame)
    img *= min(1.0, (TOTAL - t) / 0.5)
    # fine grain (also dithers the wall gradients so H.264 doesn't band them)
    rng = np.random.default_rng(fi)
    g = rng.normal(0, 1.0, (Hf // 2, Wf // 2)).astype(np.float32)
    g = cv2.resize(g, (Wf, Hf), interpolation=cv2.INTER_LINEAR) * 0.85
    img += g[..., None]
    return np.clip(img + 0.5, 0, 255).astype(np.uint8)


def init(fmt):
    load(fmt)


def check_coverage(fmt):
    """Report any frame whose camera samples outside the canvas (would show reflected border)."""
    worst = []
    Wf, Hf = FMT[fmt]
    for fi in range(0, NFR, 3):
        t = fi / FPS
        for alpha, cams in layers_at(fmt, t):
            if alpha < 0.15:
                continue
            c = cams[len(cams) // 2]
            k = K1 * c.z
            for (u, v) in ((0, 0), (Wf, 0), (0, Hf), (Wf, Hf)):
                X = c.F[0] + (u - c.pF[0] - c.sx) / k
                Y = c.F[1] + (v - c.pF[1]) / k
                o = max(-X, X - CANVAS, -Y, Y - CANVAS)
                if o > 0:
                    worst.append((round(t, 2), c.n, round(alpha, 2), int(o)))
    return worst


if __name__ == '__main__':
    fmt = sys.argv[1]
    Wf, Hf = FMT[fmt]
    args = sys.argv[2:]
    if '--check' in args:
        w = check_coverage(fmt)
        print(len(w), 'samples outside canvas; worst:', sorted(w, key=lambda x: -x[3])[:12])
        sys.exit()
    if '--frames' in args:
        fr = [int(x) for x in args[args.index('--frames') + 1].split(',')]
        od = args[args.index('--out') + 1]
        os.makedirs(od, exist_ok=True)
        load(fmt)
        for f in fr:
            cv2.imwrite(os.path.join(od, f'{fmt}-{f:04d}.png'), frame(f))
        sys.exit()
    from multiprocessing import Pool
    out = W_(f'video-{fmt}.mp4')
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
                           '-s', f'{Wf}x{Hf}', '-r', str(FPS), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-profile:v', 'high',
                           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out],
                          stdin=subprocess.PIPE)
    with Pool(4, initializer=init, initargs=(fmt,)) as pool:
        for i, fr in enumerate(pool.imap(frame, range(NFR), chunksize=2)):
            ff.stdin.write(fr.tobytes())
            if i % 150 == 0:
                print(f'{fmt} frame {i}/{NFR}', flush=True)
    ff.stdin.close(); ff.wait()
    print('wrote', out, 'frames', NFR, 'dur', TOTAL)
