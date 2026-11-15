# How to make social content that lands: the deep structure

Synthesis of the November 2026 clarity research. Written 2026-11-15 by the Showrunner after a
team of Sonnet agents collected the evidence. This file explains WHY the doctrine says what it
says. The operating rules live in `knowledge/craft/clarity.md`, `knowledge/craft/carousels/` and
`knowledge/craft/captions.md`.

## Evidence base

| File | What it holds |
|---|---|
| `harvest_ai_publishers.md` | 30 posts (27 carousels, about 140 slides, all viewed) from @openai, @googledeepmind, @therundownai, @evolving.ai, @airesearches, @wired, @nvidia, @axios, @theaifield, @verge |
| `harvest_ai_creators.md` | 26 posts, every slide viewed: Harper Carroll, Ishan Sharma, Tiff In Tech, Rowan Cheung, Varun Mayya, Aashish Pahwa (@okaashish), Greg Isenberg, Luis P, and small "I built X with AI" builders (Jacklyn Collins, Ayesha, Dhruv Rane, Shubham Verma, Ana Robakidze, Zoof04) |
| `harvest_simplicity_masters.md` | 32 posts from accounts known for plain, premium carousels: The School of Life, Aeon, Visualize Value, Morning Brew, Ankur Warikoo, Finshots, Kurzgesagt, NASA, Vox, Axios, Sahil Bloom, ScienceAlert, New Scientist |
| `harvest_reels_shorts.md` | 27 short videos (17 YouTube transcripts, 12 Instagram reels read frame by frame): Cleo Abram, MKBHD, Varun Mayya, Ishan Sharma, Tiff In Tech, Riley Brown, Harper Carroll, Kallaway, Kurzgesagt |
| `cognition_platform_audience.md` | Fluency, cognitive load, Mayer's multimedia principles, curse of knowledge, plain-language practice, platform mechanics, audience surveys |
| `nlp_research.md` | Neuro-Linguistic Programming: what survives scrutiny (as a lint tool) and what does not |
| `reader_feedback.md` | Two voice notes from a first-time, non-tech reader (Sparsh's wife) on the deleted carousel and the earlier Panditji launch carousel |
| Cold-read test (this session) | A fresh Sonnet reader with no context, given the deleted carousel's real slides as two personas |

About 115 posts and videos were read at the slide or frame level: 30, 26 and 32 still posts,
plus 27 videos. Engagement numbers are noisy. Brand, celebrity, authority and news timing
drive reach: Nvidia's 59.6K-like post has no text at all, and Harper Carroll's likes follow
her authority and the news, not her clarity. So the craft lessons come mainly from comparing
strong and weak posts INSIDE the same account, where the audience is held constant, and from
reading every slide.

That second point matters for Tangent more than for anyone in the corpus. A big account can
post an unclear carousel and still do well on trust. An account with no audience yet has
nothing else carrying the post. **For Tangent, clarity is the main lever, not a nice-to-have.**

## 1. What actually failed

Three separate failures stacked on top of each other. The old system guarded against none of
them.

**Failure 1: the riddle voice.** Every headline compressed a private fact into a stylish
phrase. "One sky, two ways to count it." The NLP Meta Model names exactly what was done: the
agent was deleted ("Tested."), actions were frozen into nouns ("ways to count"), "the" was
used for things the reader had never met ("the maths", "the model", "the sky's reference
books"), and plain verbs were swapped for metaphors ("moving Saturn"). Each one is a question
the reader has to answer silently. On a feed, nobody does. The research is blunt about the
cost: needless complexity makes the writer look less intelligent (Oppenheimer 2006), and
hard-to-process text is liked and trusted less (Reber et al. 2004).

**Failure 2: the deck voice.** Even the plain lines read like a slide deck. The earlier
launch carousel's "It reads your day, in plain words." and "It finds good hours to begin, and
ones to avoid." are clear but impersonal: third-person feature bullets with no speaker. The
first-time reader called it "very presentation-ish ... not as if the owner is talking to his
audience". This is a separate axis from clarity. It is fixed by a person talking (I, you), not
by simpler words.

**Failure 3: no single message, and a cover that was not a label.** The deleted carousel
covered six topics in six slides (the bug, the zodiac, the architecture, the accuracy tests,
the safety tests, the links). Its cover was a teaser. The reader's first rule: "the cover
page has to tell me exactly what this post is going to be about in very simple few words".
Neither cold-reader persona learned what Panditji is or what it does for them.

The cold-read test reproduced the reader's verdict without seeing her feedback: the everyday
persona would not stop on slide 1, flagged 22 phrases it did not understand, and would have
left by slide 4. The tech persona followed it but still never learned what the app does.

**Why agents write like this.** Four causes, all fixable:
1. The voice rules rewarded it: "dry wit", "quotable-beat engineering", "never flat", "the
   slightly richer word". An agent reads those as "be clever".
2. The curse of knowledge: the agent had just read the whole article, so "arcsecond" and "the
   maths" felt like plain words to it.
3. Language models default to the cadence of marketing copy: short parallel fragments that
   feel like insight. (An inference; no study found.)
4. Nothing checked the post through a stranger's eyes. Readability formulas would not have
   helped: the failed copy scores reading grade 5.0.

## 2. The deep structure: one sentence, unfolded

Every strong post in the corpus is a single sentence that has been unfolded into layers. Each
layer must deliver the message at its own resolution, so the reader can stop at any layer and
still leave with the point.

```
Layer 0  THE MESSAGE        one plain sentence a viewer would repeat to a friend
Layer 1  THE COVER          what this post is about, in a few simple words (a label + a stake)
Layer 2  THE HEADLINES      one per slide; read alone, in order, they tell the whole story
Layer 3  THE BODY           optional depth under each headline, for the interested
Layer 4  THE CAPTION        line 1 restates the message; later lines carry the "more" layer
Layer 5  THE DEPTH PATH     article, long video, link in bio: where the enthusiast goes
```

This is the inverted pyramid (most important first, so a reader who stops early still has the
point) applied to every surface at once. It shows up independently across the evidence:
- The reader's own rule: "if I'm not interested, I can scroll past, but I still get the
  message".
- @googledeepmind's bold lead lines, which read as a complete summary when you skim only the
  bold.
- Axios Smart Brevity ("why it matters", "go deeper").
- Cleo Abram's descriptions, which restate beat 1 and the tease.
- Mosseri's carousel "second chance": an unswiped carousel can reappear starting at slide 2,
  so every slide has to work on its own.

**Three skim tests follow directly**, and they are the core quality checks:
1. *Cover-only read:* from the cover alone, can a stranger say what the post is about?
2. *Headline-only read:* do the headlines alone, in order, tell the story? (`clarity_lint.py`
   prints this.)
3. *Full read (cold read):* after the whole post, can a stranger say the message back?

## 3. The decisions behind every artifact

Before any copy is written, five decisions (the Message Brief):

1. **The message**, as the sentence a viewer would repeat. If it cannot be written plainly, the
   post is not ready.
2. **The audience.**
   - *A, the AI-curious everyday viewer:* wants the cool result and what it does for them.
   - *B, the tech enthusiast:* wants a surprising problem or mechanism, and a path to depth.
   The evidence says to write the slides for A and give B a door. NN/g found experts prefer
   plain, scannable text too, so plain costs nothing with B. Depth belongs off the slide.
3. **The arc**, 3 to 5 beats, each a plain sentence. The shapes that recur in the corpus are
   few and stable (the arc library in `clarity.md`): I made a thing; before and after;
   explain one thing; what went wrong and the fix; guess; news and what it means for you.
   Under every one of them sits the same move: start from something the reader already knows,
   add exactly one new idea, show the proof, then give the next step. NLP calls this "pace,
   then lead"; learning research calls it pre-training plus segmenting.
4. **The picture for each beat.** Plan the visual before the line (Cleo Abram's stated
   method). The muted-reel test confirms it: every reel that could be followed with the sound
   off showed the thing and carried one persistent label.
5. **The voice and tone.** Who is talking, and to whom (section 5).

## 4. The line: what a good headline is

Across about 120 posts, the strong headlines share one shape: **a full, literal sentence that
says who did what, or what it means for you, in 6 to 15 words.**
- "This legend built an app to help your grandparents not get scammed" (@openai)
- "The Most Successful Person You Know Is Just as Anxious as You Are" (The School of Life)
- "5 money rules my wife and I follow. We're 45, with two kids." (Warikoo, 12.3K likes)
- "This camera allows you to see sound in real time" (MKBHD, 2.7M views)
- "What a bad day for Nvidia means to you" (Finshots)

Weak headlines, in the same feeds: "THE END OF THE FOUNDER FAIRY TALE" (metaphor), "Gemini 3.8
Live" (a version number with no benefit), "Fugitive imagination" (a coinage), "Artificial
Super Intelligence" (a topic label), "Use AI as a Sparring Partner for Your Thinking" (3.8K
views, against 253K for the same creator's plain question).

Numbers that kept recurring across independent harvests:
- **Cover:** 6 to 14 words.
- **Body slides:** about 8 to 35 words. Slides over 45 to 50 words were consistently the
  weakest, unless one plain anchor line led them.
- **Sentences:** about 9 to 17 words.
- **Reading grade:** 5 to 8 for the clearest posts. The hardest ran grade 12 to 14 with
  stacked technical nouns.
- **Spoken scripts:** grade 5 to 8, sentences about 12 to 15 words. Cleo Abram writes at
  grade 5 to 6.
- **Reel on-screen text:** 2 to 6 words at a time, matching the speech, plus one persistent
  topic label.

**When clever works.** The masters do use wit, and it works under one condition: the reader
can say what the line means from the same slide, before swiping. "Boring is beautiful" comes
after a list of boring habits. "So you're dead... my condolences" works because the picture
shows exactly what is meant. "Metal potatoes" is a nickname you can see. Wit that needs a
second slide, the article or the writer's head to decode is the riddle voice.

**How slides chain.** Every strong post links its slides with something explicit. Stories use
bridge words: "Before this / Then I saw / So I built / Now I get to" (a small builder's
first-app post), "None of these actually work" (The School of Life), or a teaser line at the
foot of each slide (Shubham Verma). Lists and explainers use a fixed frame or a counter:
"step 1 to 5", "App 3 of 6", "One chip / One company / One island" (Tiff In Tech), or
question-then-answer headlines (Harper Carroll). News pages use chronology or a repeated
subject. The device varies with the format, but there is always one. The deleted carousel had
none: six slides, six unconnected headlines.

**Words and type size.** The same author's 55-word card in large type got 124.5K likes, while
his 230-word block in small type got 1.1K (Greg Isenberg). The most-shared post in the
creators harvest (5.7K shares) had 2 to 5 words a slide, each with a literal cartoon of the
action ("Call instead of text"). Fewer words, larger, with a picture of the thing.

**Jargon.** Five strategies, in order of reliability:
1. Avoid it.
2. Restate it in an everyday verb.
3. Define it in the same sentence (NASA's "one light-day (16 billion miles)").
4. Give it its own slide as the headline (a glossary card).
5. Let a screenshot carry it. This is the least reliable.

The masters put the nickname or picture first and the label second.

## 5. Voice and tone: the person, not the deck, not the riddle

| Voice | Example | Problem |
|---|---|---|
| Riddle | "One sky, two ways to count it." | Hides the meaning |
| Deck | "It finds good hours to begin, and ones to avoid." | Clear, but nobody is talking |
| Person, direct | "Starting something new? Panditji tells you which hours are good for it." | None |
| Person, warm | "My mum always asked the family Panditji before starting anything. I built one you can ask from anywhere." | None |
| Person, witty (one-glance) | "It won't tell you when you'll die. Or which coin will 10x." | Works: the joke is instantly understood |

The person voice is the one used by every creator who wins with a general audience. Its
marks:
- **First person and second person:** "I built", "you can".
- **A real situation:** "my first app", "I can't code", "we're 45, with two kids".
- **A small honest aside:** "Pulling that trigger is hilarious" (MKBHD), "my condolences"
  (Cleo).

Mayer's personalization principle (conversational style, d about 0.79) is the research version
of the same finding. The reader explicitly asked to try more than one tone, witty and direct,
and see what lands. The doctrine makes tone a declared choice in the Message Brief and keeps a
running tone experiment (section 9).

The brand's register (calm, honest, never hype) survives intact. What changes is that calm now
means "a thoughtful person talking plainly", not "a curated line on a gallery wall".

## 6. Tangent's two core stories, as the evidence shapes them

**"I built an app with AI"** (the builder story). No account over 50K followers posts this as
a carousel. The big builders use reels, so this template rests on small accounts, on Luis P
(21.6K) and on @openai's real-user stories. Across all of them the clear ones share five
moves:
1. **The cover says it literally, with the person and what the app does.** "Hi, I'm Jacklyn.
   I built Shelf by JC with AI." Posts that never said what the app does left a cold viewer
   unsure what it was for (Shubham Verma's story post, Dhruv Rane's screenshot tour).
2. **Admit being a non-expert.** "I don't understand a thing about code." This is the most
   trusted line type in the set.
3. **Chain the headlines Before / Then / So / Now, or Step 1 to N.**
4. **Put a real screenshot, prompt or result on every slide.**
5. **Add one candid aside** ("claude gaslit me multiple times btw").

Never lead with the tool or model name.

**AI-edited photographs** (the gallery story). An image-only carousel whose caption did not
describe the images got 7 likes (Shubham Verma's AI city maps). Tiff In Tech's text-free
factory stills worked because the caption stated the claim in its first line. So a photo post
needs a plain label of what the images are and what was done to them, either on the cover or
in caption line 1, and a short label per slide ("Brighter sky", "Warmer skin"). The
before-and-after pair is the picture of the change.

## 7. The visual layer

- **Premium comes from restraint, not from wordplay.** The quiet, classy accounts (The School
  of Life, Aeon, Visualize Value) use one background colour, one type weight, wide margins and
  one idea per slide. Their titles are still plain claims, and their weakest posts are exactly
  the ones with abstract titles. Quiet does not mean cryptic.
- **Show the thing.** Every slide carries a picture of what it talks about, with labels ON
  the picture (Mayer's spatial contiguity). Analogies that worked were drawn: Finshots' basket
  and scale, Cleo's basketball and pin.
- **Contrast.** The deleted carousel used gold, pink and green text and dim grey body text on
  near-black. The reader asked for "more white, less black", though she was unsure.
  Display-polarity research generally finds dark text on a light background easier to read,
  especially at small sizes (Piepenbrock et al. 2013; cited from memory, verify before quoting
  externally). The doctrine does three things:
  - It requires high-contrast body text (no dim grey for anything that must be read).
  - It allows light backgrounds for text-heavy slides.
  - It runs the light-versus-dark question as a test, because the dark look is part of the
    brand and the decision is Sparsh's.

## 8. Platform facts that shape the rules

- Instagram ranks on watch time, likes per reach and sends per reach. Sends matter most for
  reaching non-followers (Mosseri, January 2025). A post gets sent when it is understood in
  one pass and has one clear point. [OFFICIAL-PLATFORM]
- An unswiped carousel can come back starting at slide 2 (Mosseri, October 2024), so slide 2
  must also stand alone. [OFFICIAL-PLATFORM, relayed]
- Links in captions are not clickable. Say "link in bio" and use the Story link sticker.
- Carousels slightly edge Reels on engagement rate in 2025 brand data (0.55% against 0.52%,
  Socialinsider). There is no reliable best slide count, so use as many slides as one idea
  needs, usually 4 to 7. [INDUSTRY DATA]
- No top video ended with "follow for more". Winners end on a next-video tease, a question,
  or the last fact.

## 9. What the NLP research is good for

NLP as a system is not supported by evidence (Witkowski 2010, Passmore and Rowson 2019). Its
**Meta Model** is still useful as a lint tool, because what it checks lines up with solid
mainstream research on fluency, concreteness, presupposition and the curse of knowledge:
- Who did it?
- What exactly did they do?
- To what?
- Does the reader already know this "the X"?
- What does this number count?

"Pace, then lead" maps onto the arc. "Chunk down" maps onto one concrete example per claim.
"Future pacing" maps onto one small, concrete next step at the end.

**Applied to the corpus** (`nlp_research.md` Part 3). The agent coded 31 strong lines, 15 weak
lines and our 5 failed lines for Meta Model violations:
- Strong lines averaged **0.74** violations, weak lines **2.8**, and our failed lines **4.6**.
  58% of strong lines had none. No weak line had fewer than 2.
- "One sky, two ways to count it." scored 6 of 7, the worst line in the set.
- What separated the groups: nominalizations, a presupposed "the X" or insider term,
  metaphors, unspecified verbs and unanchored numbers.
- Strong lines used verbs a camera could film 52% of the time, against 7% for weak lines. They
  had a picturable subject 74% of the time, against 33%.
- One exception: proverb-style posts stay vague and still do well. That works only when the
  reader fills the gap from their own life, the line is short, and a picture anchors it.

The coding was not blinded, and engagement tracks fame, so treat this as strong suggestive
evidence rather than proof. It is still the most direct evidence on social posts in this study,
and it points the same way as everything else.

Never used:
- Embedded commands.
- Engineered yes-sets.
- Covert hypnotic vagueness.
- Presuppositions that smuggle in claims.

They are manipulative, and on an astrology app, vague flattering language is exactly the
Barnum effect that would cost trust.

## 10. What this changes in the repo, and the open questions

**Changes (all implemented in this revamp):**
- A constitutional Clarity rule (CLAUDE.md #10) that covers every artifact, including
  ad-hoc pieces made outside the pipeline.
- The Message Brief, which is mandatory before copy.
- New craft packs for carousels and captions.
- The reels pack rewritten to defer to the clarity doctrine.
- Voice rules rewritten from "dry wit / quotable" to "person, plain, warm".
- The audience model reset to A/B with two-layer design.
- A deterministic `tools/clarity_lint.py`.
- A `cold-reader` agent and `/cold-read` skill, with two personas and no context.
- `pipeline.py` now blocks G1 without one `COLD-READ: PASS`.
- The critic weights CLARITY ×2 in the mean.
- All of these checks are deliberately light. After a first real run ground through four
  rounds on small wording snags, Sparsh had them loosened: the cold read is a sanity check,
  not a polish loop, and most lint findings are warnings.
- A fast path, `/post`, for ad-hoc pieces.

**Open questions, run as experiments and logged in `strategy/BETS.md`:**
1. Tone: person-direct against person-witty on the same kind of post.
2. Light against dark backgrounds for text-heavy carousels.
3. Cover style: plain label against plain label plus one stake line.

Each is decided on Tangent's own data, never on a single post.

**Limits:**
- Engagement is a weak signal, so the lessons rest on within-account comparisons and on
  first-principles research.
- No Instagram account over 50K followers posts "I built X" carousels. The builder template
  rests on small accounts, Luis P (21.6K), @openai's real-user stories and Riley Brown's reels.
- A truly dark, quiet, minimal AI creator at scale was not found. Aeon and The School of Life
  are the closest style matches.
- Several citations in the research files are flagged for re-verification before anyone
  quotes them publicly.
