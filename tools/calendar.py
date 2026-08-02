#!/usr/bin/env python
"""calendar.py — renders a markdown week-grid from ROADMAP.md + live pipeline state.

Combines ops/calendar/ROADMAP.md's planned item lines with the live pipeline
state (every ops/pipeline/*/item.yaml) into a week-by-week grid, and flags:
    - cadence-band violations: floor 2 reels/week, steady band 3-5/week
      (strategy/STRATEGY.md §7)
    - HERO-drought: no HERO item PUBLISHED (in the trailing 7 days) or
      currently READY

ROADMAP.md format expected (produced by the planner / `/plan` skill; see
ops/pipeline/README.md's rolling-roadmap section and templates/roadmap-week.md
for the authoring side of this contract):

    ## Week of YYYY-MM-DD

    **Cadence target:** steady-state | launch-surge -- why this band this week
    **HERO drought check:** ...

    | Day | Pillar | Item (id-slug) | Stage now | Risk |
    |---|---|---|---|---|
    | Mon | HERO | `003-some-slug` | SCRIPTED | none |
    | Tue | WORKHORSE | `004-other-slug` | BRIEFED | BLOCKED-ON-SPARSH |

One table row per planned item: pillar must be exactly HERO/WORKHORSE/FILLER,
the ref is a backtick-quoted NNN-slug, the day name (Mon..Sun) is used to
compute that item's date within the week. Unfilled template rows (blank
cells, literal "HERO|WORKHORSE|FILLER" placeholders, blank refs) simply don't
match and are skipped.

A missing or unparseable ROADMAP.md is treated as an empty roadmap (zero
planned items) rather than an error -- the tool still renders the grid and
still runs the pipeline-state-derived checks.

Usage
-----
    calendar.py [--weeks N] [--write]

Prints to stdout. --write additionally saves to ops/calendar/calendar-view.md.

Exit codes: 0 always (this is a reporting tool, not a gate).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import _common as c

DEFAULT_WEEKS = 4
FLOOR_PER_WEEK = 2
STEADY_BAND = (3, 5)
HERO_DROUGHT_WINDOW_DAYS = 7

WEEK_HEADER_RE = re.compile(r"^##\s*Week of\s+(\d{4}-\d{2}-\d{2})\s*$")

# | Day | Pillar | Item (id-slug) | Stage now | Risk |
TABLE_ROW_RE = re.compile(
    r"^\|\s*(?P<day>[A-Za-z]+)\s*\|\s*(?P<pillar>HERO|WORKHORSE|FILLER)\s*\|\s*"
    r"`?(?P<ref>\d{3}-[a-z0-9-]+)`?\s*\|\s*(?P<stage>[A-Za-z]+)\s*\|\s*(?P<risk>[^|]*)\|\s*$"
)

DAY_OFFSETS = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}


def parse_roadmap(path: Path) -> dict:
    """Returns {week_start_iso: [{"pillar", "ref", "stage", "risk", "due"}, ...]}.
    Empty dict if the file is missing or has no parseable week/table rows.
    Unfilled template rows (placeholder pillar text, blank cells) don't match
    TABLE_ROW_RE and are silently skipped."""
    weeks: dict[str, list[dict]] = {}
    if not path.is_file():
        return weeks

    current_week = None
    week_start_date = None
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.rstrip()
        m_week = WEEK_HEADER_RE.match(line)
        if m_week:
            current_week = m_week.group(1)
            week_start_date = c.parse_iso_date(current_week)
            weeks.setdefault(current_week, [])
            continue
        if current_week is None:
            continue
        m_row = TABLE_ROW_RE.match(line)
        if not m_row:
            continue
        day_offset = DAY_OFFSETS.get(m_row.group("day").lower()[:3])
        due = ((week_start_date + timedelta(days=day_offset)).isoformat()
               if day_offset is not None else None)
        weeks[current_week].append({
            "pillar": m_row.group("pillar").upper(),
            "ref": m_row.group("ref"),
            "stage": m_row.group("stage").upper(),
            "risk": m_row.group("risk").strip(),
            "due": due,
        })
    return weeks


def monday_of(d: date) -> date:
    return d - timedelta(days=d.weekday())


def build_week_grid(roadmap: dict, weeks_count: int, pipeline_items: list[dict]) -> list[dict]:
    start = monday_of(date.today())
    grid = []
    for i in range(weeks_count):
        week_start = start + timedelta(weeks=i)
        week_end = week_start + timedelta(days=6)
        wk_key = week_start.isoformat()
        roadmap_items = roadmap.get(wk_key, [])
        roadmap_refs = {ri["ref"] for ri in roadmap_items}

        extra_pipeline = []
        for item in pipeline_items:
            due = item.get("due")
            if not due or not c.is_valid_iso_date(due):
                continue
            due_date = c.parse_iso_date(due)
            if not (week_start <= due_date <= week_end):
                continue
            ref_candidates = {item.get("slug", ""), f"{item.get('id', 0):03d}-{item.get('slug', '')}"}
            if ref_candidates & roadmap_refs:
                continue
            extra_pipeline.append({
                "pillar": item.get("pillar", ""),
                "ref": f"{item.get('id', 0):03d}-{item.get('slug', '')}",
                "due": due,
            })

        total_count = len(roadmap_items) + len(extra_pipeline)
        if total_count < FLOOR_PER_WEEK:
            cadence_flag = f"FLOOR VIOLATION (<{FLOOR_PER_WEEK}/week)"
        elif not (STEADY_BAND[0] <= total_count <= STEADY_BAND[1]):
            cadence_flag = f"OUTSIDE STEADY BAND ({STEADY_BAND[0]}-{STEADY_BAND[1]}/week)"
        else:
            cadence_flag = "OK"

        grid.append({
            "week_start": wk_key,
            "week_end": week_end.isoformat(),
            "roadmap_items": roadmap_items,
            "extra_pipeline_items": extra_pipeline,
            "total_count": total_count,
            "cadence_flag": cadence_flag,
        })
    return grid


def check_hero_drought(pipeline_items: list[dict]) -> bool:
    """True if there is NO HERO item that is currently READY, or that has a
    published date within the trailing HERO_DROUGHT_WINDOW_DAYS days."""
    today = date.today()
    window_start = today - timedelta(days=HERO_DROUGHT_WINDOW_DAYS)
    for item in pipeline_items:
        if item.get("pillar") != "HERO":
            continue
        if item.get("stage") == "READY":
            return False
        published = item.get("published") or {}
        for _, dt in published.items():
            if c.is_valid_iso_date(dt) and window_start <= c.parse_iso_date(dt) <= today:
                return False
    return True


def render_markdown(grid: list[dict], drought: bool, weeks_count: int) -> str:
    lines = [f"# Calendar view ({weeks_count} week(s) from {grid[0]['week_start']})", ""]
    if drought:
        lines.append(f"**HERO-DROUGHT WARNING**: no HERO item READY or published "
                      f"in the trailing {HERO_DROUGHT_WINDOW_DAYS} days.")
        lines.append("")
    for wk in grid:
        lines.append(f"## Week of {wk['week_start']} (through {wk['week_end']})")
        lines.append(f"cadence: {wk['total_count']} item(s) -> {wk['cadence_flag']}")
        lines.append("")
        if not wk["roadmap_items"] and not wk["extra_pipeline_items"]:
            lines.append("(nothing planned)")
        else:
            for ri in wk["roadmap_items"]:
                due = f" (due {ri['due']})" if ri.get("due") else ""
                risk = f" [risk: {ri['risk']}]" if ri.get("risk") else ""
                lines.append(f"- [{ri['pillar']}] {ri['ref']}{due} (stage {ri['stage']}){risk}")
            for pi in wk["extra_pipeline_items"]:
                due = f" (due {pi['due']})" if pi.get("due") else ""
                lines.append(f"- [{pi['pillar']}] {pi['ref']}{due} [from pipeline, not on roadmap]")
        lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="calendar.py",
        description="Render a markdown week-grid from ROADMAP.md + live pipeline state.",
    )
    parser.add_argument("--weeks", type=int, default=DEFAULT_WEEKS)
    parser.add_argument("--write", action="store_true",
                         help="also save to ops/calendar/calendar-view.md")
    args = parser.parse_args(argv)

    if args.weeks <= 0:
        print("ERROR: --weeks must be > 0", file=sys.stderr)
        return 1

    root = c.get_repo_root()
    roadmap_path = root / "ops" / "calendar" / "ROADMAP.md"
    roadmap = parse_roadmap(roadmap_path)
    pipeline_items = [item for _, item in c.iter_items(root)]

    grid = build_week_grid(roadmap, args.weeks, pipeline_items)
    drought = check_hero_drought(pipeline_items)
    output = render_markdown(grid, drought, args.weeks)

    print(output)

    if args.write:
        dest = root / "ops" / "calendar" / "calendar-view.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(output + "\n", encoding="utf-8", newline="\n")
        print(f"\n(written to {dest})", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
