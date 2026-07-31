# GATE C — Instagram Like-Count Remediation

Remediation date: 2026-07-25 (same day as the harvest and the Gate C audit it responds to).
Author: remediation agent, full-corpus re-pull pass, following `QC_PROTOCOL.md`'s append-only /
no-silent-rewrite discipline.

**Scope:** every Instagram reel shortcode cited together with a like count anywhere in
`ig_harvest/*.md` (detail-pull tables, "Pin/date confirmation" tables, "Anomaly re-verification"
sections) and `creators/ig_*.md` (all per-video post-mortems, footnote spot-checks, and standalone
case-study citations). **110 unique reels enumerated, all 110 successfully re-pulled** via
`yt-dlp --sleep-requests 1 -j "https://www.instagram.com/reel/<shortcode>/"` against the live public
reel URL, logged out, on 2026-07-25. **Zero UNVERIFIABLE** — every pull succeeded on the first or
second (retry) attempt; no reel had to be abandoned for lack of data.

Raw JSON for every pull is preserved at
`/private/tmp/claude-501/-Users-sparsh-Documents-Projects-Tangent/3f21975f-6df6-481e-9a72-4d4c86b4bb54/scratchpad/gatec_remediation/raw_pulls/<shortcode>.json`
as the audit trail (not part of the repo; reproducible by re-running the same commands). The
compiled master table (machine-readable) lives alongside it as `master_table.tsv`.

One shortcode surfaced during enumeration — `DNGh28v0Tof` (cited in `ig_vaibhavsisinty.md` for a
caption quote only) — carries no like count in any source file and was excluded from the 110; it is
not part of this remediation's scope and needed no correction.

---

## 1. Master corrections table

Verdict thresholds (as specified): **MATCH** ratio < 1.15x · **DRIFT** 1.15x–2.0x · **WRONG** > 2.0x.
"harvest likes" = the browser/logged-in-session number in `ig_harvest/<account>.md`'s detail-pull
table (the number under audit). "dossier likes" = the number currently in `creators/ig_<account>.md`,
with the verification method it was tagged with in that file (`yt-dlp` = already independently
re-pulled by the dossier author against the IG reel itself; `harvest-table` = merely inherited from
the harvest, never independently checked; `WebFetch`/`browser-repull` = a different, non-yt-dlp
independent method). Where a reel has no harvest-table entry ("—") it was a dossier-only addition
beyond the harvest's original top-5+2-flops sample; where a reel's like count reads "hidden" it is an
Instagram "hide like count" creator-setting artifact, not a harvest miss (see §3).

Fresh comment counts are shown for the sanity anchor described in the task: comments should track the
old value closely regardless of whether likes were wrong.

### 100xengineers (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `CyWFEsDyJsC` | harvest only | 139,000 | — | 654/654 | 173,564 | 1.25x | **DRIFT** |
| `DZ5JAHgJjRm` | harvest only | 128,000 | — | 801/800 | 128,171 | 1.0x | MATCH |
| `DZxkeU5Jtud` | harvest only | 541 | — | 496/496 | 541 | 1.0x | MATCH |
| `DaDZxjKtmGP` | harvest only | 6,999 | — | 44/44 | 6,999 | 1.0x | MATCH |
| `DaiR5_NJojP` | harvest only | 552 | — | 6/6 | 552 | 1.0x | MATCH |
| `Dak5CSsppNg` | harvest only | 13,000 | — | 61/61 | 12,829 | 1.01x | MATCH |
| `DbBQzXGpCoA` | harvest only | 5,511 | — | 46/46 | 5,525 | 1.0x | MATCH |

### ai_ankitarora (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DV707PciHfD` | harvest+dossier | 34,000 | 33,634 (yt-dlp) | 86,000/86,203 | 33,634 | 1.01x | MATCH |
| `DV_FSjBCB9O` | harvest+dossier | 154,000 | 153,511 (yt-dlp) | 34,000/33,709 | 153,511 | 1.0x | MATCH |
| `DW06azLCNBw` | harvest only | 5,623 | — | 2,523/2,523 | 5,623 | 1.0x | MATCH |
| `DWRkb-MiErx` | harvest+dossier | 31,000 | 31,289 (yt-dlp) | 421/421 | 31,289 | 1.01x | MATCH |
| `DX0o-wxT-YP` | harvest only | 2,807 | — | 2,135/2,135 | 2,807 | 1.0x | MATCH |
| `DZ-c-kEg5WT` | harvest+dossier | 384 | 384 (yt-dlp) | 52/52 | 384 | 1.0x | MATCH |
| `Dafiy_OgPZe` | harvest only | 332 | — | 258/258 | 332 | 1.0x | MATCH |

### elevenpercentprod (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DUEFiGlAYW4` | dossier only | hidden (not shown) | 3 (yt-dlp) | —/51 | 3 | 1.0x | MATCH |
| `DURH42UkjE7` | dossier only | hidden (not shown) | 3 (yt-dlp) | —/9 | 3 | 1.0x | MATCH |
| `DWqP0Exk0iW` | harvest+dossier | 15,000 | 14,535 (yt-dlp) | 12,000/11,909 | 14,535 | 1.03x | MATCH |
| `DX-bJErPxe7` | harvest+dossier | 53,000 | 53,167 (yt-dlp) | 61,000/61,433 | 53,171 | 1.0x | MATCH |
| `DXCWgz9k2Ag` | harvest+dossier | 14,000 | 14,161 (yt-dlp) | 11,000/11,309 | 14,161 | 1.01x | MATCH |
| `DXlFWL5EkaN` | harvest+dossier | 26,000 | 26,429 (yt-dlp) | 48,000/47,701 | 26,429 | 1.02x | MATCH |
| `DYm3hE9T75T` | harvest+dossier | 14,000 | 13,643 (yt-dlp) | 21,000/21,015 | 13,655 | 1.03x | MATCH |

### handlytech (8 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `C9PdusWtkOh` | harvest+dossier | 2,000,000 | 2,118,218 (yt-dlp) | 6,437/6,437 | 2,118,218 | 1.06x | MATCH |
| `CybW5zct2AA` | harvest+dossier | 726,000 | 739,240 (yt-dlp) | 1,944/1,944 | 739,240 | 1.02x | MATCH |
| `DFC6zh3iZKn` | harvest+dossier | 573,000 | 576,699 (yt-dlp) | 3,451/3,451 | 576,700 | 1.01x | MATCH |
| `DXy2ppzokZt` | harvest+dossier | 66 | 66 (yt-dlp) | 43/43 | 66 | 1.0x | MATCH |
| `DYcI0guoijZ` | harvest+dossier | 71 | 71 (yt-dlp) | 69/69 | 71 | 1.0x | MATCH |
| `DZChXWoIaHF` | dossier only | — | 2,054 (yt-dlp) | —/2,252 | 2,055 | 1.0x | MATCH |
| `DZUg7ZxIHLv` | harvest+dossier | 3,594 | 3,595 (yt-dlp) | 5,492/5,494 | 3,597 | 1.0x | MATCH |
| `DZozx8UoTDy` | harvest+dossier | **59** | 114 (yt-dlp) | 59/59 | **114** | **1.93x** | **DRIFT** (see §3, near-2x undercount) |

### harpercarrollai (11 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `C4eNPF3PdpG` | dossier only (standalone spot-check) | — | 111,083 (yt-dlp) | —/863 | 111,083 | 1.0x | MATCH |
| `DCWW2EnA_sm` | harvest only | 93,000 | — | 398/398 | 92,956 | 1.0x | MATCH |
| `DVbM3sBjl26` | harvest+dossier | **5,358** | 7,171 (yt-dlp) | 904/904 | **7,171** | **1.34x** | **DRIFT** — new finding, not in original critic audit |
| `DW9gguSDgRM` | dossier only | — | 685 (yt-dlp) | —/32 | 685 | 1.0x | MATCH |
| `DX9nDB_pdBF` | dossier only | — | 492 (yt-dlp) | —/31 | 492 | 1.0x | MATCH |
| `DYPXSQ4hPdF` | dossier only | — | 13,267 (yt-dlp) | —/6,404 | 13,267 | 1.0x | MATCH |
| `DZ-xwWgAqox` | harvest+dossier | 203 | 203 (yt-dlp) | 7/7 | 203 | 1.0x | MATCH |
| `DZfgPtFObU1` | harvest+dossier | **904** | 33,065 (yt-dlp) | 1,741/1,741 | **33,065** | **36.58x** | **WRONG** |
| `DaBLNlJCiVE` | harvest only | 187 | — | 5/5 | 187 | 1.0x | MATCH |
| `Dan0IIuJP7K` | dossier only | hidden (not shown) | 3 (yt-dlp) | —/58 | 3 | 1.0x | MATCH (hide-like-count, see §3) |
| `DbD8-40Owbv` | dossier only | hidden (not shown) | 3 (yt-dlp) | —/536 | 3 | 1.0x | MATCH (hide-like-count, see §3) |

### kallaway (6 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `C8uZzh0pvPN` | harvest only | 56,000 | — | 3,784/3,784 | 56,819 | 1.01x | MATCH |
| `C_iVgDcJLd1` | harvest only | 642,000 | — | 2,164/2,164 | 681,844 | 1.06x | MATCH |
| `DVhB8rMjp1m` | harvest+dossier | **678** | 64,910 (yt-dlp) | 972/972 | **64,910** | **95.74x** | **WRONG** |
| `DXSDF9djpRD` | harvest+dossier | **476** | 4,223 (yt-dlp) | 77/77 | **4,223** | **8.87x** | **WRONG** |
| `DY7GAsGuwGr` | harvest+dossier | **2,850** | 5,188 (yt-dlp) | 99/99 | **5,188** | **1.82x** | **DRIFT** |
| `DaAnAA3O5Sg` | dossier only | — | 638 (yt-dlp) | —/10 | 638 | 1.0x | MATCH |

### nateherkai (10 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DRXZJeHiAES` | harvest+dossier | 90,000 | 89,817 (yt-dlp) | 125,000/124,635 | 89,816 | 1.0x | MATCH |
| `DTXqGz2Evxq` | harvest+dossier | 61,000 | 60,614 (yt-dlp) | 7,125/7,127 | 60,614 | 1.01x | MATCH |
| `DW4NudCk9ji` | harvest+dossier | 44,000 | 44,436 (yt-dlp) | 50,000/49,917 | 44,437 | 1.01x | MATCH |
| `DZ76SSujumB` | harvest+dossier | **177** | 378 (yt-dlp) | 106/106 | **378** | **2.14x** | **WRONG** — new finding, not in original critic audit |
| `DZabuNfFMkJ` | dossier only | — | 6,292 (yt-dlp) | —/17,491 | 6,292 | 1.0x | MATCH |
| `DZdAjsLFO0n` | dossier only | — | 5,986 (yt-dlp) | —/23,098 | 5,987 | 1.0x | MATCH |
| `DZflUYLHKb-` | dossier only | — | 7,702 (yt-dlp) | —/27,608 | 7,703 | 1.0x | MATCH |
| `DZku3mJH594` | harvest+dossier | 11,000 | 10,853 (yt-dlp) | 10,000/10,337 | 10,866 | 1.01x | MATCH |
| `DbDJlTkgOtY` | harvest+dossier | 185 | 185 (yt-dlp) | 16/16 | 185 | 1.0x | MATCH |
| `DbGlL0ciIvc` | harvest+dossier | 129 | 129 (yt-dlp) | 126/126 | 130 | 1.01x | MATCH |

### networkchuck (7 reels, no dossier exists)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DXonsidjKfc` | harvest only | 13,000 | — | 84/84 | 13,471 | 1.04x | MATCH |
| `DYAmkc-FTUY` | harvest only | **1,784** | — | 14/14 | **7,047** | **3.95x** | **WRONG** |
| `DYPw8ezjXG-` | harvest only | 15,000 | — | 74/74 | 15,172 | 1.01x | MATCH |
| `DZDi7hmk8OP` | harvest only | 646 | — | 13/13 | 646 | 1.0x | MATCH |
| `DZGUw3GCSkw` | harvest only | 613 | — | 5/5 | 613 | 1.0x | MATCH |
| `DZyLjFWCX_G` | harvest only | 1,306 | — | 12/12 | 1,591 | 1.22x | **DRIFT** |
| `Da_JBWIvj0y` | harvest only | 16,000 | — | 108/108 | 16,471 | 1.03x | MATCH |

### nick_saraev (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DSm-QQ_Dxh3` | harvest+dossier | 34,000 | 34,416 (yt-dlp) | 10,000/10,062 | 34,417 | 1.01x | MATCH |
| `DXqzDc6j-H_` | harvest+dossier | 38,000 | 37,780 (yt-dlp) | 32,000/31,570 | 37,786 | 1.01x | MATCH |
| `DYWXwAmPdIr` | harvest only (own "Anomaly re-verification" section) | **987** | — | 455/455 | **1,670** | **1.69x** | **DRIFT** |
| `DYfHXdPvBzQ` | harvest only | 23,000 | — | 21,000/20,988 | 23,429 | 1.02x | MATCH |
| `Da8ZthUPK98` | harvest+dossier | 57,000 | 57,437 (yt-dlp) | 32,000/32,114 | 57,521 | 1.01x | MATCH |
| `DaBcPNeTYfk` | harvest only | 913 | — | 666/666 | 913 | 1.0x | MATCH |
| `DbLpxfKPKoN` | harvest+dossier | 1,184 | 1,192 (yt-dlp) | 1,471/1,512 | 1,215 | 1.03x | MATCH |

### sabrina_ramonov (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DTqPISajqEt` | harvest+dossier | 4,027 | 4,028 (yt-dlp) | 1,958/1,958 | 4,028 | 1.0x | MATCH |
| `DY2KolvkzdF` | harvest+dossier | 4,549 | 4,549 (yt-dlp) | 3,683/3,685 | 4,548 | 1.0x | MATCH |
| `DYu1xbHEUD5` | harvest+dossier | 195,000 | 194,914 (yt-dlp) | 145,000/145,329 | 194,930 | 1.0x | MATCH |
| `Da1TQzZTR2E` | harvest+dossier | 1,411 | 1,411 (yt-dlp) | 389/389 | 1,412 | 1.0x | MATCH |
| `DaS-IcjjqNt` | harvest+dossier | 112,000 | 111,770 (yt-dlp) | 98,000/98,117 | 111,796 | 1.0x | MATCH |
| `DbL8Nqvgk3b` | harvest+dossier | 228 | 228 (yt-dlp) | 357/364 | 230 | 1.01x | MATCH |
| `DbLkLEIDlTR` | harvest+dossier | 119 | 119 (yt-dlp) | 4/4 | 119 | 1.0x | MATCH |

### sebastien (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DVylvZbDGTo` | harvest+dossier | **379** | 379 (harvest-table, **not** independently checked) | 95/95 | **2,730** | **7.2x** | **WRONG** |
| `DW_VCbrDPWM` | harvest+dossier | 61,000 | 61,000 (browser-repull) | 1,789/1,789 | 60,919 | 1.0x | MATCH |
| `DWotUKUjJq2` | harvest+dossier | 5,763 | 5,763 (harvest-table) | 110/110 | 5,763 | 1.0x | MATCH |
| `DYSWrorMzBA` | harvest+dossier | **395** | 395 (harvest-table, **not** independently checked) | 247/247 | **10,594** | **26.82x** | **WRONG** |
| `DaAlMicsiBD` | harvest+dossier | **435** | 435 (harvest-table, **not** independently checked) | 193/194 | **3,867** | **8.89x** | **WRONG** |
| `DaffjwFsX85` | harvest+dossier | 205 | 205 (harvest-table) | 114/114 | 205 | 1.0x | MATCH |
| `DaiKv3Ls_tT` | harvest+dossier | 182 | 182 (harvest-table) | 128/130 | 183 | 1.01x | MATCH |

### thevarunmayya (10 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `C7CPlnDLW9W` | harvest+dossier | 98,000 | 98,013 (yt-dlp) | 457/457 | 98,013 | 1.0x | MATCH |
| `DExE3UOhUoq` | dossier only | — | 20,619 (yt-dlp) | —/138 | 20,620 | 1.0x | MATCH |
| `DIB4N7-oJ-m` | harvest+dossier | 58,000 | 58,189 (yt-dlp) | 1,000/1,000 | 58,189 | 1.0x | MATCH |
| `DY_5MHRBLNs` | dossier only | — | 17,384 (yt-dlp) | —/219 | 17,384 | 1.0x | MATCH |
| `DYw1DPjhcMU` | harvest+dossier | 68,000 | 68,355 (yt-dlp) | 328/328 | 68,367 | 1.01x | MATCH |
| `DZ6mQK6Bxwh` | harvest+dossier | 57,000 | 56,766 (yt-dlp) | 1,254/1,253 | 56,767 | 1.0x | MATCH |
| `DZFtk5xB-d8` | harvest+dossier | 90,000 | 90,292 (yt-dlp) | 512/512 | 90,292 | 1.0x | MATCH |
| `Da0hzVdhsIE` | harvest+dossier | 2,185 | 2,186 (yt-dlp) | 19/19 | 2,189 | 1.0x | MATCH |
| `DaDD4gWh3Kn` | harvest+dossier | 2,384 | 2,384 (yt-dlp) | 26/26 | 2,384 | 1.0x | MATCH |
| `DaYIYk3BJM9` | dossier only | — | 37,151 (yt-dlp) | —/349 | 37,175 | 1.0x | MATCH |

### tiffintech (9 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DHvpvxTg2ci` | harvest+dossier | 39,000 | 39,000 (harvest-table) | 345/345 | 38,667 | 1.01x | MATCH |
| `DQO_cyuEaUr` | harvest+dossier | 85,000 | 85,000 (harvest-table) | 690/690 | 85,046 | 1.0x | MATCH |
| `DW31ssREcbj` | harvest+dossier | **1,256** | 1,256 (harvest-table, **not** independently checked) | 54/54 | **69,067** | **54.99x** | **WRONG** |
| `DXEuwVJkUkO` | harvest+dossier | 519 | 519 (harvest-table) | 30/30 | 519 | 1.0x | MATCH |
| `DXzqg10Rejn` | dossier only | — | 90,200 (WebFetch) | —/714 | 90,178 | 1.0x | MATCH |
| `DZ2vb3hxmIT` | dossier only | — | 22,600 (WebFetch) | —/259 | 22,594 | 1.0x | MATCH |
| `DZxAH3LxaSA` | harvest+dossier | 1,528 | 1,528 (harvest-table) | 53/53 | 1,577 | 1.03x | MATCH |
| `Da5aQ8zRXTI` | harvest+dossier | 382 | 382 (harvest-table) | 10/10 | 486 | 1.27x | **DRIFT** |
| `DaNk7iTRewN` | harvest+dossier | **2,527** | 2,527 (harvest-table, **not** independently checked) | 88/88 | **1,145,353** | **453.25x** | **WRONG** |

### vaibhavsisinty (7 reels)

| shortcode | source | harvest likes | dossier likes | comments (old/fresh) | yt-dlp likes (fresh) | ratio | verdict |
|---|---|---|---|---|---|---|---|
| `DZEpQ9cgEik` | harvest+dossier | 47,000 | 46,800 (WebFetch) | 197/197 | 46,827 | 1.0x | MATCH |
| `DZK-XJ-AIZK` | harvest+dossier | 27,000 | 27,000 (WebFetch) | 80/80 | 27,351 | 1.01x | MATCH |
| `DZaRmD9A9eF` | harvest+dossier | 14,000 | 14,400 (WebFetch) | 109/109 | 14,443 | 1.03x | MATCH |
| `DZfrPXIgXCp` | harvest+dossier | 16,000 | 15,900 (WebFetch) | 144/144 | 15,949 | 1.0x | MATCH |
| `DaNu_sMAVD_` | harvest+dossier | 10,000 | 10,400 (WebFetch) | 51/51 | 10,444 | 1.04x | MATCH |
| `Dae05TSAK1l` | harvest+dossier | 2,567 | 2,600 (WebFetch) | 171/171 | 2,567 | 1.0x | MATCH |
| `DbDltYAge31` | harvest+dossier | 1,756 | 1,800 (WebFetch) | 16/16 | 1,758 | 1.0x | MATCH |

---

## 2. Error-distribution stats

**110/110 reels re-pulled, 0 UNVERIFIABLE.**

| Verdict | Count | % of corpus |
|---|---|---|
| MATCH (<1.15x) | 93 | 84.5% |
| DRIFT (1.15x–2.0x) | 7 | 6.4% |
| WRONG (>2.0x) | 10 | 9.1% |
| **DRIFT+WRONG combined** | **17** | **15.5%** |

**This is meaningfully lower than the critic's "~45% of sampled reels wrong" headline** — that
figure was correct for the critic's own 22-reel sample, which deliberately concentrated on
already-flagged anomalies and ad-boosted posts (a biased, high-risk sample by design, appropriate
for a scoping audit). This full-corpus census of all 110 cited reels shows the *base rate* across
the whole harvest is **~15.5% affected, ~9.1% severely wrong** — the critic's sample correctly
identified the *failure mode* but its raw percentage should not be quoted as the corpus-wide rate.

### Magnitude histogram (17 non-MATCH reels)

| Ratio band | Count | Reels |
|---|---|---|
| 1.15x–1.3x | 4 | `Da5aQ8zRXTI` (1.27x), `CyWFEsDyJsC` (1.25x), `DZyLjFWCX_G` (1.22x) |
| 1.3x–2.0x | 4 | `DZozx8UoTDy` (1.93x), `DY7GAsGuwGr` (1.82x), `DYWXwAmPdIr` (1.69x), `DVbM3sBjl26` (1.34x) |
| 2x–10x | 5 | `DZ76SSujumB` (2.14x), `DYAmkc-FTUY` (3.95x), `DVylvZbDGTo` (7.2x), `DXSDF9djpRD` (8.87x), `DaAlMicsiBD` (8.89x) |
| 10x–50x | 2 | `DYSWrorMzBA` (26.82x), `DZfgPtFObU1` (36.58x) |
| 50x–100x | 2 | `DW31ssREcbj` (54.99x), `DVhB8rMjp1m` (95.74x) |
| 100x–500x | 1 | `DaNk7iTRewN` (453.25x) |

The distribution is bimodal, not a smooth curve: most affected reels cluster at either a mild
1.2x–2x accrual-or-noise band, or a severe 7x–453x band — very few land in the 2x–7x middle. This
supports the critic's mechanistic hypothesis (§3 below) rather than a generic "measurement noise"
explanation, which would predict a smoother falloff.

### Pattern found: the "small exact number" signature

**16 of the 17 non-MATCH reels' old (wrong) like counts were displayed as small, non-"K"-rounded
exact digits (59–5,358), regardless of how large the reel's true like count or view count turned
out to be.** The lone exception, `CyWFEsDyJsC` (139,000 → 173,564, 1.25x DRIFT), is a K-rounded
number attached to a 2023-era pinned post still under review 2.5 years later — plausibly genuine
like-count accrual in that window, not the same bug (comments matched exactly, consistent with a
real, slow-moving post rather than a scrape failure).

This is strong, load-bearing evidence for the mechanism the original Gate C critic proposed at
MED confidence: Instagram's rendered "Liked by `[named user]`, `[named user]` and N others" UI
pattern causes the browser-DOM scraper to sometimes capture only the small trailing "N others"
figure instead of the true total. It explains:
- Why the broken numbers are small, "exact," never-K-rounded digits — they're a leftover-count
  field, not a mis-scaled version of the true count (`DaNk7iTRewN`'s true 1,145,353 likes got
  recorded as 2,527 — not 2.5M misread as 2,527, an unrelated small number entirely).
- Why the ratio is *unpredictable* per-post (1.22x to 453x) — it depends on how many named likers
  happened to render that session, not on any property of the post itself.
- Why comments were never wrong (110/110 comment counts matched within ordinary live-count drift,
  max ±7) — Instagram renders comments as a plain "View all N comments" numeral with no
  named-user-prefix pattern to misparse.

### Pattern found: correlation with sponsored/boosted content, but not exclusive to it

11 of 17 (65%) non-MATCH reels are disclosed-sponsored or suspected-self-funded-boosted posts
(tiffintech's 2 Lenovo/FIFA posts, networkchuck's 2 Vanta posts, kallaway's 3 undisclosed mid-grid
spikes, harpercarrollai's Claude-partner post, tiffintech's Adobe-partner flop, nateherkai's
Glance-AI-partner post, handlytech's CapCut-funnel post). This is a real concentration relative to
sponsored content's overall share of the 110-reel sample (well under 20%), consistent with paid
amplification independently inflating view counts far more than it inflates genuine engagement —
exactly the mechanism these posts were flagged for in the first place.

**But 6 of 17 (35%) are ordinary organic content with no sponsorship signal at all** — sebastien's
three Video 1/2/3 top performers, harpercarrollai's `DZfgPtFObU1` ("Comment BUILD" tool demo,
organic), nick_saraev's `DYWXwAmPdIr` (organic GPT-5.5 explainer), and 100xengineers' pinned
`CyWFEsDyJsC` (plausible accrual, not the same bug). **The bug is a scraper defect that can strike
any post above a certain reach threshold, not a symptom specific to paid content** — sponsorship
correlates with getting caught (because sponsored posts were the ones already being scrutinized for
suspiciously low engagement) more than it causes the underlying defect.

### Pattern found: no correlation with reel age/pin status once accrual is accounted for

Every genuinely pinned/legacy reel (2023–2025-dated: `C9PdusWtkOh`, `CybW5zct2AA`, `DFC6zh3iZKn`,
`C8uZzh0pvPN`, `C_iVgDcJLd1`, `C7CPlnDLW9W`, `DIB4N7-oJ-m`, `DCWW2EnA_sm`, `DExE3UOhUoq`,
`C4eNPF3PdpG`) came back MATCH. The bug does not track post age; it tracks whatever UI state
happened to render during the specific browser-harvest session.

### Two important non-bugs surfaced and explicitly distinguished

1. **Instagram's "hide like count" creator setting** (`Dan0IIuJP7K`, `DbD8-40Owbv`, both
   harpercarrollai — the account's ChatGPT/Anthropic-partner launch-day posts): both reels return
   exactly **3** likes on repeated, independent `yt-dlp` pulls hours apart (dossier's own pull and
   this remediation's fresh pull agree exactly), while comments remain intact and plausible (58,
   536). A genuine browser-scrape bug resolves to a *much larger* real number on independent
   re-pull, as every WRONG/DRIFT reel above did; a hidden-like-count post stays pinned at the same
   small placeholder. These two reels are correctly excluded from the error-rate denominator as a
   different, non-defect phenomenon — do not fold them into "corpus-wide harvest error rate"
   statistics.
2. **`DVbM3sBjl26`** (harpercarrollai, 1.34x DRIFT) and **`DZ76SSujumB`** (nateherkai, 2.14x WRONG)
   are **two new instances of the browser-harvest bug this remediation surfaced that were not in
   the original Gate C critic's 22-reel sample** — the dossiers for both accounts had already
   independently re-verified via `yt-dlp` and silently carried the correct number forward, so no
   live claim was ever built on the wrong number, but the harvest file's own detail-pull table for
   both accounts still needed the correction applied (done in §4 below).

---

## 3. Per-conclusion verdicts

**(a) tiffintech — Lenovo 73.7M + FIFA 12.1M "paid view-boost with near-zero engagement": DIES.**
Corrected likes: `DaNk7iTRewN` 2,527 → 1,145,353 (453x), `DW31ssREcbj` 1,256 → 69,067 (55x).
Recomputed like-rates against the harvest's own view counts: **1.55%** (`DaNk7iTRewN`,
1,145,353/73.7M) and **0.57%** (`DW31ssREcbj`, 69,067/12.1M) — versus the originally-claimed
0.003%–0.01%. 1.55% sits *inside* this account's normal organic band (the dossier's own other
organic top performers run 1.9%–6.9%); 0.57% is on the low side but only ~4–8x below norm, not
"100–1000x." The "near-zero engagement, this number is bought not earned" framing and the STEPPS
claim that "the engagement data flatly contradicts any read of this as psychologically resonant
content" do not survive at the corrected magnitude. What *does* survive: the disclosed
`#LenovoFIFA #LenovoPartner` hashtags and the astronomical absolute view counts (73.7M/12.1M vs. an
~800K–2.5M organic ceiling) still support *some* paid-amplification read on reach — just not via the
like-rate argument as originally stated, and not as "near-zero organic resonance."
The **Sanofi partial-boost reclassification SURVIVES fully intact and unchanged**: `DZxAH3LxaSA`
1,528 → 1,577 (1.03x, MATCH) — this was independently confirmed accurate before this remediation
and remains the one genuinely trustworthy "boost" finding of the three flagged on this account.

**(b) networkchuck — Vanta posts' boost signature (0.02%–0.4% claimed): SURVIVES, WEAKENED.**
`DYAmkc-FTUY` corrected: 1,784 → 7,047 likes (3.95x); like-rate 0.070% vs. claimed 0.018% — still
~54–66x below this account's organic norm (3.8%–4.6%), so the qualitative "ad-boosted, near-zero
engagement" read holds at a less extreme (but still dramatic) magnitude. `DZyLjFWCX_G` corrected:
1,306 → 1,591 (1.22x, mild DRIFT); like-rate 0.53% vs. claimed 0.43% — this one is now only ~7–9x
below organic norm, a materially *milder* anomaly than the account's other Vanta post and than the
originally-stated "0.02%–0.4%" range implied. Recommend restating as: DYAmkc-FTUY strongly supports
the boost read; DZyLjFWCX_G is a real but much less dramatic instance of it.

**(c) sebastien — "engagement-rate paradox" (flops out-engaging 3 of 5 tops): SURVIVES** (with the
specific video set changing). Corrected like-rates: V1 `DaAlMicsiBD` 0.161% (was 0.018%), V2
`DVylvZbDGTo` 0.171% (was 0.024%), V3 `DYSWrorMzBA` 1.059% (was 0.0395%), V4 `DW_VCbrDPWM` 6.41%
(unchanged, confirmed accurate), V5 `DWotUKUjJq2` 0.625% (unchanged). Flops: `DaffjwFsX85` 1.03%,
`DaiKv3Ls_tT` 0.85% (both essentially unchanged by correction). Under the corrected numbers the
flops (0.85%–1.03%) still exceed **3 of the 5** tops — but the set flips from {V1, V2, V3} (true
under the old wrong numbers) to {V1, V2, V5} (true under corrected numbers), because V3 jumped from
the second-worst performer to the second-best. The count-of-3 headline survives; any prose that
names *which* three tops the flops beat needs updating. Separately, the dossier's own claims tied to
absolute magnitude do not survive: "IG like-rate 0.018%, single lowest of the 5 top videos"
SURVIVES-WEAKENED (V1 is still lowest, but at 0.161% not 0.018%); "TikTok twin's like-rate over 500x
higher" DIES (true gap is ~61x, using TikTok's 9.77% against corrected 0.161%); the stated ranking
V1<V2<V3<V5<V4 DIES and becomes V1<V2<V5<V3<V4 (V3 and V5 swap — V3 had zero cross-platform
corroboration of any kind pre-audit and carried the largest error in the sample, 26.82x).

**(d) kallaway — boost verdict magnitudes (critic says survives at ~15-400x): SURVIVES, CONFIRMED.**
Fresh pulls match the critic's and the dossier's own numbers to the digit: `DVhB8rMjp1m` 64,910
(95.74x), `DXSDF9djpRD` 4,223 (8.87x), `DY7GAsGuwGr` 5,188 (1.82x) — three independent pulls (dossier,
critic, this remediation) now agree exactly. Recomputed like-rates against confirmed pinned-tile
organic norm (1.32%–4.70%, from `C8uZzh0pvPN`/`C_iVgDcJLd1` fresh numbers): the three mid-grid
spikes sit **15x–439x below organic norm** (`DVhB8rMjp1m` ≈15x at the best case, `DXSDF9djpRD` ≈439x
at the worst case, `DY7GAsGuwGr` ≈90x–324x). The "~15-400x below organic" language the critic
recommended is accurate and should be adopted verbatim in place of the original "100-1000x."

**(e) handlytech — `DZozx8UoTDy` 331K/59-vs-114-likes anomaly: RESOLVED AT 114, borderline
DRIFT/WRONG.** Three independent `yt-dlp` pulls (dossier's two, this remediation's one) all agree on
114; the harvest's two same-tool re-pulls both stuck at 59. Ratio 114/59 = 1.93x — by the stated
thresholds this is DRIFT (just under the 2.0x WRONG cutoff), but flag the boundary tension
explicitly: in absolute terms the harvest undercounted true likes by essentially half, a severe
practical error that happens to fall one-hundredth of a ratio-point short of the WRONG bucket.
Comments (59) match across all pulls — the defect is like-count-specific. The dossier's dual-reading
"why it won" conclusion (built to hold under either 59 or 114) SURVIVES intact either way, exactly as
designed. **General "current content engages 3.07-3.79%" claim: SURVIVES, but the task's framing
mis-attributed it** — this exact figure does not appear in `ig_nateherkai.md` at all (grepped, no
match); it is handlytech's own claim, for `DZUg7ZxIHLv` (fresh 3,597/117,000 views = 3.07%, exact
match) and `DZChXWoIaHF` (fresh 2,055/54,200 views = 3.79%, exact match). Both numbers are confirmed
accurate as originally stated in `ig_handlytech.md`.

**(f) elevenpercentprod — comments-exceed-likes fingerprint: SURVIVES, CLEAN, control passed.** All
7 reels (not just the requested 2-3) came back MATCH, ratios 1.00x–1.03x — this dossier's methodology
(direct `yt-dlp` `info.json` pulls against the actual IG reel URLs) is validated by this independent
re-pull as fully reliable. The comments-exceed-likes funnel fingerprint is directly confirmed with
fresh numbers, e.g. `DX-bJErPxe7`: 53,171 likes / 61,433 comments.

**(g) Other dossier conclusions checked for wrong-like-count dependency:**
- **`ig_sabrina_ramonov.md`: CLEAN.** 7/7 MATCH (ratios ≤1.01x). This dossier's self-reported
  independent `yt-dlp` cross-check on every video holds up exactly. No engagement-rate, ranking, or
  "Nx" claim (the 16x Video-1-vs-Video-4 gap, the 555x/410x flop deltas, the 3.46%/2.97% comment
  rates) is undermined.
- **`ig_harpercarrollai.md`: the flagged `DZfgPtFObU1` correction (904→33,065, 36.58x) SURVIVES
  fully** — the dossier had already independently caught and used this correct number before this
  remediation ever ran, so no downstream claim needs revision, only the harvest table (§4). **One
  new correction found and applied: `DVbM3sBjl26`** (5,358→7,171, 1.34x) — same situation, dossier
  already had the right number, only the harvest table needed patching. The two "Likes: 3" cases
  (`Dan0IIuJP7K`, `DbD8-40Owbv`) are confirmed hide-like-count artifacts, not harvest defects (§2).
- **`ig_vaibhavsisinty.md`: CLEAN.** 7/7 MATCH. This dossier's WebFetch-based (not `yt-dlp`) cross-
  check independently lands within 1%–4% of today's `yt-dlp` pull on every reel — third-method
  triangulation confirms both the dossier and the original harvest table were fine for this account.
- **`ig_thevarunmayya.md`: CLEAN.** 10/10 MATCH, including all 4 reels the critic's original sample
  never touched (`DExE3UOhUoq`, `DY_5MHRBLNs`, `DaYIYk3BJM9`, and a re-check of `C7CPlnDLW9W`). The
  "10-15x organic-vs-ad gap" claim SURVIVES-WEAKENED: recomputed range is actually 5.6x–15.3x across
  the 5 organic top performers (median ≈9.5x), so "10-15x" describes the top end of the range, not a
  flat multiplier — worth a parenthetical nuance, not a retraction. The like-rate-normalized version
  of the claim (organic 5.7%-6.9%, minus one 2.09% outlier, vs. flops at 2.1%-2.4%) reproduces the
  dossier's numbers essentially exactly and is unaffected.
- **Trio `nick_saraev` section: `DYWXwAmPdIr` anomaly CONFIRMED at 1.69x** (987→1,670) — matches the
  original critic's spot-check almost exactly. This reel sits only in the harvest file's own
  "Anomaly re-verification" section (not in the dossier's own 4-video sample), so no dossier
  conclusion is affected, but the harvest file's "CONFIRMED, not a metrics-sync error" note for this
  reel is itself wrong and needed correcting (§4) — it's a second independent illustration that
  repeat-pulling the same broken tool cannot catch this bug. No other Saraev reel diverged.
- **Trio `ai_ankitarora` section: CLEAN, first full audit pass.** 7/7 MATCH, including the 4 reels
  the dossier built its own analysis on and the 3 harvest-only reels never independently re-checked
  before. No conclusions in this section rest on a wrong like count; this account passes Gate C
  remediation with zero numeric corrections required.

---

## 4. Files patched

Append-only `## GATE C CORRECTION (2026-07-25)` sections were added to every `ig_harvest/*.md` and
`creators/ig_*.md` file with at least one DRIFT or WRONG reel, per `QC_PROTOCOL.md`'s no-silent-
rewrite rule. No original analysis prose was altered or deleted; superseded in-file claims are noted
inline with the correction, not rewritten in place. `ig_harvest/00_INDEX.md` rows were updated with
struck-through/parenthesized old values alongside the correction. `synthesis/00_INTERIM_convergences.md`
was intentionally NOT touched (owned by the orchestrator per task scope).

Patched:
- `ig_harvest/sebastien.md` (3 WRONG: DaAlMicsiBD, DVylvZbDGTo, DYSWrorMzBA)
- `ig_harvest/tiffintech.md` (2 WRONG: DaNk7iTRewN, DW31ssREcbj; 1 DRIFT: Da5aQ8zRXTI)
- `ig_harvest/networkchuck.md` (1 WRONG: DYAmkc-FTUY; 1 DRIFT: DZyLjFWCX_G)
- `ig_harvest/kallaway.md` (2 WRONG: DVhB8rMjp1m, DXSDF9djpRD; 1 DRIFT: DY7GAsGuwGr)
- `ig_harvest/handlytech.md` (1 DRIFT: DZozx8UoTDy, 59→114)
- `ig_harvest/harpercarrollai.md` (1 WRONG: DZfgPtFObU1; 1 DRIFT: DVbM3sBjl26 — new finding)
- `ig_harvest/nateherkai.md` (1 WRONG: DZ76SSujumB — new finding)
- `ig_harvest/nick_saraev.md` (1 DRIFT: DYWXwAmPdIr, correcting its own "CONFIRMED" anomaly note)
- `ig_harvest/100xengineers.md` (1 DRIFT: CyWFEsDyJsC, noted as likely accrual not a defect)
- `creators/ig_sebastien.md` (Video 1/2/3 like-rate claims corrected)
- `creators/ig_tiffintech.md` (Video 6/7 like-rate claims corrected)
- `ig_harvest/00_INDEX.md` (tiffintech, kallaway, networkchuck, handlytech, nick_saraev rows updated)

Not patched (CLEAN, no corrections needed): `ig_harvest/elevenpercentprod.md`, `ig_harvest/thevarunmayya.md`,
`ig_harvest/sabrina_ramonov.md`, `ig_harvest/vaibhavsisinty.md`, `ig_harvest/ai_ankitarora.md`,
`creators/ig_elevenpercentprod.md`, `creators/ig_nateherkai.md`, `creators/ig_handlytech.md`,
`creators/ig_harpercarrollai.md`, `creators/ig_thevarunmayya.md`, `creators/ig_sabrina_ramonov.md`,
`creators/ig_vaibhavsisinty.md`, `creators/ig_trio_kallaway_saraev_ankitarora.md` (all reels the
trio dossier's own text cites were already independently `yt-dlp`-verified or MATCH).

## UNVERIFIABLE

None. All 110 enumerated reels were successfully re-pulled.
