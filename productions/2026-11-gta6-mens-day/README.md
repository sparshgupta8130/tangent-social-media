# Men's Day x GTA 6 posters (IG carousel, 1:1, 19 Nov 2026)

**Request (Sparsh, 2026-11-19):** "DUDE!! GTA 6 is being released today on Nov 19!! Can we use
that as an element in this work somehow?? Or perhaps a different post". This led to the idea list
in the Museum of Men chat. Sparsh liked A-E and chose one carousel for the feed plus a Stories
drip ("yes go ahead").

Made with `/post`. Posts 6-8 h after the Museum of Men carousel.

| File | What |
|---|---|
| `message-brief.md` | Message, arc, look, IP limits, sourced facts |
| `carousel.md` | Copy and caption |
| `image-prompts.md` | Nano Banana prompts (7 images) |
| `lint.txt` | clarity_lint (0 FAIL) |

## Decision log
- 2026-11-19: Sparsh: the GTA-poster *style* is fine, like the Ghibli trend. Showrunner's limits:
  - no Rockstar logo, "VI" lettering, font or characters;
  - no copied art or exact game screens;
  - no weapons or violence;
  - "Not affiliated with Rockstar Games" in the caption.
- 2026-11-19: "Exhibit 9" framing dropped for the feed (post order isn't fixed). It is fine in
  Stories.
- 2026-11-19: order is cover → cheat code → second life/check-up → main characters → Vice City
  boys → missions → maker card.
- Gift voucher (3) and reserved couch (6) are parked for a weekend follow-up.

## Status
Copy linted. Image session and cold read running.
- 2026-11-19: images landed (session_01ETPVMNaYJvUyTDvD8Uz5Ko; provenance in `assets/gen/README.md`).
  Slides v1 rendered with `build.mjs` → `slides/` (Anton + Inter type, our own).
- 2026-11-19: Sparsh: the style is close to GTA but the drawing could be better, "more straight
  line strokes". The current images use sketchy comic hatching and wobbly ink. A style test is
  running on 2 images × 3 cleaner styles (`assets/style-test/`) before a full regeneration.
- 2026-11-19: Sparsh: the cover "sucks" and every title is too verbose, so the carousel reads
  like a flat slide deck. v2 copy (`carousel.md`; v1 kept as `carousel-v1.md`):
  - one short line per poster, in game language (respawn, NPCs, level, press Start);
  - counter chips dropped;
  - end card made self-aware.
  Lint 0 FAIL; v2 cold read running.
- 2026-11-19: Sparsh: no explanation line under LEAVEMEALONE on slide 2. Removed; the caption
  still explains it.
