#!/usr/bin/env python
"""ingest_stats.py — turns a platform analytics export into posts.csv rows
(Phase R3, tools/README.md).

HONEST CONSTRAINT — read this before trusting any output
-----------------------------------------------------------------------------
As of this build, tangentideas.ai has not published anything: no real
Instagram or YouTube analytics export has ever been seen by this tool. The
column mappings below are built from DOCUMENTED formats (secondary
export-guide sources + research/briefs/platform_ops_2026-07.md §4, tiered
[HIGH]/[MED]/[LOW]/[UNVERIFIED] there) and encoded here as best-effort
defaults — NOT verified against a real file, because no real file exists
yet. Treat every default mapping as a hypothesis.

format assumptions unvalidated against real exports — run
`ingest_stats.py inspect <file>` on the FIRST real export and reconcile
before trusting batch ingestion.

Subcommands
-----------
    inspect <file> [--platform ig|yt]
        Sniffs a CSV/XLSX export: format, delimiter, headers, sample rows.
        Prints the detected columns against the built-in expected mapping(s)
        (both platforms if --platform omitted) — what would MAP, what would
        DROP (unrecognized), what's MISSING (expected but absent). The
        reconciliation tool for first contact with a real export. Never
        writes anything.

    ig <file> --followers N [--funnel-urls url1,url2] [--mapping <json>] [--dry-run]
        Maps an Instagram professional-dashboard/Business-Suite content
        export to posts.csv rows (platform=ig). funnel=1 for URLs listed in
        --funnel-urls (exact match); followers_at_post = --followers for
        every row in this batch. Appends to ops/calendar/posts.csv with
        dedup-by-url (see below). --dry-run prints the would-be rows and
        touches nothing.

    yt <file> --followers N [--mapping <json>] [--dry-run]
        Same for a YouTube Studio content export (platform=yt). No
        --funnel-urls: the comment-keyword-DM mechanic is IG-only
        (knowledge/platform/youtube.md §10) — YT rows are never funnel-
        flagged.

Column mapping / --mapping override
------------------------------------
Each platform has a built-in default mapping of {export column name ->
posts.csv target field}. Targets are any of posts.csv's own columns (date,
url, views, likes, comments, shares, saves) plus the yt-only pseudo-target
"video_id" (a Video ID column is turned into a canonical
https://www.youtube.com/watch?v=<id> URL — the URL *scheme* is
well-documented and stable even though the export's exact column name is
not). platform/pillar/funnel/followers_at_post are never sourced from the
export; they're computed. A --mapping <path.json> file, shaped exactly like
the built-in dict ({"Source Column": "target_field", ...}), REPLACES the
default mapping entirely for that run — this is the escape hatch for when
`inspect` shows reality differs from the built-in guess.

Dedup / update-in-place (ops/calendar/posts.csv, keyed by url)
-----------------------------------------------------------------------------
Analytics accrue — a repost's numbers should only ever go up. For each of
views/likes/comments/shares/saves/followers_at_post: if the new value is
higher than what's stored, the stored value is updated; if the new value is
LOWER, it is never silently written over the higher stored value — a
WARNING is printed and the higher stored value is kept. `funnel` is
monotonic (0->1 allowed, never silently downgraded). A brand-new url is
appended as a new row.

Every real (non-dry-run) append/update prints:
    REMINDER: second-source rule: verify via tools/verify_stats.py before
    these numbers enter a postmortem (QC_PROTOCOL).

Exit codes: 0 success, 1 bad input/usage, 2 optional dependency (openpyxl)
missing for a .xlsx file.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import _common as c
import metrics

try:
    import openpyxl  # optional; only needed for .xlsx input
except ImportError:  # pragma: no cover - exercised via the exit-2 path
    openpyxl = None


FORMAT_CAVEAT = (
    "format assumptions unvalidated against real exports — run "
    "`ingest_stats.py inspect <file>` on the FIRST real export and reconcile "
    "before trusting batch ingestion."
)

REMINDER = (
    "second-source rule: verify via tools/verify_stats.py before these "
    "numbers enter a postmortem (QC_PROTOCOL)."
)

# Non-export-sourced posts.csv fields, and the yt-only pseudo-target.
_COMPUTED_FIELDS = {"platform", "pillar", "funnel", "followers_at_post"}
VALID_MAPPING_TARGETS = (set(metrics.CSV_FIELDS) - _COMPUTED_FIELDS) | {"video_id"}

# ---------------------------------------------------------------------------
# Built-in expected column mappings.
#
# IG: Meta Business Suite / IG professional-dashboard Insights > Content >
# Export Data flow. Column names per secondary export-guide sources
# (Graphed, Coupler.io) — NOT Meta's own docs, which don't publish a literal
# CSV header list. "Views" reflects the 2026 unified-metric name (Media
# impressions/Reel plays/Reel replays/Reel initial plays deprecated into it)
# per research/briefs/platform_ops_2026-07.md §4a [MED]. "Permalink" is the
# WEAKEST assumption here: no source confirms a literal URL column exists in
# this export at all — it's included because a dedup key is a hard
# requirement, not because it's been seen. See tools/README.md's ranked
# weakest-assumptions note.
IG_DEFAULT_MAPPING: dict[str, str] = {
    "Post Date": "date",
    "Permalink": "url",
    "Views": "views",
    "Likes": "likes",
    "Comments": "comments",
    "Shares": "shares",
    "Saves": "saves",
}

# YT: YouTube Studio content/Advanced-Mode export. Column names per
# secondary export-guide sources (ops-brief §4b/§4c) — exact literal headers
# not confirmed. "Video ID" -> canonical watch URL is HIGH confidence (a
# documented, stable URL scheme), independent of whatever the export's real
# column name turns out to be.
YT_DEFAULT_MAPPING: dict[str, str] = {
    "Video ID": "video_id",
    "Video publish time": "date",
    "Views": "views",
    "Likes": "likes",
    "Comments added": "comments",
    "Shares": "shares",
}

DEFAULT_MAPPINGS = {"ig": IG_DEFAULT_MAPPING, "yt": YT_DEFAULT_MAPPING}


class MissingDependencyError(RuntimeError):
    """Raised when a .xlsx file is given but openpyxl isn't installed."""


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# File sniffing (CSV stdlib-only; XLSX via openpyxl if installed)
# ---------------------------------------------------------------------------

def _read_csv(path: Path) -> tuple[str, list[str], list[dict]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        sample = fh.read(4096)
        fh.seek(0)
        try:
            delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
        except csv.Error:
            delimiter = ","
        reader = csv.DictReader(fh, delimiter=delimiter)
        headers = list(reader.fieldnames or [])
        rows = [dict(r) for r in reader]
    return delimiter, headers, rows


def _read_xlsx(path: Path) -> tuple[str | None, list[str], list[dict]]:
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    try:
        ws = wb.worksheets[0]
        rows_iter = ws.iter_rows(values_only=True)
        try:
            header_row = next(rows_iter)
        except StopIteration:
            raise ValueError(f"{path} has no rows (empty sheet)")
        headers = [("" if h is None else str(h)) for h in header_row]
        rows = []
        for raw in rows_iter:
            if raw is None or all(v is None for v in raw):
                continue
            row = {headers[i]: ("" if v is None else str(v))
                   for i, v in enumerate(raw) if i < len(headers)}
            rows.append(row)
    finally:
        wb.close()
    return None, headers, rows


def sniff_file(path: Path) -> dict:
    """Returns {"format", "delimiter", "headers", "rows"}. Dependency check
    happens before the file-existence check (mirrors hygiene_check.py /
    verify_stats.py: the install hint must surface cleanly either way)."""
    suffix = path.suffix.lower()
    if suffix in (".xlsx", ".xlsm") and openpyxl is None:
        raise MissingDependencyError(
            "reading .xlsx exports requires openpyxl, which is not installed.\n"
            "Install hint: pip install openpyxl"
        )
    if not path.is_file():
        raise OSError(f"file not found: {path}")
    if suffix == ".xls":
        raise ValueError(
            "legacy binary .xls is not supported (openpyxl reads .xlsx only) — "
            "re-export as .xlsx or .csv"
        )
    if suffix in (".xlsx", ".xlsm"):
        delimiter, headers, rows = _read_xlsx(path)
        fmt = "xlsx"
    else:
        delimiter, headers, rows = _read_csv(path)
        fmt = "csv"
    return {"format": fmt, "delimiter": delimiter, "headers": headers, "rows": rows}


def load_export(path: Path) -> tuple[list[str], list[dict]]:
    info = sniff_file(path)
    return info["headers"], info["rows"]


# ---------------------------------------------------------------------------
# Mapping
# ---------------------------------------------------------------------------

def load_mapping_override(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise OSError(f"mapping file not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        try:
            data = json.load(fh)
        except json.JSONDecodeError as exc:
            raise ValueError(f"mapping file is not valid JSON: {exc}") from exc
    if not isinstance(data, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in data.items()
    ):
        raise ValueError(
            'mapping file must be a JSON object of {"export column": "target field"}'
        )
    bad = sorted({v for v in data.values() if v not in VALID_MAPPING_TARGETS})
    if bad:
        raise ValueError(
            f"mapping targets not recognized: {bad} "
            f"(valid: {sorted(VALID_MAPPING_TARGETS)})"
        )
    return data


def apply_mapping(headers: list[str], rows: list[dict], mapping: dict[str, str]):
    """Returns (mapped_rows, dropped_columns, missing_columns).

    mapped_rows carry only the target-field keys the mapping produces
    (date/url/views/... and/or video_id) — the caller fills in the
    computed fields (platform/pillar/funnel/followers_at_post)."""
    missing = [src for src in mapping if src not in headers]
    dropped = [h for h in headers if h not in mapping]
    mapped_rows = [{target: row.get(src, "") for src, target in mapping.items()}
                   for row in rows]
    return mapped_rows, dropped, missing


# ---------------------------------------------------------------------------
# Value coercion
# ---------------------------------------------------------------------------

_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def normalize_date(raw: str) -> str:
    """Tolerant date parser -> ISO YYYY-MM-DD.

    Deliberately avoids datetime.strptime: as documented in _common.py,
    strptime lazily imports the stdlib `calendar` module, which every
    script in tools/ would instead resolve to tools/calendar.py and crash.
    """
    s = raw.strip()
    if not s:
        raise ValueError("empty date value")
    head = s.split("T")[0].split(" ")[0]
    if c.is_valid_iso_date(head):
        return head
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", s)
    if m:
        mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"{y:04d}-{mo:02d}-{d:02d}"
    m = re.match(r"^([A-Za-z]{3,9})\s+(\d{1,2}),?\s+(\d{4})$", s)
    if m:
        mon = m.group(1)[:3].lower()
        if mon in _MONTHS:
            return f"{int(m.group(3)):04d}-{_MONTHS[mon]:02d}-{int(m.group(2)):02d}"
    raise ValueError(
        f"unrecognized date format: {raw!r} (expected ISO YYYY-MM-DD or a "
        "common export variant like MM/DD/YYYY or 'Jul 1, 2026')"
    )


def _coerce_int(raw, field_name: str) -> int:
    s = ("" if raw is None else str(raw)).strip().replace(",", "")
    if s == "":
        return 0
    try:
        return int(s)
    except ValueError:
        try:
            return int(float(s))
        except ValueError:
            raise ValueError(f"could not parse {field_name} value {raw!r} as an integer")


# ---------------------------------------------------------------------------
# Pillar enrichment (best-effort, via ops/pipeline's own published-URL ledger)
# ---------------------------------------------------------------------------

def resolve_pillar(url: str, root: Path) -> str:
    """Best-effort: if this url was recorded by pipeline.py publish under
    some item, use that item's pillar. Blank (tolerated by metrics.py) if
    unresolvable — exports don't carry our internal pillar taxonomy."""
    try:
        for _, data in c.iter_items(root):
            published = data.get("published") or {}
            if url in published:
                pillar = data.get("pillar")
                if isinstance(pillar, str) and pillar:
                    return pillar
    except Exception:
        pass
    return ""


# ---------------------------------------------------------------------------
# Row construction
# ---------------------------------------------------------------------------

def build_posts_row(mapped: dict, platform: str, followers: int,
                     funnel_urls: set[str], root: Path) -> dict:
    raw_date = mapped.get("date", "")
    if not raw_date:
        raise ValueError("row has no mapped 'date' value")
    date = normalize_date(str(raw_date))

    url = str(mapped.get("url") or "").strip()
    if not url:
        video_id = str(mapped.get("video_id") or "").strip()
        if not video_id:
            raise ValueError("row has neither a mapped 'url' nor a 'video_id' to derive one from")
        url = f"https://www.youtube.com/watch?v={video_id}"

    return {
        "date": date,
        "platform": platform,
        "url": url,
        "pillar": resolve_pillar(url, root),
        "views": _coerce_int(mapped.get("views", ""), "views"),
        "likes": _coerce_int(mapped.get("likes", ""), "likes"),
        "comments": _coerce_int(mapped.get("comments", ""), "comments"),
        "shares": _coerce_int(mapped.get("shares", ""), "shares"),
        "saves": _coerce_int(mapped.get("saves", ""), "saves"),
        "funnel": 1 if url in funnel_urls else 0,
        "followers_at_post": int(followers),
    }


# ---------------------------------------------------------------------------
# posts.csv dedup / merge / write
# ---------------------------------------------------------------------------

_ACCRUAL_FIELDS = ("views", "likes", "comments", "shares", "saves", "followers_at_post")


def merge_rows(existing_rows: list[dict], new_rows: list[dict]):
    """Returns (final_rows, warnings, n_appended, n_updated)."""
    by_url: dict[str, dict] = {r["url"]: r for r in existing_rows}
    order = [r["url"] for r in existing_rows]
    warnings: list[str] = []
    n_appended = 0
    n_updated = 0

    for new in new_rows:
        url = new["url"]
        if url not in by_url:
            by_url[url] = dict(new)
            order.append(url)
            n_appended += 1
            continue

        existing = by_url[url]
        changed = False
        for field in _ACCRUAL_FIELDS:
            if new[field] > existing[field]:
                existing[field] = new[field]
                changed = True
            elif new[field] < existing[field]:
                warnings.append(
                    f"WARNING: {url} field '{field}' new value {new[field]} is "
                    f"lower than stored {existing[field]} — analytics should "
                    "only accrue; keeping the higher stored value, NOT overwriting."
                )
        if new["funnel"] > existing["funnel"]:
            existing["funnel"] = new["funnel"]
            changed = True
        if not existing.get("pillar") and new.get("pillar"):
            existing["pillar"] = new["pillar"]
            changed = True
        if changed:
            n_updated += 1

    final_rows = [by_url[u] for u in order]
    return final_rows, warnings, n_appended, n_updated


def write_posts_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(metrics.CSV_FIELDS))
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def posts_csv_path(root: Path) -> Path:
    return root / "ops" / "calendar" / "posts.csv"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_inspect(args) -> int:
    path = Path(args.file)
    try:
        info = sniff_file(path)
    except MissingDependencyError as exc:
        _err(str(exc))
        return 2
    except (OSError, ValueError) as exc:
        _err(str(exc))
        return 1

    print(f"file: {path}")
    if info["delimiter"]:
        print(f"format: {info['format']} (delimiter: {info['delimiter']!r})")
    else:
        print(f"format: {info['format']}")
    print(f"headers ({len(info['headers'])}): {info['headers']}")
    print(f"rows detected: {len(info['rows'])}")
    print("sample rows (up to 3):")
    for r in info["rows"][:3]:
        print(f"  {r}")

    platforms = [args.platform] if args.platform else ["ig", "yt"]
    for plat in platforms:
        mapping = DEFAULT_MAPPINGS[plat]
        print(f"\n--- reconciliation vs built-in {plat!r} mapping ---")
        for h in info["headers"]:
            if h in mapping:
                print(f"  MAP     {h!r} -> {mapping[h]}")
            else:
                print(f"  DROP    {h!r} (unrecognized, would be ignored)")
        missing = [src for src in mapping if src not in info["headers"]]
        for src in missing:
            print(f"  MISSING {src!r} expected -> {mapping[src]!r} (not found in file)")
        if not missing:
            print(f"  all expected {plat!r} columns found.")

    print(f"\n{FORMAT_CAVEAT}")
    return 0


def _ingest(args, platform: str, supports_funnel: bool) -> int:
    root = c.get_repo_root()
    path = Path(args.file)

    try:
        headers, rows = load_export(path)
    except MissingDependencyError as exc:
        _err(str(exc))
        return 2
    except (OSError, ValueError) as exc:
        _err(str(exc))
        return 1

    mapping = DEFAULT_MAPPINGS[platform]
    if args.mapping:
        try:
            mapping = load_mapping_override(Path(args.mapping))
        except (OSError, ValueError) as exc:
            _err(f"could not load --mapping file: {exc}")
            return 1

    mapped_rows, dropped, missing = apply_mapping(headers, rows, mapping)
    if missing:
        _err(f"mapping references column(s) not present in the file: {missing}")
        _err("run `ingest_stats.py inspect <file>` to see the real headers, "
             "then supply a --mapping override.")
        return 1
    targets = set(mapping.values())
    if "date" not in targets or not ({"url", "video_id"} & targets):
        _err("mapping must map at least one column to 'date' and one to "
             "'url' (or 'video_id' for yt).")
        return 1

    funnel_urls: set[str] = set()
    if supports_funnel and args.funnel_urls:
        funnel_urls = {u.strip() for u in args.funnel_urls.split(",") if u.strip()}

    new_rows = []
    for i, mapped in enumerate(mapped_rows, start=1):
        try:
            new_rows.append(build_posts_row(mapped, platform, args.followers, funnel_urls, root))
        except ValueError as exc:
            _err(f"data row {i}: {exc}")
            return 1

    if args.dry_run:
        print(f"[DRY RUN] {platform} — {len(new_rows)} row(s) from {path.name} (nothing written)")
        for i, r in enumerate(new_rows, start=1):
            line = " ".join(f"{k}={r[k]}" for k in metrics.CSV_FIELDS)
            print(f"  row {i}: {line}")
        if dropped:
            print(f"  dropped (unmapped) source column(s): {dropped}")
        print(FORMAT_CAVEAT)
        return 0

    out_path = posts_csv_path(root)
    existing_rows: list[dict] = []
    if out_path.is_file():
        try:
            existing_rows = metrics.read_posts_csv(out_path)
        except ValueError as exc:
            _err(f"existing {out_path} is invalid: {exc}")
            return 1

    final_rows, warnings, n_appended, n_updated = merge_rows(existing_rows, new_rows)
    write_posts_csv(out_path, final_rows)

    for w in warnings:
        print(w)
    print(f"{platform}: {n_appended} row(s) appended, {n_updated} row(s) updated in {out_path}")
    if dropped:
        print(f"(dropped unmapped source column(s): {dropped})")
    print(f"REMINDER: {REMINDER}")
    return 0


def cmd_ig(args) -> int:
    return _ingest(args, "ig", supports_funnel=True)


def cmd_yt(args) -> int:
    return _ingest(args, "yt", supports_funnel=False)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ingest_stats.py",
        description="Ingest a platform analytics export into ops/calendar/posts.csv. "
                     + FORMAT_CAVEAT,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_in = sub.add_parser(
        "inspect",
        help="Sniff a CSV/XLSX export and show the column reconciliation "
             "against the (unvalidated) built-in mappings.",
        description="Sniff a CSV/XLSX export and show the column reconciliation "
                     "against the built-in mappings. " + FORMAT_CAVEAT,
    )
    p_in.add_argument("file")
    p_in.add_argument("--platform", choices=("ig", "yt"), default=None,
                       help="Reconcile against only this platform's mapping (default: both)")
    p_in.set_defaults(func=cmd_inspect)

    p_ig = sub.add_parser(
        "ig",
        help="Ingest an Instagram content export into posts.csv. " + FORMAT_CAVEAT,
        description="Ingest an Instagram professional-dashboard/Business-Suite content "
                     "export into ops/calendar/posts.csv. " + FORMAT_CAVEAT,
    )
    p_ig.add_argument("file")
    p_ig.add_argument("--followers", type=int, required=True)
    p_ig.add_argument("--funnel-urls", default=None,
                       help="Comma-separated URLs to flag funnel=1 (comment-keyword-DM mechanic live)")
    p_ig.add_argument("--mapping", default=None,
                       help="Path to a JSON {\"export column\": \"target field\"} override")
    p_ig.add_argument("--dry-run", action="store_true")
    p_ig.set_defaults(func=cmd_ig)

    p_yt = sub.add_parser(
        "yt",
        help="Ingest a YouTube Studio content export into posts.csv. " + FORMAT_CAVEAT,
        description="Ingest a YouTube Studio content export into ops/calendar/posts.csv. "
                     + FORMAT_CAVEAT,
    )
    p_yt.add_argument("file")
    p_yt.add_argument("--followers", type=int, required=True)
    p_yt.add_argument("--mapping", default=None,
                       help="Path to a JSON {\"export column\": \"target field\"} override")
    p_yt.add_argument("--dry-run", action="store_true")
    p_yt.set_defaults(func=cmd_yt)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
