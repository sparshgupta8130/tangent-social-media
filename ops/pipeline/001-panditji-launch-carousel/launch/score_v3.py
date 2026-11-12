"""Score v3 for the Panditji launch Short: upbeat but smooth. Synthesised from scratch (no samples, no licensed audio).

History (Sparsh, 2026-11-12): v1 (`score.py`) "too mellow"; v2 (`score_v2.py`, bhangra-pop) "too jarring".
v3 keeps v2's drive and drops what made it harsh:
  - no noise-burst percussion up front: the dhol stick and claps are gone; a soft finger-snap and quiet,
    filtered hats carry the backbeat
  - straight 16ths, no swing (synthetic swing read as sloppy)
  - motion comes from melody instead: a santoor hook plus a 16th-note santoor arpeggio, a pumping warm pad
    and a driving 8th-note bass
  - a rounded kick, a gentle limiter instead of hard saturation, -14 LUFS

96 BPM, bar = 2.5 s, so every scene change still lands on a bar line.
    bars 0-3   santoor hook + arpeggio, snaps, soft kick on 1 and 3; gentle riser in bar 3
    bar  4     the phone lands: sub boom, four-on-the-floor, bass, pumping pad
    bars 9-14  lift: hook doubled an octave up
    bars 15-16 "it says no": kick and bass out, pad and arpeggio only, riser
    bars 17-20 drop: full
    bars 21-23 end card: hook resolves, held chord, tail

Usage: python score_v3.py out.wav
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
rng = np.random.default_rng(21)


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


def kick(vel=1.0):  # rounded: no click, no distortion
    n = int(0.4 * SR); t = np.arange(n) / SR
    f = 48 + 75 * np.exp(-t / 0.04)
    return vel * np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.18)


def snap(vel=1.0):  # soft finger snap: short, mid-band, quiet
    n = int(0.12 * SR); t = np.arange(n) / SR
    x = filt(rng.uniform(-1, 1, n), 'band', [1400, 3200]) * env(n, 0.001, 0.025)
    x += 0.3 * np.sin(2 * np.pi * 1900 * t) * env(n, 0.001, 0.012)
    return vel * x


def hat(vel=1.0):
    n = int(0.05 * SR)
    return vel * filt(filt(rng.uniform(-1, 1, n), 'high', 6000), 'low', 11000) * env(n, 0.001, 0.012)


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


def santoor(m, vel=1.0, dur=1.6, bright=0.6):  # paired strings, rounded attack
    x = 0.5 * (ks(hz(m), dur, 0.9965, bright) + ks(hz(m) * 1.003, dur, 0.9963, bright))
    x = filt(filt(x, 'high', 200), 'low', 6500)
    n = len(x); t = np.arange(n) / SR
    return vel * x * (1 - np.exp(-t / 0.003))


def pad(midis, dur, cutoff):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for m in midis:
        for d in (-0.06, 0, 0.06):
            x += signal.sawtooth(2 * np.pi * hz(m + d) * t + rng.random() * 6.28)
    x = filt(x, 'low', cutoff)
    return x * np.minimum(1, t / 0.4) * np.clip((dur - t) / 0.4, 0, 1) / (3 * len(midis))


def bassnote(m, dur=0.27):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * hz(m) * t) + 0.25 * filt(signal.sawtooth(2 * np.pi * hz(m) * t), 'low', 500)
    return x * env(n, 0.004, 0.16)


def riser(dur):  # soft: a filtered noise swell and a rising tone, no harsh top
    n = int(dur * SR); t = np.arange(n) / SR; p = t / dur
    x = filt(rng.uniform(-1, 1, n), 'band', [400, 4000]) * 0.6
    x += 0.35 * np.sin(2 * np.pi * np.cumsum(300 + 900 * p ** 2) / SR)
    return x * p ** 2.5


def boom():
    n = int(1.6 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * np.cumsum(38 + 50 * np.exp(-t / 0.08)) / SR) * env(n, 0.003, 0.5)


def reverb(x, rt, mix, seed):
    r = np.random.default_rng(seed); t = np.arange(int(rt * SR)) / SR
    ir = filt(r.uniform(-1, 1, len(t)) * np.exp(-t * 6.9 / rt), 'low', 5000)
    ir /= np.sqrt(np.sum(ir ** 2))
    return (1 - mix) * x + mix * signal.fftconvolve(x, ir)[:len(x)]


CH = [  # (bass root, pad voicing, arpeggio cell of 4 notes)
    (38, [50, 57, 62, 66], [62, 66, 69, 74]),   # D
    (35, [47, 54, 59, 62], [59, 62, 66, 71]),   # Bm
    (43, [43, 50, 55, 59], [55, 59, 62, 67]),   # G
    (45, [45, 52, 57, 61], [57, 61, 64, 69]),   # A
]
# the hook (16ths, None = rest): Bhupali D E F# A B, two-bar call and answer
HOOK_A = [74, None, None, 76, 78, None, 76, None, 74, None, 69, None, 71, None, None, None]
HOOK_B = [78, None, None, 81, 78, None, 76, None, 74, None, 76, None, 74, None, None, None]
HOOK_END = [81, None, 78, None, 76, None, 74, None, 71, None, 69, None, 74, None, None, None]

FULL = set(range(4, 15)) | set(range(17, 21))
LIFT = set(range(9, 15)) | set(range(17, 21))
BREAK = {15, 16}

drums = np.zeros(N); hook = np.zeros(N); arp = np.zeros(N); padb = np.zeros(N); bass = np.zeros(N); fx = np.zeros(N)
side = np.zeros(N)

for bar in range(22):
    t0 = bar * BAR
    root, voicing, cell = CH[(bar // 2) % 4]
    full = bar in FULL

    # drums
    for b in range(4):
        tb = t0 + b * BEAT
        if full or (bar < 4 and b in (0, 2)) or (bar in BREAK and b == 0 and bar == 15):
            place(drums, kick(1.0 if full else 0.7), tb, 0.95)
            place(side, np.exp(-np.arange(int(0.3 * SR)) / SR / 0.11), tb, 1.0 if full else 0.5)
        if b in (1, 3) and bar not in BREAK:
            place(drums, snap(), tb, 0.5)
        if full or bar < 4:
            place(drums, hat(0.9), tb + BEAT / 2, 0.22)
            if full:
                place(drums, hat(0.45), tb + BEAT / 4, 0.16)
                place(drums, hat(0.45), tb + 3 * BEAT / 4, 0.16)

    # pad: one chord per two bars, brighter when full
    if bar % 2 == 0:
        cutoff = 1300 if bar < 4 else (900 if bar in BREAK else 2200)
        place(padb, pad(voicing, 2 * BAR + 0.3, cutoff), t0, 0.9)

    # bass: driving 8ths in the full sections
    if full:
        for k in range(8):
            m = root + (12 if k % 2 else 0)
            place(bass, bassnote(m), t0 + k * BEAT / 2, 0.75 if k % 2 == 0 else 0.5)

    # santoor arpeggio, 16ths, always on (it is the motor)
    for s in range(16):
        m = cell[s % 4] + (12 if (s // 4) % 2 and bar in LIFT else 0)
        vel = 0.85 if s % 4 == 0 else 0.55
        place(arp, santoor(m, vel, 0.9, 0.5), t0 + s * S16, 0.22 if bar < 4 else 0.26)

    # hook
    if bar not in BREAK:
        h = HOOK_END if bar == 21 else (HOOK_B if bar % 2 else HOOK_A)
        for s, m in enumerate(h):
            if m is None:
                continue
            place(hook, santoor(m, 1.0, 1.8, 0.7), t0 + s * S16, 0.5)
            if bar in LIFT:
                place(hook, santoor(m + 12, 0.7, 1.4, 0.6), t0 + s * S16, 0.25)

# end: held D chord, a last high D, the bass, a soft boom; the arpeggio stopped at bar 22
END = 22 * BAR
place(padb, pad([50, 57, 62, 66, 69], 3.0, 1800), END, 1.0)
place(hook, santoor(86, 0.9, 3.0, 0.6), END, 0.45)
place(hook, santoor(74, 0.9, 3.0, 0.6), END, 0.45)
place(bass, bassnote(38, 1.6), END, 0.9)
place(fx, boom(), END, 0.6)

place(fx, riser(BAR), 3 * BAR, 0.5); place(fx, boom(), 4 * BAR, 0.9)
place(fx, riser(BAR), 16 * BAR, 0.55); place(fx, boom(), 17 * BAR, 0.9)

# pumping pad and bass under the kick: motion without harshness
padb *= 1 - 0.5 * np.clip(side, 0, 1)
bass *= 1 - 0.3 * np.clip(side, 0, 1)

hook = reverb(hook, 1.8, 0.25, 1)
arp = reverb(arp, 1.5, 0.22, 2)
padb = reverb(padb, 2.5, 0.25, 3)
fx = reverb(fx, 2.0, 0.25, 4)
drums = reverb(drums, 0.8, 0.08, 5)


def wide(x, ms):
    d = int(ms / 1000 * SR)
    return np.stack([x, np.concatenate([np.zeros(d), x[:-d]]) if d else x], 1)


mix = (wide(drums, 0) * 0.9 + wide(hook, 10) * 1.0 + wide(arp, 14) * 0.8 + wide(padb, 8) * 0.8
       + wide(bass, 0) * 0.8 + wide(fx, 6) * 0.6)
t = np.arange(N) / SR
mix *= np.clip((LENGTH - t) / 1.5, 0, 1)[:, None]
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(1.15 * mix) / np.tanh(1.15)   # gentle limiting only
wavfile.write(sys.argv[1], SR, (mix * 0.9 * 32767).astype(np.int16))
print('wrote', sys.argv[1])
