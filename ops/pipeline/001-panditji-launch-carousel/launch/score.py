"""Original score for the Panditji launch Short, synthesised from scratch (no samples, no licensed audio).

96 BPM (beat 0.625 s, bar 2.5 s). Raag Bhupali colour (Sa Re Ga Pa Dha in D) over a D - Bm - G - A
progression: tanpura drone, paired-string santoor plucks (Karplus-Strong), warm pad, sub, soft kick,
shaker and claps, two risers into impacts. Scene changes in the video land on the bar lines below.

    bars 0-1   hook            drone + pad only
    bars 2-3   the gap         santoor enters, riser into bar 4
    bar  4     phone lands     impact, beat starts
    bars 5-14  features        full groove (claps from bar 9)
    bars 15-16 "it says no"    break: drums out, filtered pad, riser into bar 17
    bars 17-20 trust + get it  full groove, biggest energy
    bars 21-23 end card        drums out, final chord, santoor phrase, tail

Usage: python score.py out.wav
"""
import sys
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
LENGTH = 58.0
N = int(LENGTH * SR)
rng = np.random.default_rng(7)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def place(buf, x, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf):
        return
    x = x[: len(buf) - i]
    buf[i : i + len(x)] += gain * x


def lp(x, fc, order=2):
    b, a = signal.butter(order, fc / (SR / 2), 'low')
    return signal.lfilter(b, a, x)


def hp(x, fc, order=2):
    b, a = signal.butter(order, fc / (SR / 2), 'high')
    return signal.lfilter(b, a, x)


def bp(x, lo, hi, order=2):
    b, a = signal.butter(order, [lo / (SR / 2), hi / (SR / 2)], 'band')
    return signal.lfilter(b, a, x)


# ---------- instruments ----------
def tanpura(f, dur=6.0):
    t = np.arange(int(dur * SR)) / SR
    out = np.zeros_like(t)
    for n in range(1, 34):
        if f * n > 9000:
            break
        # jawari: a slow bump that travels up the harmonic series gives the buzzing shimmer
        centre = 4 + 18 * (t / dur)
        shimmer = 0.35 + 0.65 * np.exp(-((n - centre) ** 2) / 18)
        env = np.exp(-t / (2.6 + 0.4 * rng.random())) * (1 - np.exp(-t / 0.01))
        out += (1 / n ** 0.85) * shimmer * env * np.sin(2 * np.pi * f * n * t + rng.random() * 6.28)
    return out / 6


def ks_string(f, dur, decay=0.9965, bright=0.5):
    """Karplus-Strong, vectorised one period at a time."""
    L = max(2, int(round(SR / f)))
    n = int(dur * SR)
    y = np.zeros(n + L + 1)
    burst = rng.uniform(-1, 1, L)
    burst = bright * burst + (1 - bright) * np.convolve(burst, np.ones(3) / 3, 'same')
    y[:L] = burst
    k = L
    while k < n + L:
        end = min(k + L, n + L)
        prev = y[k - L : end - L]
        prev2 = y[k - L - 1 : end - L - 1] if k - L - 1 >= 0 else np.concatenate([[0], y[k - L : end - L - 1]])
        y[k:end] = decay * 0.5 * (prev + prev2)
        k = end
    return y[L : L + n]


def santoor(f, dur=2.4, vel=1.0):
    a = ks_string(f, dur, 0.9968, 0.75)
    b = ks_string(f * 1.0035, dur, 0.9966, 0.75)  # paired, slightly detuned strings
    x = (a + b) * 0.5
    x = hp(x, 180)
    t = np.arange(len(x)) / SR
    return vel * x * (1 - np.exp(-t / 0.002))


def pad_chord(midis, dur, cutoff=1400):
    t = np.arange(int(dur * SR)) / SR
    x = np.zeros_like(t)
    for m in midis:
        for det in (-0.07, 0.0, 0.07):
            x += signal.sawtooth(2 * np.pi * hz(m + det) * t + rng.random() * 6.28)
    x = lp(x, cutoff, 2)
    env = np.minimum(1, t / 1.2) * np.minimum(1, (dur - t) / 1.0).clip(0, 1)
    return x * env / (len(midis) * 3)


def kick():
    t = np.arange(int(0.45 * SR)) / SR
    f = 46 + 90 * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t / 0.22)
    x += 0.15 * hp(rng.uniform(-1, 1, len(t)), 3000) * np.exp(-t / 0.004)
    return x


def shaker(vel=1.0):
    t = np.arange(int(0.09 * SR)) / SR
    return vel * hp(rng.uniform(-1, 1, len(t)), 8000) * np.exp(-t / 0.022) * (1 - np.exp(-t / 0.004))


def clap():
    t = np.arange(int(0.35 * SR)) / SR
    env = np.zeros_like(t)
    for off in (0.0, 0.011, 0.022):
        env += np.where(t >= off, np.exp(-(t - off) / 0.008), 0)
    env += 0.6 * np.exp(-t / 0.11)
    return bp(rng.uniform(-1, 1, len(t)), 900, 2600) * env * 0.6


def sub(f, dur):
    t = np.arange(int(dur * SR)) / SR
    env = np.minimum(1, t / 0.08) * np.minimum(1, (dur - t) / 0.1).clip(0, 1)
    return np.sin(2 * np.pi * f * t) * env


def riser(dur):
    t = np.arange(int(dur * SR)) / SR
    p = t / dur
    noise = rng.uniform(-1, 1, len(t))
    x = (1 - p) * lp(noise, 900) + p * hp(noise, 2500)  # smooth crossfade dark -> bright
    sweep = np.sin(2 * np.pi * np.cumsum(180 + 700 * p ** 2) / SR) * 0.25
    return (x * 0.9 + sweep) * p ** 2.2


def impact():
    t = np.arange(int(2.2 * SR)) / SR
    f = 38 + 60 * np.exp(-t / 0.06)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.7)
    hit = lp(rng.uniform(-1, 1, len(t)), 2500) * np.exp(-t / 0.18) * 0.5
    return boom + hit


def reverb(x, rt=2.2, mix=0.28, seed=0):
    r = np.random.default_rng(seed)
    t = np.arange(int(rt * SR)) / SR
    ir = r.uniform(-1, 1, len(t)) * np.exp(-t * 6.9 / rt)
    ir = lp(ir, 5000)
    ir /= np.sqrt(np.sum(ir ** 2))
    wet = signal.fftconvolve(x, ir)[: len(x)]
    return (1 - mix) * x + mix * wet


# ---------- arrangement ----------
D2, D3, D4 = 38, 50, 62
CHORDS = [  # (root midi for sub, pad voicing, Bhupali-safe arpeggio notes)
    (38, [50, 54, 57, 62], [62, 66, 69, 74, 71, 69, 66, 64]),   # D
    (35, [47, 50, 54, 59], [59, 62, 66, 71, 69, 66, 62, 64]),   # Bm
    (43, [43, 50, 55, 59], [62, 67, 71, 74, 71, 69, 67, 64]),   # G (Ga->Ma colour on top)
    (45, [45, 52, 57, 61], [64, 69, 73, 76, 73, 69, 66, 64]),   # A
]

drone = np.zeros(N)
pad = np.zeros(N)
strings = np.zeros(N)
drums = np.zeros(N)
bass = np.zeros(N)
fx = np.zeros(N)
kick_env = np.zeros(N)

nbars = int(np.ceil(LENGTH / BAR))
GROOVE = set(range(4, 15)) | set(range(17, 21))
CLAPS = set(range(9, 15)) | set(range(17, 21))
SANTOOR = set(range(2, 15)) | set(range(17, 21))

# tanpura: Pa Sa Sa Sa(low), one cycle per bar
for bar in range(nbars):
    t0 = bar * BAR
    for k, m in enumerate((45, 50, 50, 38)):
        place(drone, tanpura(hz(m)), t0 + k * BEAT, 0.5 if bar in GROOVE else 0.8)

for bar in range(0, nbars, 2):
    root, voicing, arp = CHORDS[(bar // 2) % 4]
    t0 = bar * BAR
    dur = min(2 * BAR + 1.0, LENGTH - t0)
    cutoff = 900 if bar < 4 else (700 if bar in (15, 16) else 1600)
    place(pad, pad_chord(voicing, dur, cutoff), t0, 1.0)

    for b in (bar, bar + 1):
        tb = b * BAR
        if b in GROOVE:
            place(bass, sub(hz(root + 12 if root < 40 else root), BAR), tb, 0.55)
        if b in SANTOOR:
            sparse = b in (2, 3)
            for i, m in enumerate(arp):
                if sparse and i % 2:
                    continue
                vel = (1.0 if i % 4 == 0 else 0.7) * (0.8 if sparse else 1.0)
                place(strings, santoor(hz(m)), tb + i * (BAR / 8), 0.38 * vel)
        if b in GROOVE:
            for i in range(4):
                if i in (0, 2) or (i == 3 and b % 2):
                    tk = tb + i * BEAT + (BEAT / 2 if i == 3 else 0)
                    place(drums, kick(), tk, 0.9)
                    place(kick_env, np.exp(-np.arange(int(0.3 * SR)) / SR / 0.12), tk, 1.0)
            for i in range(16):
                place(drums, shaker(0.55 if i % 4 == 2 else 0.3), tb + i * BEAT / 4, 0.11)
        if b in CLAPS:
            for i in (1, 3):
                place(drums, clap(), tb + i * BEAT, 0.35)

# break (bars 15-16): sparse high santoor, a question left hanging
for i, m in enumerate([74, 0, 71, 69, 0, 0, 66, 0, 74, 76, 0, 74, 0, 0, 0, 0]):
    if m:
        place(strings, santoor(hz(m), 2.8), 15 * BAR + i * BEAT / 2, 0.3)

# ending (bars 21-23): descending Bhupali phrase over a held D
for i, m in enumerate([78, 76, 74, 71, 69, 66, 64, 62]):
    place(strings, santoor(hz(m), 3.5), 21 * BAR + i * BEAT * 0.75, 0.34)
place(strings, santoor(hz(50), 5.0), 22 * BAR + BEAT * 2, 0.4)
place(bass, sub(hz(38), 5.5), 21 * BAR, 0.5)

# risers + impacts
place(fx, riser(2.5), 3 * BAR, 0.5)
place(fx, impact(), 4 * BAR, 0.9)
place(fx, riser(2.5), 16 * BAR, 0.5)
place(fx, impact(), 17 * BAR, 0.8)

# sidechain pump: pad and bass duck under the kick
duck = 1 - 0.45 * np.clip(kick_env, 0, 1)
pad *= duck
bass *= 1 - 0.6 * np.clip(kick_env, 0, 1)

strings = reverb(strings, 2.4, 0.33, 1)
pad = reverb(pad, 3.0, 0.25, 2)
drone = reverb(drone, 2.0, 0.2, 3)
fx = reverb(fx, 2.6, 0.3, 4)


def stereo(x, ms):  # width by a short Haas delay on one side
    d = int(ms / 1000 * SR)
    r = np.concatenate([np.zeros(d), x[:-d]]) if d else x
    return np.stack([x, r], 1)


mix = (
    stereo(drone, 0) * 0.55
    + stereo(pad, 9) * 0.9
    + stereo(strings, 12) * 1.0
    + stereo(bass, 0) * 0.9
    + stereo(drums, 0) * 0.8
    + stereo(fx, 7) * 0.7
)
# fades and a gentle master glue
t = np.arange(N) / SR
mix *= np.minimum(1, t / 0.05)[:, None] * np.clip((LENGTH - t) / 2.0, 0, 1)[:, None]
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(1.6 * mix) / np.tanh(1.6)
wavfile.write(sys.argv[1], SR, (mix * 0.89 * 32767).astype(np.int16))
print('wrote', sys.argv[1], f'{LENGTH}s', 'bars', nbars)
