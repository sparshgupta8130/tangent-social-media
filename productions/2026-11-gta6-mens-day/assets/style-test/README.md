# Style test: cleaner, straight-line drawing (img-02, img-05)

- **Why:** the art director said the current set (`../gen/contact-sheet.jpg`) feels sketchy: scratchy hatching, wobbly inked strokes, painterly texture. He asked for cleaner drawing with more straight-line strokes. This is a test, not the final.
- **Model/API:** `gemini-3-pro-image`, `generateContent`. Config: `responseModalities: [IMAGE]`, `imageConfig: {aspectRatio: "1:1", imageSize: "2K"}`. This is the same approach as `../gen/README.md`. Saved as JPEG q88 at 2048 px. Date: 2026-11-18. Run by Claude (Showrunner session), autonomous mode for this one task only.
- **Files:** `S{1,2,3}-img-0{2,5}-cK.jpg` holds every candidate, rejects included. `contact-sheet.jpg` has one row per style, with the best img-05 and img-02 in each row.
- **Disclosure:** fully AI-generated. No photo or third-party image was used as input.

## Prompt construction

Each prompt has five parts in this order: **STYLE** (replaces BASE's first sentence) + **PALETTE** + **REST OF BASE** (unchanged) + **SUBJECT**. Round 2 also adds **EXTRA**.

BASE's first sentence also carried the palette, poses and sky. I kept those as PALETTE and changed "painted gradient sky" to "smooth gradient sky", because "painted" pulls toward the painterly texture we are trying to drop.

**STYLE**
- S1 crisp vector: `Clean digital vector illustration like premium open-world game loading-screen art: crisp confident straight-edged linework of uniform weight, flat colour planes with hard-edged cel shadows, sharp angular highlights, no hatching, no cross-hatching, no sketch lines, no brush or paper texture.`
- S2 geometric poster: `Bold graphic poster illustration built from straight lines and angular geometric shapes, faceted planes of flat colour, minimal crisp outlines, strong silhouettes, no hatching, no texture, no curvy sketchy strokes.`
- S3 ligne claire: `Ligne claire comic style: clean uniform black outlines drawn with steady straight strokes, flat bright colours, no hatching, no shading texture, very tidy and precise.`

**PALETTE:** `Saturated sunset palette (orange, magenta, teal), dramatic but friendly poses, smooth gradient sky.`

**REST OF BASE:** `Set in present-day urban India with realistic Indian people, clothes and streets. Square composition, the top 30% is open sky or plain background. ABSOLUTELY NO text, letters, numbers, logos, game logos, signage, watermarks or UI. No weapons, no guns, no violence, no police chases, no real or famous people, no characters from any existing game.`

**SUBJECT:** these are the exact subject lines behind the current picks in `../gen/README.md`.
- img-02: the FULL-BLEED line followed by the refined lungi line (`One single continuous full-bleed illustration from edge to edge: no border, no frame, no separate sky panel, no comic panels. A relaxed Indian man in his 30s wearing a white sleeveless banian and a traditional South Indian checked lungi: one single tube of cotton cloth wrapped around the waist like a long skirt, with a visible tucked knot at the waist and NO separation between the legs (it is not trousers and not shorts), reaching down to his ankles, bare feet. He lounges back on a red plastic chair on a rooftop terrace at sunset, legs stretched out and crossed at the ankles, holding a game controller, eyes closed with a smug peaceful smile, a small glass of chai on a stool beside him, water tank and clothesline behind. The upper 30% of the frame is open sunset sky.`)
- img-05: the spec line, unchanged (`A split poster with a vertical divide. LEFT: a 12-year-old Indian boy in a cramped 2000s cyber café, glowing old CRT monitor and beige PC, hand on the keyboard, excited face. RIGHT: the same man now in his mid-30s on a living-room sofa, office ID lanyard still on, a sleeping baby on his shoulder, game controller in one hand, tired but happy smile. Same face, clearly the same person.`)

**EXTRA** (added in round 2 only): `No border, no frame or outline around the edge of the image; the artwork runs to all four edges. Any screens show only abstract colour shapes, no words.`

## Rounds

- **Round 1** (c1-c2, 12 images):
  - All S1 candidates were usable.
  - S2-02-c2 has a white border.
  - S2-05-c1 has no open sky at the top.
  - Every S3 candidate draws comic-panel frames.
  - S3-05-c1 has legible "PAUSE" menu text on the TV, so it was rejected.
- **Round 2** (+EXTRA; S2-02-c3, S2-05-c3, S3-02-c3/c4, S3-05-c3/c4):
  - S2-02-c3 is full-bleed, but the lungi reads as shorts.
  - S2-05-c3 still has a white border.
  - S3-02-c4 is near full-bleed (a thin edge line).
  - S3-05-c3/c4 still draw panel frames and gutters, but their screens are abstract (no text).
  - I stopped there. A border isn't a reject reason for this test, and the frames are a trait of the style, so another round wouldn't settle it.
- **Checks on the picks:** I cropped the lower 70% of each pick and looked at it. No legible text, logos, or bad faces or hands. ID cards show only blank photo shapes.

## Picks (contact sheet)

| Style | img-05 | img-02 |
|---|---|---|
| S1 | c2 | c1 |
| S2 | c2 | c1 |
| S3 | c3 | c4 |

## Verdict (one line each, honest)

- **S1 crisp vector:** the hatching and texture are gone. The lines are clean, even-weight, cel-shaded, and the set stays closest to the current look and palette. The drawing leans toward a generic clean cartoon rather than "straight-line", and the lungi still drapes like pyjamas. **Safest swap.**
- **S2 geometric poster:** this answers "more straight-line strokes" most literally. Faceted angular planes, hard-edged shadows, strong poster silhouettes, and the most distinctive and graphic of the three. It is less GTA-loading-screen and more flat poster. Faces get a little angular or stiff. 1 of 3 img-02 candidates had a border and 2 of 3 img-05 candidates broke the layout.
- **S3 ligne claire:** the tidiest and most legible linework, but it reads as a newspaper or webcomic. All 8 candidates had comic-panel borders or frames (S3-02-c4 only a thin edge line), even when told not to, and once put readable UI text on a TV. **Least suited**: it would need cropping and more rounds.
- **Common to all three:** the lungi problem from `../gen/README.md` persists. Every style draws checked pyjama-like legs, with a waist knot at best.
