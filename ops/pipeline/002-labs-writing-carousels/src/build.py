"""Builds the three Labs Writing "key highlights" carousels (5 highlight slides + 1 follow slide each).

Every number on a slide is copied from the published post in tangent-sites/writing/<slug>.md.
Usage: python build.py   (writes <slug>.html next to this file; render with ../../001-.../carousel/src/render.js)
"""
from pathlib import Path

HERE = Path(__file__).parent
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;'
         '1,9..144,300..500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">')
LABS_ICON = ('<svg class="icon" viewBox="0 0 120 120" fill="none" aria-hidden="true">'
             '<rect x="28" y="44" width="64" height="50" rx="15" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
             '<line x1="60" y1="44" x2="60" y2="30" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
             '<circle cx="60" cy="24" r="4.045" fill="currentColor"/><circle cx="47" cy="67" r="4.045" fill="currentColor"/>'
             '<circle cx="73" cy="67" r="4.045" fill="currentColor"/></svg>')
YT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'
      '<path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/></svg>')
IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'
      '<rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>')
BOOK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M2 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H2z"/><path d="M22 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/></svg>')


def slide(n, kicker, body, sid):
    return (f'<section class="slide" id="s{sid}"><div class="top"><span class="k">{kicker}</span><span>{n} / 6</span></div>'
            f'<div class="main">{body}</div><div class="foot"><span>Tangent Labs · <b>Writing</b></span><span>{"Swipe →" if n == 1 else ""}</span></div></section>')


def follow(series):
    body = f'''{LABS_ICON}
<div class="h h2" style="margin-top:40px">Read the full post, and follow <em>for more.</em></div>
<div class="links">
  <div class="lnk">{BOOK}<div><span>The whole story, with the data</span><b>labs.tangentideas.ai/writing</b></div></div>
  <div class="lnk">{IG}<div><span>Follow on Instagram</span><b>@tangentideas.ai</b></div></div>
  <div class="lnk">{YT}<div><span>Subscribe on YouTube</span><b>youtube.com/@tangentideasai</b></div></div>
</div>'''
    return slide(6, series, body, 6)


def page(title, slides):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>{FONTS}'
            f'<link rel="stylesheet" href="blog.css"></head><body>\n' + '\n'.join(slides) + '\n</body></html>\n')


# ---------------------------------------------------------------- 1. deterministic-logic-first (Panditji)
S = 'Building Panditji'
p1 = [
    slide(1, S, '''
<div style="display:grid; grid-template-columns: 1fr 380px; gap: 30px; align-items:center; margin-top: 40px">
  <div class="h" style="font-size:80px">The AI kept moving Saturn. So I took the maths <em>away from it.</em></div>
  <img src="rings.png" style="width:380px; border-radius: 24px">
</div>
<p class="lede">Building an astrology guide that cannot guess: the key points from my post.</p>''', 1),
    slide(2, 'Why it guessed', '''
<div class="h h2">Two zodiacs, <em>24° apart.</em></div>
<p class="lede">Models learn from astrology text that mixes two systems. Asked from memory, a model blurred them: it put Saturn in one sign, then the next sign over, and invented a date that was off by months.</p>
<div class="stats" style="margin-top:40px">
  <div class="stat"><div class="v" style="color:var(--rose); font-size:60px">Western</div><div class="t">Counts the signs from the <b>spring equinox</b>.</div></div>
  <div class="stat"><div class="v" style="color:var(--sage); font-size:60px">Vedic</div><div class="t">Counts them from the <b>fixed stars</b>, about 24° further round.</div></div>
</div>''', 2),
    slide(3, 'The fix', '''
<div class="h h2">The phone does the maths. <em>The model only explains it.</em></div>
<div class="list">
  <div class="li"><div class="n">1</div><div>Every position, timing window and calendar lookup runs in <b>deterministic code on the phone</b>.</div></div>
  <div class="li"><div class="n">2</div><div>The model is told <b>“this is the only chart you know”</b>. It reads it through tools filtered by tradition, at most four steps a question.</div></div>
  <div class="li"><div class="n">3</div><div>Every answer carries <b>source badges</b> that open the exact numbers behind it.</div></div>
</div>''', 3),
    slide(4, 'The proof', '''
<div class="h h2">Checked against outside references, <em>not its own tests.</em></div>
<div class="stats">
  <div class="stat"><div class="v">1″</div><div class="t">Planet positions within <b>1 arcsecond</b> of NASA JPL and the Swiss Ephemeris.</div></div>
  <div class="stat"><div class="v">27<small> of 28</small></div><div class="t">Almanac transitions at the <b>exact printed minute</b>. The 28th within 6 seconds.</div></div>
  <div class="stat"><div class="v">11 <small>days</small></div><div class="t">The error an <b>AI-written commit</b> had added. A published almanac caught it.</div></div>
</div>''', 4),
    slide(5, 'Safety', '''
<div class="h h2">It also knows <em>what not to answer.</em></div>
<div class="stats" style="margin-top:36px">
  <div class="stat"><div class="v">427</div><div class="t">Red-team prompts in <b>English, Hinglish and Hindi</b>.</div></div>
  <div class="stat"><div class="v">100%</div><div class="t">Of <b>crisis messages</b> caught.</div></div>
  <div class="stat"><div class="v">0</div><div class="t">False blocks on <b>113 ordinary questions</b>.</div></div>
</div>
<div class="note">The lesson: when the input is physics, <b>compute every value before the model sees the prompt.</b></div>''', 5),
    follow(S),
]

# ---------------------------------------------------------------- 2. model-first-code-second (Pai-Pai)
S = 'Building Pai-Pai'
p2 = [
    slide(1, S, '''
<div class="h h1" style="font-size:82px">My hand-written parser beat the AI models, 88% to 66%. <em>Then I audited the test.</em></div>
<div class="chips"><span class="chip">kal</span><span class="chip">auto</span><span class="chip">180</span><span class="chip">me and रेवती</span></div>
<p class="lede" style="margin-top:30px">What an 18,000-sentence benchmark taught me about reading expense notes.</p>''', 1),
    slide(2, 'The leak', '''
<div class="h h2">The agents that built the parser <em>also wrote its test.</em></div>
<div class="list">
  <div class="li"><div class="n">1</div><div><b>65%</b> of the cases the rule fixes newly passed were in the held-out split.</div></div>
  <div class="li"><div class="n">2</div><div><b>78 of 80</b> easy test cases appeared word for word in the parser’s own unit tests.</div></div>
  <div class="li"><div class="n">3</div><div>Almost half the notes used the default split, and the median note was <b>five words</b> long.</div></div>
  <div class="li"><div class="n">4</div><div>Rules the parser knew were <b>missing from the models’ prompt</b>.</div></div>
</div>''', 2),
    slide(3, 'The rebuild', '''
<div class="h h2">Ground truth first. <em>Sentences second.</em></div>
<div class="flow">
  <div class="step"><div class="v">3,000</div><div class="t">Accounting scenarios, with every balance fixed <b>before a sentence existed</b>.</div></div>
  <div class="step"><div class="v">18,000</div><div class="t">Sentences written by <b>22 blind AI personas</b> that never saw the parser.</div></div>
  <div class="step"><div class="v">7,588</div><div class="t">Hidden test cases, double-labelled at <b>94.1% agreement</b>.</div></div>
</div>''', 3),
    slide(4, 'The flip', '''
<div class="h h2">On sentences it had never seen, <em>the order flipped.</em></div>
<div class="bars">
  <div class="bar"><div class="name"><span>Parser alone<small>12.2% silent errors</small></span><b>36.0%</b></div><div class="track"><span style="width:36%"></span></div></div>
  <div class="bar"><div class="name"><span>Best parser-first hybrid<small>10.6% silent</small></span><b>51.1%</b></div><div class="track"><span style="width:51.1%"></span></div></div>
  <div class="bar ship"><div class="name"><span>Model first, phone checks second<small>5.5% silent</small></span><b>84.4%</b></div><div class="track"><span style="width:84.4%"></span></div></div>
</div>
<p class="lede" style="font-size:24px; color:var(--muted); margin-top:34px">Right outcomes on 7,588 hidden cases: the right decision and every balance exact.</p>''', 4),
    slide(5, 'What I’m keeping', '''
<div class="h h2">Two rules <em>I’m keeping.</em></div>
<div class="list">
  <div class="li"><div class="n">1</div><div><b>Never let the agent that builds the solution write its test.</b> Generate the ground truth first, then the language.</div></div>
  <div class="li"><div class="n">2</div><div><b>Messy language, private data:</b> the model reads the sentence, and the phone checks it and does the sums. The model never sees your friends or balances.</div></div>
</div>''', 5),
    follow(S),
]

# ---------------------------------------------------------------- 3. single-fast-model-vs-ensemble (Pai-Pai)
p3 = [
    slide(1, S, '''
<div class="h h1" style="font-size:86px">One fast model beat a 3-model ensemble <em>at one-tenth the cost.</em></div>
<div class="stats" style="margin-top:44px">
  <div class="stat"><div class="v" style="font-size:66px">$0.44</div><div class="t">per 1,000 calls: <b>one model</b>, a better prompt.</div></div>
  <div class="stat"><div class="v" style="font-size:66px; color:var(--rose)">$4.44</div><div class="t">per 1,000 calls: <b>three models voting</b>.</div></div>
</div>''', 1),
    slide(2, 'Ensembles', '''
<div class="h h2">More models, <em>more hesitation.</em></div>
<div class="list">
  <div class="li"><div class="n">1</div><div>Three models voting got <b>78.1%</b> right, still behind one bigger model alone (<b>82.4%</b>).</div></div>
  <div class="li"><div class="n">2</div><div>Making two models agree cut silent errors to 1.9%, but it asked a question on <b>38% of clear notes</b>.</div></div>
  <div class="li"><div class="n">3</div><div>Models rated their own confidence <b>“high” on 97–100%</b> of replies, even when the money was wrong.</div></div>
</div>''', 2),
    slide(3, 'Experiments', '''
<div class="h h2">Every prompt change, <em>tested as an experiment.</em></div>
<div class="stats">
  <div class="stat"><div class="v" style="color:var(--rose)">−2.8</div><div class="t">Points from wrapping the <b>same words in XML tags</b>.</div></div>
  <div class="stat"><div class="v" style="color:var(--muted)">+0.8</div><div class="t">From a generic <b>“step by step”</b> checklist: noise.</div></div>
  <div class="stat"><div class="v">80.9%</div><div class="t">With <b>40 worked examples</b> and a headcount field, up from 74.3%.</div></div>
</div>''', 3),
    slide(4, 'The decision order', '''
<div class="h h2">Ask only when the answer <em>changes the money.</em></div>
<div class="list" style="gap:20px; margin-top:36px">
  <div class="li"><div class="n">1</div><div>Not an expense or a payment: <b>out of scope</b>.</div></div>
  <div class="li"><div class="n">2</div><div>The numbers contradict each other: <b>reject</b>.</div></div>
  <div class="li"><div class="n">3</div><div>Two readings give someone a different balance: <b>ask</b>.</div></div>
  <div class="li"><div class="n">4</div><div>Otherwise: <b>answer</b>, with the usual defaults.</div></div>
</div>
<div class="note">The decision order added <b>5.1 points</b>, to 86.1% on the validation set.</div>''', 4),
    slide(5, 'The result', '''
<div class="h h2">On 7,588 sentences <em>it had never seen.</em></div>
<div class="stats">
  <div class="stat"><div class="v">84.4%</div><div class="t">Right outcomes, up from <b>65.3%</b> for the same model before.</div></div>
  <div class="stat"><div class="v">12.8%</div><div class="t">Needless questions, down from <b>42.2%</b>.</div></div>
  <div class="stat"><div class="v">$0.44</div><div class="t">Per 1,000 calls. It beat the bigger model by <b>10.2 points at one-fifth the cost</b>.</div></div>
</div>''', 5),
    follow(S),
]

for slug, title, slides in [('deterministic-logic-first', 'Deterministic logic first', p1),
                            ('model-first-code-second', 'Model first, code second', p2),
                            ('single-fast-model-vs-ensemble', 'One fast model vs an ensemble', p3)]:
    (HERE / f'{slug}.html').write_text(page(title, slides))
    print('wrote', slug)
