"""v2 (Flow) timeline: every cue time for the picture (v2_build.py) and the score (v2_score.py).

    python v2_timeline.py      # prints the timeline

Units: seconds of OUTPUT time unless a name says src (seconds inside a Flow clip, 24 fps).
Musical grid: 72 BPM. Everything sits on that beat grid (beat 0 = the hard cut from the row to exhibit 1):
each clip's playback length is solved to a whole number of half-beats by its eased speed-up factor
(1.0-1.6x, only inside the clip's empty-wall middle), and every hold is a whole number of beats.
"""
import math

FPS = 30
SRC_FPS = 24
BPM = 72
BEAT = 60 / BPM

OPEN_BEATS = 4         # the row still + title (3.33 s), then a hard cut to exhibit 1
HOLD1_BEATS = 4        # exhibit 1 hold on C1's first frame (3.33 s)
HOLD_BEATS = 3.5       # freeze on each landed exhibit (2.92 s; text is up ~3.6 s) with a very slow push-in
PHONE_BEATS = 12       # exhibit 7: push-in + the chat, then the hard cut to the row
CLOSE_BEATS = 6        # the row + close line, then the dissolve to the end card
END_BEATS = 6          # dissolve + end card + fade out
DISSOLVE = 1.2         # row -> end wall
FADE_OUT = 1.0

# Per clip: src_end = where playback stops (the landed frame that is then held);
# fast = src window of the empty-wall middle that may be sped up; decel = src seconds eased to a stop
# (unused now). C2 is cut mid-zoom at 5.58 s (Sparsh); its hold continues that zoom in code (v2_build.py).
# C0 is not used (spec change, Sparsh 2026-11-19).
CLIPS = {
    'C1': dict(src_end=189 / 24, fast=(1.4, 6.0), decel=0.0),
    'C2': dict(src_end=134 / 24, fast=(1.0, 4.0), decel=0.0),
    'C3': dict(src_end=6.0, fast=(1.0, 4.4), decel=0.0),
    'C4': dict(src_end=7.4, fast=(1.3, 4.9), decel=0.0),
    'C5': dict(src_end=6.5, fast=(1.0, 4.4), decel=0.0),
    'C6': dict(src_end=6.9, fast=(1.0, 4.8), decel=0.0),
}
RAMP = 0.6   # src seconds to ease the speed up / down at each edge of the fast window
KMAX = 1.6


def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def smoother(x):
    x = min(1.0, max(0.0, x))
    return x * x * x * (x * (6 * x - 15) + 10)


def _speed(c, k, tau):
    f = CLIPS[c]['fast']
    if not f or k == 1:
        return 1.0
    a, b = f
    w = smooth((tau - a) / RAMP) * (1 - smooth((tau - (b - RAMP)) / RAMP))
    return 1 + (k - 1) * w


def src_curve(c, k, dt=1 / FPS / 8):
    """Output-time -> src-time samples (fine steps) for clip c at speed factor k. Returns (ts, taus)."""
    end, dec = CLIPS[c]['src_end'], CLIPS[c]['decel']
    tau, t, ts, taus = 0.0, 0.0, [0.0], [0.0]
    main_end = end - dec
    while tau < main_end:
        tau += _speed(c, k, tau) * dt
        t += dt
        ts.append(t); taus.append(min(tau, main_end))
    if dec > 0:  # linear velocity ramp 1 -> 0: covers dec src seconds in 2*dec output seconds
        T = 2 * dec
        n = int(T / dt)
        t0 = t
        for i in range(1, n + 1):
            u = i / n
            ts.append(t0 + u * T); taus.append(main_end + dec * (1 - (1 - u) ** 2))
    return ts, taus


def clip_len(c, k):
    return src_curve(c, k)[0][-1]


def solve_k(c):
    """Speed factor so the clip's output length is a whole number of beats ."""
    if not CLIPS[c]['fast']:
        return 1.0, clip_len(c, 1.0)
    lo, hi = clip_len(c, KMAX), clip_len(c, 1.0)
    q = BEAT / 2                            # half-beat (8th-note) grid
    n = math.ceil(lo / q - 1e-6)            # shortest grid length reachable with speed <= KMAX
    target = n * q
    a, b = 1.0, KMAX
    for _ in range(40):
        m = (a + b) / 2
        if clip_len(c, m) > target:
            a = m
        else:
            b = m
    return (a + b) / 2, target


class Seg:
    def __init__(self, kind, t0, t1, **kw):
        self.kind, self.t0, self.t1 = kind, t0, t1
        self.__dict__.update(kw)

    def __repr__(self):
        x = {k: v for k, v in self.__dict__.items() if k not in ('kind', 't0', 't1', 'curve')}
        return f'{self.kind:6s} {self.t0:6.2f}-{self.t1:6.2f} ({self.t1 - self.t0:5.2f}) {x}'


def build():
    """Spec change (Sparsh, 2026-11-19): C0 is dropped. Open on the row still, hard cut to exhibit 1
    (C1's first frame, held), then C1 carries the move on."""
    segs, t = [], 0.0
    segs.append(Seg('open', 0.0, OPEN_BEATS * BEAT))
    t = OPEN_BEATS * BEAT
    land = {1: t}             # the hard cut lands on exhibit 1
    segs.append(Seg('hold', t, t + HOLD1_BEATS * BEAT, ex=1, clip=None, first='C1'))
    t += HOLD1_BEATS * BEAT
    for i, c in enumerate(['C1', 'C2', 'C3', 'C4', 'C5', 'C6']):
        k, L = solve_k(c)
        ts, taus = src_curve(c, k)
        segs.append(Seg('clip', t, t + ts[-1], clip=c, k=round(k, 3), curve=(ts, taus)))
        t += ts[-1]
        land[i + 2] = t       # C1 lands on exhibit 2, ... C6 on exhibit 7
        if i < 5:
            segs.append(Seg('hold', t, t + HOLD_BEATS * BEAT, ex=i + 2, clip=c))
            t += HOLD_BEATS * BEAT
    segs.append(Seg('phone', t, t + PHONE_BEATS * BEAT, ex=7))
    t += PHONE_BEATS * BEAT
    cut = t
    segs.append(Seg('close', t, t + CLOSE_BEATS * BEAT))
    t += CLOSE_BEATS * BEAT
    segs.append(Seg('end', t, t + END_BEATS * BEAT))
    t += END_BEATS * BEAT
    return segs, land, cut, t


SEGS, LAND, CUT, TOTAL = build()
END0 = CUT + CLOSE_BEATS * BEAT      # dissolve to the end card starts
NFRAMES = int(round(TOTAL * FPS))
GRID0 = LAND[1]                      # beat 0 of the musical grid = exhibit 1 lands

# ---- text cues: (layer, t_in, fade_in, t_out, fade_out)
TEXT_IN_LEAD = 0.55   # exhibit text starts fading in this long before the landing
TEXT = [('title', 0.3, 0.7, 2.45, 0.65)]   # gone by 3.10, before the cut at 3.33
for s in SEGS:
    if s.kind == 'hold' and s.ex == 1:   # arrives just after the hard cut
        TEXT.append(('ex1', LAND[1] + 0.2, 0.5, s.t1 + 0.15, 0.5))
    elif s.kind == 'hold':
        nxt = s.t1   # next clip starts moving here; the text leaves as the camera starts to move
        if s.clip == 'C2':   # C2 -> C3 is a real cut: the text leaves before it
            TEXT.append((f'ex{s.ex}', LAND[s.ex] - TEXT_IN_LEAD, 0.6, nxt - 0.55, 0.45))
        else:
            TEXT.append((f'ex{s.ex}', LAND[s.ex] - TEXT_IN_LEAD, 0.6, nxt + 0.15, 0.5))

# ---- exhibit 7, the phone (relative to L7 = the landing on the phone)
L7 = LAND[7]
PUSH = (0.0, 3.0)           # eased push-in toward the screen
WAKE = (0.55, 0.35)         # screen UI fades in (t, dur)
BUBBLE_IN = 1.35            # incoming "How are you, bro?" appears
DRAFT1 = 'Honestly bro, I’m not doing good.'
DRAFT2 = ['A', 'l', 'l', ' ', 'g', 'o', 'o', 'd', ',', ' ', 'b', 'r', 'o', ' ', '\U0001F44D']


def _typing_times(n, t0, mean, seed):
    """Human-ish key timing: jitter, a slightly longer gap after spaces/punctuation."""
    import random
    r = random.Random(seed)
    out, t = [], t0
    for i in range(n):
        out.append(t)
        t += mean * r.uniform(0.7, 1.3)
    return out


TYPE1 = _typing_times(len(DRAFT1), 2.25, 0.072, 7)          # 33 keys
for i, ch in enumerate(DRAFT1[:-1]):                          # pause after a space or comma
    if ch in ' ,':
        TYPE1 = TYPE1[:i + 1] + [x + 0.05 for x in TYPE1[i + 1:]]
TYPE1_END = TYPE1[-1]
BACK0 = TYPE1_END + 1.0                                       # hold ~1 s on the honest draft
# backspace: held key, accelerating (first two presses slower, then fast repeat)
BACK = []
t = BACK0
for i in range(len(DRAFT1)):
    BACK.append(t)
    t += 0.15 if i == 0 else (0.09 if i == 1 else 0.032)
BACK_END = BACK[-1]
TYPE2 = _typing_times(len(DRAFT2), BACK_END + 0.42, 0.085, 3)
SEND = TYPE2[-1] + 0.42      # tap send: draft clears, green bubble appears, headline crossfades
SENT_FADE = 0.14
HEAD_XF = (SEND, 0.45)       # 'What he typed.' -> 'What he sent.'
EX7_TEXT_IN = -TEXT_IN_LEAD  # label + headline fade in like the other exhibits


def chat_state(tr):
    """Chat screen at tr seconds after L7 -> (state name, ui alpha). State names match v2_overlays.mjs."""
    blink = (int(tr / 0.53) % 2) == 0
    if tr < WAKE[0]:
        return None, 0.0
    ua = smooth((tr - WAKE[0]) / WAKE[1])
    if tr < BUBBLE_IN:
        return 'a00-1', ua                    # header, no bubble, empty draft, cursor
    if tr < TYPE1[0]:
        return f'b00-{int(blink)}', ua
    if tr < BACK0:
        n = sum(1 for x in TYPE1 if x <= tr)
        cur = 1 if tr < TYPE1_END + 0.25 else int(blink)
        return f'b{n:02d}-{cur}', ua
    if tr < TYPE2[0]:
        n = len(DRAFT1) - sum(1 for x in BACK if x <= tr)
        cur = 1 if tr < BACK_END + 0.2 else int(blink)
        return f'b{n:02d}-{cur}', ua
    if tr < SEND:
        n = sum(1 for x in TYPE2 if x <= tr)
        return f'c{n:02d}-1', ua
    if tr < SEND + 0.12:
        return 'press', ua
    return f'sent-{int(blink)}', ua


def describe():
    for s in SEGS:
        print(s)
    print(f'exhibit landings: ' + ', '.join(f'{k}:{v:.2f}' for k, v in LAND.items()))
    print(f'CUT {CUT:.2f}  END0 {END0:.2f}  TOTAL {TOTAL:.2f} s  ({NFRAMES} frames)')
    print(f'phone: type1 {TYPE1[0]:.2f}-{TYPE1_END:.2f}, back {BACK0:.2f}-{BACK_END:.2f}, '
          f'type2 {TYPE2[0]:.2f}-{TYPE2[-1]:.2f}, send {SEND:.2f} (rel. to L7 {L7:.2f}); cut at +{CUT - L7:.2f}')


if __name__ == '__main__':
    describe()
