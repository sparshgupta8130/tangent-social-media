// Renders each <section class="slide"> in slides.html to a 1080x1350 PNG.
// Usage: node render.js <slides.html> <outdir> [scale]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out, scale = '1'] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: Number(scale) });
  await page.goto('file://' + path.resolve(src), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const ids = await page.$$eval('section.slide', els => els.map(e => e.id));
  for (const id of ids) {
    const n = id.replace('s', '').padStart(2, '0');
    await page.locator('#' + id).screenshot({ path: path.join(out, `panditji-${n}.png`) });
  }
  const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family));
  console.log('rendered', ids.length, 'fonts loaded:', [...new Set(fonts)].join(', '));
  await browser.close();
})();
