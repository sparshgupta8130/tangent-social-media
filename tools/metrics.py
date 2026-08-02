#!/usr/bin/env python
"""metrics.py — the measurement constitution (strategy/STRATEGY.md §6), as code.

Subcommands
-----------
    likerate --views N --likes N [--json]
        LR = likes/views*100, verdict vs the 1-10% organic sanity band.

    decompose --views N --likes N --median-views N --median-lr X [--json]
        views x LR quadrant verdict:
          LR>=median_lr AND views<0.5*median_views -> HOOK/DISCOVERY FAILURE
          LR<median_lr  AND views<0.5*median_views -> CRAFT FAILURE
          views>=2*median_views AND LR<1.0         -> BOOST-SUSPECT
          views>=median_views AND LR in [1,10]      -> HEALTHY
          else                                      -> IN-BAND

    efficiency --csv posts.csv --followers N [--json]
        median(views)/followers*100 with bands:
          <5% WARNING, 5-10% OK, 10-15% HEALTHY, 15-20% GOOD, >=20% EXCELLENT.
        (The 15-20% "GOOD" label fills a gap left open by the spec's named
        bands so every real number gets a verdict; see tools/README.md.)

    funnel --comments N --likes N [--json]
        ratio=comments/likes vs the funnel bar: >=0.5 WORKING, 0.2-0.5
        MIDDLING, <0.2 FAILING.

    report --csv posts.csv --followers N [--json]
        Per-row likerate/decompose/efficiency/funnel + an account-level
        summary (median views, median LR, top/median spread, efficiency,
        funnel median over funnel-flagged rows, early-warning triad).

CSV schema (see tools/README.md):
    date,platform,url,pillar,views,likes,comments,shares,saves,funnel,followers_at_post

Exit codes: 0 success, 1 bad input/usage.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path

CSV_FIELDS = (
    "date", "platform", "url", "pillar", "views", "likes", "comments",
    "shares", "saves", "funnel", "followers_at_post",
)
CSV_INT_FIELDS = ("views", "likes", "comments", "shares", "saves", "funnel", "followers_at_post")


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Core math
# ---------------------------------------------------------------------------

def likerate(views: float, likes: float) -> dict:
    if views <= 0:
        return {"lr": 0.0, "verdict": "INVALID (zero or negative views)"}
    lr = likes / views * 100.0
    if lr < 1:
        verdict = "BELOW-BAND (<1%, check for view-inflation or dead audience)"
    elif lr > 10:
        verdict = "ABOVE-BAND (>10%, check for coordinated engagement or bad sample)"
    else:
        verdict = "IN-BAND (organic-plausible, 1-10%)"
    return {"lr": lr, "verdict": verdict}


def decompose(views: float, likes: float, median_views: float, median_lr: float) -> dict:
    lr = likerate(views, likes)["lr"]
    if lr >= median_lr and views < 0.5 * median_views:
        quadrant = "HOOK/DISCOVERY FAILURE (content resonated, distribution didn't)"
    elif lr < median_lr and views < 0.5 * median_views:
        quadrant = "CRAFT FAILURE"
    elif views >= 2 * median_views and lr < 1.0:
        quadrant = "BOOST-SUSPECT (check second source + paid-partnership tag)"
    elif views >= median_views and 1 <= lr <= 10:
        quadrant = "HEALTHY"
    else:
        quadrant = "IN-BAND"
    return {"lr": lr, "quadrant": quadrant}


def efficiency_band(pct: float) -> str:
    if pct < 5:
        return "WARNING"
    if pct < 10:
        return "OK"
    if pct < 15:
        return "HEALTHY"
    if pct < 20:
        return "GOOD"
    return "EXCELLENT"


def funnel(comments: float, likes: float) -> dict:
    if likes <= 0:
        return {"ratio": 0.0, "verdict": "INVALID (zero or negative likes)"}
    ratio = comments / likes
    if ratio >= 0.5:
        verdict = "WORKING"
    elif ratio >= 0.2:
        verdict = "MIDDLING"
    else:
        verdict = "FAILING"
    return {"ratio": ratio, "verdict": verdict}


# ---------------------------------------------------------------------------
# CSV
# ---------------------------------------------------------------------------

def read_posts_csv(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        missing = [f for f in CSV_FIELDS if f not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"CSV is missing required column(s): {', '.join(missing)}")
        for raw in reader:
            row = dict(raw)
            for f in CSV_INT_FIELDS:
                v = (row.get(f) or "").strip()
                row[f] = int(v) if v != "" else 0
            row["pillar"] = (row.get("pillar") or "").strip().upper()
            rows.append(row)
    return rows


def build_report(rows: list[dict], followers: float) -> dict:
    views_list = [r["views"] for r in rows]
    median_views = statistics.median(views_list) if views_list else 0.0
    lr_list = [likerate(r["views"], r["likes"])["lr"] for r in rows]
    median_lr = statistics.median(lr_list) if lr_list else 0.0

    row_reports = []
    for r in rows:
        lr_result = likerate(r["views"], r["likes"])
        decomp = decompose(r["views"], r["likes"], median_views, median_lr)
        row_efficiency = (r["views"] / r["followers_at_post"] * 100.0
                           if r["followers_at_post"] else None)
        funnel_result = funnel(r["comments"], r["likes"])
        row_reports.append({
            "date": r["date"],
            "platform": r["platform"],
            "url": r["url"],
            "pillar": r["pillar"],
            "views": r["views"],
            "likes": r["likes"],
            "comments": r["comments"],
            "shares": r["shares"],
            "saves": r["saves"],
            "funnel_flag": bool(r["funnel"]),
            "likerate_pct": lr_result["lr"],
            "likerate_verdict": lr_result["verdict"],
            "decompose_quadrant": decomp["quadrant"],
            "efficiency_pct": row_efficiency,
            "funnel_ratio": funnel_result["ratio"],
            "funnel_verdict": funnel_result["verdict"],
        })

    top_views = max(views_list) if views_list else 0
    spread = (top_views / median_views) if median_views else None
    efficiency_pct = (median_views / followers * 100.0) if followers else None
    efficiency_verdict = efficiency_band(efficiency_pct) if efficiency_pct is not None else None

    funnel_ratios = [r["comments"] / r["likes"] for r in rows if r["funnel"] == 1 and r["likes"] > 0]
    funnel_median = statistics.median(funnel_ratios) if funnel_ratios else None
    if funnel_median is None:
        funnel_median_verdict = "NO-FUNNEL-POSTS"
    elif funnel_median >= 0.5:
        funnel_median_verdict = "WORKING"
    elif funnel_median >= 0.2:
        funnel_median_verdict = "MIDDLING"
    else:
        funnel_median_verdict = "FAILING"

    hits = [r for r in rows if median_views and r["views"] >= 2 * median_views]
    efficiency_low = bool(efficiency_pct is not None and efficiency_pct < 5)
    off_pillar_hits_only = bool(hits) and all(r["pillar"] not in ("HERO", "WORKHORSE") for r in hits)
    flat_spread = bool(spread is not None and spread < 2.0)
    triad = {
        "efficiency_sliding_under_5pct": efficiency_low,
        "hits_only_off_pillar": off_pillar_hits_only,
        "flat_non_pinned_spread": flat_spread,
    }
    triad_count = sum(1 for v in triad.values() if v)

    summary = {
        "n_posts": len(rows),
        "median_views": median_views,
        "median_likerate_pct": median_lr,
        "top_views": top_views,
        "top_to_median_spread": spread,
        "efficiency_pct": efficiency_pct,
        "efficiency_verdict": efficiency_verdict,
        "funnel_median_ratio": funnel_median,
        "funnel_median_verdict": funnel_median_verdict,
        "early_warning_triad": triad,
        "early_warning_triad_count": triad_count,
        "strategy_review_triggered": triad_count >= 2,
    }
    return {"rows": row_reports, "summary": summary}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_kv(d: dict) -> None:
    for k, v in d.items():
        print(f"{k}: {v}")


def cmd_likerate(args) -> int:
    result = likerate(args.views, args.likes)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"LR: {result['lr']:.3f}%")
        print(f"verdict: {result['verdict']}")
    return 0


def cmd_decompose(args) -> int:
    if args.median_views <= 0:
        _err("--median-views must be > 0")
        return 1
    result = decompose(args.views, args.likes, args.median_views, args.median_lr)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"LR: {result['lr']:.3f}%")
        print(f"quadrant: {result['quadrant']}")
    return 0


def cmd_efficiency(args) -> int:
    try:
        rows = read_posts_csv(Path(args.csv))
    except (OSError, ValueError) as exc:
        _err(str(exc))
        return 1
    if not rows:
        _err("CSV has no data rows")
        return 1
    if args.followers <= 0:
        _err("--followers must be > 0")
        return 1
    views_list = [r["views"] for r in rows]
    median_views = statistics.median(views_list)
    pct = median_views / args.followers * 100.0
    result = {"median_views": median_views, "followers": args.followers,
              "efficiency_pct": pct, "verdict": efficiency_band(pct)}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_kv(result)
    return 0


def cmd_funnel(args) -> int:
    result = funnel(args.comments, args.likes)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"ratio: {result['ratio']:.3f}")
        print(f"verdict: {result['verdict']}")
    return 0


def cmd_report(args) -> int:
    try:
        rows = read_posts_csv(Path(args.csv))
    except (OSError, ValueError) as exc:
        _err(str(exc))
        return 1
    if not rows:
        _err("CSV has no data rows")
        return 1
    if args.followers <= 0:
        _err("--followers must be > 0")
        return 1
    report = build_report(rows, args.followers)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("Per-row:")
        for r in report["rows"]:
            print(f"  {r['date']} {r['platform']:>4} {r['url']:<40} "
                  f"views={r['views']:<8} LR={r['likerate_pct']:.2f}% "
                  f"[{r['likerate_verdict']}] -> {r['decompose_quadrant']}")
        print("\nSummary:")
        _print_kv(report["summary"])
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="metrics.py",
        description="Measurement constitution: likerate, decompose, efficiency, funnel, report.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_lr = sub.add_parser("likerate", help="LR + organic-sanity-band verdict")
    p_lr.add_argument("--views", type=float, required=True)
    p_lr.add_argument("--likes", type=float, required=True)
    p_lr.add_argument("--json", action="store_true")
    p_lr.set_defaults(func=cmd_likerate)

    p_dc = sub.add_parser("decompose", help="views x LR quadrant verdict")
    p_dc.add_argument("--views", type=float, required=True)
    p_dc.add_argument("--likes", type=float, required=True)
    p_dc.add_argument("--median-views", type=float, required=True, dest="median_views")
    p_dc.add_argument("--median-lr", type=float, required=True, dest="median_lr")
    p_dc.add_argument("--json", action="store_true")
    p_dc.set_defaults(func=cmd_decompose)

    p_ef = sub.add_parser("efficiency", help="median(views)/followers*100 + band")
    p_ef.add_argument("--csv", required=True)
    p_ef.add_argument("--followers", type=float, required=True)
    p_ef.add_argument("--json", action="store_true")
    p_ef.set_defaults(func=cmd_efficiency)

    p_fn = sub.add_parser("funnel", help="comment:like ratio vs the funnel bar")
    p_fn.add_argument("--comments", type=float, required=True)
    p_fn.add_argument("--likes", type=float, required=True)
    p_fn.add_argument("--json", action="store_true")
    p_fn.set_defaults(func=cmd_funnel)

    p_rp = sub.add_parser("report", help="full per-row + account-summary report")
    p_rp.add_argument("--csv", required=True)
    p_rp.add_argument("--followers", type=float, required=True)
    p_rp.add_argument("--json", action="store_true")
    p_rp.set_defaults(func=cmd_report)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
