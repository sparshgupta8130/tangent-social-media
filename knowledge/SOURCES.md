# SOURCES — The System-Wide Trusted-Source Whitelist

**Owner:** shared — this file governs both teams (`SYSTEM_DESIGN.md` §12.2). The Studio's
existing evidence tiers (`knowledge/INDEX.md` provenance legend: `[RESEARCH-BACKED]` /
`[INDUSTRY DATA]` / `[PRACTITIONER LORE]` / `[CORPUS: file]` / `[OWN-DATA]` /
`[UNVERIFIED STAT]`) govern claims sourced from the 18-dossier research corpus. The
Brand Office's tags (`[CANON: author/institute, year]` / `[VERIFIED-ONLINE: url, date]` /
`[REPO: file]` / `[EXTRAPOLATION]` / `[CONTESTED]`, `SYSTEM_DESIGN.md` §12.5) govern claims
sourced from the wider marketing-science/creator-economy literature. This file is what
makes a `[VERIFIED-ONLINE: ...]` or `[CANON: ...]` citation legitimate: the source it
points to must sit in Tier T1 or T2 below, or the tag is misapplied.

**Load context:** read before writing any citation in any brief, memo, critique, verdict,
or knowledge-file entry — either team, any skill. Read in full at the quarterly SOURCES.md
whitelist refresh (`ops/RUNBOOK.md` §9 / `SYSTEM_DESIGN.md` §12.6).

## Tier T1 — cite freely

Findings from these sources may be tagged `[CANON: ...]` or `[VERIFIED-ONLINE: url, date]`
without a confidence qualifier:

- **Peer-reviewed academic journals** — *Journal of Marketing Research*, *Journal of
  Advertising Research*, *Marketing Science*, *Journal of Marketing*, *Journal of
  Personality and Social Psychology*, and equivalent peer-reviewed venues. (Examples
  already load-bearing in this build: Berger & Milkman 2012 in *JMR*; Zajonc 1968.)
- **Ehrenberg-Bass Institute for Marketing Science** — its own publications
  (marketingscience.info) and the books its research staff author (Sharp, Romaniuk).
- **Official platform sources** — Meta/Instagram's own blog and Help Center
  (about.instagram.com, help.instagram.com, developers.facebook.com), YouTube's official
  blog and Creator Insider channel, transparency.meta.com.
- **Pew Research Center** — pewresearch.org, for demographic/usage survey data.
- **Stanford HAI** (Human-Centered AI Institute) — for AI-adoption/impact research.
- **Official company newsrooms** — Adobe, Anthropic, Google's own press/blog channels, for
  first-party product/policy statements (not third-party coverage of them — that's T2).
- **Government/regulatory sources** — FTC disclosure guidance (ftc.gov) and equivalent
  official regulatory guidance relevant to AI-content disclosure or creator-economy
  compliance.

## Tier T2 — cite with `[MED]` confidence

Usable, but every citation carries an explicit confidence qualifier (`[MED]` or the
Studio's `[INDUSTRY DATA]`/`[PRACTITIONER LORE]` tags as appropriate) rather than being
presented as settled fact:

- **Named-methodology industry research** — Kantar, System1, Nielsen, the IPA (Binet &
  Field's own published work), LinkedIn's B2B Institute — usable when the specific study/
  report is named and its methodology is stated, not just "a study found."
- **Major tech press with editorial standards** — TechCrunch, The Verge, Variety,
  PetaPixel — for reported events (e.g. the backlash-map flashpoints in
  `audience/positioning.md`), not for uncredited statistics.
- **Named creator-economy analysts with disclosed data** — vidIQ's own published studies,
  Wistia's own hosted-analytics data (already cited, `research/03_virality_science.md`
  §2.6.2), SocialInsider, and equivalent vendors publishing their own first-party dataset
  analysis with a stated methodology.
- **The books canon, attributed** — Sharp, Romaniuk, Keller, Aaker, Berger, Ries & Trout,
  Binet & Field — cite the specific book/paper and year; a claim attributed to "marketing
  science says" with no named author/year does not qualify, even if the underlying idea
  traces to one of these authors.

## Tier T3 — direction only, never numbers

Convergent practitioner consensus — multiple independent sources agreeing on a *direction*
without a traceable primary study. Must be labeled `[PRACTITIONER LORE]` (Studio) or
explicitly flagged as directional-only (Brand Office) every time it's used. Never supplies a
number, a percentage, or a threshold used as a scoring bar — only a qualitative "this
tends to matter" signal. Example already in this build: the mere-directional claim that
sends/shares outweigh likes for cold reach on Instagram is T3-sourced (convergent secondary
reporting on Mosseri's public statements, no single citable transcript) even though the
*direction* is credible — see `platform/instagram.md` §1's own handling of exactly this
case as the template.

## DISQUALIFIED — never cite

- SEO content-farm blogs and uncited "marketing tips" listicles.
- AI-generated aggregator sites (no identifiable human author or named methodology).
- Any "study" or statistic that cannot be traced to a named methodology, named
  institution, or named author — this is the same standard `research/03_virality_science.md`
  already applies throughout (its own worked examples of disqualified claims: "open loops
  increase ADV by 40–60%," "-8 to -15% for a 3-second logo," "35% lost in first 10 seconds
  never recovers by 5:00" — all specific-sounding numbers with no traceable source, logged
  `[UNVERIFIED STAT]` rather than used). Treat any new specific-sounding number that fails
  the same traceability test the same way.
- Self-reported marketing copy used to sell a product/course, presented as an independent
  finding (e.g. a creator's own claimed follower-total or revenue figure on their own sales
  page) — usable only as a self-reported claim, explicitly labeled as such, never as a
  verified number. [REPO: research/00_seed_accounts.md already demonstrates this exact
  distinction — Sebastien Jefferies's self-reported "1.9M+ followers" is logged as
  self-reported/LOW confidence, not asserted as fact.]

## The zero-hallucination procedural rule (verbatim, `SYSTEM_DESIGN.md` §12.5)

> Every factual claim in any brief, memo, critique, verdict, or knowledge write must carry
> one of: (a) a knowledge-bank citation (file + section), (b) a live citation to a
> `knowledge/SOURCES.md`-whitelisted source (URL + date fetched), or (c) an explicit
> `[OWN-DATA]` reference to our verified metrics. A claim with none of these is written as
> **UNKNOWN** with a logged research gap — never estimated, never "probably." Numbers are
> never invented, interpolated, or recalled from memory without a source.
> `knowledge/SOURCES.md` defines the whitelist tiers and the disqualified-source list; the
> weekly review audits a sample of the week's citations.

This rule is constitutional for both teams, not a Brand Office-specific add-on — the Studio's
`[UNVERIFIED STAT]` discipline in `research/03_virality_science.md` and
`knowledge/INDEX.md`'s provenance legend already implement its spirit; this file makes the
whitelist that decides which sources actually qualify for tags (b) and makes it explicit
that the rule binds the Brand Office's own outputs (BTS notes, consult memos, G3 verdicts)
exactly as it binds Studio briefs and critiques.

## Logging a research gap

When a claim would be load-bearing but no T1/T2 source and no repo file supports it: write
it inline as `UNKNOWN — research gap: <the specific question>` at the point it would have
appeared, rather than omitting it silently or writing a plausible-sounding placeholder.
Example form: `UNKNOWN — research gap: does YT Analytics segment retention support a
new-vs-returning-viewer split for Shorts` (the live example already logged in
`brand-health-metrics.md` §1). Every research gap logged in a given week gets a one-line
note in that week's `/weekly-review` output — not necessarily resolved that week, but never
silently dropped; a gap that recurs across multiple weeks without resolution is itself a
signal the Showrunner should surface to Sparsh (a genuine capability gap in the stack, not
just a documentation gap).

## Weekly citation-audit sampling rule

At every `/weekly-review`, sample a small set of the week's citations (across both teams'
outputs — briefs, critiques, consult memos, G3 verdicts) and verify: (1) the tag matches
the source's actual tier per this file, (2) the URL/file citation actually resolves and
actually says what it's cited for, (3) no number appears without one of the three carriers
named in the procedural rule above. A sample is deliberate, not exhaustive — the audit
exists to catch systematic drift (a source being casually upgraded from T2 to "cite
freely" over time, or a `[CANON]` tag creeping onto an extrapolated claim) rather than to
re-verify every citation every week. Findings that reveal a *pattern* (not a one-off typo)
get logged as a knowledge-bank correction per the retraction discipline
(`knowledge/INDEX.md` — "a corrected claim is marked, not silently deleted") and, if
severe enough to indicate a tagging-discipline problem rather than a single error,
escalated to the Showrunner for a process fix, not just a content fix.
