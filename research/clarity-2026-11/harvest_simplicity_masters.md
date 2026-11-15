# Harvest: simplicity masters (Instagram carousels / stills)

Collector notes
- Method: Claude in Chrome, own tab, read-only. IG CDN image URLs are blocked from being returned by the JS tool, so curl download was NOT possible. Every slide was viewed as a screenshot/zoom of the post page (?img_index=N). Nothing was liked/followed/saved.
- Likes/comments are as shown on the post page on 2026-11-15. Brand accounts often show rounded values (1.4K).
- Evidence tags: [OBSERVED] seen on slide/page. [INFERENCE] my reasoning.
- Scope note: 32 posts analysed with every slide viewed (see "Coverage update" after Account 13). File was rebuilt after a concurrent-write collision; some Round-1 metadata (e.g. exact post dates for Round-1 accounts) was not retained.

---
## ACCOUNT 1: @morningbrew (2.2M followers, 10.8K posts)
Why picked: Brand-level "Smart Brevity"-style business news. Carousels on current news, daily cadence, strong engagement (1-3K likes). Tech/business explanations for a general audience.

### Post MB1 - https://www.instagram.com/p/Dfqghnpk6AU/  ("The fall of Nvidia's Jensen Huang")
- Date: ~2 days before 2026-11-15 | Format: carousel | 7 slides | 1.5K likes, 16 comments
- S1: "THE FALL OF NVIDIA'S JENSEN HUANG" + "SWIPE FOR MORE >" . ~9 words. Full-bleed dark portrait, headline bottom-left in 2-colour (white + yellow-green) heavy sans caps; tiny brand tag top-left. ~85% image / 15% text. Job: hook.
- S2: "JENSEN'S FALL A TIMELINE:" (blue + orange, 2 lines), "Oct. 2025—" two bullets ("US and local officials both open investigations into Singapore-based Megaspeed", "The data center firm is suspected of helping Chinese companies skirt US chip embargoes") + photo. ~40 words. White background, 40/60 text/image. Job: context.
- S3: same frame, "Late 2025/Early 2026—", one bullet (Megaspeed exec close to Huang "was a spy for China's Ministry of State Security") + photo with Trump. ~30 words. Job: tension.
- S4: "Oct. 29, 2026—" three bullets (NYT reports long-term affair; US officials feared secrets shared with Beijing; Nvidia calls it "completely normal and not unusual") + circular photo. ~55 words. Job: reveal.
- S5: "Nov. 4, 2026—" / "Nov. 8, 2026—", three bullets (lawmakers call to testify; Jensen admits affair; board investigates). ~50 words. Job: escalation.
- S6: "Nov. 11, 2026—" two bullets (second affair; board meets) + B/W portrait. ~35 words.
- S7: "Nov. 12, 2026—" five bullets (resigns; CFO interim CEO; search; briefs Congress; third affair). ~60 words. Job: payoff/latest state.
- One-line message: "Nvidia's CEO went from top of the world to resigned in 3 weeks; here is the dated sequence."
- Audience: general business-news readers; no jargon beyond "embargoes", "interim CEO".
- Beat arc: hook (name+drama) -> why it started (Megaspeed) -> spy allegation -> affair report -> escalation -> resignation.
- Readability: ~grade 8-9. Concrete, dated, subject-verb-object bullets, ~12 words per bullet. Zero metaphor. Key phrase of each bullet is coloured blue (scan-reading: reading only the blue gives the whole story). 
- Cohesion: IDENTICAL repeated frame (same two-colour title "JENSEN'S FALL A TIMELINE:") on slides 2-7 + dates as running numbering = strong sense of progress. Slide 1 says "Swipe for more".
- Hook: [OBSERVED] named-person + dramatic noun ("THE FALL OF"); swipe prompt. Stops thumb because a famous name + fall narrative.
- Caption (~650 chars): starts "How'd we get here?" then "3 weeks ago, Nvidia and CEO Jensen Huang were on top of the world. Today, the company has shed nearly $2 trillion..." Extends the slides with the stakes and upcoming events; CTA none visible besides photo credit.
- Clarity: 9/10. The title "Jensen's fall: a timeline" is literally what it is. Not clever. [INFERENCE] the date labels are what make 7 slides feel light.

### Post MB2 - https://www.instagram.com/p/Dfs3K5GleGE/ ("Bessent points blame at Lutnick")
- Date: 1 day old | carousel | 4 slides | 1.4K likes, 41 comments
- S1: "Bessent points blame at Lutnick for Megaspeed's access to Nvidia AI chips" (13 words) bottom-left white heavy sans over two inset portraits; tag "BREW MARKETS". 90% image. Job: hook/headline.
- S2: big pull quote "Commerce has the pen. You'll have to ask them about their internal processes." attribution "- Treasury Secretary Scott Bessent (CNBC)". 22 words. Big quote mark glyph. Job: tension.
- S3: quote "Treasury, War, USTR and State were in favor of putting Megaspeed on the entity list for months." ~20 words.
- S4: quote "The real story here should be: Did Nvidia know their client, ... pass-through shell companies?" ~45 words. Job: payoff (the accusation).
- Message: "A US cabinet official is publicly blaming another for letting AI chips reach a suspect company."
- Audience: general news/finance. Jargon: "entity list", "shell companies" are not explained on slides (caption does a bit).
- Readability: grade ~10; names-heavy. Slides are only quotes: one idea per slide, 1 quote per slide at large size.
- Cohesion: same photo-bg/quote template, 3 consecutive quotes by same person, escalating. Dots show 4.
- Hook: headline-as-news-sentence (who blames whom for what).
- Caption (~900 chars): "Jensen Huang's drama has reached the White House. In an interview with CNBC today, ..." long paragraphs; extends the slides with the backstory (restates headline then background). No CTA.
- Clarity: 7/10. Structure is clear; content assumes you follow the saga (Megaspeed, Lutnick).

### Post MB3 - https://www.instagram.com/p/Dfr55PGE_xU/ ("Microsoft races to recover from massive services outage")
- 1 day old | carousel | 3 slides | 2.7K likes, 42 comments
- S1: "Microsoft races to recover from massive services outage" (8 words) bottom-left white heavy sans; photo of Satya Nadella + Microsoft logo circle. Job: hook.
- S2: "430 MILLION" huge neon-yellow caps over meme clip frame (man throwing computer in a dumpster); chip "EST. USERS OF MICROSOFT 365 APPS"; "SOURCE: MICROSOFT". 6 words. ~95% image. Job: scale/stakes.
- S3: screenshot of a Morning Brew tweet: bullet-list status ("Full service still not restored..."). ~85 words, the densest. Job: facts/update.
- Message: "Microsoft's big outage affects 430M users and is partly fixed."
- Readability grade ~7-8. Number slide is the standout: one number, one label, funny image.
- Cohesion: weak-ish; slide 3 is a different design (tweet). 
- Hook: plain news headline with "races to".
- Caption (~700 chars): "Terrible news for anyone who had planned on circling back today." Playful line first (office humour), then facts. CTA none.
- Clarity: 9/10. The joke in the caption ("circling back") is instantly decodable: a corporate cliche.
Account patterns (Morning Brew) - [INFERENCE] 3-7 slides; cover = full-bleed photo + one sentence headline in plain news voice; inside slides alternate a single huge element (number or quote) or a scannable dated list with coloured key phrases. Text per slide 6-60 words. All carousel templates repeat a frame. Captions: one hook-line then 2-3 short paragraphs that EXTEND (context and upcoming events).



---
## ACCOUNT 2: @ankurwarikoo (Indian creator; 4M followers, 6.7K posts)
Why picked: biggest Indian "simple advice" creator; mixes text-on-photo carousels and reels. Plain Indian-English; carousels use a tweet-card overlay on personal photos.

### Post AW1 - https://www.instagram.com/p/Dfun_mRmtiS/ ("5 money rules my wife and I follow")
- 20h old | carousel | 7 slides | 12.3K likes, 81 comments, 150 shares/sends
- S1: tweet-card (white box with avatar, "Ankur Warikoo @warikoo") reading "5 money rules my wife and I follow. We're 45, with two kids." (~16 words) over a photo of the couple at a tennis court. Text ~25% / photo 75%. Job: hook (specific number + credible persona + age/family detail).
- S2: "1. We don't spend to look rich. We spend to become wealthy and free with our time." + "No owned car, it's rented. We own the home we live in, no other real estate. No spending on brands just to show people." (~45 words), card at bottom over a new couple photo.
- S3: "2. We spend extravagantly on good food." + 2 sentences "What goes into your body is the biggest wealth you have..." (~40 words)
- S4: "3. We spend on experiences over things." "Things give you happiness once. Experiences change who you are. We travelled 116 days last year." (~30 words)
- S5: "4. We invest before we spend." "The moment income comes in, the largest chunk is invested first. We live on what's left." (~28 words)
- S6: "5. No budget for books and learning." "No amount here is ever 'too much.' Ruchi is learning pottery, watercolour, and tennis. The kids are in all kinds of classes." (~35 words)
- S7: "These are our rules. They may not be yours. But having your own money rules, and actually following them, is what builds a life of freedom. What's one money rule you live by?" (~35 words). Job: payoff + engagement question.
- One-line message: "Here are the five simple money rules a 45-year-old couple actually follows."
- Audience: general Indian middle class, aspirational.
- Beat arc: promise (5 rules) -> rules 1..5 (one per slide, numbered) -> "make your own" + question.
- Readability: grade ~6. Short declaratives, "we" voice, concrete (rented car, 116 travel days). Almost no jargon; "invest" is the hardest word. Sentence length 6-14 words. Bold rule line + 2 plain support sentences.
- Cohesion: SAME tweet-card frame on every slide, numbering "1." to "5.", a different personal photo each slide (photo changes, text template fixed). Last slide closes the loop ("These are our rules").
- Hook: number + "my wife and I" + credibility ("We're 45, with two kids"). Stops the thumb: a real person you can picture + a list promise.
- Caption (~620 chars). First ~125: "We think wealth is about how much you earn. It's really about the rules you follow with what you earn." Restates and extends (adds the 3 core ideas as short lines); CTA "Save this and write your own." No hashtags seen.
- Clarity: 10/10. Nothing to decode. The one rhetorical line (caption contrast "how much you earn / rules you follow") is instantly decodable.

### Post AW2 - https://www.instagram.com/p/DfsIKa9qBit/ ("Your relationships will never be better than your self-esteem")
- 1d | SINGLE image | 2.6K likes, 11 comments, 41 shares
- Visual: poster-style black heavy sans text, 8 words, on white paper stuck to a wall (photo), tiny author sticker bottom-left. ~90% text, lots of white space.
- Message: "How you see yourself caps the quality of your relationships."
- Readability: grade ~7; abstract ("self-esteem") but the sentence is a complete one-line thesis.
- Caption (~480 chars): "We keep trying to fix our relationships from the outside." Extends with reasoning in 1-line paragraphs, ends "Work on how you see yourself. Everything else slowly rises to meet it." No CTA.
- Clarity: 9/10. Proverb-shaped claim; the wall-poster look lends authority.
- Contrast: 2.6K likes vs 12.3K on AW1 -> the specific, numbered, personal carousel got ~5x the likes of the abstract poster. [INFERENCE: format + specificity, not proven]

Excluded: https://www.instagram.com/p/DfpS8Tjlw0y/ is a @youtubeindia collab ("comment your adulthood watchlist") - not Warikoo's own craft.

Account patterns (Warikoo): [OBSERVED] one numbered rule per slide; bold rule on the first line of each card then 1-2 plain sentences; personal photo as the "visual" (the visual does not explain, it adds trust). Captions are line-per-sentence "poem" style. Ends with a question to trigger comments and "save this".

---
## ACCOUNT 3: @kurzgesagt (science explainer; 1.6M followers)
Why picked: the benchmark for explaining science to a general audience; the IG feed is image-led and caption-led. (Note: on IG the recent static posts are video promos, not text carousels.)

### Post KG1 - https://www.instagram.com/p/DfmwZOyl6Yz/ ("What happens when you die", video promo)
- 3d | single image (all img_index values render the same image) | 7K likes, 55 comments
- Visual: one illustration with ZERO text: a floating figure with red flame-like cell tendrils on deep indigo, glowing.
- Caption (~620 chars). First ~125: "Death isn't a single switch that shuts down your entire body at once. When your heart stops beating and your brain goes silent, trillions..." The caption IS the headline; then 3 question lines ("What actually happens when you die? What makes death so mysterious...") then CTA "Watch our full video to find out!".
- Message: "Death is a slow process, not one moment; your cells keep trying to survive."
- Hook: strange, glowing, slightly alarming picture + a first sentence that reverses a common belief.
- Clarity: 8/10. The picture conveys mood not facts; the caption explains via a concrete metaphor ("single switch") that needs no decoding. This is a clever line that works: it is a familiar object (a switch) used literally.

### Post KG2 - https://www.instagram.com/p/DfXTfsEl5DL/ ("Munster 1534", Nightshift video promo)
- 1w | carousel 2 slides | 17.1K likes, 115 comments
- S1: illustration only: silhouette in an iron cage before flames and a crowd. S2: skeleton in cage (the fate). No on-image text. Jobs: hook, payoff (dark).
- Caption (~600 chars): "In 1534, a radical religious movement took control of the German city of Munster, promising to create a paradise on Earth where everyone would be equal and free. But under the rule of ..." then a paragraph of 3 questions and CTA "Watch our latest Nightshift video to find out!".
- Structure: promise then twist in two sentences ("paradise" -> "nightmare"), then questions = curiosity gaps.
- Clarity: 8/10.

Account patterns (Kurzgesagt): [OBSERVED] art style is the brand; 0 words on slides, ~100 words in caption; 1-2 slides; caption = "claim + twist -> 3 questions -> watch the video". [INFERENCE] illustration carries emotion, caption carries information; they are separated rather than stacked, so each is light.

---
## ACCOUNT 4: @nasa (104M followers; science/tech for a general audience)
Why picked: largest science account; extreme engagement; pure "one great image + plain caption".

### Post NA1 - https://www.instagram.com/p/DfkkknjD6vm/ ("Voyager Golden Record")
- 4d | carousel 2 slides | 560.2K likes, 1.9K comments, 29.1K sends
- S1: studio shot of the gold disc ("THE SOUNDS OF EARTH" etched) on black. S2: back of the disc with engraved diagrams. No overlay text.
- Caption (~520 chars): "The sounds of Earth have traveled nearly a light-day away." then a dated fact (Sept. 5, 1977), then a scale line "one light-day (16 billion miles)" which translates the unit immediately, then an event CTA "Join us after sunset on Nov. 17 to 'Shine Bright'... Check the link in bio". Hashtags: #NASA #Voyager #GoldenRecord (3).
- Message: "Voyager's record is almost a full day of light-travel from Earth."
- Clarity: 9/10. "Light-day" is jargon but is translated with miles in the same breath. The first line is poetic yet literal.
- Hook: one glowing object on black + a poetic literal sentence.

Account pattern (NASA): [OBSERVED] one striking image, caption does the explaining in 3 short paragraphs; jargon is defined with a number right after; 1-3 hashtags at the end. Premium-looking via restraint: black background, no overlay text.


---
## ACCOUNT 5: @visualizevalue (475K followers, 1.1K posts; the visually minimal + premium benchmark)
Why picked: the closest match to Tangent's quiet, premium look: black/white, tiny type, lots of empty space, a one-line caption. Nearly all recent posts are SINGLE images (the grid shows only 1 carousel in the first 12), so this is a "still image" study.

### VV1 - https://www.instagram.com/p/DdZSm1clEqm/ ("I'm auctioning my next symbol project", collab with jckbtchr)
- 8w | carousel 5 slides (slide 5 confirmed; dots) | 461 likes, 9 comments, 6 shares
- S1-S4: 2x4 grid of black line-art symbols on white (and black-background version): a face, an eye in a circle, a bold X-shape, brackets, etc. No words. 100% visual. S5: three-line monospace text top-left on white: "EXECUTION IS ABUNDANT. JUDGEMENT IS SCARCE. BUY MINE." plus a small signature, then ~95% blank page. ~9 words.
- Message: "Symbols are art; bid on the next one."
- Caption (~100 chars): "I'm auctioning my next symbol project. Bid at visualizevalue.com/jack for the next 24 hours." Plain, one CTA with a URL, no hashtags.
- Hook: the visual grid itself (visual curiosity); payoff slide is a three-line aphorism then CTA.
- Clarity: 7/10 (the point only lands on slide 5; "symbol project" is insider). Works because slide 5 is blunt and uses parallel structure.

### VV2 - https://www.instagram.com/p/DdPfN_-mVL7/ ("Distraction, Focus")
- 8w | single | 1.5K likes, 4 comments, 66 shares
- Visual: black square; left, a wavy short line (messy) and right a clean curve (calm). ZERO words on image. Caption is exactly "Distraction, Focus" (2 words) - the caption labels the two shapes.
- Message: "Distraction is jagged; focus is one smooth line."
- Readability: grade ~3. A metaphor that needs decoding but is decoded in the caption in 2 words, and the shapes are literally wobbly vs smooth.
- Clarity: 8/10. Clever line that works because caption + shape together form a legend.

### VV3 - https://www.instagram.com/p/DdVKYsgEdtq/ ("you are only as free as the approval you don't need")
- 8w | single | 2.3K likes, 14 comments, 156 shares
- Visual: lone silhouette on a white page under a blurred black cloud of figures (a crowd of opinions). No on-image text; the one-sentence caption is the idea: "you are only as free as the approval you don't need".
- Message: "Needing approval makes you less free."
- Clarity: 9/10. Visual metaphor (a crowd looming over one person) matches the caption; the caption is a ready-to-quote sentence (lowercase, 11 words).

### VV4 - https://www.instagram.com/p/DdHCilmEcsm/ ("No position can be permanently occupied.")
- 9w | single | 1.1K likes, 6 comments, 37 shares
- Visual: tiny figure at the top of a very tall thin ladder on a white field. 90% white space. Caption: "No position can be permanently occupied." (6 words).
- Clarity: 8/10. Visual shows precariousness; caption states the thesis. Same pattern.

### VV5 (weakest, and the most relevant to AI) - https://www.instagram.com/p/DdHEjoyxXDf/ ("Artificial Super Intelligence")
- 9w | single | 243 likes, 1 comment, 6 shares
- Visual: the shadow of a hand whose palm is a light-bulb. Caption is a bare label: "Artificial Super Intelligence". A commenter wrote "Hand-shaped lamp" - i.e., the viewer had to decode the meaning.
- Clarity: 5/10. The image is lovely but the idea (intelligence = hand + bulb?) is ambiguous and the caption is a topic label, not a claim. Engagement is 1/10th of VV3.
- Lesson [INFERENCE]: when the caption names a topic instead of stating a claim, the image alone has to do all the work; here it did not. Compare VV2-VV4 where the caption states a sentence or a 2-word contrast.

Account patterns (Visualize Value): [OBSERVED] single image on a 1:1 / 4:5 white or black field; no overlaid text at all in 4 of 5 posts; caption is 2-11 words; one concept per post; tons of negative space; monochrome. [INFERENCE] Premium = restraint: one subject, one idea, no decoration; the "sentence" lives in the caption where the platform renders it in a normal readable font. Risk: metaphor-only posts (VV5) get low engagement and need a claim in the caption.

---
## ACCOUNT 6: @sahilbloom (1M followers; handwritten-note single images)
Why picked: the "plain words, huge type" benchmark: every post is one handwritten list or aphorism. All three recent posts studied were single images (no carousel).

### SB1 - https://www.instagram.com/p/Dfik-rvTfuJ/ ("Just stay in the game")
- 5d | single | 32K likes, 118 comments, 4K shares
- Visual: white page, black handwritten caps, 7 short sentences ("Just Stay In The Game. The Best Things In Life Are From Compounding. Whatever Storm Comes, Adapt. Survive. Stay In The Game."), ~28 words, a small signature. Text ~85% of image; generous margins.
- Message: "Success mostly comes from not quitting; compounding needs you still playing."
- Caption (~330 chars). First ~125: "I'm convinced that 99% of success is just the ability to stay in the game. Do you agree?" Then 3 sentences restating. Hashtags (4): #growth #mindset #progress #relationships. CTA = "Do you agree?".
- Readability: grade ~5. Metaphor "stay in the game" is a stock idiom (instantly decodable). "Compounding" is the only jargon and is left undefined, but is common.
- Clarity: 10/10.

### SB2 - https://www.instagram.com/p/DfqLUHMTzyy/ ("Build a boring baseline")
- 2d | single | 6.1K likes, 58 comments, 381 shares
- Visual: 8 imperative lines in handwritten caps: "Build a Boring Baseline. Go to bed early. Wake up early. Move. Eat simple foods. Save money. Avoid drama. Be present. Boring is beautiful." (~28 words). A list = easy scanning.
- Caption: "I think boring is beautiful. Do you agree?" + 4 hashtags.
- Clarity: 10/10. The oxymoron "boring is beautiful" is a clever line that works because each preceding line is a plain example (the list explains it).

### SB3 (weak) - https://www.instagram.com/p/DfvMgdWzl4M/ ("Become a beginner again")
- 15h | single | 2.5K likes, 14 comments, 153 shares (early; only 15h old)
- Visual: handwritten 10 sentences, ~45 words: "Become A Beginner Again. Join A Run Club. Learn Piano. Take Up Painting. Plant A Garden. Whatever Pulls You. It Slows You Down. A Small Rebellion In A World Obsessed With Outcomes." Caption "Just become a beginner again." + 4 hashtags.
- Clarity: 8/10. The last line is abstract ("a small rebellion... obsessed with outcomes"). Lowest engagement of the three, though it is the newest so not a fair comparison.

Account patterns (Sahil Bloom): [OBSERVED] 25-45 words on one image in big handwriting; one idea; 5-8 short lines; caption restates it in one question ("Do you agree?") and adds 4 generic hashtags. Compounding of 32K likes (SB1) over 6K/2.5K suggests the "stay in the game" idiom + universal appeal beat the list posts. [INFERENCE]

---
## ACCOUNT 7: @voxdotcom (1M followers; explainer journalism; carousels = magazine covers + big quotes)
Why picked: explains science/health/news to a general audience; has a clear, designed carousel template. Note: @vox on Instagram is a German TV channel (swapped); the right handle is @voxdotcom.

### VX1 - https://www.instagram.com/p/DfppvTSk1sg/ ("Why are so many young guys taking Viagra?")
- 2d | carousel ~7 slides (dots; viewed 1-4) | 1.3K likes, 27 comments, 25 shares
- S1: flat colourful illustration (shirtless man, worried face, abstract blue/yellow shapes) with headline "Why are so many young guys taking Viagra?" in white serif-ish bold, a dek "A new generation is leaning on erectile dysfunction pills. The reasons are surprising.", byline "By Allie Volpe", Vox logo. ~28 words. Job: hook (question headline).
- S2: abstract illustration only (men on phones, couple), no text. Job: mood/pacing.
- S3: yellow background; bold black lead "When considering the stereotypical Viagra patient, the mind conjures up an image of a man decidedly older than his 20s, after all. But that picture is changing." + body of 2 sentences with stats ("as high as 39%", "31-fold increase..."). ~75 words.
- S4: blue background, large quote mark + pull-quote, ~30 words, attribution.
- Message: "Younger men are using ED pills; here is why."
- Readability: grade ~10-11 (sentences 20+ words; "adolescent males", "pediatric urology practice"). Slide 3 is dense.
- Cohesion: constant colour-block backgrounds + Vox logo bottom-right; text slides alternate with image slides.
- Hook: curiosity question ("Why are so many...?") with a surprising demographic ("young guys").
- Caption (~900 chars) starts with a story: "Colby was in his 20s - far too young, according to some, to struggle with this particular thing - when he noticed an issue..." (narrative lede, not a restatement), then link-in-bio CTA.
- Clarity: 7/10 (title instantly clear; body slides heavier than the best-practice 25-35 words).

### VX2 - https://www.instagram.com/p/DfulgOHk4i2/ ("Could this bacteria save coral reefs from the heat?")
- 18h | single | 140 likes, 3 comments, 9 shares
- Visual: underwater coral photo; Vox logo; serif caps headline "COULD THIS BACTERIA SAVE CORAL REEFS FROM THE HEAT?" in dark navy, dek "The ocean's most important habitats are in danger. Scientists are looking to their microbiome to save them." byline. ~30 words. Same cover format as VX1.
- Caption (~600 chars): "Could bacteria help coral reefs survive extreme heat?" then a plain 3-paragraph summary, jargon "Endozoicomonas" named but surrounded by plain wording ("a type of bacteria called ..."). CTA "Read more at the link in our bio."
- Clarity: 9/10 on the image (one question + one picture), but only 140 likes. [INFERENCE] the weak engagement is due to news-topic interest and a headline-as-article-cover, not clarity.

Account patterns (Vox): [OBSERVED] "magazine cover" first slide (photo/illustration + serif headline + dek + byline), then solid colour text slides with one pull-quote per slide; the logo repeats bottom-right; question headlines.

---
## ACCOUNT 8: @axios (344K followers; "Smart Brevity")
Why picked: the Smart Brevity originator. Instagram grid is mostly reels; only occasional carousels and many single-image breaking-news cards.

### AX1 - https://www.instagram.com/p/DfUt7bPgQUW/ ("The biggest surprises of a stunning election night", collab with @applenews)
- 1w (Nov 4) | carousel ~7 slides (dots; viewed 1-4) | 2.3K likes, 42 comments, 37 shares
- S1: photo of a crowd, "The biggest surprises of a stunning election night." bottom-left in white, "Apple News+" tag, "From Axios" bottom-right. 9 words over image.
- S2: pale lavender background, plain black sans text only: "1. The Texas trifecta" (bold) + 3 paragraphs (~65 words), "From Axios" bottom-right.
- S3: "2. North Carolina was a bloodbath" + 3 paragraphs (~80 words).
- S4: "3. The ridiculously cheap wins" + 3 paragraphs (~95 words).
- Message: "Democrats won in surprising places: Texas, North Carolina, and cheaply."
- Readability: grade ~10-11; political insider names (DCCC, AdImpact, FEC) with no gloss, ~25-word sentences.
- Cohesion: numbered headings 1-2-3 with a distinct labelled phrase each ("trifecta", "bloodbath", "cheap wins") = scan-friendly even though body copy is dense.
- Hook: superlative + event ("biggest surprises").
- Caption (~200 chars): "Democrats didn't just flip swing districts - they broke through in some of the reddest corners of the map. Tap the link in bio to read the full story, via @axios." One sentence of stakes + CTA.
- Clarity: 6/10. The numbered bold headings are excellent; the body paragraphs are 3-4x too long for a thumb-scroll and lean on insider terms. It is a "wall of article" carousel and performed modestly vs Morning Brew's shorter ones (2.3K likes, 42 comments).

Account patterns (Axios): [OBSERVED] bold numbered label + short paragraphs; very low design; shows what the Smart-Brevity phrase "Why it matters" structure becomes when pasted onto slides - text-heavy. IG feed uses video for most storytelling.


---
## ROUND 2 additions

### Corrections to Round 1 slide counts (all slides now viewed)
- VX1 (Vox Viagra, https://www.instagram.com/p/DfppvTSk1sg/) is 6 slides. S5 (yellow): bold lead "The sex lives of young people - young men, in particular - are full of contradictions." + ~55 words of body (Gen Z, porn, "female orgasm gap", influencers) = ~70 words. S6: blue, big quote mark, pull-quote from a urologist: "A lot of the guys who come in are not coming from a place of deficiency. There is abundance." ~20 words, attribution + title ("UROLOGIST"). There is NO explicit CTA slide; the carousel ends on a quote.
- AX1 (Axios election, https://www.instagram.com/p/DfUt7bPgQUW/) is 5 slides, not 7. S5 is a CTA card: "Tap the link in bio for more." centered on lavender, nothing else (7 words, ~97% empty). Structure = cover + 3 numbered points + CTA. Clarity verdict stays 6/10 (S2-S4 are 65-95 words), but the final CTA slide is a clean, calm closer.
- MB1: 7 slides (all viewed).

---
## ACCOUNT 9: @finshots.in (Indian explainer; 381K followers, ~2K posts) - plain-language finance/economics carousels
Why picked: the Indian "explain it simply" benchmark requested. Almost every post is an 8-10 slide carousel (the real handle is finshots.in; @finshots is a private placeholder). Style: light grey/white text slides with a spot-illustration bottom-right, a dark CTA end card. All slides below were viewed.

### FS1 (best studied) - https://www.instagram.com/p/Dfrk61HlAa2/ ("What a bad day for Nvidia means to you")
- 2d | carousel 10 slides | 576 likes, 5 comments, 5 shares
- S1: heavy condensed black sans, "WHAT A BAD DAY FOR NVIDIA MEANS TO YOU." with "NVIDIA" in lime green; B/W cut-out of Jensen Huang on the right; green frame border; "Swipe to know" with arrow; logo top. 9 words. Text 45% / image 55%. Job: hook (personalises the news: "to you").
- S2: light off-white page, plain sans, left-aligned, ~40 words: "Since October 2, Nvidia has lost about Rs.154 lakh crore in value on the US bourses. To put that in context, every company listed on the BSE put together is worth about Rs.511 lakh crore." + illustration (green Nvidia logo on falling arrow). Job: context/scale (comparison to a familiar total).
- S3: ~45 words: "On Tuesday alone, the shares fell another 5.6%... Here's the thing. You may have felt this fall without ever buying a single Nvidia share." + illustration. Job: tension (the "you" hook).
- S4: "Why? Well, let's start with the basics. An index fund buys a bit of every company on a list... The S&P 500 is a list of 500 big US companies. The Nasdaq-100 is a list of 100 big, mostly tech, companies." ~60 words + illustration of a shopping basket full of buildings. Job: define (concept = basket).
- S5: "Most funds tracking these lists split your money by size... Out of every Rs.100 in an S&P 500 fund, about Rs.8.50 goes to Nvidia." ~50 words + illustration (stack of Rs.100 with a green Rs.8.50 slice).
- S6: "Why does that matter? Say Nvidia drops by 10%. That wipes out about 88 paise from every Rs.100 in your fund. If a small company holding just Rs.0.10 of your Rs.100 drops 10%, you lose one paisa. It's the same fall but it hits very differently." ~60 words + balance-scale illustration (-Rs.0.88 vs -Rs.0.01). Job: proof, by arithmetic.
- S7: "Now bring it home. Say you run a SIP in a Nasdaq 100 fund... Roughly Rs.9 of every Rs.100 goes into one company. 'But I bought 100 companies, not one.' You did and that's the catch." ~50 words. Job: personalise.
- S8: "Your fund may have never chosen Nvidia, but its growing size certainly did... Just ten companies now make up about 39% of the S&P 500." ~55 words, basket-with-logos illustration.
- S9: "It works both ways... You don't need to panic. But here's a two-minute check. Open your fund's factsheet and look at the companies that have the highest weightage..." ~60 words + clipboard. Job: payoff/action.
- S10 (dark end card): "So if one company can shake a fund built to spread your risk, what exactly are you betting on?" + boxed "FINSHOTS Follow Finshots for more such insigths!" (the slide has a typo, "insigths"). ~30 words. Job: CTA + reflective question.
- One-line message: "Nvidia's fall hurts index-fund holders, because the fund is weighted toward the biggest names."
- Audience: Indian retail investors (SIP holders), general; difficulty = basic.
- Beat arc: hook (it affects you) -> scale -> "you may have felt it" -> what an index fund is (basket) -> weights -> 10%-drop arithmetic -> your SIP -> concentration -> what to do -> question.
- Readability: grade ~8. Conversational ("Here's the thing", "Well, let's start with the basics", "But I bought 100 companies, not one"), 12-18 words per sentence, bold only the key numeric claim in each slide. Jargon (index fund, weightage, S&P 500, SIP) is defined in the sentence after it appears, using a basket metaphor that is literal. Numbers are converted to a per-Rs.100 view ("88 paise from every Rs.100").
- Cohesion: [OBSERVED] each slide opens with a connective that continues the previous one: "Why? Well, ...", "Why does that matter?", "Now bring it home.", "It works both ways.", "But here's a two-minute check." Same layout every slide (text top-left, illustration bottom-right).
- Hook: "WHAT A BAD DAY FOR NVIDIA MEANS TO YOU." (current event + "you") + "Swipe to know".
- Caption (~260 chars). First ~125: "Nvidia's fall could hit your portfolio too. Even if you don't own its shares, your index fund probably does." Then "So, how diversified is your index fund portfolio really? Let us know in the comments!" + "Follow @finshots.in for more stories behind the numbers." Restates the thesis in 2 sentences, ends with a comment-bait question.
- Clarity: 9/10 (slides 7-9 are long but each starts with a bridge word and has one picture). The only 'clever' device is the basket metaphor, shown literally.

### FS2 - https://www.instagram.com/p/DfpHr4wFG6h/ ("Is pollution shrinking India's economy?")
- 2d | carousel 8 slides | 431 likes, 5 comments, 20 shares
- S1: heavy orange/red condensed caps over a dramatic image (burning-earth, factory smoke): "IS POLLUTION SHRINKING INDIA'S ECONOMY?" + dek "India's 176th environmental rank comes with a $260 billion bill." + "Swipe to know". ~20 words. Job: hook (question + a big number).
- S2: "India has landed second from the bottom in the world's environmental rankings. It ranked 176th out of 177 countries... Only Laos did worse. That's the headline everyone's talking about. But what does this actually cost India?" ~45 words + illustration (rank cards 174/175/176/177). Job: context + tension.
- S3: "A report by Dalberg and the Clean Air Fund found that fine particulate matter pollution alone cost Indian businesses $260 billion in lost revenue in 2024... roughly 6% of India's GDP... 3.5 times the government's entire annual health budget" ~55 words + donut chart. Job: proof.
- S4: "this isn't a problem that's sitting still. Back in 2021... $95 billion, or 3% of GDP. In three years, that figure had nearly tripled." ~50 words + two pie charts. Job: trend.
- S5: Davos / Gita Gopinath said "air pollution posed a bigger threat to India's economy than any tariff the US could impose." ~40 words + balance scale illustration (factory vs US flag). Job: authority + framing.
- S6: "But carbon adds a twist. Countries report only emissions released inside their borders, so when India makes goods for export, the carbon stays on its books." ~30 words + illustration (factory, truck). Job: explain a hidden mechanism.
- S7: "So while India's environment ministry argues over rankings and methodology, businesses are absorbing a bill that dwarfs most trade disputes..." ~40 words + illustration.
- S8 (dark end card): "Do you think India can afford to treat pollution as an environmental problem when the government and businesses are already paying for it like an economic one?" + "Follow @finshots.in for more such content!"
- Message: "Pollution is not only a health or environmental issue - it already costs India about 6% of GDP."
- Readability: grade ~9; only one technical term "fine particulate matter" (not explained but not needed). Bridge words: "But what does this actually cost India?", "this isn't a problem that's sitting still", "But carbon adds a twist."
- Caption (~330 chars). First ~125: "Is pollution shrinking India's economy? India ranked 176th out of 177 countries in the 2026 Environmental Performance Index. But the price tag is steeper than the rank..." ends "Do you think India is treating pollution like the economic problem it has become? Tell us in the comments!" + follow CTA.
- Clarity: 9/10. The headline is a plain question; the dek has the number.

### FS3 (weaker contrast) - https://www.instagram.com/p/De_xfBtFASV/ ("Your plate has a 90-day shelf life")
- 2w (Oct 27) | carousel 9 slides | 238 likes, 9 comments, 3 shares
- S1: blue background, boxed heavy sans "YOUR PLATE HAS A 90-DAY SHELF LIFE" + dek "The birth of fibremaxxing & the next food trend"; phone mock-up of a TikTok + food bowls. ~15 words.
- S2-S8: text + small food/brand picture (cheese->whey liquid; "70%" donut; detox water; TikTok logo; Lindt + Coca-Cola; "13%" food waste; veg bowl). ~45-55 words each.
- S9: dark end card "Which food trend did you fall for first?" + follow CTA.
- Message: "Social-media food crazes force big food companies to chase 90-day trends, causing waste."
- Readability: grade ~11-12. Needs cultural knowledge (Dalgona coffee, Brookie, FMCG, 'Dubai-style chocolate bar'); FMCG is never defined; "shelf life" for a trend is clever but the headline does not say the topic.
- Clarity: 6/10. "Your plate has a 90-day shelf life" is a clever line that does NOT work on its own: topic and benefit are unclear; "fibremaxxing" is in-group slang.
- Best-vs-weak (Finshots): FS1/FS2 headlines state the subject and the personal stake; FS3 is a metaphor + slang. FS1/FS2 have an everyday-object analogy (basket, balance scale) shown literally; FS3 has no unifying analogy and ends up a list of brand anecdotes. Likes 576/431 vs 238. [INFERENCE: partly topic].

Account patterns (Finshots): [OBSERVED] 8-10 slides, 40-60 words per text slide, left-aligned, ~4 sentences, 1 bold phrase per slide for the key number, one flat illustration per slide, dark end card with 1 question + brand CTA. Slides flow by bridge words ("Why?", "Now bring it home.") rather than digits. Captions: 2-3 sentences + question + "Follow @finshots.in for more stories behind the numbers."


---

---
## ACCOUNT 10: @theschooloflifelondon (967K followers; premium, quiet, serif-adjacent; the closest style match to Tangent)
Why picked: philosophy/psychology for a general audience, calm and classy look, nearly every post is a 7-9 slide carousel. (@theschooloflife is a private placeholder; the real handle is theschooloflifelondon.) Note: its type is a geometric sans, not serif, on flat pastel backgrounds; the "classy" feel comes from colour, spacing and restraint. Every slide of all three carousels below was viewed.

### TS1 (best) - https://www.instagram.com/p/DfoXOjvFwID/ ("Why Only the Happy Single Find True Love")
- 3d | carousel 9 slides | 4K likes, 40 comments, 116 shares
- S1: sage-green background; a vintage B/W portrait photo of a woman (hand on chin) in a square with a thin margin; title in a grey-black rounded sans, 2 lines, centered at bottom: "Why Only the Happy Single Find True Love". 8 words. ~55% image / 45% text, lots of margin.
- S2-S9: flat sage-green, ONE paragraph of 4 lines centred in the middle of the slide (about 25-30 words, 4-5 lines, ~7 words per line), normal weight sans of ~30px-equivalent, no icon, no photo, no number:
  - S2 "One of the most important rules for choosing a partner well is refusing to rush the decision out of fear of staying single."
  - S3 "Choosing wisely is basically impossible when remaining single feels unbearable. We end up loving the escape from loneliness more than the actual person."
  - S4 "Society doesn't make this easy. Past a certain age, couples stop inviting single friends around as often, maybe unsettled by their independence."
  - S5 "Friendship and real connection get genuinely harder to find once that happens, which is exactly why so many of us cling to someone merely decent."
  - S6 "Sexual liberation was meant to free people from marrying just to access sex. That project only half worked."
  - S7 "Companionship itself is still locked up inside coupledom in a similar way. Being single rarely comes with the same security or warmth."
  - S8 "Until that changes, the only real fix is personal, building an actual, solid peace with the idea of being alone for a long time."
  - S9 "Only then does choosing someone start to reflect their actual merits, rather than simple relief at no longer being on our own."
- One-line message: "If you are scared of being single you will pick the wrong partner, so learn to be alone first."
- Audience: adults 25-45, general; emotionally curious.
- Beat arc: promise (title) -> rule -> why it is hard (fear) -> society makes it worse -> friendship/companionship lock-in -> only fix is personal -> payoff: then you choose well.
- Readability: grade ~9-10; concrete everyday phrases ("inviting single friends around", "cling to someone merely decent"); abstract words ("independence", "companionship") are in context. Sentences 10-22 words but split by the slide break so each slide is read in ~6 seconds.
- Cohesion: [OBSERVED] ONE continuous argument written as a chain, where every slide continues the previous sentence's logic with a connective: "Choosing wisely is..." (answers S2), "Society doesn't make this easy" (but), "Friendship ... get harder once that happens" ("that" refers to the previous slide), "Until that changes", "Only then does...". Same background colour on all inner slides = no decoding of layout. Dots show 9.
- Hook: [OBSERVED] a paradox title ("Why Only the Happy Single Find True Love") + a vintage portrait. Reads plainly: no slang, 8 words. Stops thumb via a counterintuitive claim about a universal desire (love).
- Caption (~700 chars). First ~125: "A useful private test, imagine the exact relationship you're currently in or considering ending, then imagine five ordinary Tuesdays alone afterwards, no plan, no one to call first." It does NOT restate the slides; it gives a practical exercise (an extension), then promotes membership ("Our membership has a dedicated space for single people navigating dating...") and no hashtags seen.
- Clarity: 9/10. The title is a paradox that is decoded by slide 2 in one sentence. Cleverness works because "the happy single" is a familiar phrase.

### TS2 - https://www.instagram.com/p/Dfq8CMOl8Ee/ ("The Most Successful Person You Know Is Just as Anxious as You Are")
- 2d | carousel 9 slides | 3.2K likes, 21 comments, 153 shares
- S1: pale Munch-like painting (face) in the background; a white square card centred with the title in 4 centred lines of rounded sans, grey text. 13 words. Text ~50%.
- S2-S9: lilac background, one centred paragraph of 25-33 words each (4-5 lines):
  - S2 "Most of what makes us anxious on a given day looks specific: a party, an email, a flight. Zoom out far enough and a different picture appears."
  - S3 "Anxiety isn't really a reaction to this week's problems. It's closer to a permanent feature of being alive, one that just latches onto whatever's nearby."
  - S4 "We tend to fantasise that calm is waiting somewhere specific, a beach eleven hours away, a perfectly decluttered home, a certain amount of money or status."
  - S5 "None of these actually work. There is still anxiety at the beach, in the tidy house, after the deal closes, and in the arms of whoever we've just fallen for."
  - S6 "There are real reasons for this. Fragile bodies, huge decisions made on incomplete information, and nervous systems still wired for the savannah, not the suburbs."
  - S7 "The single most useful move is acceptance. Feeling anxious isn't proof that life has gone wrong. It's mostly just proof that we're alive."
  - S8 "It helps enormously to remember how universal this actually is. Even the person who looks entirely calm and successful is carrying roughly the same weight."
  - S9 "We're mostly left to suffer this alone. But we can still turn to the people next to us and say, honestly, I know exactly what that feels like."
- Message: "Everyone is anxious, it's part of being alive, and saying so to someone helps."
- Readability: grade ~8-9; concrete lists ("a party, an email, a flight"; "a beach eleven hours away"); one funny-literal metaphor ("wired for the savannah, not the suburbs"), which is instantly decodable because the contrast is stated.
- Cohesion: same chain pattern: S3 corrects S2, S5 refutes S4 ("None of these actually work"), S6 "There are real reasons for this", S7 "The single most useful move", S9 emotional ending. Colour-per-post (lilac) rather than per-slide.
- Hook: a status-reversal title ("The most successful person you know is just as anxious as you are"): clear, reassuring and a bit surprising.
- Caption (~900 chars) starts: "Two of the more useful responses to anxiety rarely get much credit. The first is laughter, which is really just relief given a shape..." - it ADDS a second idea (laughter + hugging) instead of restating. Ends with a pointer to an article and membership.
- Clarity: 9/10.

### TS3 (weak) - https://www.instagram.com/p/DfjNEwXDdcD/ ("Four Ways of Coping With Anxiety")
- 5d | carousel 7 slides | 951 likes, 7 comments, 24 shares
- S1: abstract blocks of blue/beige/navy (looks like a flag) above a cream banner with title "Four Ways of Coping With Anxiety". The art has no relation to the content; 7 words.
- S2: "Anxiety and an ordinary bout of nerves are not the same condition, though they often get talked about as if they were." (~24 words)
- S3-S6: numbered cards "1. Understanding the Past Projected Forward." / "2. Understanding Internalised Aggression." / "3. Companionship." / "4. Acceptance." each with a 2-3 line bold label + ~25 word explanation, e.g. "Anger we were never allowed to feel as children doesn't disappear. It often returns later as a vague, constant sense that everyone's against us."
- S7: "None of this makes anxiety a curse. It's a genuine nuisance that can shape a life without needing to ruin it."
- Message: "Four psychological ways to cope with anxiety: history, buried anger, other people, acceptance."
- Readability: grade ~10-11; labels are clinical terms ("Internalised Aggression", "Past Projected Forward") with an explanation ONE slide later in the same slide, but the labels are the biggest text, so a skimmer sees jargon.
- Clarity: 7/10. Title is clear. Numbered slides are good for skimming but the labels are abstract and the cover art is generic.
- Best-vs-weak difference (School of Life): TS1/TS2 have a title that makes a surprising specific claim about the reader ("The most successful person you know is just as anxious as you are") and then a continuous, plain-spoken argument with no labels. TS3 has an informational title ("Four Ways of Coping With Anxiety") + jargon labels + unrelated art. Engagement 4K / 3.2K vs 951 likes. [INFERENCE] a reader-centred, mildly surprising claim beats a "listicle of concepts" even in the same style.

Account patterns (School of Life): [OBSERVED] 7-9 slides; slide 1 = artwork (vintage portrait, painting, geometric pattern) + a 7-13 word title in centred rounded sans; slides 2+ = flat single colour (sage / lilac / cream), ONE centred paragraph 22-33 words, 4-5 lines, no images, no bold (except labels in a numbered variant), no brand marks on inner slides. A colour per post. Captions are separate content (an exercise or an extra idea), 600-900 chars, no hashtags, closing with link to article/membership. [INFERENCE] The "quiet and classy" effect is made of three things: a restrained 2-colour palette per post, huge margins, and continuous prose chained slide-to-slide.


### TS4 - https://www.instagram.com/p/DflycGPjX27/ ("How to Stop Fearing the Worst Case", Seneca)
- 4d | carousel 9 slides | 2.5K likes, 23 comments, 93 shares
- S1: pink geometric pattern (alternating light/dark red bars) above a cream banner; serif-like rounded sans title "How to Stop Fearing the Worst Case" (7 words). S2-S9 on flat cream, one centred paragraph each (24-30 words): "Most of us wildly overestimate how fragile we actually are, assuming disaster the moment life falls short of comfortable." / "Commercial society spends a lot of effort convincing us that heated car seats and business class flights are necessities rather than luxuries." / "In truth our real needs are much simpler. We could manage being poor, unpopular, or living alone far better than we assume, we just never test it." / "Seneca ran what we'd now call a venture capital firm, owned beautiful villas, and still regularly slept on an outhouse floor eating stale bread." / "He wasn't punishing himself. He was proving to his own nervous system that losing everything wouldn't actually be unbearable, just uncomfortable." / "That proof gave him real confidence in business, because the worst case stopped being a catastrophe and started being simply survivable." / "Our culture tells endless rags to riches stories. It would do us more good to hear riches to rags stories where people coped just fine." / "Fear of loss holds most of us back more than any actual danger does. Getting reacquainted with what we could survive tends to make us braver."
- Message: "Practising small discomforts shows you the worst case is survivable, so fear shrinks."
- Clarity: 9/10. A known-figure story (Seneca as a "venture capital" owner) translates ancient philosophy into a modern phrase; the chain pattern is the same (claim -> wrong belief -> truth -> example -> proof -> moral). The "rags to riches / riches to rags" inversion is a clever line that works because the familiar phrase is flipped, and the flip is explained in the next sentence.


---
## ACCOUNT 11: @aeonmag (100K followers; serif, black or muted-blue; magazine of ideas)
Why picked: this is the nearest visual match to Tangent (dark/muted, serif display title, small sans deck, byline). Serif title + short sans dek + photo + byline + logo. Studied to see what premium serif posts cost in engagement.

### AE1 (best) - https://www.instagram.com/p/DfXxM0iF9DX/ ("Ways of living", on John Berger)
- 1w (Nov 6) | carousel 2 slides | 1.1K likes, 7 comments, 57 shares
- S1: slate-blue background; tiny caps label "ESSAY / CULTURE"; serif title "Ways of living" (large, ~7% of width per letter, left-aligned); sans dek "John Berger's Ways of Seeing exploded a discipline. But his greatest legacy might be a quieter project of re-enchantment" (~21 words); a landscape photo of Berger standing in snow; "by Joshua Sperling" + "aeon" logo bottom. ~35 words. Text 50% / image 40% / whitespace 10%.
- S2: same blue; a single paragraph in sans about Berger (~50 words) ending "Read more at aeon.co". Job: payoff/teaser + CTA.
- Message: "A centenary essay on John Berger and his gift for noticing the world."
- Caption (~700 chars). First ~125: "The question, John Berger once said, is of 'continually learning to be embedded in life'. Berger's 'Ways of Seeing' captured young imaginations and changed the way that people saw the world..." = the essay's own opening, a quote hook. CTA: link in bio.
- Clarity: 7/10. A famous name carries the hook; the title "Ways of living" is a riff on "Ways of Seeing" that only works if you know it. [INFERENCE] a clever line that works for the in-group only.

### AE2 (weak) - https://www.instagram.com/p/DfrfGnnFwT5/ ("Fugitive imagination")
- 2d | single image (img_index=2 returns the same image) | 125 likes, 3 comments, 9 shares
- Visual: pure black background; tiny mono caps "ESSAY / SOCIETY"; white serif title "Fugitive imagination" (big, left-aligned); sans dek "Wherever people are confined, displaced, silenced or made disposable, fugitive forms of knowledge and imagination emerge" (~19 words); a framed photo of people walking by a mural; "by Shahram Khosravi" and "aeon" bottom. ~25 words. Layout is textbook "dark, quiet, classy serif".
- Message: "An essay on how oppressed people create imagination as resistance."
- Clarity: 4/10. "Fugitive imagination" is an academic coinage that needs a decoder; the dek is abstract with 4 negative abstract nouns ("confined, displaced, silenced, disposable" + "forms of knowledge"). No concrete picture of what this is about.
- Takeaway: it LOOKS premium and uses the same template as AE1 but got 1/9th the likes. The look is not the problem; the abstract title is.

### AE3 (middle) - https://www.instagram.com/p/DfqL7gzlzPF/ ("Slow hope")
- 2d | single | 214 likes, 6 comments, 10 shares
- Visual: full-bleed photo of Greta Thunberg listening at a conference, tiny logo top-right, serif title "Slow hope", dek "Climate change is an emergency but despair is not the answer. The world is full of untold stories of people-powered change", byline. ~25 words. Text bottom-left over a darkened photo.
- Clarity: 7/10. "Slow hope" is a small oxymoron; the dek explains it in plain words; the famous face helps. Gets ~2x the AE2 likes with the same template.
- Best-vs-weak difference (Aeon): AE1 (a known figure + a decoded title + 2 slides + a read-more CTA) vs AE2 (abstract coinage, no face/name, 1 slide). AE3 sits in between because the dek translates the title into a plain thesis.

Account patterns (Aeon): [OBSERVED] 1-2 slides; the title is serif and at most 3 words; the dek is a sans sentence of ~20 words; byline + logo are tiny; background is black, slate blue or a darkened photo; labels ("ESSAY / SOCIETY") in small mono caps. Engagement varies 125 - 1.1K by title clarity and name recognition. [INFERENCE] Tangent's serif-on-dark style is fine; the 2-3 word serif title must be a plain subject, and the sans dek must carry the plain claim.

---
## ACCOUNT 12: @sciencealert (903K followers) and @newscientist (1.5M) - science to a general audience
Why picked: the requested "one more science explainer"; both post headline cards.

### SA1 - https://www.instagram.com/p/DfvwgBYDMWW/ ("Coffee doesn't just help you poop...")
- 10h | single | 259 likes, 5 comments (young post)
- Visual: photo of an espresso drip with a left-aligned bold sans headline over a dark gradient: "Coffee Doesn't Just Help You Poop. It May Change The Physiology in Your Gut." (key words in amber-yellow: "Coffee", "Physiology in Your Gut"). "BY JESS COCKERILL" + logo. ~16 words. Text ~30%.
- Caption (~900 chars): "Regular coffee consumption may have a few other interesting effects on your gut, beyond getting your bowels going." then study details (61 participants, Denmark/Singapore/Belgium, PRIMA). Details are included.
- Clarity: 9/10. Plain conversational line (a familiar effect, then an unfamiliar one); colour-highlighted keywords.

### SA2 - https://www.instagram.com/p/DfvOQnCjGvi/ ("A mysterious object in space pulsed every 62 minutes. Then it vanished.")
- 15h | single | 142 likes, 4 comments
- Visual: night-sky radio dishes with red lights; headline "A Mysterious Object in Space Pulsed Every 62 Minutes. Then It Vanished." (14 words, amber on "Every 62 Minutes" and "Vanished"). Caption opens "There, in the data, every 62.2 minutes: another powerful flare of radio waves from a mysterious source." Technical term "long-period transients (LPTs)" is introduced in the 4th caption paragraph and defined as "unidentified objects that emit long, bright pulses of radio waves..."
- Clarity: 9/10. Two-sentence mystery structure (what + twist) with a number.

### SA3 (weakest) - https://www.instagram.com/p/DfwuMNZF3r-/ ("Strange 'Metal Potatoes' Contain a Microcosm of Life...")
- 1h | single | 37 likes, 1 comment (too young; not comparable)
- Visual: seafloor nodules photo; headline "Strange 'Metal Potatoes' Contain a Microcosm of Life Not Seen Anywhere Else on The Seafloor, Scientists Find" (~19 words, amber highlights on 'Metal Potatoes' and 'Microcosm of Life').
- Clarity: 7/10. "Metal potatoes" is a funny visual nickname (good), but "Microcosm of Life Not Seen Anywhere Else" is wordier; caption explains "polymetallic nodules" after the nickname.
- Best-vs-weak (ScienceAlert): the coffee and "62 minutes" cards say one familiar thing + one surprise in 14-16 words; the nodule headline is 19 words with 3 clauses. [INFERENCE] shorter + familiar > longer; likes are not comparable because posts are 1-15 hours old.

### NS1 - https://www.instagram.com/p/Dfkt0T6DahF/ (New Scientist, "Global carbon emissions are expected to decrease 0.4% in 2026")
- 4d | carousel 2 slides | 1.5K likes, 44 comments, 46 shares
- S1: white page, small "Environment" label, serif headline "Global carbon emissions are expected to decrease 0.4% in 2026"; sans dek "A view of global carbon emissions for the past two decades, labelled with suspected reasons for 'blips'"; line chart (GtCO2/year, 2006-2026) with three orange hand-drawn annotations: "Covid-19 pandemic", "Global financial crisis", "Energy shock, following Iran conflict", and "Projected" in red; source note. ~40 words + chart. Chart = visual explains.
- S2: plain paragraphs (~75 words) on why and what could reverse it.
- Message: "Emissions will fall slightly for the first time in five years, but it's because of an oil shock."
- Readability: grade ~11; the chart labels give each dip a plain cause, no decoder needed.
- Caption (~600 chars): "Carbon dioxide emissions from fossil fuels are expected to drop this year for the first time in five years." then explanation, "Tap the link in our bio to read more."
- Clarity: 8/10. The annotated chart is the kind of visual that does the explaining.

Account patterns (ScienceAlert / New Scientist): [OBSERVED] ScienceAlert: single card, headline = what + twist, 2 amber keyword highlights, bold sans, byline, logo; New Scientist: white page, serif headline, annotated chart, 2 slides. Captions are mini-articles (600-900 chars) with the study details; CTA = link in bio.

---
## ACCOUNT 13: @nasdaily (4.7M followers) - checked, not usable for this study
[OBSERVED] The first 12 grid items are all reels (clips) plus 3 pinned reels; no carousel or still seen. Swapped out; its slot is covered by @finshots.in (explainer for general public, India) and @theschooloflifelondon.

Also checked and excluded: @finshots (private placeholder), @theschooloflife (private placeholder), @thefutur (dead), @sciencenaturepage (0 posts), @interestingengineering (first 12 items are reels), @bigthink (not found).

---
## Coverage update
Posts analysed with every slide viewed: 33 total.
- Round 1: MB1, MB2, MB3, AW1, AW2, KG1, KG2, NA1, VV1, VV2, VV3, VV4, VV5, SB1, SB2, SB3, VX1 (now all 6 slides), VX2, AX1 (now all 5 slides) = 19
- Round 2: FS1, FS2, FS3, TS1, TS2, TS3, AE1, AE2, AE3, SA1, SA2, SA3, NS1 = 13  -> subtotal 32 (+ the 3 single-image Aeon/ScienceAlert posts count once each, included above). Total: 32 posts.
(Single-image posts have 1 slide, which was viewed.)
Method limits: screenshots only; likes for posts younger than 1 day are not comparable.

---
# HOW PREMIUM ACCOUNTS STAY SIMPLE (Tangent-specific; dark, quiet, classy, serif)

Evidence base: @theschooloflifelondon (TS1-TS3), @aeonmag (AE1-AE3), @visualizevalue (VV1-VV5), @nasa (NA1), @kurzgesagt (KG1-2), @sahilbloom (SB1-3).

1. Type size and weight. [OBSERVED] Cover title: 7-13 words in a single weight, centred (School of Life) or left-aligned (Aeon), roughly 3-4 lines of ~4 words each, filling 40-60% of the card width. Inner slides (School of Life): one paragraph at roughly the size where a 4-5 line block fills about 60-65% of the card's width and ~35% of its height. Premium accounts use ONE typeface weight for the body; hierarchy is created by position and size, not by bold/italic/colour changes. Aeon: serif title large + sans dek ~1/3 the size; label is tiny mono caps. [INFERENCE] Two sizes + one weight is the limit; add a third only as a tiny label/byline.
2. Word count. [OBSERVED] Cover: 7-13 words (TS1 8, TS2 13, TS3 7, AE1 ~35 incl. dek, AE2 ~25, VV 0, NASA 0). Inner slides: 22-33 words (all 16 School-of-Life inner slides read 21-33), ~4-5 lines, 6-8 words per line, sentences of 8-22 words. Visualize Value / NASA / Kurzgesagt: 0 words on slide, with the idea in the caption. Over 45 words/slide appears only in less engaging posts (AX1 65-95, VX1 slide 5 ~70, FS 45-60 works only with a picture on each).
3. Whitespace. [OBSERVED] School of Life inner slides: text block occupies ~40% of the area; margins ~15% each side; nothing else on the slide (no logo, no page number except the dots). Visualize Value: ~90% empty (VV4, VV1 slide 5). Aeon: title block top, photo middle, byline bottom with a clear 8-10% margin. [INFERENCE] If you can't add whitespace, remove words.
4. Image vs caption. [OBSERVED] Three patterns: (a) all words ON slides, caption adds new content (School of Life, Warikoo); (b) nothing on image, all words in the caption (NASA, Kurzgesagt, VV); (c) short title on image + dek, long caption mirrors the essay (Aeon, ScienceAlert). The ones that look most premium (b and a) never repeat the same text in both places. [INFERENCE] Use the slide for the claim and the caption for the extra, not the same sentence twice.
5. Colour. [OBSERVED] One background colour per post (sage, lilac, cream, slate-blue, black); one text colour; zero gradients except under photo text. Visualize Value: black or white only. School of Life: photo on cover, flat colour inside. Highlight colour is used in news brands (amber in ScienceAlert; lime in Finshots) and NOT in premium accounts.
6. Imagery. [OBSERVED] Premium covers use a single, slightly unusual image (vintage portrait, Munch painting, a lone silhouette, a gold disc) rather than icons or diagrams. Inner slides: no images (School of Life) or 1 picture (Finshots, but its look is playful, not premium).
7. Titles stay plain even when the look is quiet. [OBSERVED] "Why Only the Happy Single Find True Love"; "The Most Successful Person You Know Is Just as Anxious as You Are". The lower-engagement quiet ones were abstract: "Fugitive imagination" (125 likes), "Four Ways of Coping With Anxiety" (951), "Artificial Super Intelligence" (243). [INFERENCE] Quiet does not mean cryptic; the thumb-stopping line should still be a full sentence that states a claim.
8. Chain slide to slide. [OBSERVED] Each inner slide starts with a bridge ("None of these actually work.", "Society doesn't make this easy.", "Until that changes,", "Only then does..."). A reader never needs to remember layout; they only follow the sentence.

---
# TEMPLATES TANGENT COULD BORROW

Each is a slide-by-slide skeleton. Replace the example topic with a Tangent one (e.g., a photo-edit story or the Panditji app). Word counts are targets from the evidence above.

## T1. "Quiet Argument" (School of Life)
Examples: https://www.instagram.com/p/DfoXOjvFwID/ , https://www.instagram.com/p/Dfq8CMOl8Ee/ , https://www.instagram.com/p/DflycGPjX27/
- S1: one image (photo/painting) + a 8-13 word plain title that states a surprising claim about the reader. Serif title in a card or at the bottom, big margins.
- S2: the plain version of the problem in 25 words ("Most of what makes us X looks specific: a, b, c.").
- S3: the reframe (25 words).
- S4: the common wrong fix.
- S5: "None of these actually work." + why.
- S6: the real reason (one concrete image).
- S7: the useful move (acceptance / do this).
- S8: "It helps to remember..." (reassurance).
- S9: the human close ("We can turn to the person next to us and say...").
- All inner slides: same flat dark background, one centred serif paragraph of 21-33 words, no icons. Caption = a DIFFERENT idea (exercise), not a recap.
- Tangent use: "Why I edit photos with AI I won't use for faces" as a reflective post.

## T2. "Numbered Rules + Face" (Warikoo)
Example: https://www.instagram.com/p/Dfun_mRmtiS/
- S1: "N things I do/learned about X. [credibility detail]" in a card over a personal photo (16 words).
- S2-S(N+1): "1. <bold rule>." + 2 plain sentences with one concrete detail (30-45 words), same card position, a new photo each time.
- Last: "These are mine. They may not be yours." + a question.
- Caption: restate the thesis in 2 sentences, then "Save this."
- Tangent use: "5 rules I follow when I edit a photo with AI" over before/after crops.

## T3. "Dated Timeline" (Morning Brew)
Example: https://www.instagram.com/p/Dfqghnpk6AU/
- S1: full-bleed image + "THE <NOUN> OF <NAME/THING>" + "SWIPE FOR MORE".
- S2-S7: identical frame, title "<NAME>'S <NOUN>: A TIMELINE:", date label, 1-5 bullets of 8-12 words with the key phrase coloured, one photo.
- Tangent use: "How I built Panditji in 7 days": Day 1 ... Day 7, with a screenshot each.

## T4. "Basket Explainer" (Finshots)
Examples: https://www.instagram.com/p/Dfrk61HlAa2/ , https://www.instagram.com/p/DfpHr4wFG6h/
- S1: "WHAT <EVENT> MEANS TO YOU" (or a question + number dek) + swipe cue.
- S2: scale in a familiar comparison (a total everyone knows).
- S3: the "you may have felt it" personal line.
- S4: define the concept as an everyday object (basket, scale) with a matching illustration.
- S5-S8: one number per slide, converted to a "per Rs.100" or "per day" view; start each slide with a bridge ("Why does that matter?", "Now bring it home.").
- S9: "two-minute check" (what to do).
- S10: dark end card = one reflective question + follow.
- Tangent use: "What an AI 'seed' actually does to your photo" with a die/lottery drum analogy.

## T5. "One Image, One Claim" (Visualize Value / NASA / Kurzgesagt)
Examples: https://www.instagram.com/p/DdVKYsgEdtq/ , https://www.instagram.com/p/DdHCilmEcsm/ , https://www.instagram.com/p/DfkkknjD6vm/
- Slide 1: a single image on a black or white field with no text, one subject at 10% of the frame.
- Slide 2 (optional): second angle/detail, still no text.
- Caption (6-12 words, or 3 short paragraphs for factual posts): states the claim as a sentence; if there is jargon, define it with a number in the same sentence.
- Tangent use: one AI-edited photo from his gallery, caption "This took 4 prompts and 20 minutes." (plain claim).

## T6. "Cover + Annotated Chart" (New Scientist / Aeon)
Examples: https://www.instagram.com/p/Dfkt0T6DahF/ , https://www.instagram.com/p/DfXxM0iF9DX/
- S1: serif headline (<=12 words) + sans dek + one image (annotated chart or photo) + byline.
- S2: one paragraph + "Read more".
- Tangent use: before/after photo with 3 labelled arrows naming what the AI changed.

---
# UPDATED CROSS-ACCOUNT LESSONS (all 32 posts)

Replaces Round-1 lessons where numbers differ; Round-1 lessons that still hold are restated with new evidence.

1. Words per slide. [OBSERVED] Premium carousels (School of Life) = 22-33 words per inner slide, 6-8 words per line; Warikoo = 28-45; Morning Brew = 6-60; Finshots = 40-60 but with one picture per slide; heavy ones were weaker or less skimmable (Axios 65-95, Vox slide 5 ~70, Finshots FS3 45-55). Cover slides: 7-16 words everywhere. Posts that hit 3K+ likes while text-only inside: TS1 (4K), TS2 (3.2K), TS-Seneca (2.5K, https://www.instagram.com/p/DflycGPjX27/).
2. Slide count. [OBSERVED] Premium text-chain carousels run 7-9 (School of Life); numbered-rule carousels 5-7 (Warikoo, Axios); news 3-7 (Morning Brew); explainer with pictures 8-10 (Finshots); art/photo 1-2 (NASA, Kurzgesagt, Aeon, VV). The best-performing long carousels (TS1, FS1) kept every slide to ONE idea and began each with a bridge word. [INFERENCE] Length is not the problem; skimmable repetition is.
3. Headline vs visual. [OBSERVED] 4 working patterns: (a) headline over a photo (Morning Brew, ScienceAlert); (b) zero text on image, caption states the claim (NASA, Kurzgesagt, VV); (c) bold line + 1-2 sentences in a card (Warikoo, Axios); (d) title + painting/photo on slide 1, plain paragraphs after (School of Life). In all, the headline is literal. [OBSERVED] Where the visual is abstract AND the caption is a topic label (VV5 "Artificial Super Intelligence" 243 likes; AE2 "Fugitive imagination" 125 likes; TS3 abstract cover art 951) engagement is 5-10x lower than comparable posts in the same account.
4. Jargon. [OBSERVED] NASA "light-day (16 billion miles)"; Finshots "index fund... The S&P 500 is a list of 500 big US companies" then a basket drawing; ScienceAlert "polymetallic nodules" after calling them "metal potatoes"; School of Life uses everyday words ("beach eleven hours away"). Failure cases: Finshots FMCG/"fibremaxxing" (FS3) and Aeon "fugitive imagination", Axios acronyms (DCCC, AdImpact). Rule: nickname/analogy first, label second.
3b. Analogies that worked were SHOWN, not just said: basket (FS1), balance scale (FS1, FS2), "single switch" (KG1), two shapes for focus (VV2).
5. Hooks. [OBSERVED] Wording types: (a) personal claim about the reader: "The Most Successful Person You Know Is Just as Anxious as You Are" (TS2), "Why Only the Happy Single Find True Love" (TS1); (b) personal stake in news: "What a bad day for Nvidia means to you" (FS1); (c) number + persona: "5 money rules my wife and I follow. We're 45, with two kids." (AW1); (d) question with a number: "Is pollution shrinking India's economy?" + "$260 billion bill" (FS2); (e) mystery + twist: "Pulsed Every 62 Minutes. Then It Vanished." (SA2); (f) belief reversal in a caption (KG1). None use a riddle; all are readable aloud once.
6. How slides chain. [OBSERVED] Strongest chain = bridge words at the start of each slide ("But what does this actually cost India?", "Why does that matter?", "None of these actually work.", "Until that changes,", "Only then does..."); also numbering ("1." to "5."), dates (MB1), same frame/colour. Weak chain = a list of labels (TS3) or brand anecdotes (FS3).
7. Captions. [OBSERVED] Four types: (a) mini-article (ScienceAlert, Vox, Aeon, New Scientist, NASA); (b) a NEW idea not on the slides (School of Life); (c) thesis restated + question (Finshots, Warikoo); (d) 2-11 words (VV). Hashtags: none in 9 of 12 accounts; 3-4 only at NASA and Sahil Bloom. CTAs: "link in bio" (news), "Save this" (Warikoo), question for comments (Finshots, Warikoo, Sahil), membership (School of Life). First lines are plain claims.
8. How premium accounts stay simple. See the dedicated section above; short version: one colour, one weight, one idea per slide, wide margins, a plain title, and the caption carrying the extra.
9. What separates most- from least-engaged. [OBSERVED within accounts] Finshots 576/431 vs 238 (plain stake vs slang metaphor); School of Life 4K/3.2K vs 951 (reader-claim vs concept-list); Aeon 1.1K vs 125 (known name + translatable title vs coinage); VV 2.3K/1.5K vs 243 (stated claim vs topic label); Warikoo 12.3K vs 2.6K (numbered personal vs abstract poster). [INFERENCE] The one common factor is how fast a stranger can say what the post is about in one sentence.
10. "Clever" lines that work, extended. [OBSERVED] "Why Only the Happy Single Find True Love" (paradox on a familiar phrase), "Boring is beautiful" (explained by the list above), "Death isn't a single switch" (familiar object), "metal potatoes" (a nickname that is instantly visual), "wired for the savannah, not the suburbs" (contrast both halves familiar), "What a bad day for Nvidia means to you" (plain). Those that fail: "Your plate has a 90-day shelf life" (no topic named), "Fugitive imagination" (coinage), "Ways of living" (needs Berger), "Artificial Super Intelligence" with a hand-lamp (no stated claim). Rule of thumb [INFERENCE]: a clever line works when the reader can say what it means BEFORE slide 2, from the same slide.

## UPDATED rules a writer could follow (supersedes Round-1 list where different)
1. Title = 8-13 words, a full sentence with a stake for the reader or a surprising claim; no coinages, no slang, no topic labels.
2. Chain: every inner slide opens with a bridge ("But", "So", "Why does that matter?", "None of these actually work.", "Until that changes,", "Now bring it home.").
3. Inner slides: 22-33 words, 4-5 lines, one centred or left-aligned block, one weight, same background colour for the whole post.
4. One idea per slide; one number per slide; convert numbers to something familiar ("per Rs.100", "per day", "x% of a thing everyone knows").
5. Show analogies (basket, scale, switch). Name the concept only after the picture.
6. Define any unavoidable term in the same sentence with a number or example; otherwise cut it.
7. Cover: one image, little text; for the quiet/premium look keep a margin of ~10-15% and one accent (or none).
8. Close with a human line or a question; then CTA (save / link in bio).
9. Caption: a new idea or an exercise (premium) or a 2-sentence thesis + question (explainer); first line is a plain claim; 0-3 hashtags.
10. Slide count: 5-9 when each slide advances the argument; 1-2 when the image carries it.


---
# APPENDIX: Round-1 lessons (superseded by the UPDATED lessons above; kept for the record)
# CROSS-ACCOUNT LESSONS

1. Words per slide. [OBSERVED] The highest-engaged carousels used 25-45 words per slide: AW1 (12.3K likes, 28-45 words), MB1 (1.5K, 30-60). The dense ones cost clarity: AX1 slides had 65-95 words and 25-word sentences (https://www.instagram.com/p/DfUt7bPgQUW/); VX1 slide 3 had ~75 words. Cover slides used 8-16 words (MB2, MB3, AW1, AX1). Number-only slides ("430 MILLION", MB3) used 6.
2. Slide count. [OBSERVED] Winners: 3 (MB3, 2.7K), 5-7 (AW1, MB1, AX1, VX1), or 1-2 (NASA 560K, Kurzgesagt 17K, VV, SB). Nobody exceeded 8. [INFERENCE] Count matters less than "each slide = one new thing"; the 7-slide Nvidia timeline felt short because every slide had the same frame and a new date.
3. Headline vs visual. [OBSERVED] Three patterns: (a) headline over photo as a news sentence (MB2, MB3, AX1); (b) image with zero text + caption makes the point (KG1/2, NA1, VV3, VV4); (c) bold one-line headline in a card + 1-2 plain sentences (AW1, AX1 inner slides). In all, the headline on the image is a complete, literal statement; none needed decoding.
4. Jargon. [OBSERVED] NASA translates the unit immediately ("one light-day (16 billion miles)", https://www.instagram.com/p/DfkkknjD6vm/). Morning Brew uses almost no jargon; Vox names "Endozoicomonas" but surrounds it with "a type of bacteria called". Axios leaves insider acronyms unglossed, which pushed readability down. Rule: define in the same sentence or skip it.
5. Hooks. [OBSERVED] Wordings: "5 money rules my wife and I follow. We're 45, with two kids." (number + persona); "THE FALL OF NVIDIA'S JENSEN HUANG / SWIPE FOR MORE"; "Why are so many young guys taking Viagra?"; "Death isn't a single switch that shuts down your entire body at once." (belief reversal); "I'm convinced that 99% of success is just the ability to stay in the game. Do you agree?" None are stylised riddles; each could be read aloud and understood once.
6. How slides chain. [OBSERVED] (a) identical frame + running numbers (AW1 "1." to "5."; AX1 "1./2./3."); (b) dates as a spine (MB1); (c) one speaker quote per slide escalating (MB2). No account used "but/so" bridges on slides; progress is carried by numbering/dates and repeating frame. [INFERENCE] Template repetition is what lets the reader skip decoding the layout and focus on the new line.
7. Captions. [OBSERVED] Three types: (a) restate-and-extend in line-per-sentence style (Warikoo, Sahil Bloom); (b) the caption IS the article lede (Kurzgesagt, NASA, Vox, Morning Brew: long, 500-900 chars); (c) 2-11 word label (Visualize Value). First line is always a plain claim or question. CTAs: "Save this and write your own." (AW1), "Do you agree?" (SB1/SB2), "Watch our full video to find out!" (KG), "link in bio" (NA, AX, VX). Hashtags: 0 (Warikoo, MB), 3-4 (NASA, Sahil Bloom).
8. How premium-looking accounts stay simple. [OBSERVED] Visualize Value and NASA: one subject, black or white field, no overlay text, 90% empty (VV4, VV3); captions of 2-11 words; the sentence lives in the caption. Kurzgesagt: a signature illustration style, zero on-image words. [INFERENCE] For Tangent's dark serif look: one-sentence headline per slide in large serif on dark, with huge margins, is consistent with this - but only if the sentence is literal.
9. Most vs least engaged. [OBSERVED] Top: NASA 560K (iconic object), Sahil Bloom 32K (universal idiom) and Kurzgesagt 17K, Warikoo 12.3K (specific numbered list from a real couple). Weak: VV5 (243 likes; image-only metaphor with topic-label caption "Artificial Super Intelligence", viewer had to guess "Hand-shaped lamp"), Vox coral post 140 likes, Axios wall-of-text carousel. [INFERENCE] Weak = either the idea is not stated, or the topic is niche; strong = a complete, relatable sentence in the first 2 seconds.
10. "Clever" lines that worked. [OBSERVED] "Distraction, Focus" (VV2): two words + two shapes = legend. "Boring is beautiful" (SB2): oxymoron proved by the list above. "Death isn't a single switch" (KG1): familiar object, literal. "circling back" joke in Morning Brew's caption (MB3): corporate cliche. Common thread: a familiar phrase or object, plus a visual/list that decodes it in the same view. Tangent's failed lines ("Checked against the sky's reference books") have no familiar anchor and no visual decoder.

## Rules a writer could follow
1. Slide 1 must be one complete literal sentence (8-16 words) that someone could repeat after one glance. Put a number or a "who" in it if possible.
2. One new idea per slide; 25-45 words max; 6-14 words per sentence; bold the first line, plain text below.
3. Repeat the same frame on every slide and number it ("1." to "5.", or dates).
4. If a word needs a dictionary, either define it in the same sentence with a number, or cut it.
5. Metaphors must be familiar (switch, game, circling back) and decoded within the same slide by a picture or a list.
6. Let the picture carry feeling and the words carry facts; do not make the words stylish.
7. Put the idea into the caption's first line as a plain claim or question; add one clear CTA ("Save this", "Do you agree?", "link in bio").
8. Last slide: close the loop in plain words and ask one question.
9. A topic label ("Artificial Super Intelligence") is not a claim; write the claim.
10. Premium look = space and restraint, not abstraction: big type, huge margins, one subject.

