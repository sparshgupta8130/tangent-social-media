"""Instruments for the Panditji festive reels, synthesised from scratch (no samples). From the launch reel score."""
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
import wave, sys

SR = 44100
import os
DUR = float(os.environ.get('REEL_DUR', '9.0'))  # set by score.py per reel
N = int(SR * DUR)
rng = np.random.default_rng(42)
BEAT = 0.5
SIX = 0.125  # a 16th


def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def buf():
    return np.zeros(N)


def add(dst, sig, t, gain=1.0):
    sig = np.array(sig, dtype=float)
    # short fade edges on every event: no clicks where a sound is cut while still ringing
    fi, fo = min(len(sig), int(0.001 * SR)), min(len(sig), int(0.012 * SR))
    if fi: sig[:fi] *= np.linspace(0, 1, fi)
    if fo: sig[-fo:] *= np.linspace(1, 0, fo)
    i = int(t * SR)
    if i >= N:
        return
    j = min(N, i + len(sig))
    dst[i:j] += sig[: j - i] * gain


def env_exp(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))


def lp(x, f, order=2):
    return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)


# ---------------- instruments ----------------
def sitar(f, dur, bend=True, bright=0.5):
    """Karplus-Strong pluck with a meend (pitch glide up from below) and a jawari buzz."""
    n = int(dur * SR)
    period = SR / f
    L = int(period)
    out = np.zeros(n)
    line = rng.uniform(-1, 1, L) * 0.9
    line = lp(line, 2000 + 6000 * bright) if L > 30 else line
    idx = 0
    # pitch glide: shorten the delay line over the first 60 ms (approximate meend)
    for k in range(n):
        out[k] = line[idx]
        nxt = (idx + 1) % L
        line[idx] = 0.5 * (line[idx] + line[nxt]) * 0.997
        idx = nxt
    if bend:
        # resample for a gentle upward glide of ~70 cents settling in 80 ms
        tt = np.arange(n) / SR
        cents = -70 * np.exp(-tt / 0.03)
        ratio = 2 ** (cents / 1200)
        pos = np.cumsum(ratio)
        pos = pos[pos < n - 1]
        out = np.interp(pos, np.arange(n), out)
        out = np.pad(out, (0, n - len(out)))
    buzz = np.tanh(hp(out, 1800) * 6) * 0.18  # jawari: a bright, buzzy edge
    sig = out + buzz
    sig *= env_exp(n, dur * 0.45)
    return sig * 0.8


def kick(gain=1.0):
    n = int(0.42 * SR)
    t = np.arange(n) / SR
    f = 45 + 95 * np.exp(-t / 0.045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 0.16)
    click = hp(rng.standard_normal(n), 3000) * np.exp(-t / 0.004) * 0.25
    return np.tanh((body + click) * 1.6) * gain


def clap():
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    noise = bp(rng.standard_normal(n), 900, 2600)
    e = np.zeros(n)
    for d in (0.0, 0.011, 0.022):
        e += (t >= d) * np.exp(-np.maximum(t - d, 0) / 0.007)
    e += (t >= 0.03) * np.exp(-np.maximum(t - 0.03, 0) / 0.09)
    return noise * e * 0.55


def hat(open_=False):
    n = int((0.25 if open_ else 0.06) * SR)
    t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7500, 4) * np.exp(-t / (0.08 if open_ else 0.014)) * 0.35


def shaker():
    n = int(0.07 * SR)
    t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 4000, 10000) * np.sin(np.pi * t / t[-1]) ** 2 * 0.12


def tabla_na():
    n = int(0.3 * SR)
    t = np.arange(n) / SR
    f = 520 * (1 + 0.04 * np.exp(-t / 0.01))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.07)
    ring = np.sin(2 * np.pi * 1040 * t) * np.exp(-t / 0.04) * 0.3
    slap = bp(rng.standard_normal(n), 1500, 5000) * np.exp(-t / 0.006) * 0.5
    return (tone + ring + slap) * 0.45


def tabla_ge():
    n = int(0.5 * SR)
    t = np.arange(n) / SR
    f = 85 + 45 * (1 - np.exp(-t / 0.08))  # the bayan's rising "ghe"
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.18)
    return np.tanh(tone * 1.4) * 0.55


def bass(m, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = midi(m)
    saw = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 9))
    sig = lp(saw, 900) * np.minimum(1, t / 0.005) * np.exp(-t / (dur * 0.6))
    sub = np.sin(2 * np.pi * f * t) * np.exp(-t / (dur * 0.7))
    return np.tanh((sig * 0.6 + sub * 0.45) * 1.2) * 0.45


def pad(ms, dur, cutoff=2500):
    n = int(dur * SR)
    t = np.arange(n) / SR
    sig = np.zeros(n)
    for m in ms:
        for det in (-0.12, 0.0, 0.12):
            f = midi(m + det)
            sig += sum(np.sin(2 * np.pi * f * k * t + rng.uniform(0, 6.28)) / k for k in range(1, 7))
    sig = lp(sig / (len(ms) * 3), cutoff)
    a = np.minimum(1, t / 0.02)
    return sig * a * np.exp(-t / (dur * 0.45)) * 0.5


def tanpura(dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    sig = np.zeros(n)
    for m, g, ph in ((38, 0.45, 0.0), (45, 0.7, 0.25), (50, 0.65, 0.5), (50, 0.5, 0.75)):
        f = midi(m)
        shimmer = 1 + 0.35 * np.sin(2 * np.pi * (0.5 + ph) * t + ph * 6)
        for k in range(1, 12):
            sig += g * np.sin(2 * np.pi * f * k * t + k * ph) / k ** 1.1 * (shimmer if k > 3 else 1)
    return lp(sig, 3500) * 0.05


def noise_sweep(dur, f0, f1, shape='up'):
    n = int(dur * SR)
    x = rng.standard_normal(n)
    out = np.zeros(n)
    chunks = 40
    for c in range(chunks):
        a, b = c * n // chunks, (c + 1) * n // chunks
        p = c / (chunks - 1)
        fc = f0 * (f1 / f0) ** p
        out[a:b] = bp(x[max(0, a - 2000):b], fc * 0.7, min(fc * 1.4, SR / 2 - 100))[-(b - a):]
    t = np.linspace(0, 1, n)
    amp = t ** 2 if shape == 'up' else np.sin(np.pi * t) ** 1.5
    return out * amp


def whoosh(dur=0.32):
    return noise_sweep(dur, 400, 5000, 'arc') * 0.55


def crash(dur=1.8):
    n = int(dur * SR)
    t = np.arange(n) / SR
    metal = sum(np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) for f in (3120, 4470, 5310, 6890, 8210)) * 0.05
    return (hp(rng.standard_normal(n), 5000) * 0.5 + metal) * np.exp(-t / 0.55) * 0.5


def boom():
    n = int(1.4 * SR)
    t = np.arange(n) / SR
    f = 32 + 40 * np.exp(-t / 0.12)
    return np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.35) * 2.0) * 0.5


def bell(f=880 * 1.0):
    n = int(2.2 * SR)
    t = np.arange(n) / SR
    parts = ((1, 1.0, 1.2), (2.0, 0.5, 0.9), (2.76, 0.45, 0.7), (5.4, 0.25, 0.4), (8.93, 0.12, 0.25))
    return sum(g * np.sin(2 * np.pi * f * r * t) * np.exp(-t / d) for r, g, d in parts) * 0.32


def blip(f, dur=0.05):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * np.sin(np.pi * t / t[-1]) * 0.25


def pop(f):
    n = int(0.16 * SR)
    t = np.arange(n) / SR
    fr = f * (1 + 0.6 * np.exp(-t / 0.01))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.05) * 0.4


def glitch():
    n = int(0.36 * SR)
    t = np.arange(n) / SR
    tone = np.sign(np.sin(2 * np.pi * (220 - 160 * t / t[-1]) * t)) * 0.3
    noise = rng.standard_normal(n) * 0.5
    gate = (np.floor(t * 34) % 2 == 0).astype(float)
    x = (tone + noise) * gate * np.exp(-t / 0.2)
    crushed = np.round(x * 8) / 8  # bit-crush
    return lp(crushed, 6000) * 0.55



# ---------------- festive additions ----------------
def fwump():
    """A flame catching: a soft low noise swell."""
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    env = np.minimum(1, t / 0.05) * np.exp(-t / 0.12)
    return lp(rng.standard_normal(n), 900) * env * 0.6


def boing(f0=330, f1=660, dur=0.35):
    """A cartoon spring: a sine that glides up with a wobble."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = f0 + (f1 - f0) * (1 - np.exp(-t / 0.05)) + 25 * np.sin(2 * np.pi * 18 * t) * np.exp(-t / 0.15)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * 0.3


def whistle(dur=0.45):
    """A rocket going up: a thin rising whistle."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 1400 + 1600 * (t / dur) ** 1.4
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / dur) ** 0.7 * 0.08 + hp(rng.standard_normal(n), 5000) * 0.02


def crackle(dur=1.2, density=90, seed=0):
    """Firework sparkle: many tiny decaying clicks."""
    n = int(dur * SR)
    out = np.zeros(n)
    r = np.random.default_rng(seed)
    for _ in range(int(density * dur)):
        i = int(r.uniform(0, 1) ** 1.6 * (n - 400))
        L = 300
        click = hp(r.standard_normal(L), 3000) * np.exp(-np.arange(L) / 40)
        out[i:i + L] += click * r.uniform(0.2, 1)
    return out * np.exp(-np.arange(n) / (dur * 0.5 * SR)) * 0.25


def burst():
    """A firework: a soft thump plus the crackle."""
    n = int(0.6 * SR)
    t = np.arange(n) / SR
    thump = np.sin(2 * np.pi * np.cumsum(60 + 80 * np.exp(-t / 0.03)) / SR) * np.exp(-t / 0.12) * 0.5
    noise = lp(rng.standard_normal(n), 2500) * np.exp(-t / 0.06) * 0.35
    return thump + noise


def dandiya(gain=1.0):
    """Two wooden sticks: a short, bright, resonant clack."""
    n = int(0.09 * SR)
    t = np.arange(n) / SR
    knock = sum(np.sin(2 * np.pi * f * t) * np.exp(-t / d) for f, d in ((1850, 0.018), (2900, 0.012), (4100, 0.008)))
    hit = bp(rng.standard_normal(n), 1500, 6000) * np.exp(-t / 0.004)
    return (knock * 0.25 + hit * 0.35) * gain


def tick(f=2200):
    n = int(0.03 * SR)
    t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * 0.5 + bp(rng.standard_normal(n), 2000, 8000) * 0.6) * np.exp(-t / 0.005) * 0.4


def bansuri(f, dur, vib=0.012):
    """A breathy flute: sine + a little 2nd/3rd harmonic, delayed vibrato, breath noise."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    v = 1 + vib * np.sin(2 * np.pi * 5.5 * t) * np.minimum(1, t / 0.25)
    ph = 2 * np.pi * np.cumsum(f * v) / SR
    tone = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    breath = bp(rng.standard_normal(n), f * 0.8, min(f * 3, 15000)) * 0.12
    env = np.minimum(1, t / 0.04) * np.minimum(1, (dur - t) / 0.06).clip(0)
    return (tone + breath) * env * 0.32


def reverb(x, secs=1.6):
    n = int(secs * SR)
    t = np.arange(n) / SR
    out = []
    for seed in (1, 2):
        r = np.random.default_rng(seed).standard_normal(n) * np.exp(-t / (secs / 5))
        r = lp(r, 6000)
        out.append(fftconvolve(x, r)[:N] * 0.012)
    return np.stack(out)


def master(dry, send, out):
    wet = reverb(hp(send, 250))
    mono = hp(dry, 32, 2)
    low = lp(mono, 140, 2)
    mono = mono - low * 0.3
    mix = np.stack([mono + wet[0], mono + wet[1]])
    fade = np.ones(N); fn = int(0.5 * SR); fade[-fn:] = np.linspace(1, 0, fn) ** 1.5
    mix *= fade
    mix = np.tanh(mix * 0.9) / np.tanh(0.9)
    mix /= np.max(np.abs(mix)) * 1.05
    with wave.open(out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mix.T * 32767).astype(np.int16).tobytes())
    print('wrote', out, mix.shape[1] / SR, 's')
