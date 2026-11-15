"""Render the Panditji article carousel (v2) to 1080x1350 PNGs with headless Chrome.

Usage:  python build.py            (needs network for Google Fonts: Fraunces + Inter)
Output: slides/slide-01.png ... slide-07.png, plus slides/html/ for inspection.

Copy comes from carousel.md (the cold-read-passed words). Do not change wording here;
change carousel.md, re-run clarity_lint, then mirror it below. Look: Tangent dark palette,
one display line per slide (Fraunces), body in Inter at full contrast, real assets only.
"""
from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "slides"
HTML = OUT / "html"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TOTAL = 7

BG, INK, CARD, LINE, ACCENT = "#100f0d", "#ece7de", "#1b1916", "#3a352d", "#e8a07a"

MARK = """<svg viewBox="0 0 120 120" fill="none" width="{s}" height="{s}">
<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="{w}" stroke-linecap="round"/>
<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="{w}" stroke-linecap="round"/>
<circle cx="59.2" cy="74.5" r="{r}" fill="currentColor"/></svg>"""


def mark(size: int) -> str:
    w = 6 if size < 64 else 5
    return MARK.format(s=size, w=w, r=round(w * 0.809, 3))


BASE_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=block');
*{{box-sizing:border-box}}
html,body{{margin:0;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{INK}}}
body{{background:radial-gradient(120% 80% at 80% 0%, #221d18 0%, {BG} 55%)}}
.slide{{position:relative;width:1080px;height:1350px;padding:96px 84px 0}}
.top{{display:flex;justify-content:space-between;align-items:center;font:600 24px Inter,sans-serif;
     letter-spacing:.16em;text-transform:uppercase;color:{INK};opacity:.75}}
h1{{margin:44px 0 0;font:400 68px/1.12 Fraunces,Georgia,serif;letter-spacing:-.01em;max-width:910px}}
h1 em{{font-style:normal;color:{ACCENT}}}
.body{{margin:28px 0 0;font:400 36px/1.42 Inter,sans-serif;max-width:900px}}
.foot{{position:absolute;left:84px;right:84px;bottom:60px;display:flex;justify-content:space-between;
      align-items:center;font:500 26px Inter,sans-serif;color:{INK}}}
.foot .me{{display:flex;gap:14px;align-items:center}}
.swipe{{font:600 26px Inter,sans-serif}}
"""


def page(n: int, inner: str, extra_css: str = "", swipe: bool = False) -> str:
    right = '<span class="swipe">Swipe &rarr;</span>' if swipe else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div class="slide">
<div class="top"><span>Building Panditji</span><span>{n} / {TOTAL}</span></div>
{inner}
<div class="foot"><span class="me">{mark(40)}<span>@tangentideas.ai</span></span>{right}</div>
</div></body></html>"""


def chat_card(label: str, answer: str) -> str:
    return f"""<div class="chat"><div class="lbl">{label}</div>
<div class="q">What does my chart say about my career?</div>
<div class="a">{answer}</div></div>"""


SLIDES = []

# 1 -- cover: what this post is about, plus the real app on a phone
SLIDES.append(page(1, """
<h1>My free astrology app won&rsquo;t let the AI make up <em>where planets are.</em></h1>
<p class="body">It&rsquo;s called Panditji, and I built it with AI.</p>
<div class="phone"><img src="../../assets/ask-top.webp"></div>
""", f"""
.phone{{position:absolute;left:50%;transform:translateX(-50%);top:560px;width:470px;height:980px;
  border-radius:58px;border:14px solid #2b2722;background:#fff8ec;overflow:hidden;
  box-shadow:0 30px 90px rgba(0,0,0,.6)}}
.phone img{{width:100%;display:block}}
.foot{{background:linear-gradient(rgba(16,15,13,0), {BG} 55%);padding-top:110px;bottom:0;padding-bottom:60px;left:0;right:0;padding-left:84px;padding-right:84px}}
""", swipe=True))

# 2 -- two answers to one question
SLIDES.append(page(2, f"""
<h1>At first, my app&rsquo;s AI gave <em>two answers</em> to one question.</h1>
<p class="body">I asked about my career twice and got Saturn in two different zodiac signs.
In astrology, that changes your career reading.</p>
<div class="pair">{chat_card("1st time", "&hellip;Saturn is in <b>Pisces</b>.")}
<div class="neq">&ne;</div>
{chat_card("2nd time", "&hellip;Saturn is in <b>Aries</b>.")}</div>
""", f"""
.pair{{margin-top:84px;display:flex;align-items:center;gap:24px}}
.chat{{flex:1;background:{CARD};border:2px solid {LINE};border-radius:28px;padding:28px}}
.lbl{{font:600 24px Inter;letter-spacing:.12em;text-transform:uppercase;margin-bottom:18px}}
.q{{background:#f6e7c8;color:#2a1f12;font:500 26px/1.35 Inter;border-radius:20px;padding:16px 20px;margin-left:40px}}
.a{{background:#fffaf0;color:#1c1712;font:400 32px/1.35 Inter;border-radius:20px;padding:20px 22px;margin:18px 30px 0 0}}
.a b{{font-weight:700;color:#b5452a}}
.neq{{font:400 120px Fraunces;color:{ACCENT};flex:none}}
"""))

# 3 -- why: chatbots repeat what they've read, and the web mixes two astrologies
pages = [("Western astrology", "Saturn in Aries"), ("Vedic astrology", "Saturn in Pisces"),
         ("Horoscope 2026", "Saturn moves into&hellip;"), ("Your sign this week", "Saturn says&hellip;")]
cards = "".join(f'<div class="web w{i}"><div class="bar"><i></i><i></i><i></i></div>'
                f'<div class="t">{a}</div><div class="s">{b}</div></div>' for i, (a, b) in enumerate(pages))
SLIDES.append(page(3, f"""
<h1>That&rsquo;s because AI chatbots don&rsquo;t work things out. <em>They repeat what they&rsquo;ve read.</em></h1>
<p class="body">And millions of web pages mix up Western and Indian astrology, which put the planets in different signs.</p>
<div class="viz"><div class="pile">{cards}</div>
<div class="arrow">&rarr;</div>
<div class="bot"><div class="who">AI chatbot</div><div class="say">Saturn is in&hellip; Aries? Pisces?</div></div></div>
""", f"""
.viz{{margin-top:70px;display:flex;align-items:center;gap:22px}}
.pile{{position:relative;width:500px;height:520px;flex:none}}
.web{{position:absolute;width:370px;background:{CARD};border:2px solid {LINE};border-radius:18px;padding:16px 22px 22px}}
.bar{{display:flex;gap:8px;margin-bottom:14px}} .bar i{{width:12px;height:12px;border-radius:50%;background:{LINE};display:block}}
.t{{font:600 26px Inter}} .s{{font:400 26px Inter;margin-top:6px}}
.w0{{left:0;top:0;transform:rotate(-4deg)}} .w1{{left:100px;top:132px;transform:rotate(3deg)}}
.w2{{left:10px;top:264px;transform:rotate(-2deg)}} .w3{{left:110px;top:396px;transform:rotate(4deg)}}
.arrow{{font:400 80px Inter;color:{ACCENT};flex:none}}
.bot{{width:270px;flex:none;background:#fffaf0;color:#1c1712;border-radius:28px;padding:26px 28px}}
.who{{font:600 22px Inter;letter-spacing:.1em;text-transform:uppercase;color:#7a6a58}}
.say{{font:500 34px/1.3 Inter;margin-top:10px}}
"""))

# 4 -- the fix: the app does the maths, the AI explains
step = lambda icon, text: f'<div class="step"><div class="ic">{icon}</div><div class="tx">{text}</div></div>'
phone_svg = '<svg viewBox="0 0 64 64" width="84" height="84" fill="none" stroke="currentColor" stroke-width="3"><rect x="18" y="6" width="28" height="52" rx="6"/><line x1="28" y1="50" x2="36" y2="50"/></svg>'
calc_svg = '<svg viewBox="0 0 64 64" width="84" height="84" fill="none" stroke="currentColor" stroke-width="3"><rect x="14" y="6" width="36" height="52" rx="5"/><rect x="20" y="12" width="24" height="10" rx="2"/><g fill="currentColor" stroke="none"><circle cx="23" cy="31" r="2.6"/><circle cx="32" cy="31" r="2.6"/><circle cx="41" cy="31" r="2.6"/><circle cx="23" cy="40" r="2.6"/><circle cx="32" cy="40" r="2.6"/><circle cx="41" cy="40" r="2.6"/><circle cx="23" cy="49" r="2.6"/><circle cx="32" cy="49" r="2.6"/><circle cx="41" cy="49" r="2.6"/></g></svg>'
chat_svg = '<svg viewBox="0 0 64 64" width="84" height="84" fill="none" stroke="currentColor" stroke-width="3"><path d="M10 14h44v28H30l-12 10V42h-8z" stroke-linejoin="round"/><line x1="20" y1="24" x2="44" y2="24"/><line x1="20" y1="32" x2="38" y2="32"/></svg>'
SLIDES.append(page(4, f"""
<h1>So now my app <em>works out</em> where each planet is.</h1>
<p class="body">Planets move every day, so it does the maths for your exact birth time, like a calculator.
The AI only explains the result.</p>
<div class="flow">{step(phone_svg, "Your birth date, time and place")}<div class="ar">&rarr;</div>
{step(calc_svg, "The app works out each planet")}<div class="ar">&rarr;</div>
{step(chat_svg, "The AI explains it in plain words")}</div>
""", f"""
.flow{{margin-top:90px;display:flex;align-items:stretch;gap:14px}}
.step{{flex:1;background:{CARD};border:2px solid {LINE};border-radius:28px;padding:34px 22px;text-align:center}}
.step:nth-of-type(2){{border-color:{ACCENT}}}
.ic{{color:{INK}}} .tx{{font:500 30px/1.3 Inter;margin-top:18px}}
.ar{{align-self:center;font:400 54px Inter;color:{ACCENT}}}
"""))

# 5 -- the proof: checked against NASA's data
saturn = '<svg viewBox="0 0 64 64" width="70" height="70" fill="none" stroke="currentColor" stroke-width="3"><circle cx="32" cy="32" r="12"/><ellipse cx="32" cy="32" rx="28" ry="8" transform="rotate(-18 32 32)"/></svg>'
SLIDES.append(page(5, f"""
<h1>Then I checked my app&rsquo;s answers against <em>NASA&rsquo;s planet data.</em> They match.</h1>
<p class="body">Every answer also shows which planets it looked at, so you can check too.</p>
<div class="cmp">
  <div class="row"><span class="who">NASA&rsquo;s data</span>{saturn}<span class="pos">Saturn&rsquo;s position</span></div>
  <div class="row"><span class="who">Panditji</span>{saturn}<span class="pos">Saturn&rsquo;s position</span></div>
  <div class="ok"><span class="tick">&#10003;</span> The same, to within 1/3600 of a degree</div>
</div>
""", f"""
.cmp{{margin-top:80px;background:{CARD};border:2px solid {LINE};border-radius:32px;padding:20px 40px 34px}}
.row{{display:flex;align-items:center;gap:28px;padding:26px 0;border-bottom:2px solid {LINE}}}
.who{{width:300px;font:600 34px Inter}} .pos{{font:400 34px Inter}}
.ok{{margin-top:30px;font:500 36px/1.3 Inter;display:flex;gap:18px;align-items:center}}
.tick{{color:#9fd39b;font:700 56px Inter}}
"""))

# 6 -- read the full story on Medium; try the app
md_icon = '<svg viewBox="0 0 48 48" width="64" height="64" fill="currentColor"><ellipse cx="14" cy="24" rx="10" ry="10"/><ellipse cx="31" cy="24" rx="5" ry="9.5"/><ellipse cx="41" cy="24" rx="2" ry="8.5"/></svg>'
SLIDES.append(page(6, f"""
<h1>Read the full story, with every number, <em>on Medium.</em></h1>
<div class="card read">{md_icon}<div><div class="w">Link in bio</div><div class="h">medium.com/p/26370dd5be48</div></div></div>
<div class="card"><img src="../../assets/icon-512.png"><div><div class="w">Try it free</div><div class="h">labs.tangentideas.ai/panditji</div></div></div>
""", f"""
.card{{margin-top:56px;display:flex;gap:30px;align-items:center;background:{CARD};border:2px solid {LINE};border-radius:28px;padding:34px 36px}}
.card + .card{{margin-top:24px}}
.read{{border-color:{ACCENT}}}
.card img{{width:110px;height:110px;border-radius:24px;flex:none}}
.card svg{{flex:none;margin:0 23px}}
.w{{font:500 28px Inter;letter-spacing:.08em;text-transform:uppercase}} .h{{font:600 40px Inter;margin-top:6px}}
"""))

# 7 -- follow (Tangent's standard end slide)
ig = '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3.2"><rect x="6" y="6" width="36" height="36" rx="10"/><circle cx="24" cy="24" r="8"/><circle cx="35" cy="13" r="1.8" fill="currentColor"/></svg>'
yt = '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3.2"><rect x="4" y="10" width="40" height="28" rx="8"/><path d="M20 17l11 7-11 7z" fill="currentColor"/></svg>'
md = '<svg viewBox="0 0 48 48" width="56" height="56" fill="currentColor"><ellipse cx="14" cy="24" rx="10" ry="10"/><ellipse cx="31" cy="24" rx="5" ry="9.5"/><ellipse cx="41" cy="24" rx="2" ry="8.5"/></svg>'
web = '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3"><circle cx="24" cy="24" r="18"/><ellipse cx="24" cy="24" rx="8" ry="18"/><line x1="6" y1="24" x2="42" y2="24"/></svg>'
row = lambda icon, where, handle: f'<div class="ch">{icon}<div><div class="w">{where}</div><div class="h">{handle}</div></div></div>'
SLIDES.append(page(7, f"""
<div class="big">{mark(120)}</div>
<h1>Follow along for more things I build <em>with AI.</em></h1>
<div class="list">
{row(ig, "Instagram", "@tangentideas.ai")}
{row(yt, "YouTube", "@tangentideasai")}
{row(md, "Medium", "@tangentideasai")}
{row(web, "Website", "tangentideas.ai")}
</div>
""", f"""
.big{{margin-top:40px;color:{INK}}}
h1{{margin-top:24px}}
.list{{margin-top:50px;display:grid;gap:20px}}
.ch{{display:flex;gap:30px;align-items:center;background:{CARD};border:2px solid {LINE};border-radius:24px;padding:22px 32px}}
.w{{font:500 26px Inter;letter-spacing:.08em;text-transform:uppercase}} .h{{font:600 42px Inter;margin-top:2px}}
"""))


def main() -> None:
    HTML.mkdir(parents=True, exist_ok=True)
    for i, html in enumerate(SLIDES, 1):
        src = HTML / f"slide-{i:02d}.html"
        src.write_text(html, "utf-8")
        out = OUT / f"slide-{i:02d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1350", "--virtual-time-budget=8000",
                        f"--screenshot={out}", src.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
