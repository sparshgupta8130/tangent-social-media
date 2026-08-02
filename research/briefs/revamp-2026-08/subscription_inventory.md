# Capability Inventory — Google AI Ultra vs. Claude Max 20x

**Compiled:** 2026-08-02. All quotas/limits are **as-of this date** and flagged with source + confidence — both vendors change these often (Google restructured its entire Ultra lineup on 2026-05-19; Anthropic has flip-flopped on Agent SDK billing at least once in 2026). **Do not treat any number below as permanent — re-check before a purchase decision or a hard production commitment.**

Confidence legend: **High** = confirmed on a live official page, recent and consistent. **Medium** = official but ambiguous/single-sourced, or press-confirmed only. **Low/Unconfirmed** = flagged gap, treat as a guess.

---

## SUBSCRIPTION A — Google AI Ultra

### 0. Name & price (verify before assuming the old numbers)

Google restructured the plan at **I/O 2026 (2026-05-19)**. "Google AI Ultra" is now **two SKUs under one brand name**, not the old single $249.99/mo tier:

| Tier | Price/mo | Storage | Flow (video) credits/mo | Flow Music credits/mo |
|---|---|---|---|---|
| Ultra (lower) | **$99.99** | 20TB | 10,000 | not separately confirmed |
| Ultra (upper, was $249.99) | **$199.99** | 30TB | 25,000 | 30,000 (~6,000 songs, estimate) |

Sources: [gemini.google/subscriptions](https://gemini.google/subscriptions/) (live), [blog.google I/O 2026 subscriptions post](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/) (2026-05-19), [Antigravity plans blog](https://antigravity.google/blog/changes-to-antigravity-plans) (2026-05-19). **Confidence: High** on the two-tier structure and prices; **Medium** on exact 20TB/30TB↔price pairing (no single page states both in one sentence) and on Flow Music's Ultra-lower-tier allocation.

This document uses the **$199.99/mo tier** as "Google AI Ultra" per the brief's $200-250 bracket, since it's the direct successor to the old $249.99 plan and gets the highest limits everywhere. The $99.99 tier is noted where it materially differs.

> 9to5Google reported Google had to UI-patch checkout because two identically-named "Ultra" tiers confused buyers ([2026-05-25](https://9to5google.com/2026/05/25/google-one-ai-ultra-clarification/)) — a sign this is a genuinely recent and still-settling change.

### 1. Video — Veo / Flow

- **Model:** **Veo 3.1** (sub-variants Lite/Fast/Quality) remains the API/precision baseline; the **consumer Gemini app now defaults to "Gemini Omni Flash,"** a unified multimodal gen/edit model shipped at I/O 2026. No Veo 4 exists as of 2026-08-02 — Google shipped Omni instead. Sources: [ai.google.dev/gemini-api/docs/video](https://ai.google.dev/gemini-api/docs/video), [support.google.com/flow/answer/16352836](https://support.google.com/flow/answer/16352836). **High confidence.**
- **Flow credits (Ultra $199.99 tier): 25,000/mo.** Per-generation costs (official, [support.google.com/flow/answer/16526234](https://support.google.com/flow/answer/16526234), High confidence):
  - Veo 3.1 Lite: **5 credits** (Ultra rate; 10 for lower tiers)
  - Veo 3.1 Fast: **10 credits** (Ultra rate; 20 for lower tiers)
  - Veo 3.1 Quality: **100 credits** (flat, all tiers)
  - Gemini Omni Flash generation: 15/20/25/30 credits for 4s/6s/8s/10s
  - Gemini Omni Flash editing: 40 credits flat
  - 1080p upscale: free (Plus/Pro/Ultra) · **4K upscale: 50 credits, Ultra-exclusive**
- **Clip length:** 4s/6s/8s base; Fast and Quality add 10s. Longer output only via chained **Extend**.
- **Resolution:** native sub-1080p + upscale layer — 1080p free, **4K Ultra-only**.
- **9:16 vertical:** confirmed, all Veo 3.1 variants support both aspect ratios. **High confidence.**
- **Image-to-video:** "Ingredients to Video" (multi-reference-image → video, character/style control), frames-to-video (first frame now; first+last "coming soon" on Quality). **High confidence.**
- **Native audio:** SFX, dialogue, and music generated in-sync with visuals, built into both Veo 3.1 and Omni. Custom/consistent character voice via "ingredients"-based generation. **High confidence.**
- **Scene Extension / Extend:** feature confirmed to exist; **no official numeric cap found** on chain length or count despite checking the dedicated help page ([support.google.com/flow/answer/16935718](https://support.google.com/flow/answer/16935718)) — a 2025-10-15 blog post said chained output can run "a minute or more," but that predates the May 2026 restructure. **Flag: unconfirmed ceiling.**
- **Commercial use:** Flow's help page states "Google won't claim ownership over that content" ([support.google.com/flow/answer/16353333](https://support.google.com/flow/answer/16353333)) — but **no dedicated, tier-specific commercial-licensing document was found**. Treat as **medium confidence you own it, low/unconfirmed on exact monetization/resale terms** — verify directly in-account before monetizing at scale.
- **SynthID:** invisible watermark is universal and always-on ([deepmind.google/technologies/synthid](https://deepmind.google/technologies/synthid)). **Visible watermark removed for Ultra on images**, confirmed. For **video specifically, Ultra visible-watermark removal is weakly sourced** — plausible by analogy, not independently confirmed. **Flag as unconfirmed for video.** SynthID Detector (public verification tool) still appeared waitlist-gated in the fetched page (undated) — in-Gemini-app "is this AI-generated" checking was announced broadly at I/O 2026, not Ultra-exclusive.

### 2. Image — Nano Banana (Imagen is being retired)

- **Imagen 4 is deprecating 2026-08-17** (roughly two weeks after this document's date) — [ai.google.dev/gemini-api/docs/imagen](https://ai.google.dev/gemini-api/docs/imagen). **High confidence.** Don't build a workflow around it.
- **Actual current top image model: Nano Banana Pro (= Gemini 3 Pro Image),** launched 2025-11-20 — [blog.google Nano Banana Pro post](https://blog.google/innovation-and-ai/products/nano-banana-pro/). **2K/4K resolution**, multi-image blending (up to 14 images), character consistency (up to 5 people), localized/inpainting-style editing, lighting/color-grade/depth control, multilingual text-in-image rendering. **High confidence.**
- **Nano Banana 2 (Gemini 3.1 Flash Image)** — faster/lighter sibling, 2026-02-26. **Nano Banana 2 Lite** serves the free tier inside Flow. Ultra gets **Nano Banana Pro as the default**. **High confidence.**
- **Whisk no longer exists as a standalone product** — folded into Flow's unified image/ingredients-to-video tools as of 2026-02-25 ([blog.google Flow Feb 2026 update](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/)). Describe its capability (image-prompted remixing) as now inside Flow, not as a separate app.
- **Google Pics** (new dedicated image tool, object segmentation, text editing/translation, Workspace integration) was announced at I/O 2026 for a **"summer 2026" rollout to Pro/Ultra** — **unconfirmed whether it has actually shipped by 2026-08-02.** Check live before including it in workflow plans.
- **Limits:** images and video draw from the **same shared Flow credit pool**; exact per-image credit cost was **not disclosed** in any page reached — **flag as gap.** Nano Banana Pro inside plain Gemini chat gives paid tiers "higher quotas" than free with **no published number** — **flag as gap.**
- **Editing:** localized edits/inpainting, object add/remove, multi-image blend, face consistency, lighting/color/depth/camera-angle control, freehand annotation, natural-language edit commands. "Style transfer" as a literal label wasn't used verbatim in official copy but the capability is covered. **High confidence** on capabilities, **medium** on the "style transfer" label specifically.

### 3. Music/audio — Lyria, Flow Music, MusicFX (dead), TTS

- **MusicFX and MusicFX DJ were shut down 2026-07-31** — two days before this document's date — in favor of Flow Music. Source: Google Labs' own announcement, corroborated by [alphasignal.ai](https://alphasignal.ai/news/google-kills-musicfx-to-go-all-in-on-flow-music). **High confidence the shutdown happened; the primary post itself was paywalled on fetch, corroborated by one secondary outlet only.** **Do not list MusicFX as a live product.**
- **Current model: Lyria 3.5** (2026-07-29) — [blog.google Lyria 3.5](https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/). Lineage: Lyria 2 → Lyria 3 (Feb 2026) → Lyria 3 Pro (2026-03-25, full ~3-minute songs with verse/chorus structural prompting) → Lyria 3.5 (current). **High confidence.**
- **Access:** Full songs (not just loops) generated directly in the **Gemini app** ("available to paid subscribers") and in the dedicated **Google Flow Music** app. In-place editing — highlight a section, rewrite/restyle/translate just that part. **High confidence.**
- **Ultra allocation:** Flow Music "Member" plan benefits + **30,000 credits/mo**, informally equated to **~6,000 songs/mo** by a secondary source (conversion not officially documented). **Medium confidence** on the credit figure (official), **low-medium** on the songs-per-month conversion.
- **Music AI Sandbox:** still exists as a **separate invite/waitlist program** for professional musicians (grew out of YouTube's Music AI Incubator) — **not bundled into the Ultra consumer subscription**. Most recent official confirmation dates to 2025-04-24; may be merging into Flow Music's Believe/TuneCore artist partnership (2026-05-06) — **unconfirmed, flag as possibly stale.**
- **Commercial use:** Google's Believe partnership post states "Google doesn't claim ownership of the original content generated with Flow Music" — but **no explicit monetization/platform-distribution license text found** (e.g., YouTube Content ID eligibility). **Medium confidence on ownership, low/unconfirmed on monetization terms** — verify before releasing monetized music.
- **Speech/TTS:** Gemini Live voice mode refreshed at I/O 2026; voice features for Gmail/Docs/Keep ("Docs Live," "Talk to Keep") announced for "summer 2026" to Pro/Ultra — **unconfirmed whether shipped yet.** Standalone API TTS (Gemini 3.1 Flash TTS Preview, updated 2026-07-30) offers **30 prebuilt voices, multi-speaker, streaming** — but **explicitly no voice cloning** ([ai.google.dev/gemini-api/docs/speech-generation](https://ai.google.dev/gemini-api/docs/speech-generation)). **High confidence** this is API/AI Studio-surfaced, not a dedicated consumer TTS app.

### 4. NotebookLM → renamed "Gemini Notebook" (2026-07-16)

Rebrand: [blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/), **High confidence**. Same product/purpose, new name and URLs (`support.google.com/gemininotebook/`).

**Daily limits (official, [support.google.com/gemininotebook/answer/16213268](https://support.google.com/gemininotebook/answer/16213268), High confidence, cross-checked against two independent aggregators):**

| Feature | Free | Plus | Pro | Ultra 20TB | Ultra 30TB |
|---|---|---|---|---|---|
| Notebooks | 100 | 200 | 500 | 500 | 500 |
| Sources/notebook | 50 | 100 | 300 | 500 | 600 |
| Chats/day | 50 | 200 | 500 | 2,500 | 5,000 |
| Audio Overviews/day | 3 | 6 | 20 | 100 | 200 |
| Video Overviews/day | 3 | 6 | 20 | 100 | 200 |
| Cinematic Video Overviews/day | — | — | 2 | 10 | 20 |

Hard caps regardless of tier: 500,000 words/source, 200MB/file, no copy-protected PDFs.

- **Audio Overviews ("podcast"):** 4 formats — **Deep Dive** (2 hosts, default), **The Brief** (1 host, <2 min), **The Critique** (2 hosts, evaluative), **The Debate** (2 hosts, structured). Length control (Shorter/Default/Longer, English-only), 80+ output languages, free-text custom-instruction steering. Host voices appear **fixed per format, not user-selectable/brand-consistent** — unconfirmed either way, worth hands-on verification. **No confirmed post-generation editing** (best inference from the Video Overview docs is regenerate-only, not directly confirmed for audio) — **flag as gap**, and export format/bitrate specs weren't documented anywhere official.
- **Video Overviews:** three formats — **Explainer** (50+ languages, narrated-slides style), **Cinematic** (launched 2026-03-04, English-only, 18+, built on Gemini 3 + Veo 3 + Nano Banana Pro, original animation/storytelling, ~2-5 min per secondary source), **Short** (launched 2026-06-30, ~60s vertical, Ultra+Pro, web+mobile, English-only, 18+). Style presets: Classic, Whiteboard, Watercolor, Retro Print, Heritage, Paper-craft, Kawaii, Anime, or custom text description. Generation can exceed 30 min, runs in background. Sharing via link, full notebook, or file download.
- **Other Ultra perks:** per-notebook code execution / "cloud computer" (new with the July rebrand, Ultra + Workspace first). **Deep Research integration into Gemini Notebook: no evidence found either way — flag as unconfirmed.**
- **Podcast-production honest take:** genuinely strong for volume (100-200 audio overviews/day means quota is a non-issue) and format variety, weak on voice brand-consistency and post-edit control — best used as a fast draft/explainer generator feeding into a real edit pass, not a drop-in finished-podcast pipeline.

### 5. Gemini app — models, Deep Research, Canvas, Gems, agentic features

- **Models (live, [deepmind.google/models/gemini](https://deepmind.google/models/gemini/)):** Gemini 3.5 flagship family, **Gemini 3.6 Flash** (2026-07-21, coding/knowledge work), Gemini 3.5 Flash-Lite, **Gemini 3.1 Pro**, **Gemini 3.1 Deep Think** (reasoning), Gemini 3.5 Pro listed **"coming soon."** Base "Gemini 3 Pro" is available at **all paid tiers**, not Ultra-exclusive — Ultra-exclusive is **Deep Think** (originally launched 2025-12-04 as "Gemini 3 Deep Think," now 3.1). Model-version labeling is genuinely churning roughly monthly across Google's own pages — treat exact version numbers as soft, the tier hierarchy (Ultra = best model + Deep Think + biggest context) as solid.
- **Context window:** Free 32k · Plus 128k · **Pro & Ultra 1,000,000 tokens** — confirmed on two independent official pages. **High confidence.**
- **Deep Research:** browses "hundreds of websites" plus your Gmail/Drive/Chat, 150 countries, 45+ languages, now "powered by Gemini 3." **Quota system changed 2026-05-17**: fixed daily numbers (the old "Ultra = 200 reports/day" figures still floating around online) were **replaced by a compute-based system** — usage metered by task complexity, refreshes every 5 hours, weekly cap. Multipliers: Plus 2x, Pro 4x, **Ultra 5x or 20x standard** depending on sub-tier. **No absolute current number is published** — any specific figure you see cited for 2026 is very likely a stale pre-restructure number. **High confidence the system changed; flag the lack of an absolute number as a real gap for production planning.**
- **Canvas:** available at **all tiers including free** — prompt-driven apps/games, quizzes, web pages, infographics, code visualization, docs, dashboards; can turn Deep Research output into a web page/infographic/quiz/audio overview. Ultra's edge is the top model + 1M context for bigger projects, not exclusive features.
- **Gems:** custom AI experts with saved instructions + file context, available even on free tier. **No official tier-specific limits (max Gems, Ultra-only agentic capability) were found — flag as a real gap**, this section is thin in official docs.
- **Project Mariner: discontinued 2026-05-04.** Folded into **"Gemini in Chrome" auto-browse**, which is notably now listed as a **Pro-tier feature too**, not Ultra-exclusive — a real downgrade in exclusivity versus the Mariner era. **Medium confidence** on shutdown mechanics (secondary press only, no direct blog.google post found).
- **Jules (async coding agent) — bundled, tiered, GA at I/O 2026:**
  | Tier | Tasks/day | Concurrent | Model |
  |---|---|---|---|
  | Free | 15 | 3 | Gemini 2.5 Pro |
  | Jules Pro (with AI Pro, $19.99) | 100 | 15 | Gemini 3 Pro |
  | **Jules Ultra (with AI Ultra)** | **300** | **60** | Gemini 3 Pro, priority |

  Source: [jules.google](https://jules.google) (official, live). **High confidence** on the numbers; model-version label may lag the very latest Gemini release by a point-version.
- **Gemini Spark — new, Ultra-exclusive, the standout 2026 addition.** A **24/7 autonomous personal agent** on Google Cloud VMs (keeps working after your laptop closes), built on Gemini 3.5, works across Gmail/Docs/Slides/Calendar plus MCP connections to third-party apps (Canva, OpenTable, Instacart, Dropbox, Zillow Rentals, Tasks, Keep). Launched I/O 2026 (2026-05-19), reached **Beta for US Ultra subscribers 18+ starting 2026-05-26**, expanded to **macOS 2026-06-30** (desktop automation, proactive topic-tracking alerts, custom MCP support). **High confidence on the feature and gating (Ultra-only, US-only, 18+, Beta); unconfirmed whether it's expanded past US by 2026-08-02** — last-confirmed state may be ~1-2 months stale.
- **Antigravity (agentic coding IDE):** Pro/Ultra get priority/highest rate limits on a compute-based system (5-hour refresh). Post-restructure: **$99.99 Ultra = 5x** Pro's token rate, **$199.99 Ultra = 20x**. Credits are now an overage mechanism, not bundled allowance.
- **Project Genie (Genie 3 world model):** real-time interactive-world generation, tied to the **$199.99 Ultra tier** specifically per the clearest source; inclusion in the $99.99 tier is **unconfirmed**.

### 6. Storage / bundling

- **Storage:** Ultra $99.99 = **20TB**, Ultra $199.99 = **30TB** (direction confirmed, exact price↔TB pairing only medium-confidence since no single page states both together). Pro = 5TB, Plus = 2TB, Free = 15GB.
- **YouTube Premium:** full **YouTube Premium** (ad-free, offline, background play, YT Music) bundled with Ultra; Pro gets the lesser **YouTube Premium Lite**. **High confidence.**
- **Other Ultra perks (official, I/O 2026 announcement + Google One support page):** Google Home Premium **Advanced** plan (Pro gets "Standard"), Google Health Premium (Gemini AI coaching), highest Google Photos photo-to-video/Remix limits, **~$40/mo Google Cloud credits** claimed on one page (medium confidence, not cross-verified), 1,500-page file upload and ~30,000 lines-of-code analysis capability (inherited from Pro tier), **Google Pics** ("summer 2026" rollout — unconfirmed if live yet).

---

## SUBSCRIPTION B — Claude Max 20x ($200/month)

### 7. Usage, limits, and inclusions

- **How limits work:** Anthropic **does not publish exact token/message quotas** for any plan — burn rate depends on conversation length, model, and reasoning effort. Max 20x = "**20x more usage than Pro per 5-hour session**." Max 5x = 5x Pro. Source: [support.claude.com — What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) **High confidence** on the multiplier framing; unofficial estimate (medium confidence, [IntuitionLabs](https://intuitionlabs.ai/articles/claude-max-plan-pricing-usage-limits)) puts Max 20x around **~220k tokens/5-hr window**, roughly **240-480 Sonnet-hours/week** and **24-40 Opus-tier-hours/week** — treat as ballpark, not contract.
- **Weekly caps:** Max plans carry **two** weekly limits — one across all models, one Sonnet-specific. Pro has only one (all-models). Resets at a fixed per-account time, visible in Settings > Usage. **High confidence.**
- **A "+50% weekly limits" promotion** was reported running through **2026-08-19** for Pro/Max/Team/seat Enterprise — **medium confidence, time-boxed, may have changed by the time you read this.**
- **Shared pool across every surface:** claude.ai web/mobile/desktop, Claude Code, Cowork, Chrome extension all draw the **same** usage pool. This is the single most important practical fact — running several surfaces concurrently drains the budget faster than expected.
- **Flagship model:** **Claude Fable 5** included on Max, but capped at **up to 50% of your weekly usage limit** on that specific model — [support.claude.com — Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan). **High confidence.** Recent model ships: **Claude Sonnet 5** (2026-06-30), **Claude Opus 5** (2026-07-24), with Fable 5 positioned as the flagship above Opus-tier.
- **Overage:** metered "usage credits" at standard API rates once you exhaust plan limits, **$2,000/day redemption cap**. **High confidence.**

**Practical constraint:** the 5-hour rolling session cap and the two weekly caps (all-models + Sonnet-only) are the real walls. Because every surface shares one pool, stacking Cowork + Claude Code + chat concurrently is the fastest way to hit them — and because Anthropic won't publish hard numbers, you can't precisely budget in advance, only monitor via Settings > Usage.

### 8. Feature-by-feature, with the practical constraint that matters

**Claude Code** — included at no extra charge across terminal/VS Code/Cursor/JetBrains, shares the Max 20x pool (no separate quota). Supports sub-agents, background/parallel sessions, `--chrome`, computer use (macOS research preview), Routines (see below), Remote Control, `--teleport`/`--cloud`, Slack `@Claude`, CI integration. **Contested/volatile area:** Anthropic announced (effective 2026-06-15) that non-interactive Agent SDK use, `claude -p` headless mode, and GitHub Actions would move to a **separate** monthly credit pool ($200 for Max 20x) — but the live official Agent SDK support page, fetched today, says this was **"paused"** and such usage **"still draw[s] from your subscription's usage limits."** **This flip-flopped once already in 2026 — verify same-day before relying on it.** *Practical constraint:* agentic coding loops burn tokens per turn much faster than chat, so a long Claude Code session eats the shared weekly budget disproportionately.

**Claude in Chrome** — beta extension, GA underlying capability, available on **all paid plans** (not Free), Chrome/Edge officially (Claude Code auto-detects Brave/Arc/Vivaldi/Opera), no separate quota. Requires direct Anthropic account login — not usable via Bedrock/Vertex/Foundry. A 2026-07 Malwarebytes report flagged a rogue-extension/Gmail-access risk worth a footnote for sensitive workflows. *Practical constraint:* interactive-only, no headless/scale use, draws the shared pool.

**Cowork** — agentic task-completion for knowledge work (distinct from Claude Code's dev focus): give it an objective, it works across files/connected tools unattended, delivers a reviewable result. Research preview 2026-01-12 → GA ~April 2026 → **expanded to web + mobile (beta) 2026-07-07, Max subscribers first.** Included standard on both Max tiers. **Explicitly consumes the shared usage pool faster than chat** per Anthropic's own guidance — this is the single fastest way to burn your weekly budget among all Claude surfaces. Real-world usage skews toward general business ops (33.4%) over software dev (<9%) per Anthropic's own July 2026 disclosure.

**Skills / MCP / connectors** — Agent Skills: feature preview on claude.ai (Pro/Max/Team/Enterprise, requires code execution enabled), beta in Claude Code/API. MCP: remote connectors on Pro/Max/Team/Enterprise; local MCP via Desktop config works on any plan. No Max-20x-specific cap found beyond the shared usage pool — these are enablers, not separately metered resources. *Practical constraint:* labeled "feature preview," so behavior can change without notice.

**Scheduled tasks / cloud agents** — three distinct mechanisms:
1. **Cowork Scheduled Tasks** (2026-04-09, all paid plans, beta): hourly/daily/weekly/weekdays/manual triggers, runs remotely even with your device asleep.
2. **Claude Code Routines** (research preview, Pro/Max/Team/Enterprise, requires Claude Code on web): scheduled/API/GitHub-event triggers, **1-hour minimum interval** (hard published floor), account-specific daily run-count cap (visible in-app, not published as a fixed number), GitHub webhook triggers subject to hourly caps. One-off single-fire runs are exempt from the daily routine-run-count cap (still consume regular usage). Runs on Anthropic-managed cloud infra — survives your machine being off.
3. **`/loop`** (local, session-scoped): max 50 scheduled tasks/session, 7-day auto-expiry, dies with the session unless resumed.
4. **Desktop scheduled tasks**: local-machine-only, 1-minute minimum interval, needs local files + machine on.

*Practical constraint:* Routines is explicitly "research preview... may change," and all four mechanisms still draw the same shared subscription pool — there's no separate automation allowance baked into the $200/month beyond the plan's normal limits.

**Claude Agent SDK entitlements** — the murkiest area found in this research. The **official Quickstart/Overview docs** tell third-party developers to use **API-key auth** (separate, metered, pay-as-you-go at standard rates) — no claude.ai/Max-login path is documented as supported. A **separate** support article describes a subscription-credit mechanism that was supposed to launch 2026-06-15 but is now marked **"paused"** on the live page. **Bottom line: budget for separate API billing for Agent SDK work — do not assume Max 20x's $200/month covers it**, pending Anthropic re-confirming otherwise.

**Computer use** — research preview, **Pro/Max only** (not Team/Enterprise). Available **only** via the Claude Desktop app (macOS + Windows) or the Claude Code CLI (**macOS only** — no Linux/Windows CLI path), **never plain claude.ai web chat**. Requires direct account login (not Bedrock/Vertex/Foundry). Tool-selection precedence: MCP server → Bash → Claude in Chrome → computer use (last resort). **Holds a machine-wide lock from first action until session exit — only one computer-use session at a time per machine**, and it's **not available in headless (`-p`) mode**. *Practical constraint:* fine for supervised one-off desktop-GUI tasks, unusable for parallelized or background automation.

---

## THE TOOLING MATRIX

| Vertical | Primary | Secondary | Honest gap (not covered by either) | Cheapest quality external option |
|---|---|---|---|---|
| **(a) Photo/image art** | Google — Nano Banana Pro (2K/4K, editing, character consistency, Flow/Gemini app) | Claude — Cowork/Chrome for batch renaming, metadata, prompt engineering, QA (no native image gen) | Print-grade upscale beyond 4K, RAW/color-managed photo editing, guaranteed commercial-print licensing chain | Adobe Firefly (already in your Adobe subscription per your stack) for commercial-safe gen; Topaz Gigapixel ($99 one-time) for print upscale |
| **(b) Short-form video/reels** | Google — Flow (Veo 3.1 / Gemini Omni), native 9:16 + audio | Claude — Cowork/Routines for caption copy, batch pipeline, post-scheduling | Native auto-caption/subtitle burn-in, multi-track timeline trims | CapCut (free/$10mo) for caption burn + quick edit |
| **(c) Web-series/long-form AI video** | Google — Flow Extend chains + Gemini Notebook Cinematic Video Overviews for structure | Claude — scriptwriting, continuity/shot-list tracking, orchestration across episodes | Long-form multi-scene character/world consistency at scale, real color grading/finishing | DaVinci Resolve (free) for assembly/grade; ElevenLabs ($5-22/mo) if Google TTS voice consistency proves insufficient |
| **(d) Music** | Google — Flow Music (Lyria 3.5), full songs, 30,000 credits/mo | none (Claude has no native audio generation) | DAW mixing/mastering, stem separation, confirmed monetization/Content ID clearance | BandLab (free) or Logic Pro ($200 one-time, Mac) for mix/master; DistroKid (~$20/yr) once monetization terms are verified |
| **(e) Podcasts** | Google — Gemini Notebook Audio Overviews (100-200/day, 4 formats, 80+ languages) | Claude — show notes, transcript cleanup, SEO descriptions, Routines-based publish scheduling | Brand-consistent/selectable host voice, post-generation editing, confirmed export quality | ElevenLabs ($5-22/mo) for branded voice narration; Descript ($12-24/mo) for actual cut/mix |
| **(f) Games/apps (vibe-coded)** | Claude — Claude Code (Max 20x) for architecture, implementation, debugging, judgment | Google — Jules Ultra (300 tasks/day, 60 concurrent) as async overflow, or Antigravity IDE, or Project Genie for interactive-world prototyping | App-store deployment/signing automation, dedicated 3D/sprite asset pipeline | itch.io (free hosting), Godot/Unity (free engines), Kenney.nl (free placeholder art) |
| **(g) Writing/newsletter** | Claude — Max 20x chat/Cowork for drafting, editing, long-context synthesis | Google — Deep Research (compute-based quota) + Canvas for source-grounded reports and quick web publishing | Built-in delivery/ESP, dedicated SEO keyword research | Beehiiv or Substack (free tier) for delivery; Claude for drafting |

---

## WORKLOAD ROUTING

**Route to Claude (Max 20x):** anything that needs judgment, multi-step orchestration, code, or brand-voice consistency — Claude Code for all coding/vibe-coding, Cowork/Routines as the glue that ties Google's generation output into your publish pipeline (renaming, QA, scheduling, cross-posting), script/story structuring, editing and rewriting, review passes, and any MCP-driven automation linking tools together. This is also where your existing `tangent-social-media` pipeline (ideate/script/critique/produce/publish skills) should keep living — it's agentic/orchestration work, Claude's strength.

**Route to Google AI Ultra:** anything generation-heavy — video (Flow/Veo), image (Nano Banana Pro), music (Flow Music/Lyria), podcast audio drafts (Gemini Notebook), and raw research gathering via Deep Research. These are the jobs where Google's per-tier credit/quota pools are large enough that a solo creator is very unlikely to bottleneck.

**Why this split maximizes both subscriptions without hitting caps:** Google's generation quotas (video/image/music/podcast) are sized for creator-scale bulk output and reset monthly; Claude's constraint is the **shared, weekly-capped** pool across chat+Code+Cowork, which is the tighter and more unpredictable budget of the two. Keeping Claude focused on judgment/orchestration (fewer, higher-value turns) and Google focused on bulk generation (cheap-per-unit, high headroom) avoids starving either.

### Realistic per-week production volume (with arithmetic, Ultra $199.99 + Max 20x)

**Short-form video/reels (Flow, Veo 3.1 Fast, Ultra rate):**
- 1 reel ≈ 3 clips × 8s (Fast tier, 10 credits/clip) = 30 credits/reel.
- Monthly budget: 25,000 credits ÷ 30 = **~833 reels/month theoretically possible on credits alone** → far beyond any solo creator's editing/curation throughput. **Credits are not the constraint for reels — your own time to select/caption/post is.**
- A realistic cadence (5-10 reels/week = ~20-40 clips = 200-400 credits/week) uses **under 2% of the weekly credit allowance.**

**Long-form/web-series video (Flow, Veo 3.1 Quality, chained Extend):**
- A 3-minute (180s) episode assembled from ~23 chained 8s Quality segments × 100 credits = **~2,300 credits/episode**.
- 25,000 credits/mo ÷ 2,300 ≈ **10.8 episodes/month ≈ ~2.5 episodes/week** at full Quality-tier, fully-chained production. **This is the one Google-side quota that can actually bind** if you commit to a weekly high-quality long-form episode — mixing in Fast-tier segments for non-hero shots stretches this considerably.

**Music (Flow Music, Lyria 3.5):**
- 30,000 credits/mo ÷ (implied ~5 credits/song from the ~6,000 songs/mo estimate) ≈ **~1,385 songs/week theoretical ceiling** — not a real-world constraint at any plausible solo-creator volume.

**Podcasts (Gemini Notebook Audio Overviews):**
- 200/day (top Ultra tier) × 7 = **1,400/week ceiling** vs. a realistic 1-3 episodes/week need. **Not a constraint**; the real limits are voice-brand-consistency and lack of post-edit control (see gap above), not quota.

**Claude Code / Cowork / orchestration (Max 20x):**
- No official absolute numbers exist; using the unofficial estimate (~220k tokens/5-hr window, ~240-480 Sonnet-hours/week, ~24-40 Opus/Fable-hours/week, medium confidence), a solo creator can sustain **several hours/day of active Claude Code + Cowork use**, but the **Sonnet-specific weekly sub-cap and the Fable-5 50%-of-weekly-limit cap** are the binding walls if you run heavy agentic sessions daily. Practical rule of thumb: default routine/bulk work (renaming, QA passes, scheduling, trend sweeps) to Sonnet-tier usage; reserve Opus/Fable-tier turns for architecture decisions, brand-voice judgment calls, and final review — this keeps the smaller, contested Fable-5 allowance from being exhausted on mechanical work.

---

## Sources index (primary official sources used)

- Google: gemini.google/subscriptions, one.google.com/about/google-ai-plans, blog.google (I/O 2026 wrap-up, Ultra subscriptions post, Nano Banana Pro, Lyria 3/3.5, Flow updates, Gemini Notebook rebrand, Gemini Spark posts), support.google.com (Flow models/credits/extend, Google One Ultra benefits, Gemini Notebook limits/audio/video overviews, Gemini plan comparison), ai.google.dev (Imagen, video, speech-generation docs), deepmind.google (SynthID, Gemini models, Deep Think, Music AI Sandbox), jules.google, antigravity.google/blog.
- Anthropic: support.claude.com (Max plan, usage limits, Claude Code, Claude in Chrome, Agent SDK, Fable 5, extra usage), code.claude.com/docs (overview, Chrome, Routines, Agent SDK quickstart/overview), claude.com/cowork, Anthropic newsroom (Sonnet 5, Opus 5 release dates).
- Secondary press used only to fill official-source gaps (dates, numeric estimates): 9to5Google, TechCrunch, SiliconANGLE, 9to5Mac, IntuitionLabs, alphasignal.ai, various — all flagged inline as medium/low confidence where used.
