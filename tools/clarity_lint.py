#!/usr/bin/env python
"""clarity_lint.py: deterministic plain-language lint for social copy (the Clarity Doctrine,
`knowledge/craft/clarity.md`). Same conventions as the sibling tools (argparse, --json,
TANGENT_ROOT-aware, exit codes below).

What it is for
--------------
Agents kept writing stylish lines that readers had to decode ("One sky, two ways to count it.",
"Checked against the sky's reference books.", "427 ways to ask the wrong thing. Tested.").
This tool flags the MECHANICAL half of that failure: long slides, long sentences, agentless
fragments, aphorism templates, AI-tell words, hype words, jargon left undefined, URLs in
captions. It is a nudge, not a judge. Only hard rules FAIL: walls of text (over 50 words a
slide), empty slides, brand-banned hype words, em dashes, URLs in captions and more than 5
hashtags. Everything else is a WARN for the writer to weigh. Meaning is checked by a light
cold read (`/cold-read`).

Input format (the copy file, `templates/carousel.md` and `templates/script.md` use it)
----------------------------------------------------------------------------------
    ### Slide 1            (or "### Beat 1", "### Frame 1", "### Card 1")
    H: the headline / main on-screen line
    B: optional body text (carousels)
    S: spoken words (reels/shorts voiceover or talking head)
    V: what the picture shows (NOT linted for words; it is a production note)

    ## Caption
    free text until the next "## " heading

Lines without a prefix inside a slide block are ignored, so notes can sit next to the copy.
A line ending in `<!-- lint-ok: reason -->` is exempt from the FAIL-level pattern checks
(the reason is printed, so exceptions stay visible to the critic).

Subcommands
-----------
    check FILE [--format carousel|reel|auto] [--json]

Exit codes
----------
    0  no FAIL findings (WARNs may exist; read them)
    1  at least one FAIL finding
    2  input problem (file missing, no slides found)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import _common as c

try:
    import yaml
except ImportError:  # pragma: no cover - yaml is in requirements.txt
    yaml = None

# ---------------------------------------------------------------------------
# Defaults (brand/kit.yaml `verbal.clarity` overrides / extends these)
# ---------------------------------------------------------------------------

LIMITS = {
    "carousel": {
        "headline_warn": 12, "headline_fail": 16,
        "slide_words_warn": 35, "slide_words_fail": 50,
        "sentence_warn": 16, "sentence_fail": 22,
        "slides_min": 3, "slides_max": 10,
    },
    "reel": {
        "headline_warn": 8, "headline_fail": 12,      # on-screen text must read in ~1s
        "slide_words_warn": 12, "slide_words_fail": 20,
        "sentence_warn": 14, "sentence_fail": 20,      # spoken: breath-length sentences
        "slides_min": 2, "slides_max": 30,
    },
}
GRADE_WARN = 8.0
GRADE_FAIL = 10.0
CAPTION_FIRST_LINE_MAX = 125
CAPTION_HASHTAGS_MAX = 5

DEFAULT_AI_TELL_WORDS = [
    "delve", "tapestry", "testament", "journey", "realm", "vibrant", "pivotal", "seamless",
    "seamlessly", "robust", "elevate", "unlock", "unleash", "leverage", "foster", "showcase",
    "curated", "immersive", "stunning", "boasts", "embark", "truly", "incredibly", "harness",
    "landscape", "paradigm", "synergy", "revolutionize", "revolutionise", "supercharge",
]

DEFAULT_JARGON = [
    "deterministic", "llm", "llms", "inference", "pipeline", "ephemeris", "arcsecond",
    "arcseconds", "red-team", "red team", "token", "tokens", "context window", "api",
    "agentic", "latency", "embedding", "embeddings", "fine-tune", "fine-tuned", "rag",
    "hallucinate", "hallucination", "hallucinations", "sidereal", "tropical zodiac",
    "ayanamsa", "parameters", "benchmark", "benchmarks", "guardrail", "guardrails",
    "system prompt", "repo", "commit", "deploy", "backend", "frontend", "pwa", "model",
]

# A term counts as "defined" if the same slide also contains one of these cues.
DEFINITION_CUES = (" means ", " is a ", " is an ", " are ", "(", " = ", " called ", " i.e.")

# FAIL-level stylistic templates: lines that sound like insight but hide the meaning.
# Each pattern carries its level. Only hard brand rules FAIL; style smells WARN, so the lint
# nudges the writer instead of blocking (kept deliberately light, per Sparsh 2026-11-15).
STYLE_PATTERNS = [
    (re.compile(r"\bone\s+\w+(?:'s)?,\s+(?:two|three|four|many)\s+\w+", re.I),
     "aphorism template 'One X, two Y': say what the two things are, literally", "WARN"),
    (re.compile(r"\b(?:it'?s|this is|that'?s)\s+not\s+(?:just\s+)?[^.,;]+[,;]\s*(?:it'?s|but)\b", re.I),
     "'It's not X, it's Y' contrast template: state the plain claim instead", "WARN"),
    (re.compile(r"\bnot\s+just\s+[^.,;]+,\s*but\b", re.I),
     "'Not just X, but Y' template: state the plain claim instead", "WARN"),
    (re.compile(r"\u2014"), "em dash: use a full stop, comma or colon", "FAIL"),
    (re.compile(r"\b(?:the|a)\s+\w+(?:'s)?\s+(?:reference books|north star|secret sauce|holy grail|"
                r"magic|dna|heartbeat|soul)\b", re.I),
     "metaphor standing in for a plain noun: name the real thing", "WARN"),
    (re.compile(r"\b(?:here'?s the thing|let that sink in|read that again|and that changes everything)\b", re.I),
     "filler drumroll phrase: cut it and say the point", "WARN"),
]

URL_RE = re.compile(r"(?:https?://|www\.)\S+|\b[\w-]+\.(?:com|ai|io|in|org|net|co|app|dev)/\S*", re.I)
HASHTAG_RE = re.compile(r"(?<!\w)#\w+")
SLIDE_HEAD_RE = re.compile(r"^###\s+(slide|beat|frame|card)\s*(\d+)?(.*)$", re.I)
SECTION_RE = re.compile(r"^##\s+(?!#)(.*)$")
LINT_OK_RE = re.compile(r"<!--\s*lint-ok:\s*(.*?)\s*-->", re.I)
PREFIX_RE = re.compile(r"^\s*(H|B|S|V)\s*:\s*(.*)$")

# ---------------------------------------------------------------------------
# kit loading (optional; the lint runs on defaults if the kit has no clarity block)
# ---------------------------------------------------------------------------


def load_lists(root: Path) -> dict:
    lists = {"ai_tell": list(DEFAULT_AI_TELL_WORDS), "jargon": list(DEFAULT_JARGON), "banned": []}
    kit = root / "brand" / "kit.yaml"
    if yaml is None or not kit.is_file():
        return lists
    try:
        data = yaml.safe_load(kit.read_text(encoding="utf-8")) or {}
    except Exception:  # a broken kit is brandkit_check's job to report, not ours
        return lists
    verbal = data.get("verbal") or {}
    bw = verbal.get("banned_words") or {}
    lists["banned"] = [w for w in (bw.get("starter_list") or []) + (bw.get("kit_additions") or []) if w]
    clar = verbal.get("clarity") or {}
    for key, kit_key in (("ai_tell", "ai_tell_words"), ("jargon", "jargon_watchlist")):
        extra = clar.get(kit_key) or []
        lists[key] = sorted(set(lists[key]) | {str(w).lower() for w in extra if w})
    return lists


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------


def parse_copy(text: str) -> dict:
    slides: list[dict] = []
    caption_lines: list[str] = []
    current: dict | None = None
    in_caption = False
    for raw in text.splitlines():
        line = raw.rstrip()
        m_slide = SLIDE_HEAD_RE.match(line.strip())
        if m_slide:
            in_caption = False
            current = {"label": line.strip("# ").strip(), "kind": m_slide.group(1).lower(),
                       "H": [], "B": [], "S": [], "V": [], "ok": []}
            slides.append(current)
            continue
        m_sec = SECTION_RE.match(line.strip())
        if m_sec:
            current = None
            in_caption = m_sec.group(1).strip().lower().startswith("caption")
            continue
        if in_caption:
            caption_lines.append(line)
            continue
        if current is None:
            continue
        m_pre = PREFIX_RE.match(line)
        if not m_pre:
            continue
        key, value = m_pre.group(1), m_pre.group(2)
        ok = LINT_OK_RE.search(value)
        if ok:
            current["ok"].append(ok.group(1))
            value = LINT_OK_RE.sub("", value).strip()
            current.setdefault("ok_lines", []).append(value)
        if value:
            current[key].append(value)
    # trim a fenced/blank caption tail
    caption = "\n".join(caption_lines).strip()
    caption = re.sub(r"^```\w*\n|\n```$", "", caption).strip()
    caption = "\n".join(l[2:] if l.startswith("> ") else ("" if l == ">" else l) for l in caption.splitlines())
    return {"slides": slides, "caption": caption.strip()}


# ---------------------------------------------------------------------------
# text measures
# ---------------------------------------------------------------------------

WORD_RE = re.compile(r"[A-Za-z0-9\u0900-\u097F][A-Za-z0-9'\u2019\u0900-\u097F%.,-]*")


def words(text: str) -> list[str]:
    return [w.strip(".,") for w in WORD_RE.findall(text) if w.strip(".,")]


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|\n+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def syllables(word: str) -> int:
    w = word.lower()
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 1  # numerals and symbols read as roughly one beat each
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")):
        n -= 1
    return max(1, n)


def fk_grade(text: str) -> float | None:
    ws = words(text)
    ss = sentences(text)
    if len(ws) < 20 or not ss:
        return None  # too little text for the formula to mean anything
    syl = sum(syllables(w) for w in ws)
    return round(0.39 * (len(ws) / len(ss)) + 11.8 * (syl / len(ws)) - 15.59, 1)


def contains_term(text_lower: str, term: str) -> bool:
    return re.search(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", text_lower) is not None


# ---------------------------------------------------------------------------
# lint
# ---------------------------------------------------------------------------


def lint(parsed: dict, fmt: str, lists: dict) -> dict:
    findings: list[dict] = []
    lim = LIMITS[fmt]

    def add(level: str, where: str, msg: str):
        findings.append({"level": level, "where": where, "message": msg})

    slides = parsed["slides"]
    n = len(slides)
    if n < lim["slides_min"] or n > lim["slides_max"]:
        add("WARN", "post", f"{n} slides/beats; expected {lim['slides_min']}-{lim['slides_max']} "
                            f"(carousels: as many as ONE idea needs, usually 4-7; never pad)")

    all_copy: list[str] = []
    headline_read: list[str] = []
    for s in slides:
        where = s["label"]
        head = " ".join(s["H"])
        body = " ".join(s["B"])
        spoken = " ".join(s["S"])
        headline_read.append(head or "(no headline)")
        on_screen = " ".join(x for x in (head, body) if x)
        slide_text = " ".join(x for x in (head, body, spoken) if x)
        all_copy.append(slide_text)
        exempt = set(s.get("ok_lines", []))

        if not head and not spoken:
            add("FAIL", where, "no H: (headline/on-screen line) and no S: (spoken line); every "
                                "slide/beat must say something a stranger can read")
        hw = len(words(head))
        if hw > lim["headline_fail"]:
            add("WARN", where, f"headline is {hw} words: long for a glance (aim <= {lim['headline_warn']})")
        elif hw > lim["headline_warn"]:
            add("WARN", where, f"headline is {hw} words (aim <= {lim['headline_warn']})")
        sw = len(words(on_screen))
        if sw > lim["slide_words_fail"]:
            add("FAIL", where, f"{sw} on-screen words (max {lim['slide_words_fail']}; aim <= {lim['slide_words_warn']})")
        elif sw > lim["slide_words_warn"]:
            add("WARN", where, f"{sw} on-screen words (aim <= {lim['slide_words_warn']})")

        for line in s["H"] + s["B"] + s["S"]:
            line_exempt = line in exempt
            for sent in sentences(line):
                n_w = len(words(sent))
                if n_w > lim["sentence_warn"]:
                    tip = " (consider splitting it)" if n_w > lim["sentence_fail"] else ""
                    add("WARN", where, f"sentence of {n_w} words: \"{sent[:70]}...\"{tip}")
                stripped = sent.strip()
                if (n_w == 1 and stripped.endswith(".") and not re.match(r"^[\d.,%$₹]+\.?$", stripped)
                        and not line_exempt):
                    add("WARN", where, f"one-word fragment \"{stripped}\": who did what? usually clearer as a full sentence")
            if not line_exempt:
                for pat, why, level in STYLE_PATTERNS:
                    if pat.search(line):
                        add(level, where, f"{why}: \"{line[:80]}\"")
            low = " " + line.lower() + " "
            for w in lists["ai_tell"]:
                if contains_term(low, w):
                    add("WARN", where, f"AI-tell word \"{w}\": use the plain word")
            for w in lists["banned"]:
                if contains_term(low, str(w).lower()):
                    add("FAIL", where, f"banned hype word \"{w}\" (brand/kit.yaml)")

        slide_low = " " + slide_text.lower() + " "
        defined = any(cue in slide_low for cue in DEFINITION_CUES)
        for term in lists["jargon"]:
            if contains_term(slide_low, term):
                if defined:
                    add("WARN", where, f"jargon \"{term}\" (a definition cue is present; the cold "
                                       f"read decides if a stranger gets it)")
                else:
                    add("WARN", where, f"jargon \"{term}\" with no definition on the same slide: "
                                       f"define it in plain words here, or cut it (general audience)")
        for s_ok in s["ok"]:
            add("INFO", where, f"lint-ok exemption: {s_ok}")

    grade = fk_grade(" ".join(all_copy))
    if grade is not None:
        if grade > GRADE_WARN:
            add("WARN", "post", f"reading grade {grade} (target 6-8; India-first posts 5-7)")

    cap = parsed["caption"]
    if cap:
        first = next((l for l in cap.splitlines() if l.strip()), "")
        if len(first) > CAPTION_FIRST_LINE_MAX:
            add("WARN", "caption", f"first line is {len(first)} chars; only ~{CAPTION_FIRST_LINE_MAX} "
                                   f"show before 'more', so put the one-line message there")
        if URL_RE.search(cap):
            add("FAIL", "caption", "URL in an Instagram caption: links are not clickable there. Say "
                                   "'link in bio' (or use the Story link sticker)")
        tags = HASHTAG_RE.findall(cap)
        if len(tags) > CAPTION_HASHTAGS_MAX:
            add("FAIL", "caption", f"{len(tags)} hashtags (max {CAPTION_HASHTAGS_MAX})")
        for pat, why, level in STYLE_PATTERNS:
            if pat.search(cap):
                add(level, "caption", f"{why}")
        low = " " + cap.lower() + " "
        for w in lists["ai_tell"]:
            if contains_term(low, w):
                add("WARN", "caption", f"AI-tell word \"{w}\"")
    else:
        add("WARN", "caption", "no '## Caption' section found (captions are linted too)")

    fails = sum(1 for f in findings if f["level"] == "FAIL")
    warns = sum(1 for f in findings if f["level"] == "WARN")
    return {"format": fmt, "slides": n, "reading_grade": grade, "fails": fails, "warns": warns,
            "headline_only_read": headline_read, "findings": findings}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def cmd_check(args) -> int:
    path = Path(args.file)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    parsed = parse_copy(path.read_text(encoding="utf-8", errors="replace"))
    if not parsed["slides"]:
        print("ERROR: no '### Slide N' / '### Beat N' blocks with H:/B:/S: lines found "
              "(see templates/carousel.md for the copy format)", file=sys.stderr)
        return 2
    fmt = args.format
    if fmt == "auto":
        kinds = {s["kind"] for s in parsed["slides"]}
        fmt = "reel" if kinds & {"beat", "frame"} else "carousel"
    result = lint(parsed, fmt, load_lists(c.get_repo_root()))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"clarity_lint: {path.name} ({result['format']}, {result['slides']} slides/beats, "
              f"reading grade {result['reading_grade']})")
        print("\nHEADLINE-ONLY READ (do these lines alone tell the story?):")
        for i, h in enumerate(result["headline_only_read"], 1):
            print(f"  {i}. {h}")
        print()
        for f in result["findings"]:
            print(f"[{f['level']}] {f['where']}: {f['message']}")
        print(f"\n{result['fails']} FAIL, {result['warns']} WARN. "
              + ("PASS (mechanical checks only; now run /cold-read)" if result["fails"] == 0
                 else "FAIL: fix the FAIL lines, then re-run"))
    return 1 if result["fails"] else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Plain-language lint for social copy (Clarity Doctrine).")
    sub = p.add_subparsers(dest="cmd", required=True)
    pc = sub.add_parser("check", help="lint a copy file (carousel.md / script.md format)")
    pc.add_argument("file")
    pc.add_argument("--format", choices=("auto", "carousel", "reel"), default="auto")
    pc.add_argument("--json", action="store_true")
    pc.set_defaults(func=cmd_check)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
