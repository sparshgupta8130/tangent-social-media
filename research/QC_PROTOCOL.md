# QC Protocol — Social Launch Research Pipeline

Owner standard (verbatim intent): no lazy work anywhere in the pipeline. Every single analyzed
video gets a full post-mortem logged with thorough, accurate, copious notes. Work will be audited
by the owner. Dishonest or padded analysis poisons all downstream synthesis.

## Hard rules for every research agent

1. NO FABRICATION. Every number carries: source URL + as-of date + confidence (HIGH/MED/LOW).
   A stat without a source is deleted, not kept.
2. EVIDENCE TIERS. Every substantive claim is tagged [OBSERVED] / [REPORTED] / [INFERRED] per
   templates/video_postmortem_template.md. Inference dressed as observation = dossier voided.
3. DATA GAPS ARE LOGGED, NOT PAPERED OVER. "Could not obtain transcript; analysis based on
   title/caption/comments" is acceptable. Pretending to have watched something is not.
4. TEMPLATE COMPLIANCE. Every video post-mortem contains ALL nine sections of the template.
   A section that doesn't apply says why. No collapsed/merged sections.
5. MINIMUM DEPTH. A per-video post-mortem under ~40 substantive lines is presumptively lazy and
   gets rejected unless the data-gap log justifies it.
6. BOTH TAILS. Each creator dossier must analyze top performers AND 2-3 of the creator's WORST
   recent performers (the delta is where the signal is).
7. WORK SHOWN. Each dossier ends with a "Method log": what was searched, what was fetched, what
   failed (e.g., Instagram logged-out walls), so the audit can verify effort.

## Pipeline gates

- GATE A (post-discovery): orchestrator reviews rosters, verifies stat sourcing on a sample,
  selects deep-dive list.
- GATE B (post-dossier): orchestrator spot-audits every dossier — template compliance, evidence
  tags, source-link validity on sampled claims. FAIL → dossier re-dispatched with named defects.
  No dossier enters synthesis without passing.
- GATE C (pre-presentation): independent critic agent (fresh context, no stake in the work)
  audits the corpus for fabrication smells: numbers without sources, suspiciously uniform
  analyses, copy-paste psychology sections, missing worst-performer analyses.

## Known data-access constraints (honesty baseline)

- Instagram blocks most logged-out access. Reel-level exact stats often come from third-party
  aggregators or press — that's [REPORTED], MED confidence at best. Expected and acceptable.
- YouTube is public: watch pages, /shorts tab, transcripts where available → [OBSERVED] should
  dominate YT analyses. YT dossiers are held to a higher observation standard than IG ones.
- Where a creator cross-posts the same video to YT, use the YT copy to get transcript-level
  detail for the IG reel — log that this proxy was used.
- STANDING RULE (added post-Gate-C, 2026-07-25): the logged-in browser scrape's LIKE counts are
  unreliable (~45% of sampled reels wrong by 1.8x-453x; comments/dates reliable 22/22). ANY like
  count or like-rate backing a substantive claim (especially "near-zero engagement" / boost
  signatures) requires one independent yt-dlp pull against the public reel URL before it ships.
  Repeat-pulling the same tool does NOT count as verification — only a second independent method.
