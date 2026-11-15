# Harvest: AI/tech creators (carousels and stills) - clarity craft study

Collected 2026-11-15 via Claude in Chrome (read-only, own tab). Method note: Instagram CDN image URLs carry query strings and the tool blocked printing them, so I could not curl images; I viewed every slide of each carousel as a zoomed screenshot of my own tab instead (same visual evidence). Likes are hidden on most posts ("Liked by X and others"); comment counts are shown. Direct calls to Instagram's private JSON API were refused by the tool classifier, so I did not use them. All data below is DOM/visual only.

## Access and discovery findings (important)
- [OBSERVED] The candidate accounts are overwhelmingly REEL-FIRST. In the 12 most recent grid items: @cleoabram 0 carousels / 12 reels; @thevarunmayya 0/12; @realrileybrown 0/12 (reels only); @dhruvrathee 0/12; @tiffintech 2/12 (both personal-life "stills/recap" carousels); @harpercarrollai 2/12; @ishansharma7390 2/12 (both lifestyle "Diwali/Apple event" photo dumps); @rowancheung 25 posts total, mostly personal/news recap carousels.
- [INFERENCE] The best carousel craft among well-known tech creators is therefore found in a minority of their posts, so per-account sample sizes are small.
- No login wall, captcha or challenge was hit.

---
## ACCOUNT: @harpercarrollai (690K followers, ~266 posts; Stanford-trained AI computer scientist, ex-Meta; explains AI)

### POST 1: https://www.instagram.com/p/DfsDz6IlfCP/
- date 2026-11-13, carousel, 9 slides, comments 191, likes hidden
- Audience: tech-curious builders (the caption says "Send this to someone building with AI"); medium-high jargon (tokens, agentic loops).
- One-line message: AI companies earn most revenue by charging per token, but the next wave is software that uses AI only at the steps that need it.
- Slides (all viewed):
  1. HOOK. Headline "The days of Tokenmaxxing might be over, y'all." (9 words) over a full-bleed photo of Harper at a laptop; progress bar "TOKENS" top-left, pixel coin icons, "SWIPE >>>" pill bottom right, brand wordmark. Text ratio ~25%, photo ~75%. Face as hero. Serif headline mixed with italic-blue emphasis word "over".
  2. CONTEXT. "LVL 02 - THE BIG SHIFT" label. Headline "The next level: software that selectively uses AI." (8 words) + 1 line body + two comparison cards ("Token-heavy agentic loops" vs "Purpose-built AI systems", ~25 words each). ~65 words. Text ~85%. Cream background, no photo.
  3. TENSION. "Wait - isn't everyone already minimizing tokens?" (6 words) + a definition box ("Token minimization: designing systems that call the model as little as possible...") + a mini diagram (Mode A agent loop vs Mode B built system) + 2-line takeaway "Plot twist: the receipts say otherwise." ~60 words. Photo background with dark overlay.
  4. PROOF. "LVL 04 - CASE FILE: ANTHROPIC" tag + giant "~80%" numeral + "of Anthropic's revenue is usage-based - billed by the token, not flat monthly subscriptions." + 10-square bar visual (8 filled) + source line. ~35 words. Number is the hero.
  5. PROOF 2. "The numbers tell a story." three stat cards ($376M -> $11.6M revenue; ~20X Claude Code users; ~900% revenue growth). ~45 words.
  6. REVEAL. "So what does this actually mean?" + equation tiles "how long agents run x how often they run = revenue grows with both" + 2 sentences. ~40 words.
  7. PAYOFF. "The bigger opportunity is about to go mainstream." + 3 labelled worlds (cleared / you are here / unlocking next). ~60 words.
  8. PERSONA. "Hi, I'm Harper. Why listen to me?" with face photo + credential list (Stanford, Meta, NVIDIA startup). ~45 words.
  9. CTA. "Want to build your AI skills from the ground up?" + "10 Days of AI Basics" + "Comment GUIDE". ~25 words.
- Words per slide ~25-65 (avg ~45): heavier than a typical "simple" carousel. Text-to-visual ranges 25% to 90% text.
- Layout/type hierarchy: always one big headline (serif + italic coloured keyword), one subhead or card block, brand footer and "SWIPE >" cue on every slide. Slide label "LVL 0X" works as numbering (video-game progression metaphor) plus a segmented progress bar bottom centre = visible sense of progress. Consistent frame across slides.
- Readability: grade ~10-12. Jargon: "tokens", "agentic loops", "usage-based". Handled by in-place definition ("Token minimization: designing systems that call the model as little as possible") and by diagram, but only partly; "tokenmaxxing" is insider slang never fully defined for a lay reader. Metaphor: levels/game progress (light decoding). Sentences medium (10-20 words).
- Cohesion: [OBSERVED] "LVL 02..09" numbering, repeated frame, bridging questions as headlines ("Wait - isn't everyone already minimizing tokens?", "So what does this actually mean?"), plot-twist line, "Takeaway" at the end. Strong chain.
- Hook: statement/provocation using insider term; thumb-stopper is the face + bold claim "might be over, y'all" (casual voice). Weak for a general viewer ("tokenmaxxing" undefined).
- Caption: ~590 chars. Starts "Tokenmaxxing might be over & here's what I mean" (restates hook), then "Send this to someone building with AI." (share CTA), then bio paragraph (credentials), then "comment GUIDE" keyword-DM CTA for free series. No hashtags seen. No AI disclosure.
- Clarity verdict: 5/10 for a general viewer (6-7 for tech enthusiasts). Visual design is excellent and slides chain well; clarity is limited by insider jargon and ~45 words per slide. "The numbers tell a story" and "~80%" slides are the clearest (one giant number).
- Persona: face is slide 1 hero and slide 8 ("Hi, I'm Harper. Why listen to me?") - credibility slide inside the carousel; first person throughout the caption.

### POST 2: https://www.instagram.com/p/DUQ_6LXkqR2/ ("Context Windows explAIned")
- date 2026-02-02, carousel, 6 slides, comments 162, shares 10, likes shown only as "Liked by neohiveai and others"
- Audience: general AI-curious users; low jargon.
- One-line message: AI "forgets" because it has a limited working memory; put your important rules at the top and bottom.
- Slides (all viewed):
  1. HOOK "Why AI "forgets" things." (4 words, large blue serif) + subline "It has a limit to how much it can hold in its "brain"" (~15 words) + "Swipe" pill. Text ~35%, rest empty cream card. No face.
  2. "What is a "Context Window"?" (5 words) + 4 pink-chip bullets, ~40 words: "Think of it as the AI's working memory." / "It's the total number of pages the AI can "hold open" at one time." / "The 2026 truth: windows are huge (millions of tokens)..." / "...but "holding a book" != "studying every word.""
  3. "It has "fuzzy" focus." + 3 bullets (~40 words): U-shaped attention, the middle of a long prompt is a "dead zone."
  4. "What happens when it's "full"?" + 3 bullets (~40 words): truncation, first-in first-out, "if your rules were in the first message, they're first to go."
  5. "The strategy." + 3 bullets (~42 words): system instructions, summarize + start fresh, "Data sandwich: Goal at the top, Constraints at the very bottom."
  6. CTA "Want my free AI guide?" + "Comment GUIDE" (~20 words).
- Words/slide 20-45 (avg ~35). Text ~60-70% of each card. Strict repeated template: tag pill top-left, headline as a QUESTION or plain label, 3-4 bullets with tiny pink chips, footer logo. The headline is literally the question the viewer has.
- Readability: grade ~8-9. Jargon ("context window", "tokens", "truncating") defined in place with a plain metaphor ("working memory", "pages the AI can hold open", "pinned memory"). Metaphors are everyday and need no decoding ("fuzzy focus", "dead zone", "data sandwich"). Sentences 8-14 words.
- Cohesion: [OBSERVED] question-as-headline chain (What is -> fuzzy focus -> what happens when full -> the strategy), same frame every slide, one concept per slide; arc problem -> mechanism -> consequence -> fix.
- Hook: problem/curiosity hook naming a familiar frustration ("Why AI forgets things"); anyone who has used ChatGPT recognises it. Quotes around "forgets" signal metaphor.
- Caption: ~560 chars. First 125: "Context Windows explAIned. Context windows in AI are the maximum amount of data - measured in tokens (words, images, or video) - a large language model (LLM) can process..." Caption is MORE technical than the slides (extends with formal definition), ends "Please leave your questions below"; the 162 comments are mostly "Guide" keyword replies (free-guide funnel). No hashtags seen. No AI disclosure.
- Clarity verdict: 8/10. One idea per slide, question headlines, everyday metaphors, short bullets. Minor: ~40 words per slide; "tokens" defined only in the caption.
- Persona: no face on slides; brand wordmark only; credibility lives in caption/profile.

### POST 3: https://www.instagram.com/p/DRukrQYDsWD/ ("AI vs. AGI vs. ASI, explAIned")
- date 2025-12-01, carousel, 6 slides, likes 2.7K, comments 63, shares 124 (strongest of her viewed posts)
- Audience: general viewers confused by acronyms.
- One-line message: AI today is a narrow specialist; AGI would be a human-level learner; ASI would be far beyond us.
- Slides:
  1. HOOK "The Path to Superintelligence" (4 words) as a staircase diagram: AI (Narrow, Today) -> AGI (General, Future) -> ASI (Super, The Singularity). ~20 words in labels. The diagram IS the message. Text ~30%.
  2. "AI / ANI - Artificial (Narrow) Intelligence" + orange tag "where we are now" + 3 labelled paragraphs (The Standard Definition / The "ChatGPT" Exception / The Reality Check), ~70 words. Text ~90%.
  3. "AGI" + tag "the next step" + 3 numbered capabilities, ~75 words.
  4. "ASI" + tag "the inflection point" + The Event / The Mechanism / The Result, ~65 words.
  5. "So, to recap:" 3 numbered one-liners + "Save for future reference / Share to spread the knowledge." ~55 words.
  6. "Welcome!" + photo of Harper + credentials + "My goal is to help everyone understand AI/ML & how it works, while filtering hype." ~55 words.
- Words/slide: 20 on cover, 55-75 on body slides (dense). Template: big blue serif acronym title, orange timeline tag, three labelled blocks.
- Readability: grade ~11-12; jargon heavy (Proto-AGI, singularity, recursive self-improvement) but each term is the slide subject and defined right below; the staircase cover shows the relationship visually first. Concrete image: "as far ahead of humanity as we are to a mouse".
- Cohesion: cover previews the three slides; identical 3-block pattern per slide; recap slide 5. No "but/so" bridges.
- Hook: diagram/promise hook. Stops the thumb because the answer to "what are these acronyms" is already drawn.
- Caption: long (~1,400+ chars), repeats slide text almost verbatim. First 125: "AI vs. AGI vs. ASI, explAIned 1 AI / ANI: Artificial (Narrow) Intelligence Where we are now. The Standard Definition: Almost all AI to date is..." No AI disclosure seen.
- Clarity verdict: 7/10. Best-in-sample cover (the staircase); slides 2-4 are text blocks a reader must work through.
- Persona: face only on the last slide (credibility after value).

### POST 4: https://www.instagram.com/p/DUy6erqkuHt/ (Karpathy microgpt.py, news + reference)
- date 2026-02-15, carousel, 6 slides, likes 2.6K, comments 34, shares 36
- Audience: tech enthusiasts / coders.
- One-line message: a complete GPT can be written in 243 lines of plain Python (just released by Andrej Karpathy).
- Slides: 1 = designed cover: "microgpt.py - Andrej Karpathy" + screenshot of his tweet + architecture flow (Tokenizer -> Embedding -> Attention -> MLP -> Softmax -> Loss) + 4 stat tiles. ~90 words but mostly screenshot. 2-5 = dark-mode screenshots of the actual code (no prose). 6 = "Welcome!" credentials slide.
- Hook: authority/news hook with the original tweet as proof; no headline written for the image.
- Caption first 125: "Legendary AI educator Andrej Karpathy released microgpt.py today on GitHub - it's a transformer (the groundbreaking neural network architecture behind modern AI), fully implemented..." Defines jargon in parentheses, adds personal story ("I taught a class yesterday..."), ends "Pretty cool, huh?".
- Clarity verdict: 4/10 general viewer (7/10 for developers). Cover is a diagram + tweet, then four pages of unreadable code. 2.6K likes suggests the audience came for the NAME and the "243 lines" claim, not slide detail.
- Persona: first-person caption; face on slide 6.

### Account patterns: @harpercarrollai
- [OBSERVED] Carousels are a minority of her output (reels dominate) but they are templated explainers titled "X, explAIned". Two eras: Dec 2025-Feb 2026 cream/blue "explAIned" series with 3-block text slides; Nov 2026 "LVL 0X" gamified series with photo backgrounds and stat cards.
- Slide counts 6-9. Words per slide 20-75; the cover is always lighter than interior slides.
- A credentials slide ("Welcome! / Why listen to me?") appears in 3 of 4 posts: trust-building inside the carousel.
- Engagement: AGI explainer (2.7K likes) and Karpathy post (2.6K) beat context window (162 comments, driven by "Guide" keyword replies). [INFERENCE] comments are inflated by keyword-DM farming; likes/shares are the cleaner signal.
- Clarity risk: insider word in the HOOK ("Tokenmaxxing") vs. her clearest post, which uses a question a layperson asks ("Why AI forgets things").

---
## ACCOUNT: @ishansharma7390 (Ishan Sharma; 1.2M followers; Indian audience; AI + business/career creator, YouTube-led; carousels are ~2 of 12 recent grid items but he posts many list carousels)
Why picked: large Indian audience, simple English, strong carousel engagement (12.6K likes), mix of AI-course, career and lifestyle posts. Honest caveat: his AI carousels here are mostly lists and one course promo, not explainers of how AI works; he is not a "built-it" creator in carousels (his built-tool story, "I built a tool to solve my hiring problem", is a reel).

### POST 1: https://www.instagram.com/p/De4EaBqH-uq/ ("Zero to Infinity with AI" course announcement)
- date ~2026-10-24, carousel, 9 slides, likes 12.6K, comments 3.6K, shares 139 (collab post with @ca_nandini19; labelled "AI content")
- Audience: Indian working professionals / students who want to "use AI at work". Intent: sell a Rs 6,000 12-month course.
- One-line message: AI changes daily, one course ends, so join a 12-month program (5 modules + 12 live sessions) for Rs 500/month.
- Slides (all viewed):
  1. HOOK: full-bleed photo of both hosts, caption box on image "We have something for YOU" (5 words) + "Swipe >" pill. Text ~15%, photo ~85%. Faces as hook.
  2. TITLE card: "Zero to (infinity symbol) with AI" (big infinity sign as the O) + "Learn. -> Apply. -> Evolve." + "by Nandini Agrawal & Ishan Sharma". ~15 words. Slide counter "2/9" printed on the slide.
  3. PROBLEM: "AI changes every single day." + giant "300+" "new AI models launched in the last 12 months" + visual: One AI course = 1 box filled of 12, Zero to Infinity = 12 ticks; line "A course ends. AI doesn't." ~35 words. Number is the hero.
  4. "5 modules to build your base" + tool logos (ChatGPT, Claude, Gemini, NotebookLM, Nano? Flow, n8n) + 5 numbered tiles each with a 6-10 word plain description ("Essential AI Tools: Hands-on with each tool, and when to use which", "How AI works: Why AI sometimes gets it wrong", "Automation with n8n: The boring work runs on its own"). ~70 words but tiled.
  5. "12 live sessions with us" + 3 black cards (What's New in AI / Your Questions / Made for Your Field) + 4 stat tiles (12 months, 5 core modules, 15-20 hours, 12 live sessions). ~60 words.
  6. "The simple formula" Learn + Join live + Keep up = You (using AI on real work, not falling behind). Equation layout. ~35 words.
  7. "Everything you get" price card "Rs 6,000 (struck: Rs 10,000) That's just Rs 500 a month." + checklist. ~50 words.
  8. "Rs 500 a month costs less than one night out": 4 horizontal comparison bars (Dinner for two ~Rs 1,500, Movie ~Rs 1,200, Two Uber rides ~Rs 600, course Rs 500) + refund guarantee. ~55 words.
  9. CTA: "A course ends. AI doesn't." + 3 numbered actions: Comment INFINITY / Share with the friend who keeps asking you about AI / "What would you want to use AI for?".
- Layout: ultra-consistent template (cream background, heavy black serif headline with yellow highlighter on ONE key word, small caps label above ("WHY 12 MONTHS, NOT ONE COURSE", "HOW IT WORKS", "JOIN"), outlined cards with drop shadow, slide counter "n/9" on-slide). 1 headline + 1 visual block per slide. Words per slide 15-70, avg ~45 but structured into cards so reading feels light.
- Readability: grade ~6-8. Almost no jargon; tool names are shown as logos; "n8n" is named but described as "the boring work runs on its own". Concrete (rupee prices, "dinner for two") and visual comparison bars. Sentences 5-10 words.
- Cohesion: [OBSERVED] repeated refrain ("A course ends. AI doesn't." on slide 3 and slide 9 - bookends), numbered counter on each slide, an eyebrow label that announces each step's role, classic problem -> solution -> how -> price -> proof of value -> CTA arc.
- Hook: curiosity/"offer tease" hook ("We have something for YOU" + eyes emoji) with two faces. Soft hook; the engagement is mostly audience-trust-driven (big following + comment-to-get funnel).
- Caption: long (~1,000+ chars). First 125: "Comment "INFINITY" to know more!" then "AI is changing every single day. While you are watching creators cover the latest ai models and tools, you don't know how to actually apply them..." Restates slide 3 stat (291 launches, 51,000 tools). CTA = keyword-DM. Edited, labelled "AI content". 3.6K comments are inflated by the keyword CTA.
- Clarity verdict: 9/10 as communication (every slide is understood in 2 seconds; one number or one comparison per slide). Caveat: it is an ad, and the engagement is boosted by comment-to-DM mechanics.
- Persona: two faces on cover and CTA (polaroid-style photos), first-person plural "we've created", "with us".

### POST 2: https://www.instagram.com/p/Dcky6Zhn6yS/ ("Read This Before You Turn 25" - 7 career lessons)
- date 2026-08-28, carousel, 10 slides, likes 7K, comments 39, shares 112
- Audience: Indian 20-somethings (general, not AI-specific).
- One-line message: seven things that make careers grow, learned from working with fortune-500 companies and mistakes.
- Slides (all viewed): 
  1. HOOK "Read This Before You Turn 25" (6 words) top-left in black serif over a black-and-white cut-out of Ishan with a hand-drawn arrow pointing at the title and "Swipe ->". Text ~15%. Face + age-deadline.
  2. Photo (Apple WWDC26 sign) + caption block "Career growth isn't rocket science. I've interviewed and worked with dozens of 20-somethings over the years. The ones who blew up all did these things." ~30 words, bottom text panel.
  3-9. Each = full-bleed real photo (top ~65%) + bottom white panel: bold numbered headline + 1-2 sentence explanation (~20-30 words): "#1 One year of experience >>> years of experience", "#2 Work-life balance doesn't exist. Accept it.", "#3 Growth hides behind the questions you're scared to ask.", "#4 Keep upskilling or get replaced by AI.", "#5 Content is your moat.", "#6 Hard skills get you in. Soft skills get you to the top.", "#7 Get REALLY good at what you do."
  10. CTA: portrait + question "Which of these hit hardest? & What would YOU add to the list?" + "Follow For More".
- Words per slide 20-40, photo-led (photos are decorative / personal-life, not explanatory). Numbered headlines are the whole cohesion mechanism. 
- Readability: grade ~6. No jargon. Headlines are opinions (strong claims) - "AI is eating junior tasks faster than they think" is the only AI line.
- Hook: identity + deadline ("before you turn 25") = high relevance; "Share this with a friend" in caption.
- Caption first 125: "Share this with a friend. Here are 7 things every 20 something needs to know. I learned this over the last 7 years of college, content, marketing company, ai..." Short (~330 chars), extends with credibility line + follow CTA. No hashtags, no AI label.
- Clarity verdict: 9/10. Instantly clear; but the content is generic advice and photos don't explain anything.
- Persona: strong. Real photos of him in London, Apple Park, office, team selfies make each tip feel earned ("I've seen...") - the face IS the proof.

### Account patterns: @ishansharma7390
- [OBSERVED] Template discipline: serif headline + one yellow-highlight word, numbered headlines, photo-or-card per slide, slide counter, 7-10 slides, 15-40 words per slide (up to 70 in tiled cards).
- Posts that are heavily engaged are either (a) personal-authority listicles ("Read This Before You Turn 25": 7K likes) or (b) a clear offer with a keyword CTA (12.6K likes, 3.6K comments).
- Lifestyle photo-dump carousels (Diwali with the team, Apple event, New York) exist in the same grid; these are low-text and presumably lower informational value (not opened).
- Indian-audience note: English with simple sentences; rupee anchors ("Rs 500 a month costs less than one night out") make price concrete; "Look maa, I'm on TV" style emotional captions mix in Hinglish in other posts.

---
## ACCOUNT GROUP: small "I built X with AI" carousel makers (found via #vibecoding / #builtwithai). All are SMALL accounts (600-900 followers), so engagement is a weak signal; they are included because they are the closest match to Tangent's own situation (a non-famous solo person telling a "my first app" story) and the slide craft is instructive. [OBSERVED] No large creator in the candidate list (e.g. @realrileybrown, 332K, the "vibe coding" king) posts builder carousels: his last 12 grid items are all reels.

### @thejacklyncollins (Jacklyn Collins; 616 followers on profile; bio claims an audience of 26k+ elsewhere; 7 posts)
#### POST: https://www.instagram.com/p/DezcWvgoP1Z/ ("Hi, I'm Jacklyn. I built Shelf by JC with AI.")
- date ~2026-10-22, carousel, 5 slides, likes ~3, comments 0 (tiny). Hashtags #builtwithAI #AIapps #womeninbusiness #shelfbyjc.
- Audience: general, non-technical people; the "I can't code either" crowd.
- One-line message: a non-coder built a showcase app for other non-coders' AI-built apps.
- Slides (all viewed), 5 slides, 8-22 words each:
  1. HOOK: portrait photo of her holding a mug, bottom dark panel: "Hi, I'm Jacklyn." (big white) / "I built **Shelf by JC** with AI." (purple highlight on the product name) / "Swipe for the story >" + counter "1/5". ~15 words. Face + plain first-person claim.
  2. "Before this, I sold digital products." + 1 line "I don't understand a thing about code. Honestly, I still don't. And I had never built an app." ~28 words. Cream page, one purple underline accent.
  3. "Then I saw what people were building with AI." + "Amazing apps, made by people who'd never coded. And nowhere to really show them off." ~22 words.
  4. "So I built a home for them." + "Shelf by JC is my first app. I built the whole thing with AI, and it launched this October." + photo of her on a sofa (half-split layout). ~30 words.
  5. "Now I get to celebrate them." purple full-bleed + "Every week I feature someone who built something with AI. Follow along to meet them." ~25 words. Soft CTA.
- Cohesion: [OBSERVED] the four headlines are one running sentence: BEFORE... / THEN... / SO... / NOW... Each slide begins with a time/causal connector ("Before this", "Then", "So", "Now"), so the story reads without decoding even if you skip the body. Counter "n/5" on every slide, same template, large bold sans headline, ONE sentence of body.
- Readability: grade ~5. Zero jargon ("AI", "app" only). Concrete personal facts. Sentences 5-12 words.
- Hook: identity + self-deprecation ("I don't understand a thing about code") + "I built X with AI". Stops the thumb because a real face states a surprising capability for a non-expert.
- Caption: ~480 chars; first 125: "Hi, I'm Jacklyn 👋 I don't understand a thing about code. Before this, I sold digital products. I had never built an app. Then I started seeing what people were..." The caption repeats the carousel almost verbatim (restates), then "Follow along to meet them", 4 hashtags. No explicit AI-use disclosure beyond the claim itself.
- Clarity verdict: 9/10. Gets everything across in ~100 words total. Not "clever": every line is literal. Weakness: no screenshot of the app itself (the viewer never sees what Shelf looks like in the carousel).
- Persona: face on cover and slide 4; warmth through confessional tone.

### @dhruvarajrane01 (Dhruv Rane; 623 followers; 38 posts; Indian, Marathi caption)
#### POST: https://www.instagram.com/p/Dbr6UVziDXA/ ("My first app, built with AI" - expense/food tracker)
- date ~2026-08-06, carousel, 5 slides, likes 14, comments ~0. Hashtags #MyFirstApp #BuiltWithAi #AiProjects.
- Audience: Marathi/English-speaking friends and aspiring builders.
- One-line message: "I don't know coding, but I knew what I wanted" - here's the tracker app I built.
- Slides (all viewed): 1 = a collage cover of 4 phone screenshots (balance Rs 970, Today/Expenses, Upcoming planned bills "Mutual fund / Ghee / Dabba bili") in one image; 2-5 = single full-bleed phone screenshots of the app (Expenses/Food cards; Upcoming; "What did you eat?" log; Today list). ZERO words on any slide.
- Words per slide: 0. 100% product screenshots. Slide order = tour of screens, no headline, no arrows.
- Readability: no text; the app UI (Indian rupees, Idli, Ghee, Dabba bill) is itself the content. Caption (Marathi + English): "एक छोटीशी कल्पना... आणि AI च्या मदतीने बनवलेलं माझं पहिलं App." / "I don't know coding, but I knew what I wanted to build. Started from zero, planned it, tested it, found bugs, made changes - and slowly turned an idea into something that actually works." Caption carries the entire story arc (idea -> plan -> test -> bugs -> works); the slides carry only proof.
- Hook: slide 1 collage of finished UI + local-language caption line (cultural recognition).
- Clarity verdict: 6/10. Visually clear and honest ("data shown is sample data"), but a viewer must read the caption to know what the app does; no slide says "expense tracker" or what problem it solves. Slides never show the person.
- Persona: first person in caption, humility, "only the beginning". No face.

### @theayeshaharoon (Ayesha; "product designer, mom, tech, Lahore"; 866 followers; 148 posts)
#### POST: https://www.instagram.com/p/DZMxVIiCD7L/ ("i vibe-coded my first app in just 2 hours!")
- date ~2026-06-05, carousel, 7 slides, likes 20, comments 3. 
- Audience: designers / non-coders curious about vibe coding.
- One-line message: you can go from idea to live app in 2 hours with a project brief, Claude and Vercel.
- Slides (all viewed): 
  1. HOOK: "i vibe-coded my first app in just 2 hours!" over a Windows-XP "Bliss" hill wallpaper with scrapbook stickers (butterfly, heart), a mockup of the app ("Trinket", a digital tin for unfinished thoughts), tool logos "1) build - Claude", "2) deploy - Vercel". ~12 words visible + labels.
  2. "step 1: shaping the idea / I asked claude to help me build a project brief" + screenshot of the actual prompt + two aesthetic reference images. ~15 words + screenshot.
  3. "step 2: building using the brief / I asked claude to build the first version of the app / [this literally feels like magic as someone who doesn't code]" + app screenshot.
  4. "step 3: customising it / I asked claude to change out a few elements / [claude gaslit me multiple times btw so keep prompts clear]" + screenshot of icon options and a prompt.
  5. "step 4: deploying / I went back & forth following Claude's instructions to deploy the app on vercel" + screenshots of the instructions and the app in a retro Paint window.
  6. "step 5: deployed / I connected my project to Vercel, clicked deploy, and had a real link in 2 min" + the live URL + "No server. No tech setup. Just a live app with my name on it."
  7. CTA "save this for your first vibe-coded project / and follow me for more vibe-coding content" over desktop-folder icons.
- Words per slide 12-30. Layout: playful Windows-desktop-nostalgia aesthetic, handwritten-style headline in a consistent position, screenshot of the REAL prompt or product on every slide, red heart sticker as recurring motif, "step N:" numbering.
- Readability: grade ~5-6. Jargon ("vibe-coded", "deploy", "project brief") handled by showing the actual artifact each time; "deploy on vercel" explained as "had a real link in 2 min". Candid asides in brackets ("claude gaslit me multiple times btw") carry personality and honesty.
- Cohesion: "step 1 ... step 5" numbering; each slide's headline begins "I asked claude to..."; cover promises "1) build 2) deploy" and the body delivers it. Strong cause-effect.
- Hook: result-in-the-title ("first app in just 2 hours") + aesthetic curiosity. Caption (first 125): "I shipped my first app in 2 hours (for funsies ofcourse) and I don't know how to code. I came across this really cute digital tin box for half-finished thoughts." Caption repeats and extends with the steps and a tip ("a brief, not code"). 
- Clarity verdict: 8/10 (high for designers/Gen Z; a little dense visually because of stickers). Tutorial arc is exactly "what I did, step by step, with screenshots".
- Persona: no face; voice is lower-case, funny, honest about failure. 

### Account patterns: small builder carousels
- [OBSERVED] The posts that read best for a general viewer share one trick: the claim is in plain words on the cover ("I built X with AI", "I vibe-coded my first app in just 2 hours") and the following slides are either a causal chain of short sentences (Jacklyn: Before/Then/So/Now) or numbered steps with a real screenshot each (Ayesha).
- [OBSERVED] The zero-text screenshot carousel (Dhruv) is the least self-explanatory: a viewer must read the caption to learn what the app is for.
- [OBSERVED] Engagement is tiny (3-20 likes) so none of this proves reach; it is a craft sample, not a performance sample.

### POST 3 (Ishan): https://www.instagram.com/p/DdCHiKcG5UB/ ("Content I watch instead of doomscrolling" - 4 YouTube recommendations)
- date 2026-09-08, carousel, 7 slides (slides 1-5 viewed; slides 6-7 not viewed), likes 3.5K, comments 17, shares 93
- Audience: Indian young adults who want self-improvement/AI content.
- Message: here are 4 YouTube videos worth watching instead of scrolling.
- Slides: 1 = HOOK full-bleed portrait of Ishan with huge white serif "Content I watch instead of doomscrolling." with the last word in an orange highlighter block (6 words, text ~35% of image). 2-5 = identical template: grey paper background, big numeral "1." to "4.", a YouTube-style screenshot (thumbnail + title bar: "Elon Musk: the full-length interview", "What if the AI Bubble Bursts", "Rule of Three", "before you adapt to AI... watch this") and one 20-25 word plain description under it ("A day-by-day walkthrough of what actually happens if the AI bubble pops, more useful than another hot take thread about it."). Double-chevron ">>" cue bottom right.
- Readability: grade ~7; the proof (a real thumbnail) is the visual. 
- Cohesion: numbered 1-4, same frame; slide 1 sets the promise "instead of doomscrolling" so the list has a reason to exist.
- Hook: identity/habit-contrast hook ("instead of doomscrolling"); orange-highlighted last word. Caption (~160 chars) first 125: "Youtube videos that'll teach you more than any course out there. All video links are in my bio. Save this and follow @ishansharma7390 for more." Pure CTA (save + follow).
- Clarity 9/10. Persona: close-up face, warm, relatable habit.

### POST 4 (Ishan, glance): https://www.instagram.com/p/DdOhw4UjEiF/ and other photo-dump carousels (Diwali, Apple events, NYC) are lifestyle posts; not analyzed at slide level.

---
## ACCOUNT: @tiffintech (Tiffany Janzen; 815K followers; Stanford AI/ML; "Inside AI, robotics & the companies shaping the future"; reel/YouTube-led, carousels are mostly photo recaps)
Why picked: large, high-quality explainer voice; strong example of image-led carousels. Caveat: only 2 of ~120 scanned grid items marked "Carousel" in the last year are explainers.

### POST 1: https://www.instagram.com/p/DYkM7zZlAwz/ ("The world runs on one tiny chip.")
- date ~2026-05-20, carousel, 9 slides, comments 41, shares 14, likes hidden ("Liked by hermes... and others"). Comment: "you make ordinary people (like me) fall in love with technology".
- Audience: general, curious adults. No jargon needed.
- One-line message: modern tech depends on a fragile chip supply chain controlled by a few countries and companies.
- Slides (all viewed):
  1. HOOK: portrait photo on a sofa; frosted-glass text card "The world runs on one tiny chip." / "Small technology. Massive global dependence." + SWIPE pill. ~14 words. Photo ~75%.
  2. "The world runs on one tiny chip." + "From AI to iPhones, modern technology depends on one of the most fragile supply chains ever built." + 3 emoji-icon stats (70+ countries involved / 1000+ companies / Years to build a single fab). ~35 words.
  3. "One chip touches 70+ countries." + flag list (Australia -> silicon materials; China -> rare earth refining; Ukraine -> neon gas; Japan -> ultra-pure chemicals). ~35 words.
  4. "One company controls the machines." + ASML: 100,000+ parts / costs hundreds of millions / takes years to build + "No ASML = no cutting-edge AI chips." ~40 words.
  5. "Most chip blueprints come from the US." + Nvidia, Apple, AMD, Qualcomm + "The supply chain isn't just physical - it's intellectual too." ~30 words.
  6. "One island powers modern technology." + TSMC ~90% of advanced chips; "Your phone, laptop, AI tools, and even modern cars likely depend on chips made there." ~45 words.
  7. "A few countries control the future of tech." + flag lines (Taiwan/Netherlands/China) + "Semiconductors aren't just technology anymore - they're geopolitics." ~35 words.
  8. "The most advanced industry on Earth is also one of the most fragile." + "One earthquake. One export restriction. One factory shutdown." ~30 words.
  9. CTA question "Which part surprised you most?" + "Drop a comment. Was it ASML's monopoly, Taiwan's dominance, or how global the supply chain really is?" ~25 words.
- Words/slide 14-45 (avg ~32). Layout: dark background, ONE big white sentence-headline (with a teal hand-drawn underline on the key phrase), 1 short support line or 3 icon bullets, brand handle bottom, thin dotted "path" line drawn across slides (continuity motif).
- Readability: grade ~8. Jargon limited to ASML, fab, EUV, each tied to a concrete claim ("One company controls the machines"). Every headline is a complete claim in 5-9 words with a NUMBER or "ONE" repetition: "One chip... / One company... / One island... / One earthquake. One export restriction." Repetition makes it a chain.
- Cohesion: [OBSERVED] the headlines alone tell the full story in order (chip -> 70 countries -> one company -> blueprints -> one island -> few countries -> fragile). Anaphora ("One ... One ...") plus the continuous dotted line. Funnel from a big claim to a specific cause, then back out to a consequence.
- Hook: bold claim ("The world runs on one tiny chip") + her face; the claim is surprising and literal.
- Caption: ~140 chars, one sentence: "The more I learn about semiconductors, the more I'm convinced this is the most important industry most people know nothing about." (opinion framing; doesn't restate slides; no hashtags, no CTA beyond slide 9 comment question). 
- Clarity verdict: 9/10. Plain nouns, one claim per slide, concrete numbers/countries. Not clever; the only figurative phrase ("One island powers modern technology") is immediately explained on the same slide.
- Persona: face on slide 1 only; her voice appears as the "more I learn... I'm convinced" caption (first-person curiosity). Warm via "ordinary people fall in love with technology" comment.

### POST 2: https://www.instagram.com/p/DX4ecU8FE2E/ (1X Neo humanoid factory "stills", 8 slides; caption: "Humanoids are no longer science fiction. They're being built right now, and we went inside the factory making it happen.")
- Contrast post: photo stills from a YouTube video, little/no on-slide text (cover and slides not opened individually; 8 slides counted; comments are jokes: "As long as it can fold laundry"). Image-led and fun, low informational load; caption does the work. Clarity as a standalone post is moderate (needs the caption).

### Account patterns: @tiffintech
- [OBSERVED] Her explainer carousel uses one-sentence-per-slide with number/anaphora ("One chip.. One company.. One island..") and drops the face after slide 1. Photo-recap carousels (month recaps, event stills) dominate her carousel use.
- Slide counts 8-9; words ~14-45 per slide; first slide is the lightest.

---
## ACCOUNT: @rowancheung (Rowan Cheung; 531K followers; 25 posts total; founder of The Rundown AI)
Why picked: the biggest AI-news creator; but his IG is sparse and mostly personal-brand carousels (the news product lives in reels/newsletter, covered by other agents).

### POST: https://www.instagram.com/p/DcY-w3plZJg/ ("I dropped out in 2021 and now I somehow run one of the fastest-growing media companies.")
- date ~2026-08-23, carousel, 7 slides (6 viewed), comments 62, shares 8, likes hidden ("Liked by graham59harris and others")
- Audience: tech-aspirational general / founders.
- One-line message: the skill that matters is "AI intuition": knowing when to use AI and when not to; ask one question before every task.
- Slides: every slide is TWO stacked photo panels (top: team/office/event photo; bottom: him on stage at Forbes 30 Under 30) with a video-subtitle-style caption burned into each panel. The captions chain into one paragraph across slides: "I dropped out in 2021 and now I somehow run one of the fastest-growing media companies." / "The difference was one skill that nobody is talking about..." / "See when we started there were hundreds of AI newsletter competitors." / "They all used AI to write their content... but we did something that made no sense..." / "We did the complete opposite. We hired real people who live and breathe AI." / "We still leverage AI in many ways, but NEVER for the human part." / "And our readers could feel the difference... somehow it led me to rooms like this." / "Because AI beats me at grunt work. But I beat AI at opinions, jokes, and knowing my audience." / "That skill is called AI intuition... knowing when and when NOT to use AI." / "The next billion dollar companies will be built by the people who have it." / "And building AI intuition is surprisingly simple. Simply ask yourself one question before every task, every single day..."
- Words/slide: ~12-20 per caption x 2 panels = 25-35 words per slide. Layout: 100% photos, text as subtitles over photos, no graphic design. Text ~15%.
- Readability: grade ~6-7; no jargon (the one coined term "AI intuition" is defined in a single sentence on the slide where it appears). Voice is spoken-style, first person.
- Cohesion: [OBSERVED] sentences run on across slides with ellipses ("...about..." / "...that made no sense...") - a continued-sentence structure that pulls the swipe. The "The difference was..." and "We did the complete opposite" lines are "but/so" bridges.
- Hook: personal-story contrast ("I dropped out in 2021 and now I somehow run one of the fastest-growing media companies") - credibility + curiosity; the second line adds a mystery ("one skill nobody is talking about").
- Caption: ~1,000+ chars; first 125: "I dropped out in 2021 and now I somehow run one of the fastest-growing media companies. The difference was one skill that nobody is talking about..." Restates the slides, extends with the Rundown story, closes with CTA. No hashtags noted.
- Clarity verdict: 7/10. Plain language and a strong chain, but the "one question" payoff is on the last (7th) slide and the photos are decorative; the viewer must swipe the whole way for the point.
- Persona: heavy face presence, authority photos (Zuckerberg, Forbes stage), but warmth is modest; "somehow" and "made no sense" add humility.

### Account patterns: @rowancheung
- Only 25 posts; 8 of 12 grid items are carousels but mostly recaps/news-of-self ("q3 in the books", "Forbes 30u30", "some nyc moments"). His AI news is reels. Not a model for explainer carousels; useful for the subtitle-chain device.

---
## ACCOUNT: @thevarunmayya (Varun Mayya; 1.2M followers; Indian; entrepreneur, tech/AI commentary; reel-first)
### POST: https://www.instagram.com/p/DdO0TLoAXqz/ ("From 13,000 to 3 winners" - OpenAI x VM hackathon)
- date ~2026-09-13, carousel, 5 slides (only slide 1 and a blurred repeat captured; slides 2-5 not reliably viewed because the viewer layout differed; treat as partial), likes 25.7K, comments 156, shares 76.
- Slide 1: photo of the three winning teams holding a giant cheque "Trip to San Francisco", sponsor logos (OpenAI, Varun Mayya), zero headline text on the image. Caption: "From 13,000 to 3 winners. Thank you to everyone who participated: your time and energy was channeled towards a good cause. Thank you to OpenAI for partnering with us..." 
- Takeaway: a celebration/photo post whose 25.7K likes come from audience size and event energy, not from slide copy. Clarity of the claim is immediate ("13,000 to 3 winners"; a cheque photo explains itself). Not an explainer; contrast case.
- Account pattern: 0 of the first 12 grid items are carousels; the 3 non-reel carousels in the scanned grid are "the month that was", the hackathon, and a throwback.

---
## ACCOUNTS CHECKED AND REJECTED FOR CAROUSEL STUDY (with evidence)
- @cleoabram (3.2M): 12/12 recent grid items are reels. Her still-image craft is not in evidence. Her reel hooks are short curiosity-gap titles, e.g. caption openers "Your map shows Antarctica wrong." / "The sun is... jiggling?" / "Why are zombies green?" (first line of each caption is the plain-language hook). [OBSERVED from grid captions]
- @realrileybrown (332K, vibe-coding/builder): 12/12 reels; caption openers are blunt ("You can build basically any Saas app in a few hours", "Comment 'Phone' if you want...") - keyword-DM CTA heavy.
- @dhruvrathee (20.2M, Indian): 12/12 reels; politics-heavy; not an AI explainer on stills.
- @tiffintech, @harpercarrollai, @rowancheung, @thevarunmayya, @ishansharma7390: covered above; all reel-first.

---
# Cross-account lessons

Sample actually analyzed at slide level: Harper x3 (+1 partial), Ishan x3, Tiffin x1 (+1 contrast), Rowan x1, Varun x1 (partial), builders x3 = about 14 carousels, not the 30 requested. Reason: the listed creators are reel-first and very few of their carousels are explainers; the builder category had to be sourced from small accounts. Treat the lessons as strong patterns from a small, honest sample.

1. One sentence-sized claim per slide beats stylish phrasing. [OBSERVED] The most instantly understood posts have headlines that are literal complete claims in 4-9 words: "The world runs on one tiny chip." / "One company controls the machines." (https://www.instagram.com/p/DYkM7zZlAwz/), "Why AI "forgets" things." / "What happens when it's "full"?" (https://www.instagram.com/p/DUQ_6LXkqR2/), "AI changes every single day." / "A course ends. AI doesn't." (https://www.instagram.com/p/De4EaBqH-uq/). None needs decoding. [INFERENCE] A reader who only reads headlines still gets the story; that is the test Tangent's last carousel failed ("One sky, two ways to count it." names no thing).
2. Chain the headlines like one spoken sentence. [OBSERVED] Four chaining devices recur: (a) time/cause connectors, Jacklyn's "Before this... / Then I saw... / So I built... / Now I get to..." (https://www.instagram.com/p/DezcWvgoP1Z/); (b) anaphora, Tiffin's "One chip / One company / One island / One earthquake"; (c) question-then-answer headlines, Harper's "What is a Context Window? / What happens when it's full? / The strategy."; (d) subtitles that continue across slides with ellipses, Rowan (https://www.instagram.com/p/DcY-w3plZJg/). Plus visible progress: "2/9" counters (Ishan), "LVL 02..09" and a progress bar (Harper, https://www.instagram.com/p/DfsDz6IlfCP/), "step 1..5" (Ayesha, https://www.instagram.com/p/DZMxVIiCD7L/).
3. Words per slide: the clearest posts sit at 12-35 words per slide; the dense ones (Harper's AGI explainer 55-75 words/slide, https://www.instagram.com/p/DRukrQYDsWD/) are rated lower for clarity even though they got 2.7K likes. The cover is the lightest slide (4-15 words) in every post. [OBSERVED]
4. Slide count: 5 (Jacklyn) to 10 (Ishan 7-things); explainers cluster at 6-9. [OBSERVED] The 5-slide builder story needs ~100 words in total.
5. Headline-to-visual relation: three patterns. (i) Headline over a real face photo (Harper cover, Ishan covers, Tiffin cover): the face supplies trust, the headline supplies the claim. (ii) Headline + one proof object per slide: a giant number ("~80%", "300+"), a comparison bar (Rs 500 vs dinner for two), a flag list. (iii) Headline + screenshot of the real thing (Ayesha's prompts, Ishan's YouTube thumbnails). Decorative photos with no link to the message (Ishan "turn 25", Rowan) work only because of the creator's existing authority. [OBSERVED/INFERENCE]
6. Jargon handling: the clearest posts either avoid it or define it in the same slide with an everyday metaphor ("Think of it as the AI's working memory" - Harper context windows; "Token minimization: designing systems that call the model as little as possible" - Harper tokens), or show it instead of naming it (tool logos, Ayesha's real prompt). The weakest hook, "Tokenmaxxing might be over", leads with an undefined insider term (https://www.instagram.com/p/DfsDz6IlfCP/). Tangent should put the plain-language noun first (the app, what it does) and any term second, with its definition. [OBSERVED + INFERENCE]
7. Hooks, by type and wording [OBSERVED]: (a) result-in-title: "i vibe-coded my first app in just 2 hours!"; "I built Shelf by JC with AI."; (b) problem the viewer already has: "Why AI forgets things."; (c) identity + deadline: "Read This Before You Turn 25"; (d) habit contrast: "Content I watch instead of doomscrolling"; (e) big surprising claim + face: "The world runs on one tiny chip."; (f) offer tease: "We have something for YOU". Patterns: first person or "you", concrete nouns, no metaphors, 4-10 words.
8. "I built X with AI" stories that land with general audiences (closest to Tangent): they (1) open with the plain claim and the person ("Hi, I'm Jacklyn. I built Shelf by JC with AI."), (2) state the non-expert status as a feature ("I don't understand a thing about code"), (3) tell a literal story or numbered steps, (4) show the real artifact or prompt, and (5) keep lessons candid ("claude gaslit me multiple times btw"). The weakest builder post shows only app screenshots with no on-slide words (Dhruv, https://www.instagram.com/p/Dbr6UVziDXA/): visually honest but the viewer can't tell what the app is for without the caption. Best practice combination to test: Jacklyn's Before/Then/So/Now headline chain + Ayesha's real screenshot on each slide + a one-line "what it does for you" on the cover. [INFERENCE] Caveat: all three are tiny accounts, so none proves reach.
9. Captions: three modes. (i) Restate-and-extend (Harper, Rowan, Jacklyn): first line repeats the cover, the rest adds credentials/story. (ii) One-line opinion that does not repeat slides (Tiffin: "The more I learn about semiconductors, the more I'm convinced..."). (iii) CTA-only (Ishan: "Save this and follow"). Many top posts use keyword-comment CTAs ("Comment INFINITY", "Comment GUIDE"), which inflates comments (3.6K, 162). Hashtags are rare among big creators and used by small builders (3-4). No post carried an explicit "made with AI" disclosure except Instagram's own "AI content" label on one collab (Ishan). [OBSERVED]
10. What separates most-engaged from weak [OBSERVED + INFERENCE]: engagement tracked (a) the offer or authority attached (Ishan course Rs 500/month 12.6K likes; Varun hackathon 25.7K likes; Harper Karpathy 2.6K), (b) share-worthiness of a list or definition (AGI explainer 124 shares; Ishan 7-things 112 shares), and (c) an identifiable face. Slide clarity mattered most inside a given account, e.g. Harper's clearest post (context windows, 8/10 clarity) got 162 comments but its likes were not visible; her most-liked posts were AGI and Karpathy. Weak/low posts were photo dumps or text-free screenshot tours. Follower count dominates absolute numbers, so use within-account comparisons.
11. Persona: the face is used as the proof on the cover (Harper, Ishan, Tiffin, Jacklyn) and as a credentials slide (Harper "Why listen to me?"); first-person admissions of not knowing ("I don't understand a thing about code", "claude gaslit me") are the warmest, most trusted lines.
12. Practical template for Tangent (INFERENCE): cover = one literal sentence + the thing itself (photo or app screenshot) ; slides 2-5 = headlines that read as one running sentence (Before/Then/So/Now or step N), each with ONE proof visual and <=25 words; last slide = a question or save/share CTA. Keep any domain term (e.g. ayanamsa, Saturn positions) out of headlines; put it in the body in plain words or show it in a picture.


=====================================================================
# ROUND 2 ADDITIONS (appended after coordinator follow-up)
=====================================================================

## Completed partials from round 1
- Varun Mayya https://www.instagram.com/p/DdO0TLoAXqz/ (all 5 slides now viewed): 1 = winners with giant "Trip to San Francisco" cheque; 2 = host on stage in front of a "BUILD WHAT MOVES INDIA" screen; 3 = wide stage shot with a projected form; 4 = "OpenAI x VARUN MAYYA" title card; 5 = runners-up holding a trophy against "RUNNER-UP". ZERO text overlays on any of the 5 slides; all meaning is in the caption ("From 13,000 to 3 winners..."). Likes 25.7K / comments 156 / shares 76. Verdict: pure event-photo post; it works for a 1.2M-follower audience who already know the hackathon; a cold viewer would not know what was won or why (clarity 4/10 standalone, 8/10 for followers). Note the only "clear" number ("13,000 to 3") lives in the caption, not on a slide.
- Rowan Cheung https://www.instagram.com/p/DcY-w3plZJg/ slide 7 (final): top panel office photo with a sticky note "COULD AI DO THIS?", bottom subtitle "That ONE question will teach you more than any AI course on the internet." Headline of the final slide: "COULD AI DO THIS?" (quoted). So the payoff is a 5-word question, delivered on slide 7 of 7. Likes hidden, comments 62, shares 8.
- Ishan Sharma https://www.instagram.com/p/DdCHiKcG5UB/ slides 6-7 (the 7-slide post): slide 5 (labelled "5." in the viewer; earlier I had counted 4 items - there are 5) = YouTube card "LIFEMAXXXING - Everything changes when you stop playing it safe" + "A reminder that most of what's holding you back isn't risk. It's comfort wearing a disguise."; slide 7 = selfie portrait with "Save this for the next time. Comment which one you're starting with" + "Follow For More" pill. Structure: cover + 5 numbered picks + CTA. Correction to round 1: 5 picks, not 4.

---
## ACCOUNT: @luispdoesai (Luis P; 21.6K followers; AI automation/"I turn AI into systems"; reel-heavy, builder voice)
Why picked: an "I built X with Claude Code" carousel from an account with real reach, not just friends.

### BEST POST: https://www.instagram.com/p/DWoa5SWDmuk/ ("6 Apps to Build With Claude Code Instead of Paying For.")
- date ~2026-04-02, carousel, 8 slides, likes 275, comments 314 (keyword CTA "CLAUDE"), shares 9
- Audience: small-business owners / solo founders paying for SaaS.
- One-line message: six paid tools (CRM, chatbot, invoicing, dashboard, booking, email writer) can each be built with one Claude Code prompt, saving $3,540/yr.
- Slides (all 8 viewed):
  1. HOOK (editorial cream page): small tag "BUILD - NOT BUY"; big serif headline "6 Apps to Build With Claude Code Instead of Paying For." (11 words) with "Claude Code" in italic terracotta; 1 grey sub-line "Stop paying subscriptions for tools you can own forever."; a row of 6 mini tool chips (CRM, Chatbot, Invoice, Dashboard, Booking, Email Tool) at the bottom as a preview. ~28 words. No face.
  2-7. IDENTICAL split layout: left = a real screenshot/mockup of the finished app; right = small tag "APP N OF 6", serif headline (a noun phrase: "A custom CRM that actually fits your business." / "An AI chatbot trained on your own business." / "A branded invoice and billing tool." / "A live analytics dashboard for your business." / "A booking and scheduling tool with zero fees." / "An AI email writing tool built around your voice."), a price tag chip of what it replaces (HubSpot $1,200/yr, Intercom $74/mo...), 2-3 sentence body (~35 words), a quoted prompt hint. Huge ghost numeral 1-6 in corner. ~45 words per slide.
  8. CTA: "Stop paying. Start building." + stat tiles "$3,540/yr in subscriptions replaced / 6 apps / $0 cost" + button "COMMENT "CLAUDE"". ~30 words.
- Layout: editorial serif type, alternating light/dark pages, one hero visual per slide (the real app), numbered "APP N OF 6".
- Readability: grade ~9; jargon minimal (Claude Code named once, "single prompt" repeated). Everything is stated in money terms (HubSpot $1,200/yr), which is concrete. Sentences 10-18 words.
- Cohesion: the cover previews all six as chips, each slide says "App N of 6" with the same layout, the closer sums the savings (a payoff that adds up the whole carousel).
- Hook: "Build, not buy" - a benefit/loss-aversion hook ("Stop paying for apps you could own forever") with the number of items ("6 apps").
- Caption: ~1,000+ chars, a repeat-and-extend of each app with the same sentence skeleton ("HubSpot charges $1,200 a year for a CRM with features you use 20% of. I built one with exactly the fields... Paid for it once with 10 minutes of prompting."). First 125: "Stop paying for apps you could own forever. I built all 6 of these with Claude Code and a single prompt each. App 1 - Custom CRM". CTA comment "CLAUDE".
- Clarity verdict: 8/10. Every slide = one named app + what it replaces + the price; the numbered "App N of 6" creates progress. Weakness: the claim "built all 6 with a single prompt each" is unverifiable from slides (no prompt shown), and the "I" of the builder is never seen (no face).
- Persona: first-person claim in caption only; slides are brand-neutral.

### WEAK/CONTRAST POST (same account): reel-first; the account's grid shows 2 pinned reels and one carousel in the first 48 items, so there is no second carousel to compare. Contrast within-account instead: the carousel above (275 likes, 314 comments) vs. the pinned reels (counts not read). Not scored.

---
## ACCOUNT: @zoof04_official (Zoof04; 2,033 followers; small, but posts tight builder-safety carousels)
### BEST POST (single sample): https://www.instagram.com/p/DfiTkHUgY40/ ("5 mistakes that can sink your app.")
- date ~2026-11-10, carousel, 7 slides, likes ~3, comments 0
- Audience: non-coders who "made an app with AI".
- One-line message: before sharing an AI-built app, check 5 things: secret keys, open data, fake payments, runaway AI bills, fake admins.
- Slides (all 7 viewed): 
  1. HOOK "5 mistakes that can sink your app." (7 words; "sink" in coral) + sub "Made your app with AI? Check these five first. Each one takes about a minute." + 5 coloured number tiles labelled Secret keys / Open data / Fake payments / AI bills / Fake admins + "Swipe". The table of contents is on the cover. ~30 words.
  2-6. SAME frame, numbered tile "01 Secret keys showing", then "THE PROBLEM" label + one plain sentence ("Anyone who visits your app can copy your secret keys and run up your bill.") + a green "THE FIX" box with a copy-paste instruction ("Ask your AI tool: 'Does my app check with Stripe that a payment is real before it unlocks anything?'") + a source stat ("1 in 5 AI-built apps had this problem. Redirect Labs, Sep 2026"). ~40 words per slide. 
  7. Recap "Check all five before you share your link." + the same 5-item list + teaser box for another product. ~35 words.
- Readability: grade ~7. "Secret keys", "admin" are jargon but each slide has "THE PROBLEM" in one sentence of what happens to YOU ("run up your bill") and "THE FIX" as something you can paste into your AI tool. Jargon is translated into consequence + action.
- Cohesion: preview-on-cover list, numbered 01-05, identical Problem/Fix template, recap closes the loop.
- Hook: list/number + stakes ("mistakes that can sink your app"), with an audience filter ("Made your app with AI?").
- Caption (first ~125): "Made your app with AI? Check these 5 things before you share the link." then emoji-numbered list repeating all five, "Each check takes about a minute. No coding needed." Restate + reassure. 
- Clarity verdict: 9/10. Best "how" structure in the sample for a non-technical builder.
- Contrast (same account): not run; tiny account, so no per-post engagement comparison possible.


---
## ACCOUNT: @shubhamv.ai (Shubham Verma; 1,923 followers; Indian; "Simplifying AI for non-tech people"; builds Vestra, a startup app)
### BEST POST (builder story): https://www.instagram.com/p/DdZYtP0k8oI/ ("My Reddit post showed up in a Varun Mayya reel")
- date 2026-09-17, carousel, 11 slides (all viewed), likes 23, comments 2, shares 3; collab post with @eldobaggins and @vestra.ai_official. Hashtags #buildinpublic #aiagent. [Small account; craft sample]
- Audience: founders and builders in the Indian AI/startup community.
- One-line message: a rival "stealth" AI app got $2.5B-valuation press; the builder tested whether his own app works as well (11 of 12 testers preferred it) and decided to build in the open.
- Slides: 1 cover = left headline "One of India's biggest voices in AI, Varun Mayya, just used my Reddit post in his latest reel." + a phone-frame still of the actual reel; bottom: "Privileged, excited, and back to building Vestra" + "SWIPE ->". 2 "He used it to explain the AI story of the month." 3 "Instinct." + 3 micro-labels (No team page / No launch / Just a waitlist) + giant "$2.5 billion" 4 quote-card of his Reddit post + "Face on every post. Real name on every claim. So I asked Reddit: is that a mistake?" 5 "Both of us have a waitlist. Mine is a signup form. Theirs is a velvet rope." + "$2.5 billion... Something didn't add up." 6 "The comments had the answer." + 4 words (PR / Brand assets / Primed influencers / VC networks) + "Well planned. Well funded. It just looks accidental." 7 "Another comment reframed the whole question. A launch tactic with a shelf life. A brand play that takes years. They're not competing. They run on different clocks." 8 "My post ended on one question: does the thing work?" + "So I tested it. 12 people got invites to both... None of them knew I founded Vestra." 9 giant "11 of 12 preferred Vestra." 10 "Instinct is a good product. But mystery is a debt. Showing your face is prepaid." 11 close "We don't need to beat the hype machine. We just need to be the product you try next to it." + "Vestra | invite link in bio".
- Words per slide 15-40. Layout: dark editorial pages with serif type and ONE lime-yellow italic phrase per slide as the takeaway; tiny label top-left naming the beat (THE STORY, THE POST, SAME MECHANIC, THE REFRAME, THE TEST, THE RESULT, THE BET, LET'S GO) and counter "02/10"; a small teaser line bottom-left that bridges to the next slide ("Here's the part he didn't talk about", "Meanwhile I'm building in the same space. The opposite way.", "So I went looking for the answer", "Then another comment changed the question", "What I take from it"). 
- Cohesion: [OBSERVED] this is the strongest chaining device in the sample: every slide ends with a bottom-left "next line" in small type + an arrow, and the eyebrow label names the beat. A true story arc (hook, mystery, hypothesis, test, result, bet).
- Readability: grade ~9; jargon "waitlist", "velvet rope" explained in the same sentence; the "11 of 12" result is a giant number slide. Metaphors ("velvet rope", "mystery is a debt") are clever and need a beat of decoding; they sit next to a literal statement so they work for founders but would slow a general viewer.
- Hook: borrowed-authority hook (a famous name) + personal stake. The cover uses a screenshot of the reel as proof. Caption (first 125): "My Reddit post showed up in a Varun Mayya reel. Swipe for the story behind it, and the test that settled it for me. Grateful and excited to compete with the likes of Grokbot and Instinct." Short; CTA = invite code.
- Clarity verdict: 7/10 (9/10 for founders). Very clear structure; a general viewer meets unfamiliar brand names (Instinct, Grokbot) on slide 3 and never learns what Vestra does until the end (slide 11 only says "product you try next to it"). Lesson: the "I built X" post needs a literal one-line "X is an app that does Y" on the cover.
### WEAK POST (same account): https://www.instagram.com/p/DTm8okLkY15/ (AI isometric city maps: London, Dubai, Rome, Tokyo, New York; 5 slides, all viewed)
- date ~2026-01-17, likes 7, comments 0, 5 slides, ZERO words on the images (each slide = one AI-generated 3D diorama of a city). Caption: "Unlock the branding secrets behind 7-figure empires! Comment 'PROMPT' and we'll DM you the game-changing prompt pack... #BrandingHacks #DesignInspo #AIRevolution #MarketingMagic..." (promo-speak that does not describe the images; 7 hashtags; keyword-DM CTA).
- Difference in clarity: the Vestra post tells a story in words with progress cues; the city-map post is a text-free gallery whose caption talks about "branding secrets" for images that are cities - image and caption do not match. [OBSERVED] For Tangent's AI photo gallery: an image-only carousel with a mismatched hype caption got 7 likes; this is evidence that a gallery needs a plain label of what the images are and how they were made.

---
## ACCOUNT: @okaashish (Aashish Pahwa; 196K followers; likely Indian audience; "I speak AI, I teach AI, I choose to stay human"; founder of Koso.ai; 713 posts; carousels are cartoon-explainers)
Why picked: large audience, one consistent illustrated format (a bearded cartoon host and a black stick-figure pupil), massive share counts. Unusual: the images are AI-generated (a commenter says "the graphics in the post are obviously ai generated") and the account does not hide it.
### BEST POST: https://www.instagram.com/p/DdTUopHD8Qj/ ("How to stay human in the age of AI")
- date 2026-09-15, carousel, 13 slides (cover + 12 items viewed through #12), likes 41.7K, comments 253, shares 5.7K (the highest share count in the sample). Pinned post.
- Audience: broad general audience; low-tech.
- One-line message: 12 offline habits (read something long, call instead of text, get lost without GPS, be bored, fall in love...) keep you human when AI does your thinking.
- Slides: 1 cover = hand-lettered "HOW TO STAY HUMAN IN THE AGE OF AI" + cartoon of the two characters sitting on a giant phone with a map and a coffee (~9 words). 2-13 = one habit per slide: numeral in a circle + 2-5 word imperative in heavy hand-drawn caps + one cartoon that illustrates it literally: "01 Read something long" (scroll-length paper), "02 Make something badly" (wonky pot), "03 Call instead of text" (tin-can phone across a canyon of speech bubbles), "04 Eat with people", "05 Get lost without GPS", "06 Be bored for a while" (cloud-watching with a whale), "07 Buy something from a human" (market stall), "08 Remember a phone number", "09 Leave your phone at home", "10 Fall in love", "11 Trust your taste", "12 Take the long way".
- Words per slide: 2-5 (the lowest text load in the whole sample) + one illustration. Text ratio ~15%, picture ~85%. Identical template; white background, black outline art, one orange accent.
- Readability: grade ~2-3; no jargon; every instruction is concrete and doable. Cartoon metaphors are literal (a long scroll = "read something long").
- Cohesion: numbering 01-12, same frame, the two recurring characters (human + stick figure) create continuity; closing item "Take the long way" reads as a natural end. No bridge sentences - the list order is the chain.
- Hook: question-as-title ("How do you stay human in the age of AI?") + a relatable image. Caption (first ~125): "How do you stay human in the age of AI? As AI gets better at thinking, creating, communicating, and even making decisions for us, the things that make us human become even more important." (Edited.) Ends with an engagement question "What do you think we need to protect most?" and hashtags (#ai #artificialintelligence #stayhuman...). The caption states the thesis the slides never state.
- Clarity verdict: 10/10 as comprehension; it is also the most "engaging" format: shareable, quotable and zero-effort to read.
- Persona: the cartoon host (bearded, glasses, a likeness of the creator) is a face substitute; first-person voice is absent on slides.
### WEAK/CONTRAST POST: https://www.instagram.com/p/Dfttt8ECg7B/ ("Why does everyone want AI progress to halt?")
- date 2026-11-14 (1 day old at viewing), carousel, 10 slides (all viewed), likes ~143, comments 7, shares 5. [Age-adjusted: it is new, so low counts are partly recency; the contrast is still instructive.]
- Same cartoon host format but a NEWS explainer: slides 1-10 = speech-bubble dialogue panels with 25-45 words each ("Why does it suddenly feel like the whole world wants AI progress to halt?" / "Come, let me explain."; "Four nonprofits went to court" + a screenshotted tweet; "What changed about AI?"; "A test spilled into the real world" (Hugging Face incident); "Why ask for a freeze?"; "What are the AI labs asking for?"; "Why not slow down alone?"; "Could warnings double as ads?"; "Who can afford the new rules?"; "Who gets to pull the brake?"). Question headline per slide; 2-3 speech bubbles; embedded tweet/Reddit screenshots.
- Differences: (a) 3x-10x more words per slide than the 41.7K post; (b) topic requires prior context (OpenAI, METR, Redwood, Hugging Face); (c) abstract policy argument vs. 12 concrete life actions; (d) no imperative, nothing to do or share. [INFERENCE] The format is the same; the clarity and the share-worthiness are not. The question-headline-per-slide chain still gave good cohesion ("Why ask..? / What are the labs asking for? / Why not slow down alone? / Who can afford..? / Who gets to pull the brake?").
- Clarity verdict: 6/10 (the dialogue form helps, but heavy topic).
### Account pattern: @okaashish - a repeatable "host + pupil" cartoon system makes even policy topics approachable; his highest performers are the low-text lifestyle lists.

---
## ACCOUNT: @robakidtech (Ana Robakidze, founder of Theneo, YC; 1,421 followers)
### POST: https://www.instagram.com/p/DcOQqXRFyTo/ ("I've never posted about any of it." - founder's first post)
- date 2026-08-19, carousel, 9 slides (all viewed), likes 86, comments 17, shares 4.
- Audience: founders/builders.
- One-line message: after four years building an AI company (a language model that writes API docs), I'm going to post the real behind-the-scenes version.
- Slides: 1 = full-bleed photo of her speaking on stage, "Four years building an AI company. / I've never posted about any of it." + "SWIPE". 2 "So, hi. I'm Ana. I make API documentation for a living. I know. Stay with me." (the self-aware aside defuses boredom). 3 "Every job, same story. The API worked. The docs never did." (blue highlight on the key line). 4 "So we built a language model just for API docs. Paste in a spec, get docs back in seconds. Before ChatGPT existed." 5 "It was still a side project. We applied to Y Combinator anyway. We got in." + YC logo. 6 "We entered everything, Startup World Cup, TechCrunch Disrupt, Web Summit. We won more than 15." + stage photo. 7 "But that's the highlight reel. Nobody posts the rest." 8 "So here's what I'm actually going to post. The mistakes that cost us money. What a normal Tuesday looks like. San Francisco's brand of toxic. The founders who kept me sane." 9 "Following along? All of it. The good parts and the ones that aren't."
- Words per slide 12-30. Layout: warm off-white pages, one serif headline, ONE blue-highlighted phrase (the claim), photo slides interspersed, handle at bottom. Text 40-60%.
- Cohesion: narrative connectives ("So hi", "Every job, same story", "So we built", "It was still...We applied anyway", "But that's the highlight reel", "So here's what I'm actually going to post") - a story told in short declaratives, ending on a promise.
- Hook: confession of silence ("I've never posted about any of it") + face. Readability: grade ~6; the one technical term (API documentation) is explicitly named, laughed at ("I know. Stay with me.") and explained by consequence ("the docs never did [work]").
- Caption: long first-person story, restating the carousel with more detail (Google -> Head of Engineering -> YC). 
- Clarity verdict: 8/10. What is built (a language model for API docs) is stated plainly by slide 4. Persona: face on slides 1 and 6-7; humour in the first aside.
- Contrast: her post is a credibility intro, not a product demo; no screenshot of the product appears.

---
## ACCOUNT: @gregisenberg (Greg Isenberg; 156K followers; "building your ideas in the AI age"; single-image and meme posts, many reels)
Why picked: large builder audience; single-image craft; AI-content label visible on a post.
### BEST POST: https://www.instagram.com/p/DKw9h2-R95X/ (tweet screenshot "our kids will think we were crazy for using Google for 20 years")
- date 2025-06-11, single image, likes 124.5K, comments 924, shares 28.
- Image: black canvas, his tweet in large white sans text (about 55 words): "so you typed a question, got 100000 blue links gamed by SEO agencies, opened 11 tabs, skimmed each site, pieced together an answer, and repeated this process 20 times a day?" they'll think we were digital cavemen." Caption: "our kids will think we were crazy for using Google for 20 years" (the same sentence as the tweet headline). 
- Why it is clear: ONE idea, the quoted hypothetical child's disbelief, and a vivid concrete sequence (100000 blue links, 11 tabs). The metaphor ("digital cavemen") is instantly understood. No jargon.
- Clarity verdict: 10/10. Comment themes: agreement and jokes ("typing keywords into a search box was ancient").
### MID POST: https://www.instagram.com/p/DezgmLDxbVm/ ("POV: October 2026", flagged "AI content" by Instagram)
- date 2026-10-22, single image, likes 5.8K, comments 57, shares 441. A meme: a crouched, head-in-hands anime figure on a folding chair surrounded by 10 quote-bubbles of current AI-world worries ("Agent stack", "Software factory", "WebMCP", "Railway outage", "PHP", "Cheeky Pint", "GTA 6 delayed", "Data brokers", "$200 AI subscriptions", "Local AI"). Only understandable to people who know the references. Commenters add their own bubbles (the format invites co-creation). 
- Clarity verdict: 4/10 for a general viewer (insider references), 9/10 for the builder in-group; engagement is high because in-jokes signal belonging.
### WEAK POST: https://www.instagram.com/p/DKhiZPeRwN3/ ("lock in for AI summer": a screenshot of a text-editor window with a wall of all-caps text)
- date 2025-06-05, single image, likes 1.1K, comments 65, shares 10.
- Difference: a ~230-word block of text in small type inside an app window ("LOOK AT THIS BLOCK OF TEXT BECAUSE WITH AI THIS IS THE GREATEST TIME IN HUMAN HISTORY TO START A COMPANY...") - unreadable at feed size. Same author, same message family, ~100x fewer likes than the 55-word tweet card. [OBSERVED] Word count and font size explain most of the difference: 55 words at large type got 124.5K; 230 words in small type got 1.1K.
### Account pattern: @gregisenberg - his top image is a single legible idea; the format (tweet screenshot) is the lowest design effort in the sample and the highest-performing.

---
## ADDITIONAL HARPER POSTS (best vs weak within one big account)
### https://www.instagram.com/p/DMrPTAPR3Na/ ("Top AI scientists call for urgent research into reasoning models' chain-of-thought (CoT) outputs")
- date 2025-07-29, carousel, 7 slides (all viewed), likes 1.9K, comments 32, shares 1.
- Slides: 1 cover = three-part sandwich: big white all-caps headline on green "TOP AI SCIENTISTS CALL FOR URGENT RESEARCH INTO REASONING MODELS' CHAIN-OF-THOUGHT (CoT) OUTPUTS" / a video frame of her on TBPN / "PLUS: RESEARCH SHOWS THEY DON'T RELIABLY SAY WHAT THEY THINK" (~28 words, jargon-dense). 2 = screenshot of her own tweet; 3 = a video clip frame with caption "Open and..." (the slide is a clip); 4 = screenshot of the paper's first page "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety"; 5 = screenshot of the Anthropic paper "Reasoning Models Don't Always Say What They Think"; 6 = a diagram from the paper + "They also tested with deliberately incorrect hints."; 7 = "Follow for more educational AI content" (plain text).
- Readability: grade 14+; dense terms (chain-of-thought, CoT, monitorability) never defined on a slide; slides are raw screenshots of papers. Cohesion: only through the caption; no on-slide bridge.
- Caption first 125: "REASONING MODELS ARE TOP-OF-MIND FOR MAJOR AI RESEARCHERS I was recently on @tbpn discussing a few topics, including reasoning models." 
- Clarity verdict: 3/10 for a general viewer. Performs (1.9K likes) because of her authority and the news hook.
### https://www.instagram.com/p/DYGWf5pDAWn/ ("What's left until AGI?")
- date 2026-05-09, carousel, 2 slides (slide 2 appeared identical to slide 1 in my viewer, so it may be a pure duplicate or a render issue), likes 451, comments 20, shares 4.
- Content: a text-only card styled as a social post with her avatar and a 55-word paragraph (Hassabis says "continual learning, long-term reasoning, some aspects of memory", AGI estimate 2030). Caption asks "What do you think? Do you think a lab may have achieved AGI?" 
- Clarity: 6/10; plain sentences but no visual; engagement lowest among her posts viewed.
### Comparison within Harper (7 posts viewed): clarity by design: context windows (8/10, 162 comments) > AGI/ASI (7/10, 2.7K likes) > Tokenmaxxing (5/10) > reasoning models (3/10, 1.9K likes). Likes do NOT track clarity within this account; they track news/authority, so for an unknown account, clarity must carry the post.

---
## ADDITIONAL TIFFINTECH POST (image-led)
### https://www.instagram.com/p/DX4ecU8FE2E/ ("Humanoids are no longer science fiction", Neo factory stills)
- date 2026-05-03, carousel, 8 slides (all viewed), likes 2.3K, comments 39, shares 20.
- 8 video stills, ZERO text overlays: (1) her interviewing the 1X Neo humanoid in a showroom (landscape frame), (2) the robot alone in a hall, (3) two interviewers seated with the robot behind, (4) the robot waving at a front door, (5) a factory scene with "HANDS" title, (6) a technician and her at a CNC machine, (7) her with an engineer on the factory floor, (8) a comparison of a robot hand and a human hand with keypoints.
- Caption (first 125): "Humanoids are no longer science fiction. They're being built right now, and we went inside the factory making it happen." then "Some stills from our latest video covering the 1X Neo Factory!" The caption states the claim the images illustrate.
- Compared with her chip explainer (9/10 clarity, 41 comments): this post has more likes (2.3K) with no text on slides; the image of a robot is its own hook. Clarity verdict: 7/10 - the pictures are self-explanatory and curiosity-provoking but explain nothing alone.

---
# TEMPLATES TANGENT COULD BORROW
(Each is built from slides actually observed. Word targets are from the observed clear posts. Replace bracketed items.)

### Template A: "I BUILT AN APP WITH AI" (the Tangent core story)
Evidence: https://www.instagram.com/p/DezcWvgoP1Z/ (Jacklyn), https://www.instagram.com/p/DZMxVIiCD7L/ (Ayesha), https://www.instagram.com/p/DWoa5SWDmuk/ (Luis), https://www.instagram.com/p/DdZYtP0k8oI/ (Shubham), https://www.instagram.com/p/DcOQqXRFyTo/ (Ana).
1. COVER (<=15 words + the thing): "Hi, I'm [name]. I built [App] with AI." + a photo of you OR a phone screenshot of the finished app. Add one literal line: "It [does X for Y]." Swipe cue.
2. BEFORE (<=25 words): "Before this, I [hobby / day job]. I don't write code." (admission = trust)
3. PROBLEM (<=25 words): "Then I [ran into / wanted]..." the real everyday problem in a sentence a stranger could say back.
4. BUILD (<=25 words + screenshot): "So I asked [AI tool] to [one verb phrase]." Show the real prompt or the first screen.
5. PAYOFF (<=25 words + the app's best screen): "Now [what the app does for me today]" with ONE number if you have it (hours saved, 2 hours to build, 11 of 12 testers).
6. CTA (<=15 words): "Try it / see it: [link in bio]" or a question: "What would you build?" Optionally "save this for your first build."
Rules from evidence: first-person connectors on every headline (Before / Then / So / Now); one proof visual per slide; counter "n/6"; one candid aside on a failure ("claude gaslit me", Ayesha); never lead with the tool or model name.

### Template B: "AI EXPLAINED SIMPLY" (question-headline chain)
Evidence: https://www.instagram.com/p/DUQ_6LXkqR2/ (Harper context windows), https://www.instagram.com/p/DYkM7zZlAwz/ (Tiffin chips), https://www.instagram.com/p/DRukrQYDsWD/ (Harper AGI staircase).
1. COVER: the question a layperson asks, as the headline, 4-8 words ("Why AI forgets things.").
2. "What is [the thing]?" - one everyday metaphor + 3 bullets of <=12 words.
3. "Why does it [matter / go wrong]?" - one concrete consequence.
4. "What happens when [edge case]?" - one example with real numbers.
5. "What can you do about it?" - 3 steps (strategy).
6. CTA: a single question or "Save this".
Rules: <=40 words per slide, a 4-8 word headline that is a complete claim or question, a repeated frame, define any term in the slide where it first appears.

### Template C: "ONE NOUN PER SLIDE" claim chain (Tiffin pattern)
Evidence: https://www.instagram.com/p/DYkM7zZlAwz/.
Cover: a big surprising literal claim + face. Slides 2-8: each headline = "One [noun] [verb]" (One chip touches 70+ countries. One company controls the machines. One island powers modern technology.) + one supporting line or 3 icon facts. Closer: "The most [X] thing is also the most fragile" + comment question. Works for any "how this thing works behind the scenes" post, e.g. how Panditji computes a chart.

### Template D: "BUILD, DON'T BUY" numbered showcase (Luis)
Evidence: https://www.instagram.com/p/DWoa5SWDmuk/. Cover lists all N items as chips; slides 2..N+1 = same split frame: left = screenshot of the thing, right = "App K of N" + noun-phrase headline + what it replaces + 2 lines; closer = totals. Good for Tangent's "small everyday AI apps" series.

### Template E: "LIST OF 12 PICTURES" low-text shareable (Aashish) and "TIPS WITH A PROBLEM/FIX BOX" (zoof04)
Evidence: https://www.instagram.com/p/DdTUopHD8Qj/ (12 habits, 2-5 words each, one literal cartoon/photo each, 41.7K likes and 5.7K shares), https://www.instagram.com/p/DfiTkHUgY40/ (5 checks; "The problem" one sentence + "The fix" one copy-paste instruction). For Tangent's AI photo gallery: "12 photos, 12 edits" - one before/after plus a 3-word label per slide ("Brighter sky", "Remove tourist"), numbered; cover = the best result.

---
# UPDATED CROSS-ACCOUNT LESSONS (all 26 posts)

Set analysed: 26 posts, every slide viewed (Harper 6, Ishan 3, Tiffin 2, Rowan 1, Varun 1, Luis 1, zoof04 1, Shubham 2, Okaashish 2, Robakidtech 1, Greg 3 single images, Jacklyn, Dhruv Rane, Ayesha 1 each). Coverage caveats: Harper DYGWf5pDAWn slide 2 looked identical to slide 1; Shubham slide 8 initially failed to render and was re-viewed.

A. Words per slide vs. performance and clarity [OBSERVED]
 - 2-5 words + 1 picture: 41.7K likes / 5.7K shares (Aashish 12 habits). 14-35 words: 8-9/10 clarity posts (Tiffin chips, Harper context windows, Ishan INFINITY, zoof04). 55-75 words: lower clarity (Harper AGI). 230 words in an app window: 1.1K likes vs. 124.5K for a 55-word card from the same author (Greg).
 - Cover = lightest slide in every high-clarity post (4-15 words).
B. Slide count [OBSERVED]: 5 (Jacklyn) to 14 (Aashish); 6-9 is the typical explainer/story length; 10-14 works only when every slide is one repeated 3-word item (Aashish).
C. Headline vs. visual [OBSERVED/INFERENCE]: the winning relationship is literal: headline = the claim, visual = a picture of the thing named in the headline ("Call instead of text" = a cartoon of a phone; "A custom CRM..." = the CRM screenshot). Decorative photos work only with a famous face (Ishan, Rowan, Varun). Image-only galleries need a plain label (Shubham 7 likes; Tiffin stills worked only because the caption supplied the claim).
D. Jargon [OBSERVED]: successful pattern = plain noun first, term second, defined in place, or consequence instead of term (zoof04: "Secret keys showing: anyone can copy them and run up your bill"). Failure pattern = undefined acronym in the cover (Harper "Tokenmaxxing", "CoT"); Greg's insider-bubble meme works only for the in-group.
E. Hook wording [OBSERVED]: strongest covers are one literal sentence in first person or a plain claim: "I built Shelf by JC with AI." / "i vibe-coded my first app in just 2 hours!" / "The world runs on one tiny chip." / "Why AI forgets things." / "How to stay human in the age of AI" / "5 mistakes that can sink your app." / "6 Apps to Build With Claude Code Instead of Paying For." / "Read This Before You Turn 25" / "our kids will think we were crazy for using Google for 20 years". All 4-12 words, no metaphor needing decoding, a number or a person in half of them.
F. Chaining [OBSERVED]: (1) connectors Before/Then/So/Now (Jacklyn, Ana); (2) step N (Ayesha); (3) anaphora One... (Tiffin); (4) question-answer headlines (Harper, Aashish news post); (5) per-slide teaser line + arrow + beat label (Shubham Vestra); (6) "App K of N" counters (Luis, Ishan "n/9"); (7) refrains that bookend the post ("A course ends. AI doesn't." slides 3 and 9, Ishan); (8) recap slide (Harper AGI, zoof04).
G. "I built X with AI" stories that land [OBSERVED + INFERENCE]: in the larger accounts (Luis 21.6K, Shubham, Ana), what works is (a) the build is shown as an outcome with money or time numbers (HubSpot $1,200/yr vs. built once; 2 hours; 11 of 12 testers), (b) a screenshot of the real thing every slide, (c) the author states what the thing DOES in one literal sentence on slide 1 (Luis does; Shubham and Dhruv do not), (d) a personal confession. Weak spots: no face or no explanation of purpose (Dhruv), brand names unknown to cold viewers (Shubham slide 3). No creator with 50K+ followers posts a pure "my first app" carousel; the big builder accounts (Riley Brown 332K, Greg 156K) post it as reels or single images, so the closest large-scale proof for carousels is Luis (21.6K).
H. Captions [OBSERVED]: five modes: (1) restate-then-extend (Harper, Rowan, Jacklyn, Ana); (2) single plain sentence that is the same as the cover (Greg 124.5K tweet; Tiffin chips); (3) long list repeating the slides with a keyword CTA (Luis "Comment CLAUDE", Ishan "INFINITY", Harper "GUIDE"); (4) hashtag-stack promo copy that does not describe the images (Shubham city maps: "branding secrets", 7 hashtags; 7 likes); (5) a question that invites an answer (Aashish "What do you think we need to protect most?", zoof04's recap). Hashtags: none on big-creator carousels except Aashish (a handful) and small builders (3-7). AI disclosure: only Instagram's own "AI content" label on Greg's meme and the Ishan/Nandini collab post; Aashish's cartoons are AI-made and unlabelled by the creator but acknowledged by commenters.
I. What separates most-engaged from weak [OBSERVED]: (1) one legible idea at feed size (Greg 55 words 124.5K vs. 230 words 1.1K); (2) a share-worthy "do this" list with concrete actions (Aashish 12 habits: 5.7K shares) vs. a policy debate in the same format (143 likes, new); (3) authority or an offer (Ishan, Varun); (4) a shareable in-group joke (Greg POV 441 shares). Weak: text-free galleries with promo captions, raw paper screenshots, walls of text. For a new account without authority, (1) and (2) are the levers.
J. Persona [OBSERVED]: face on the cover and a "why listen to me" slide (Harper); real life photos as proof (Ishan); a cartoon avatar standing in for the face (Aashish); self-deprecating asides ("I don't understand a thing about code", "I know. Stay with me.", "claude gaslit me") are the warmest lines in the set and appear in the three clearest builder posts.
K. Mapped to Tangent's failed carousel (INFERENCE): "The AI kept moving Saturn. So I took the maths away from it." / "One sky, two ways to count it." / "Checked against the sky's reference books." / "427 ways to ask the wrong thing. Tested." break the observed rules: the headlines do not state a literal claim (what changed? what was tested?), they use metaphor (math taken away, reference books) with no plain restatement, and they have no connective that makes them one sentence. A same-length rewrite following Template A: "Hi, I'm Sparsh. I built Panditji with AI." / "I wanted a Vedic astrology guide that doesn't guess." / "But the AI kept getting Saturn's position wrong." / "So I let a calculator do the maths and the AI only explains it." / "Now it matches the standard tables, in 427 tests." / "Try it: link in bio." (Phrasing is only an illustration of structure.)
