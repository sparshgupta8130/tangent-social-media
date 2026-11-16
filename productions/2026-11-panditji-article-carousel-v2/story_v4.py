"""Render the Instagram Story frame for the Panditji article post (1080x1920).

Usage:  python story_v4.py   ->  story/story-v4.png
Same look as the v4 carousel. Instagram's top ~250px and bottom ~350px are kept free of
anything important. The gap under "Tap the link below" is left empty for the Link sticker,
which Sparsh adds in the Instagram app and points at https://medium.com/p/26370dd5be48 .
"""
from __future__ import annotations

import pathlib
import subprocess

import build_v3 as b

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "story"

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400&family=Inter:wght@500;600&display=block');
*{{box-sizing:border-box}}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;color:{b.INK};
  background:radial-gradient(120% 70% at 80% 0%, #221d18 0%, {b.BG} 55%) {b.BG}}}
.wrap{{position:absolute;left:84px;right:84px;top:270px}}
.tag{{display:flex;align-items:center;gap:16px;font:600 30px Inter;letter-spacing:.16em;text-transform:uppercase}}
h1{{margin:40px 0 0;font:400 92px/1.08 Fraunces,Georgia,serif;letter-spacing:-.01em;text-wrap:balance}}
h1 em{{font-style:normal;color:{b.ACCENT}}}
.viz{{position:absolute;left:0;right:0;top:660px;height:560px;overflow:hidden;display:flex;justify-content:center}}
.viz:after{{content:"";position:absolute;left:0;right:0;bottom:0;height:220px;
  background:linear-gradient(rgba(16,15,13,0),{b.BG} 85%)}}
.phone{{width:560px;height:1180px;border-radius:58px;border:14px solid #2b2722;background:#fff8ec;
  overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.6)}} .phone img{{width:100%;display:block}}
.cta{{position:absolute;left:0;right:0;top:1250px;text-align:center;font:600 44px Inter}}
.cta span{{color:{b.ACCENT}}}
</style></head><body>
<div class="wrap"><div class="tag">{b.mark(56)}<span>New post</span></div>
<h1>Why my astrology app doesn&rsquo;t let AI <em>do the maths</em></h1></div>
<div class="viz"><div class="phone"><img src="../assets/ask-top.webp"></div></div>
<div class="cta">Tap the link below <span>&darr;</span></div>
</body></html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    src = OUT / "story-v4.html"
    src.write_text(HTML, "utf-8")
    out = OUT / "story-v4.png"
    subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=1080,1920", "--virtual-time-budget=8000",
                    f"--screenshot={out}", src.as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
