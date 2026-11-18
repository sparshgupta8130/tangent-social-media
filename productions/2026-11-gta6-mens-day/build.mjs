// Render the Men's Day x GTA 6 poster carousel to 1080x1080 PNGs.
// Usage: node build.mjs   (run from this folder; needs network for Google Fonts)
// Copy source: carousel.md. Images: assets/gen/pick/img-0N.png (provenance: assets/gen/README.md).
// Type is our own (Anton + Inter). Never Rockstar's font, logo or "VI" lettering.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(ROOT, 'slides');
const HTML = path.join(OUT, 'html');
fs.mkdirSync(HTML, { recursive: true });
const IMG = (n) => 'file://' + path.join(ROOT, 'assets/gen-v3/pick', `img-0${n}.png`);

const mark = (size) =>
  `<svg viewBox="0 0 120 120" fill="none" width="${size}" height="${size}">` +
  `<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<circle cx="59.2" cy="74.5" r="5.6" fill="currentColor"/></svg>`;

const SH = '0 3px 0 #1a0f22,0 0 2px #1a0f22,0 6px 22px rgba(20,8,30,.55)';
const BASE = `
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@500;600;700;800&display=block');
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1080px;overflow:hidden;color:#fff}
.s{position:relative;width:1080px;height:1080px;padding:48px 60px;display:flex;flex-direction:column}
.chip{align-self:flex-start;background:#1a0f22;color:#ffd166;font:800 22px Inter;letter-spacing:.12em;text-transform:uppercase;
  padding:9px 16px;border-radius:6px}
h1{margin:16px 0 0;font:400 64px/1.04 Anton,Impact,sans-serif;letter-spacing:.005em;text-shadow:${SH};text-wrap:balance}
.sub{margin-top:12px;font:700 28px/1.25 Inter;text-shadow:${SH}}
.spacer{flex:1}
.foot{align-self:flex-end;display:flex;gap:10px;align-items:center;font:700 24px Inter;text-shadow:${SH}}
`;
const page = (n, inner, css = '', foot = true) => `<!doctype html><html><head><meta charset="utf-8"><style>${BASE}${css}</style></head>
<body style="background:url('${IMG(n)}') center/cover no-repeat #222"><div class="s">${inner}<div class="spacer"></div>
${foot ? `<div class="foot">${mark(34)}<span>@tangentideas.ai</span></div>` : ''}</div></body></html>`;

const S = [];
// 1 cover
S.push(page(1, `<h1 class="t">Happy Men&rsquo;s Day.</h1><div class="t2">Or, as men call it, GTA&nbsp;6 Day.</div>`,
  `.t{margin-top:6px;font-size:104px;text-align:center} .t2{margin-top:6px;text-align:center;font:400 64px/1.05 Anton,Impact,sans-serif;color:#ffd166;text-shadow:${SH}}
   .foot:before{content:"Swipe \\2192";margin-right:auto}`));
// 2 cheat code
S.push(page(2, `<h1>The Men&rsquo;s Day cheat code:</h1><div class="code">LEAVEMEALONE</div>`,
  `h1{font-size:62px} .code{margin-top:6px;font:400 112px Anton,Impact,sans-serif;letter-spacing:.03em;color:#ffd166;text-shadow:${SH}}`));
// 3 check-up
S.push(page(3, `<h1>Real life has no respawn.</h1><div class="y">Book the check-up.</div>`,
  `h1{font-size:76px} .y{margin-top:6px;font:400 64px Anton,Impact,sans-serif;color:#ffd166;text-shadow:${SH}}`));
// 4 main characters (sky band is narrow: keep it compact)
S.push(page(4, `<h1>No NPCs today.</h1><div class="y">Every man is a main character.</div>`,
  `.s{padding-top:30px} h1{margin-top:0;font-size:70px} .y{margin-top:2px;font:400 44px Anton,Impact,sans-serif;color:#ffd166;text-shadow:${SH}}`));
// 5 then & now
S.push(page(5, `<h1>Same player. Harder level.</h1><div class="y">From Vice City to GTA 6.</div>`,
  `h1{font-size:80px} .y{margin-top:6px;font:400 46px Anton,Impact,sans-serif;color:#ffd166;text-shadow:${SH}}`));
// 6 missions (card on the open-sky left side)
S.push(page(6, `<div class="card"><div class="ct">Before you press Start:</div>
<div class="m"><span class="bx"></span>Call your dad.</div>
<div class="m"><span class="bx"></span>Text the friend who went quiet.</div>
<div class="m"><span class="bx"></span>Tell a man you&rsquo;re proud of him.</div></div>`,
  `.card{margin-top:10px;width:560px;background:rgba(26,15,34,.82);border:3px solid #ffd166;border-radius:14px;padding:30px 32px;
   box-shadow:0 14px 40px rgba(0,0,0,.4)}
   .ct{font:400 54px/1.05 Anton,Impact,sans-serif;color:#ffd166;margin-bottom:16px}
   .m{display:flex;gap:16px;align-items:center;font:700 32px/1.2 Inter;padding:11px 0}
   .bx{flex:none;width:32px;height:32px;border:3px solid #fff;border-radius:6px}`));
// 7 maker card
S.push(page(7, `<div class="card"><div class="ct">Made with AI by a guy who should be playing GTA 6 right now.</div>
<div class="cs">Follow for more art, apps and stories.</div>
<div class="rows"><div><span>Instagram</span>@tangentideas.ai</div><div><span>YouTube</span>@tangentideasai</div>
<div><span>Medium</span>@tangentideasai</div><div><span>Web</span>tangentideas.ai</div></div></div>`,
  `.card{margin:90px auto 0;width:840px;background:rgba(26,15,34,.85);border:3px solid #ffd166;border-radius:14px;padding:44px 52px}
   .ct{font:400 54px/1.08 Anton,Impact,sans-serif;text-wrap:balance} .cs{margin-top:14px;font:700 32px/1.3 Inter;color:#ffd166}
   .rows{margin-top:28px;display:grid;gap:10px;font:600 30px Inter} .rows span{display:inline-block;width:190px;color:#c9b8d8}`, false));

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
