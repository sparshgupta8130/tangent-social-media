// Render Option B "If an Indian man's life were GTA" to 1080x1080 PNGs + a contact sheet.
// Usage: node optB/build.mjs   (from the production folder or anywhere; needs network for Google Fonts: Anton fallback)
// Copy source: optB/carousel.md (exact words). Images: optB/assets/pick/img-0N.png (provenance: optB/assets/README.md).
// Headline font: Pricedown Black if a licensed copy sits in ../fonts/ (git-ignored, never committed),
// otherwise Anton (our house display face). HUD elements are our own simple designs, drawn here in code.
// No GTA logo, wordmark or "VI" lettering anywhere.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(ROOT, 'slides');
const HTML = path.join(OUT, 'html');
fs.mkdirSync(HTML, { recursive: true });
const IMG = (n) => 'file://' + path.join(ROOT, 'assets/pick', `img-0${n}.png`);

// --- headline font: Pricedown if present locally, else Anton ---
const FONTDIR = path.join(ROOT, '..', 'fonts');
const pd = fs.existsSync(FONTDIR)
  ? fs.readdirSync(FONTDIR).filter((f) => /pricedown/i.test(f) && /\.(otf|ttf)$/i.test(f))
      .sort((a, b) => (/b(lac)?k|bl\b/i.test(b) ? 1 : 0) - (/b(lac)?k|bl\b/i.test(a) ? 1 : 0))
  : [];
const PRICEDOWN = pd.length ? 'file://' + path.join(FONTDIR, pd[0]) : null;
const HEAD = PRICEDOWN ? `'PD',Anton,Impact,sans-serif` : `Anton,Impact,sans-serif`;
console.log('headline font:', PRICEDOWN ? pd[0] : 'Anton (fallback: no Pricedown in fonts/)');

const mark = (size) =>
  `<svg viewBox="0 0 120 120" fill="none" width="${size}" height="${size}">` +
  `<path d="M 52.26 25.06 A 25 25 0 1 1 45.45 26.5" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<line x1="24" y1="82" x2="116.2" y2="62.4" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>` +
  `<circle cx="59.2" cy="74.5" r="5.6" fill="currentColor"/></svg>`;

const DROP = 'drop-shadow(0 5px 0 rgba(0,0,0,.55)) drop-shadow(0 8px 18px rgba(10,4,20,.45))';
const BASE = `
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@600;700;800;900&display=block');
${PRICEDOWN ? `@font-face{font-family:'PD';src:url('${PRICEDOWN}');font-display:block}` : ''}
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1080px;overflow:hidden;color:#fff}
.s{position:relative;width:1080px;height:1080px;padding:40px 52px 36px;display:flex;flex-direction:column}
.o{paint-order:stroke fill;-webkit-text-stroke:var(--sw,12px) #000;filter:${DROP}}
h1{margin:0;font:400 var(--hs,66px)/1.02 ${HEAD};letter-spacing:.01em;text-wrap:balance}
.b{margin-top:8px;font:400 var(--bs,40px)/1.08 ${HEAD};color:#ffd166;--sw:9px;letter-spacing:.01em;text-wrap:balance}
/* With Pricedown, small B lines switch to Inter 800 (Pricedown's 1 reads as I at small sizes; same call as optA). */
${PRICEDOWN ? `.b:not(.pd){font:800 calc(var(--bs,40px) * 1.0)/1.14 Inter,sans-serif;--sw:8px;letter-spacing:-.005em}` : ''}
.spacer{flex:1}
.foot{display:flex;align-items:flex-end;gap:10px}
.handle{margin-left:auto;display:flex;gap:9px;align-items:center;font:700 22px Inter;text-shadow:0 2px 0 #000,0 0 3px #000,0 3px 12px rgba(0,0,0,.6)}
.hud{position:absolute;font-family:Inter}
`;
const page = (n, inner, css = '', foot = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${BASE}${css}</style></head>
<body style="background:url('${IMG(n)}') center/cover no-repeat #222"><div class="s">${inner}<div class="spacer"></div>
<div class="foot">${foot}<div class="handle">${mark(30)}<span>@tangentideas.ai</span></div></div></div></body></html>`;

// --- HUD pieces (our own designs) ---
const star = (s) => `<svg width="${s}" height="${s}" viewBox="0 0 100 100"><polygon points="50,6 62,38 96,38 69,59 79,93 50,72 21,93 31,59 4,38 38,38"
  fill="#ffd166" stroke="#000" stroke-width="8" stroke-linejoin="round"/><polygon points="50,20 58,42 50,38 42,42" fill="#fff" opacity=".55"/></svg>`;
const stars = `<div class="stars">${star(62).repeat(5)}</div>`;
const health = `<div class="hp"><svg width="44" height="40" viewBox="0 0 100 90"><path d="M50 86 C10 58 2 38 8 22 C16 2 42 4 50 22 C58 4 84 2 92 22 C98 38 90 58 50 86Z" fill="#ff3b3b" stroke="#000" stroke-width="9" stroke-linejoin="round"/></svg>
  <div class="bar"><div class="fill"></div></div></div>`;
const money = `<div class="money"><div class="in o">+<span class="rs">&#8377;</span> salary</div><div class="out o">&minus;<span class="rs">&#8377;</span> EMI</div></div>`;
const box = (done) => `<span class="bx">${done ? '<svg viewBox="0 0 24 24" width="26" height="26"><path d="M4 12.5l5 5L20 6" fill="none" stroke="#7CFC8A" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>' : ''}</span>`;
const cheat = `<div class="cheat"><span class="code">LEAVEMEALONE</span><span class="cur"></span></div>`;

const S = [];
// 1 cover. His head top is at ~21% (227px): headline stays above it; B line sits low-left.
S.push(page(1, `<h1 class="o" style="text-align:center">If an Indian man&rsquo;s life were GTA</h1>`,
  `.s{padding-top:30px} h1{--hs:${PRICEDOWN ? 86 : 84}px;line-height:.98;max-width:900px;margin:0 auto}
   .swipe{font:800 30px Inter;text-shadow:0 2px 0 #000,0 0 3px #000,0 3px 12px rgba(0,0,0,.6);margin-left:auto;margin-right:22px}
   .handle{margin-left:0}`,
  `<div class="b o pd" style="--bs:46px;margin:0">A Men&rsquo;s Day special</div><span class="swipe">Swipe &rarr;</span>`));
// 2 wanted level: stars top-right on the headline row
S.push(page(2, `<div class="row"><h1 class="o">Wanted level: 5&nbsp;stars.</h1>${stars}</div>
<div class="b o">Relatives asking when he&rsquo;s getting married.</div>`,
  `.row{display:flex;align-items:center;gap:20px} .row h1{--hs:62px;white-space:nowrap} .stars{margin-left:auto;display:flex;gap:2px;filter:${DROP}}
   .b{--bs:36px}`));
// 3 health
S.push(page(3, `<h1 class="o">Health: back pain at&nbsp;32.</h1><div class="b o">Resting doesn&rsquo;t fix&nbsp;it.</div>${health}`,
  `h1{--hs:68px} .hp{margin-top:18px;display:flex;align-items:center;gap:12px;filter:${DROP}}
   .bar{width:380px;height:34px;border:5px solid #000;border-radius:6px;background:rgba(40,10,20,.75);padding:3px;box-shadow:inset 0 0 0 2px rgba(255,255,255,.25)}
   .fill{width:9%;height:100%;background:linear-gradient(#ff6b6b,#d61f1f);border-radius:2px}`));
// 4 money: readout on the open left side, below the headline
S.push(page(4, `<h1 class="o">Money: salary in, EMI&nbsp;out.<br>Same minute.</h1>${money}`,
  `h1{--hs:64px;max-width:960px} .money{margin-top:22px;font:400 54px/1.08 ${HEAD};--sw:10px}
   .in{color:#5ef08a} .out{color:#ff5050} .rs{font-family:Inter,sans-serif;font-weight:900;font-size:.9em} /* display faces lack the rupee glyph */`));
// 5 side missions: B line rendered as the mission checklist (same words, split per item)
S.push(page(5, `<h1 class="o">Side missions: never&#8209;ending.</h1>
<div class="card"><div class="m">${box(true)}<span>Drop Mummy at the temple.</span></div>
<div class="m">${box(false)}<span>Pick up the gas cylinder.</span></div>
<div class="m">${box(false)}<span>Then office.</span></div></div>`,
  `h1{--hs:66px} .card{margin-top:22px;width:560px;background:rgba(14,6,24,.78);border:4px solid #000;outline:2px solid rgba(255,209,102,.9);
   border-radius:12px;padding:16px 22px;box-shadow:0 10px 30px rgba(0,0,0,.45)}
   .m{display:flex;gap:14px;align-items:center;font:800 31px/1.2 Inter;padding:8px 0}
   .bx{flex:none;width:34px;height:34px;border:3px solid #fff;border-radius:6px;display:grid;place-items:center;background:rgba(0,0,0,.35)}`));
// 6 cheat code: typed-cheat box bottom-left
S.push(page(6, `<h1 class="o">Cheat code: LEAVEMEALONE.</h1><div class="b o">Doesn&rsquo;t work at home.</div>`,
  `h1{--hs:64px;white-space:nowrap}
   .cheat{display:flex;align-items:center;gap:6px;background:rgba(8,4,14,.82);border:3px solid #000;outline:2px solid rgba(255,255,255,.55);
   border-radius:8px;padding:12px 18px;font:800 30px 'Inter';letter-spacing:.14em;color:#7CFC8A;text-shadow:0 0 10px rgba(124,252,138,.5)}
   .cur{display:inline-block;width:16px;height:30px;background:#7CFC8A;margin-left:2px}`,
  cheat));
// 7 closer
S.push(page(7, `<h1 class="o">Life on hard mode.</h1><div class="b2 o">Happy Men&rsquo;s Day to every man still&nbsp;playing.</div>`,
  `h1{--hs:76px} .b2{margin-top:6px;max-width:820px;font:400 54px/1.04 ${HEAD};--sw:10px;letter-spacing:.01em;text-wrap:balance}`));
// 8 maker card
S.push(page(8, `<div class="card"><div class="ct o">Made with AI by a guy who should be playing GTA&nbsp;6 right&nbsp;now.</div>
<div class="cs">Follow for more art, apps and stories.</div>
<div class="rows"><div><span>Instagram</span>@tangentideas.ai</div><div><span>YouTube</span>@tangentideasai</div>
<div><span>Medium</span>@tangentideasai</div><div><span>Web</span>tangentideas.ai</div></div></div>`,
  `.card{margin:70px auto 0;width:860px;background:rgba(26,15,34,.86);border:3px solid #ffd166;border-radius:14px;padding:42px 52px}
   .ct{font:400 58px/1.04 ${HEAD};--sw:10px;text-wrap:balance;letter-spacing:.01em} .cs{margin-top:16px;font:700 32px/1.3 Inter;color:#ffd166}
   .rows{margin-top:26px;display:grid;gap:10px;font:600 30px Inter} .rows span{display:inline-block;width:190px;color:#c9b8d8}
   .handle{display:none}`));

const browser = await chromium.launch();
const pg = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
const report = [];
for (let i = 0; i < S.length; i++) {
  const id = String(i + 1).padStart(2, '0');
  const f = path.join(HTML, `slide-${id}.html`);
  fs.writeFileSync(f, S[i]);
  await pg.goto('file://' + f, { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  // overflow check: any element extending past the 1080 frame or its own box
  const issues = await pg.evaluate(() => {
    const out = [];
    for (const el of document.querySelectorAll('.s *')) {
      const r = el.getBoundingClientRect();
      if (r.width && (r.right > 1080 || r.bottom > 1080 || r.left < 0 || r.top < 0)) out.push(`${el.className || el.tagName} out of frame`);
      if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow !== 'visible') out.push(`${el.className} overflows`);
    }
    const s = document.querySelector('.s');
    if (s.scrollHeight > 1080) out.push('content taller than frame');
    return out;
  });
  if (issues.length) report.push(`slide ${id}: ${issues.join('; ')}`);
  await pg.screenshot({ path: path.join(OUT, `slide-${id}.png`) });
}
await browser.close();
console.log(report.length ? report.join('\n') : 'overflow check: clean');
// contact sheet (4x2, 540px tiles) via ffmpeg
const inputs = S.flatMap((_, i) => ['-i', path.join(OUT, `slide-${String(i + 1).padStart(2, '0')}.png`)]);
const scale = S.map((_, i) => `[${i}:v]scale=540:540[v${i}]`).join(';');
const layout = S.map((_, i) => `${(i % 4) * 540}_${Math.floor(i / 4) * 540}`).join('|');
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...inputs, '-filter_complex',
  `${scale};${S.map((_, i) => `[v${i}]`).join('')}xstack=inputs=${S.length}:layout=${layout}`, '-q:v', '3',
  path.join(ROOT, 'contact-sheet.jpg')]);
console.log(`rendered ${S.length} slides to ${OUT} + contact-sheet.jpg`);
