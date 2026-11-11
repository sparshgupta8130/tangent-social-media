# Bhutan legends for Tangent Studios: handoff (2026-11-11)

The first session ran in the `tangent-sites` environment, which could not open any web page and
had no generation access. Work continues in a session on the "Default and Testing" environment
(unrestricted network, `GEMINI_API_KEY` environment variable). This file is the full state.

## The owner's brief (Sparsh)

- New Tangent area: **Tangent Studios**, at `studios.tangentideas.ai` (he wrote `.com`; he
  confirmed `.ai`). Build the site on the feature branch in `tangent-sites` **after episode 1
  exists** (use that repo's `add-tangent-site` skill). Nothing goes to `main` without his say.
- Series idea: short (about 5 minute) videos retelling the legends and history of places he
  travelled to in 2026: Puerto Rico (March), Alaska (June), Bhutan (November, he is there now),
  Cancun (December). **Start with Bhutan.**
- Publish on YouTube; promote on Instagram, YouTube Shorts and LinkedIn.
- End to end: research, story, screenplay, narration, visuals with consistent characters and
  locations, animation, score. Output wanted: finished, ready-to-post videos.
- Research must find the versions most accepted in Bhutan, with reference images of places,
  people, murals, and the elements of Bhutanese music. He invited pushback where his versions
  are wrong.
- Orchestration rule: the lead session plans, orchestrates and critically verifies; **every
  subagent must be Sonnet 5.5 (Agent tool `model: "sonnet"`), no other model.**
- His standing preference: be truthful and accurate, contradict him when he is wrong.

## His four Bhutan stories, as he wrote them (claims to test, several are likely wrong)

1. Padmasambhava ("Hindi name"): first Buddhist monk to migrate to Bhutan; one of three deities
   in most temples (with the Buddha of the Present and the Founder); flew in "Rudra form" to
   Tiger's Nest, subdued a demon, meditated in a cave, founded the monastery.
2. Three types of Buddha (past, present, future), each with its own posture and hand gesture.
3. The Founder: prince and heir of Tibet; uncle tried to assassinate him; fled; dreamed on the
   first night of a Thunder Dragon flying south; arrived in the 15th-16th century; united warring
   tribes into Bhutan, the Land of the Thunder Dragon.
4. The relic "from the 21st backbone of a great guru"; Tibetan armies came for it; he won without
   killing anyone by throwing a replica into the Pho Chhu or Mo Chhu; the real relic is in Punakha
   Dzong in a chamber only the King, the "Dharmaraja" and the caretaker may enter.

## Lead's pushback so far (from memory, UNVERIFIED: the research must confirm or overturn)

- Padmasambhava is Sanskrit; in Bhutan he is Guru Rinpoche. An 8th-century tantric master from
  Oddiyana who visited (first Bumthang, by tradition), not a migrant monk.
- The form at Taktsang is Dorje Drolo on a tigress; "Rudra" is probably a mishearing.
- He meditated in the cave; the temple was built in 1692 under Tenzin Rabgye.
- Buddhas of the three times (usually Dipankara, Shakyamuni, Maitreya): not "types", and shared
  across Buddhism.
- The Founder is Zhabdrung Ngawang Namgyal, hereditary prince-abbot of Ralung (Drukpa lineage),
  not heir of Tibet; his conflict was with the ruler of Tsang over a rival claimant to his
  incarnation title; no uncle known; arrived 1616.
- The vision is of a raven (Mahakala) flying south, not a dragon. "Druk" comes from Druk
  monastery in Tibet (Tsangpa Gyare).
- The relic is the Rangjung Kharsapani, a self-arisen Avalokiteshvara image from a vertebra of
  Tsangpa Gyare. "No one killed" is doubtful (several real invasions). The title is Je Khenpo.
  The relic and Zhabdrung's preserved body (Machen) are separate; check which chamber is
  restricted and to whom.
- Likely series shape: stories 3 and 4 are one life in two episodes; story 2 is an explainer.

## Decisions Sparsh has made

- **Visual style: "living scroll painting".** Original illustrations inspired by Bhutanese
  thangka and mural painting, brought to life with slow camera moves, parallax, drifting cloud,
  flame and water, plus a few fully animated hero shots. Chosen for consistency, cost, and the
  lower risk of distorting sacred figures.
- **Narration: AI narrator, disclosed** on screen and in the description; same voice across the
  series. His own voice is not to be used or cloned.
- **Generation route: Gemini API** (Nano Banana images, Veo for hero shots, Gemini voice, Lyria
  music). Pay-as-you-go. **Money is his approval point: show a cost estimate from live pricing
  and get his yes before any paid generation.**
- Site: as above.

## Research status: nothing verified yet

Files `01` to `05` in this folder are **blocked notes, not dossiers**: no page could be opened.
They hold only unverified search leads. Re-run all five briefs with web access:

1. `01_guru_rinpoche_taktsang.md`
2. `02_buddhas_of_three_times.md` (include the altar triad a visitor actually sees)
3. `03_zhabdrung_founding.md` (Treasury of Lives may have no full biography; lean on Karma
   Phuntsho and John Ardussi)
4. `04_relic_rangjung_kharsapani.md` (invasion years in the blocked note are unconfirmed)
5. `05_art_sound_sensitivity_pack.md` (painting style, architecture, dress, symbols, music and
   instruments, BICMA and other rules, etiquette for sacred imagery, at least 25 public-domain or
   Creative Commons study images with licences)

Each brief: test every one of Sparsh's claims (CORRECT / PARTLY / INCORRECT / CONTESTED); tag
statements `[TRADITION]` or `[HISTORY]`; prefer Bhutanese institutional and scholarly sources
(Department of Culture, Department of Tourism, Kuensel, BBS, Centre for Bhutan and GNH Studies,
UVA Mandala, Karma Phuntsho), then academic (Treasury of Lives, Ardussi, Aris, Himalayan Art
Resources, Rigpa Wiki), Wikipedia and blogs only as leads; URL and access date for every fact;
pages must be opened and read; UNKNOWN where unsourced; report disagreements; spellings and a
pronunciation guide; sensitivities; 5 to 8 memorable sourced details; overwrite the blocked file.
Tell agents to write a first draft early so a restart does not lose work.

## Rules that bind production

- This repo's `CLAUDE.md` constitution applies: own work only (reference images are for study,
  never reused), AI disclosure, no fabricated facts, critic gates, Sparsh approves SHIP, money
  and his face or voice. Open pipeline items with `tools/pipeline.py`.
- Sacred figures: stylised and painterly, never photoreal close-ups; check every frame for wrong
  hands, fingers or faces; wrathful forms are not "demons"; no public image of the relic exists
  to copy, so do not invent a close-up of it.
- Recommend a Bhutanese reader check each script before publish.

## Next steps, in order

1. Re-run the five research briefs; the lead cross-checks them against each other.
2. Present Sparsh the corrected story outlines and episode list. Wait for his nod.
3. Screenplays and narration, G1 critique.
4. Style tests (character and location sheets), then the cost estimate. Wait for his yes.
5. Produce episode 1, G2 and G3 gates, his SHIP approval. Then the Studios site and the
   promotion cut-downs.
