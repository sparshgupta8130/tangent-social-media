"""Surgical fix for Flow clip C0: remove the jarring re-light/swing at ~6.5-7.3 s.
Keeps C0 up to CUT, then a 1.25 s eased match-dissolve (scale/position-matched on the drawer)
into the clip's own final frame (F1 framing), then a short hold. Usage: python fix_c0.py
"""
import subprocess, numpy as np
from PIL import Image
SRC, OUT = 'flow-clips/C0.mp4', 'flow-clips/C0-fixed.mp4'
W, H, FPS = 720, 1280, 24
CUT = 153                       # last original frame kept (~6.37 s)
TR, HOLD = 30, 12               # transition / hold frames
raw = subprocess.run(['ffmpeg','-v','error','-i',SRC,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
fr = np.frombuffer(raw,np.uint8).reshape(-1,H,W,3)
A, B = fr[CUT], fr[-1]
# drawer centre/width (px): A angled close-up, B frontal (measured from frames)
ca, wa = np.array([358.,920.]), 716.
cb, wb = np.array([355.,830.]), 378.
def warp(img, scale, center_src, center_dst):
    # scale about center_src then move it to center_dst
    im = Image.fromarray(img)
    a = 1/scale
    tx = center_src[0] - a*center_dst[0]; ty = center_src[1] - a*center_dst[1]
    return np.asarray(im.transform((W,H), Image.AFFINE, (a,0,tx,0,a,ty), resample=Image.BICUBIC)).astype(np.float32)
ease = lambda t: t*t*(3-2*t)
frames = [f for f in fr[:CUT+1]]
k0 = wa/wb
for i in range(1,TR+1):
    t = ease(i/TR)
    # A keeps drifting in gently (momentum) and slides toward B's drawer position
    sa = 1 + 0.06*t
    ctrA = ca + (cb-ca)*t
    a_img = warp(A, sa*(1-t) + (wb/wa)*t*0 + sa*t if False else sa, ca, ctrA)
    # B starts drawer-matched to A, eases to its natural framing
    sb = k0 + (1-k0)*t
    ctrB = ca + (cb-ca)*t
    b_img = warp(B, sb, cb, ctrB)
    alpha = ease(min(1, max(0, (i/TR - 0.1)/0.8)))
    frames.append(((1-alpha)*a_img + alpha*b_img).clip(0,255).astype(np.uint8))
frames += [B]*HOLD
p = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
    '-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
for f in frames: p.stdin.write(np.ascontiguousarray(f).tobytes())
p.stdin.close(); p.wait()
print('wrote', OUT, len(frames), 'frames', round(len(frames)/FPS,2), 's')
