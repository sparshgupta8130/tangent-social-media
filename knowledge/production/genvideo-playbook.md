# Gen-Video Playbook — Veo/Flow B-Roll + TTS

Load before scripting or producing any `[GEN]`-tagged asset. Source: July-2026 production-stack
research brief (`[stack-brief]` = `research/briefs/production_stack_2026-07.md`, tiered `[HIGH]`/`[MED]`/`[LOW]`/`[UNVERIFIED]`). Disclosure
rules cross-reference `knowledge/audience/positioning.md` and `knowledge/platform/youtube.md` §8.

## 1. What's included — Veo 3.1 via Gemini AI Ultra

**Access/cost**: Google AI Ultra = **$249.99/mo**, includes **25,000 monthly AI credits** (vs.
AI Pro $19.99/mo for 1,000); non-subscribers get 50 free Flow credits/day [MED —
pricing context carried from 2025, reported still current 2026]. Credit-to-second conversion for
Ultra's monthly pool is **[UNVERIFIED]** — confirm on the live Flow billing page before planning
monthly volume.

**Veo 3.1 capabilities** [HIGH unless noted]:
- **Native synchronized audio** — dialogue with lip-sync, ambient sound, generated in the same
  pass, 48kHz, no separate audio pipeline.
- **Image-to-video ("Ingredients to Video")**: accepts **up to 3 reference images** for
  character/style consistency; **native 9:16 vertical generation** — a direct fit for our
  Shorts/Reels canvas.
- **Clip length**: base generation **8 seconds**; **Scene Extension** chains/extends up to
  **~60 seconds** total [MED/HIGH]. Native resolution 1080p, optional 4K upscale post-pass.
- Credit cost scales with duration; exact per-second cost table not found — **[UNVERIFIED]**,
  verify before budgeting a month's b-roll volume.

## 2. What we use it for — b-roll only

**Atmosphere shots, transitions, abstract visuals** — establishing shots of a workspace mood,
abstract light/texture transitions between segments, ambient loops behind a VO passage. This is
the disclosure-labeled, clearly-supplementary layer of a cut, never the subject the cut is about.

## 3. What we NEVER use it for — this is constitutional, not a style preference

**Never for the photographs themselves.** The craft claim — "an engineer taught an AI taste,
using his camera, his code" (`STRATEGY.md` §2) — is the entire brand. If the photographs
Lightroom is shown editing were themselves AI-generated rather than Sparsh's own raws, the brand
is fraudulent at its foundation, not just non-compliant. **Never to fake a screen recording,
never to fake a result, never to present generated video as our photography or as our pipeline's
actual output.** This is the single hardest line in the whole knowledge bank — genvideo output is
decoration around real work, never a stand-in for it. Any script that proposes using gen-video to
*simulate* an editing session, a UI interaction, or a result the pipeline didn't actually produce
is an automatic critique-lens-8 FAIL and should be killed at G1, not fixed.

## 4. Prompt patterns for our aesthetic

Target: **calm, gallery-grade, natural light** — matches the tangent.gallery quality anchor
(`STRATEGY.md` §1). Prompt construction pattern: [subject/setting] + [natural light quality —
"soft window light," "golden-hour," "overcast diffuse"] + [camera behavior — "slow push-in,"
"static locked-off," "gentle handheld drift," never whip-pans or frenetic motion] + [mood word —
"contemplative," "unhurried," "quiet"] + explicit negative framing against stock-footage clichés
(no lens flares, no corporate-stock gloss, no oversaturated color grade). Keep clips short (one
idea per generated shot, matching the craft file's one-idea rule) — a single generated shot
should read as one atmospheric beat, not a scene needing its own internal edit.

## 5. Disclosure — SynthID and the enforcement risk

**SynthID is invisible but detected.** Google embeds SynthID in effectively all Google-generated
image/video/audio by 2026; it survives re-encoding and minor edits at ~95-99% detectability
[HIGH]. **YouTube**: since **January 2026**, YouTube auto-labels AI-altered/synthetic content via
its own SynthID-aware + classifier detection, independent of creator disclosure. First
non-disclosure violation = warning + education; **second violation = 90-day monetization
suspension** [HIGH — `stack-brief` §4; see `knowledge/platform/youtube.md` §8 for the full
policy]. **Instagram/Meta**: detects C2PA content-credentials and auto-labels "AI generated" even
without creator disclosure — currently "detect & label," not a hard ban [MED].

**Practical takeaway**: undisclosed Veo/Flow b-roll is *likely to be auto-labeled anyway*, so
self-disclosure is strictly cheaper than the alternative — it costs nothing (YouTube's own
statement: voluntary disclosure doesn't hurt reach/monetization) and hedges against the
auto-detection framing the omission as concealment.

## 6. Disclosure integration — how it actually triggers

Any `[GEN]` asset present in a cut requires the disclosure line per
`knowledge/audience/positioning.md` — **stated on-screen and in the caption**, not buried
(`CLAUDE.md` non-negotiable #2). Mechanically: the story-lead tags every generative asset
`[GEN]` in `assets.md` at script time; that tag is what the producer checks against when filling
`publish.md`'s disclosure-line field, and it's what the critic checks at G2 lens 8 (hygiene/
compliance — binary, blocks SHIP if missing). The tag is the trigger — an untagged `[GEN]` asset
slipping into a cut is a process failure to catch at G2, not a judgment call to make at publish
time.

## 7. TTS options

- **Primary (if VO needed for a monetized/public post)**: **ElevenLabs Starter ~$5/mo** —
  30,000 credits (~30 min), the **first tier with a commercial license**, the practical minimum
  for monetized YouTube/IG content [MED — figures approximate, confirm on elevenlabs.io before
  committing budget].
- **Free fallback for drafts**: **Edge-TTS** (`edge-tts` Python package) — 200 voices, 50
  languages, no per-character cap, free; quality rated below ElevenLabs/Gemini for expressiveness
  but fine for internal draft review before a final VO pass [MED].
- **Adjacent options, not yet load-bearing**: Google Cloud TTS free tier (4M chars/mo Standard/
  WaveNet, 1M chars/mo Neural2/Studio/Chirp 3: HD) as a zero-cost fallback if Edge-TTS quality
  isn't sufficient [MED]; whether Gemini Ultra's shared 25,000-credit pool covers Gemini-TTS
  generation at usable volume, or bills separately, is **[UNVERIFIED]** — confirm in the Google
  Cloud/AI Studio billing console before planning around it.

**Cloned-voice disclosure rule**: YouTube's Jan-2026 policy carves out **cloning your own voice**
as not requiring disclosure; cloning **someone else's voice does**, and additionally requires
that person's consent [HIGH]. Generic TTS narration (no real person's identity cloned) is
lower-risk but still evaluated against exact platform wording at upload time — when in doubt,
disclose. Instagram has no narration-specific rule beyond the general AI-content-credentials
auto-labeling behavior in §5 [MED].
