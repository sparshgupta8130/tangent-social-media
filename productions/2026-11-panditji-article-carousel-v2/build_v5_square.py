"""Render the approved v4 carousel as 1:1 squares (1080x1080), for Instagram carousels.

Usage:  python build_v5_square.py   ->  slides-v5-square/slide-01.png ... slide-09.png
Same words, order and pictures as v4 (build_v4.py). Only the layout is tightened to fit a
square: smaller margins, a slightly smaller headline, and per-slide picture sizes.
"""
from __future__ import annotations

import pathlib
import subprocess

import build_v4 as v

b = v.b
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "slides-v5-square"
HTML = OUT / "html"

# Applies to every slide: square canvas, tighter frame.
COMMON = """
html,body{height:1080px}
.slide{height:1080px;padding:64px 76px 44px}
h1{margin-top:30px;font-size:70px}
"""

# Per-slide fixes, appended last so they win.
PER = {
    1: """.viz{height:600px;margin:30px -76px auto} .phone{width:540px}
          .viz:after{height:200px}""",
    2: """.q{font-size:36px;padding:20px 28px} .stack .lbl[style]{margin-top:32px!important}""",
    3: """.a{font-size:38px} .neq{font-size:110px}""",
    4: """h1{font-size:58px} .sys{padding:28px 28px} .sg{font-size:38px} .ok{margin-top:12px}
          .gap{margin-top:24px;font-size:30px}""",
    5: """h1{font-size:58px} .switch{margin-bottom:18px} .switch span{font-size:32px;padding:10px 34px}
          .chart{padding:14px 36px} .r{padding:13px 0;font-size:34px}""",
    6: """.mini{padding:20px 30px} .m{font-size:36px} .ar{font-size:54px} .flow{gap:12px}
          .ex{font-size:36px}""",
    7: """.rows{gap:22px} .sm{font-size:30px}""",
    8: """.cards{gap:20px} .c{padding:26px 32px}""",
    9: """.list{gap:14px} .ch{padding:14px 30px} .ch svg{width:48px;height:48px}
          .h{font-size:36px} .w{font-size:22px}""",
}


def squarify(n: int, html: str) -> str:
    html = html.replace("height:1350px", "height:1080px")
    return html.replace("</style>", COMMON + PER.get(n, "") + "</style>", 1)


def main() -> None:
    HTML.mkdir(parents=True, exist_ok=True)
    for i, html in enumerate(v.S, 1):
        src = HTML / f"slide-{i:02d}.html"
        src.write_text(squarify(i, html).replace('src="../assets/', 'src="../../assets/'), "utf-8")
        out = OUT / f"slide-{i:02d}.png"
        subprocess.run([b.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1080", "--virtual-time-budget=8000",
                        f"--screenshot={out}", src.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
