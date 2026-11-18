"""Step 2: build the 'stage' for every shot = canvas (3300x3300 BGR) + disparity map.

    python stage.py           # compose canvases from work/gen/slide-NN-o*.jpg (latest pick), then depth
Canvas: the outpaint is registered to the original (ECC affine), colour-matched at the seam,
and the ORIGINAL pixels are pasted back 1:1 over the centre, so every pixel
of the exhibit itself is the approved still, not a re-generation.
Depth: Depth Anything V2 Small (Apache-2.0, depth-anything/Depth-Anything-V2-Small-hf) via
transformers on CPU -> relative disparity (near = 1), saved as work/depth/slide-NN.npy (1100x1100).
"""
import glob, os, sys
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '2026-11-museum-of-men', 'assets', 'gen', 'pick')
W = lambda *p: os.path.join(HERE, 'work', *p)
CW = CH = 3300
OX, OY = 722, 498
PICK = {'05': 6, '07': 2}
# small retouches (canvas px boxes, inpainted): the ceiling downlight in the row sits exactly in the
# close line's text band in the video and reads like a hyphen between two words
RETOUCH = {'09': [(1612, 515, 1700, 580)]}  # lowest seam score (seamscore.py); o1 of both showed the photo's rectangle


def latest_gen(n):
    if n in PICK:
        return W('gen', f'slide-{n}-o{PICK[n]}.jpg')
    fs = sorted(glob.glob(W('gen', f'slide-{n}-o*.jpg')), key=lambda f: int(f.rsplit('-o', 1)[1][:-4]))
    return fs[-1]


def compose(n):
    orig = cv2.imread(os.path.join(SRC, f'slide-{n}.png'))
    gen = cv2.resize(cv2.imread(latest_gen(n)), (CW, CH), interpolation=cv2.INTER_AREA)
    # register gen -> canvas frame, using the original's area (ECC, affine, coarse-to-fine)
    ref = np.zeros((CH, CW), np.float32); ref[OY:OY + 2304, OX:OX + 1856] = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    mask = np.zeros((CH, CW), np.uint8); mask[OY + 20:OY + 2284, OX + 20:OX + 1836] = 255
    g = cv2.cvtColor(gen, cv2.COLOR_BGR2GRAY).astype(np.float32)
    warp = np.eye(2, 3, dtype=np.float32)
    s = 0.25
    r_s, g_s = cv2.resize(ref, None, fx=s, fy=s), cv2.resize(g, None, fx=s, fy=s)
    m_s = cv2.resize(mask, None, fx=s, fy=s, interpolation=cv2.INTER_NEAREST)
    crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6)
    try:
        _, warp = cv2.findTransformECC(r_s, g_s, warp, cv2.MOTION_AFFINE, crit, m_s, 5)
        warp[:, 2] /= s
    except cv2.error as e:
        print(n, 'ECC failed, identity', e)
    gen_al = cv2.warpAffine(gen, warp, (CW, CH), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP,
                            borderMode=cv2.BORDER_REFLECT)
    # colour match: low-frequency difference inside the original area, diffused outward
    inside = np.zeros((CH, CW), np.float32); inside[OY:OY + 2304, OX:OX + 1856] = 1
    diff = (orig.astype(np.float32) - gen_al[OY:OY + 2304, OX:OX + 1856].astype(np.float32))
    D = np.zeros((CH, CW, 3), np.float32); D[OY:OY + 2304, OX:OX + 1856] = diff
    sm = 1 / 8
    Ds, Is = cv2.resize(D * inside[..., None], None, fx=sm, fy=sm, interpolation=cv2.INTER_AREA), \
        cv2.resize(inside, None, fx=sm, fy=sm, interpolation=cv2.INTER_AREA)
    num, den = cv2.GaussianBlur(Ds, (0, 0), 12), cv2.GaussianBlur(Is, (0, 0), 12)[..., None]
    corr = num / np.maximum(den, 1e-3)
    fall = np.clip(den / 0.15, 0, 1)  # fades the correction out far from the photo
    corr = cv2.resize(corr * fall, (CW, CH), interpolation=cv2.INTER_CUBIC)
    out = np.clip(gen_al.astype(np.float32) + corr, 0, 255)
    # seam fix: if the outpaint itself has a step at the photo's border, pull a 24 px ring just
    # outside the border onto the original's edge values and let that correction decay outward.
    B = 24
    rep = cv2.copyMakeBorder(cv2.GaussianBlur(orig, (0, 0), 4).astype(np.float32), B, B, B, B, cv2.BORDER_REPLICATE)
    ring = np.zeros((CH, CW), np.float32)
    ring[OY - B:OY + 2304 + B, OX - B:OX + 1856 + B] = 1; ring[OY:OY + 2304, OX:OX + 1856] = 0
    tgt = np.zeros((CH, CW, 3), np.float32); tgt[OY - B:OY + 2304 + B, OX - B:OX + 1856 + B] = rep
    step = (tgt - cv2.GaussianBlur(out, (0, 0), 4)) * ring[..., None]
    sm2 = 1 / 4
    num = cv2.GaussianBlur(cv2.resize(step, None, fx=sm2, fy=sm2, interpolation=cv2.INTER_AREA), (0, 0), 10)
    den = cv2.GaussianBlur(cv2.resize(ring, None, fx=sm2, fy=sm2, interpolation=cv2.INTER_AREA), (0, 0), 10)[..., None]
    c2 = num / np.maximum(den, 1e-4) * np.clip(den / 0.25, 0, 1)
    c2 = cv2.resize(c2, (CW, CH), interpolation=cv2.INTER_CUBIC)
    out = np.clip(out + c2 * (1 - inside[..., None]), 0, 255)
    # paste the original 1:1 (the ring correction above already matches the outpaint to its edge),
    # then soften just the 1-px border line with a narrow blur in a 12 px band
    canvas = out.copy()
    canvas[OY:OY + 2304, OX:OX + 1856] = orig
    band = np.zeros((CH, CW), np.float32)
    band[OY - 6:OY + 2304 + 6, OX - 6:OX + 1856 + 6] = 1; band[OY + 6:OY + 2304 - 6, OX + 6:OX + 1856 - 6] = 0
    band = cv2.GaussianBlur(band, (0, 0), 3)[..., None]
    canvas = canvas * (1 - band) + cv2.GaussianBlur(canvas, (0, 0), 2.5) * band
    canvas = np.clip(canvas + 0.5, 0, 255).astype(np.uint8)
    if n in RETOUCH:  # clone clean wall from 160 px to the left (same height = same gradient), Poisson-blended
        for x0, y0, x1, y1 in RETOUCH[n]:
            src = canvas[y0 - 20:y1 + 20, x0 - 180:x1 - 140].copy()
            mask = np.full(src.shape[:2], 255, np.uint8)
            canvas = cv2.seamlessClone(src, canvas, mask, ((x0 + x1) // 2, (y0 + y1) // 2), cv2.NORMAL_CLONE)
    os.makedirs(W('canvas'), exist_ok=True)
    cv2.imwrite(W('canvas', f'slide-{n}.png'), canvas)
    err = np.abs(diff).mean()
    print(n, 'warp', np.round(warp, 4).tolist(), 'mean |orig-gen| in photo area', round(float(err), 1))


def depth(ns):
    import torch
    from transformers import AutoImageProcessor, AutoModelForDepthEstimation
    name = 'depth-anything/Depth-Anything-V2-Small-hf'
    proc = AutoImageProcessor.from_pretrained(name)
    model = AutoModelForDepthEstimation.from_pretrained(name).eval()
    os.makedirs(W('depth'), exist_ok=True)
    for n in ns:
        im = cv2.cvtColor(cv2.imread(W('canvas', f'slide-{n}.png')), cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, (1100, 1100), interpolation=cv2.INTER_AREA)
        inp = proc(images=im, return_tensors='pt')
        with torch.no_grad():
            pd = model(**inp).predicted_depth  # relative inverse depth (bigger = nearer)
        d = torch.nn.functional.interpolate(pd[:, None], size=(1100, 1100), mode='bicubic',
                                            align_corners=False)[0, 0].numpy()
        lo, hi = np.percentile(d, 1), np.percentile(d, 99.5)
        d = np.clip((d - lo) / (hi - lo), 0, 1).astype(np.float32)
        np.save(W('depth', f'slide-{n}.npy'), d)
        cv2.imwrite(W('depth', f'slide-{n}.png'), (d * 255).astype(np.uint8))
        print(n, 'depth ok')


if __name__ == '__main__':
    ns = sys.argv[1:] or [f'{i:02d}' for i in range(2, 10)]
    for n in ns:
        compose(n)
    depth(ns)
