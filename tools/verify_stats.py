#!/usr/bin/env python
"""verify_stats.py — the second-source rule (research/QC_PROTOCOL.md), as code.

Pulls independent metadata for a public post URL via yt-dlp and diffs it
against claimed numbers. Never guesses a number the platform hides (IG often
hides like counts) — such fields are reported "UNAVAILABLE", not estimated.

Usage
-----
    verify_stats.py --url <post_url> [--views N] [--likes N] [--comments N] [--json]

Behavior
--------
    - Runs: yt-dlp --dump-json --no-download <url>
    - For each of views/likes/comments where the platform exposes a number:
        - no claim given  -> reported as INFO (platform value only)
        - claim given     -> percent-diff'd; >10% divergence -> FAILED-VERIFICATION
    - Where the platform does not expose a field -> UNAVAILABLE (never guessed).

Exit codes
----------
    0  ran successfully (verification outcome, pass or fail, is data — see output)
    2  yt-dlp is not installed (prints an install hint)
    3  network / extraction error (yt-dlp ran but failed, or returned unparseable output)
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

FIELDS = ("views", "likes", "comments")
YTDLP_KEYS = {"views": "view_count", "likes": "like_count", "comments": "comment_count"}
DIVERGENCE_THRESHOLD_PCT = 10.0


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def check_ytdlp_available() -> bool:
    return shutil.which("yt-dlp") is not None


def fetch_platform_stats(url: str, timeout: int = 60) -> dict:
    """Runs yt-dlp --dump-json against url. Raises RuntimeError on failure."""
    proc = subprocess.run(
        ["yt-dlp", "--dump-json", "--no-download", url],
        capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"yt-dlp exited with code {proc.returncode}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"could not parse yt-dlp output as JSON: {exc}") from exc


def diff_field(claimed, actual) -> dict:
    if actual is None:
        return {"platform_value": None, "claimed_value": claimed, "status": "UNAVAILABLE"}
    if claimed is None:
        return {"platform_value": actual, "claimed_value": None, "status": "INFO"}
    if actual == 0:
        pct = 0.0 if claimed == 0 else 100.0
    else:
        pct = abs(claimed - actual) / actual * 100.0
    status = "FAILED-VERIFICATION" if pct > DIVERGENCE_THRESHOLD_PCT else "OK"
    return {"platform_value": actual, "claimed_value": claimed,
            "divergence_pct": round(pct, 2), "status": status}


def build_report(url: str, claims: dict, platform_data: dict) -> dict:
    fields = {}
    for f in FIELDS:
        actual = platform_data.get(YTDLP_KEYS[f])
        fields[f] = diff_field(claims.get(f), actual)
    any_failed = any(v["status"] == "FAILED-VERIFICATION" for v in fields.values())
    return {
        "url": url,
        "fields": fields,
        "any_failed_verification": any_failed,
        "extractor": platform_data.get("extractor") or platform_data.get("extractor_key"),
    }


def print_human(report: dict) -> None:
    print(f"url: {report['url']}")
    if report.get("extractor"):
        print(f"extractor: {report['extractor']}")
    for field, r in report["fields"].items():
        if r["status"] == "UNAVAILABLE":
            print(f"  {field}: UNAVAILABLE (platform does not expose this field)")
        elif r["status"] == "INFO":
            print(f"  {field}: platform={r['platform_value']} (no claim provided)")
        else:
            print(f"  {field}: claimed={r['claimed_value']} platform={r['platform_value']} "
                  f"divergence={r['divergence_pct']}% -> {r['status']}")
    print(f"overall: {'FAILED-VERIFICATION' if report['any_failed_verification'] else 'OK'}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="verify_stats.py",
        description="Second-source verification of claimed post stats via yt-dlp.",
    )
    parser.add_argument("--url", required=True, help="public post URL")
    parser.add_argument("--views", type=int, default=None)
    parser.add_argument("--likes", type=int, default=None)
    parser.add_argument("--comments", type=int, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not check_ytdlp_available():
        _err("yt-dlp not found on PATH.")
        _err("Install hint: pip install yt-dlp")
        return 2

    try:
        platform_data = fetch_platform_stats(args.url)
    except subprocess.TimeoutExpired:
        _err("yt-dlp timed out fetching the URL")
        return 3
    except RuntimeError as exc:
        _err(f"yt-dlp / extraction error: {exc}")
        return 3

    claims = {"views": args.views, "likes": args.likes, "comments": args.comments}
    report = build_report(args.url, claims, platform_data)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_human(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
