"""Render the Panditji article carousel v4 to 1080x1350 PNGs (9 slides).

Usage:  python build_v4.py      (needs network for Google Fonts)
Output: slides-v4/slide-01.png ... slide-09.png

Copy: carousel-v4.md (one beat sentence per slide). Reuses the v3 visual system from
build_v3.py. The chat answers are illustrative mock-ups; the signs are the real 2026 values
from Panditji's engine (saturn_check_output.txt).
"""
from __future__ import annotations

import pathlib
import subprocess

import build_v3 as b

b.TOTAL = 9
b.BASE += "h1{text-wrap:balance}"  # even line lengths; no stranded last word
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "slides-v4"
HTML = OUT / "html"
ACCENT, CARD, LINE, INK = b.ACCENT, b.CARD, b.LINE, b.INK
page = b.page
Q = "Which sign is Saturn in right now?"
SMALL_H1 = "h1{font-size:68px}"

S = []

# 1 cover
S.append(page(1, "Why my astrology app doesn&rsquo;t let AI <em>do the maths</em>",
    '<div class="phone"><img src="../assets/ask-top.webp"></div>',
    f""".viz{{flex:none;height:600px;align-items:flex-start;overflow:hidden;margin:44px -84px auto;position:relative}}
.phone{{width:560px;height:1180px;border-radius:58px;border:14px solid #2b2722;background:#fff8ec;
  overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.6)}} .phone img{{width:100%;display:block}}
.viz:after{{content:"";position:absolute;left:0;right:0;bottom:0;height:230px;
  background:linear-gradient(rgba(16,15,13,0),{b.BG} 85%)}}""", swipe=True))

# 2 asked twice
S.append(page(2, "I asked an AI the same astrology question <em>twice.</em>",
    f'<div class="stack"><div class="lbl">1st chat</div><div class="bubble q">{Q}</div>'
    f'<div class="lbl" style="margin-top:48px">2nd chat</div><div class="bubble q">{Q}</div></div>',
    ".stack{width:760px} .q{font-size:40px}"))

# 3 two answers
ans = lambda lbl, sign: (f'<div class="card col"><div class="lbl">{lbl}</div>'
                         f'<div class="bubble a">Saturn is in <b>{sign}</b>.</div></div>')
S.append(page(3, "It said Pisces. <em>Then it said Aries.</em>",
    f'<div class="pair">{ans("1st answer", "Pisces")}<div class="neq">&ne;</div>{ans("2nd answer", "Aries")}</div>',
    f""".pair{{display:flex;align-items:center;gap:22px;width:100%}} .col{{flex:1;padding:30px}}
.a b{{color:#b5452a;font-weight:700}} .a{{font-size:42px}} .neq{{font:400 130px Fraunces;color:{ACCENT}}}"""))

# 4 both right, two astrologies
sys_card = lambda name, sign: (f'<div class="card sys"><div class="lbl">{name} astrology</div>'
                               f'<div class="sg">Saturn in <b>{sign}</b></div><div class="ok">&#10003; correct</div></div>')
S.append(page(4, "Both were right, in two different astrologies. <em>The AI mixed them up.</em>",
    f'<div class="wrap"><div class="pair">{sys_card("Vedic", "Pisces")}{sys_card("Western", "Aries")}</div>'
    f'<div class="gap">The two zodiacs sit about 24&deg; apart</div></div>',
    f"""h1{{font-size:64px}} .wrap{{width:100%}} .pair{{display:flex;gap:24px}} .sys{{flex:1;padding:36px 32px}}
.sg{{font:500 42px/1.25 Inter}} .sg b{{color:{ACCENT};font-weight:700}}
.ok{{margin-top:18px;font:600 30px Inter;color:#9fd39b}}
.gap{{margin-top:34px;text-align:center;font:500 34px Inter}}"""))

# 5 established rules of the astrology you pick
S.append(page(5, "So my app uses the established rules of Vedic or Western astrology, <em>whichever you pick.</em>",
    '<div class="wrap"><div class="switch"><span class="on">Vedic</span><span>Western</span></div>'
    '<div class="card chart"><div class="lbl">Your chart &middot; Vedic rules</div>'
    '<div class="r"><span>Saturn</span><span>Pisces</span><span>House 10</span></div>'
    '<div class="r"><span>Jupiter</span><span>Gemini</span><span>House 1</span></div>'
    '<div class="r"><span>Moon</span><span>Virgo</span><span>House 4</span></div></div></div>',
    f"""{SMALL_H1} .wrap{{width:100%}}
.switch{{display:inline-flex;border:2px solid {LINE};border-radius:999px;padding:6px;margin-bottom:28px}}
.switch span{{font:600 36px Inter;padding:14px 40px;border-radius:999px}}
.switch .on{{background:{ACCENT};color:#1c1712}}
.chart{{padding:28px 40px}} .r{{display:grid;grid-template-columns:1.2fr 1fr 1fr;padding:20px 0;
  border-top:2px solid {LINE};font:500 38px Inter}} .r span:first-child{{font-weight:600}}"""))

# 6 only then does AI explain
S.append(page(6, "Only then does AI read your chart and <em>explain it to you.</em>",
    '<div class="flow"><div class="card mini"><div class="lbl">Your chart</div>'
    '<div class="m">Saturn &middot; Pisces &middot; House 10</div></div>'
    '<div class="ar">&darr;</div>'
    '<div class="bubble a ex">Saturn in your 10th house points to slow, steady growth at work.</div></div>',
    f""".flow{{width:100%;display:flex;flex-direction:column;align-items:center;gap:18px}}
.mini{{padding:26px 34px;width:100%}} .m{{font:600 40px Inter}}
.ar{{font:400 70px Inter;color:{ACCENT}}} .ex{{font-size:40px;width:100%}}"""))

# 7 same answer every time
row = lambda lbl: (f'<div class="r"><div class="bubble q sm">{Q}</div><span class="to">&rarr;</span>'
                   f'<div class="bubble a res">Pisces <span class="tick">&#10003;</span></div></div>')
S.append(page(7, "Now the same question gets <em>the same answer, every time.</em>",
    f'<div class="rows"><div class="lbl">Your chart &middot; Vedic rules</div>{row("1")}{row("2")}</div>',
    f""".rows{{width:100%;display:grid;gap:30px}} .r{{display:flex;align-items:center;gap:20px}}
.sm{{font-size:32px;flex:1}} .to{{font:400 56px Inter;color:{ACCENT}}}
.res{{font:700 42px Inter;white-space:nowrap}} .tick{{color:#3f8f3a}}"""))

# 8, 9 standard end slides: reuse v3's (slides 7 and 8), renumbered
S.append(b.S[6].replace("7 / 8", "8 / 9"))
S.append(b.S[7].replace("8 / 8", "9 / 9"))


def main() -> None:
    HTML.mkdir(parents=True, exist_ok=True)
    for i, html in enumerate(S, 1):
        src = HTML / f"slide-{i:02d}.html"
        src.write_text(html.replace('src="../assets/', 'src="../../assets/'), "utf-8")
        out = OUT / f"slide-{i:02d}.png"
        subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1350", "--virtual-time-budget=8000",
                        f"--screenshot={out}", src.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
