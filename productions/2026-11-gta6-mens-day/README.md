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
- 2026-11-19: style test → Sparsh picked **S2 "geometric poster"**. `image-prompts.md` BASE was
  updated, and image 2's lungi became pyjama shorts (the model never drew a lungi). Full redraw
  is running.
- 2026-11-19: Sparsh stopped the S2 redraw and shared 6 brand GTA-6 posts (BK, Dunkin', KFC,
  Rapido, Axe via exchange4media; Haldiram's) as the target look. The analysis is in
  `STYLE-REFERENCE.md`. The S2 session (session_01ETPVMPkzdHmWug71rrty2F) was interrupted.
  - Prompts are now v3: semi-realistic key-art, clean lines, cel and airbrush shading, rim light,
    violet sunset, wet reflections, a Marine Drive-style coast.
  - The cover became a three-men key-art shot.
  - Not copied: the GTA logo and font, the bandana couple (GTA VI's leads), brand logos.
- 2026-11-19: v3 key-art images landed (session_01ETPVMPQ62xUQ4kXWnZYX7j; `assets/gen-v3/README.md`).
  Slides re-rendered with v2 copy → `slides/`. Weak spots, per the image session and the Showrunner:
  - the img-02 face leans cartoon;
  - the img-05 boy has big cartoon eyes;
  - img-03's top band is wall plus window, not sky.
- 2026-11-19: Sparsh: regenerate slides 2 and 5, then upload to Post 7.
  - Regen session: session_01ETPVMPmryYn8kMYyniWtki → `assets/gen-v3b/`.
  - Drive Post 7 (1YCmknRLuqMvpSy3lzrFW-QyN_TRnsSIR): slide-01, 03, 04, 06, 07 and caption.txt
    are uploaded. Slides 02 and 05 follow after the regen.
- 2026-11-19: **First-time reader (Sparsh's wife) failed v2.** It read as "a random set of
  images", with no connection between slides and no hint that each slide is a separate pun; the
  check-up slide in the middle made no sense. A real reader's verdict beats the AI cold-read PASS
  (cold-read skill rule). Sparsh asked for a rethink.
  - Proposed: A, one man's life told through three GTA releases (Vice City → GTA V → GTA 6) as a
    single story (recommended); B, "If a man's life were GTA" with game mechanics; C, a single
    image (the voucher or the couch). Waiting on Sparsh.
  - Verified release years: GTA V on 17 Sep 2013 (Giant Bomb release list; HEXUS); Vice City on
    PC in May 2003. GTA IV's year was not verified, so it is not used.
- 2026-11-19: Sparsh asked for final outputs of BOTH A and B, set in GTA's font as other brands
  did.
  - Font: Pricedown Black. Typodermic's free desktop licence covers advertising and rendered
    graphics but not sharing font files (per a web search, 2026-11-19; the build session
    verifies the bundled licence). So the font is downloaded at build time and git-ignored,
    never committed.
  - Still not used: the GTA logo or "grand theft" wordmark, characters, brand logos.
  - Copy: `optA/carousel.md` and `optB/carousel.md` (lint 0 FAIL each). Two build sessions
    produce images and slides; a cold read runs on both.
- 2026-11-19: Option A slides landed (session_01ETPVMNAgrWUka4sohQFQn4, Pricedown via Typodermic's
  free desktop pack; EULA v260817 §2.2 permits rendered images).
  - Licence caveat from that session: §2.1 ties install to a personal "Workstation", and the
    render ran in a cloud container. For the cleanest compliance Sparsh can re-render on his own
    laptop.
- Option B landed in Anton (session_01ETPVMNND9cfbvARXBJ5N6g could not download the font: 406)
  and still had the old slide-3 line. The A session was asked to re-render B in Pricedown with
  "Resting doesn't fix it."
- 2026-11-19: Option B re-rendered in Pricedown with "Resting doesn't fix it." (commit a0b9c37,
  by the Option A session). Both A and B are final, waiting on Sparsh's pick and his wife's read.
- 2026-11-19: **Sparsh picked Option B.** Drive Post 7: the 5 void v2 slides and the old caption
  were moved to Drive trash. The 8 Option B slides and the B caption.txt were uploaded (sizes
  match local).
- 2026-11-19: post order: the Showrunner recommends Post 7 (GTA) first, in the IST morning, and
  Post 6 (Museum) in the evening. This flips the earlier plan; reasons in chat. There is no
  own-data on best times yet (benchmarks empty).
