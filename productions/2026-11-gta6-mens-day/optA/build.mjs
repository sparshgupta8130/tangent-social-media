// Option A, "The boy who played Vice City": render the 7-slide carousel to 1080x1080 PNGs + a contact sheet.
// Usage: node build.mjs   (run from optA/; needs network for Inter from Google Fonts)
// Copy source: carousel.md (exact words). Images: assets/pick/img-0N.png (provenance: assets/README.md).
// Headline type: Pricedown Black (Typodermic Desktop EULA v260817, finished static images only).
// The font file lives in ../fonts/ (git-ignored) and is NEVER committed or shipped; only the rendered PNGs leave this machine.
// No GTA logo, wordmark or "VI" lettering anywhere.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const FONT = path.join(ROOT, '..', 'fonts', 'PricedownBl.otf');
if (!fs.existsSync(FONT)) {
  console.error(`Missing ${FONT}. Download Pricedown Black from typodermicfonts.com/downloads (free desktop package) and put "Pricedown Bl.otf" there as PricedownBl.otf.`);
  process.exit(1);
}
const OUT = path.join(ROOT, 'slides');
const HTML = path.join(OUT, 'html');
fs.mkdirSync(HTML, { recursive: true });
const IMG = (n) => 'file://' + path.join(ROOT, 'assets/pick', `img-0${n}.png`);

const mark = (size) =>
  `<svg viewBox="0 0 120 120" fill="none" width="${size}" height="${size}">` +
  `<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<circle cx="59.2" cy="74.5" r="5.6" fill="currentColor"/></svg>`;

// Poster type: white (or yellow) fill, thick black outline drawn behind the fill (paint-order), hard drop shadow.
const DROP = '0 6px 0 #000, 0 10px 18px rgba(0,0,0,.45)';
const BASE = `
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=block');
@font-face{font-family:Pricedown;src:url('file://${FONT}') format('opentype');font-display:block}
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1080px;overflow:hidden;color:#fff}
.s{position:relative;width:1080px;height:1080px;padding:40px 56px 36px;display:flex;flex-direction:column}
.scrim{position:absolute;inset:0 0 auto 0;height:55%;pointer-events:none;
  background:linear-gradient(180deg,rgba(18,6,28,.42) 0%,rgba(18,6,28,.22) 45%,rgba(18,6,28,0) 100%)}
.h,.b{position:relative;font-family:Pricedown,Impact,sans-serif;font-weight:400;paint-order:stroke fill;
  -webkit-text-stroke:var(--sw) #000;text-shadow:${DROP};text-wrap:balance;margin:0}
.h{--sw:14px;font-size:96px;line-height:.98;letter-spacing:.01em}
.b{--sw:10px;margin-top:14px;font-size:54px;line-height:1.02;color:#ffd166;letter-spacing:.015em}
/* B lines on slides 2-6: Inter 800 (Pricedown's 1 reads as I at this size: "12" -> "IZ", "11 p.m." -> "II p.m.") */
.b.i{--sw:9px;font-family:Inter,sans-serif;font-weight:800;font-size:46px;line-height:1.14;letter-spacing:-.005em;margin-top:16px;
  text-shadow:0 4px 0 #000,0 8px 16px rgba(0,0,0,.45)}
.spacer{flex:1}
.foot{position:relative;display:flex;align-items:center;gap:9px;font:700 22px Inter;
  text-shadow:0 2px 0 #000,0 0 6px rgba(0,0,0,.8)}
.foot .h1{margin-left:auto;display:flex;align-items:center;gap:9px}
`;
const page = (n, inner, css = '', { foot = true, swipe = false } = {}) => `<!doctype html><html><head><meta charset="utf-8"><style>${BASE}${css}</style></head>
<body style="background:url('${IMG(n)}') center/cover no-repeat #222"><div class="scrim"></div><div class="s">${inner}<div class="spacer"></div>
${foot ? `<div class="foot">${swipe ? '<span class="sw">Swipe &rarr;</span>' : ''}<span class="h1">${mark(30)}<span>@tangentideas.ai</span></span></div>` : ''}</div></body></html>`;

const S = [];
// 1 cover: one headline, set as two lines (white, then yellow). Faces sit below ~37%.
S.push(page(1, `<h1 class="h">The boy who played Vice&nbsp;City is a man&nbsp;now.</h1><div class="b y">Today, GTA&nbsp;6 is&nbsp;out.</div>`,
  `.s{padding-top:58px} .h{font-size:78px;text-align:center} .b{text-align:center;font-size:68px;margin-top:10px}
   .sw{font:800 30px Inter;color:#ffd166;background:#000;padding:8px 16px;border-radius:6px;text-shadow:none}`, { swipe: true }));
// 2 2003
S.push(page(2, `<h1 class="h">2003. Vice&nbsp;City.</h1><div class="b i">He was 12. Cyber caf&eacute;, one hour at a&nbsp;time.</div>`,
  `.h{font-size:118px} .b{max-width:900px}`));
// 3 2013 (head reaches ~24% at centre: headline top-left, second line right-aligned over the open window, clear of his face)
S.push(page(3, `<h1 class="h">2013. GTA&nbsp;V.</h1><div class="b i">He was 22.<br>First salary.<br>First thing he&nbsp;bought.</div>`,
  `.s{padding-top:30px} .h{font-size:112px} .b{align-self:flex-end;text-align:right;max-width:420px;font-size:50px;margin-top:4px;text-wrap:wrap}`));
// 4 2026
S.push(page(4, `<h1 class="h">2026. GTA&nbsp;6.</h1><div class="b i">He&rsquo;s 35. A job, a home loan, a baby asleep on his&nbsp;shoulder.</div>`,
  `.s{padding-top:30px} .h{font-size:112px} .b{max-width:900px}`));
// 5 tonight (night: fill stays white, B yellow)
S.push(page(5, `<h1 class="h">He&rsquo;ll play tonight.</h1><div class="b i">After the baby sleeps. After the 11&nbsp;p.m.&nbsp;call.</div>`,
  `.h{font-size:104px} .b{max-width:820px}`));
// 6 Men's Day
S.push(page(6, `<h1 class="h">Happy Men&rsquo;s Day to every boy who grew&nbsp;up.</h1><div class="b i">Today, play. You&rsquo;ve earned&nbsp;it.</div>`,
  `.h{font-size:84px;text-align:center} .b{text-align:center;font-size:52px}`));
// 7 maker card on the skyline
S.push(page(7, `<div class="card"><h1 class="h">Made with AI by a guy who should be playing GTA&nbsp;6 right&nbsp;now.</h1>
<div class="cs">Follow for more art, apps and stories.</div>
<div class="rows"><div><span>Instagram</span>@tangentideas.ai</div><div><span>YouTube</span>@tangentideasai</div>
<div><span>Medium</span>@tangentideasai</div><div><span>Web</span>tangentideas.ai</div></div></div>`,
  `.scrim{display:none}
   .card{margin:70px auto 0;width:880px;background:rgba(20,8,30,.86);border:4px solid #000;outline:3px solid #ffd166;outline-offset:-10px;
     border-radius:16px;padding:46px 54px 44px;box-shadow:0 16px 44px rgba(0,0,0,.45)}
   .card .h{--sw:12px;font-size:66px;line-height:1.02;text-align:center}
   .cs{margin-top:22px;font:800 32px/1.3 Inter;color:#ffd166;text-align:center}
   .rows{margin-top:26px;display:grid;gap:10px;font:600 30px Inter} .rows span{display:inline-block;width:190px;color:#c9b8d8}`, { foot: false }));

const browser = await chromium.launch();
const pg = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
const files = [];
for (let i = 0; i < S.length; i++) {
  const id = String(i + 1).padStart(2, '0');
  const f = path.join(HTML, `slide-${id}.html`);
  fs.writeFileSync(f, S[i]);
  await pg.goto('file://' + f, { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  // overflow check: no element may spill past the 1080 frame or out of its block
  const bad = await pg.evaluate(() => [...document.querySelectorAll('.h,.b,.card,.foot')]
    .filter((e) => { const r = e.getBoundingClientRect(); return r.right > 1080 || r.bottom > 1080 || r.left < 0 || e.scrollWidth > e.clientWidth + 1; })
    .map((e) => e.className));
  const pd = await pg.evaluate(() => document.fonts.check('40px Pricedown'));
  if (!pd) throw new Error('Pricedown failed to load');
  if (bad.length) console.warn(`slide ${id}: overflow in ${bad.join(', ')}`);
  const png = path.join(OUT, `slide-${id}.png`);
  await pg.screenshot({ path: png });
  files.push(png);
}
// contact sheet: 4 + 3 grid of 360px thumbs
const thumbs = files.map((f) => `<img src="file://${f}">`).join('');
await pg.setViewportSize({ width: 1500, height: 760 });
await pg.setContent(`<html><body style="margin:0;background:#111;padding:12px;display:grid;grid-template-columns:repeat(4,360px);gap:12px">
<style>img{width:360px;height:360px;display:block}</style>${thumbs}</body></html>`);
await pg.waitForTimeout(300);
await pg.screenshot({ path: path.join(ROOT, 'contact-sheet.jpg'), type: 'jpeg', quality: 85 });
await browser.close();
console.log(`rendered ${S.length} slides to ${OUT}`);
