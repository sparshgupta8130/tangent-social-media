"""Render the Panditji article carousel v3 (approved message and arc) to 1080x1350 PNGs.

Usage:  python build_v3.py      (needs network for Google Fonts: Fraunces + Inter)
Output: slides-v3/slide-01.png ... slide-08.png (+ slides-v3/html/ for inspection)

Copy comes from carousel-v3.md: ONE beat sentence per slide, nothing else but the picture.
Change words there first, re-lint, then mirror them here.
"""
from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "slides-v3"
HTML = OUT / "html"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TOTAL = 8
BG, INK, CARD, LINE, ACCENT = "#100f0d", "#ece7de", "#1b1916", "#3a352d", "#e8a07a"


def mark(size: int) -> str:
    w = 6 if size < 64 else 5
    return (f'<svg viewBox="0 0 120 120" fill="none" width="{size}" height="{size}">'
            f'<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="{w}" stroke-linecap="round"/>'
            f'<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="{w}" stroke-linecap="round"/>'
            f'<circle cx="59.2" cy="74.5" r="{round(w * 0.809, 3)}" fill="currentColor"/></svg>')


BASE = f"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400&family=Inter:wght@400;500;600;700&display=block');
*{{box-sizing:border-box}}
html,body{{margin:0;width:1080px;height:1350px;overflow:hidden;color:{INK};
  background:radial-gradient(120% 80% at 80% 0%, #221d18 0%, {BG} 55%) {BG}}}
.slide{{width:1080px;height:1350px;padding:96px 84px 60px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;font:600 24px Inter;letter-spacing:.16em;
  text-transform:uppercase;opacity:.75}}
h1{{margin:48px 0 0;font:400 82px/1.1 Fraunces,Georgia,serif;letter-spacing:-.01em}}
h1 em{{font-style:normal;color:{ACCENT}}}
.viz{{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}}
.foot{{display:flex;justify-content:space-between;align-items:center;font:500 26px Inter}}
.foot .me{{display:flex;gap:14px;align-items:center}}
.bubble{{border-radius:26px;padding:24px 30px;font:500 36px/1.3 Inter}}
.q{{background:#f6e7c8;color:#2a1f12}} .a{{background:#fffaf0;color:#1c1712}}
.lbl{{font:600 24px Inter;letter-spacing:.12em;text-transform:uppercase;margin-bottom:14px}}
.card{{background:{CARD};border:2px solid {LINE};border-radius:28px}}
"""


def page(n: int, h1: str, viz: str, css: str = "", swipe: bool = False) -> str:
    right = '<span style="font:600 26px Inter">Swipe &rarr;</span>' if swipe else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{css}</style></head><body>
<div class="slide"><div class="top"><span>Building Panditji</span><span>{n} / {TOTAL}</span></div>
<h1>{h1}</h1><div class="viz">{viz}</div>
<div class="foot"><span class="me">{mark(40)}<span>@tangentideas.ai</span></span>{right}</div></div></body></html>"""


S = []
Q = "What does my chart say about my career?"

# 1 cover
S.append(page(1, "Why my astrology app doesn&rsquo;t let AI <em>do the maths</em>",
    '<div class="phone"><img src="../assets/ask-top.webp"></div>',
    f""".viz{{align-items:flex-start;overflow:hidden;margin:44px -84px 0;position:relative}}
.phone{{width:470px;height:1000px;border-radius:58px;border:14px solid #2b2722;background:#fff8ec;
  overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.6)}} .phone img{{width:100%;display:block}}
.viz:after{{content:"";position:absolute;left:0;right:0;bottom:0;height:200px;
  background:linear-gradient(rgba(16,15,13,0),{BG})}}""", swipe=True))

# 2 asked twice
S.append(page(2, "I asked an AI the same astrology question <em>twice.</em>",
    f'<div class="stack"><div class="lbl">1st time</div><div class="bubble q">{Q}</div>'
    f'<div class="lbl" style="margin-top:48px">2nd time</div><div class="bubble q">{Q}</div></div>',
    ".stack{width:760px}"))

# 3 two signs
ans = lambda lbl, sign: (f'<div class="card col"><div class="lbl">{lbl}</div>'
                         f'<div class="bubble a">Saturn is in <b>{sign}</b>.</div></div>')
S.append(page(3, "It put Saturn in <em>two different signs.</em>",
    f'<div class="pair">{ans("1st answer", "Pisces")}<div class="neq">&ne;</div>{ans("2nd answer", "Aries")}</div>',
    f""".pair{{display:flex;align-items:center;gap:22px;width:100%}} .col{{flex:1;padding:30px}}
.a b{{color:#b5452a;font-weight:700}} .a{{font-size:42px}}
.neq{{font:400 130px Fraunces;color:{ACCENT}}}"""))

# 4 AI guesses
bot = ('<svg viewBox="0 0 64 64" width="150" height="150" fill="none" stroke="currentColor" stroke-width="2.6">'
       '<rect x="12" y="18" width="40" height="32" rx="9"/><line x1="32" y1="10" x2="32" y2="18"/>'
       '<circle cx="32" cy="8" r="2.5" fill="currentColor"/><circle cx="24" cy="33" r="3" fill="currentColor"/>'
       '<circle cx="40" cy="33" r="3" fill="currentColor"/><line x1="25" y1="42" x2="39" y2="42"/></svg>')
S.append(page(4, "AI guesses. <em>It doesn&rsquo;t calculate.</em>",
    f'<div class="row"><div class="bot">{bot}</div><div class="bubble a big">Saturn is in&hellip;<br>Pisces? Aries?</div></div>',
    ".row{display:flex;align-items:center;gap:40px} .bot{color:#ece7de} .big{font-size:46px;padding:34px 40px}"))

# 5 app does the maths
calc = ('<svg viewBox="0 0 64 64" width="120" height="120" fill="none" stroke="currentColor" stroke-width="2.6">'
        '<rect x="14" y="6" width="36" height="52" rx="5"/><rect x="20" y="12" width="24" height="10" rx="2"/>'
        '<g fill="currentColor" stroke="none">' + "".join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for y in (31, 40, 49) for x in (23, 32, 41)) + '</g></svg>')
chat = ('<svg viewBox="0 0 64 64" width="120" height="120" fill="none" stroke="currentColor" stroke-width="2.6">'
        '<path d="M10 14h44v28H30l-12 10V42h-8z" stroke-linejoin="round"/><line x1="20" y1="24" x2="44" y2="24"/>'
        '<line x1="20" y1="32" x2="38" y2="32"/></svg>')
S.append(page(5, "So my app does the maths, and <em>AI just explains it.</em>",
    f'<div class="flow"><div class="card step hi">{calc}<div class="tx">My app works out each planet</div></div>'
    f'<div class="ar">&rarr;</div><div class="card step">{chat}<div class="tx">AI explains it to you</div></div></div>',
    f""".flow{{display:flex;align-items:stretch;gap:20px;width:100%}}
.step{{flex:1;text-align:center;padding:48px 28px}} .hi{{border-color:{ACCENT}}}
.tx{{font:500 38px/1.3 Inter;margin-top:24px}} .ar{{align-self:center;font:400 70px Inter;color:{ACCENT}}}"""))

# 6 matches NASA
sat = ('<svg viewBox="0 0 64 64" width="84" height="84" fill="none" stroke="currentColor" stroke-width="3">'
       '<circle cx="32" cy="32" r="12"/><ellipse cx="32" cy="32" rx="28" ry="8" transform="rotate(-18 32 32)"/></svg>')
S.append(page(6, "Now its answers match <em>NASA&rsquo;s planet data.</em>",
    f'<div class="card cmp"><div class="r"><span>NASA</span>{sat}<span>Saturn</span></div>'
    f'<div class="r"><span>Panditji</span>{sat}<span>Saturn</span></div>'
    f'<div class="ok"><span class="tick">&#10003;</span>Same place</div></div>',
    f""".cmp{{width:100%;padding:16px 48px 40px}}
.r{{display:flex;align-items:center;gap:36px;padding:30px 0;border-bottom:2px solid {LINE};font:600 44px Inter}}
.r span:first-child{{width:260px}}
.ok{{margin-top:34px;display:flex;align-items:center;gap:20px;font:600 46px Inter}}
.tick{{color:#9fd39b;font:700 66px Inter}}"""))

# 7 read on Medium (standard end slide 1)
md = ('<svg viewBox="0 0 48 48" width="70" height="70" fill="currentColor"><ellipse cx="14" cy="24" rx="10" ry="10"/>'
      '<ellipse cx="31" cy="24" rx="5" ry="9.5"/><ellipse cx="41" cy="24" rx="2" ry="8.5"/></svg>')
S.append(page(7, "Read the full story <em>on Medium.</em>",
    f'<div class="cards"><div class="card c hi">{md}<div><div class="w">Link in bio</div><div class="h">medium.com/p/26370dd5be48</div></div></div>'
    f'<div class="card c"><img src="../assets/icon-512.png"><div><div class="w">Try it free</div><div class="h">labs.tangentideas.ai/panditji</div></div></div></div>',
    f""".cards{{width:100%;display:grid;gap:26px}} .c{{display:flex;gap:30px;align-items:center;padding:36px}}
.hi{{border-color:{ACCENT}}} .c svg{{margin:0 20px;flex:none}} .c img{{width:110px;height:110px;border-radius:24px}}
.w{{font:500 28px Inter;letter-spacing:.08em;text-transform:uppercase}} .h{{font:600 40px Inter;margin-top:6px}}"""))

# 8 follow (standard end slide 2)
icons = {
    "Instagram": '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3.2"><rect x="6" y="6" width="36" height="36" rx="10"/><circle cx="24" cy="24" r="8"/><circle cx="35" cy="13" r="1.8" fill="currentColor"/></svg>',
    "YouTube": '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3.2"><rect x="4" y="10" width="40" height="28" rx="8"/><path d="M20 17l11 7-11 7z" fill="currentColor"/></svg>',
    "Medium": md.replace('width="70" height="70"', 'width="56" height="56"'),
    "Website": '<svg viewBox="0 0 48 48" width="56" height="56" fill="none" stroke="currentColor" stroke-width="3"><circle cx="24" cy="24" r="18"/><ellipse cx="24" cy="24" rx="8" ry="18"/><line x1="6" y1="24" x2="42" y2="24"/></svg>',
}
handles = [("Instagram", "@tangentideas.ai"), ("YouTube", "@tangentideasai"), ("Medium", "@tangentideasai"), ("Website", "tangentideas.ai")]
rows = "".join(f'<div class="card ch">{icons[w]}<div><div class="w">{w}</div><div class="h">{h}</div></div></div>' for w, h in handles)
S.append(page(8, "Follow along for more things I build <em>with AI.</em>", f'<div class="list">{rows}</div>',
    """.list{width:100%;display:grid;gap:20px} .ch{display:flex;gap:30px;align-items:center;padding:22px 32px}
.w{font:500 26px Inter;letter-spacing:.08em;text-transform:uppercase} .h{font:600 42px Inter;margin-top:2px}"""))


def main() -> None:
    HTML.mkdir(parents=True, exist_ok=True)
    for i, html in enumerate(S, 1):
        src = HTML / f"slide-{i:02d}.html"
        src.write_text(html.replace('src="../assets/', 'src="../../assets/'), "utf-8")
        out = OUT / f"slide-{i:02d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1350", "--virtual-time-budget=8000",
                        f"--screenshot={out}", src.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
