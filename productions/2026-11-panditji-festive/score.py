"""Original 9 s scores for the two festive reels, 120 BPM in D, synthesised from scratch (no samples).

python score.py diwali  out.wav   -> sitar, tabla, a tanpura, a 'ting' for every diya, fireworks
python score.py newyear out.wav   -> a garba-style triplet groove with dandiya clicks and a bansuri; a tick for every digit
Hit points match the timelines in diwali.html / newyear.html.
"""
import os
import sys
import numpy as np

which, out = sys.argv[1], sys.argv[2]
# The New Year reel is the 120 BPM layout stretched ×1.5 (80 BPM, 13.5 s); Diwali stays 9 s at 120 BPM.
K = 1.5 if which == 'newyear' else 1.0
os.environ['REEL_DUR'] = str(9.0 * K)
from synth import *  # noqa: E402,F401,F403  (SR, N, DUR, add, instruments, master)
SIX = 0.125      # a 16th at 120 BPM
TRI = 0.5 / 3    # an 8th-note triplet
dry, send = buf(), buf()


def put(sig, t, g=1.0, s=0.0):
    add(dry, sig, t, g)
    if s:
        add(send, sig, t, s)


def drone(gain=1.0):
    d = tanpura(DUR)
    ramp = np.minimum(1, np.arange(N) / (0.6 * SR))
    return d[:N] * ramp * gain


def flourish(t, notes, inst='sitar', g=0.45):
    for i, m in enumerate(notes):
        s = sitar(midi(m), 0.9, bend=(i == 0), bright=0.7) if inst == 'sitar' else bansuri(midi(m), 0.5)
        put(s, t + i * 0.07, g, 0.35)


def ending(t, chord=(54, 57, 62, 64, 66, 69)):
    b = bell(midi(86)); put(b, t, 0.7, 0.5)
    p = pad(chord, 2.4, 3600); put(p, t, 0.7, 0.4)
    put(bass(38, 1.6), t, 0.6)


if which == 'diwali':
    dry += drone(1.0)
    # 0–2: a flame catches, Panditji springs up, gasps, namaste
    put(pop(midi(74)), 0.02, 0.5)
    put(fwump(), 0.25, 0.9); b = bell(midi(86)); put(b, 0.3, 0.45, 0.5)
    put(whoosh(0.4), 0.45, 0.5); put(boing(300, 620), 0.72, 0.8)
    put(blip(1500, 0.06), 1.06, 0.6); put(blip(2000, 0.08), 1.13, 0.6)
    for tt, m in ((1.0, 69), (1.25, 71), (1.5, 74)):
        put(sitar(midi(m), 1.0), tt, 0.7, 0.35)
    b = bell(midi(81)); put(b, 1.5, 0.35, 0.4)
    put(noise_sweep(0.8, 300, 8000, 'up') * 0.45, 1.2)
    for k in range(8):
        put(tabla_na(), 1.5 + k * 0.0625, 0.2 + 0.45 * k / 7)
    # 2.0 drop: the row of diyas, one ting each
    put(boom(), 2.0, 0.8); put(crash(), 2.0, 0.55, 0.3)
    for i, m in enumerate((81, 83, 86, 88)):
        b = bell(midi(m)); put(b, 2.0 + i * 0.125, 0.45, 0.35)
    put(whoosh(0.3), 2.42, 0.5); put(pop(midi(81)), 2.5, 0.8); put(pop(midi(86)), 2.95, 0.9); put(whoosh(0.3), 2.85, 0.5)
    # groove 2.0–6.5: dholak-ish tabla, claps on 2 and 4, shaker, bass
    for bt in np.arange(2.0, 6.5, 0.5):
        k = int(round((bt - 2.0) / 0.5))
        put(tabla_ge(), bt, 0.9 if k % 2 == 0 else 0.55)
        put(tabla_na(), bt + 0.25, 0.6)
        if k % 4 == 3:
            put(tabla_na(), bt + 0.375, 0.45)
        if k % 2 == 1:
            put(clap(), bt, 0.55, 0.2)
        put(kick(0.55), bt) if k % 2 == 0 else None
    for s16 in range(int((6.5 - 2.0) / SIX)):
        put(shaker(), 2.0 + s16 * SIX, 0.9 if s16 % 2 else 0.5)
    for start, m, length in ((2.0, 38, 1.0), (3.0, 43, 1.0), (4.0, 35, 1.0), (5.0, 33, 1.0), (6.0, 38, 0.5)):
        for e in range(int(length / 0.5)):
            put(bass(m, 0.4), start + e * 0.5, 0.75)
    A = [(0, 81), (2, 83), (3, 81), (4, 78), (6, 81), (8, 86), (10, 83), (11, 81), (12, 78), (14, 76)]
    B = [(0, 74), (2, 76), (3, 78), (4, 81), (6, 78), (8, 76), (10, 74), (11, 76), (12, 78), (14, 76)]
    for start, riff in ((2.0, A), (4.0, B)):
        for pos, m in riff:
            put(sitar(midi(m), 0.6, bend=(pos % 4 == 0), bright=0.65), start + pos * SIX, 0.75, 0.3)
    put(sitar(midi(74), 1.2), 6.0, 0.75, 0.35)
    # fireworks (rocket whistle, then the burst and its crackle), kept under the music
    for i, t0 in enumerate((3.0, 3.75, 4.5, 5.5, 6.25, 7.25)):
        put(whistle(), t0 - 0.45, 0.6)
        put(burst(), t0, 0.45); put(crackle(1.3, 70, seed=i), t0 + 0.05, 0.5, 0.15)
    # 6.5: namaste, the music settles
    ending(6.5); flourish(6.52, (74, 78, 81, 86))
    for bt in (6.5, 7.0, 7.5, 8.0):
        put(tabla_ge(), bt, 0.45); put(tabla_na(), bt + 0.25, 0.3)
    put(pop(midi(78)), 6.6, 0.35)

elif which == 'newyear':
    k = lambda x: x * K  # schedule time (120 BPM layout) -> seconds
    B, T3 = k(0.5), k(0.5) / 3  # a beat and a triplet at 80 BPM
    dry += drone(0.8)
    # dawn, a bansuri; the counter pops in; Panditji springs up and thinks
    for tt, m, d in ((0.05, 69, 0.6), (0.5, 74, 0.6), (0.9, 76, 0.9)):
        put(bansuri(midi(m), k(d)), k(tt), 0.8, 0.45)
    put(pop(midi(78)), k(0.27), 0.6); put(whoosh(0.45), k(0.3), 0.45); put(boing(320, 640, 0.45), k(0.55), 0.75)
    put(blip(520, 0.14), k(0.97), 0.5); put(blip(470, 0.16), k(0.97) + 0.2, 0.5)  # "hmm"
    put(blip(1600, 0.06), k(1.76), 0.6); put(blip(2300, 0.08), k(1.76) + 0.08, 0.6)  # the gasp
    # one tick for every digit the last tile rolls past: invert the page's ease (eIO over 0.95–2.0, 11 steps)
    eio = lambda x: 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2
    xs = np.linspace(0, 1, 20001); ys = np.array([eio(x) for x in xs]) * 11
    for j in range(1, 11):
        x = xs[np.searchsorted(ys, j)]
        put(tick(1800 + j * 90), k(0.95 + x * 1.05), 0.9)
    put(noise_sweep(k(0.85), 300, 8000, 'up') * 0.4, k(1.15))
    # the drop: the year lands
    put(boom(), k(2.0), 0.8); put(crash(2.2), k(2.0), 0.5, 0.3)
    b = bell(midi(88)); put(b, k(2.0), 0.8, 0.5)
    put(crackle(0.8, 110, seed=5), k(2.0) + 0.02, 0.6)
    put(whoosh(0.35), k(2.5), 0.5); put(pop(midi(83)), k(2.62), 0.9); put(blip(1300, 0.05), k(3.02), 0.4); put(pop(midi(88)), k(3.52), 0.8)
    # garba groove on the triplet grid: dhol "dha . na", dandiya on the beat and the last triplet
    for bt in np.arange(k(2.0), k(6.5) - 1e-6, B):
        n = int(round((bt - k(2.0)) / B))
        put(tabla_ge(), bt, 0.95 if n % 2 == 0 else 0.6)
        put(kick(0.5), bt) if n % 2 == 0 else None
        put(tabla_na(), bt + 2 * T3, 0.65)
        put(dandiya(1.0), bt, 0.9); put(dandiya(0.7), bt + 2 * T3, 0.9)
        if n % 2 == 1:
            put(clap(), bt, 0.45, 0.2)
        for j in range(3):
            put(shaker(), bt + j * T3, 0.9 if j else 0.5)
    for start, m in ((2.0, 38), (3.0, 43), (4.0, 33), (5.0, 38), (6.0, 33)):
        for e in range(2):
            if start + e * 0.5 < 6.5:
                put(bass(m, 0.5), k(start + e * 0.5), 0.75)
    A = [(0, 78), (2, 81), (3, 83), (5, 81), (6, 78), (8, 76), (9, 74), (11, 76)]
    Bm = [(0, 78), (2, 81), (3, 86), (5, 83), (6, 81), (8, 78), (9, 76), (11, 78)]
    for start, riff in ((2.0, A), (4.0, Bm)):
        poss = {p for p, _ in riff}
        for pos, m in riff:
            d = T3 * (0.95 if pos + 1 in poss else 2)
            put(bansuri(midi(m), max(d, 0.2)), k(start) + pos * T3, 0.9, 0.4)
            put(sitar(midi(m - 12), 0.5, bend=False, bright=0.5), k(start) + pos * T3, 0.25, 0.1)
    put(bansuri(midi(76), 0.7), k(6.0), 0.9, 0.4)
    # namaste
    ending(k(6.5)); flourish(k(6.5) + 0.02, (74, 78, 81, 86), inst='sitar', g=0.4)
    put(bansuri(midi(74), 2.4), k(6.6), 0.8, 0.5)
    for bt in np.arange(k(6.5), k(8.5), B):
        put(dandiya(0.6), bt, 0.6); put(tabla_ge(), bt, 0.4)
else:
    raise SystemExit('which: diwali | newyear')

master(dry, send, out)
