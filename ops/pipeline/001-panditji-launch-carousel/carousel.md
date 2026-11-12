# 001 · Panditji launch carousel (IG) + profile bio

Status: DRAFT for Sparsh's review (INTERACTIVE). Not gated yet: no G2, no G3, no SHIP.
Created 2026-11-12.

## Ask (Sparsh, 2026-11-12)
A carousel that is fun to follow, tells people about Panditji, asks them to install it from
panditji-seven.vercel.app, and ends on "follow tangentideas.ai / link in bio". Plus a bio for
@tangentideas.ai in the spirit of @travelandleisure.

## Files
- `carousel/out/panditji-01.png` … `panditji-11.png`: 1080×1350 (4:5), upload in this order.
- `carousel/src/slides.html`: source. Re-render: `node carousel/src/render.js carousel/src/slides.html carousel/out`.
- Screens are the real app's screenshots from `tangent-sites/labs/assets/panditji/` (sample user "Asha",
  labelled "sample profile" on every phone slide).

## Slide copy (every claim sourced from the owner-approved Labs page, labs.tangentideas.ai/panditji)
1. Cover. "Every family had someone to ask." / When to travel, when to sign the lease, when to begin something new. / Meet Panditji · Swipe
2. पंडितजी · pun-dith-jee · A learned person a family trusts and turns to. / "Many of us now live far from the Panditji we grew up with." / So I built one for your phone: an astrology app with an AI guide that reads your chart and answers your questions, any time of day. / "Here's what it does for you →"
3. What it does · 1 of 4: "It reads your day, in plain words." + Today screen.
4. What it does · 2 of 4: "It finds good hours to begin, and ones to avoid." + Timing screen (day strip, starred Wednesday, day dial).
5. What it does · 3 of 4: "It answers your questions, from your own chart." Ask about work, marriage or a move in your own words.
6. What it does · 4 of 4: "Vedic or Western, it reads your chart your way." Two phones side by side, same sample profile: Vedic kundli (Labs screenshot) and Western birth chart (shot 2026-11-12 from a local build of panditji main, `img/chart-western.webp`).
6b → slide 7 (added round 4, 2026-11-12, Sparsh: "no slide on compatibility match"). What it does · Match: "It matches two charts for marriage, verdict first." Pick any two people you've saved; Vedic = 36-point Gun Milan, Western = how the two charts meet. Real Match screen (Asha + Rohan fixture, Vedic) shot from a local build of panditji main; Western synastry shot saved as `img/match-western.webp`, unused.
Slides 7-10 below are now 8-11.
7. It knows when to say no: "It won't tell you when you'll die. Or which coin will 10x." + the real refusal screen.
8. How it works: "The AI isn't allowed to guess." Phone does the maths (checked vs NASA JPL, Swiss Ephemeris, Drik Panchang) · the AI only explains it and can be wrong · your chart stays on your phone, no ads.
9. Get it: "Free. No app store needed." panditji-seven.vercel.app · Safari/Chrome · Add to Home Screen / Install app · Get a code by email · open in your browser, not inside Instagram · 18+.
10. Tangent mark · "Small AI apps for the small problems of everyday life." · Follow @tangentideas.ai for the next one · Link in bio.

Story shape: a relatable gap (1-2) → four things it does, each one screen (3-6) → the shareable twist (7)
→ why you can trust it, which is also the AI disclosure (8) → how to get it (9) → follow (10).

## Caption (draft)
```
Many families once had a Panditji to ask when to travel or when to begin. I built one for your phone, with an AI guide.

It reads your day, finds good hours to begin, matches two charts for marriage and answers your questions. Your phone works out the chart from real astronomy; the AI only puts it into words, and it turns down questions about death, health and money.

Install it free at panditji-seven.vercel.app (link in bio). Open it in Safari or Chrome rather than inside Instagram, then add it to your home screen. Your access code arrives by email in about a minute.

No ads, nothing for sale. Adults 18+. English and हिंदी, Vedic or Western.

#astrology #vedicastrology #kundli #panchang #jyotish
```
First line = 119 chars, so the hook and the AI disclosure both show before "more".
The kit's `instagram_caption` disclosure line (names Claude + the critic) is written for photo edits;
it does not describe how this app works, so it is deliberately not used here.

## Bio (draft, Instagram limit 150 chars)
Round 1 (lists "AI apps" + "photographs") rejected by Sparsh 2026-11-12: jarring; don't call out the
verticals, borrow the general definition of a tangent from the hub (tangentideas.ai) instead.

Round 2 rejected 2026-11-12: too abstract, reads like a maths definition; must say how it relates to
Sparsh and carry the official tangentideas.ai link.

Round 3, recommended (146 chars), builds on the hub's own opening ("AI, off the clock."):
```
AI, off the clock.
I'm Sparsh. Every project here is a tangent: an idea that slipped out of my daily routine and went its own way.
New: Panditji ↓
```
Alternatives: (137) "I'm Sparsh. Life runs in a circle: work, sleep, repeat. / These are my tangents, ideas I follow with AI
wherever they lead. / New: Panditji ↓" · (120) "AI, off the clock. / I'm Sparsh, and I follow my curiosity with AI.
Each idea that gets made is a tangent. / New: Panditji ↓"
Links field: 1) https://tangentideas.ai titled "Tangent Ideas" 2) https://panditji-seven.vercel.app titled
"Panditji, free astrology app". Day job deliberately left out (tangent-sites rule: it appears only on the hub).
Slide headers round 3: "What it does · Today / Good times / Ask / Your chart" (Sparsh disliked "n of 4").

Round 2 drafts (rejected), kept for the record (144 chars):
```
A tangent touches a circle at one point, then goes its own way.
Everyday life is the circle. These are the ideas that leave it.
New: Panditji ↓
```
Alternatives:
- (127) "Everyday life is a circle, left a little open so new ideas can get in. / This is where they set off on their own. / New: Panditji ↓"
- (132) "Work, sleep, repeat: that's the circle. / A tangent touches it once and sets off on its own. / Here's where my ideas go. / New: Panditji ↓"
Name field (searchable, separate from the bio): "Tangent Ideas · Sparsh Gupta".
Links (IG allows up to 5): 1) panditji-seven.vercel.app titled "Panditji, free astrology app";
2) tangentideas.ai. Do NOT link tangent.gallery (retired per tangent-sites/CLAUDE.md; the bio drafts in
`knowledge/brand/tangent-voice.md` still point there and are stale).

## Round 1 feedback (Sparsh, 2026-11-12), all taken
- Slide 2 "phone number" line and "doesn't replace him / keeps you company" were confusing → rewritten.
- 2→3 jump into screenshots had no setup → bridge line on slide 2 + "What it does · n of 4" kickers on 3-6.
- Slide 5 "tap one to see the numbers" confusing → removed.
- Slide 6 languages irrelevant and Vedic-only → Vedic + Western side by side, "your way" headline.

## Decisions + open questions
- Frame is the dark Tangent world (sites palette #100f0d / #ece7de, Fraunces + Inter); the app keeps its
  own cream colours inside the phones, same rule as Labs. Accent = Panditji's saffron, taken from the app.
- 4:5 portrait, not 1:1: takes more feed height.
- Travel + Leisure's current bio could not be fetched from this environment (Instagram blocks it); the
  drafts follow the publisher pattern (one-line promise, what you'll find, a pointer to the link), not its text.
- Risk: sign-ups have a daily cap (Labs page). A post that lands could hit "full, try tomorrow".
- Gates still owed before posting: G2 critique + G3 brand review (non-negotiable 7), then Sparsh's SHIP.
  The `app` vertical has no craft pack yet, so the critic would grade on the general lenses.

## Round 5 (2026-11-12): square
Sparsh asked for 1:1 so the carousel doesn't need the crop toggle. Square set: `carousel/out-square/`
(source `carousel/src/slides-square.html` = the 4:5 source + a square override block; screenshot slides go
two-column, text left / phone right). The 4:5 set stays in `carousel/out/`. Trade-off flagged: square is ~20%
shorter in feed than 4:5, and the 3:4 profile grid trims a square cover's sides. Note for next time: the
carousel ratio is set once by the crop toggle on the first image and applies to every slide.
