#!/usr/bin/env python
"""hygiene_check.py — pre-publish export hygiene via ffprobe/ffmpeg (SYSTEM_DESIGN.md §7/§8).

Runs a battery of PASS/WARN/FAIL checks against an exported video file before
it can pass the G2 cut gate:
    - resolution/aspect per platform (ig/yt: >=1080x1920, 9:16; yt-long: >=1920x1080, 16:9)
    - duration band (platform-dependent; see below)
    - video codec h264, audio codec aac, audio stream present
    - pixel format yuv420p
    - black-border detection via ffmpeg cropdetect sampling
    - SHA256 not already in ops/pipeline/.published_hashes.json (repost guard)

Duration bands:
    ig:      hard 3-180s, warn outside 20-45s
    yt:      hard <=180s (Shorts eligibility 2026 - max 3 min), warn outside 20-60s
    yt-long: hard 60s-60min, warn outside 8-20min (BET-4 flagship band)

Usage
-----
    hygiene_check.py <video_path> [--platform ig|yt|yt-long] [--json]

Exit codes
----------
    0  all checks PASS (WARNs allowed)
    1  at least one check FAILed
    2  ffprobe/ffmpeg not found (prints an install hint)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import _common as c

ASPECT_TOLERANCE_PCT = 2.0

PLATFORM_SPECS = {
    "ig": {
        "target_aspect": 9 / 16, "aspect_label": "9:16",
        "min_width": 1080, "min_height": 1920,
        "duration": {"hard_min": 3, "hard_max": 180, "warn_min": 20, "warn_max": 45},
    },
    "yt": {
        "target_aspect": 9 / 16, "aspect_label": "9:16",
        "min_width": 1080, "min_height": 1920,
        "duration": {"hard_min": 1, "hard_max": 180, "warn_min": 20, "warn_max": 60},
    },
    "yt-long": {
        "target_aspect": 16 / 9, "aspect_label": "16:9",
        "min_width": 1920, "min_height": 1080,
        "duration": {"hard_min": 60, "hard_max": 3600, "warn_min": 480, "warn_max": 1200},
    },
}


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def check_deps_available() -> bool:
    return shutil.which("ffprobe") is not None and shutil.which("ffmpeg") is not None


def ffprobe_json(path: Path, timeout: int = 30) -> dict:
    proc = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"ffprobe exited with code {proc.returncode}")
    return json.loads(proc.stdout)


def _stream_of_type(data: dict, kind: str) -> dict | None:
    for s in data.get("streams", []):
        if s.get("codec_type") == kind:
            return s
    return None


def check_resolution(video: dict, spec: dict) -> tuple[str, str]:
    w, h = video.get("width"), video.get("height")
    if not w or not h:
        return "FAIL", "no width/height reported"
    if w >= spec["min_width"] and h >= spec["min_height"]:
        return "PASS", f"{w}x{h} >= {spec['min_width']}x{spec['min_height']}"
    return "FAIL", f"{w}x{h} below minimum {spec['min_width']}x{spec['min_height']}"


def check_aspect(video: dict, spec: dict) -> tuple[str, str]:
    w, h = video.get("width"), video.get("height")
    if not w or not h:
        return "FAIL", "no width/height reported"
    ratio = w / h
    target = spec["target_aspect"]
    label = spec["aspect_label"]
    pct_off = abs(ratio - target) / target * 100.0
    if pct_off <= ASPECT_TOLERANCE_PCT:
        return "PASS", f"{w}x{h} ratio={ratio:.4f} within {ASPECT_TOLERANCE_PCT}% of {label}"
    return "FAIL", f"{w}x{h} ratio={ratio:.4f} off by {pct_off:.2f}% from {label}"


def check_video_codec(video: dict) -> tuple[str, str]:
    codec = video.get("codec_name")
    if codec == "h264":
        return "PASS", "h264"
    return "FAIL", f"expected h264, got '{codec}'"


def check_audio_present(audio: dict | None) -> tuple[str, str]:
    if audio is not None:
        return "PASS", "audio stream present"
    return "FAIL", "no audio stream found"


def check_audio_codec(audio: dict | None) -> tuple[str, str]:
    if audio is None:
        return "FAIL", "no audio stream to check"
    codec = audio.get("codec_name")
    if codec == "aac":
        return "PASS", "aac"
    return "FAIL", f"expected aac, got '{codec}'"


def check_pixel_format(video: dict) -> tuple[str, str]:
    pf = video.get("pix_fmt")
    if pf == "yuv420p":
        return "PASS", "yuv420p"
    return "FAIL", f"expected yuv420p, got '{pf}'"


def check_duration(fmt: dict, platform: str) -> tuple[str, str]:
    band = PLATFORM_SPECS[platform]["duration"]
    try:
        duration = float(fmt.get("duration"))
    except (TypeError, ValueError):
        return "FAIL", "no duration reported"
    if duration < band["hard_min"] or duration > band["hard_max"]:
        return "FAIL", (f"{duration:.1f}s outside hard band "
                         f"[{band['hard_min']}-{band['hard_max']}]s for {platform}")
    if duration < band["warn_min"] or duration > band["warn_max"]:
        return "WARN", (f"{duration:.1f}s outside recommended band "
                         f"[{band['warn_min']}-{band['warn_max']}]s for {platform}")
    return "PASS", f"{duration:.1f}s within recommended band [{band['warn_min']}-{band['warn_max']}]s"


def check_black_borders(path: Path, width: int | None, height: int | None, timeout: int = 60) -> tuple[str, str]:
    cmd = ["ffmpeg", "-hide_banner", "-i", str(path), "-t", "8",
           "-vf", "cropdetect=24:16:0", "-f", "null", "-"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return "WARN", "cropdetect timed out"
    matches = re.findall(r"crop=(\d+):(\d+):(\d+):(\d+)", proc.stderr)
    if not matches:
        return "WARN", "could not sample crop (no cropdetect output)"
    cw, ch, cx, cy = (int(x) for x in matches[-1])
    if width and height and cw >= width * 0.98 and ch >= height * 0.98:
        return "PASS", f"crop={cw}:{ch}:{cx}:{cy} matches full frame {width}x{height}"
    return "FAIL", f"crop={cw}:{ch}:{cx}:{cy} smaller than full frame {width}x{height} (black borders detected)"


def check_repost_guard(path: Path, root) -> tuple[str, str]:
    digest = c.sha256_file(path)
    ledger = c.load_published_hashes(root)
    if digest in ledger:
        prior = ledger[digest]
        return ("FAIL", f"SHA256 {digest[:12]}... already published as item "
                         f"{prior.get('id')} ({prior.get('slug')}) -> {prior.get('url')} on {prior.get('date')}")
    return "PASS", f"SHA256 {digest[:12]}... not in published-hashes ledger"


def run_checks(path: Path, platform: str, root) -> list[dict]:
    probe = ffprobe_json(path)
    video = _stream_of_type(probe, "video")
    audio = _stream_of_type(probe, "audio")
    fmt = probe.get("format", {})

    checks = []

    spec = PLATFORM_SPECS[platform]
    if video is None:
        checks.append({"name": "resolution", "status": "FAIL", "detail": "no video stream found"})
        checks.append({"name": "aspect_ratio", "status": "FAIL", "detail": "no video stream found"})
        checks.append({"name": "video_codec", "status": "FAIL", "detail": "no video stream found"})
        checks.append({"name": "pixel_format", "status": "FAIL", "detail": "no video stream found"})
    else:
        s, d = check_resolution(video, spec); checks.append({"name": "resolution", "status": s, "detail": d})
        s, d = check_aspect(video, spec); checks.append({"name": "aspect_ratio", "status": s, "detail": d})
        s, d = check_video_codec(video); checks.append({"name": "video_codec", "status": s, "detail": d})
        s, d = check_pixel_format(video); checks.append({"name": "pixel_format", "status": s, "detail": d})

    s, d = check_audio_present(audio); checks.append({"name": "audio_present", "status": s, "detail": d})
    s, d = check_audio_codec(audio); checks.append({"name": "audio_codec", "status": s, "detail": d})
    s, d = check_duration(fmt, platform); checks.append({"name": "duration", "status": s, "detail": d})

    width = video.get("width") if video else None
    height = video.get("height") if video else None
    s, d = check_black_borders(path, width, height); checks.append({"name": "black_borders", "status": s, "detail": d})

    s, d = check_repost_guard(path, root); checks.append({"name": "repost_guard", "status": s, "detail": d})

    return checks


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="hygiene_check.py",
        description="Pre-publish export hygiene checks via ffprobe/ffmpeg.",
    )
    parser.add_argument("video_path")
    parser.add_argument("--platform", choices=("ig", "yt", "yt-long"), default="ig")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not check_deps_available():
        _err("ffprobe/ffmpeg not found on PATH.")
        _err("Install hint: winget install Gyan.FFmpeg")
        return 2

    path = Path(args.video_path)
    if not path.is_file():
        _err(f"video file does not exist: {path}")
        return 1

    root = c.get_repo_root()
    try:
        checks = run_checks(path, args.platform, root)
    except (RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        _err(f"could not read video: {exc}")
        return 1

    overall = "FAIL" if any(chk["status"] == "FAIL" for chk in checks) else "PASS"

    if args.json:
        print(json.dumps({"video": str(path), "platform": args.platform,
                           "checks": checks, "overall": overall}, indent=2))
    else:
        print(f"video: {path}")
        print(f"platform: {args.platform}")
        for chk in checks:
            print(f"  [{chk['status']:<4}] {chk['name']}: {chk['detail']}")
        print(f"overall: {overall}")

    return 1 if overall == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
