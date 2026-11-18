// Step 3: render every text layer and the phone screen as transparent PNGs (Playwright + Google Fonts).
// Usage: node overlays.mjs   -> work/overlays/{v,p}/*.png and work/overlays/screen/*.png
// Copy is mirrored EXACTLY from ../2026-11-museum-of-men/carousel.md (and build.mjs). Change words there first.
// Typography = build.mjs: Fraunces display, Inter small-caps label, ink #1d1a16, muted #7a6650.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(ROOT, 'work', 'overlays');
const INK = '#1d1a16', MUTED = '#7a6650';

export const EXHIBITS = [
  [1, 'The cable drawer', 'Chargers for phones nobody has used in years.<br>Just in case.'],
  [2, 'The phone box', 'He kept his phone&rsquo;s box, to sell the phone one day.'],
  [3, 'The mystery keys', 'Nobody knows what these keys open.<br>Nobody can throw them away.'],
  [4, 'His chappals', 'His chappals are twelve years old.<br>He says they&rsquo;re still fine.'],
  [5, 'The T-shirt', 'His college T-shirt became his gym T-shirt.<br>Next, a car cloth.'],
  [6, 'The remote', 'The TV remote is still in its plastic cover.<br>The TV is nine years old.'],
  [7, 'His phone', 'One message he typed, but never sent.'],
];
const DRAFT = 'Honestly bro, I’m not doing okay.';

const mark = (size) =>
  `<svg viewBox="0 0 120 120" fill="none" width="${size}" height="${size}">` +
  `<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>` +
  `<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>` +
  `<circle cx="59.2" cy="74.5" r="4.85" fill="currentColor"/></svg>`;

// Format geometry. v = 9:16 master (text kept below the top 220 px and above the bottom 380 px);
// p = 4:5 (carousel-like margins).
const F = {
  v: { w: 1080, h: 1920, padT: 262, padX: 84, lbl: 27, h1: 74, title: 116, sub: 60, titleT: 330,
       close: 76, wallT: 300, wall: 84, cardT: 56, cardW: 900, cardS: 1.06 },
  p: { w: 1080, h: 1350, padT: 70, padX: 80, lbl: 24, h1: 66, title: 112, sub: 58, titleT: 120,
       close: 70, wallT: 96, wall: 72, cardT: 50, cardW: 820, cardS: 1.0 },
};

const css = (g) => `
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=block');
*{box-sizing:border-box}
html,body{margin:0;width:${g.w}px;height:${g.h}px;overflow:hidden;background:transparent;color:${INK}}
.wrap{position:absolute;left:${g.padX}px;right:${g.padX}px;top:${g.padT}px}
.lbl{font:600 ${g.lbl}px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
h1{margin:18px 0 0;max-width:920px;font:400 ${g.h1}px/1.13 Fraunces,Georgia,serif;letter-spacing:-.012em;text-wrap:pretty}
.dark{color:#f6f1e8}
.sh{text-shadow:0 2px 18px rgba(0,0,0,.38),0 1px 3px rgba(0,0,0,.25)}
`;

const doc = (g, body, extra = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${css(g)}${extra}</style></head><body>${body}</body></html>`;

const layers = (k) => {
  const g = F[k], L = {};
  L.title = doc(g, `<div class="dark sh" style="position:absolute;left:0;right:0;top:${g.titleT}px;text-align:center">
    <div style="font:500 ${g.title}px/1.02 Fraunces,Georgia,serif;letter-spacing:-.02em">The Museum of Men</div>
    <div style="margin-top:22px;font:400 ${g.sub}px/1.15 Fraunces,Georgia,serif">Things men never throw away</div></div>`);
  for (const [n, name, line] of EXHIBITS)
    L[`ex${n}`] = doc(g, `<div class="wrap"><div class="lbl">Exhibit ${n} &middot; ${name}</div><h1>${line}</h1></div>`);
  L.close = doc(g, `<div class="wrap dark sh"><h1 style="font-size:${g.close}px;margin-top:0">Men keep a lot to themselves.<br>Today, ask one how he&rsquo;s really doing.</h1></div>`);
  L.end = doc(g, `<div class="wall">Happy International<br>Men&rsquo;s Day</div><div class="card">
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
  <div class="disc"><span class="mk">${mark(30)}</span>Images made with AI</div>
</div>`, `.wall{position:absolute;left:0;right:0;top:${g.wallT}px;text-align:center;font:400 ${g.wall}px/1.08 Fraunces,Georgia,serif;letter-spacing:-.01em;color:#2a241d}
.card{position:absolute;left:50%;top:${g.wallT + g.wall * 2.16 + g.cardT}px;width:820px;transform:translateX(-50%) scale(${g.cardS});transform-origin:top center;
  background:#fbfaf7;border-radius:6px;padding:56px 60px 44px;box-shadow:0 18px 50px rgba(60,45,30,.18),0 2px 6px rgba(60,45,30,.10)}
.cl{font:600 24px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
.ct{margin-top:18px;font:400 58px/1.12 Fraunces,Georgia,serif;letter-spacing:-.01em;text-wrap:balance}
.cs{margin-top:18px;font:400 36px/1.25 Fraunces,Georgia,serif;color:#3a332b}
.rule{height:1px;background:#d9d2c6;margin:36px 0 26px}
.rows{display:grid;gap:14px;font:500 30px Inter}
.rows span{display:inline-block;width:190px;color:${MUTED};font-weight:500}
.disc{margin-top:30px;display:flex;align-items:center;gap:12px;font:400 24px Inter;color:${MUTED}}
.mk{display:inline-flex;color:${INK};opacity:.8}`);
  return L;
};

// Phone screen: designed at the carousel's 2.25x scale (367x740 CSS px for the 163x329 source-px screen),
// rendered at deviceScaleFactor 4/2.25 => 652x1316 = 4 px per source px. Notch matches the photo's.
const SW = 367, SH = 740;
const screen = (nChars, cursor) => {
  const typed = DRAFT.slice(0, nChars);
  const draft = nChars ? `${typed.replace(/’/g, '&rsquo;')}` : '<span style="color:#9a958d">Message</span>';
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=block');
*{box-sizing:border-box} html,body{margin:0;width:${SW}px;height:${SH}px;background:transparent;overflow:hidden}
.scr{position:absolute;inset:0;border-radius:32px;overflow:hidden;background:#efeae2;display:flex;flex-direction:column;font-family:Inter}
.scr:after{content:"";position:absolute;inset:0;background:linear-gradient(155deg,rgba(255,255,255,.22),rgba(255,255,255,0) 45%);pointer-events:none}
.notch{position:absolute;left:${(39 / 163) * SW}px;width:${(86 / 163) * SW}px;top:0;height:25px;background:#111;border-radius:0 0 16px 16px;z-index:3}
.hd{display:flex;gap:12px;align-items:center;padding:40px 16px 14px;background:#f7f5f1;border-bottom:1px solid #ddd6cb}
.av{width:44px;height:44px;border-radius:50%;background:#9db7a8;color:#fff;font:600 22px Inter;display:grid;place-items:center}
.nm{font:600 23px Inter;color:#1d1a16} .st{font:400 16px Inter;color:#6f8f7c}
.body{flex:1;padding:16px 12px}
.in{display:inline-block;background:#fff;border-radius:4px 16px 16px 16px;padding:12px 18px;font:400 25px/1.3 Inter;color:#1d1a16;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.bar{display:flex;gap:8px;align-items:flex-end;padding:10px 10px 22px}
.draft{flex:1;min-height:66px;background:#fff;border-radius:22px;padding:14px 18px;font:500 30px/1.25 Inter;color:#1d1a16}
.cur{display:inline-block;width:3px;height:32px;margin-left:2px;vertical-align:-4px;background:#2f7d5b;opacity:${cursor ? 1 : 0}}
.send{width:54px;height:54px;border-radius:50%;background:#c9c3b9;color:#fff;font-size:24px;display:grid;place-items:center}
</style></head><body><div class="scr"><div class="notch"></div>
  <div class="hd"><div class="av">R</div><div><div class="nm">Rahul</div><div class="st">online</div></div></div>
  <div class="body"><div class="in">Kaisa hai bhai? 🙂</div></div>
  <div class="bar"><div class="draft">${draft}<span class="cur"></span></div><div class="send">&#10148;</div></div>
</div></body></html>`;
};

const browser = await chromium.launch();
for (const k of Object.keys(F)) {
  const dir = path.join(OUT, k); fs.mkdirSync(dir, { recursive: true });
  const pg = await browser.newPage({ viewport: { width: F[k].w, height: F[k].h }, deviceScaleFactor: 1 });
  for (const [name, html] of Object.entries(layers(k))) {
    const f = path.join(dir, `${name}.html`); fs.writeFileSync(f, html);
    await pg.goto('file://' + f, { waitUntil: 'networkidle' }); await pg.evaluate(() => document.fonts.ready);
    await pg.screenshot({ path: path.join(dir, `${name}.png`), omitBackground: true });
  }
  await pg.close();
}
const sdir = path.join(OUT, 'screen'); fs.mkdirSync(sdir, { recursive: true });
const sp = await browser.newPage({ viewport: { width: SW, height: SH }, deviceScaleFactor: 4 / 2.25 });
const f = path.join(sdir, 'screen.html');
for (let n = 0; n <= DRAFT.length; n++) for (const c of [0, 1]) {
  fs.writeFileSync(f, screen(n, c));
  await sp.goto('file://' + f, { waitUntil: 'networkidle' }); await sp.evaluate(() => document.fonts.ready);
  await sp.screenshot({ path: path.join(sdir, `s${String(n).padStart(2, '0')}-${c}.png`), omitBackground: true });
}
fs.writeFileSync(path.join(sdir, 'n.txt'), String(DRAFT.length));
await browser.close();
console.log('overlays done');
