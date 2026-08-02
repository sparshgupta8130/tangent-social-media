# SYSTEM DESIGN V2 — "The Label"

**Status: APPROVED by Sparsh 2026-08-02 (structure + Phase R1; first-product decision
deferred to a dedicated session; campaign decisions queued post-build). Where this document
and `SYSTEM_DESIGN.md` (V1) disagree, THIS document wins; V1 remains the detailed reference
for everything V2 doesn't amend. Phase R1 delivered 2026-08-02. R2 delivered 2026-08-02 (repurposing engine + longform craft pack + Hedra vendor memo at research/briefs/hedra_eval_2026-08.md — verdict: no vendor, Flow-only; podcast/music/app packs deliberately deferred until their lanes activate). R3 half-delivered 2026-08-02 (ingest_stats.py built against documented formats — first-real-export reconciliation via `inspect` is mandatory before trust; publishing automation remains BLOCKED on accounts/handles/tokens that don't yet exist).** Evidence base: the four August-2026
research briefs at `research/briefs/revamp-2026-08/` (products teardown, architecture
patterns, monetization economics, subscription inventory) — cited below as [TEARDOWN],
[ARCH], [MONEY], [SUBS].

## 0. The goal, restated honestly

Sparsh is a solo AI-creative who wants to (a) spend his hours making art with AI — images,
web series, music, games, podcasts, apps — and (b) build "Tangent" into a brand that earns
serious money, with (c) a professional-grade brand manager running management and promotion.
The evidence says the goal is reachable only product-led: ads-only $1M/yr requires 4–28M
long-form views/month [MONEY §3]; every documented 7-figure creator mix is dominated by
owned products/sponsorships, not RPM [MONEY §2]. The system's job is to maximize the odds
on a 3–5-year product-led path while keeping the floor (audience + list + craft reputation)
compounding weekly.

## 1. Design principles (each carries its evidence)

1. **Artist-first.** Sparsh's calendar is for art. Every hour the system asks of him that
   isn't taste, approval, or performance is a design failure. (His stated constraint.)
2. **Single agent by default; fan out only for context isolation or true parallelism** —
   Anthropic's own production rule; role-play multiplication is how vendor systems fake
   depth [ARCH §1]. V2 grows the roster by exactly ONE agent.
3. **Deterministic spine, judgment at the joints.** Harden proven paths into code — the
   production case study moved 45% of executions to deterministic workflows and cut cost
   70% [ARCH §1]. Our `pipeline.py` spine stays; more plumbing joins it.
4. **Hard, un-blended gates** [ARCH §4]. G1/G2/G3 stand unchanged. One addition to the
   critic's checks: explicit narrative-originality/human-creative-input verification —
   YouTube's inauthentic-content policy targets templated mass-production, the exact drift
   an efficient AI pipeline invites [MONEY §4].
5. **Brand kit as code.** Machine-readable brand tokens (hard constraints) + prose (voice
   rationale), injected at every generation, validated deterministically — the one
   brand-voice mechanism with real evidence behind it; no serious vendor fine-tunes for
   text voice [ARCH §2]. Visual-asset injection is market table-stakes [TEARDOWN].
6. **Product-led revenue is a first-class office, not advice.** No current agent owns
   "turn audience into a paying product" — the single biggest structural gap the money
   goal exposes [MONEY design-implications §2].
7. **Visible human craft is the moat.** Audiences punish *perceived* over-automation
   (Duolingo lost 400K+ followers to perception alone [ARCH §5]); "machine craft, human
   taste" upgrades from positioning to survival strategy. Disclosure stays constitutional.
8. **Steal plumbing, not architecture.** The seven commercial products offer no
   architecture worth copying — their real assets are unglamorous integration debt:
   brand-asset injection, 1→N repurposing fan-out, scheduling [TEARDOWN]. We build thin
   versions of exactly those three; Hedra is a potential *vendor* (Character-3 avatar/
   lip-sync) for the web-series lane, not a rival.
9. **Route work to the subscription built for it.** Claude = judgment, orchestration,
   code, brand voice (its weekly caps are the binding budget). Google Ultra = generation
   volume (Flow/Veo video ~2.5 quality episodes/wk ceiling; Lyria 3.5 music effectively
   unlimited; Gemini Notebook audio 100–200/day; Nano Banana Pro images; Jules 300
   tasks/day for code grunt work) [SUBS]. The workload-router doctrine lives in
   `knowledge/production/workload-router.md`.
10. **Zero hallucination, unchanged and extended** — SOURCES.md governs V2's new files;
    subscription limits get as-of dates and live re-verification before any plan relies
    on them (several are volatile [SUBS]).

## 2. The reframe: an artist and his label

```
            SPARSH — the artist
   (makes the art; owns taste; three approvals: ship/money/face)
                     │
              THE SHOWRUNNER
        (live session: orchestrator, creative partner, final internal gate)
        ┌────────────┼───────────────┐
   THE STUDIO   THE BRAND OFFICE   OPERATIONS
   (create)     (manage·promote·   (plan·measure·scout)
                 monetize)
```

One pipeline, one knowledge bank, one constitution — three offices.

## 3. The roster (11 agents; changes marked)

### The Studio — creates, across all verticals
| Agent | Change | Mandate |
|---|---|---|
| `creative-director` | expanded | Concepts/briefs for ALL verticals (reels, series, music, podcast, games/apps content); selector generalizes per craft pack |
| `story-lead` | renamed from `scriptwriter` (historical name), expanded | Narrative architecture: reel scripts, episode arcs/screenplays, podcast outlines, devlog stories |
| `producer` | expanded | Tool operator across the [SUBS] matrix: Lightroom/ffmpeg (existing), Flow/Veo, Lyria, Gemini Notebook, Nano Banana, Hedra-as-vendor when approved; owns per-vertical production playbooks |
| `critic` | expanded | Same brutal gates; scorecard loads the item's CRAFT PACK (per-vertical lenses); new originality/human-input check (principle 4) |

### The Brand Office — the professional brand manager (upgraded from consulting bench)
| Agent | Change | Mandate |
|---|---|---|
| `brand-director` | renamed from `brand-strategist` (historical name), expanded | OWNS the brand: brand kit (code + prose), G3 chair, positioning across all verticals + surfaces, brand health, quarterly audit |
| `growth-lead` | renamed from `growth-scientist` (historical name), expanded | Owns PROMOTION, not just evidence: repurposing fan-out plans, cross-platform distribution calendar, funnel ops, discoverability; niche-CPM discipline (teach-the-workflow framing over raw entertainment — 5–10x sponsor economics [MONEY §4]) |
| `audience-advocate` | + community ops | Same trust mandate + comment/community engagement doctrine and execution oversight |
| `revenue-lead` | **NEW** | The missing owner [MONEY]: product pipeline (presets → courses → apps/SaaS), offer design + pricing, email-list P&L (KPI from item #1), sponsorship readiness (media kit, rate card, deal tracker), monetization sequencing against real thresholds |

### Operations — the shared spine
| Agent | Change | Mandate |
|---|---|---|
| `planner` | unchanged | Roadmaps, Plane, standups, accountability, `/plan campaign` |
| `analyst` | + ingestion | Verified stats, postmortems, benchmarks + semi-automated stats ingestion (`tools/ingest_stats.py`) |
| `trend-scout` | unchanged | Horizon sweeps, A1/A2/A3, now across all active verticals |

## 4. New infrastructure (the build items)

1. **`brand/kit.yaml` + `tools/brandkit_check.py`** — tokens: palette, type, logo/wordmark
   paths, watermark/credit rules, banned vocabulary, disclosure lines, caption footers,
   per-platform handles; every production skill injects it; the checker validates exports
   deterministically (colors/logo presence where required, banned-word scan on captions).
   Prose voice rationale stays in `knowledge/brand/tangent-voice.md` (they cross-reference).
2. **The repurposing engine** — `/repurpose` skill + `pipeline.py` child-item support:
   one hero asset fans out to platform-native derivatives (reel → Shorts variant, stills
   carousel, newsletter section, community post) as linked child items with their own
   hygiene checks; per-platform derivative checklists in `knowledge/platform/`.
   [TEARDOWN gap 2]
3. **Craft packs** — `knowledge/craft/` reorganized: `craft/reels/` (existing corpus-built
   doctrine moves here), then packs built ON LANE ACTIVATION, never speculatively:
   `craft/longform-video/`, `craft/podcast/`, `craft/music/`, `craft/games-apps/`. Each
   pack: craft doctrine + critic lens adaptations + production playbook + evidence sources.
   `item.yaml` gains a `vertical` field; the critic and producer load the matching pack.
4. **The revenue layer** — `strategy/REVENUE.md` (the money roadmap: scenario math from
   [MONEY §6], activation thresholds, product sequencing), `ops/revenue/` (offer briefs,
   media kit, deal + product trackers — Google Sheets, same pattern as candidates),
   `/revenue-review` monthly ritual (revenue-lead + Showrunner + Sparsh; the only place
   revenue strategy changes). Email capture wired into week-1 setup, tracked weekly.
5. **Publishing/analytics plumbing** — extend `knowledge/platform/publishing-ops.md` with
   the verified automation paths (Claude Routines/cloud scheduled tasks for cadence jobs;
   IG Graph publish for non-trend posts; YT API post-audit) and add `tools/ingest_stats.py`
   (parse platform CSV exports → posts.csv, second-source rule intact). [TEARDOWN gap 3]
6. **`knowledge/production/workload-router.md`** — the [SUBS] tooling matrix + routing
   doctrine + the three binding caps (Claude weekly caps; Flow quality-tier credits
   ~2.5 episodes/wk; computer-use single-machine lock) + re-verification protocol.

## 5. What does NOT change

The pipeline state machine and all four gates (G1/G2/G3/SHIP) · zero-hallucination +
SOURCES.md (extended, not weakened) · the reels knowledge bank (becomes `craft/reels/`
pack, contents intact) · Plane + candidates-Sheet workflow · the interactive session model ·
the PVC series plan (BET-5, its ethics doctrine, and the pending 6-week campaign — which
resumes immediately post-approval with two additions: email capture in W1 setup and
repurposing fan-outs on hero items).

## 6. The realism contract (posted where the team plans)

From [MONEY §6], 24-month probability read for a consistent solo creator: <$15K/yr
~50–60% · ~$100K/yr ~10–15% · $1M+/yr <2–3%. The documented 7-figure paths took 4–5 years
and are product-led. Therefore: the system optimizes (a) floor-raising (cadence + craft +
format ownership), (b) lottery exposure (volume + trend velocity + hero engineering),
(c) conversion of whatever hits (wrappers + funnel + email + products from day 1) — and
treats Sparsh's app-building skill as the highest-leverage revenue asset in the portfolio
(software products at 85–95% margin [MONEY §2/§4]; Jules + Claude Code as the production
line [SUBS]). No plan may assume the bull case; every plan must survive the base case.

## 7. Migration plan

- **Phase R1 (one session):** roster changes (rename/expand 6 agent files, write
  `revenue-lead`), `brand/kit.yaml` + checker, `strategy/REVENUE.md` + `/revenue-review`,
  constitution/RUNBOOK/ROLES/INDEX updates, craft-pack reorganization (move reels doctrine).
- **Phase R2 (as lanes activate):** `/repurpose` + child items; craft packs for web-series
  and podcast (the two nearest lanes); Hedra vendor evaluation for the PVC pipeline.
- **Phase R3 (when volume justifies):** publishing automation + stats ingestion tools;
  scheduled-task cadence jobs.

## 8. Decisions required from Sparsh

1. Approve the V2 structure (3 offices, 11 agents, revenue-lead added)?
2. Approve Phase R1 build now, campaign resuming in parallel right after?
3. First product bet for revenue-lead to develop (recommendation: preset/prompt pack first
   — fastest to ship off existing craft; an app/SaaS as the 6–12-month flagship, since
   that's where his skills + margins concentrate)?
4. The four campaign decisions from 2026-08-01 remain open (launch package, PVC
   architecture, PVC timing, raw-batch day + F2 IP) — answer together with this or after R1.
