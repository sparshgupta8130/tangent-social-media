"""v2 (Flow): original score, synthesised from scratch (no samples, no loops). Adapted from score.py.

    python v2_score.py work/v2/score.wav
Felt piano + warm pad, 72 BPM in D, on the same beat grid as the picture (v2_timeline.py: every landing and
every move starts on a beat). Opening on the row -> exhibits 1-6 (a chord lands with each exhibit, quiet
8th-note arpeggio) -> the phone (a lift: Em9 F#m7 Gadd9 Asus, higher voicing, pad swell; the arpeggio drops
out while he deletes the draft; synthesised key clicks under typing and deleting, a soft tap on send) ->
the cut to the row (space: low bass + a few single notes) -> the end card (resolves to D).
Quiet room tone throughout; a faint air movement under each fast stretch of a camera move.
Mastered to -14 LUFS integrated, true peak <= -1 dBTP (4x-oversampled, stereo-linked limiter).
"""
import sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly
import soundfile as sf
import pyloudnorm as pyln
import v2_timeline as T

SR = 48000
DUR = T.TOTAL
N = int(SR * (DUR + 0.05))
rng = np.random.default_rng(19)
BEAT = T.BEAT
midi = lambda m: 440.0 * 2 ** ((m - 69) / 12)
lp = lambda x, f, o=2: sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
hp = lambda x, f, o=2: sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
bp = lambda x, a, b, o=2: sosfilt(butter(o, [a, b], 'band', fs=SR, output='sos'), x)


def add(dst, sig, t, g=1.0):
    i = int(t * SR)
    if i >= len(dst):
        return
    j = min(len(dst), i + len(sig))
    dst[i:j] += sig[:j - i] * g


def piano(m, dur=4.0, vel=0.6):
    """Felt piano: inharmonic partials, per-partial decay, soft hammer thump, gentle stereo-free mono."""
    f0 = midi(m)
    n = int(dur * SR); t = np.arange(n) / SR
    B_inh = 0.00025
    out = np.zeros(n)
    for k in range(1, 14):
        fk = f0 * k * np.sqrt(1 + B_inh * k * k)
        if fk > 9000:
            break
        amp = (vel ** (0.6 + 0.25 * k)) / k ** 1.15
        dec = (2.8 + 6 * (60 - min(m, 60)) / 60) / (1 + 0.35 * k)  # low notes ring longer
        det = 1 + rng.uniform(-0.0004, 0.0004)
        out += amp * np.sin(2 * np.pi * fk * det * t + rng.uniform(0, 6.28)) * np.exp(-t / dec)
    att = np.minimum(1, t / 0.006)
    thump = lp(rng.normal(0, 1, n), 900) * np.exp(-t / 0.012) * 0.15 * vel
    rel = np.minimum(1, (dur - t) / 0.35)
    sig = (out * att + thump) * rel
    return lp(sig, 2500 + 3000 * vel) * 0.35


def pad(ms, dur, att=2.5, rel=2.5, bright=900):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for m in ms:
        for d in (-0.07, 0.0, 0.06):  # cents-ish detune via ratio
            f = midi(m) * 2 ** (d / 12)
            ph = rng.uniform(0, 1)
            saw = 2 * ((f * t + ph) % 1) - 1
            s += saw
    env = np.minimum(1, t / att) * np.minimum(1, np.maximum(0, (dur - t) / rel))
    s = lp(lp(s, bright), bright * 1.3)
    s *= (1 + 0.08 * np.sin(2 * np.pi * 0.13 * t))  # slow breathing
    return s * env / (len(ms) * 3) * 0.5


def reverb(x, secs=3.2, mix=0.32):
    n = int(secs * SR); t = np.arange(n) / SR
    ir = rng.normal(0, 1, n) * np.exp(-t / (secs / 6.9))
    ir = lp(hp(ir, 180), 5000)
    ir[: int(0.012 * SR)] = 0
    ir /= np.sqrt((ir ** 2).sum())
    wet = fftconvolve(x, ir)[: len(x)]
    return x * (1 - mix) + wet * mix * 1.6


piano_b, pad_b, amb, fx = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)

Dmaj9 = (38, [62, 66, 69, 73, 76]); Bm9 = (35, [62, 66, 69, 73]); Gmaj7 = (31, [59, 62, 66, 71])
Aadd4 = (33, [61, 62, 64, 69]); Em9 = (28, [59, 62, 66, 67]); F_m7 = (30, [61, 64, 69, 73])
Gadd9 = (31, [57, 62, 67, 71]); Asus = (33, [62, 64, 69, 74]); D6 = (38, [62, 66, 69, 71])

g0 = T.GRID0
grid = lambda t: g0 + round((t - g0) / (BEAT / 2)) * (BEAT / 2)     # snap to the 8th-note grid

# ---- 0 -> exhibit 1: the row. Pad in, a few spaced notes on the grid, title.
add(pad_b, pad([50, 57, 62, 66], T.LAND[1] + 1.5, att=2.5, rel=2.0), 0.0, 1.0)
add(piano_b, piano(38, 7, 0.45), grid(0.4))
for b, m, v in ((0, 74, 0.45), (2, 69, 0.36), (4, 73, 0.40), (6, 66, 0.34), (7.5, 71, 0.32)):
    add(piano_b, piano(m, 5, v), grid(0.4) + b * BEAT)

# ---- exhibits 1-6: one chord per exhibit, landing on its arrival; arpeggio on 8ths until the next landing
prog = [Dmaj9, Bm9, Gmaj7, Aadd4, Dmaj9, Bm9]
PAT = (0, 2, 1, 3, 2, 1, 4, 2)
for i in range(1, 7):
    t0, t1 = T.LAND[i], T.LAND[i + 1]
    bass, v = prog[i - 1]
    add(piano_b, piano(bass + 12, 6.5, 0.46), t0)
    add(piano_b, piano(bass, 6.5, 0.30), t0)
    add(pad_b, pad(v[:3], t1 - t0 + 2.0, att=1.0, rel=2.0, bright=820), t0 - 0.3, 0.72)
    n = int((t1 - t0) / (BEAT / 2))
    for j in range(1, n):
        t = t0 + j * BEAT / 2
        moving = t >= t0 + T.HOLD_BEATS * BEAT
        vel = (0.30 if moving else 0.38) * (1.08 if j % 4 == 0 else 1.0) * (0.9 + 0.1 * rng.random())
        add(piano_b, piano(v[PAT[j % len(PAT)] % len(v)] + (12 if (moving and j % 8 == 5) else 0), 3.2, vel), t)

# ---- exhibit 7, the phone: the lift. Chords change on beats across the 12-beat phone section.
L7 = T.L7
lift = [(0, Em9), (3, F_m7), (6, Gadd9), (9, Asus)]
for b, (bass, v) in lift:
    t = L7 + b * BEAT
    add(piano_b, piano(bass + 12, 5.0, 0.42), t)
    add(piano_b, piano(bass, 5.0, 0.26), t)
    for j, m in enumerate(v[1:] + [v[0] + 12]):
        tt = t + (j + 1) * BEAT / 2
        if L7 + T.BACK0 - 0.1 <= tt < L7 + T.TYPE2[0]:   # silence the arpeggio while he deletes the draft
            continue
        add(piano_b, piano(m + 12, 3.0, 0.33 + 0.02 * b / 3), tt)
add(pad_b, pad([55, 62, 66, 71, 74], T.CUT - L7 + 1.2, att=3.0, rel=1.0, bright=1500), L7 - 0.4, 1.1)
# a single low held note under the deletion
add(piano_b, piano(40, 4.0, 0.30), grid(L7 + T.BACK0))


def click(kind='key'):
    n = int(0.05 * SR); t = np.arange(n) / SR
    if kind == 'key':
        s = bp(rng.normal(0, 1, n), 1800, 6500) * np.exp(-t / 0.0045) + 0.25 * np.sin(2 * np.pi * 3100 * t) * np.exp(-t / 0.003)
    elif kind == 'back':
        s = bp(rng.normal(0, 1, n), 1200, 4800) * np.exp(-t / 0.004)
    else:  # send: a soft tap plus a small rising blip
        s = bp(rng.normal(0, 1, n), 900, 4000) * np.exp(-t / 0.006)
        n2 = int(0.09 * SR); t2 = np.arange(n2) / SR
        blip = np.sin(2 * np.pi * (700 * t2 + 2200 * t2 ** 2)) * np.sin(np.pi * t2 / t2[-1]) * 0.35
        s = np.concatenate([s, np.zeros(n2 - n)]) + blip
    return s * rng.uniform(0.75, 1.0)


for x in T.TYPE1 + T.TYPE2:
    add(fx, click('key'), L7 + x, 0.020)
for x in T.BACK:
    add(fx, click('back'), L7 + x, 0.015)
add(fx, click('send'), L7 + T.SEND, 0.03)

# ---- the cut to the row: space. Low B, a few single high notes.
C = T.CUT
add(piano_b, piano(35, 7, 0.40), C + 0.03)
add(pad_b, pad([47, 54, 59, 62], T.END0 - C + 2.5, att=0.8, rel=2.5, bright=700), C, 0.8)
for b, m, v in ((1, 74, 0.34), (3, 73, 0.30), (4.5, 69, 0.28)):
    add(piano_b, piano(m, 5, v), C + b * BEAT)

# ---- end card: resolve to D, a final chord left to ring
te = T.END0 + 0.15
add(piano_b, piano(31, 5, 0.34), T.END0 - BEAT); add(piano_b, piano(69, 4, 0.28), T.END0 - BEAT / 2)
add(piano_b, piano(38, 8, 0.48), te); add(piano_b, piano(26, 8, 0.34), te)
for j, m in enumerate((62, 66, 69, 73, 76, 81)):
    add(piano_b, piano(m, 7, 0.38), te + 0.3 + j * BEAT / 4)
add(pad_b, pad([50, 57, 62, 66, 69], DUR - T.END0 + 0.5, att=2.0, rel=3.0, bright=1000), T.END0, 0.95)

# ---- room tone + air under the fast stretch of each move
room = lp(hp(rng.normal(0, 1, N), 70), 900, 4)
room = room * (1 + 0.15 * np.sin(2 * np.pi * 0.05 * np.arange(N) / SR)) * 0.010
amb += room
for s in T.SEGS:
    if s.kind == 'clip' and s.clip != 'C0':
        n = int((s.t1 - s.t0) * SR); tt = np.arange(n) / n
        sw = hp(lp(rng.normal(0, 1, n), 1500), 250) * np.sin(np.pi * tt) ** 2 * 0.010
        add(amb, sw, s.t0)

mix = reverb(piano_b + pad_b * 0.55, 3.4, 0.34) + amb + reverb(fx, 0.8, 0.18)
mix = hp(mix, 30)
fade = np.ones(N); fo = int(1.2 * SR); fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
mix *= fade

# ---- master: loudness to -14 LUFS, then a 4x-oversampled lookahead limiter to -1 dBTP
meter = pyln.Meter(SR)


def tp(x):
    return np.abs(resample_poly(x, 4, 1)).max()


def limit(x, ceil):
    up = np.abs(resample_poly(x, 4, 1))[::4][: len(x)]
    need = np.minimum(1, ceil / np.maximum(np.maximum(up, np.abs(x)), 1e-9))
    la = int(0.004 * SR)  # 4 ms lookahead/attack, 120 ms release
    from scipy.ndimage import minimum_filter1d
    g = minimum_filter1d(need, la * 2 + 1)
    a = np.exp(-1 / (0.12 * SR))
    out = np.empty_like(g); cur = 1.0
    for i in range(len(g)):  # smooth release (attack is instant on the pre-min'd curve)
        cur = g[i] if g[i] < cur else a * cur + (1 - a) * g[i]
        out[i] = cur
    return x * out


# a touch of width: the right channel carries an 11 ms offset copy (decorrelates the reverb tail)
st = np.stack([mix, mix * 0.92 + np.roll(mix, int(0.011 * SR)) * 0.08], 1)


def limit_st(st, ceil):
    """Stereo-linked: one gain curve from the louder channel's (oversampled) peak."""
    pk = np.maximum(*[np.maximum(np.abs(resample_poly(st[:, c], 4, 1)).reshape(-1, 4).max(1)[: len(st)],
                                 np.abs(st[:, c])) for c in (0, 1)])
    need = np.minimum(1, ceil / np.maximum(pk, 1e-9))
    from scipy.ndimage import minimum_filter1d
    g = minimum_filter1d(need, int(0.004 * SR) * 2 + 1)
    a = np.exp(-1 / (0.12 * SR)); out = np.empty_like(g); cur = 1.0
    for i in range(len(g)):
        cur = g[i] if g[i] < cur else a * cur + (1 - a) * g[i]
        out[i] = cur
    return st * out[:, None], out


for _ in range(5):
    L = meter.integrated_loudness(st)
    st *= 10 ** ((-14.0 - L) / 20)
    st, gr = limit_st(st, 10 ** (-1.3 / 20))
L = meter.integrated_loudness(st)
P = 20 * np.log10(max(tp(st[:, 0]), tp(st[:, 1])))
print(f'integrated {L:.2f} LUFS, true peak {P:.2f} dBTP, max gain reduction {20*np.log10(gr.min()):.1f} dB')
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'work/v2/score.wav', st, SR, subtype='PCM_24')
