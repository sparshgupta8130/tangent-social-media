# 002 · Labs Writing "key highlights" carousels (IG)

Status: DRAFT for Sparsh's review. Not gated yet (no G2/G3, no SHIP). Created 2026-11-13.

Ask (Sparsh, 2026-11-13): one short "key highlights" carousel per published Labs post, at most 5 images,
plus a 6th "follow for more" with Instagram, YouTube and the Labs Writing section. Square (1080×1080), as
Sparsh asked for the Panditji carousel.

Round 1 (one shared template for all three) rejected by Sparsh 2026-11-13: "Don't templatize these carousels. Each
carousel should be the best representation of the corresponding post." Round 2: three separate designs.

| Post | Design idea | Signature visuals |
|---|---|---|
| deterministic-logic-first (Panditji) | a night sky: the post is astronomy done exactly | Saturn between two zodiac rings; the 24° offset drawn; phone-computes / model-explains; 1″, a 28-dot grid (27 exact, one 6 s), the 11-day error on a line; 427 prompts as a dot field (113 ordinary in green) |
| model-first-code-second (Pai-Pai) | an audit file, in Pai-Pai's own paper and green | a v1 report with a "TOO GOOD?" stamp; Exhibits A-D incl. commit c7ea64e; the rebuild with real notes from the post; a slope chart of the same readers on both tests (exact match); the real Pai-Pai expense card |
| single-fast-model-vs-ensemble (Pai-Pai) | a lab notebook on graph paper: the post is a run of experiments | cost-vs-accuracy scatter (log $), the voting diagram, a forest plot of each prompt change with its 95% interval, the four gates with "asha gave me 1000" / "riya paid 500", held-out dumbbells |

Shared on purpose: square 1080×1080, Fraunces headlines (the brand's display face), slide 6 links (Writing, Instagram,
YouTube) with each post's own closing line. Files: `out/<slug>/<slug>-01.png … -06.png`; source `src/<slug>.html`
(render: `node src/render.js src/<slug>.html out/<slug> 1 <slug>`). Every number is from the post in
tangent-sites/writing/<slug>.md; the 28-dot grid and the 427-dot field are drawn to the post's counts.

## Captions (drafts)

### 1. deterministic-logic-first
```
My astrology guide's AI kept moving Saturn between signs. So I took the maths away from it.

The phone computes every position; the model only explains numbers it is handed, and shows which ones it used. Checked against NASA JPL, the Swiss Ephemeris and a published almanac, the testing even caught an 11-day error an AI-written commit had added.

Full post: labs.tangentideas.ai/writing (link in bio). Carousel made with Claude.

#ai #llm #astrology #softwareengineering
```

### 2. model-first-code-second
```
My hand-written expense parser beat the AI models 88% to 66%. Then I audited the test, and the result flipped.

The coding agents had built the parser and its test together. Rebuilt from 3,000 ground-truth scenarios and 18,000 blind sentences, the parser fell to 36%. Model first, phone checks second: 84.4%.

Full post: labs.tangentideas.ai/writing (link in bio). Carousel made with Claude.

#ai #llm #benchmarks #softwareengineering
```

### 3. single-fast-model-vs-ensemble
```
One fast model beat a three-model ensemble at one-tenth the cost. Here's what moved the needle.

Voting models asked needless questions, and every model called itself "high" confidence even when wrong. Worked examples and a four-step decision order took one model from 65.3% to 84.4% on 7,588 unseen sentences, at $0.44 per 1,000 calls.

Full post: labs.tangentideas.ai/writing (link in bio). Carousel made with Claude.

#ai #llm #promptengineering #softwareengineering
```
Each first line is under 125 characters (the part shown before "more").

## Notes
- "22 blind AI personas" is said explicitly (post 2): the sentence writers were model personas, not people.
- Bio link: these carousels say "link in bio"; the bio's links should include labs.tangentideas.ai/writing
  (or tangentideas.ai, which links to Labs) while they run.
