"""_common.py — shared helpers for the Tangent deterministic tools.

Not a CLI itself. Provides: repo-root resolution (respects TANGENT_ROOT for
tests/sandboxing), the item.yaml schema constants, YAML load/save, pipeline
item discovery, date helpers, and the published-hash ledger used by both
pipeline.py (repost guard on publish) and hygiene_check.py (repost guard on
export).

All file I/O is UTF-8 explicit and pathlib-based (Windows-path-safe).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

# ---------------------------------------------------------------------------
# Schema constants (item.yaml) — must stay in sync across all tools.
# ---------------------------------------------------------------------------

PILLARS = ("HERO", "WORKHORSE", "FILLER")

PLATFORMS = ("ig", "yt", "yt-long")

VERTICALS = ("reels", "longform", "podcast", "music", "app", "image", "newsletter")

# Forward-only legal sequence. KILLED is reachable from any stage but only
# via `pipeline.py kill` (never via a bare `stage` transition) so a reason is
# always recorded.
STAGE_SEQUENCE = (
    "IDEA",
    "BRIEFED",
    "SCRIPTED",
    "PRODUCING",
    "CUT",
    "READY",
    "PUBLISHED",
    "POSTMORTEM",
    "CLOSED",
)

ALL_STAGES = STAGE_SEQUENCE + ("KILLED",)

TERMINAL_STAGES = ("CLOSED", "KILLED")

OWNERS = (
    "creative-director",
    "trend-scout",
    "story-lead",
    "producer",
    "critic",
    "analyst",
    "planner",
    "brand-director",
    "growth-lead",
    "audience-advocate",
    "revenue-lead",
    "showrunner",
    "sparsh",
)

ITEM_FILENAME = "item.yaml"
PUBLISHED_HASHES_FILENAME = ".published_hashes.json"

FOLDER_RE = re.compile(r"^(\d{3,})-(.+)$")


# ---------------------------------------------------------------------------
# Repo root / paths
# ---------------------------------------------------------------------------

def get_repo_root() -> Path:
    """Resolve the repo root.

    Respects TANGENT_ROOT (used by tests/tests/smoke.py to sandbox all
    filesystem effects). Defaults to the parent of tools/, i.e. this file's
    grandparent directory, which is the real repo root in production.
    """
    env_root = os.environ.get("TANGENT_ROOT")
    if env_root:
        return Path(env_root).resolve()
    return Path(__file__).resolve().parent.parent


def pipeline_dir(root: Path | None = None) -> Path:
    root = root or get_repo_root()
    return root / "ops" / "pipeline"


def published_hashes_path(root: Path | None = None) -> Path:
    return pipeline_dir(root) / PUBLISHED_HASHES_FILENAME


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def today_iso() -> str:
    return date.today().isoformat()


def parse_iso_date(value: str) -> date:
    """Raises ValueError with a clear message on malformed input.

    Deliberately uses date.fromisoformat rather than datetime.strptime:
    strptime lazily imports the stdlib `calendar` module on first use, and
    since tools/calendar.py sits in this same directory (on sys.path[0] for
    every script here), that lazy import would resolve to OUR calendar.py
    instead of the stdlib one and crash. fromisoformat never touches the
    `calendar` module. The regex pre-check keeps validation strictly
    YYYY-MM-DD (fromisoformat alone is more permissive on 3.11+).
    """
    if not isinstance(value, str) or not _ISO_DATE_RE.match(value):
        raise ValueError(f"not an ISO date (YYYY-MM-DD): {value!r}")
    return date.fromisoformat(value)


def is_valid_iso_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parse_iso_date(value)
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# YAML item I/O
# ---------------------------------------------------------------------------

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data or {}


def save_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True, default_flow_style=False)


def item_folder_for_id(item_id: int, root: Path | None = None) -> Path | None:
    """Find the NNN-slug folder for a given numeric id. None if not found."""
    pdir = pipeline_dir(root)
    if not pdir.is_dir():
        return None
    padded = f"{item_id:03d}"
    for child in sorted(pdir.iterdir()):
        if not child.is_dir():
            continue
        m = FOLDER_RE.match(child.name)
        if not m:
            continue
        # Compare numerically (handles ids >= 1000 too) AND the zero-padded
        # 3-digit form, so both "007" and, if it ever happens, "1000" match.
        if m.group(1) == padded or int(m.group(1)) == item_id:
            return child
    return None


def load_item(item_id: int, root: Path | None = None) -> tuple[Path, dict]:
    """Returns (folder, data). Raises FileNotFoundError if not found."""
    folder = item_folder_for_id(item_id, root)
    if folder is None:
        raise FileNotFoundError(f"no pipeline item with id {item_id:03d}")
    item_path = folder / ITEM_FILENAME
    if not item_path.is_file():
        raise FileNotFoundError(f"{item_path} is missing")
    return folder, load_yaml(item_path)


def save_item(folder: Path, data: dict) -> None:
    save_yaml(folder / ITEM_FILENAME, data)


def iter_items(root: Path | None = None):
    """Yields (folder, data) for every ops/pipeline/*/item.yaml, sorted by id."""
    pdir = pipeline_dir(root)
    if not pdir.is_dir():
        return
    folders = []
    for child in pdir.iterdir():
        if not child.is_dir():
            continue
        if not FOLDER_RE.match(child.name):
            continue
        item_path = child / ITEM_FILENAME
        if item_path.is_file():
            folders.append(child)
    folders.sort(key=lambda p: p.name)
    for folder in folders:
        try:
            yield folder, load_yaml(folder / ITEM_FILENAME)
        except yaml.YAMLError as exc:
            yield folder, {"__yaml_error__": str(exc)}


def next_item_id(root: Path | None = None) -> int:
    max_id = 0
    for folder, _ in iter_items(root):
        m = FOLDER_RE.match(folder.name)
        if m:
            max_id = max(max_id, int(m.group(1)))
    return max_id + 1


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


# ---------------------------------------------------------------------------
# Hashing / repost-guard ledger
# ---------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_published_hashes(root: Path | None = None) -> dict:
    p = published_hashes_path(root)
    if not p.is_file():
        return {}
    with p.open("r", encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError:
            return {}


def save_published_hashes(data: dict, root: Path | None = None) -> None:
    p = published_hashes_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)
        fh.write("\n")


# ---------------------------------------------------------------------------
# Misc
# ---------------------------------------------------------------------------

def print_table(rows: list[list[str]], headers: list[str]) -> None:
    """Prints a simple left-aligned, whitespace-padded table to stdout."""
    all_rows = [headers] + rows
    widths = [max(len(str(r[i])) for r in all_rows) for i in range(len(headers))]
    def fmt_row(r):
        return "  ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(r))
    print(fmt_row(headers))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(fmt_row(r))
