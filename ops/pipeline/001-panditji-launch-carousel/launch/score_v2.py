"""Score v2 for the Panditji launch Short: upbeat bhangra-pop, synthesised from scratch (no samples, no licensed audio).

v1 (`score.py`, tanpura + santoor + soft beat) was rejected by Sparsh 2026-11-12 as too mellow ("doesn't even
feel like there is a background score"). v2 keeps 96 BPM, a natural bhangra tempo, so every scene change still
lands on a bar line (bar = 2.5 s), and drives from frame 0:

    bars 0-3   dhol chaal + tumbi riff + claps from the first beat; riser in bar 3
    bar  4     the phone lands: impact, four-on-the-floor kick, offbeat bass, chord stabs, shaker
    bars 5-8   full groove
    bars 9-14  lift: tumbi doubled an octave up, extra dhol rolls at phrase ends
    bars 15-16 "it says no": half-time dhol, filtered stabs, riser into the drop
    bars 17-20 drop: everything, the biggest section
    bars 21-22 end card: riff once more, final "dha!" hit on bar 22, tail to 58 s

Instruments: dhol (dagga bass head + tilli stick, swung), tumbi (bright short Karplus-Strong pluck), kick,
clap, shaker, saw bass, saw chord stabs, riser, impact. Raag Bhupali notes (D E F# A B) over D - Bm - G - A.

Usage: python score_v2.py out.wav
"""
import sys
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
S16 = BEAT / 4
LENGTH = 58.0
N = int(LENGTH * SR)
rng = np.random.default_rng(11)
SWING = 0.62  # swung offbeat position inside a beat (0.5 = straight, 0.667 = triplet)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def place(buf, x, t, g=1.0):
    i = int(round(t * SR))
    if i < 0 or i >= len(buf):
        return
    x = x[: len(buf) - i]
    buf[i:i + len(x)] += g * x


def filt(x, kind, fc, order=2):
    wn = np.array(fc) / (SR / 2) if np.ndim(fc) else fc / (SR / 2)
    b, a = signal.butter(order, wn, kind)
    return signal.lfilter(b, a, x)


def env(n, a, d):
    t = np.arange(n) / SR
    return (1 - np.exp(-t / a)) * np.exp(-t / d)


# ---------- instruments ----------
def dagga(vel=1.0):  # dhol bass head: a pitched thump with a slap
    n = int(0.5 * SR); t = np.arange(n) / SR
    f = 62 + 70 * np.exp(-t / 0.03)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    x += 0.35 * np.sin(2 * np.pi * np.cumsum(f * 1.52) / SR) * np.exp(-t / 0.08)
    x += 0.25 * filt(rng.uniform(-1, 1, n), 'low', 1200) * np.exp(-t / 0.015)
    return vel * x


def tilli(vel=1.0):  # dhol treble head, played with a thin stick: a bright, dry "tak"
    n = int(0.12 * SR); t = np.arange(n) / SR
    x = filt(rng.uniform(-1, 1, n), 'band', [1800, 7000]) * np.exp(-t / 0.028)
    x += 0.5 * np.sin(2 * np.pi * np.cumsum(520 + 300 * np.exp(-t / 0.01)) / SR) * np.exp(-t / 0.04)
    return vel * x


def kick():
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 50 + 110 * np.exp(-t / 0.03)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)
    x += 0.2 * filt(rng.uniform(-1, 1, n), 'high', 2500) * np.exp(-t / 0.003)
    return np.tanh(1.8 * x)


def clap():
    n = int(0.3 * SR); t = np.arange(n) / SR
    e = sum(np.where(t >= o, np.exp(-(t - o) / 0.007), 0) for o in (0, 0.009, 0.019)) + 0.7 * np.exp(-t / 0.09)
    return filt(rng.uniform(-1, 1, n), 'band', [1000, 4000]) * e * 0.7


def shaker(vel):
    n = int(0.07 * SR)
    return vel * filt(rng.uniform(-1, 1, n), 'high', 7000) * env(n, 0.003, 0.02)


def ks(f, dur, decay, bright):
    L = max(2, int(round(SR / f))); n = int(dur * SR)
    y = np.zeros(n + L + 1)
    b = rng.uniform(-1, 1, L)
    y[:L] = bright * b + (1 - bright) * np.convolve(b, np.ones(3) / 3, 'same')
    k = L
    while k < n + L:
        e = min(k + L, n + L)
        p1 = y[k - L:e - L]
        p2 = y[k - L - 1:e - L - 1] if k - L - 1 >= 0 else np.concatenate([[0], y[k - L:e - L - 1]])
        y[k:e] = decay * 0.5 * (p1 + p2)
        k = e
    return y[L:L + n]


def tumbi(m, vel=1.0, dur=0.6):  # one bright string, short and twangy
    x = ks(hz(m), dur, 0.992, 0.95) + 0.5 * ks(hz(m) * 2.003, dur, 0.985, 1.0)
    x = filt(x, 'high', 350)
    n = len(x); t = np.arange(n) / SR
    return vel * x * (1 - np.exp(-t / 0.001)) * np.exp(-t / 0.35)


def saw(freqs, dur, cutoff, det=(-0.08, 0, 0.08)):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        for d in det:
            x += signal.sawtooth(2 * np.pi * f * 2 ** (d / 12) * t + rng.random() * 6.28)
    return filt(x, 'low', cutoff) / (len(freqs) * len(det))


def stab(midis, cutoff=3200):
    x = saw([hz(m) for m in midis], 0.22, cutoff)
    return x * env(len(x), 0.002, 0.09)


def bassnote(m, dur=0.28):
    x = saw([hz(m)], dur, 900, det=(0,)) * 0.6 + np.sin(2 * np.pi * hz(m) * np.arange(int(dur * SR)) / SR)
    return x * env(len(x), 0.003, 0.12)


def riser(dur):
    n = int(dur * SR); t = np.arange(n) / SR; p = t / dur
    nz = rng.uniform(-1, 1, n)
    x = (1 - p) * filt(nz, 'low', 1200) + p * filt(nz, 'high', 3000)
    sweep = np.sin(2 * np.pi * np.cumsum(220 + 1400 * p ** 2) / SR) * 0.3
    return (x + sweep) * p ** 2


def impact():
    n = int(2.0 * SR); t = np.arange(n) / SR
    boom = np.sin(2 * np.pi * np.cumsum(40 + 80 * np.exp(-t / 0.05)) / SR) * np.exp(-t / 0.6)
    return boom + 0.5 * filt(rng.uniform(-1, 1, n), 'low', 3000) * np.exp(-t / 0.15)


def reverb(x, rt, mix, seed):
    r = np.random.default_rng(seed); t = np.arange(int(rt * SR)) / SR
    ir = filt(r.uniform(-1, 1, len(t)) * np.exp(-t * 6.9 / rt), 'low', 6000)
    ir /= np.sqrt(np.sum(ir ** 2))
    return (1 - mix) * x + mix * signal.fftconvolve(x, ir)[:len(x)]


# ---------- arrangement ----------
CH = [  # (bass root, stab voicing)
    (38, [62, 66, 69]),   # D
    (35, [62, 66, 71]),   # Bm
    (43, [62, 67, 71]),   # G
    (45, [61, 64, 69]),   # A
]
# tumbi riff, 16 steps per bar (None = rest), Bhupali: D E F# A B
RIFF_A = [74, None, 74, 76, 78, None, 76, 74, 69, None, 71, None, 74, None, None, None]
RIFF_B = [78, None, 78, 81, 78, 76, 74, None, 76, None, 74, 71, 69, None, 71, None]
RIFF_C = [74, 76, 78, 81, 83, None, 81, 78, 76, None, 78, 76, 74, None, None, None]

nbars = int(np.ceil(LENGTH / BAR))
dhol = np.zeros(N); perc = np.zeros(N); lead = np.zeros(N); bass = np.zeros(N); keys = np.zeros(N); fx = np.zeros(N)
side = np.zeros(N)  # kick envelope for sidechain pumping

FULL = set(range(4, 15)) | set(range(17, 21))
LIFT = set(range(9, 15)) | set(range(17, 21))
BREAK = {15, 16}
INTRO = {0, 1, 2, 3}


def swung(beat_start, step16):
    """time of a 16th step inside a beat, with the off-8th pushed late (swing)."""
    pos = {0: 0.0, 1: SWING / 2, 2: SWING, 3: SWING + (1 - SWING) / 2}[step16]
    return beat_start + pos * BEAT


for bar in range(nbars):
    t0 = bar * BAR
    if t0 >= 55.0 + BAR:
        break
    root, voicing = CH[(bar // 2) % 4]
    ending = bar >= 21

    # --- dhol chaal: dagga on 1, the swung "and" of 2, and 3; tilli on swung offbeats + fills
    if not ending or bar == 21:
        for b in range(4):
            tb = t0 + b * BEAT
            if bar in BREAK:  # half time
                if b in (0, 2):
                    place(dhol, dagga(1.0), tb, 0.9)
                place(dhol, tilli(0.8), swung(tb, 2), 0.5)
                continue
            if b in (0, 2):
                place(dhol, dagga(1.0), tb, 1.0)
            if b == 1:
                place(dhol, dagga(0.8), swung(tb, 2), 0.9)
            place(dhol, tilli(1.0), swung(tb, 2), 0.7)
            place(dhol, tilli(0.6), tb, 0.45 if b % 2 else 0.3)
            if bar in LIFT or bar in INTRO:
                place(dhol, tilli(0.5), swung(tb, 3), 0.35)
        # roll into the next phrase every second bar
        if bar % 2 == 1 and bar not in BREAK:
            for k in range(8):
                place(dhol, tilli(0.5 + 0.06 * k), t0 + 3 * BEAT + k * BEAT / 8, 0.5)

    # --- claps on 2 and 4 (from the first bar: the energy is there on frame 0)
    if not ending and bar not in BREAK:
        for b in (1, 3):
            place(perc, clap(), t0 + b * BEAT, 0.6)

    # --- full section: kick, shaker, bass, stabs
    if bar in FULL:
        for b in range(4):
            tb = t0 + b * BEAT
            place(perc, kick(), tb, 1.0)
            place(side, np.exp(-np.arange(int(0.25 * SR)) / SR / 0.09), tb, 1.0)
            for s in range(4):
                place(perc, shaker(0.9 if s == 2 else 0.45), swung(tb, s), 0.28)
            # offbeat bass, root and octave
            place(bass, bassnote(root + 12), swung(tb, 2), 0.9)
            if b in (0, 2):
                place(bass, bassnote(root, 0.2), tb, 0.6)
            # chord stabs on the swung offbeats of 2 and 4, plus a push before the bar
            if b in (1, 3):
                place(keys, stab(voicing), swung(tb, 2), 0.55)
        place(keys, stab(voicing), t0 + 3 * BEAT + SWING * BEAT + BEAT * 0.19, 0.35)
    if bar in BREAK:
        for b in (1, 3):
            place(keys, stab(voicing, 1100), swung(t0 + b * BEAT, 2), 0.5)

    # --- tumbi riff
    if bar not in BREAK and bar < 23:
        riff = RIFF_C if bar == 21 else (RIFF_B if bar % 2 else RIFF_A)
        for s, m in enumerate(riff):
            if m is None:
                continue
            ts = swung(t0 + (s // 4) * BEAT, s % 4)
            vel = 1.0 if s % 4 == 0 else 0.75
            place(lead, tumbi(m, vel), ts, 0.42 if bar in INTRO else 0.5)
            if bar in LIFT:
                place(lead, tumbi(m + 12, vel * 0.6, 0.4), ts, 0.28)

# break: a teasing tumbi call on the last half of bar 16
for k, m in enumerate([74, 76, 78, 81, 83, 86]):
    place(lead, tumbi(m, 0.9), 16 * BAR + 2 * BEAT + k * BEAT / 3, 0.45)

# ending: one big "dha!" on bar 22 with the chord, then let it ring
END = 22 * BAR
place(dhol, dagga(1.0), END, 1.3)
place(perc, kick(), END, 1.0)
place(keys, saw([hz(m) for m in (50, 62, 66, 69, 74)], 3.0, 2500) * env(int(3.0 * SR), 0.004, 0.9), END, 0.9)
place(bass, bassnote(38, 1.6), END, 0.9)
place(lead, tumbi(86, 1.0, 1.5), END, 0.5)
place(fx, impact(), END, 0.6)

# risers + impacts on the two drops
place(fx, riser(BAR), 3 * BAR, 0.55); place(fx, impact(), 4 * BAR, 0.8)
place(fx, riser(BAR), 16 * BAR, 0.6); place(fx, impact(), 17 * BAR, 0.8)

# sidechain pump
duck = 1 - 0.55 * np.clip(side, 0, 1)
keys *= duck; bass *= 1 - 0.35 * np.clip(side, 0, 1)

lead = reverb(lead, 1.3, 0.18, 1)
keys = reverb(keys, 1.6, 0.2, 2)
dhol = reverb(dhol, 0.9, 0.12, 3)
fx = reverb(fx, 2.2, 0.25, 4)


def wide(x, ms):
    d = int(ms / 1000 * SR)
    return np.stack([x, np.concatenate([np.zeros(d), x[:-d]]) if d else x], 1)


mix = (wide(dhol, 0) * 1.0 + wide(perc, 0) * 0.85 + wide(lead, 11) * 0.95 + wide(bass, 0) * 0.75
       + wide(keys, 8) * 0.7 + wide(fx, 6) * 0.6)
t = np.arange(N) / SR
mix *= np.clip((LENGTH - t) / 1.5, 0, 1)[:, None]
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(2.2 * mix) / np.tanh(2.2)   # glue + loudness
wavfile.write(sys.argv[1], SR, (mix * 0.9 * 32767).astype(np.int16))
print('wrote', sys.argv[1])
