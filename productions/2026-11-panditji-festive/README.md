# Panditji festive reels — Diwali + Gujarati New Year (Nov 2026)

Two Instagram reels for **@tangentideas.ai** (Diwali 9 s at 120 BPM; New Year 13.5 s at 80 BPM, slowed on Sparsh's note that 9 s felt too short; the title is "Happy New Year!" with the Gujarati greeting below, not "Saal Mubarak", on his note that it is Urdu-leaning rather than the usual Gujarati/Hindi wish), made on 2026-11-09 at Sparsh's request:

| File | Post on | What happens |
|---|---|---|
| `out/panditji-diwali-reel.mp4` | Diwali, 9 Nov 2026 (today) | Night. A diya catches, Panditji pops up behind it, gasps, does namaste. On the drop the row of diyas lights up one by one, a marigold toran drops in, and he cheers: **Happy Diwali! / शुभ दीपावली**. Fireworks either side, a wave, then namaste to sign off. |
| `out/panditji-newyear-reel.mp4` | Bestu Varas, 10 Nov 2026 (tomorrow) | Dawn. A *Vikram Samvat* counter reads **2082**; Panditji does the maths (hand on chin) while the last digit spins round to **2083**. It lands on the drop: confetti, a rangoli blooms behind him, **Happy New Year! / Wishing you a prosperous year / નૂતન વર્ષાભિનંદન**, garba hops, a wave, namaste. |

Cover frames (Diwali at 4.2 s, New Year at 6.3 s): `out/panditji-diwali-cover.jpg`, `out/panditji-newyear-cover.jpg`.

Both: 1080×1920, 30 fps, H.264 + AAC, loudness normalised to about −14 LUFS (measured −14.9 / −13.7 LUFS integrated, peaks about −4 dBFS). On-screen sign-off: "with love, Panditji" and
"@tangentideas.ai · animated with Claude" (the disclosure line, per CLAUDE.md non-negotiable 2).

**The year.** 10 Nov 2026 begins Gujarati (Kartikadi) **VS 2083**; Panditji's own engine says so
(`src/engine/panchang/calendar.ts` → `vikramKartikadi`: "VS 2082 began 2025-10-22"). The North-Indian (Chaitradi) year has
read 2083 since Chaitra (March 2026), which is the number the app's Today screen shows. The counter takes the year from
`newyear.html`'s `YEAR` constant (or `newyear.html?year=NNNN`); change it there and re-render if needed.

**Provenance.** Panditji is the app's own mascot, drawn from the same paths and colours as `panditji/src/ui/Panditji.tsx`
(male look, traditional style), split into parts in `lib.js` so he can blink, tilt and change pose. Everything else
(diyas, toran, fireworks, rangoli, counter) is drawn in code. The scores are original, synthesised from scratch in
`score.py` / `synth.py` (instrument code adapted from the Panditji launch reel), with no samples or licensed audio. Fonts:
Baloo 2 / Baloo Bhai 2 (Gujarati) and Nunito, all SIL Open Font License.

**Status:** made outside the pipeline (not registered with `tools/pipeline.py`, no G1/G2/G3 files): a time-boxed festive
greeting Sparsh asked for directly. Not posted.

## Captions (drafts)

**Diwali**

> Panditji lit the first diya so you don't have to. Happy Diwali! 🪔
> Animated and scored by Claude, entirely in code; I set the brief and picked the cut.
>
> May your home be full of light, laddoos and good company. ✨
>
> #Diwali #HappyDiwali #ShubhDeepavali #Panditji #MadeWithClaude

**New Year (Bestu Varas)**

> Panditji did the maths: Vikram Samvat 2082 → 2083. Nutan Varshabhinandan! 🎉
> Animated and scored by Claude, entirely in code; I set the brief and picked the cut.
>
> Happy New Year to everyone ringing in the Gujarati New Year today. Wishing you a happy, healthy and prosperous year ahead. 🪔
>
> #NutanVarshabhinandan #GujaratiNewYear #BestuVaras #HappyNewYear #Panditji

## Rebuild

`bash build.sh` (see the header for what it needs). Stills for checking: `node render.mjs diwali.html stills/ stills 2.2 3.3`.
Each page is a pure function of time: `window.render(t)` draws frame *t*, so any frame can be re-rendered on its own.
