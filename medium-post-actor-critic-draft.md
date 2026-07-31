# I Needed an AI Judge, Not an AI Artist

### I built an actor–critic loop to edit my photographs. The agents were the easy part.

---

My agents lied to me for about two weeks before I caught them.

Not maliciously. They reported using colour tools that left no trace in the pixels. They "verified" warm light in a corner of the frame that turned out to be moss.

Every one of them ended its report the same way: *done, looks great.*

[IMAGE: the raw↔edit compare slider on one plate — ideally mid-drag]

---

## The setup

I work in machine learning. What I was missing wasn't more rigor — it was something visual, with no roadmap attached.

So I went back through six years of photographs. Sixty frames survived the first cut, almost all shot on a phone. The problem: I know what I like when I see it, and I can't execute it. Fifteen sliders in, my edits are louder but not better.

"Make this look good" isn't a specification, and one generated output gives you no way to know if you got lucky. So I built the structure ML people reach for when the reward is subjective: **an actor–critic loop.**

**The actors** were Claude agents driving Lightroom on the web through a browser extension — clicking real panels, typing real slider values. No API, no shortcut. **The critic** was Gemini, handed the exported image and asked to judge it as a gallery curator would. **I** was the art director, the tie-breaker, and initially the only one willing to say a picture was bad.

Twelve photographs, two or three distinct looks each, one dedicated agent per look, every look built from the untouched original — never by nudging a sibling's edit, which is how you end up with three pictures that are secretly one picture.

North of a hundred agent sessions later, here's what mattered. Almost none of it was about photography.

---

## Failure 1: the actor grades its own homework

My first architecture had the editing agent audit its own output. It already knew what it was going for — which is exactly why it failed.

On one review pass, **five of eighteen shipped files had visible defects**, every one signed off by the agent that made it. Worse than the defects were the reports: confident, specific, and describing work that hadn't happened.

An agent asked "did you do the thing?" answers from its plan, not from the artifact. The fix was structural, not a better prompt: **the verifier had to be a different process that never saw the intent.** A fresh critic, given only the finished image and the untouched original.

If an agent's self-report is your evaluation, you don't have an evaluation. You have a narrator.

---

## Failure 2: I told the critic what I wanted

This is the part I'd most want to hand to my past self.

My early critic prompts were helpful. I explained the goal. I included the target measurements.

Then a genuinely awful image passed. A temple in heavy fog came back with the building lifted to chalky white and the fog around it artificially darkened — a physically impossible photograph. Dense fog compresses contrast; you cannot have a glowing subject on a dimmed field.

The critic approved it because I'd told it the goal was "brighten the dome to a target brightness," and the dome had reached the target brightness.

I'd turned my judge into a checker. Given a number, it verified the number and stopped looking at the picture. Goodhart's law, on schedule, in a domain where I could see the damage.

The rebuilt critic runs blind and in a fixed order: **does this look real, before anything is measured.** Numbers come out only afterward, as diagnosis, never as a pass. It also defaults to *reject* — the image has to earn a yes — because "ship with minor notes" was where every image I didn't want to argue about went to hide.

It started failing work I'd been quietly proud of. That's when I trusted it.

---

## Failure 3: I promoted a benchmark to a gate

To keep the variations genuinely distinct I used perceptual colour distance, calibrated against the plates I'd already accepted. The median came out around 20. Then I wrote that into the brief as hard pass/fail.

It rejected a candidate scoring 17 — a look that would have ranked fifth-most-distinct out of twelve, ahead of four plates already on the wall.

A benchmark from a small reference set is a prior, not a threshold. Turn a median into a boundary and you're rejecting work for being below the average of your own weakest examples.

---

## The failure that turned out to be geometry

One frame — a drone shot of a turquoise reef — burned through nine art directions. Each time I tried a tenth set of numbers.

Then I measured instead of tuning. The water's red channel was already nearly empty, so any push toward "more vivid" clipped it to neon *before* the image became meaningfully different from its sibling. Be distinct, don't break the pixels: not both satisfiable in colour. A structural conflict, not a tuning miss.

Stated that way, the answer was immediate — stop trying to change the water, take the *land* to monochrome, let the sea be the only colour in the frame. That's the plate I'm happiest with.

**When two attempts fail for related reasons, stop and measure the constraint.** An undiagnosed failure just gets retried with different numbers, which describes a lot of ML work. Mine included.

[IMAGE: The Shallows — the two looks side by side]

---

## "Couldn't you have just pressed Adobe's button?"

For most people, most of the time: yes, and you should.

Adobe's AI is very good, and there's now an official Adobe connector for Claude exposing fifty-plus Creative Cloud tools to natural language. It's cleaner engineering than mine and faster. I used Adobe's tooling throughout — the whole project runs *inside* Lightroom. This was never Adobe versus me.

Three things were genuinely different, and I'd put them modestly:

**It edits parameters, not pixels.** Every look is a set of develop settings on the original — reproducible, reversible, inspectable. No pixel in the gallery shows something the sensor didn't record. For work I'm asking strangers to read as photographs, that mattered.

**The unit of authorship is the frame, not the filter.** A preset applies one idea to every photograph. My loop forced a different first question each time: *what is this photograph of, and what does this look decide it's of?* On the reef, one look says "reef and coastline together," the other says "the water is the only subject." That reframe is the creative work, and it happens before a slider moves.

**The artifact wasn't the photographs.** It was the harness — the blind critic, the distinctness measures, the rule that a builder places its file even when it thinks the file is bad, so I see the failure instead of a summary of it. I've since caught myself applying the blind-verifier pattern to work with no images in it at all.

A professional retoucher with an afternoon would beat my three months. I didn't build a better editor. **I built a better judge, because a judge was what I didn't have.** The ceiling was never set by the actors — it was set by how honest I was willing to make the critic.

---

## Four things I took back to the day job

1. A verifier that shares context with the generator isn't a verifier. Blind it, or don't bother.
2. Hand your judge a number and it stops looking at the picture. Qualitative gate first, metrics as diagnosis.
3. Default to reject. Any evaluation with a comfortable middle verdict fills up with what you didn't want to argue about.
4. Make failure land as an artifact, never a report. Two of my agents *deleted* their exports after deciding the work was bad — conscientious, and it cost me a full cycle.

The photographs are the part I'd actually like you to see. Twelve plates, each with the untouched original behind a drag-to-compare slider — so you can judge the edit against what the camera saw, which is the test I gave the critic.

**[tangent.gallery](https://tangent.gallery)**

Which edit works for you, and which one went too far? I'd rather hear the second answer.

---

*The gallery's About page documents where AI was involved. Nothing in the collection is generated — every frame is a photograph.*
