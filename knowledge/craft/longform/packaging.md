# Long-Form Packaging — Title + Thumbnail Doctrine

Craft pack: `longform`. Load-bearing for `/script` (packaging drafted with the script, never
after the cut), `/produce` (thumbnail is a manifest asset), and G1/G2 lens 1 — packaging is
half of the longform HOOK score (`craft/longform/structure-and-retention.md`, lens
adaptations). Platform mechanics: `knowledge/platform/youtube.md` §3/§5 — cited, not
duplicated.

## The inversion — why this file exists at all

For Shorts, packaging is moot: ~99.9% of views come from the swipe feed and effort on a
thumbnail is misallocated (`platform/youtube.md` §3; research/03 §1.2.3 — the corpus's
established distinction [RESEARCH-BACKED]). **Long-form is the inverse: the view begins with
a deliberate choice from a grid, so the title+thumbnail unit carries the entire scroll-stop
burden the reel's frame 0 used to carry.** Everything `craft/reels/hooks.md` says about frame
0 — payoff legible unaided, no preamble, curiosity gap — transfers to the thumbnail, which is
frame 0 you can design after the fact.

## CTR mechanics — the honest numbers

- **The only whitelisted CTR benchmark:** "Half of all channels and videos on YouTube have an
  impressions CTR that can range between 2% and 10%"; new videos/channels and sub-100-view
  videos range wider [VERIFIED-ONLINE: support.google.com/youtube/answer/7628154
  "Impressions & click-through-rate FAQs," accessed 2026-08-02 — T1 official]. Any narrower
  "good CTR" figure circulating is vendor folklore — treat as [UNVERIFIED STAT].
- **CTR is surface-relative, never absolute** [same T1 source]: broad-reach surfaces (Home)
  naturally depress CTR; channel-page traffic inflates it. Never compare an episode's CTR
  against another video with a different surface mix — compare against our own median per
  surface once [OWN-DATA] exists.
- **CTR without retention is worthless, per the platform's own scoring:** YouTube's Test &
  compare declares a thumbnail "Winner" **based on watch time share, not raw clicks**
  [VERIFIED-ONLINE: support.google.com/youtube/answer/13861714, accessed 2026-08-02 — T1].
  YouTube's own title guidance states the interplay outright: "Be accurate. Make sure your
  title accurately represents the video. If not, viewers may stop watching, which can impact
  discoverability" [VERIFIED-ONLINE: support.google.com/youtube/answer/12340300 "Thumbnail &
  title tips," accessed 2026-08-02 — T1]. Clickbait is mechanically self-defeating on this
  platform, before it is a brand problem — the first-30s contract
  (`craft/longform/structure-and-retention.md`) is where the check gets cashed.

## Testing doctrine

Test & compare supports **up to three titles and thumbnails per video** (title testing added
2025-09-16; thumbnail testing used 15M+ times since 2023) and runs only on public long-form
and podcast episodes — consistent with packaging being a long-form-only lever
[VERIFIED-ONLINE: blog.youtube "New in YouTube Studio" (Made on YouTube 2025) +
support.google.com/youtube/answer/13861714, accessed 2026-08-02 — T1]. Policy: every HERO
long-form ships with 3 packaging variants prepared at script time (same discipline as the
reels pack's ≥3 hook variants), entered into Test & compare at publish; the "winner" result
is recorded in the item's postmortem as [OWN-DATA].

## Thumbnail rules — brand kit is binding

`brand/kit.yaml` `visual` + `frame_never_use` apply to thumbnails as to any frame:
- **The image is the richest color in the frame** — accent comes from the photograph/still
  itself, never a template gradient (kit `visual.palette.accent_rule`). For BET-4: the
  finished plate IS the thumbnail. For BET-5: one composed still that carries the episode's
  stakes — a face, a landscape, an object of the story.
- **Banned outright** (kit `frame_never_use`): meme fonts, red circle/arrow call-outs,
  shocked-face reactions, countdown-timer urgency, neon drop-shadows — the exact visual
  register of the AI-slop aesthetic the positioning is built against
  (`knowledge/brand/tangent-voice.md`).
- **Text: Fraunces, one load-bearing line maximum, or none** (kit `visual.type.rules`).
  YouTube's own guidance: readable text, restrained complexity, and "thumbnails show up
  differently across devices" — design at small size [T1: answer/12340300 above].
  Suggested-videos placements render small; if the line isn't legible at grid size, cut the
  line, not the image.
- The thumbnail must be a true frame or true still of the work — a thumbnail that promises
  an image the video never shows is a disclosure-adjacent integrity fail, scored at lens 8,
  not a style note (CLAUDE.md non-negotiable 2 spirit; the accuracy rule above).

## Title patterns — sell the story, not the AI

STRATEGY §2's law, adapted for narrative long-form: **pure-AI framing caps reach even when
per-viewer resonance is equal or higher** [CORPUS: pattern-library §3.14a — the Skill Leap
reach-ceiling finding]. The corpus's biggest long-form win sold the story, not the tool:
Curious Refuge's 4.4M-view piece is packaged as a director×franchise trailer premise, with
AI nowhere in the promise [CORPUS: pattern-library §1.3, §2.17]. Rule: **the title names the
story's stakes; the AI pipeline is the twist inside the video** (and the disclosure lives in
the description and on-screen — `craft/longform/series-doctrine.md`).

- Title classes (ranked by corpus long-form evidence, thin — flagged): story/stakes-first
  ("He held the ridge alone for four hours") > bold specific claim ("One raw file. Nine
  rejected grades.") > process-promise ("Start to finish" — BET-4's own frame). Ranking
  within long-form specifically is [PRACTITIONER LORE + corpus-adjacent] — the corpus's
  long-form n is small; log as research gap for [OWN-DATA].
- Front-load the load-bearing words; "viewers may only see part of your title" [T1:
  answer/12340300]. Searchable (descriptive) vs intriguing (curiosity) is an explicit
  either/or in YouTube's own guidance — pick per episode, don't hedge into mush.
- `brand/kit.yaml` `verbal.banned_words` applies to titles verbatim — a hype title fails
  the 35+ tone standard exactly as a hype caption does (`craft/reels/scripting-voice.md`).
- Never put "AI" in a PVC episode title. It reads as bravado framing against a martyr's
  story (`ops/council/consults/2026-08-01-pvc-ethics.md` Q3 trust-toxic form 4) AND caps
  reach [CORPUS §3.14a]. The craft-tribute disclosure does that work, in its place.

## Episode numbering and the browse-vs-suggested split

- Browse features (Home/subscriptions) and Suggested videos are distinct official traffic
  sources [VERIFIED-ONLINE: support.google.com/youtube/answer/9314355, accessed 2026-08-02 —
  T1]; a series playlist marks episodes as an official set and gets sibling episodes
  featured/recommended alongside the one being watched [T1: answer/6084043 — see
  `craft/longform/series-doctrine.md`].
- Numbering convention (extends `craft/reels/scripting-voice.md` series rules): number every
  episode plainly and consistently across platforms, never renumber a live series. **But the
  number sits at the title's tail ("— Ep 2"), never the head** — cold viewers on browse/
  suggested surfaces meet each episode as a standalone promise; leading with "Ep 7" tells a
  cold viewer they're late, and the story-stakes words lose the visible-title window
  [PRACTITIONER LORE for tail placement — no whitelisted study; consistent with the T1
  front-load-important-words guidance above. Log: research gap, test with [OWN-DATA]].
- Thumbnail numbering: small, consistent corner mark at most — the episode number is wrapper
  identity for returning viewers, not the sell for cold ones (series power =
  commitment-signaling, [CORPUS: pattern-library §2.3]).

## Anti-patterns

- **Packaging-first production** — building a video to justify a clickable thumbnail
  inverts the pipeline; the promise must be extracted from the strongest true material at
  script time, or the first-30s contract can't be honored.
- **AI-forward packaging** — "AI made this war film" class titles: reach-capped
  [CORPUS §3.14a] and trust-toxic for BET-5 (ethics memo Q3).
- **Uniform packaging across a season** — Curious Refuge's engagement rate declined across
  three reuses of the same packaging formula (2.08% → 1.94% → 0.82%) even as views held
  [CORPUS: pattern-library §2.17]; vary the promise per episode inside a consistent visual
  identity.
- **Judging packaging by CTR alone** — the platform itself doesn't (watch-time-share
  winner, T1 above); neither does lens 1.

UNKNOWN — research gaps: no T1/T2 evidence on thumbnail style-feature lifts (faces vs.
none, text vs. none — vendor claims all fail SOURCES.md traceability); no whitelisted
long-form title-class win-rate data (corpus n too small; build [OWN-DATA] via Test &
compare records).

## G1/G2 lens adaptations (longform)

- **Lens 1 — HOOK (×2):** packaging is scored *inside* this lens, as a pair with the first
  30 seconds: (a) does the title+thumbnail unit stop a cold grid-scroller unaided
  (the reels first-frame test, applied to the thumbnail); (b) does the cold open cash
  exactly that check? Score the weaker of the two — a mismatched pair is one broken promise,
  not two half-credits.
- **Lens 2 — STRUCTURE & RETENTION:** packaging accuracy is a structural input — the
  master loop the packaging opens must be the loop the loop-map closes (T1 accuracy rule
  above); a packaging promise absent from the loop map is a lens-2 deduction.
- **Lens 5 — CRAFT & AESTHETICS:** thumbnail held to the gallery bar — kit palette/type/
  frame_never_use compliance, small-size legibility, and the thumbnail-is-a-true-frame
  integrity check; a thumbnail that needed staging the video never shows escalates to
  lens 8.
