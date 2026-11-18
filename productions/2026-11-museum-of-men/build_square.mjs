// Render "The Museum of Men" carousel to 1080x1080 (1:1) PNGs. Square twin of build.mjs (4:5).
// Usage: node build_square.mjs   (run from this folder; needs network for Google Fonts)
// Copy source: carousel.md. Change words there first, re-lint, then mirror them here.
// Images: assets/gen/pick/slide-0N.png (Nano Banana Pro; provenance in assets/gen/README.md).
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(ROOT, 'slides-square');
const HTML = path.join(OUT, 'html');
fs.mkdirSync(HTML, { recursive: true });
const IMG = (n) => 'file://' + path.join(ROOT, 'assets/gen/pick', `slide-0${n}.png`);
const TOTAL = 10;
const INK = '#1d1a16', MUTED = '#7a6650';
const SRC_W = 1856, SRC_H = 2304;
const Y0 = { 9: 448 }; // per-slide top of the square window (source px); default 300

const mark = (size, color = 'currentColor') =>
  `<svg viewBox="0 0 120 120" fill="none" width="${size}" height="${size}" style="color:${color}">` +
  `<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>` +
  `<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>` +
  `<circle cx="59.2" cy="74.5" r="4.85" fill="currentColor"/></svg>`;

// background crop: [x0, y0, w] in source px (square window); null = default square crop
const bg = (n, crop = null) => {
  const [x0, y0, w] = crop || [0, Y0[n] ?? 300, SRC_W], s = 1080 / w;
  return `background:url('${IMG(n)}') no-repeat;background-size:${SRC_W * s}px ${SRC_H * s}px;` +
    `background-position:${-x0 * s}px ${-y0 * s}px`;
};

const BASE = `
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=block');
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1080px;overflow:hidden;color:${INK}}
.slide{position:relative;width:1080px;height:1080px;padding:50px 72px 42px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;font:600 22px Inter;letter-spacing:.18em;text-transform:uppercase;opacity:.62}
.lbl{margin-top:6px;font:600 24px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
h1{margin:14px 0 0;max-width:940px;font:400 56px/1.12 Fraunces,Georgia,serif;letter-spacing:-.012em;text-wrap:balance}
.spacer{flex:1}
.foot{display:flex;justify-content:space-between;align-items:center;font:500 24px Inter;opacity:.8}
.foot .me{display:flex;gap:12px;align-items:center}
.dark{color:#f6f1e8} .dark .lbl{color:#e6cfae}
`;

const page = (n, inner, style, css = '', cls = '', footRight = '') => `<!doctype html><html><head><meta charset="utf-8">
<style>${BASE}${css}</style></head><body style="${style}"><div class="slide ${cls}">
${inner}<div class="spacer"></div>
<div class="foot"><span class="me">${mark(36)}<span>@tangentideas.ai</span></span><span>${footRight}</span></div>
</div></body></html>`;

const exhibit = (n, num, name, h1, crop = null, extra = '', css = '') =>
  page(n, `<div class="lbl">Exhibit ${num} &middot; ${name}</div><h1>${h1}</h1>${extra}`, bg(n, crop), css);

const S = [];

// 1 cover
S.push(page(1, `<div class="cov"><h1 class="t">The Museum of Men</h1>
<div class="sub">Things men never throw away</div></div>`,
  bg(1), `.cov{margin-top:24px;text-align:center}
.t{max-width:none;margin:0;font:500 96px/1.02 Fraunces,Georgia,serif;letter-spacing:-.02em}
.sub{margin-top:16px;font:400 50px/1.15 Fraunces,Georgia,serif}
.ex{margin-top:22px;font:500 26px Inter;color:${MUTED}}`, '',
  'Swipe &rarr;'));

// 2-7 exhibits
S.push(exhibit(2, 1, 'The cable drawer', 'Chargers for phones nobody has used in years. Just in case.'));
S.push(exhibit(3, 2, 'The phone box', 'He kept his phone&rsquo;s box, to sell the phone one day.'));
S.push(exhibit(4, 3, 'The mystery keys', 'Nobody knows what these keys open. Nobody can throw them away.'));
S.push(exhibit(5, 4, 'His chappals', 'His chappals are twelve years old. He says they&rsquo;re still fine.'));
S.push(exhibit(6, 5, 'The T-shirt', 'His college T-shirt became his gym T-shirt. Next, a car cloth.'));
S.push(exhibit(7, 6, 'The remote', 'The TV remote is still in its plastic cover. The TV is nine years old.'));

// 8 the phone: zoomed crop so the screen is readable; chat drawn in code
const C8 = [648, 994, 560], s8 = 1080 / C8[2];
const scr = { x: (847 - C8[0]) * s8, y: (1156 - C8[1]) * s8, w: (1010 - 847) * s8, h: (1485 - 1156) * s8 };
const screen = `<div class="scr">
  <div class="hd"><div class="av">R</div><div><div class="nm">Rahul</div><div class="st">online</div></div></div>
  <div class="body"><div class="in">Kaisa hai bhai? 🙂</div></div>
  <div class="bar"><div class="draft">Honestly bro, I&rsquo;m not doing okay.<span class="cur"></span></div><div class="send">&#10148;</div></div>
</div>`;
S.push(exhibit(8, 7, 'His phone', 'One message he typed, but never sent.', C8, screen,
  `h1{font-size:54px}
.scr{position:absolute;left:${scr.x}px;top:${scr.y}px;width:${scr.w}px;height:${scr.h}px;border-radius:34px;overflow:hidden;
  background:#efeae2;display:flex;flex-direction:column;font-family:Inter;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}
.scr:after{content:"";position:absolute;inset:0;background:linear-gradient(155deg,rgba(255,255,255,.22),rgba(255,255,255,0) 45%);pointer-events:none}
.hd{display:flex;gap:12px;align-items:center;padding:34px 14px 12px;background:#f7f5f1;border-bottom:1px solid #ddd6cb}
.av{width:38px;height:38px;border-radius:50%;background:#9db7a8;color:#fff;font:600 19px Inter;display:grid;place-items:center}
.nm{font:600 20px Inter;color:#1d1a16} .st{font:400 14px Inter;color:#6f8f7c}
.body{flex:1;padding:16px 12px}
.in{display:inline-block;background:#fff;border-radius:4px 16px 16px 16px;padding:10px 15px;font:400 22px/1.3 Inter;color:#1d1a16;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.bar{display:flex;gap:8px;align-items:flex-end;padding:10px 10px 22px}
.draft{flex:1;background:#fff;border-radius:22px;padding:12px 15px;font:500 26px/1.25 Inter;color:#1d1a16}
.cur{display:inline-block;width:3px;height:28px;margin-left:2px;vertical-align:-4px;background:#2f7d5b}
.send{width:46px;height:46px;border-radius:50%;background:#c9c3b9;color:#fff;font-size:20px;display:grid;place-items:center}`));

// 9 the close (dark image, light text)
S.push(page(9, `<h1 class="close">Men keep a lot to themselves. Today, ask one how he&rsquo;s really doing.</h1>`,
  bg(9), `.close{margin-top:0;font-size:54px;max-width:860px;text-shadow:0 2px 18px rgba(0,0,0,.35)}`, 'dark'));

// 10 the maker: label card only (Sparsh's call: no photo)
const C10 = [560, 0, 736];
S.push(page(10, `<div class="wall">Happy International<br>Men&rsquo;s Day</div><div class="card">
  <div class="cl">Exhibit 8 &middot; The maker</div>
  <div class="ct">The man who made this museum, with AI.</div>
  <div class="cs">Follow him for more art, apps and stories.</div>
  <div class="rule"></div>
  <div class="rows">
    <div><span>Instagram</span>@tangentideas.ai</div>
    <div><span>YouTube</span>@tangentideasai</div>
    <div><span>Medium</span>@tangentideasai</div>
    <div><span>Web</span>tangentideas.ai</div>
  </div>
</div>`, bg(3, C10),
  `.wall{margin-top:40px;text-align:center;font:400 60px/1.08 Fraunces,Georgia,serif;letter-spacing:-.01em;color:#2a241d}
.card{margin:34px auto 0;width:800px;background:#fbfaf7;border-radius:6px;padding:44px 56px 38px;
  box-shadow:0 18px 50px rgba(60,45,30,.18),0 2px 6px rgba(60,45,30,.10)}
.cl{font:600 24px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
.ct{margin-top:14px;font:400 50px/1.12 Fraunces,Georgia,serif;letter-spacing:-.01em;text-wrap:balance}
.cs{margin-top:14px;font:400 32px/1.25 Fraunces,Georgia,serif;color:#3a332b}
.rule{height:1px;background:#d9d2c6;margin:28px 0 20px}
.rows{display:grid;gap:10px;font:500 27px Inter}
.rows span{display:inline-block;width:190px;color:${MUTED};font-weight:500}
.disc{margin-top:26px;font:400 22px Inter;color:${MUTED}}`));

const browser = await chromium.launch();
const pg = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
for (let i = 0; i < S.length; i++) {
  const f = path.join(HTML, `slide-${String(i + 1).padStart(2, '0')}.html`);
  fs.writeFileSync(f, S[i]);
  await pg.goto('file://' + f, { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: path.join(OUT, `slide-${String(i + 1).padStart(2, '0')}.png`) });
}
await browser.close();
console.log(`rendered ${S.length} slides to ${OUT}`);
