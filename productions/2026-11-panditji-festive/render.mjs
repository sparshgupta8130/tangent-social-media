// Render a reel page to PNG frames with the installed Chrome.
// node render.mjs <page.html> <outDir> frames <seconds> [fps]      -> f0000.png …
// node render.mjs <page.html> <outDir> stills <t1> <t2> …          -> t1.00.png …
// Needs playwright-core (any 1.5x) and the page served at http://127.0.0.1:8766/.
import { chromium } from 'playwright-core';
import { mkdirSync } from 'node:fs';

const [, , pageName, out, mode, ...rest] = process.argv;
mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ executablePath: process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe', args: ['--force-color-profile=srgb', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
const errs = [];
page.on('pageerror', (e) => errs.push(e.message));
page.on('console', (m) => m.type() === 'error' && errs.push(m.text()));
await page.goto(`http://127.0.0.1:8766/${pageName}`, { waitUntil: 'networkidle' });
await page.evaluate(() => window.ready);
await page.waitForTimeout(300);
const fps = Number(rest[1] || 30);
// frames mode takes an optional [from, to) frame range, to re-render part of a reel
const from = Number(rest[2] || 0), to = Number(rest[3] || Math.round(Number(rest[0]) * fps));
const list = mode === 'frames' ? Array.from({ length: to - from }, (_, i) => (from + i) / fps) : rest.map(Number);
const stage = await page.$('#stage');
for (const [i, t] of list.entries()) {
  await page.evaluate((t) => window.render(t), t);
  const name = mode === 'frames' ? `f${String(from + i).padStart(4, '0')}.png` : `t${t.toFixed(2)}.png`;
  await stage.screenshot({ path: `${out}/${name}`, type: 'png' });
}
await browser.close();
if (errs.length) console.log('ERRORS', errs);
console.log('rendered', list.length);
