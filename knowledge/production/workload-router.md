# Workload Router — Claude vs. Google AI Ultra

Load-bearing for the producer's tool-selection calls across every vertical, and for any
capacity/scheduling decision the planner or Showrunner makes (SYSTEM_DESIGN_V2_PROPOSAL.md
principle 9, §4.6 item 6). Source: the subscription-inventory research brief, compiled
2026-08-02 — cited below as `[SUBS]` = `research/briefs/revamp-2026-08/subscription_inventory.md`.
That brief's own confidence tiers (**High** = confirmed on a live official page, recent and
consistent; **Medium** = official but ambiguous/single-sourced or press-confirmed only;
**Low/Unconfirmed** = flagged gap, treat as a guess) are preserved verbatim below rather than
converted to another scheme — do not upgrade a Medium/Low figure to High by repetition.

**Both vendors change these numbers often** — Google restructured the entire Ultra lineup at
I/O 2026 (2026-05-19); Anthropic has flip-flopped on Agent SDK billing at least once in 2026.
Section 4 below is not optional reading.

## 1. Routing doctrine — job type → subscription, and why

| Job type | Route | Why |
|---|---|---|
| Judgment, multi-step orchestration, code, brand-voice consistency | **Claude (Max 20x)** | Claude Code for all coding/vibe-coding; Cowork/Routines as the glue tying Google's generation output into the publish pipeline (renaming, QA, scheduling, cross-posting); script/story structuring, editing/rewriting, review passes, MCP-driven automation. The `tangent-social-media` pipeline itself (ideate/script/critique/produce/publish) lives here — it's agentic/orchestration work, Claude's strength `[SUBS §WORKLOAD ROUTING]`. |
| Generation-heavy: video, image, music, podcast-draft audio, raw research gathering | **Google AI Ultra** | Per-tier credit/quota pools are sized for creator-scale bulk output and reset monthly — a solo creator is very unlikely to bottleneck on them `[SUBS §WORKLOAD ROUTING]`. |

**Why this split maximizes both subscriptions without hitting caps:** Google's generation
quotas (video/image/music/podcast) have high headroom and are cheap per unit; Claude's
constraint is the **shared, weekly-capped** pool across chat + Code + Cowork, which is the
tighter and more unpredictable budget of the two. Keeping Claude focused on judgment/
orchestration (fewer, higher-value turns) and Google focused on bulk generation avoids
starving either `[SUBS §WORKLOAD ROUTING]`.

## 2. Tooling matrix per vertical (condensed from `[SUBS §THE TOOLING MATRIX]`)

| Vertical | Primary | Secondary | Honest gap | Cheapest external option |
|---|---|---|---|---|
| (a) Photo/image art | Google — Nano Banana Pro (2K/4K, editing, character consistency) | Claude — Cowork/Chrome for batch renaming, metadata, QA (no native image gen) | Print-grade upscale beyond 4K; guaranteed commercial-print licensing chain | Adobe Firefly (already in-stack) for commercial-safe gen; Topaz Gigapixel for print upscale |
| (b) Short-form video/reels | Google — Flow (Veo 3.1 / Gemini Omni), native 9:16 + audio | Claude — Cowork/Routines for caption copy, batch pipeline, post-scheduling | Native auto-caption/subtitle burn-in, multi-track timeline trims | CapCut for caption burn + quick edit |
| (c) Web-series/long-form AI video | Google — Flow Extend chains + Gemini Notebook Cinematic Video Overviews | Claude — scriptwriting, continuity/shot-list tracking, orchestration | Long-form multi-scene character/world consistency at scale; real color grading | DaVinci Resolve for assembly/grade; ElevenLabs if Google TTS voice consistency proves insufficient |
| (d) Music | Google — Flow Music (Lyria 3.5), full songs | none (Claude has no native audio generation) | DAW mixing/mastering, stem separation, confirmed monetization/Content ID clearance | BandLab or Logic Pro for mix/master; DistroKid once monetization terms are verified |
| (e) Podcasts | Google — Gemini Notebook Audio Overviews (4 formats) | Claude — show notes, transcript cleanup, SEO descriptions, publish scheduling | Brand-consistent/selectable host voice; post-generation editing | ElevenLabs for branded narration; Descript for actual cut/mix |
| (f) Games/apps (vibe-coded) | Claude — Claude Code (Max 20x): architecture, implementation, debugging | Google — Jules Ultra as async overflow, or Antigravity IDE, or Project Genie for world prototyping | App-store deployment/signing automation; dedicated 3D/sprite asset pipeline | itch.io hosting; Godot/Unity engines; Kenney.nl placeholder art |
| (g) Writing/newsletter | Claude — Max 20x chat/Cowork for drafting, editing, long-context synthesis | Google — Deep Research + Canvas for source-grounded reports | Built-in delivery/ESP; dedicated SEO keyword research | Beehiiv or Substack for delivery |

## 3. The three binding caps (as-of 2026-08-02 — verify live before relying)

1. **Claude weekly caps (Max 20x).** Two weekly limits — all-models and Sonnet-specific — plus
   Claude Fable 5 capped at **up to 50% of the weekly usage limit** on that model specifically
   (High confidence, support.claude.com `[SUBS §7]`). No official absolute token number is
   published; an unofficial estimate puts Max 20x around ~220k tokens/5-hr window, ~240-480
   Sonnet-hours/week, ~24-40 Opus/Fable-tier-hours/week (Medium confidence, IntuitionLabs via
   `[SUBS §7]`) — treat as ballpark, not contract. **Binding because every surface — claude.ai
   web/mobile/desktop, Claude Code, Cowork, Chrome extension — draws the SAME pool**; running
   several concurrently is the fastest way to exhaust it.
2. **Flow Quality-tier credits — ~2.5 episodes/week ceiling.** A 3-minute episode chained from
   ~23 Veo 3.1 Quality segments (100 credits/8s segment, official per-credit costs, High
   confidence) costs ~2,300 credits; 25,000 credits/mo ÷ 2,300 ≈ 10.8 episodes/month ≈ **~2.5
   episodes/week** at full Quality-tier, fully-chained production (`[SUBS]`, arithmetic on
   official figures). This is the one Google-side quota that can actually bind if a weekly
   high-quality long-form episode is committed to; mixing in Fast-tier segments for non-hero
   shots stretches it considerably.
3. **Computer-use single-machine lock.** Claude's computer-use (Pro/Max only; Claude Desktop
   macOS+Windows, or Claude Code CLI macOS-only) **holds a machine-wide lock from first action
   until session exit — only one computer-use session at a time per machine**, and it is not
   available in headless (`-p`) mode (High confidence, `[SUBS §8]`). Not a volume cap — an
   exclusivity constraint that rules out parallel or background computer-use automation.

## 4. Re-verification protocol

`[SUBS]`'s own header rule, restated as a checklist — this file inherits it:

1. Check this file's as-of date (§3 above) against today's date. If it's more than ~30 days
   stale, treat every number below as provisional, not planning-grade.
2. Before a purchase decision or a hard production commitment, re-check the live source page
   cited in `[SUBS]`'s Sources index for the specific number in question — do not cite this
   file's numbers as the source of record; it is a snapshot.
3. Anything tagged **Medium**, **Low**, or **Unconfirmed** in `[SUBS]` must be independently
   re-verified in-account (Google AI subscription settings; Anthropic Settings > Usage) before
   it enters a roadmap commitment. Never plan production volume off an Unconfirmed number.
4. A correction gets logged back into this file (or a dated addendum), never silently applied —
   retraction discipline per `knowledge/INDEX.md` ("a corrected claim is marked CORRECTED/
   RETRACTED in place, never silently deleted").

## 5. Per-week production-volume guidance

- **Reels:** a realistic 5-10 reels/week (~20-40 clips) uses under 2% of Flow's monthly credit
  allowance — credits are not the constraint; Sparsh's own select/caption/post time is (High
  confidence on the credit math, `[SUBS]`).
- **Long-form/web-series:** ~2.5 episodes/week hard ceiling at full Quality-tier chained
  production (binding cap #2 above) — mixing in Fast-tier non-hero segments stretches this.
- **Music:** a ~1,385 songs/week theoretical ceiling from the 30,000-credit/mo pool — not a
  real-world constraint at any plausible solo-creator volume (Medium confidence on the official
  credit figure, Low/Medium on the songs-per-month conversion, `[SUBS §3]`).
- **Podcasts:** a 1,400/week ceiling (200/day × 7, top Ultra tier) vs. a realistic 1-3
  episodes/week need — not a constraint. The real limits are voice-brand-consistency and lack
  of post-edit control, not quota (High confidence on the quota, gap on the qualitative limits,
  `[SUBS §4]`).
- **Claude Code / Cowork / orchestration:** no official absolute numbers exist (gap, `[SUBS
  §7]`). Rule of thumb: default routine/bulk work (renaming, QA passes, scheduling, trend
  sweeps) to Sonnet-tier usage; reserve Opus/Fable-tier turns for architecture decisions,
  brand-voice judgment calls, and final review — this protects the smaller, contested Fable-5
  allowance from being exhausted on mechanical work.

## 6. Open gaps carried forward from `[SUBS]` — do not silently resolve these

- Flow Extend chain-length/count: no official numeric cap found (`[SUBS §1]`).
- Flow video commercial-licensing/monetization terms beyond "Google won't claim ownership":
  unconfirmed (`[SUBS §1]`).
- Flow Music monetization/Content ID clearance terms: unconfirmed (`[SUBS §3]`).
- Gemini Deep Research: the old fixed-quota numbers are stale; the replacement compute-based
  system publishes no absolute figure (`[SUBS §5]`).
- Claude Agent SDK billing: a separate-credit-pool migration was announced then marked "paused"
  on the live docs — this has flipped once already in 2026, verify same-day before relying on
  it (`[SUBS §8]`).

Owner: brand-director/producer jointly maintain this file's currency; re-verified at the
quarterly stale-claim sweep (`ops/RUNBOOK.md` §7) at minimum, and immediately before any
production commitment that leans on §3's caps.
