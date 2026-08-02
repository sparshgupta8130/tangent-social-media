#!/usr/bin/env python
"""brandkit_check.py — deterministic validator for brand/kit.yaml (SYSTEM_DESIGN_V2_PROPOSAL.md
§4.1). Same conventions as the sibling tools (argparse, --json, TANGENT_ROOT-aware exit codes).

Subcommands
-----------
    validate [--json]
        Loads brand/kit.yaml and checks: (1) it parses to a mapping, (2) every path in
        REQUIRED_PATHS below is present (key exists, value may legitimately be null — e.g. an
        unset handle), (3) every `null` leaf value anywhere in the file has a matching entry in
        `meta.todo_sparsh` (an "unfilled non-TODO null" is an error), and (4) every
        `meta.todo_sparsh` entry's declared dotted path actually exists somewhere in the file
        (catches a stale/typo'd TODO — reported as a warning, not a failure).

    caption [FILE] [--platform ig|yt] [--json]
        Reads caption text from FILE if given (must exist) or from stdin if FILE is omitted.
        Runs, against the loaded kit: a case-insensitive, word-boundary banned-word scan
        (verbal.banned_words.starter_list + kit_additions), a disclosure-line presence check
        (verbal.disclosure_lines.instagram_caption / youtube_description — ALL required_keywords
        must appear, case-insensitive substring), and a caption-footer check (hashtag count <= 5,
        no known URL-shortener domain). For --platform ig, also prints an informational (non-
        blocking) first-125-characters report per the scripting-voice.md truncation rule.

    export <video> [--platform ig|yt|yt-long] [--json]
        SKELETON ONLY. Runs the same checks as `validate` against brand/kit.yaml and reports
        them, then prints "visual checks pending Phase R2 (logo/palette detection)" and exits 0
        regardless of the kit-validate result — this subcommand does NOT open, decode, or inspect
        the video file in any way yet. It exists so the export call-site is stable; do not treat
        a 0 exit here as any kind of visual-compliance signal. That is the honest scope: this is
        a placeholder, not a passing check.

Exit codes
----------
    validate:  0 clean, 1 validation failure(s) found, 2 kit.yaml missing/unparseable
    caption:   0 all checks passed, 1 at least one check failed, 2 kit.yaml or input file problem
    export:    0 always (skeleton), except 2 if kit.yaml itself is missing/unparseable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

import _common as c

KIT_RELATIVE_PATH = Path("brand") / "kit.yaml"

REQUIRED_TOP_KEYS = ("identity", "verbal", "visual", "distinctive_assets", "per_vertical", "meta")

# Dotted paths that must exist in the parsed kit (value may be null; presence is what's checked).
REQUIRED_PATHS = (
    "identity.brand_name",
    "identity.surfaces.gallery.domain",
    "identity.surfaces.instagram.handle",
    "identity.surfaces.youtube.handle",
    "identity.surfaces.series_channel.handle",
    "verbal.tagline",
    "verbal.disclosure_lines.instagram_caption.standard",
    "verbal.disclosure_lines.instagram_caption.required_keywords",
    "verbal.disclosure_lines.youtube_description.standard",
    "verbal.disclosure_lines.youtube_description.required_keywords",
    "verbal.disclosure_lines.on_screen.standard",
    "verbal.banned_words.starter_list",
    "verbal.banned_words.kit_additions",
    "verbal.caption_footer.rules",
    "visual.palette.gallery_white.hex",
    "visual.palette.ink.hex",
    "visual.type.display_face",
    "visual.type.ui_face",
    "visual.logo.wordmark_path",
    "visual.logo.mark_path",
    "visual.safe_zone_1080x1920.top_px",
    "visual.safe_zone_1080x1920.bottom_px",
    "visual.safe_zone_1080x1920.right_pct",
    "distinctive_assets.critic_rejection_card",
    "distinctive_assets.before_after_snap",
    "distinctive_assets.sliders_visible",
    "meta.todo_sparsh",
) + tuple(f"per_vertical.{v}" for v in c.VERTICALS)

URL_SHORTENER_DOMAINS = (
    "bit.ly", "tinyurl.com", "t.co", "ow.ly", "is.gd", "buff.ly", "goo.gl", "rebrand.ly", "cutt.ly",
)

IG_FIRST_CHARS = 125

PLATFORM_TO_DISCLOSURE_KEY = {"ig": "instagram_caption", "yt": "youtube_description"}


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# kit.yaml load
# ---------------------------------------------------------------------------

def kit_path(root: Path | None = None) -> Path:
    root = root or c.get_repo_root()
    return root / KIT_RELATIVE_PATH


def load_kit(root: Path | None = None) -> dict:
    """Raises FileNotFoundError / yaml.YAMLError / ValueError — caller maps to exit 2."""
    path = kit_path(root)
    if not path.is_file():
        raise FileNotFoundError(str(path))
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse to a mapping (got {type(data).__name__})")
    return data


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

def _walk_null_paths(node, prefix: str = ""):
    """Yields dotted paths of every leaf whose value is None. Dict keys only (no list indexing
    needed — nothing in kit.yaml's schema nests a null inside a list)."""
    if isinstance(node, dict):
        for k, v in node.items():
            path = f"{prefix}.{k}" if prefix else str(k)
            yield from _walk_null_paths(v, path)
    else:
        if node is None:
            yield prefix


def _path_present(data: dict, path: str) -> bool:
    node = data
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return True


def _declared_todo_paths(todo_sparsh: list) -> set[str]:
    """Convention: each entry is "dotted.path: free-text explanation" (an em-dash after the
    path is also accepted). Returns the set of declared dotted-path heads."""
    declared = set()
    for entry in todo_sparsh or []:
        if not isinstance(entry, str):
            continue
        head = re.split(r"[:—]", entry, maxsplit=1)[0].strip()
        if head:
            declared.add(head)
    return declared


def validate_kit(data: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    for key in REQUIRED_TOP_KEYS:
        if key not in data or data[key] is None:
            errors.append(f"missing required top-level key: {key}")

    missing_paths = [p for p in REQUIRED_PATHS if not _path_present(data, p)]
    for p in missing_paths:
        errors.append(f"missing required key: {p}")

    meta = data.get("meta") or {}
    todo_sparsh = meta.get("todo_sparsh") or []
    declared = _declared_todo_paths(todo_sparsh)

    null_paths = sorted(set(_walk_null_paths(data)))
    undeclared_nulls = [p for p in null_paths if p not in declared]
    for p in undeclared_nulls:
        errors.append(f"unfilled null not declared in meta.todo_sparsh: {p}")

    stale_todos = sorted(p for p in declared if not _path_present(data, p))
    for p in stale_todos:
        warnings.append(f"meta.todo_sparsh declares '{p}' but that path does not exist in "
                         f"kit.yaml (typo, or the TODO is stale and should be removed)")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "null_count": len(null_paths),
        "declared_todo_count": len(declared),
    }


# ---------------------------------------------------------------------------
# caption
# ---------------------------------------------------------------------------

def _flatten_banned_words(data: dict) -> list[str]:
    bw = (data.get("verbal") or {}).get("banned_words") or {}
    return list(bw.get("starter_list") or []) + list(bw.get("kit_additions") or [])


def scan_banned_words(text: str, words: list[str]) -> list[dict]:
    hits = []
    for phrase in words:
        pattern = r"\b" + re.escape(phrase) + r"\b"
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            hits.append({"phrase": phrase, "matched": m.group(0), "position": m.start()})
    hits.sort(key=lambda h: h["position"])
    return hits


def check_disclosure(text: str, data: dict, platform: str) -> dict:
    key = PLATFORM_TO_DISCLOSURE_KEY[platform]
    cfg = ((data.get("verbal") or {}).get("disclosure_lines") or {}).get(key) or {}
    required = list(cfg.get("required_keywords") or [])
    lowered = text.lower()
    missing = [kw for kw in required if kw.lower() not in lowered]
    return {
        "checked_line": key,
        "required_keywords": required,
        "missing_keywords": missing,
        "present": not missing,
    }


def check_footer(text: str) -> dict:
    hashtags = re.findall(r"#\w+", text)
    lowered = text.lower()
    shorteners_found = [d for d in URL_SHORTENER_DOMAINS if d in lowered]
    problems = []
    if len(hashtags) > 5:
        problems.append(f"{len(hashtags)} hashtags found, max 5 (`platform/instagram.md` §3)")
    if shorteners_found:
        problems.append(
            f"URL shortener domain(s) found: {', '.join(shorteners_found)} "
            f"(`platform/instagram.md` §8)"
        )
    return {
        "hashtag_count": len(hashtags),
        "shorteners_found": shorteners_found,
        "ok": not problems,
        "problems": problems,
    }


def first_n_chars_report(text: str, n: int = IG_FIRST_CHARS) -> dict:
    return {"n": n, "text": text[:n], "truncated": len(text) > n}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _load_kit_or_exit(root: Path):
    """Returns (data, None) on success, or (None, exit_code) on failure — printing the error."""
    try:
        return load_kit(root), None
    except FileNotFoundError as exc:
        _err(f"kit.yaml not found at {exc}")
        return None, 2
    except (yaml.YAMLError, ValueError) as exc:
        _err(f"kit.yaml did not parse: {exc}")
        return None, 2


def cmd_validate(args) -> int:
    root = c.get_repo_root()
    data, exit_code = _load_kit_or_exit(root)
    if data is None:
        return exit_code

    result = validate_kit(data)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"kit.yaml: {kit_path(root)}")
        print(f"nulls found: {result['null_count']}  declared TODOs: {result['declared_todo_count']}")
        if result["errors"]:
            print("ERRORS:")
            for e in result["errors"]:
                print(f"  - {e}")
        if result["warnings"]:
            print("WARNINGS:")
            for w in result["warnings"]:
                print(f"  - {w}")
        print("overall: " + ("PASS" if result["ok"] else "FAIL"))
    return 0 if result["ok"] else 1


def cmd_caption(args) -> int:
    root = c.get_repo_root()
    data, exit_code = _load_kit_or_exit(root)
    if data is None:
        return exit_code

    if args.file:
        path = Path(args.file)
        if not path.is_file():
            _err(f"file does not exist: {path}")
            return 2
        text = path.read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    words = _flatten_banned_words(data)
    banned_hits = scan_banned_words(text, words)
    disclosure = check_disclosure(text, data, args.platform)
    footer = check_footer(text)

    result = {
        "platform": args.platform,
        "banned_word_hits": banned_hits,
        "disclosure": disclosure,
        "footer": footer,
    }
    if args.platform == "ig":
        result["first_125_chars"] = first_n_chars_report(text)

    ok = not banned_hits and disclosure["present"] and footer["ok"]
    result["ok"] = ok

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"platform: {args.platform}")
        if banned_hits:
            print(f"BANNED WORDS FOUND ({len(banned_hits)}):")
            for h in banned_hits:
                print(f"  - '{h['matched']}' (rule: '{h['phrase']}') at char {h['position']}")
        else:
            print("banned words: none found")
        if disclosure["present"]:
            print(f"disclosure ({disclosure['checked_line']}): PRESENT")
        else:
            print(f"disclosure ({disclosure['checked_line']}): MISSING keywords "
                  f"{disclosure['missing_keywords']}")
        if footer["ok"]:
            print(f"footer: OK (hashtags={footer['hashtag_count']})")
        else:
            print(f"footer: PROBLEMS -- {'; '.join(footer['problems'])}")
        if args.platform == "ig":
            r = result["first_125_chars"]
            suffix = " (truncated)" if r["truncated"] else ""
            print(f"first {r['n']} chars: {r['text']!r}{suffix}")
        print("overall: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def cmd_export(args) -> int:
    root = c.get_repo_root()
    data, exit_code = _load_kit_or_exit(root)
    if data is None:
        return exit_code

    kit_result = validate_kit(data)
    note = "visual checks pending Phase R2 (logo/palette detection)"
    result = {
        "video": args.video,
        "platform": args.platform,
        "kit_validate": kit_result,
        "note": note,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"video: {args.video}")
        print(f"platform: {args.platform}")
        if kit_result["ok"]:
            print("kit validate: PASS")
        else:
            print(f"kit validate: FAIL ({len(kit_result['errors'])} error(s) -- "
                  f"run `brandkit_check.py validate` for detail)")
        print(note)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brandkit_check.py",
        description=(
            "Deterministic brand/kit.yaml validator: schema + TODO-null checks, caption "
            "compliance (banned words, disclosure, footer), and an honest export skeleton. "
            "The export subcommand does NOT perform visual (logo/palette) detection yet -- "
            "see its --help for exact scope."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_val = sub.add_parser(
        "validate",
        help="brand/kit.yaml parses + required keys present + every null has a declared TODO",
    )
    p_val.add_argument("--json", action="store_true")
    p_val.set_defaults(func=cmd_validate)

    p_cap = sub.add_parser(
        "caption",
        help="banned-word / disclosure-line / footer checks on caption text (file or stdin)",
    )
    p_cap.add_argument("file", nargs="?", default=None,
                        help="path to a text file containing the caption; omit to read stdin")
    p_cap.add_argument("--platform", choices=("ig", "yt"), default="ig")
    p_cap.add_argument("--json", action="store_true")
    p_cap.set_defaults(func=cmd_caption)

    p_exp = sub.add_parser(
        "export",
        help="SKELETON -- runs kit validate only; visual checks pending Phase R2 (no fake pass)",
    )
    p_exp.add_argument("video")
    p_exp.add_argument("--platform", choices=("ig", "yt", "yt-long"), default="ig")
    p_exp.add_argument("--json", action="store_true")
    p_exp.set_defaults(func=cmd_export)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
