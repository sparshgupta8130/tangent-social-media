"""Original score for The Museum of Men video, synthesised from scratch (no samples, no loops).

    python score.py work/score.wav
Soft felt-piano + warm pad at 70 BPM in D, gallery room tone (filtered noise), a faint air
movement under each lateral glide. Cue points come from build.py's timeline:
intro on the row -> exhibits 1-6 (gentle arpeggios) -> the phone (a lift: higher voicing,
pad swell) -> back to the row (space, single notes) -> end card (resolves to D).
Mastered to -14 LUFS integrated, true peak <= -1 dBTP (4x oversampled limiter).
"""
import sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly
import soundfile as sf
import pyloudnorm as pyln

sys.path.insert(0, __import__('os').path.dirname(__file__))
import build as B  # timeline only

SR = 48000
DUR = B.TOTAL
N = int(SR * (DUR + 0.05))
rng = np.random.default_rng(19)
BEAT = 60 / 70
midi = lambda m: 440.0 * 2 ** ((m - 69) / 12)
lp = lambda x, f, o=2: sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
hp = lambda x, f, o=2: sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)


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


piano_b, pad_b, amb = np.zeros(N), np.zeros(N), np.zeros(N)

# chords (MIDI): bass, then voicing
Dmaj9 = (38, [62, 66, 69, 73, 76]); Bm9 = (35, [62, 66, 69, 73]); Gmaj7 = (31, [59, 62, 66, 71])
Aadd4 = (33, [61, 62, 64, 69]); Em9 = (28, [59, 62, 66, 67]); F_m7 = (30, [61, 64, 69, 73])
Gadd9 = (31, [57, 62, 67, 71]); Asus = (33, [62, 64, 69, 74])
BAR = 4 * BEAT


def bar_chords(t0, t1, prog):
    bars, t, i = [], t0, 0
    while t < t1 - 0.2:
        bars.append((t, prog[i % len(prog)])); t += BAR; i += 1
    return bars


def arp(t0, ch, vel=0.42, pattern=(0, 2, 1, 3, 2, 1), octave=0, step=BEAT / 2, n=8):
    bass, v = ch
    add(piano_b, piano(bass + 12, 6.0, vel * 0.9), t0)
    for j in range(n):
        m = v[pattern[j % len(pattern)] % len(v)] + octave
        add(piano_b, piano(m, 3.5, vel * (0.85 + 0.15 * rng.random())), t0 + BEAT + j * step * 0.999)


# 0 - 6.2: the row. Pad in, a few spaced notes.
add(pad_b, pad([50, 57, 62, 66], 7.5, att=2.0, rel=2.5), 0.0, 1.0)
for t, m, v in ((0.25, 74, 0.45), (1.9, 69, 0.38), (3.3, 73, 0.40), (4.6, 66, 0.35)):
    add(piano_b, piano(m, 5, v), t)
add(piano_b, piano(38, 7, 0.45), 0.25)

# 6.2 - 38.0: exhibits 1-6, gentle arpeggios, bar-aligned from exhibit 1's arrival
prog = [Dmaj9, Bm9, Gmaj7, Aadd4]
for t, ch in bar_chords(B.DISS1 - BEAT, B.ARR[6] - 0.2, prog):
    arp(t, ch, 0.40, n=6)
    add(pad_b, pad([c for c in ch[1][:3]], BAR + 2.2, att=1.2, rel=2.0, bright=800), t, 0.7)

# 38.0 - 44.8: the phone. A lift: Em9 -> F#m7 -> Gadd9 -> Asus, higher octave, pad swell
lift = [Em9, F_m7, Gadd9, Asus]
tl = B.ARR[6] - 0.2
for i, ch in enumerate(lift):
    t = tl + i * (B.HOLD7 / 4)
    bass, v = ch
    add(piano_b, piano(bass + 12, 5, 0.42), t)
    for j, m in enumerate(v[1:] + [v[0] + 12]):
        add(piano_b, piano(m + 12, 3.0, 0.36 + 0.03 * i), t + 0.45 + j * 0.30)
add(pad_b, pad([55, 62, 66, 71, 74], B.HOLD7 + 1.5, att=3.5, rel=1.2, bright=1500), tl, 1.15)

# 44.8 - 51.8: back to the row. Space: bass + single high notes
add(piano_b, piano(35, 7, 0.40), B.CUT + 0.05)
add(pad_b, pad([47, 54, 59, 62], 7.8, att=1.0, rel=2.5, bright=700), B.CUT, 0.8)
for t, m, v in ((0.7, 74, 0.36), (2.4, 73, 0.32), (4.1, 69, 0.30), (5.6, 71, 0.30)):
    add(piano_b, piano(m, 5, v), B.CUT + t)

# 51.8 -> end: resolve to D, a final chord left to ring
te = B.END_D0 + 0.4
add(piano_b, piano(31, 6, 0.38), B.END_D0 - 0.6); add(piano_b, piano(69, 4, 0.3), B.END_D0 - 0.3)
add(piano_b, piano(38, 8, 0.48), te); add(piano_b, piano(26, 8, 0.35), te)
for j, m in enumerate((62, 66, 69, 73, 76, 81)):
    add(piano_b, piano(m, 7, 0.40), te + 0.35 + j * 0.22)
add(pad_b, pad([50, 57, 62, 66, 69], DUR - B.END_D0 + 0.5, att=2.0, rel=3.5, bright=1000), B.END_D0, 0.95)

# room tone: soft filtered noise, slow drift; air movement under each glide
room = lp(hp(rng.normal(0, 1, N), 70), 900, 4)
room = room * (1 + 0.15 * np.sin(2 * np.pi * 0.05 * np.arange(N) / SR)) * 0.010
amb += room
for i in range(1, 7):
    t0 = B.ARR[i - 1] + B.HOLD
    n = int(B.GLIDE * SR); tt = np.arange(n) / n
    sw = hp(lp(rng.normal(0, 1, n), 1600), 250) * np.sin(np.pi * tt) ** 2 * 0.012
    add(amb, sw, t0)

mix = reverb(piano_b + pad_b * 0.55, 3.4, 0.34) + amb
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
sf.write(sys.argv[1] if len(sys.argv) > 1 else 'work/score.wav', st, SR, subtype='PCM_24')
