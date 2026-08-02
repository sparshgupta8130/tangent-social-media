# tools/ — Tangent deterministic tools

Everything here is a plain Python 3.13 CLI: stdlib + PyYAML, ffmpeg/yt-dlp driven
via `subprocess`. Anything that must be *exact* (state transitions, metrics math,
file hygiene, stat verification) lives here rather than in a model's head — see
`SYSTEM_DESIGN.md` §7.

All tools are Windows-path-safe (pathlib throughout), read/write UTF-8
explicitly, support `--help`, and exit non-zero on failure. `--json` is
available where noted for machine-parseable output.

## Install

```
pip install -r tools/requirements.txt
```

That gets you PyYAML (required by every tool) and yt-dlp (only used by
`verify_stats.py`). ffmpeg/ffprobe are external binaries, not pip packages:

```
winget install Gyan.FFmpeg
```

Every tool that needs a missing dependency detects it and prints the relevant
install hint instead of crashing (`verify_stats.py` -> exit 2 + `pip install
yt-dlp`; `hygiene_check.py` -> exit 2 + the winget line above).

## TANGENT_ROOT

Every tool resolves the repo root as `$TANGENT_ROOT` if that environment
variable is set, else the parent directory of `tools/` (i.e. the real repo
root in normal use). This is what lets `tools/tests/smoke.py` run entirely
against a temp directory with no risk to the real `ops/` tree.

## Tool index

| Tool | Purpose |
|---|---|
| `pipeline.py` | Content-pipeline state machine: `new`, `derive`, `stage`, `board`, `blocked`, `kill`, `publish`, `validate`. |
| `metrics.py` | The measurement constitution as code: `likerate`, `decompose`, `efficiency`, `funnel`, `report`. |
| `ingest_stats.py` | Maps an IG/YT analytics export into `posts.csv` rows: `inspect`, `ig`, `yt`. **Format assumptions unvalidated against real exports** — see below. |
| `verify_stats.py` | Second-source stat verification against a public post URL via yt-dlp. |
| `hygiene_check.py` | Pre-publish export hygiene via ffprobe/ffmpeg (resolution, aspect, duration, codecs, black borders, repost guard). |
| `calendar.py` | Renders a markdown week-grid from `ops/calendar/ROADMAP.md` + live pipeline state; flags cadence and HERO-drought. |
| `brandkit_check.py` | Deterministic `brand/kit.yaml` validator + caption compliance (banned words, disclosure, footer). `export` is a documented skeleton — no visual checks yet. |
| `_common.py` | Shared helpers (repo root resolution, item.yaml I/O, hashing, date parsing). Not a CLI. |
| `tests/smoke.py` | No-network smoke test covering every tool above. |

---

## pipeline.py

One folder per content item: `ops/pipeline/NNN-slug/` (`NNN` = zero-padded
3-digit sequence id). `pipeline.py` is the *only* thing allowed to change an
item's stage.

### item.yaml schema

| Field | Type | Notes |
|---|---|---|
| `id` | int | matches the folder's `NNN` |
| `slug` | str | matches the folder's `-slug` suffix |
| `title` | str | |
| `pillar` | str | one of `HERO`, `WORKHORSE`, `FILLER` |
| `vertical` | str | one of `reels`, `longform`, `podcast`, `music`, `app`, `image`, `newsletter` — selects the craft pack (default `reels`) |
| `platforms` | list[str] | any of `ig`, `yt`, `yt-long` |
| `parent_id` | int\|null | set by `derive`; points at the item this one was fanned out from (Repurposing Engine — see below). `null` for everything created by `new`. |
| `stage` | str | `IDEA`\|`BRIEFED`\|`SCRIPTED`\|`PRODUCING`\|`CUT`\|`READY`\|`PUBLISHED`\|`POSTMORTEM`\|`CLOSED`\|`KILLED` |
| `created` | str | ISO date |
| `due` | str\|null | ISO date |
| `next_action` | str | |
| `next_action_owner` | str | one of `creative-director`, `trend-scout`, `story-lead`, `producer`, `critic`, `analyst`, `planner`, `brand-director`, `growth-lead`, `audience-advocate`, `revenue-lead`, `showrunner`, `sparsh` |
| `plane_issue` | str\|null | |
| `approved_by_sparsh` | str\|null | ISO date; the SHIP gate |
| `published` | dict | `url -> ISO date`, one entry per platform post |
| `kill_reason` | str\|null | required (non-empty) when `stage == KILLED` |

### Stage transitions

Legal forward sequence (one step at a time, no skipping):
`IDEA -> BRIEFED -> SCRIPTED -> PRODUCING -> CUT -> READY -> PUBLISHED -> POSTMORTEM -> CLOSED`.
`KILLED` is reachable from any non-terminal stage, but **only** via
`pipeline.py kill` (never via a bare `stage` call) so a reason is always
recorded.

Gated edges:
- `SCRIPTED -> PRODUCING` requires `critiques/G1-script.md` to exist with a
  line reading exactly `VERDICT: SHIP` — **unless** the item has `parent_id`
  set (a derivative, created via `derive`), in which case a `derivative-spec.md`
  file present in the item folder (exact filename) is accepted as an
  alternate unlock; see "Derivative gate policy" below. A non-derivative item
  always needs the full G1 SHIP verdict.
- `CUT -> READY` requires a `critiques/G2-cut*.md` file (glob, so
  `G2-cut.md`, `G2-cut-r2.md`, ... all count) with a `VERDICT: SHIP` line —
  unchanged for derivatives; they face full G2 like any item.
- `READY -> PUBLISHED` requires `approved_by_sparsh` to be set — unchanged
  for derivatives; they face full G3 + SHIP like any item.

Calling `stage NNN STAGE` with `STAGE` equal to the item's *current* stage is
legal and skips the transition check entirely — it's a "touch" used purely to
update fields (see below), most commonly to set `approved_by_sparsh` while an
item sits at READY:

```
python tools/pipeline.py stage 12 READY --approved-by-sparsh
```

(passing no value defaults to today's date; pass an explicit `YYYY-MM-DD` to
backdate/correct it).

### Subcommands

```
pipeline.py new "<title>" --pillar HERO|WORKHORSE|FILLER --platform ig,yt
    [--due YYYY-MM-DD] [--next-action TEXT] [--next-action-owner OWNER] [--plane-issue ID]

pipeline.py derive PARENT_NNN --title "<title>" --platform ig,yt
    [--vertical V] [--pillar P] [--due YYYY-MM-DD] [--next-action-owner OWNER] [--plane-issue ID]

pipeline.py stage NNN STAGE
    [--due YYYY-MM-DD|''] [--next-action TEXT] [--next-action-owner OWNER]
    [--plane-issue ID] [--approved-by-sparsh [YYYY-MM-DD]]

pipeline.py board
pipeline.py blocked
pipeline.py kill NNN --reason "..."
pipeline.py publish NNN --url <url> [--video <path>]
pipeline.py validate
```

`new` copies `templates/brief.md` and `templates/script.md` into the new
item folder if those templates exist at the repo root; otherwise it writes a
one-line stub (`# Brief — <title>` / `# Script — <title>`). `new` always sets
`parent_id: null`.

`derive` (the Repurposing Engine — `SYSTEM_DESIGN_V2_PROPOSAL.md` §4 item 2,
`.claude/skills/repurpose/SKILL.md`) creates a child item exactly like `new`
(same folder/stub behavior), except: `parent_id` is set to `PARENT_NNN`;
`--pillar`/`--vertical` default to the parent's values when omitted;
`next_action` is prefilled `"derivative spec from parent NNN"` with
`next_action_owner` defaulting to `story-lead` (who writes the item's
`derivative-spec.md`). Errors (exit 2) if `PARENT_NNN` doesn't exist; errors
(exit 1) if the parent is `KILLED`, or if the resolved platform/pillar/
vertical is invalid. See "Derivative gate policy" below for what a
derivative unlocks and what it still owes at G2/G3/SHIP.

`board` shows all *open* items (everything except `CLOSED`/`KILLED`), sorted
by stage order then due date, with an `OVERDUE` flag for open items whose due
date has passed. `blocked` shows items where `next_action_owner == sparsh`
(the BLOCKED-ON-SPARSH set) plus any overdue open item.

`publish` requires the item to already be at `READY` with `approved_by_sparsh`
set; it records `published[url] = today`, transitions the item to
`PUBLISHED`, and — if `--video` is given — SHA256-hashes the file into
`ops/pipeline/.published_hashes.json`, erroring out (repost guard) if that
exact file was already published under any item.

`validate` schema-checks every `item.yaml` (field presence/types/enums, id
and slug matching the folder name, dates parsing as ISO, KILLED items having a
kill_reason, PUBLISHED+ items having both `approved_by_sparsh` and a non-empty
`published`, `parent_id` referential integrity — see below) and exits
non-zero listing every violation found.

### Derivative gate policy

Full policy and rationale: `ops/pipeline/README.md` "Derivative gate policy".
Summary: an item with `parent_id` set skips the fresh-G1 requirement on
SCRIPTED→PRODUCING IF a `derivative-spec.md` file (exact filename, item
folder root) is present — its content (source beats used, platform
re-grammar applied per `knowledge/virality/laws.md` law 10, native changes
made) is what justifies not re-running G1 on material whose parent already
cleared that bar. The G1-SHIP path also still works for a derivative if a
fresh critique is actually run. From CUT onward — hygiene, G2 critique, G3
brand gate, SHIP, publish repost guard — a derivative is treated exactly
like any other item; nothing is relaxed past the G1 substitution. `board`
annotates every child with a `^NNN` suffix on its slug (parent's id);
`validate` requires `parent_id` be `null` or reference an existing,
non-self item.

---

## metrics.py

```
metrics.py likerate --views N --likes N [--json]
metrics.py decompose --views N --likes N --median-views N --median-lr X [--json]
metrics.py efficiency --csv posts.csv --followers N [--json]
metrics.py funnel --comments N --likes N [--json]
metrics.py report --csv posts.csv --followers N [--json]
```

### CSV schema (`posts.csv`, used by `efficiency` and `report`)

```
date,platform,url,pillar,views,likes,comments,shares,saves,funnel,followers_at_post
```

- `date`: ISO date. `platform`: free text (e.g. `ig`, `yt`). `pillar`: `HERO`/`WORKHORSE`/`FILLER` (blank tolerated).
- `views,likes,comments,shares,saves,followers_at_post`: integers (blank = 0).
- `funnel`: `0` or `1` — whether this post carries the comment-keyword-DM
  funnel mechanic (used to scope the funnel-ratio account summary to the
  posts where it's actually in play).

### Math

- **likerate**: `LR = likes/views*100`. Verdict vs the 1-10% organic sanity
  band: `IN-BAND` (1-10%), `BELOW-BAND` (<1%), `ABOVE-BAND` (>10%).
- **decompose** (views x LR quadrants, checked in this order):
  1. `LR >= median_lr` and `views < 0.5*median_views` -> `HOOK/DISCOVERY FAILURE`
  2. `LR < median_lr` and `views < 0.5*median_views` -> `CRAFT FAILURE`
  3. `views >= 2*median_views` and `LR < 1.0` -> `BOOST-SUSPECT`
  4. `views >= median_views` and `LR` in `[1,10]` -> `HEALTHY`
  5. else -> `IN-BAND`
- **efficiency**: `median(views)/followers*100`, banded `<5% WARNING`,
  `5-10% OK`, `10-15% HEALTHY`, `15-20% GOOD`, `>=20% EXCELLENT`. (The spec
  names `<5/5-10/10-15/>20`, leaving a 15-20% gap; `GOOD` fills it so every
  real number gets a verdict — see "Resolved ambiguities" below.)
- **funnel**: `ratio = comments/likes`, `>=0.5 WORKING`, `0.2-0.5 MIDDLING`,
  `<0.2 FAILING`.
- **report**: runs likerate/decompose/efficiency/funnel per row (the batch's
  own median views/LR are used as the decompose baseline), plus an
  account-level summary: `n_posts`, `median_views`, `median_likerate_pct`,
  `top_views`, `top_to_median_spread`, `efficiency_pct` (+ verdict),
  `funnel_median_ratio` (+ verdict, computed only over rows with `funnel=1`),
  and the audience-mismatch **early-warning triad**
  (`strategy/STRATEGY.md` §6.6):
    - `efficiency_sliding_under_5pct`: `efficiency_pct < 5`
    - `hits_only_off_pillar`: there is at least one "hit" (`views >=
      2*median_views`) and *none* of the hits are `HERO`/`WORKHORSE`
    - `flat_non_pinned_spread`: `top_to_median_spread < 2.0`
  `strategy_review_triggered` is true when 2 of the 3 are true, per the
  constitution's "two of three -> planner triggers a strategy review" rule.

---

## ingest_stats.py

```
ingest_stats.py inspect <file> [--platform ig|yt]
ingest_stats.py ig <file> --followers N [--funnel-urls url1,url2] [--mapping <json>] [--dry-run]
ingest_stats.py yt <file> --followers N [--mapping <json>] [--dry-run]
```

### Honest constraint — read this first

As of this build, tangentideas.ai has published nothing: **no real Instagram or YouTube
analytics export has ever been seen by this tool.** Every column mapping below is built from
DOCUMENTED formats — secondary export-guide sources plus
`research/briefs/platform_ops_2026-07.md` §4 (tiered `[HIGH]`/`[MED]`/`[LOW]`/`[UNVERIFIED]`) —
encoded as a best-effort hypothesis, not a verified contract. **Format assumptions unvalidated
against real exports — run `ingest_stats.py inspect <file>` on the FIRST real export and
reconcile before trusting batch ingestion.** This caveat is also printed by every subcommand's
`--help` and at the end of every `inspect`/dry-run/append.

### `inspect` — the reconciliation tool

Sniffs a CSV (stdlib `csv`, delimiter auto-detected) or XLSX (`openpyxl`, optional — see
"XLSX support" below) export: prints the format, headers, and up to 3 sample rows, then, for
one platform (`--platform`) or both (default), a line-by-line reconciliation against the
built-in expected mapping:

- `MAP 'Header' -> target_field` — this column will be used.
- `DROP 'Header'` — present in the file but not in the mapping; ignored.
- `MISSING 'Expected Header' -> target_field` — the mapping expects this column and it isn't
  in the file; `ig`/`yt` will refuse to run against this file/mapping combination until
  reconciled (via `--mapping`, see below). This is the first thing to run against any real
  export before trusting `ig`/`yt` on it. Never writes anything.

### `ig` / `yt` — mapping to `posts.csv`

Built-in default mappings (export column name -> `posts.csv` target field):

**`ig`** — Meta Business Suite / IG professional-dashboard Insights → Content → Export Data:

| Export column | Target | Confidence |
|---|---|---|
| `Post Date` | `date` | MED — secondary export guides only |
| `Permalink` | `url` | **Weakest assumption** — no source confirms a literal URL column exists in this export at all; included because a dedup key is a hard requirement |
| `Views` | `views` | MED — reflects the 2026 unified "Views" metric name (`Media impressions`/`Reel plays`/`Reel replays`/`Reel initial plays` deprecated into it), `[ops-brief §4a]` |
| `Likes` | `likes` | MED |
| `Comments` | `comments` | MED |
| `Shares` | `shares` | MED |
| `Saves` | `saves` | MED |

**`yt`** — YouTube Studio content/Advanced-Mode export:

| Export column | Target | Confidence |
|---|---|---|
| `Video ID` | `video_id` (pseudo-field, see below) | HIGH for the URL-derivation *scheme*; MED for the column name |
| `Video publish time` | `date` | MED |
| `Views` | `views` | MED |
| `Likes` | `likes` | MED |
| `Comments added` | `comments` | MED |
| `Shares` | `shares` | MED |

`yt` has no `saves` mapping — YouTube doesn't expose a directly analogous per-video "saves"
metric in the documented export sources; it's left at `0` (tolerated blank, per the CSV
schema above). `video_id` is a pseudo-target: it's turned into a canonical
`https://www.youtube.com/watch?v=<id>` URL rather than copied verbatim — the watch-URL
*scheme* is a stable, well-documented YouTube convention (HIGH confidence) independent of
whatever the export's real "Video ID" column turns out to be named.

`platform`, `pillar`, `funnel`, and `followers_at_post` are never read from the export:
`platform` is fixed by the subcommand; `funnel` is `1` for `ig` rows whose mapped URL is in
`--funnel-urls` (comma-separated, exact match) and always `0` for `yt` (the comment-keyword-DM
mechanic is IG-only — `knowledge/platform/youtube.md` §10); `followers_at_post` is the
`--followers` value applied to every row in the batch. `pillar` gets one best-effort
enrichment: if the mapped URL matches a `published` entry in any `ops/pipeline/*/item.yaml`
(i.e. `pipeline.py publish` recorded it), that item's `pillar` is used; otherwise it's left
blank (tolerated by `metrics.py`).

### `--mapping` — the escape hatch

A `--mapping path/to/mapping.json` file, shaped exactly like the tables above
(`{"Export Column Name": "target_field", ...}`), **replaces the built-in default mapping
entirely** for that run — this is what `inspect` is for: see what a real export's headers
actually are, write the true mapping, and pass it in. Valid targets: `date`, `url`, `views`,
`likes`, `comments`, `shares`, `saves`, plus `video_id`. The mapping must cover at least one
column mapped to `date` and one mapped to `url` (or `video_id`); any mapped column absent from
the file is a hard error naming the missing column(s) and pointing back at `inspect`.

### Dedup / update-in-place (keyed by `url`, in `ops/calendar/posts.csv`)

Analytics accrue — a given post's numbers should only ever go up over time. For each of
`views`/`likes`/`comments`/`shares`/`saves`/`followers_at_post`: a new value higher than what's
stored updates the row; a new value **lower** than what's stored is **never silently written**
— a `WARNING` line names the URL, field, and both numbers, and the higher stored value is kept.
`funnel` is monotonic (`0`→`1` allowed, never silently downgraded back to `0`). A URL not
already in `posts.csv` is appended as a new row. `--dry-run` prints the would-be rows
(`row N: date=... platform=... url=... ...` — one line per row, every `posts.csv` field) and
touches nothing; every real append/update prints:

```
REMINDER: second-source rule: verify via tools/verify_stats.py before these numbers enter a postmortem (QC_PROTOCOL).
```

### XLSX support

CSV needs stdlib only. `.xlsx`/`.xlsm` needs `openpyxl` (not in `tools/requirements.txt` since
it's optional — install with `pip install openpyxl` if/when a real export arrives as a
spreadsheet); if it's missing, `inspect`/`ig`/`yt` exit `2` with that install hint instead of
crashing, checked before the file-existence check (same pattern as `verify_stats.py`/
`hygiene_check.py`'s own optional-dependency checks). Legacy binary `.xls` is not supported —
re-export as `.xlsx` or `.csv`.

### Exit codes

`0` success (a decrease `WARNING` is a printed warning, not a failure). `1` bad input — file
not found/unparseable, mapping references a column missing from the file, an unparseable
date/number. `2` `.xlsx` given and `openpyxl` not installed.

---

## verify_stats.py

```
verify_stats.py --url <post_url> [--views N] [--likes N] [--comments N] [--json]
```

Runs `yt-dlp --dump-json --no-download <url>`, extracts
`view_count`/`like_count`/`comment_count` where the platform exposes them,
and diffs each against the claimed value you pass in:

- No claim given for a field the platform *does* expose -> `INFO` (platform
  value reported, no verdict).
- Claim given and platform value available -> percent-difference computed;
  **>10% divergence -> `FAILED-VERIFICATION`**.
- Platform doesn't expose the field (e.g. Instagram usually hides likes) ->
  `UNAVAILABLE`. Never guessed.

Exit codes: `0` ran successfully (a `FAILED-VERIFICATION` field is *data* in
the output, not a tool failure), `2` yt-dlp not installed (install hint:
`pip install yt-dlp`), `3` network/extraction error.

---

## hygiene_check.py

```
hygiene_check.py <video_path> [--platform ig|yt|yt-long] [--json]
```

Runs these PASS/WARN/FAIL checks via `ffprobe`/`ffmpeg`:

| Check | Rule |
|---|---|
| `resolution` | `ig`/`yt`: width >= 1080 and height >= 1920; `yt-long`: width >= 1920 and height >= 1080 |
| `aspect_ratio` | within 2% of the platform target: 9:16 (`ig`/`yt`) or 16:9 (`yt-long`) |
| `video_codec` | h264 |
| `audio_present` | at least one audio stream |
| `audio_codec` | aac |
| `pixel_format` | yuv420p |
| `duration` | hard band (FAIL outside) + warn band (WARN outside): `ig` hard 3-180s / warn 20-45s; `yt` hard <=180s (2026 Shorts max) / warn 20-60s; `yt-long` hard 60s-60min / warn 8-20min |
| `black_borders` | `ffmpeg -vf cropdetect` sampled; FAIL if the detected crop is smaller than the full frame |
| `repost_guard` | SHA256 must not already be in `ops/pipeline/.published_hashes.json` |

Overall = `FAIL` if any check FAILed (WARNs don't block). Exit `1` on overall
FAIL, `0` on PASS. Exit `2` if `ffprobe`/`ffmpeg` aren't on PATH (install
hint: `winget install Gyan.FFmpeg`) — checked *before* even looking at the
video path, so the dependency hint always surfaces cleanly.

---

## calendar.py

```
calendar.py [--weeks N] [--write]
```

Renders a markdown week-grid combining `ops/calendar/ROADMAP.md`'s planned
items with live pipeline state (every `item.yaml`). Prints to stdout;
`--write` additionally saves to `ops/calendar/calendar-view.md`.

**ROADMAP.md format expected** (planner-owned; produced by the `/plan`
skill — see `ops/pipeline/README.md` and `templates/roadmap-week.md` for the
authoring side of this contract):

```
## Week of YYYY-MM-DD

**Cadence target:** steady-state | launch-surge -- why this band this week
**HERO drought check:** ...

| Day | Pillar | Item (id-slug) | Stage now | Risk |
|---|---|---|---|---|
| Mon | HERO | `003-some-slug` | SCRIPTED | none |
| Tue | WORKHORSE | `004-other-slug` | BRIEFED | BLOCKED-ON-SPARSH |
```

Each planned item is one table row: pillar must be exactly one of
`HERO`/`WORKHORSE`/`FILLER`, the ref is a backtick-quoted `NNN-slug`, and the
`Day` column (`Mon`..`Sun`) is used to compute that item's date within the
week. Unfilled template rows (blank cells, the literal
`HERO\|WORKHORSE\|FILLER` placeholder text) simply don't match the row
pattern and are skipped — so a freshly-scaffolded, not-yet-populated
`ROADMAP.md` degrades to an **empty roadmap** (zero planned items) exactly
like a missing file does, rather than erroring.

Flags raised:
- **Cadence-band violations** per week (`strategy/STRATEGY.md` §7): floor 2
  reels/week (`FLOOR VIOLATION` if under), steady band 3-5/week
  (`OUTSIDE STEADY BAND` if over the floor but outside 3-5).
- **HERO-drought**: no `HERO` item currently `READY` or published within the
  trailing 7 days.

---

## brandkit_check.py

```
brandkit_check.py validate [--json]
brandkit_check.py caption [FILE] [--platform ig|yt] [--json]
brandkit_check.py export <video> [--platform ig|yt|yt-long] [--json]
```

Deterministic validator for `brand/kit.yaml` (SYSTEM_DESIGN_V2_PROPOSAL.md §4.1) — the
machine-readable brand tokens every production skill injects. Reads `brand/kit.yaml` relative
to the resolved repo root (respects `TANGENT_ROOT`, same as every other tool here).

### `validate`

Checks, in order: (1) `brand/kit.yaml` exists and parses to a YAML mapping; (2) every path in
the tool's `REQUIRED_PATHS` list is present (a value may legitimately be `null` — e.g. an
unset handle — only its *presence* is required); (3) every `null` leaf value anywhere in the
file has a matching entry in `meta.todo_sparsh` (an undeclared null is an **error** — "no
unfilled non-TODO nulls"); (4) every `meta.todo_sparsh` entry's declared dotted path actually
exists somewhere in the file (a declared path that doesn't resolve is a **warning** — a stale
or typo'd TODO, not a hard failure). The TODO-declaration convention (`"dotted.path: free-text
explanation"`, one entry per pending field) is documented at the top of `brand/kit.yaml`
itself.

### `caption`

Reads caption text from `FILE` if given (must exist) or from stdin if omitted. Runs against
the loaded kit:
- **Banned-word scan** — case-insensitive, word-boundary regex match against
  `verbal.banned_words.starter_list` (verbatim from `knowledge/craft/reels/scripting-voice.md`)
  + `kit_additions` (kit-level extensions of the same category, not independently sourced).
- **Disclosure-line presence check** — for `--platform ig` (default), all of
  `verbal.disclosure_lines.instagram_caption.required_keywords` must appear (case-insensitive
  substring) in the text; for `--platform yt`, the `youtube_description` entry's keywords.
  Exact wording is expected to vary post-to-post by design (`knowledge/audience/positioning.md`
  wants a real, checkable claim, not a copy-pasted line) — the keyword check is a deterministic
  proxy for "a real disclosure statement is present," not a verbatim-string match.
- **Caption-footer check** — hashtag count (`#\w+` matches) must be ≤5
  (`knowledge/platform/instagram.md` §3); flags any of a small hardcoded set of known
  URL-shortener domains (bit.ly, tinyurl.com, t.co, ow.ly, is.gd, buff.ly, goo.gl, rebrand.ly,
  cutt.ly) per the same file's §8 anti-shortener rule.
- **First-125-characters report** (`--platform ig` only) — informational, never fails the
  check; echoes the text Instagram shows before the "more" tap
  (`knowledge/craft/reels/scripting-voice.md`).

### `export` — **honest scope note**

**Skeleton only.** It runs the same checks as `validate` against `brand/kit.yaml`, prints the
result, then prints `"visual checks pending Phase R2 (logo/palette detection)"` and **exits 0
regardless of the kit-validate result.** It does not open, decode, or otherwise inspect the
video file at all. Do not treat a `0` exit from `export` as any kind of visual-compliance
signal — it isn't one yet. Real logo/palette/frame detection is Phase R2 work
(SYSTEM_DESIGN_V2_PROPOSAL.md §7); this subcommand exists only so the call-site is stable
ahead of that build.

### Exit codes

| Subcommand | 0 | 1 | 2 |
|---|---|---|---|
| `validate` | clean | validation failure(s) found | `brand/kit.yaml` missing or unparseable |
| `caption` | all checks passed | at least one check failed | kit.yaml problem, or the given `FILE` doesn't exist |
| `export` | always (skeleton) | — | kit.yaml missing/unparseable |

---

## Resolved ambiguities

A few points in the build brief were under-specified; here's how this build
resolved them (all deliberately conservative/additive, nothing narrows a
documented contract):

1. **Setting `plane_issue`/`approved_by_sparsh`/`next_action*`/`due` after
   creation.** The spec lists exactly seven `pipeline.py` subcommands and
   doesn't name one for editing these fields post-creation. `stage` was
   extended with optional flags (`--due`, `--next-action`,
   `--next-action-owner`, `--plane-issue`, `--approved-by-sparsh`) that apply
   whenever given, including on a same-stage "touch" call — this is the only
   way `approved_by_sparsh` (the SHIP gate) can ever get set, so it had to
   live somewhere.
2. **`efficiency` bands leave a 15-20% gap.** The spec (and
   `strategy/STRATEGY.md` §6.4) names `<5% warning, 5-10% ok, 10-15% healthy,
   >20% excellent` with nothing said about 15-20%. Filled it with `GOOD` so
   every real number resolves to a verdict, documented above and in the
   `efficiency`/`report` docstrings.
3. **CSV schema**: the build brief's CSV schema (with `pillar` and
   `funnel(0|1)` columns) is more detailed than `SYSTEM_DESIGN.md` §7's
   shorthand list (which omits both) and is used as authoritative here since
   the `decompose`-by-pillar early-warning check and the funnel-median
   summary both need those columns.
4. **`report`'s "off-pillar hits" / "flat spread" triad members** aren't
   given numeric definitions anywhere. Defined as: a "hit" = a row with
   `views >= 2*median_views`; "off-pillar" = none of the hits are
   `HERO`/`WORKHORSE`; "flat spread" = `top_views/median_views < 2.0`. These
   are computable, documented proxies for the qualitative language in
   `strategy/STRATEGY.md` §6.6, not a re-derivation from more data than a
   CSV can carry.
5. **`stage` targeting `PUBLISHED`/`KILLED` directly.** `KILLED` is rejected
   from `stage` (point to `kill`, which always records a reason). `PUBLISHED`
   *is* reachable via a bare `stage` call (useful for testing/inspecting the
   SHIP gate) but real publishing should go through `publish`, since only
   `publish` records the URL and runs the repost guard.
6. **`calendar.py`'s `ROADMAP.md` line format**: matched against the actual
   scaffold `ops/calendar/ROADMAP.md` + `ops/pipeline/README.md` +
   `.claude/skills/plan/SKILL.md` produced during this same build (a
   per-week markdown table: `Day | Pillar | Item (id-slug) | Stage now |
   Risk`), rather than inventing a format — see the table above. A missing
   or not-yet-populated file degrades to "empty roadmap" rather than an
   error, which is also what the smoke test exercises.
7. **Module name collision**: `tools/calendar.py` shares a name with
   Python's stdlib `calendar` module. Since every script's own directory is
   prepended to `sys.path`, a bare `import calendar` from *any* script in
   `tools/` would otherwise resolve to `tools/calendar.py` instead of the
   stdlib module — this bit `datetime.strptime` (which lazily does `import
   calendar` internally) during development. Fixed by having
   `_common.parse_iso_date` use `date.fromisoformat` instead, which never
   touches the `calendar` module; the tool file itself is unaffected and
   still named `calendar.py` per spec.
8. **`derive`'s `--vertical` default.** The build brief only specifies that
   `--pillar` defaults to the parent's; `--vertical` is listed as an
   equally-optional flag with no stated default. Resolved by defaulting
   `--vertical` to the parent's vertical too, same as `--pillar` — most
   derivatives share the parent's container (a Shorts re-cut of a reel is
   still `vertical: reels`); callers doing a cross-vertical derivative (a
   newsletter section off a reel) pass `--vertical newsletter` explicitly.
   This is additive (narrows nothing the spec promised) and matches `new`'s
   own pattern of every field having an explicit default.
9. **`derivative-spec.md` vs. "script.md contains a DERIVATIVE SPEC block."**
   The build brief describes the G1-skip rationale as "the child's script.md
   contains a DERIVATIVE SPEC block" but also separately specifies the
   mechanical gate check as "a `derivative-spec.md` file present in the item
   folder (exact filename)." Read literally these name two different
   artifacts; resolved by treating them as the same artifact under its
   mechanical name — `derivative-spec.md` is a standalone file (item-folder
   root, sibling of `script.md`, not embedded inside it) containing the
   source-beats/re-grammar/native-changes content the brief describes. This
   keeps `pipeline.py`'s exact-filename check simple (one file to glob for,
   not "does script.md contain a specific heading") and avoids duplicating
   the same content in two places. `script.md` itself is still created for
   every derivative (same stub/template behavior as `new`) for continuity
   with the parent's format, but the G1-skip signal lives only in
   `derivative-spec.md`.
10. **`ingest_stats.py --mapping` semantics: full replace, not merge.** The brief says
    "support a `--mapping <json>` override file for when reality differs" without specifying
    whether it patches individual keys or replaces the whole mapping. Resolved as a full
    replace: simpler and more predictable (no "which of the built-in entries are still active"
    ambiguity) — `inspect` is the tool for seeing the real headers and writing a complete
    reconciled mapping, not for patching one field at a time.
11. **`ingest_stats.py` dedup: is `followers_at_post` "accrual" too?** The brief's
    "never lower silently: warn on decreases" language isn't scoped to only the engagement
    metrics, and a follower count genuinely can drop (unlike views/likes/etc, which platforms
    don't actually decrease). Resolved by treating it uniformly with the other numeric fields
    (higher-wins, warn-and-keep on lower) for implementation simplicity and to honor the
    literal "never lower silently" rule as written; flagged here as a deliberate, documented
    interpretation rather than a claim that follower counts are monotonic in reality.
12. **`ingest_stats.py` pillar enrichment.** Not requested by the brief, added because
    leaving `pillar` blank on every ingested row would silently degrade `metrics.py report`'s
    `hits_only_off_pillar` early-warning check. Best-effort only: looks up the mapped URL in
    every `ops/pipeline/*/item.yaml`'s `published` dict (written by `pipeline.py publish`);
    blank (tolerated) if no match, never guessed or defaulted to a real pillar value.

---

## Smoke test

```
python tools\tests\smoke.py
```

No network required. Runs every tool as a subprocess against a temp
directory (via `TANGENT_ROOT`), so nothing in the real `ops/` tree is
touched. Covers: `pipeline.py` end-to-end (new item -> legal transitions ->
an illegal transition rejected -> both critique gates blocking then passing
-> the SHIP gate -> publish + repost guard -> kill -> board/blocked/validate,
including validate catching an injected schema violation); the Repurposing
Engine (`derive` creates a properly-linked child item; `derive` against a
nonexistent or KILLED parent is rejected; `validate` catches an orphaned
`parent_id`; a derivative unlocks SCRIPTED->PRODUCING via `derivative-spec.md`
with no G1 critique file at all; a non-derivative item is still blocked
without a G1 SHIP verdict; `board` shows the `^NNN` child annotation);
`metrics.py`
(likerate, all five `decompose` quadrants, efficiency, funnel, a full
`report` against an inline CSV fixture); `ingest_stats.py` (writes its own
synthetic IG + YT export fixtures, 3 rows each; `inspect` against both;
`ig`/`yt` `--dry-run` mapping correctness incl. the yt video-id -> watch-url
derivation and IG funnel-url flagging; a real append that produces a
`posts.csv` consumable by `metrics.py report`; the dedup-by-url update rule
warning on a decreased number while accruing an increase; the `--mapping`
override recovering a file the built-in mapping can't read; and the
openpyxl-availability branch for `.xlsx`, present in this dev environment so
the real xlsx-read path is exercised, degrading to the exit-2 install-hint
path otherwise); `verify_stats.py` and
`hygiene_check.py`'s dependency-detection paths (both yt-dlp and
ffmpeg/ffprobe are absent in the reference dev environment, so these assert
the clean exit-2 + install-hint behavior); `calendar.py` against an
empty roadmap; and `brandkit_check.py` -- the one exception to the
"sandboxed `TANGENT_ROOT`" rule, since `validate`/`caption` are read-only and
this is the one place the suite deliberately checks the REAL `brand/kit.yaml`
parses clean, plus `caption` catching a planted banned word, catching a
missing disclosure line, and passing both a clean file-input and a clean
stdin-input caption. Prints `PASS`/`FAIL` per case and exits non-zero on any
FAIL.
