// Renders short.html frame by frame (render(t)) to PNGs, for ffmpeg.
// Usage: node render_video.js <short.html> <framesDir> [fps] [onlyTimesCSV]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out, fpsArg = '30', only] = process.argv.slice(2);
  const fps = Number(fpsArg);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(src), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const total = await page.evaluate(() => window.TOTAL);
  const times = only ? only.split(',').map(Number) : Array.from({ length: Math.round(total * fps) }, (_, i) => i / fps);
  for (let i = 0; i < times.length; i++) {
    await page.evaluate(t => window.render(t), times[i]);
    const name = only ? `t${times[i]}.png` : `f${String(i).padStart(5, '0')}.png`;
    await page.screenshot({ path: path.join(out, name) });
  }
  console.log('frames', times.length, 'total', total);
  await browser.close();
})();
