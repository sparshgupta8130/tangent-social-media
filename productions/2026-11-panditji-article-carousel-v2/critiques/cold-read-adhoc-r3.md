# Cold read, round 3 (phase adhoc, on the copy): verdict and escalation

One-line message: "I built a free astrology app where the AI can't make up where the planets are."
Audience: A+B. These are fresh readers who never saw rounds 1 or 2.

## Meaning (a): both match
- A: "A guy made a free astrology app where the app itself calculates the planet positions
  (checked against NASA) and the AI just explains them, so you don't get different answers each
  time."
- B: "A guy built a free astrology app where code calculates the planet positions, checked
  against NASA data, and the AI only explains them, because plain chatbots gave inconsistent
  answers."

## Cover (b): both PASS
A said "YES, but only just". B said "YES".

## Voice (d): both PASS
Both said "a person talking to me". A said slides 3 and 5 feel "slightly like a presentation,
but not badly". B said slide 5's "They match" leans slightly toward a demo.

## Confusions (c), classified

| Persona | Slide | Phrase | Guess | Class |
|---|---|---|---|---|
| A | 2 body | "signs" | zodiac signs (correct) | SNAG |
| A | 3 body | "mix up Western and Indian astrology" | two systems that place planets differently (correct) | SNAG |
| A | 5 body | "the planets it used" | a list under each answer (correct) | SNAG |
| A | 6 picture label | "no app store needed" | opens in the browser (correct) | SNAG |
| B | 1 cover body | "Panditji" | the app's name (correct; the slide says so) | SNAG on the cover |
| B | 1 cover headline | "make up where planets are" | the AI guessing positions wrongly (correct) | SNAG on the cover |
| B | 2 body | "signs" | zodiac signs (correct) | SNAG |
| B | 3 body | "Western and Indian astrology" | different zodiac systems (half-guess) | SNAG |
| B | 5 headline | "NASA's planet data" | official planet tables (correct) | SNAG |
| B | 6 | "no app store needed" | a web app (correct) | SNAG |

No MISS anywhere: every flagged phrase was guessed correctly.
- A: 0 on the cover, 4 SNAG (the limit is 3). **FAIL by the letter of the rule.**
- B: 2 SNAG on the cover (the limit is 0), 6 SNAG in total. **FAIL by the letter of the rule.**

## Progress across rounds (same post, a new pair of readers each round)

| | Round 1 (v2) | Round 2 | Round 3 |
|---|---|---|---|
| A would stop | maybe | yes, just | yes |
| A felt like | presentation or lecture | a person talking | a person talking |
| A confusions | 10 (incl. MISS on the cover) | 8 (5 SNAG + 2 MISS) | 4 SNAG, 0 MISS |
| A would act | nothing | save, send to a friend | save, try it, send to his wife |
| The deleted original (for reference) | would not stop, 22 confusions, would leave by slide 4, nothing | | |

## Escalation to Sparsh (the skill allows 3 rounds)

The SNAG limits were set on 2026-11-15, before any real run, and this is their first
calibration. Two questions for Sparsh:
1. **Rule calibration.**
   - Should a proper name that the same slide introduces ("It's called Panditji") count as a
     SNAG? I recommend not.
   - Should body-text SNAGs whose guess is correct be capped at 3, or at 5? I recommend 4 for
     body text, while keeping zero MISS anywhere visible and zero SNAG on cover headlines.
2. **This post.** The four small fixes below are folded into `carousel.md` as round-4
   candidate copy. It has not been cold-read. The real acceptance test is a first-time human
   reader, ideally the same one whose feedback started this, plus `/cold-read` on the rendered
   slides.

Round-4 candidate fixes:
- "signs" becomes "zodiac signs".
- Slide 3 body becomes "...Western and Indian astrology, which put the planets in different
  signs."
- "the planets it used" becomes "which planets it looked at".
- The slide 6 label becomes "Free · works in your browser".

COLD-READ: FAIL
