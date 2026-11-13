"""Generate Panditji launch-score candidates with Google Lyria RealTime (Gemini API).

Usage:  python generate.py <variant> <seed> <out_prefix>   (retries with seed+1.. if not locked)
        python generate.py master <raw.wav> <trim_s> <out.wav|out.flac>
        python generate.py metrics <file> [file ...]
        variants: sitar | bansuri | strings | duet
Writes <out_prefix>.wav (raw 48 kHz stream) and <out_prefix>.json (grid + send log).

How the timing works (measured 2026-11-13, see NOTES.md):
  * bpm=96 and scale=D_MAJOR_B_MINOR are fixed for the whole session (never reset).
  * Audio arrives in 2 s chunks, ~2.3 s ahead of wall clock. A prompt/config change
    becomes audible ~1.0 s after the end of the newest received chunk, advancing with
    wall-clock time, so changes are sent on a wall-clock schedule aimed at
    (target stream time - EFFECT_LAG).
  * Lyria's bar grid is not anchored to stream t=0, so after ~17 s of pre-roll the
    script finds the beat phase (comb over onset strength at exactly 96 BPM) and the
    downbeat (low-frequency onset accent), then puts video t=0 (T0) on the first
    downbeat >= 22 s of stream. Every section change is scheduled at T0 + cue.
The key is read from GEMINI_API_KEY and never printed.
"""
import asyncio, json, sys, time, wave
import numpy as np
from google import genai
from google.genai import types

SR, CH, BPS = 48000, 2, 2
BPM = 96; BEAT = 60 / BPM; BAR = 4 * BEAT          # 0.625 s, 2.5 s
EFFECT_LAG = 1.0       # s of stream between "frontier at send" and audible change (measured)
EARLY = 0.10           # land changes a hair before the bar line
ANALYZE_AT = 17.0      # stream seconds of pre-roll used to find the grid
MIN_CONF, MIN_LOCK, TRIES = 6.0, 1.05, 6   # restart the session if the pre-roll is not locked to 96 BPM
MIN_T0 = 22.0
VIDEO_LEN = 58.0; TAIL = 6.0

LEADS = {
    "sitar":   ("Catchy rhythmic sitar riff", "Bansuri flute"),
    "bansuri": ("Bansuri flute melody", "Sitar"),
    "strings": ("Bollywood string section melody", "Sitar"),
    "duet":    ("Sitar and bansuri flute melody in unison", "Harmonium"),
}
STYLE = "Bollywood pop instrumental, modern Indian pop fusion, upbeat, peppy, warm polished mix"

def sections(variant):
    lead, second = LEADS[variant]
    P = lambda *pairs: [types.WeightedPrompt(text=t, weight=w) for t, w in pairs]
    # (video cue s, name, prompts, density, brightness, mute_bass, mute_drums)
    return [
        (None, "intro", P((STYLE, 1.0), ("Light tabla groove", 1.0), ("Harmonium chords", 0.8),
                          (lead, 1.0), ("Bright, bouncy intro", 0.6)), 0.25, 0.55, True, False),
        (10.0, "drop", P((STYLE, 1.0), ("Dhol and tabla groove", 1.2), ("Punchy pop drums and deep bass", 1.1),
                         (lead, 1.2), ("Harmonium chords", 0.6), ("Danceable, energetic Indian pop", 1.0)),
         0.75, 0.58, False, False),
        (22.5, "lift", P((STYLE, 1.0), ("Dhol and tabla groove", 1.2), ("Punchy pop drums and deep bass", 1.1),
                         (lead, 1.2), ("Lush Bollywood string section", 1.1), (second, 0.7),
                         ("Uplifting, soaring", 0.8)), 0.85, 0.60, False, False),
        (37.5, "break", P((STYLE, 0.8), ("Half-time breakdown, building tension", 1.3),
                          ("Rising Bollywood strings", 1.0), ("Harmonium chords", 0.8), (lead, 0.7)),
         0.20, 0.52, True, True),
        (42.5, "bigdrop", P((STYLE, 1.0), ("Dhol and tabla groove", 1.4), ("Punchy pop drums and deep bass", 1.2),
                            (lead, 1.3), ("Lush Bollywood string section", 1.1), (second, 0.8),
                            ("Euphoric, celebratory, full ensemble", 1.2)), 1.00, 0.62, False, False),
        (52.5, "last", P((STYLE, 1.0), ("Dhol and tabla groove", 1.0), ("Punchy pop drums and deep bass", 0.9),
                         (lead, 1.3), ("Lush Bollywood string section", 1.0), ("Final melodic phrase", 0.9)),
         0.80, 0.58, False, False),
        (55.0, "outro", P((STYLE, 0.7), ("Sustained final D major chord, ringing out", 1.4),
                          ("Harmonium", 0.8), ("Strings", 0.8), (lead, 0.5)), 0.10, 0.50, True, True),
    ]

def config(seed, d, b, mb, md):
    return types.LiveMusicGenerationConfig(
        bpm=BPM, scale=types.Scale.D_MAJOR_B_MINOR, seed=seed, guidance=4.5,
        density=d, brightness=b, mute_bass=mb, mute_drums=md)

def find_grid(pcm_bytes):
    """Beat phase + downbeat (stream seconds, mod BAR) at exactly 96 BPM."""
    import librosa
    x = np.frombuffer(pcm_bytes, dtype=np.int16).reshape(-1, 2).mean(1) / 32768.0
    y = librosa.resample(x, orig_sr=SR, target_sr=22050); sr = 22050; hop = 128
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    S = np.abs(librosa.stft(y, hop_length=hop, n_fft=2048)); f = librosa.fft_frequencies(sr=sr, n_fft=2048)
    low = np.maximum(0, np.diff(np.log1p(S[f < 150].sum(0)), prepend=0))
    t0, t1 = 3.0, len(y) / sr - 0.5
    phs = np.linspace(0, BEAT, 125, endpoint=False)
    sc = [oenv[np.round(np.arange(t0 + p, t1, BEAT) * sr / hop).astype(int)].mean() for p in phs]
    ph = (t0 + phs[int(np.argmax(sc))]) % BEAT
    beat_conf = float(np.max(sc) / np.median(sc))
    acc = [low[np.round(np.arange(t0 + ph + k * BEAT, t1, BAR) * sr / hop).astype(int)].mean()
           + 0.5 * oenv[np.round(np.arange(t0 + ph + k * BEAT, t1, BAR) * sr / hop).astype(int)].mean()
           for k in range(4)]
    k = int(np.argmax(acc)); down = (t0 + ph + k * BEAT) % BAR
    # is 96 BPM really the dominant pulse? best comb score over 80-140 BPM
    def comb(bpm):
        per = 60 / bpm
        return max(oenv[np.round(np.arange(t0 + p, t1, per) * sr / hop).astype(int)].mean()
                   for p in np.linspace(0, per, 40, endpoint=False))
    others = max(comb(b) for b in np.arange(80, 140, 0.5) if abs(b - 96) > 1.5 and abs(b - 128) > 1.5)
    lock = float(comb(96) / others)    # >1: 96 BPM beats every other tempo (128 = 3:4 dhol pattern ignored)
    return float(ph), float(down), beat_conf, [float(a) for a in acc], lock

class NotLocked(Exception): pass

async def main(variant, seed, prefix):
    for attempt in range(TRIES):
        try:
            return await take(variant, seed + attempt, prefix, attempt)
        except NotLocked as e:
            print(f"attempt {attempt} (seed {seed + attempt}) rejected: {e}", flush=True)
        except Exception as e:      # e.g. APIError 1006 abnormal closure mid-stream
            print(f"attempt {attempt} (seed {seed + attempt}) failed: {type(e).__name__}: {e}", flush=True)
    raise SystemExit("no locked take")

async def take(variant, seed, prefix, attempt):
    client = genai.Client(http_options={"api_version": "v1alpha"})
    secs = sections(variant)
    pcm = bytearray(); st = {"recv_end": 0.0, "recv_wall": time.monotonic()}
    log = {"variant": variant, "seed": seed, "attempt": attempt, "sends": []}
    done = asyncio.Event()

    async def receiver(s):
        async for msg in s.receive():
            sc = msg.server_content
            if sc and sc.audio_chunks:
                for ch in sc.audio_chunks: pcm.extend(ch.data)
                st["recv_end"] = len(pcm) / (SR * CH * BPS); st["recv_wall"] = time.monotonic()
            if done.is_set(): break

    async def wait_until(cond, step):
        while not cond():
            if rx.done():
                raise RuntimeError(f"stream ended: {rx.exception() if not rx.cancelled() else 'cancelled'}")
            await asyncio.sleep(step)

    def frontier():   # estimated stream time a change sent *now* would land at
        return st["recv_end"] + EFFECT_LAG + (time.monotonic() - st["recv_wall"])

    async with client.aio.live.music.connect(model="models/lyria-realtime-exp") as s:
        _, name, prompts, d, b, mb, md = secs[0]
        await s.set_weighted_prompts(prompts=prompts)
        await s.set_music_generation_config(config=config(seed, d, b, mb, md))
        await s.reset_context()          # make sure bpm/scale are applied from the first frame
        await s.play()
        rx = asyncio.create_task(receiver(s))
        log["sends"].append({"name": name, "frontier": 0.0})
        await wait_until(lambda: st["recv_end"] >= ANALYZE_AT, 0.02)
        ph, down, conf, acc, lock = await asyncio.get_running_loop().run_in_executor(None, find_grid, bytes(pcm))
        if conf < MIN_CONF or lock < MIN_LOCK:
            done.set(); await s.stop(); rx.cancel()
            raise NotLocked(f"beat conf {conf:.2f}, 96-BPM lock {lock:.2f}")
        T0 = down + BAR * np.ceil((MIN_T0 - down) / BAR)
        log.update(lock_96=lock, beat_phase=ph, downbeat_phase=down, beat_conf=conf, downbeat_accents=acc, T0=float(T0))
        print(f"seed {seed}: grid beat {ph:.3f}s downbeat {down:.3f}s conf {conf:.2f} lock {lock:.2f} -> T0 = {T0:.3f}s", flush=True)
        for cue, name, prompts, d, b, mb, md in secs[1:]:
            target = T0 + cue - EARLY
            await wait_until(lambda: frontier() >= target, 0.005)
            fr = frontier()
            await s.set_weighted_prompts(prompts=prompts)
            await s.set_music_generation_config(config=config(seed, d, b, mb, md))
            log["sends"].append({"name": name, "cue": cue, "target_stream": target, "frontier": fr})
            print(f"sent {name:8s} target {target:7.3f} est.frontier {fr:7.3f}", flush=True)
        await wait_until(lambda: st["recv_end"] >= T0 + VIDEO_LEN + TAIL, 0.05)
        done.set()
        await s.stop()
        rx.cancel()
    with wave.open(prefix + ".wav", "wb") as w:
        w.setnchannels(CH); w.setsampwidth(BPS); w.setframerate(SR); w.writeframes(bytes(pcm))
    json.dump(log, open(prefix + ".json", "w"), indent=1)

# ----------------------------------------------------------------------------- mastering
# Same chain for every candidate:
#  1. sample-exact 58.000 s cut starting at the measured downbeat (no time-stretch: every
#     delivered take measures 96.00 BPM);
#  2. corrective EQ: Lyria RealTime output carries most of its energy below 125 Hz, a weak
#     0.5-4 kHz midrange (it would nearly vanish on a phone speaker) and a hiss shelf >12 kHz;
#  3. break gain ride (mix move, not synthesis): -2.5 dB at 37.5 s rising to -0.5 dB by 42.5 s,
#     30 ms ramps, so the break reads lighter and builds into the 42.5 s drop;
#  4. 1.5 s fade ending at 58.000 s;
#  5. gain + 4x-oversampled peak limiter (-1.5 dBFS), then two-pass ffmpeg loudnorm in linear
#     mode to -14 LUFS integrated / -1 dBTP.
EQ = ("highpass=f=32:p=2,lowshelf=f=110:g=-6,equalizer=f=800:t=o:w=2:g=4,"
      "equalizer=f=2500:t=o:w=1.5:g=3,lowpass=f=15000:p=2,lowpass=f=15000:p=2")
N_OUT = int(VIDEO_LEN * SR)                       # 2,784,000 samples = 58.000 s
_G = ("pow(10,(if(lt(t,37.5),0,if(lt(t,37.53),-2.5*(t-37.5)/0.03,if(lt(t,42.5),-2.5+2*(t-37.5)/5,"
      "if(lt(t,42.53),-0.5*(1-(t-42.5)/0.03),0)))))/20)")
RIDE = f"aeval='val(0)*{_G}|val(1)*{_G}'"

def _ffjson(args):
    import subprocess, re, json as _j
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *args], capture_output=True, text=True)
    if r.returncode: raise RuntimeError(r.stderr[-2000:])
    return _j.loads(re.findall(r"\{[^{}]*\}", r.stderr)[-1])

def master(raw, trim, out):
    start = int(round(trim * SR))
    pre = (f"atrim=start_sample={start}:end_sample={start + N_OUT},asetpts=PTS-STARTPTS,{EQ},{RIDE},"
           f"afade=t=out:st={VIDEO_LEN - 1.5}:d=1.5")
    ln = "loudnorm=I=-14:TP=-1:LRA=11"
    m0 = _ffjson(["-i", raw, "-af", f"{pre},{ln}:print_format=json", "-f", "null", "-"])
    gain = -14.0 - float(m0["input_i"]) + 0.8          # overshoot so the final linear pass only attenuates
    lim = (f"aresample=192000,volume={gain:.2f}dB,"
           f"alimiter=limit=0.84:attack=3:release=60:level=false,aresample={SR}")
    chain = f"{pre},{lim}"
    m = _ffjson(["-i", raw, "-af", f"{chain},{ln}:print_format=json", "-f", "null", "-"])
    ln2 = (f"{ln}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
           f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true:print_format=json")
    fmt = ["-c:a", "pcm_s24le"] if out.endswith(".wav") else ["-c:a", "flac", "-sample_fmt", "s16"]
    post = f"aresample={SR}:dither_method=triangular,apad=whole_len={N_OUT},atrim=end_sample={N_OUT}"
    m2 = _ffjson(["-y", "-i", raw, "-af", f"{chain},{ln2},{post}", "-ar", str(SR), "-ac", "2", *fmt, out])
    return {"trim_s": trim, "pre_gain_dB": round(gain, 2), "after_limiter": m,
            "normalization_type": m2.get("normalization_type")}

# ----------------------------------------------------------------------------- metrics
NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
DMAJ = [2, 4, 6, 7, 9, 11, 1]                      # D E F# G A B C#
SECTIONS = [("intro", 0, 10), ("drop", 10, 22.5), ("lift", 22.5, 37.5), ("break", 37.5, 42.5),
            ("bigdrop", 42.5, 52.5), ("last", 52.5, 55), ("outro", 55, 58)]

def metrics(path):
    import librosa, subprocess, re
    y, sr = librosa.load(path, sr=22050, mono=True); hop = 128
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    tempo_lib = float(np.atleast_1d(librosa.beat.beat_track(onset_envelope=oenv, sr=sr, hop_length=hop, start_bpm=96)[0])[0])
    def comb(bpm, t1=55.0):
        per = 60 / bpm
        return max(oenv[np.round(np.arange(p, t1, per) * sr / hop).astype(int)].mean()
                   for p in np.linspace(0, per, 50, endpoint=False))
    grid = np.arange(94, 98.01, 0.02); fine = float(grid[int(np.argmax([comb(b) for b in grid]))])
    # beat grid at t = 0, 0.625, ... : onset strength on-grid vs off-grid, and beat-1 low-end accent
    on = oenv[np.round(np.arange(0, 55, BEAT) * sr / hop).astype(int)].mean()
    off = np.median([oenv[np.round((np.arange(0, 55, BEAT) + o) * sr / hop).astype(int)].mean()
                     for o in np.linspace(0.05, BEAT - 0.05, 20)])
    S = np.abs(librosa.stft(y, hop_length=hop, n_fft=2048)) ** 2; f = librosa.fft_frequencies(sr=sr, n_fft=2048)
    low = np.maximum(0, np.diff(np.log1p(S[f < 150].sum(0)), prepend=0))
    acc = [low[np.round(np.arange(k * BEAT, 55, BAR) * sr / hop).astype(int)].mean() for k in range(4)]
    b = int(BAR * sr)
    rms_bar = [float(20 * np.log10(np.sqrt(np.mean(y[i * b:(i + 1) * b] ** 2)) + 1e-9)) for i in range(int(len(y) // b))]
    sec = {n: float(20 * np.log10(np.sqrt(np.mean(y[int(a * sr):int(z * sr)] ** 2)) + 1e-9)) for n, a, z in SECTIONS}
    P = np.abs(librosa.stft(y, n_fft=4096)) ** 2; fq = librosa.fft_frequencies(sr=sr, n_fft=4096); tot = P.sum()
    ch = librosa.feature.chroma_cqt(y=librosa.effects.harmonic(y), sr=sr).mean(axis=1); ch = ch / ch.sum()
    top7 = [NAMES[i] for i in np.argsort(ch)[::-1][:7]]
    lu = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", lu)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", lu)[-1])
    import soundfile as sf
    info = sf.info(path)
    return {"file": path, "samples": info.frames, "sr": info.samplerate, "lufs_I": I, "true_peak_dBTP": TP,
            "tempo_librosa": tempo_lib, "tempo_fine": fine, "grid_on_off_ratio": float(on / off),
            "beat1_low_accent": [round(float(a / max(acc)), 2) for a in acc],
            "rms_bar_dB": [round(r, 1) for r in rms_bar], "rms_section_dB": {k: round(v, 1) for k, v in sec.items()},
            "harsh_2_5k": float(P[(fq >= 2000) & (fq < 5000)].sum() / tot),
            "harsh_3_10k": float(P[(fq >= 3000) & (fq < 10000)].sum() / tot),
            "chroma": {n: round(float(c), 3) for n, c in zip(NAMES, ch)},
            "dmaj_share": float(ch[DMAJ].sum()), "dmaj_min_note": float(ch[DMAJ].min()),
            "top7": top7, "top7_in_dmaj": sum(n in [NAMES[i] for i in DMAJ] for n in top7)}

if __name__ == "__main__":
    if sys.argv[1] == "master":                   # python generate.py master raw.wav trim_s out.(wav|flac)
        print(json.dumps(master(sys.argv[2], float(sys.argv[3]), sys.argv[4])))
    elif sys.argv[1] == "metrics":                # python generate.py metrics file [file ...]
        print(json.dumps([metrics(p) for p in sys.argv[2:]], indent=1))
    else:
        v, seed, prefix = sys.argv[1], int(sys.argv[2]), sys.argv[3]
        asyncio.run(asyncio.wait_for(main(v, seed, prefix), 900))
