# ops/revenue/ — The Revenue Office's Working Files

Owner: revenue-lead (`.claude/agents/revenue-lead.md`). Strategy lives in
`strategy/REVENUE.md`; this folder holds the working records that strategy governs.

## What lives here

- **Opportunity briefs** — `YYYY-MM-<slug>.md`, one product idea per file, format per
  `strategy/REVENUE.md` §3 (the product · audience evidence · effort-vs-margin · trust test ·
  distribution plan · pricing hypothesis · pre-registered kill gate · verdict). Created by
  revenue-lead whenever a product idea earns a real look; GO decisions are Sparsh's only.
- **Monthly reviews** — `review-YYYY-MM.md`, written by `/revenue-review` from
  `templates/revenue-review.md`. The decisions log inside each review is the audit trail for
  every `strategy/REVENUE.md` §2 change.
- **Launch plans and product postmortems** — attached to their opportunity brief's slug
  (`YYYY-MM-<slug>-launch.md`, `YYYY-MM-<slug>-postmortem.md`) once a product goes GO /
  is killed.
- **Later, on activation only** (never speculatively — a premature media kit is a named
  failure mode, `revenue-lead.md`):
  - **Media kit + rate card** — created when the sponsorship threshold in
    `strategy/REVENUE.md` §2 is crossed and signed off at `/revenue-review`. Verified
    `[OWN-DATA]` numbers only.
  - **Deal tracker and product tracker** — Google Sheets, following the candidates-Sheet
    pattern (`strategy/CANDIDATES.md`): tracking of record lives in the Sheet; this folder
    keeps a pointer file per tracker (`tracker-<name>.md`) holding the Sheet URL + fileId,
    the status vocabulary, and the read/write convention — agents read via the Drive MCP
    (`read_file_content`, by fileId); edits are made by Sparsh in the Sheet UI or by the
    Showrunner via Claude-in-Chrome during `/revenue-review`; if neither is available, the
    pending update is logged in the next monthly review. Sheets are created on first need,
    not in advance.

## Conventions

- Every number in every file here carries a source per `knowledge/SOURCES.md` (dashboard
  pull, weekly report, `[MONEY]`/whitelisted citation, or `[OWN-DATA]`) — or is written
  UNKNOWN with a logged research gap.
- Nothing in this folder changes `strategy/REVENUE.md` §2 by itself — that happens only
  inside `/revenue-review`, with Sparsh + Showrunner sign-off.
- Money decisions (spend, pricing, deals) are Sparsh's alone (`ops/ROLES.md` (g)) — files
  here record and propose; they never authorize.
