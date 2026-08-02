#!/usr/bin/env python
"""tests/smoke.py — no-network smoke test for the Tangent deterministic tools.

Runs every tool as a subprocess (black-box, exactly as a skill would invoke
it) against a temporary sandbox directory pointed to by the TANGENT_ROOT
environment variable, so nothing under the real repo tree is touched.

Covers:
    - pipeline.py: new / legal stage transitions / an illegal transition
      rejected / both gate checks (G1, G2, SHIP) blocking and then passing /
      kill / publish + repost guard / board / blocked / validate (clean and
      with an injected violation)
    - metrics.py: likerate, all five decompose quadrants, efficiency,
      funnel, report (against an inline CSV fixture)
    - verify_stats.py: dependency-detection path (yt-dlp not installed in
      this environment -> clean exit 2)
    - hygiene_check.py: dependency-detection path (ffprobe not installed in
      this environment -> clean exit 2)
    - calendar.py: runs cleanly against an empty ROADMAP.md
    - brandkit_check.py: validate against the REAL brand/kit.yaml (read-only,
      so unlike every tool above this one runs with TANGENT_ROOT pointed at
      the actual repo root, not the sandbox); caption catches a planted
      banned word, catches a missing disclosure line, passes a clean caption
      (file and stdin input both exercised); export skeleton runs and never
      fakes a visual-check pass.

Usage: python tools\\tests\\smoke.py
Exit codes: 0 all cases passed, 1 at least one FAIL.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

TOOLS_DIR = Path(__file__).resolve().parent.parent
RESULTS: list[tuple[str, str, str]] = []


def check(name: str, condition: bool, detail: str = "") -> bool:
    status = "PASS" if condition else "FAIL"
    RESULTS.append((name, status, detail))
    line = f"[{status}] {name}"
    if detail and status == "FAIL":
        line += f" -- {detail}"
    print(line)
    return condition


def run(tool: str, args: list[str], env: dict, input_text: str | None = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(TOOLS_DIR / tool)] + args
    kwargs = dict(capture_output=True, text=True, encoding="utf-8", errors="replace",
                  env=env, timeout=60)
    if input_text is not None:
        kwargs["input"] = input_text
    return subprocess.run(cmd, **kwargs)


def read_item(tmp_root: str, item_id: int):
    pdir = Path(tmp_root) / "ops" / "pipeline"
    matches = list(pdir.glob(f"{item_id:03d}-*/item.yaml"))
    if not matches:
        raise AssertionError(f"no item folder found for id {item_id}")
    with matches[0].open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data, matches[0].parent


def advance_to_ready(env: dict, tmp: str, item_id: int) -> None:
    """Fast-tracks an item from IDEA to READY+approved, writing the critique
    gate files it needs along the way. Used to set up the repost-guard test
    without repeating the full step-by-step gate assertions already covered
    for item 1."""
    for stage in ("BRIEFED", "SCRIPTED"):
        r = run("pipeline.py", ["stage", str(item_id), stage], env)
        check(f"item{item_id}_to_{stage}", r.returncode == 0, r.stderr)

    _, folder = read_item(tmp, item_id)
    critiques = folder / "critiques"
    critiques.mkdir(parents=True, exist_ok=True)
    (critiques / "G1-script.md").write_text("VERDICT: SHIP\n", encoding="utf-8")

    r = run("pipeline.py", ["stage", str(item_id), "PRODUCING"], env)
    check(f"item{item_id}_to_PRODUCING", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["stage", str(item_id), "CUT"], env)
    check(f"item{item_id}_to_CUT", r.returncode == 0, r.stderr)

    (critiques / "G2-cut-r1.md").write_text("VERDICT: SHIP\n", encoding="utf-8")

    r = run("pipeline.py", ["stage", str(item_id), "READY"], env)
    check(f"item{item_id}_to_READY", r.returncode == 0, r.stderr)

    (critiques / "G3-brand.md").write_text("VERDICT: ADVANCE\n", encoding="utf-8")

    r = run("pipeline.py", ["stage", str(item_id), "READY", "--approved-by-sparsh"], env)
    check(f"item{item_id}_approved", r.returncode == 0, r.stderr)


def test_pipeline(env: dict, tmp: str) -> None:
    print("\n-- pipeline.py --")

    r = run("pipeline.py", ["new", "Claude Edits Demo", "--pillar", "HERO",
                             "--platform", "ig,yt"], env)
    check("new_creates_item_exit0", r.returncode == 0, r.stderr)
    folder = Path(tmp) / "ops" / "pipeline" / "001-claude-edits-demo"
    check("new_creates_folder", folder.is_dir(), str(folder))
    check("new_creates_item_yaml", (folder / "item.yaml").is_file())
    check("new_creates_brief", (folder / "brief.md").is_file())
    check("new_creates_script", (folder / "script.md").is_file())
    item, _ = read_item(tmp, 1)
    check("new_stage_is_idea", item.get("stage") == "IDEA", str(item.get("stage")))
    check("new_owner_default", item.get("next_action_owner") == "creative-director")

    r = run("pipeline.py", ["stage", "1", "BRIEFED"], env)
    check("legal_idea_to_briefed", r.returncode == 0, r.stderr)
    r = run("pipeline.py", ["stage", "1", "SCRIPTED"], env)
    check("legal_briefed_to_scripted", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["stage", "1", "PRODUCING"], env)
    check("g1_gate_blocks_without_file", r.returncode != 0, "expected non-zero, got 0")

    critiques = folder / "critiques"
    critiques.mkdir(parents=True, exist_ok=True)
    (critiques / "G1-script.md").write_text("some notes\nVERDICT: SHIP\n", encoding="utf-8")
    r = run("pipeline.py", ["stage", "1", "PRODUCING"], env)
    check("g1_gate_passes_with_ship_verdict", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["stage", "1", "PUBLISHED"], env)
    check("illegal_transition_rejected", r.returncode != 0, "expected non-zero, got 0")

    r = run("pipeline.py", ["stage", "1", "CUT"], env)
    check("legal_producing_to_cut", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["stage", "1", "READY"], env)
    check("g2_gate_blocks_without_file", r.returncode != 0, "expected non-zero, got 0")

    (critiques / "G2-cut-r1.md").write_text("VERDICT: SHIP\n", encoding="utf-8")
    r = run("pipeline.py", ["stage", "1", "READY"], env)
    check("g2_gate_passes_with_ship_verdict", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["stage", "1", "PUBLISHED"], env)
    check("g3_gate_blocks_without_file", r.returncode != 0, "expected non-zero, got 0")
    check("g3_gate_error_names_brand_review", "G3 gate not met" in r.stderr, r.stderr)

    (critiques / "G3-brand.md").write_text("brand notes\nVERDICT: HOLD\n", encoding="utf-8")
    r = run("pipeline.py", ["stage", "1", "PUBLISHED"], env)
    check("g3_gate_blocks_on_hold", r.returncode != 0, "expected non-zero, got 0")

    (critiques / "G3-brand-r2.md").write_text(
        "override recorded\nVERDICT: ADVANCE-WITH-NOTES\n", encoding="utf-8")
    r = run("pipeline.py", ["stage", "1", "PUBLISHED"], env)
    check("ship_gate_blocks_without_approval", r.returncode != 0, "expected non-zero, got 0")
    check("ship_gate_error_names_approval", "SHIP gate not met" in r.stderr, r.stderr)

    r = run("pipeline.py", ["stage", "1", "READY", "--approved-by-sparsh"], env)
    check("same_stage_touch_sets_approval", r.returncode == 0, r.stderr)
    item, _ = read_item(tmp, 1)
    check("approved_by_sparsh_is_set", bool(item.get("approved_by_sparsh")))

    video_path = Path(tmp) / "dummy_export.mp4"
    video_path.write_bytes(b"not a real video, just bytes for hashing\x00\x01\x02")

    r = run("pipeline.py", ["publish", "1", "--url", "https://instagram.com/p/test1",
                             "--video", str(video_path)], env)
    check("publish_succeeds", r.returncode == 0, r.stderr)
    item, _ = read_item(tmp, 1)
    check("publish_sets_stage_published", item.get("stage") == "PUBLISHED", str(item.get("stage")))
    check("publish_records_url", "https://instagram.com/p/test1" in (item.get("published") or {}))
    hashes_path = Path(tmp) / "ops" / "pipeline" / ".published_hashes.json"
    check("publish_writes_hash_ledger", hashes_path.is_file())

    r = run("pipeline.py", ["new", "Second Item", "--pillar", "WORKHORSE",
                             "--platform", "ig"], env)
    check("new_second_item", r.returncode == 0, r.stderr)
    advance_to_ready(env, tmp, 2)

    r = run("pipeline.py", ["publish", "2", "--url", "https://instagram.com/p/test2",
                             "--video", str(video_path)], env)
    check("repost_guard_blocks_duplicate_video", r.returncode != 0,
          "expected non-zero (repost guard), got 0")

    r = run("pipeline.py", ["new", "Third Item", "--pillar", "FILLER", "--platform", "yt"], env)
    check("new_third_item", r.returncode == 0, r.stderr)
    r = run("pipeline.py", ["kill", "3", "--reason", "test kill reason"], env)
    check("kill_succeeds", r.returncode == 0, r.stderr)
    item, _ = read_item(tmp, 3)
    check("kill_sets_stage", item.get("stage") == "KILLED")
    check("kill_sets_reason", item.get("kill_reason") == "test kill reason")

    r = run("pipeline.py", ["new", "Fourth Item", "--pillar", "WORKHORSE",
                             "--platform", "ig"], env)
    check("new_fourth_item", r.returncode == 0, r.stderr)
    r = run("pipeline.py", ["stage", "4", "IDEA", "--next-action-owner", "sparsh"], env)
    check("touch_sets_owner_sparsh", r.returncode == 0, r.stderr)

    r = run("pipeline.py", ["blocked"], env)
    check("blocked_runs_exit0", r.returncode == 0, r.stderr)
    check("blocked_lists_item4", "004" in r.stdout, r.stdout)
    check("blocked_flags_sparsh", "BLOCKED-ON-SPARSH" in r.stdout, r.stdout)

    r = run("pipeline.py", ["board"], env)
    check("board_runs_exit0", r.returncode == 0, r.stderr)
    check("board_lists_open_items", "001" in r.stdout and "004" in r.stdout, r.stdout)
    check("board_excludes_killed", "003" not in r.stdout, r.stdout)

    r = run("pipeline.py", ["validate"], env)
    check("validate_clean_state_exit0", r.returncode == 0, r.stderr + r.stdout)

    item4, folder4 = read_item(tmp, 4)
    item4["pillar"] = "NOT-A-REAL-PILLAR"
    with (folder4 / "item.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(item4, fh, sort_keys=False, allow_unicode=True)
    r = run("pipeline.py", ["validate"], env)
    check("validate_catches_injected_violation", r.returncode != 0, "expected non-zero, got 0")
    check("validate_violation_mentions_pillar", "pillar" in r.stdout, r.stdout)


def test_metrics(env: dict, tmp: str) -> None:
    print("\n-- metrics.py --")

    r = run("metrics.py", ["likerate", "--views", "10000", "--likes", "300", "--json"], env)
    check("likerate_runs_exit0", r.returncode == 0, r.stderr)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("likerate_value_correct", abs(out["lr"] - 3.0) < 1e-6, str(out))
        check("likerate_in_band", "IN-BAND" in out["verdict"], out["verdict"])

    quadrant_cases = [
        ("hook_discovery", 400, 20, "HOOK/DISCOVERY FAILURE"),
        ("craft_failure", 400, 4, "CRAFT FAILURE"),
        ("boost_suspect", 3000, 15, "BOOST-SUSPECT"),
        ("healthy", 1200, 60, "HEALTHY"),
        ("in_band_else", 700, 35, "IN-BAND"),
    ]
    for name, views, likes, expected_prefix in quadrant_cases:
        r = run("metrics.py", ["decompose", "--views", str(views), "--likes", str(likes),
                                "--median-views", "1000", "--median-lr", "2.0", "--json"], env)
        ok = r.returncode == 0
        if ok:
            out = json.loads(r.stdout)
            ok = out["quadrant"].startswith(expected_prefix)
        check(f"decompose_{name}", ok, r.stderr or (r.stdout if r.returncode == 0 else ""))

    r = run("metrics.py", ["funnel", "--comments", "60", "--likes", "100", "--json"], env)
    check("funnel_working", r.returncode == 0 and json.loads(r.stdout)["verdict"] == "WORKING", r.stdout)
    r = run("metrics.py", ["funnel", "--comments", "25", "--likes", "100", "--json"], env)
    check("funnel_middling", r.returncode == 0 and json.loads(r.stdout)["verdict"] == "MIDDLING", r.stdout)
    r = run("metrics.py", ["funnel", "--comments", "10", "--likes", "100", "--json"], env)
    check("funnel_failing", r.returncode == 0 and json.loads(r.stdout)["verdict"] == "FAILING", r.stdout)

    csv_path = Path(tmp) / "posts.csv"
    fieldnames = ["date", "platform", "url", "pillar", "views", "likes", "comments",
                  "shares", "saves", "funnel", "followers_at_post"]
    rows = [
        {"date": "2026-07-01", "platform": "ig", "url": "https://ig/1", "pillar": "HERO",
         "views": 20000, "likes": 800, "comments": 100, "shares": 50, "saves": 40,
         "funnel": 0, "followers_at_post": 5000},
        {"date": "2026-07-05", "platform": "ig", "url": "https://ig/2", "pillar": "WORKHORSE",
         "views": 8000, "likes": 320, "comments": 200, "shares": 10, "saves": 15,
         "funnel": 1, "followers_at_post": 5100},
        {"date": "2026-07-10", "platform": "ig", "url": "https://ig/3", "pillar": "FILLER",
         "views": 4000, "likes": 160, "comments": 30, "shares": 5, "saves": 5,
         "funnel": 0, "followers_at_post": 5200},
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    r = run("metrics.py", ["efficiency", "--csv", str(csv_path), "--followers", "5000", "--json"], env)
    check("efficiency_runs_exit0", r.returncode == 0, r.stderr)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("efficiency_median_views_correct", out["median_views"] == 8000, str(out))

    r = run("metrics.py", ["report", "--csv", str(csv_path), "--followers", "5000", "--json"], env)
    check("report_runs_exit0", r.returncode == 0, r.stderr)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("report_has_3_rows", len(out["rows"]) == 3, str(len(out["rows"])))
        check("report_has_summary", "summary" in out and "early_warning_triad" in out["summary"])


def test_verify_stats(env: dict) -> None:
    print("\n-- verify_stats.py --")
    r = run("verify_stats.py", ["--url", "https://www.instagram.com/reel/does-not-matter/"], env)
    check("verify_stats_missing_ytdlp_exit2", r.returncode == 2, f"exit={r.returncode} stderr={r.stderr}")
    check("verify_stats_install_hint", "pip install yt-dlp" in r.stderr, r.stderr)


def test_hygiene_check(env: dict, tmp: str) -> None:
    print("\n-- hygiene_check.py --")
    dummy = Path(tmp) / "does_not_need_to_exist.mp4"
    r = run("hygiene_check.py", [str(dummy)], env)
    check("hygiene_check_missing_ffmpeg_exit2", r.returncode == 2, f"exit={r.returncode} stderr={r.stderr}")
    check("hygiene_check_install_hint", "winget install Gyan.FFmpeg" in r.stderr, r.stderr)


def test_calendar(env: dict) -> None:
    print("\n-- calendar.py --")
    r = run("calendar.py", ["--weeks", "2"], env)
    check("calendar_runs_with_empty_roadmap_exit0", r.returncode == 0, r.stderr)
    check("calendar_output_has_week_grid", "Week of" in r.stdout, r.stdout)


def test_brandkit(env_repo: dict, tmp: str) -> None:
    """brandkit_check.py is read-only (validate/caption never write anything), so unlike every
    tool above this one runs against env_repo -- TANGENT_ROOT pointed at the REAL repo root --
    so it validates the actual shipped brand/kit.yaml rather than a sandbox with no kit at all.
    Caption fixture files still live under the tmp sandbox; only the kit.yaml lookup uses the
    real root."""
    print("\n-- brandkit_check.py --")

    r = run("brandkit_check.py", ["validate", "--json"], env_repo)
    check("brandkit_validate_real_kit_exit0", r.returncode == 0, r.stderr + r.stdout)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("brandkit_validate_ok_true", out.get("ok") is True, r.stdout)
        check("brandkit_validate_no_errors", out.get("errors") == [], r.stdout)

    clean_path = Path(tmp) / "caption_clean.txt"
    clean_path.write_text(
        "Claude drove every adjustment here -- I set the brief, the critic rejected two passes "
        "before this one shipped. #process #AIart",
        encoding="utf-8",
    )
    banned_path = Path(tmp) / "caption_banned.txt"
    banned_path.write_text(
        "This edit is INSANE -- Claude drove every adjustment here, the critic rejected two "
        "passes. #process",
        encoding="utf-8",
    )
    nodisclosure_path = Path(tmp) / "caption_nodisclosure.txt"
    nodisclosure_path.write_text("Here's the edit process today. #process", encoding="utf-8")

    r = run("brandkit_check.py", ["caption", str(clean_path), "--platform", "ig", "--json"], env_repo)
    check("brandkit_caption_clean_exit0", r.returncode == 0, r.stderr + r.stdout)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("brandkit_caption_clean_ok", out.get("ok") is True, r.stdout)
        check("brandkit_caption_clean_no_banned_hits", out.get("banned_word_hits") == [], r.stdout)
        check("brandkit_caption_clean_disclosure_present", out["disclosure"]["present"] is True, r.stdout)

    r = run("brandkit_check.py", ["caption", str(banned_path), "--platform", "ig", "--json"], env_repo)
    check("brandkit_caption_banned_exit1", r.returncode == 1, r.stderr + r.stdout)
    if r.returncode == 1:
        out = json.loads(r.stdout)
        check("brandkit_caption_banned_hit_found",
              any(h["phrase"] == "insane" for h in out.get("banned_word_hits", [])), r.stdout)
        check("brandkit_caption_banned_ok_false", out.get("ok") is False, r.stdout)

    r = run("brandkit_check.py", ["caption", str(nodisclosure_path), "--platform", "ig", "--json"], env_repo)
    check("brandkit_caption_nodisclosure_exit1", r.returncode == 1, r.stderr + r.stdout)
    if r.returncode == 1:
        out = json.loads(r.stdout)
        check("brandkit_caption_nodisclosure_missing_flagged",
              out["disclosure"]["present"] is False and out["disclosure"]["missing_keywords"], r.stdout)
        check("brandkit_caption_nodisclosure_no_banned_hits", out.get("banned_word_hits") == [], r.stdout)

    # stdin path (no FILE argument) -- clean text piped in, should also pass.
    r = run("brandkit_check.py", ["caption", "--platform", "ig", "--json"], env_repo,
            input_text="Claude drove every adjustment here, the critic rejected two passes.")
    check("brandkit_caption_stdin_exit0", r.returncode == 0, r.stderr + r.stdout)

    dummy_video = Path(tmp) / "dummy_export_for_brandkit.mp4"
    dummy_video.write_bytes(b"not a real video")
    r = run("brandkit_check.py", ["export", str(dummy_video), "--platform", "ig", "--json"], env_repo)
    check("brandkit_export_skeleton_exit0", r.returncode == 0, r.stderr + r.stdout)
    if r.returncode == 0:
        out = json.loads(r.stdout)
        check("brandkit_export_skeleton_honest_note",
              "Phase R2" in out.get("note", ""), r.stdout)
        check("brandkit_export_skeleton_kit_validate_present", "kit_validate" in out, r.stdout)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="tangent_smoke_") as tmp:
        env = os.environ.copy()
        env["TANGENT_ROOT"] = tmp
        env["PYTHONIOENCODING"] = "utf-8"

        env_repo = os.environ.copy()
        env_repo["TANGENT_ROOT"] = str(TOOLS_DIR.parent)
        env_repo["PYTHONIOENCODING"] = "utf-8"

        test_pipeline(env, tmp)
        test_metrics(env, tmp)
        test_verify_stats(env)
        test_hygiene_check(env, tmp)
        test_calendar(env)
        test_brandkit(env_repo, tmp)

    passed = sum(1 for _, status, _ in RESULTS if status == "PASS")
    failed = [r for r in RESULTS if r[1] == "FAIL"]

    print(f"\n{passed}/{len(RESULTS)} checks passed")
    if failed:
        print("\nFAILURES:")
        for name, _, detail in failed:
            print(f"  - {name}: {detail}")
        return 1

    print("ALL SMOKE TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
