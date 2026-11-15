# Carousels and still posts: structure and slide grammar

The craft pack for `vertical: carousel` (multi-slide posts and single images on Instagram, and
YouTube community posts). It sits under `knowledge/craft/clarity.md`, which wins on any
wording question. Evidence: `research/clarity-2026-11/` (harvest files and `SYNTHESIS.md`);
counts below come from about 90 still posts read slide by slide.

## The slide grammar

Every slide has the same three parts, in this order of importance:

1. **The headline:** the slide's whole point as one plain sentence. 4 to 12 words (the cover:
   6 to 14). A skimmer who reads only this line gets the message. Never a label ("The fix"),
   never a riddle ("One sky, two ways to count it"), never a fragment ("Tested.").
2. **The picture:** the thing the headline talks about. A real screenshot, the app, the
   photograph, a simple drawing of the action, or one big number with its noun. Labels sit ON
   the picture, next to what they name.
3. **The body (optional):** one or two short sentences of depth for the interested.

Word budgets (headline plus body), from the strong posts in the corpus:

| Slide type | Words | Notes |
|---|---|---|
| Cover | 6 to 14 | The lightest slide in every high-clarity post |
| Story or explainer slide | 12 to 35 | The clear band across all four harvests |
| Glossary or list slide | 2 to 12 | One item, one picture each (the 41.7K-like "12 habits" post) |
| Never | over 45 to 50 | Unless one plain headline leads it and the body is genuinely optional |

`tools/clarity_lint.py` warns over 35 words a slide and fails over 50.

## The cover

The cover is a label, not a mood and not a teaser. A stranger who sees only the cover must be
able to say what the post is about. That is the first-time reader's first rule, and the cover
is what decides whether anyone swipes.

Strong cover shapes from the corpus:
- **Person plus what they made plus what it does:** "This legend built an app to help your
  grandparents not get scammed" (@openai). "Hi, I'm Jacklyn. I built Shelf by JC with AI."
- **A plain, surprising claim:** "The world runs on one tiny chip." (Tiff In Tech)
- **The question people already ask:** "Why AI forgets things." (Harper Carroll)
- **A stake for the reader:** "What a bad day for Nvidia means to you" (Finshots)
- **A number plus a person:** "5 money rules my wife and I follow. We're 45, with two kids."
  (Ankur Warikoo)
- **A list promise:** "5 mistakes that can sink your app." with the five items previewed on
  the cover (Zoof04)

Any intrigue lives inside the plain statement ("I built an astrology app where the AI isn't
allowed to guess"), never in withholding what the post is about.

Show the thing on the cover: the app on a phone, the photograph, or Sparsh. A face adds trust,
and an unknown account needs it.

## Slide 2 stands alone

Instagram may show an unswiped carousel again starting from slide 2 (Mosseri, October 2024).
So slide 2 must also make sense to someone who never saw the cover: name the subject again
("Panditji", "my app") instead of "it".

## Chaining: every post links its slides explicitly

Pick one device and use it on every slide:
- **Story bridges** for "I made a thing" and "what went wrong": Before / Then / So / Now; "But";
  "So I tried". The headlines read as one running story.
- **A counter or step number** for lists and how-tos: "Step 2 of 5", "App 3 of 6", "1." to "5."
- **Anaphora** for one idea seen several ways: "One chip... / One company... / One island..."
- **Question-then-answer headlines** for explainers: "What is it? / Why does it go wrong? /
  What can you do?"
- **A fixed frame** (same layout, same position, same colour) in all cases. It teaches the eye
  where to look.

Progress dots alone are not a chain. The deleted carousel had six unconnected headlines.

## How many slides

As many as the one idea needs, usually 4 to 7. Lists can run 8 to 12 only when every slide is
one short item with one picture. There is no reliable best count in the data, so never pad.
A slide that does not move the one-line message forward gets cut.

## The ending: story close, then Tangent's end slides

The story's last beat ends the story in one of three ways, chosen in the Message Brief:
- the payoff (the last true fact, the result),
- a question the reader can actually answer ("What would you build?"),
- or one next step.

Then come **Tangent's standard end slides**. Sparsh's rule: every carousel has them.
1. **Read or try more (when there is something):** the full article, with its plain place
   ("Read the full story, with every number, on Medium.") and a short, typeable link on the
   slide (medium.com/p/..., labs.tangentideas.ai/...). Add "Link in bio". If there is an app
   to try, add one line for it.
2. **Follow (always):** one plain line ("Follow along for more things I build with AI.") and
   every channel, written in full, one per row with its icon:
   - Instagram @tangentideas.ai
   - YouTube @tangentideasai
   - Medium @tangentideasai
   - tangentideas.ai

The end slides are a brand fixture, so the "one idea" and "one ending" rules don't apply to
them. Keep them plain, large and identical in layout from post to post, so viewers learn them.
Links typed on a slide are fine, because people can type them. Links in the caption are not
clickable, so the caption says "Link in bio" instead.

(Corrected 2026-11-15. An earlier version said "one CTA, never follow-for-more" and dropped
these slides from the Panditji rebuild. Sparsh wants them on every post.)

## Visual rules (Tangent look, plain words)

- **One display line per slide.** Fraunces for the headline, Inter for the body and labels.
  One weight per role. Hierarchy comes from size and position.
- **Contrast you can read on a phone.** Body text is white or near-white on dark, or
  near-black on light. No dim grey or coloured text for anything that must be read. The
  accent colour marks one key word at most. Body text is at least about 28 px on a 1080-wide
  canvas.
- **Light or dark.** Tangent's default is dark. Text-heavy slides may use a light background,
  and that choice is a live test (`strategy/BETS.md`, the first-time reader's "more white,
  less black").
- **Whitespace over shrinking.** If the words do not fit at size, cut words.
- **Safe area.** Use 1080x1350 (4:5) and keep every word inside the central area, so the 3:4
  grid crop keeps it.
- **Real things.** Real screenshots, real before and after, real numbers. No fake dashboards.

## Templates (pick one in the Message Brief)

Each one maps to an arc in `clarity.md`. Example posts are in the harvest files.

**T1. I built it (5 to 6 slides).** Arc 1.
- Slide 1, the cover: "I built [app] to [do what] for [whom]. With AI." The app on a phone,
  or Sparsh.
- Slide 2, Before: "I'm not an app developer. I [hobby or situation]."
- Slide 3, Then: the everyday problem.
- Slide 4, So: what I built, with a real screenshot.
- Slide 5, Now: what it does for you, with one real number.
- Slide 6: link in bio, or a question.

**T2. Use-case ladder (5 to 7 slides).** One app, several things it does.
- Slide 1, the cover: the app plus the promise.
- Slides 2 to 5: one "you can" headline each, with a screenshot and one example sentence
  ("Ask it if Saturday is a good day to move house.").
- Last slide: where to get it.
- This replaces the deck-voice feature list: "You can..." instead of "It finds...".

**T3. Before and after (3 to 6 slides).** Arc 2.
- Slide 1, the cover: the finished photo plus a plain label of what was done.
- Then raw and result side by side, or alternating, with 2 to 4-word labels on the picture
  ("Warmer skin", "Sky brought back").
- Last slide: who decided, and the next one.

**T4. Explain one thing (5 to 6 slides).** Arc 3.
- The question as the cover.
- Then "What is it?", "Why does it matter to you?", one picture or example, and "What you
  can do".
- Define any term on the slide where it first appears, in under 10 words.

**T5. What went wrong, and the fix (5 to 6 slides).** Arc 4. Two-layer.
- A concrete scene, then the plain reason, then the fix, then one proof with its noun, then
  the link to the full story.

**T6. One image, one claim (1 to 2 slides).** A single photograph or result, with no text on
it or one short label, and caption line 1 states the claim plainly. Only when the image
explains itself.

## Checks before anything is designed

1. `python tools/clarity_lint.py check <copy file>`: zero FAIL. Read the headline-only read.
2. The cover-only read: from the cover alone, can a stranger say what this is about?
3. One light `/cold-read`. It is a sanity check, not a polish pass.
