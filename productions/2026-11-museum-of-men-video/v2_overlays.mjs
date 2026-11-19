// v2 (Flow): render every text layer and every chat-screen state as transparent PNGs (Playwright + Google Fonts).
// Usage: node v2_overlays.mjs   -> work/v2/overlays/{v,p}/*.png and work/v2/overlays/chat/*.png
// Copy is VERBATIM from ../2026-11-museum-of-men/carousel.md (only line breaks at sentence ends are added).
// Typography = the carousel (build_square.mjs): Fraunces headlines, Inter small-caps label, ink #1d1a16, muted #7a6650.
// Chat styling = build_square.mjs PHONE_CSS, scaled to the screen of the phone in slide-08.png.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(ROOT, 'work', 'v2', 'overlays');
const INK = '#1d1a16', MUTED = '#7a6650';

const EXHIBITS = [
  [1, 'The cable drawer', 'Chargers for phones nobody has used in years.<br>Just in case.'],
  [2, 'The phone box', 'He kept his phone&rsquo;s box, to sell the phone one day.'],
  [3, 'The mystery keys', 'Nobody knows what these keys open.<br>Nobody can throw them away.'],
  [4, 'His chappals', 'His chappals are twelve years old.<br>He says they&rsquo;re still fine.'],
  [5, 'The T-shirt', 'His college T-shirt became his gym T-shirt.<br>Next, a car cloth.'],
  [6, 'The remote', 'The TV remote is still in its plastic cover.<br>The TV is nine years old.'],
];

// v = 9:16 master (text below the top 220 px, above the bottom 380 px); p = 4:5.
const F = {
  v: { w: 1080, h: 1920, padT: 262, padX: 84, lbl: 30, h1: 76, title: 116, sub: 60, titleT: 240,
       close: 66, csub: 36, closeT: 232, wallT: 300, wall: 84, cardT: 56, cardS: 1.06 },
  p: { w: 1080, h: 1350, padT: 72, padX: 80, lbl: 27, h1: 68, title: 108, sub: 56, titleT: 100,
       close: 60, csub: 32, closeT: 66, wallT: 96, wall: 72, cardT: 50, cardS: 1.0 },
};

const css = (g) => `
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=block');
*{box-sizing:border-box}
html,body{margin:0;width:${g.w}px;height:${g.h}px;overflow:hidden;background:transparent;color:${INK}}
.wrap{position:absolute;left:${g.padX}px;right:${g.padX}px;top:${g.padT}px}
.lbl{font:600 ${g.lbl}px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
h1{margin:18px 0 0;max-width:920px;font:400 ${g.h1}px/1.13 Fraunces,Georgia,serif;letter-spacing:-.012em;text-wrap:pretty}
.ghost{visibility:hidden}
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
  // exhibit 7: the label is its own layer so it stays solid while the headline crossfades
  L.ex7lbl = doc(g, `<div class="wrap"><div class="lbl">Exhibit 7 &middot; His phone</div><h1 class="ghost">What he typed.</h1></div>`);
  L.ex7typed = doc(g, `<div class="wrap"><div class="lbl ghost">Exhibit 7 &middot; His phone</div><h1>What he typed.</h1></div>`);
  L.ex7sent = doc(g, `<div class="wrap"><div class="lbl ghost">Exhibit 7 &middot; His phone</div><h1>What he sent.</h1></div>`);
  // the row's wall is short (the new row image starts ~y 530 of 1920): the close sits high, inside the safe area
  L.close = doc(g, `<div class="wrap dark sh" style="top:${g.closeT}px"><h1 style="font-size:${g.close}px;margin-top:0">Some things men keep are worth throwing out.<br>Start with &ldquo;All good, bro.&rdquo;</h1>
    <div style="margin-top:14px;font:500 ${g.csub}px/1.3 Inter;color:#f3e6d2;text-shadow:0 2px 12px rgba(0,0,0,.45)">Today, ask one how he&rsquo;s really doing.</div></div>`);
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
</div>`, `.wall{position:absolute;left:0;right:0;top:${g.wallT}px;text-align:center;font:400 ${g.wall}px/1.08 Fraunces,Georgia,serif;letter-spacing:-.01em;color:#2a241d}
.card{position:absolute;left:50%;top:${g.wallT + g.wall * 2.16 + g.cardT}px;width:820px;transform:translateX(-50%) scale(${g.cardS});transform-origin:top center;
  background:#fbfaf7;border-radius:6px;padding:56px 60px 44px;box-shadow:0 18px 50px rgba(60,45,30,.18),0 2px 6px rgba(60,45,30,.10)}
.cl{font:600 24px Inter;letter-spacing:.14em;text-transform:uppercase;color:${MUTED}}
.ct{margin-top:18px;font:400 58px/1.12 Fraunces,Georgia,serif;letter-spacing:-.01em;text-wrap:balance}
.cs{margin-top:18px;font:400 36px/1.25 Fraunces,Georgia,serif;color:#3a332b}
.rule{height:1px;background:#d9d2c6;margin:36px 0 26px}
.rows{display:grid;gap:14px;font:500 30px Inter}
.rows span{display:inline-block;width:190px;color:${MUTED};font-weight:500}`);
  return L;
};

// ---- the chat screen. Phone screen in slide-08.png = x 848-1008, y 1155-1486 (160 x 331 source px).
// CSS scale = the carousel's (1080/560 = 1.9286 CSS px per source px) so PHONE_CSS applies unchanged.
const S8 = 1080 / 560;
const SW = Math.round(160 * S8), SH = Math.round(331 * S8);           // 309 x 638 CSS px
const DSF = 2.2;                                                     // -> 680 x 1404 px PNGs
const NOTCH = { x: (886 - 848) * S8, w: (971 - 886) * S8, h: (1167 - 1155) * S8 };
const PHONE_CSS = `
.scr{position:absolute;left:0;top:0;width:${SW}px;height:${SH}px;border-radius:34px;overflow:hidden;
  background:#efeae2;display:flex;flex-direction:column;font-family:Inter;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}
.scr:after{content:"";position:absolute;inset:0;background:linear-gradient(155deg,rgba(255,255,255,.22),rgba(255,255,255,0) 45%);pointer-events:none}
.notch{position:absolute;left:${NOTCH.x}px;top:0;width:${NOTCH.w}px;height:${NOTCH.h}px;background:#121212;border-radius:0 0 14px 14px;z-index:3}
.hd{display:flex;gap:12px;align-items:center;padding:34px 14px 12px;background:#f7f5f1;border-bottom:1px solid #ddd6cb}
.av{width:38px;height:38px;border-radius:50%;background:#9db7a8;color:#fff;font:600 19px Inter;display:grid;place-items:center}
.nm{font:600 20px Inter;color:#1d1a16} .st{font:400 14px Inter;color:#6f8f7c}
.body{flex:1;padding:16px 12px;display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.in{display:inline-block;background:#fff;border-radius:4px 16px 16px 16px;padding:10px 15px;font:400 22px/1.3 Inter;color:#1d1a16;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.out{align-self:flex-end;background:#d9f2c9;border-radius:16px 4px 16px 16px;padding:10px 14px;font:500 24px/1.3 Inter;color:#1d1a16;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.tk{margin-left:8px;font-size:15px;color:#4f9fd6;letter-spacing:-3px}
.bar{display:flex;gap:8px;align-items:flex-end;padding:10px 10px 22px}
.draft{flex:1;background:#fff;border-radius:22px;padding:12px 15px;font:500 26px/1.25 Inter;color:#1d1a16}
.draft.empty{color:#a39c92;font-weight:400}
.cur{display:inline-block;width:3px;height:28px;margin-left:2px;vertical-align:-4px;background:#2f7d5b}
.cur.off{opacity:0}
.send{width:46px;height:46px;border-radius:50%;background:#c9c3b9;color:#fff;font-size:20px;display:grid;place-items:center}
.send.press{background:#9d968b;transform:scale(.9)}`;

const DRAFT1 = 'Honestly bro, I’m not doing good.';
const DRAFT2 = ['A', 'l', 'l', ' ', 'g', 'o', 'o', 'd', ',', ' ', 'b', 'r', 'o', ' ', '\u{1F44D}'];
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/’/g, '&rsquo;');
const hdr = `<div class="hd"><div class="av">R</div><div><div class="nm">Rahul</div><div class="st">online</div></div></div>`;
const incoming = `<div class="in">How are you, bro? 🙂</div>`;
const chat = ({ bubble = true, text = '', cursor = true, sent = false, press = false }) => {
  const draft = text ? `<div class="draft">${esc(text)}<span class="cur${cursor ? '' : ' off'}"></span></div>`
    : `<div class="draft empty">Message<span class="cur${cursor ? '' : ' off'}"></span></div>`;
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=block');
*{box-sizing:border-box} html,body{margin:0;width:${SW}px;height:${SH}px;background:transparent;overflow:hidden}
${PHONE_CSS}</style></head><body><div class="scr"><div class="notch"></div>${hdr}
  <div class="body">${bubble ? incoming : ''}${sent ? '<div class="out">All good, bro 👍<span class="tk">&#10003;&#10003;</span></div>' : ''}</div>
  <div class="bar">${draft}<div class="send${press ? ' press' : ''}">&#10148;</div></div>
</div></body></html>`;
};

const states = {};
states['a00-1'] = chat({ bubble: false });
for (let n = 0; n <= DRAFT1.length; n++) for (const c of [0, 1])
  states[`b${String(n).padStart(2, '0')}-${c}`] = chat({ text: DRAFT1.slice(0, n), cursor: !!c });
for (let n = 1; n <= DRAFT2.length; n++)
  states[`c${String(n).padStart(2, '0')}-1`] = chat({ text: DRAFT2.slice(0, n).join('') });
states.press = chat({ text: DRAFT2.join(''), press: true });
for (const c of [0, 1]) states[`sent-${c}`] = chat({ sent: true, cursor: !!c });

const shoot = async (pg, dir, name, html) => {
  const f = path.join(dir, `${name}.html`); fs.writeFileSync(f, html);
  await pg.goto('file://' + f, { waitUntil: 'networkidle' }); await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: path.join(dir, `${name}.png`), omitBackground: true });
};

const browser = await chromium.launch();
for (const k of Object.keys(F)) {
  const dir = path.join(OUT, k); fs.mkdirSync(dir, { recursive: true });
  const pg = await browser.newPage({ viewport: { width: F[k].w, height: F[k].h }, deviceScaleFactor: 1 });
  for (const [name, html] of Object.entries(layers(k))) await shoot(pg, dir, name, html);
  await pg.close();
}
const cdir = path.join(OUT, 'chat'); fs.mkdirSync(cdir, { recursive: true });
const cp = await browser.newPage({ viewport: { width: SW, height: SH }, deviceScaleFactor: DSF });
for (const [name, html] of Object.entries(states)) await shoot(cp, cdir, name, html);
fs.writeFileSync(path.join(cdir, 'geom.json'), JSON.stringify({ src_rect: [848, 1155, 1008, 1486], css: [SW, SH], dsf: DSF }));
await browser.close();
console.log('v2 overlays done:', Object.keys(states).length, 'chat states');
