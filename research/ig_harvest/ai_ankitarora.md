# ai_ankitarora — Instagram Harvest

[OBSERVED] Harvest date: 2026-07-25 — DEEP-DIVE NOMINEE

## Handle disambiguation
Two "Ankit Arora" accounts exist:
- **@ai_ankitarora** — 736K followers (og:description) / 735K (header), 619/591 following, 391 posts. Bio: "AI can't replace you if you follow this page". **Larger account, treated as primary.**
- **@aiwithankit** — 130K followers (og:description) / 129K (header), 55 following, 194 posts. Bio: "AI Decoded | Trends, News and Insights / Simplifying Tech for you / Want to master AI videos? DM me"
- Neither bio explicitly declares the other as a "main account" (unlike the sebastien/sebastienjefferies pair), but @ai_ankitarora has ~5.7x the followers — treated as primary per the task's disambiguation instruction. Full reels harvest + detail pulls performed on **@ai_ankitarora** only; @aiwithankit profile-only noted separately (see aiwithankit.md).

## Profile (@ai_ankitarora)
- og:description: "736K Followers, 619 Following, 391 Posts - See Instagram photos and videos from Ankit Arora (@ai_ankitarora)"
- Header: "735K followers / 591 following / AI can't replace you if you follow this page / Contact: aiankitarora@gmail.com / linktr.ee/aiankitarora and 1 more"

## Reels grid (deduped, 48 tiles collected via scrolling)

Position | Shortcode | Views
---|---|---
1 | DbJPZVpgC7B | 151K
2 | Da5kwxTgfUm | 28.4K
3 | Da0Q9Y3gxBr | 18.5K
4 | Dafiy_OgPZe | 25.8K
5 | DadFXN7Bfsu | 37.3K
6 | DaVlIO0gQNG | 101K
7 | DaQdAwOAQ9v | 43.6K
8 | DaBGaQQBkCH | 115K
9 | DZ-c-kEg5WT | 24.5K
10 | DZ8BB9wg4_B | 71.1K
11 | DZxPjfsggLi | 60.8K
12 | DZdBstHgQUt | 77K
13 | DZZNWxYgudg | 30.8K
14 | DZW54kMA-fg | 66.8K
15 | DY_3d4XAl36 | 122K
16 | DY9GrUpgheY | 35.7K
17 | DYwcHbjgsJV | 38K
18 | DYAiwoko7BG | 245K
19 | DX_PAZlIeSD | 59K
20 | DX0o-wxT-YP | 445K
21 | DXq9NZnCH84 | 223K
22 | DXou4WcgQ2W | 64.6K
23 | DXWD6RogPf0 | 172K
24 | DXgha6OiEfL | 31.3K
25 | DXcOp8-iFyZ | 111K
26 | DXI-E02EiNy | 76.5K
27 | DW8GX4qCE75 | 41K
28 | DW06azLCNBw | 378K
29 | DWvc-1bCO3Z | 234K
30 | DWrCiLyiI4U | 42.9K
31 | DWjqpgUCFA2 | 149K
32 | DWeJnqVD20h | 217K
33 | DWRkb-MiErx | 793K
34 | DWHHWVdCPAo | 106K
35 | DWEo_SCiD3M | 56K
36 | DV_FSjBCB9O | 5.5M (mid-grid outlier — see pinned-flag note)
37 | DV707PciHfD | 1M
38 | DV1R_QniKuK | 45.6K
39 | DV0Hg6RCJFS | 49.8K
40 | DVwEA36iN92 | 39.1K
41 | DVln9Gtuzbg | 107K
42 | DViRW9MjUBT | 53.2K
43 | DVQeWYsgQMc | 31.4K
44 | DVL5HFSCK_K | 263K
45 | DVECTFmCCb6 | 30.1K
46 | DVBYyJVCOJK | 61.9K
47 | DUyLi_6gCxK | 69.6K
48 | DUtFBncAA9I | 105K

**Pinned-flag note**: CONFIRMED NOT PINNED. Position 36 (DV_FSjBCB9O, 5.5M) is dated March 17, 2026, consistent with its chronological neighbors (position 37 is Mar 15, 2026) — a genuine organic viral hit, not a pin.

## Computed stats
- **Median views (30 most recent tiles, positions 1-30)**: 65.7K (avg of sorted 15th/16th: 64.6K, 66.8K)
- **Top 5**: DV_FSjBCB9O 5.5M, DV707PciHfD 1M, DWRkb-MiErx 793K, DX0o-wxT-YP 445K, DW06azLCNBw 378K
- **Bottom 2 flops (excluding 3 most recent tiles)**: DZ-c-kEg5WT 24.5K, Dafiy_OgPZe 25.8K
- **Top/median ratio**: 5.5M / 65.7K ≈ 83.7x
- **Median-views-to-followers ratio**: 65.7K / 735K ≈ 8.9%

## Reel-detail pulls (deep-dive nominee — required by spec)

| Shortcode | Views | Likes | Comments | Date | Caption hook |
|---|---|---|---|---|---|
| DV_FSjBCB9O | 5.5M | 154K | 34K | Mar 17, 2026 | "Comment 'prompt' and I'll send you this entire system" — Claude CoWorks podcast-automation-agency prompt, strong like-rate (~2.8%) |
| DV707PciHfD | 1M | 34K | 86K | Mar 15, 2026 | "Comment 'PROMPT' and I'll send you the link" — "Your AI is lying to you" hook, posted 2 days before the 5.5M hit, comments MASSIVELY exceed likes (86K vs 34K) |
| DWRkb-MiErx | 793K | 31K | 421 | Mar 24, 2026 | "Share this reel!!!" — Claude Computer Use feature announcement, share-CTA rather than comment-CTA, very low comment count relative to likes/views |
| DX0o-wxT-YP | 445K | 2,807 | 2,135 | May 1, 2026 | "Comment 'PROMPT' and I'll send you the link!" — terse, no context, notably lower like-rate (~0.6%) than the March top performers |
| DW06azLCNBw | 378K | 5,623 | 2,523 | Apr 7, 2026 | "Comment 'CHINA' and I'll send you the link" — Seedance 2.0/OpenArt AI video model demo, sponsored-adjacent (product plug) |
| DZ-c-kEg5WT | 24.5K (flop) | 384 | 52 | Jun 24, 2026 | "Comment 'CLAUDE' and I'll send you the link" — same hook family as the top performers, but flopped |
| Dafiy_OgPZe | 25.8K (flop) | 332 | 258 | Jul 7, 2026 | "Comment 'FABLE' and I'll send you the link" — same terse hook style, also flopped |

**Pattern note**: This account's biggest hits (5.5M, 1M) both landed within a tight 2-day window in mid-March 2026 with substantive captions (a full automation-agency prompt, an "AI is lying to you" narrative) — not just the terse "comment X" hook alone, which is also used on both flops. The account appears to have had a viral peak in March 2026 that hasn't been repeated since; by May-July 2026 even top reels (445K, and the two 24-25K flops) show meaningfully lower engagement rates, suggesting a possible declining-momentum trend worth flagging for anyone evaluating this account's current (mid-2026) trajectory rather than its historical peak.
