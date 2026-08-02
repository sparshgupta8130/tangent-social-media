#!/usr/bin/env python
"""pipeline.py — the content-pipeline state machine (SYSTEM_DESIGN.md §5/§7).

One folder per content item under ops/pipeline/NNN-slug/, described by an
item.yaml. This tool is the ONLY thing allowed to move an item's stage; every
skill that advances the pipeline must call it rather than hand-editing YAML.

Subcommands
-----------
    new "<title>" --pillar HERO|WORKHORSE|FILLER --platform ig,yt
        Creates ops/pipeline/NNN-slug/ (NNN = next zero-padded 3-digit id)
        with item.yaml (stage=IDEA) + brief.md + script.md (copied from
        templates/ if present, else stub files with a heading).

    stage NNN STAGE [--due YYYY-MM-DD] [--next-action TEXT]
                    [--next-action-owner OWNER] [--plane-issue ID]
                    [--approved-by-sparsh [YYYY-MM-DD]]
        Validates and applies a legal stage transition (or a same-stage field
        update — see README) and/or updates the given fields.

    board
        Aligned status table of all open (non-CLOSED/KILLED) items: id, slug,
        pillar, stage, next_action_owner, due, OVERDUE flag. Sorted by stage
        order then due date.

    blocked
        Items whose next_action_owner == sparsh (the BLOCKED-ON-SPARSH set)
        plus any overdue open items.

    kill NNN --reason "..."
        Sets stage=KILLED and records kill_reason. Reachable from any stage.

    publish NNN --url <url> [--video <path>]
        Records the published URL + today's date; requires stage==READY, a
        passing G3 brand-review verdict (critiques/G3-brand*.md with
        'VERDICT: ADVANCE' or 'VERDICT: ADVANCE-WITH-NOTES'), and
        approved_by_sparsh set (the SHIP gate), then transitions to
        PUBLISHED. If --video is given, SHA256-hashes the file into
        ops/pipeline/.published_hashes.json and errors if that hash was
        already published anywhere (repost guard).

    validate
        Schema-checks every item.yaml. Non-zero exit on any violation.

Exit codes: 0 success, 1 validation/user error, 2 not-found error.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import _common as c


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# new
# ---------------------------------------------------------------------------

def cmd_new(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    platforms = [p.strip() for p in args.platform.split(",") if p.strip()]
    if not platforms:
        _err("--platform must list at least one of: " + ", ".join(c.PLATFORMS))
        return 1
    for p in platforms:
        if p not in c.PLATFORMS:
            _err(f"unknown platform '{p}' (allowed: {', '.join(c.PLATFORMS)})")
            return 1

    if args.due is not None and not c.is_valid_iso_date(args.due):
        _err(f"--due must be an ISO date (YYYY-MM-DD), got '{args.due}'")
        return 1

    if args.next_action_owner not in c.OWNERS:
        _err(f"--next-action-owner must be one of: {', '.join(c.OWNERS)}")
        return 1

    item_id = c.next_item_id(root)
    slug = c.slugify(args.title)
    folder_name = f"{item_id:03d}-{slug}"
    folder = c.pipeline_dir(root) / folder_name

    if folder.exists():
        _err(f"{folder} already exists")
        return 1

    folder.mkdir(parents=True)

    data = {
        "id": item_id,
        "slug": slug,
        "title": args.title,
        "pillar": args.pillar,
        "platforms": platforms,
        "vertical": args.vertical,
        "stage": "IDEA",
        "created": c.today_iso(),
        "due": args.due,
        "next_action": args.next_action,
        "next_action_owner": args.next_action_owner,
        "plane_issue": args.plane_issue,
        "approved_by_sparsh": None,
        "published": {},
        "kill_reason": None,
    }
    c.save_item(folder, data)

    templates_dir = root / "templates"
    for fname, heading in (("brief.md", f"# Brief — {args.title}"),
                           ("script.md", f"# Script — {args.title}")):
        dest = folder / fname
        src = templates_dir / fname
        if src.is_file():
            shutil.copyfile(src, dest)
        else:
            dest.write_text(heading + "\n", encoding="utf-8", newline="\n")

    print(f"created {folder_name} (id={item_id}, stage=IDEA)")
    return 0


# ---------------------------------------------------------------------------
# stage
# ---------------------------------------------------------------------------

def _g3_error(folder: Path) -> str | None:
    """G3 brand gate (SYSTEM_DESIGN §12.4): READY -> PUBLISHED requires a
    critiques/G3-brand*.md whose verdict line is ADVANCE or ADVANCE-WITH-NOTES.
    A HOLD only clears via a Sparsh override recorded as a later G3-brand-r*.md."""
    critiques_dir = folder / "critiques"
    candidates = sorted(critiques_dir.glob("G3-brand*.md")) if critiques_dir.is_dir() else []
    if not candidates:
        return ("G3 gate not met: no critiques/G3-brand*.md file exists "
                 "(run /brand-review first)")
    accepted = ("VERDICT: ADVANCE", "VERDICT: ADVANCE-WITH-NOTES")
    for cand in candidates:
        text = cand.read_text(encoding="utf-8", errors="replace")
        if any(line.strip() in accepted for line in text.splitlines()):
            return None
    return ("G3 gate not met: no critiques/G3-brand*.md has a 'VERDICT: ADVANCE' or "
             "'VERDICT: ADVANCE-WITH-NOTES' line (a HOLD requires a Sparsh override "
             "recorded in a G3-brand-r2.md)")


def _gate_check(current: str, target: str, folder: Path) -> str | None:
    """Returns an error message if the gate for current->target isn't met,
    else None."""
    if current == "SCRIPTED" and target == "PRODUCING":
        g1 = folder / "critiques" / "G1-script.md"
        if not g1.is_file():
            return ("G1 gate not met: critiques/G1-script.md does not exist "
                     "(run /critique for the script gate first)")
        text = g1.read_text(encoding="utf-8", errors="replace")
        if not any(line.strip() == "VERDICT: SHIP" for line in text.splitlines()):
            return "G1 gate not met: critiques/G1-script.md has no 'VERDICT: SHIP' line"
    if current == "CUT" and target == "READY":
        critiques_dir = folder / "critiques"
        candidates = sorted(critiques_dir.glob("G2-cut*.md")) if critiques_dir.is_dir() else []
        if not candidates:
            return ("G2 gate not met: no critiques/G2-cut*.md file exists "
                     "(run /critique for the cut gate first)")
        ok = False
        for cand in candidates:
            text = cand.read_text(encoding="utf-8", errors="replace")
            if any(line.strip() == "VERDICT: SHIP" for line in text.splitlines()):
                ok = True
                break
        if not ok:
            return "G2 gate not met: no critiques/G2-cut*.md file has a 'VERDICT: SHIP' line"
    if current == "READY" and target == "PUBLISHED":
        g3 = _g3_error(folder)
        if g3:
            return g3
        item = c.load_yaml(folder / c.ITEM_FILENAME)
        if not item.get("approved_by_sparsh"):
            return ("SHIP gate not met: approved_by_sparsh is not set "
                     "(run `pipeline.py stage NNN READY --approved-by-sparsh` first)")
    return None


def cmd_stage(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    target = args.stage.upper()
    if target not in c.ALL_STAGES:
        _err(f"unknown stage '{args.stage}' (allowed: {', '.join(c.ALL_STAGES)})")
        return 1
    if target == "KILLED":
        _err("use `pipeline.py kill NNN --reason \"...\"` to kill an item "
             "(kill always records a reason)")
        return 1

    try:
        folder, item = c.load_item(args.id, root)
    except FileNotFoundError as exc:
        _err(str(exc))
        return 2

    current = item.get("stage")

    if target != current:
        if current == "KILLED":
            _err("item is KILLED; no further transitions are legal")
            return 1
        if current not in c.STAGE_SEQUENCE or target not in c.STAGE_SEQUENCE:
            _err(f"'{current}' -> '{target}' is not a legal transition")
            return 1
        cur_idx = c.STAGE_SEQUENCE.index(current)
        tgt_idx = c.STAGE_SEQUENCE.index(target)
        if tgt_idx != cur_idx + 1:
            next_legal = c.STAGE_SEQUENCE[cur_idx + 1] if cur_idx + 1 < len(c.STAGE_SEQUENCE) else None
            hint = f" (next legal stage is {next_legal})" if next_legal else " (no forward stage remains)"
            _err(f"illegal transition '{current}' -> '{target}'{hint}")
            return 1
        gate_error = _gate_check(current, target, folder)
        if gate_error:
            _err(gate_error)
            return 1

    # Field updates (also usable as a same-stage "touch").
    if args.due is not None:
        if args.due != "" and not c.is_valid_iso_date(args.due):
            _err(f"--due must be an ISO date (YYYY-MM-DD), got '{args.due}'")
            return 1
        item["due"] = args.due or None
    if args.next_action is not None:
        item["next_action"] = args.next_action
    if args.next_action_owner is not None:
        if args.next_action_owner not in c.OWNERS:
            _err(f"--next-action-owner must be one of: {', '.join(c.OWNERS)}")
            return 1
        item["next_action_owner"] = args.next_action_owner
    if args.plane_issue is not None:
        item["plane_issue"] = args.plane_issue or None
    if args.approved_by_sparsh is not None:
        value = c.today_iso() if args.approved_by_sparsh == "__TODAY__" else args.approved_by_sparsh
        if not c.is_valid_iso_date(value):
            _err(f"--approved-by-sparsh must be an ISO date (YYYY-MM-DD), got '{value}'")
            return 1
        item["approved_by_sparsh"] = value

    item["stage"] = target
    c.save_item(folder, item)
    print(f"{folder.name}: {current} -> {target}")
    return 0


# ---------------------------------------------------------------------------
# board / blocked
# ---------------------------------------------------------------------------

def _stage_sort_key(stage: str) -> int:
    try:
        return c.ALL_STAGES.index(stage)
    except ValueError:
        return len(c.ALL_STAGES)


def _is_overdue(item: dict) -> bool:
    due = item.get("due")
    if not due or not c.is_valid_iso_date(due):
        return False
    if item.get("stage") in c.TERMINAL_STAGES:
        return False
    return c.parse_iso_date(due) < c.parse_iso_date(c.today_iso())


def cmd_board(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    items = [(f, i) for f, i in c.iter_items(root) if i.get("stage") not in c.TERMINAL_STAGES]

    def sort_key(pair):
        _, item = pair
        due = item.get("due") or "9999-99-99"
        return (_stage_sort_key(item.get("stage", "")), due)

    items.sort(key=sort_key)

    if not items:
        print("(no open pipeline items)")
        return 0

    rows = []
    for folder, item in items:
        overdue = "OVERDUE" if _is_overdue(item) else ""
        item_id = item.get("id")
        rows.append([
            f"{item_id:03d}" if isinstance(item_id, int) else "?",
            item.get("slug", folder.name),
            item.get("pillar", ""),
            item.get("stage", ""),
            item.get("next_action_owner", ""),
            item.get("due") or "",
            overdue,
        ])
    c.print_table(rows, ["ID", "SLUG", "PILLAR", "STAGE", "OWNER", "DUE", "FLAG"])
    return 0


def cmd_blocked(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    rows = []
    for folder, item in c.iter_items(root):
        if item.get("stage") in c.TERMINAL_STAGES:
            continue
        flags = []
        if item.get("next_action_owner") == "sparsh":
            flags.append("BLOCKED-ON-SPARSH")
        if _is_overdue(item):
            flags.append("OVERDUE")
        if flags:
            item_id = item.get("id")
            rows.append([
                f"{item_id:03d}" if isinstance(item_id, int) else "?",
                item.get("slug", folder.name),
                item.get("stage", ""),
                item.get("next_action", ""),
                item.get("due") or "",
                ", ".join(flags),
            ])

    if not rows:
        print("(nothing blocked)")
        return 0

    rows.sort(key=lambda r: (r[4] or "9999-99-99"))
    c.print_table(rows, ["ID", "SLUG", "STAGE", "NEXT ACTION", "DUE", "FLAG"])
    return 0


# ---------------------------------------------------------------------------
# kill
# ---------------------------------------------------------------------------

def cmd_kill(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    try:
        folder, item = c.load_item(args.id, root)
    except FileNotFoundError as exc:
        _err(str(exc))
        return 2
    item["stage"] = "KILLED"
    item["kill_reason"] = args.reason
    c.save_item(folder, item)
    print(f"{folder.name}: KILLED ({args.reason})")
    return 0


# ---------------------------------------------------------------------------
# publish
# ---------------------------------------------------------------------------

def cmd_publish(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    try:
        folder, item = c.load_item(args.id, root)
    except FileNotFoundError as exc:
        _err(str(exc))
        return 2

    if item.get("stage") != "READY":
        _err(f"item is at stage '{item.get('stage')}', must be READY to publish")
        return 1
    g3 = _g3_error(folder)
    if g3:
        _err(g3)
        return 1
    if not item.get("approved_by_sparsh"):
        _err("approved_by_sparsh is not set — run "
             "`pipeline.py stage NNN READY --approved-by-sparsh` first")
        return 1

    if args.video:
        video_path = Path(args.video)
        if not video_path.is_file():
            _err(f"--video path does not exist: {video_path}")
            return 1
        digest = c.sha256_file(video_path)
        ledger = c.load_published_hashes(root)
        if digest in ledger:
            prior = ledger[digest]
            _err("repost guard: this exact file was already published as "
                 f"item {prior.get('id')} ({prior.get('slug')}) -> {prior.get('url')} "
                 f"on {prior.get('date')}")
            return 1
        ledger[digest] = {
            "id": item.get("id"),
            "slug": item.get("slug"),
            "url": args.url,
            "date": c.today_iso(),
            "path": str(video_path),
        }
        c.save_published_hashes(ledger, root)

    published = item.get("published") or {}
    published[args.url] = c.today_iso()
    item["published"] = published
    item["stage"] = "PUBLISHED"
    c.save_item(folder, item)
    print(f"{folder.name}: PUBLISHED -> {args.url}")
    return 0


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

def _validate_item(folder: Path, item: dict) -> list[str]:
    violations = []
    prefix = f"[{folder.name}]"

    if "__yaml_error__" in item:
        return [f"{prefix} invalid YAML: {item['__yaml_error__']}"]

    required = ("id", "slug", "title", "pillar", "platforms", "vertical", "stage", "created",
                "due", "next_action", "next_action_owner", "plane_issue",
                "approved_by_sparsh", "published", "kill_reason")
    for key in required:
        if key not in item:
            violations.append(f"{prefix} missing required field '{key}'")
    if violations:
        return violations  # can't safely check further without the fields

    m = c.FOLDER_RE.match(folder.name)
    if not m:
        violations.append(f"{prefix} folder name doesn't match NNN-slug pattern")
    else:
        if int(m.group(1)) != item["id"]:
            violations.append(f"{prefix} id {item['id']} does not match folder number {m.group(1)}")
        if m.group(2) != item["slug"]:
            violations.append(f"{prefix} slug '{item['slug']}' does not match folder slug '{m.group(2)}'")

    if item["pillar"] not in c.PILLARS:
        violations.append(f"{prefix} pillar '{item['pillar']}' not in {c.PILLARS}")

    if not isinstance(item["platforms"], list) or not item["platforms"]:
        violations.append(f"{prefix} platforms must be a non-empty list")
    else:
        for p in item["platforms"]:
            if p not in c.PLATFORMS:
                violations.append(f"{prefix} unknown platform '{p}'")

    if item["stage"] not in c.ALL_STAGES:
        violations.append(f"{prefix} unknown stage '{item['stage']}'")

    if not c.is_valid_iso_date(item["created"]):
        violations.append(f"{prefix} created is not an ISO date: {item['created']!r}")

    if item["due"] is not None and not c.is_valid_iso_date(item["due"]):
        violations.append(f"{prefix} due is not null or an ISO date: {item['due']!r}")

    if item.get("vertical") not in c.VERTICALS:
        violations.append(f"{prefix} vertical '{item.get('vertical')}' not in {c.VERTICALS}")

    if item["next_action_owner"] not in c.OWNERS:
        violations.append(f"{prefix} next_action_owner '{item['next_action_owner']}' not in {c.OWNERS}")

    if item["approved_by_sparsh"] is not None and not c.is_valid_iso_date(item["approved_by_sparsh"]):
        violations.append(f"{prefix} approved_by_sparsh is not null or an ISO date")

    if not isinstance(item["published"], dict):
        violations.append(f"{prefix} published must be a dict of url -> ISO date")
    else:
        for url, dt in item["published"].items():
            if not url or not isinstance(url, str):
                violations.append(f"{prefix} published has an empty/non-string url key")
            if not c.is_valid_iso_date(dt):
                violations.append(f"{prefix} published['{url}'] is not an ISO date: {dt!r}")

    if item["stage"] == "KILLED" and not item.get("kill_reason"):
        violations.append(f"{prefix} stage is KILLED but kill_reason is empty")

    if item["stage"] in ("PUBLISHED", "POSTMORTEM", "CLOSED"):
        if not item.get("approved_by_sparsh"):
            violations.append(f"{prefix} stage is {item['stage']} but approved_by_sparsh is not set")
        if not item.get("published"):
            violations.append(f"{prefix} stage is {item['stage']} but published is empty")

    return violations


def cmd_validate(args: argparse.Namespace) -> int:
    root = c.get_repo_root()
    all_violations = []
    n = 0
    for folder, item in c.iter_items(root):
        n += 1
        all_violations.extend(_validate_item(folder, item))

    if all_violations:
        for v in all_violations:
            print(v)
        print(f"\n{len(all_violations)} violation(s) across {n} item(s).")
        return 1

    print(f"all {n} item(s) valid.")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pipeline.py",
        description="Content-pipeline state machine (ops/pipeline/NNN-slug/item.yaml).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="create a new pipeline item (stage=IDEA)")
    p_new.add_argument("title", help="content title")
    p_new.add_argument("--pillar", required=True, choices=c.PILLARS)
    p_new.add_argument("--vertical", default="reels", choices=c.VERTICALS,
                        help="content vertical / craft pack (default: reels)")
    p_new.add_argument("--platform", required=True, help="comma-separated, e.g. ig,yt")
    p_new.add_argument("--due", default=None, help="ISO date YYYY-MM-DD")
    p_new.add_argument("--next-action", default="Write brief and score concept",
                        dest="next_action")
    p_new.add_argument("--next-action-owner", default="creative-director",
                        dest="next_action_owner")
    p_new.add_argument("--plane-issue", default=None, dest="plane_issue")
    p_new.set_defaults(func=cmd_new)

    p_stage = sub.add_parser("stage", help="transition (or touch) an item's stage")
    p_stage.add_argument("id", type=int)
    p_stage.add_argument("stage")
    p_stage.add_argument("--due", default=None, help="ISO date YYYY-MM-DD, or '' to clear")
    p_stage.add_argument("--next-action", default=None, dest="next_action")
    p_stage.add_argument("--next-action-owner", default=None, dest="next_action_owner")
    p_stage.add_argument("--plane-issue", default=None, dest="plane_issue")
    p_stage.add_argument("--approved-by-sparsh", nargs="?", const="__TODAY__",
                          default=None, dest="approved_by_sparsh",
                          help="set approval date (defaults to today if given with no value)")
    p_stage.set_defaults(func=cmd_stage)

    p_board = sub.add_parser("board", help="status table of open items")
    p_board.set_defaults(func=cmd_board)

    p_blocked = sub.add_parser("blocked", help="BLOCKED-ON-SPARSH + overdue items")
    p_blocked.set_defaults(func=cmd_blocked)

    p_kill = sub.add_parser("kill", help="kill an item (reachable from any stage)")
    p_kill.add_argument("id", type=int)
    p_kill.add_argument("--reason", required=True)
    p_kill.set_defaults(func=cmd_kill)

    p_publish = sub.add_parser("publish", help="record publish URL/date, transition to PUBLISHED")
    p_publish.add_argument("id", type=int)
    p_publish.add_argument("--url", required=True)
    p_publish.add_argument("--video", default=None, help="path to exported file (repost guard)")
    p_publish.set_defaults(func=cmd_publish)

    p_validate = sub.add_parser("validate", help="schema-check every item.yaml")
    p_validate.set_defaults(func=cmd_validate)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
