---
name: cold-read
description: A light sanity check before a post reaches Sparsh. Two context-free cold-reader agents (persona A everyday viewer, persona B tech-curious) read the post once, the way a viewer would, and say it back. It catches posts that strangers don't get. It is not a line-by-line polish pass. Runs once per item (on the copy in the pipeline, on the rendered post or the copy for ad-hoc pieces). Writes critiques/cold-read-<phase>.md ending in COLD-READ: PASS or FAIL.
---

## Purpose
Catch the big failure: a post a stranger doesn't get, wouldn't stop on, or feels lectured by.
That was the deleted Panditji carousel. A cold reader given its slides would not stop on
slide 1, couldn't follow it, and would have left by slide 4, which matched the verdict of
Sparsh's wife, a first-time reader.

**This is a sanity check, not a polish gate.** Readers always flag something. The question
is whether a stranger understood the post and would keep going, not whether every phrase was
effortless. Don't chase small wording snags round after round. That overfits to two AI
readers and sands the voice down. (Learned 2026-11-15: three rounds spent chasing snags on a
post that both readers understood and would share. Sparsh called it overfitting.)

## Inputs
- The artifact, in one of two forms:
  - the copy file (`carousel.md` or `script.md` beat blocks), or
  - the rendered slides or 5-8 video frames, plus the caption.

  Use the render if one exists. Otherwise use the copy.
- The one-line message and the primary audience, from `brief.md` or the Message Brief. **The
  readers never see these.** Only the judging step uses them.
- The item or production folder.

## Protocol
1. **Build the cold packet.** Write `critiques/cold-read-packet-<phase>.md` with only what a
   viewer would see, in order:
   - each slide's `H:` and `B:` lines (and `S:` labelled "Spoken:");
   - the `V:` line as "[Picture: ...]";
   - then the caption.

   For a render, the packet is the ordered image paths plus the caption. Leave out the
   message, the audience and any notes.
2. **Dispatch two `cold-reader` agents in parallel** (subagent_type `cold-reader`, model
   sonnet), one for persona A and one for persona B. Give each only the packet, its persona
   letter and its output path (`critiques/cold-read-<phase>-A.md` / `-B.md`). If the subagent
   type is unavailable, use a general-purpose sonnet agent told to read
   `.claude/agents/cold-reader.md` first.
3. **Judge.** The post PASSES when, for the audience the brief targets:
   - **Got it:** each reader's RESTATED sentence carries the same core point as the one-line
     message. The wording can differ; the point can't be missing or wrong.
   - **Would stop and keep going:** the reader would stop on the cover and didn't bail out
     partway.
   - **No real misunderstanding:** nothing on the cover or in a headline was misread or left
     the reader with no idea. Phrases they had to think about but worked out are fine.
     List them as optional polish.

   Audience rule: for A or A+B, both readers must pass. For B only, B must pass and A must at
   least say correctly what the post is about.

   Voice: if a reader says it felt like a presentation, a lecture or an ad, note the line
   they quote as a suggested fix. That is feedback for the author, not a fail on its own.
4. **Write `critiques/cold-read-<phase>.md`.** Include:
   - both RESTATED lines next to the one-line message;
   - the verdict, with a sentence of reasoning;
   - at most 3 suggested fixes, only for things that would matter to a real viewer.

   The last line is exactly `COLD-READ: PASS` or `COLD-READ: FAIL`. `tools/pipeline.py`
   checks it at G1.
5. **On FAIL:** fix the real problem (the message didn't land, or the cover or a headline was
   misread), then do ONE more read with fresh readers. If it still fails, show Sparsh the
   reports and let him decide. Never grind out rounds on small snags.

## Rules
- Never coach the readers or tell them the topic.
- Optional polish stays optional. The author or Sparsh may take it or leave it.
- In INTERACTIVE mode, show Sparsh the two RESTATED lines next to the one-line message. That
  is the quickest way to see whether the post lands.

## Outputs
- `critiques/cold-read-<phase>-A.md`, `-B.md`: the raw reader reports.
- `critiques/cold-read-<phase>.md`: the verdict, ending `COLD-READ: PASS|FAIL`.
