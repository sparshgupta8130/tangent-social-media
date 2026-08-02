# Adobe Playbook — Driving the Editing Pipeline

Load before any `/produce` session that captures a Lightroom edit. Source: the July-2026
production-stack research brief (`[stack-brief]` = `research/briefs/production_stack_2026-07.md`, tiered `[HIGH]`/`[MED]`/`[LOW]`/`[UNVERIFIED]`).
This is the flagship-format engine — BET-3's entire premise depends on the capture being genuine
and the session protocol below being followed exactly.

## (a) The Claude-in-Chrome + Lightroom Web path — our core path

**What lightroom.adobe.com exposes, mid-2026** [stack-brief §2]:
- **Masking**: subject/sky-style auto-detection plus newly added auto-detect for **mountains,
  water, vegetation, architecture**; Quick Actions let you zoom in and retouch **individual
  people** with per-person settings [HIGH].
- **Point curve**: real tonal-curve control, previously desktop/Classic-only [HIGH].
- **Color Mixer**: gained a "Color" mode + Color dropdown, closer to desktop HSL parity [HIGH].
- **Presets**: sync via Adobe ID across desktop/mobile/web, but community reports say presets
  (recommended/premium/own) don't reliably show up on web even when they work on mobile —
  **[MED/LOW], verify in-account before scripting a session around a specific preset being
  present.**
- **Versions/snapshots**: web supports Edit Versions (non-destructive alternates); full
  snapshot-panel parity with Classic is **[UNVERIFIED]** — confirm live, don't assume.
- **Export ceiling**: Lightroom Web's "JPEG – Full Size" tops out around **4620×3080px @300dpi**
  (~2MB), limited customization vs. Classic's export dialog; Adobe itself recommends desktop/
  mobile for print-grade exports [MED]. **Non-issue for our 1080×1920 vertical target** — the
  export resolution is far above what a reel needs; the actual bottleneck is screen-capture
  resolution (`assembly-playbook.md` §1), not Lightroom's export.

**Session protocol** — how a producer session structures an edit for content, in order:
1. **Brief** — read `brief.md` + `script.md`: target emotion, the specific before/after the
   script promises, which masks/tools the script calls out as on-camera beats.
2. **Global adjustments** — exposure/white balance/point-curve pass, narrated as it happens (this
   is a rewatch-worthy beat per `knowledge/craft/` if it's dramatic).
3. **Local masks** — subject/sky/architecture auto-masks, applied one at a time, each visibly
   distinct so a viewer can follow cause→effect.
4. **Critic loop** — pause for a self-check against the brief's target look before finalizing;
   if a critic pass (G2) rejects the cut later, the rejection text itself is capture-worthy
   (see below) — don't edit it out of the session record even if reshooting.
5. **Export** — JPEG Full Size, verify it cleared the resolution/crop needed for the reel's
   reframe plan before ending capture.

**What to capture for content — the moments that read on camera**: sliders moving (not static
before/after, the drag itself); masks drawing themselves (the auto-detect overlay rendering in
real time); before/after toggles (the comparison view snap); the critic's rejection text
verbatim on-screen if a fix round happens — this is proof-of-process, not a blooper, and belongs
in the cut per `STRATEGY.md` §2's "prove, don't assert" doctrine. These are the shots the
producer must flag to the assembly pass (`assembly-playbook.md`) as must-keep segments, not
b-roll to be trimmed for pacing.

## (b) The official "Adobe for creativity" Claude connector

Launched globally **April 28, 2026** — an MCP-based custom connector bringing **50+ pro-grade
tools** across Photoshop, Illustrator, Firefly, Express, Premiere, Lightroom, InDesign, Adobe
Stock into Claude's chat interface [HIGH — Adobe blog, PetaPixel]. ~40 tools usable guest/no
Adobe account; Adobe ID sign-in unlocks more tools/limits/persistent saved work. **Requires a
paid Claude plan** (our Max plan qualifies) [MED]. Capabilities: multi-step natural-language
orchestration — portrait retouching, social-graphic text/color edits, and **video resizing/
reformatting for Shorts/Reels**. **Depth caveat**: despite "Creative Cloud" branding, functional
depth is reported roughly **Adobe Express-level, not full desktop-app depth** — it will not
replace hands-on Lightroom develop-module work for anything beyond templated edits [MED]. Also
purely reactive/prompted — no file-arrival triggers.

**When to use which path**: the connector is right for quick thumbnail/social-graphic
touch-ups, batch resizes, and light Premiere timeline ops (asset binning, marker addition) where
the *editing itself* isn't the content. The **browser path (a) is the core path** whenever the
Lightroom UI *is* the footage — i.e., every flagship demo-in-motion reel. June 2026's broader
"Creative Agent" expansion (Premiere/Photoshop/Illustrator/InDesign/Frame.io beta, After Effects
private beta) is noted for awareness but not yet load-bearing to our pipeline [HIGH — Adobe
Newsroom].

## (c) Photoshop API v2 / Firefly Services note

**Lightroom API is fully deprecated, End-of-Life 2026-07-31** — do not build new automation
against it; it consolidates into **Photoshop API v2** [HIGH — Adobe deprecation notice]. Photoshop
API v2 (GA) is a unified batch/production imaging surface (linked smart objects, ICC-aware
output) — useful for **back-office batch processing** (e.g., bulk export variants), not for
producing the on-camera "watch Claude edit" footage, since it has no equivalent to the visible
develop-module UI. Photoshop 2026 desktop separately gained non-destructive Lightroom-style
curves-based color grading, meaning the "develop module feel" is migrating into Photoshop rather
than being newly exposed via a clean Lightroom-equivalent REST API [HIGH].

## (d) Honest capability boundaries — what's out of scope or [SPARSH]

- **Full masking/curves/Color-Mixer panel control via a stable, scriptable API does not exist.**
  The Lightroom Classic SDK (Lua) exposes `LrDevelopController` for Quick-Develop-level ops (Auto
  Tone, White Balance, basic Radial/Spot/Graduated filter creation) but not the full panel set,
  and has known edge-case bugs (ICC profile keys ignored on export) [MED]. This means any edit
  requiring Classic-only tooling (e.g., certain print-color-management workflows) is out of
  scope for the automated pipeline — flag it `[SPARSH]` if a script calls for it, per the
  story-lead's minimize-`[SPARSH]` mandate.
- **Raw photographs are always `[SPARSH]`** — Sparsh's camera, his raws. Nothing in this
  playbook substitutes for that; the playbook only covers how the *editing process* is captured
  and driven.
- **Preset availability and Edit Versions/snapshot parity are both unconfirmed on web** — verify
  live in the account before a script depends on either; don't assume desktop-parity features
  exist in the browser session just because Adobe's changelog implies it.
