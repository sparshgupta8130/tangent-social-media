// Real app captures for the launch video: full-length pages (tab bar hidden) + the tab bar alone.
import { createRequire } from 'node:module';
const require = createRequire('/home/user/panditji/package.json');
const { chromium } = require('playwright');
const out = process.argv[2];
const now = Date.now();
const TODAY = new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(now));
const person = (id, name, relation, date, time, gender) => ({ id, name, relation, gender,
  birth: { date, time, timeKnown: true, place: { name: 'Delhi', admin1: 'Delhi', country: 'India', lat: 28.6139, lon: 77.209, timeZone: 'Asia/Kolkata' },
    utc: new Date(`${date}T${time}:00+05:30`).toISOString() }, createdAt: now, updatedAt: now });
const fixture = (tradition) => ({ schemaVersion: 2,
  settings: { lang: 'en', tradition, theme: 'light', textSize: 'normal', westernHouseSystem: 'placidus', ayanamsa: 'lahiri', nodeType: 'mean',
    monthScheme: 'purnimanta', panchangTimeModel: 'drik', alerts: { enabled: false, cadencePerWeek: 3 }, onboarded: true, mascot: 'male',
    ageVerifiedAt: now, ageAttestVersion: 1 },
  people: [person('self', 'Asha', 'self', '1990-06-15', '09:30', 'female'), person('p1', 'Rohan', 'partner', '1988-11-02', '21:15', 'male')],
  selfId: 'self', currentPlace: null, intents: [], streak: { count: 7, best: 12, lastDay: TODAY }, ritual: { day: TODAY, done: ['reading'] },
  tours: { today: 1, timing: 1, ask: 1, chart: 1, you: 1 } });
const browser = await chromium.launch();
async function session(t) {
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'en-IN', timezoneId: 'Asia/Kolkata' });
  await ctx.route('**/api/**', r => r.fulfill({ status: 503, body: '{"error":"offline"}' }));
  await ctx.addInitScript(d => { localStorage.setItem('panditji:v2', JSON.stringify(d)); localStorage.setItem('panditji:access', 'ABCD-EFGH'); }, fixture(t));
  const page = await ctx.newPage();
  await page.goto('http://localhost:4173', { waitUntil: 'networkidle' });
  await page.waitForTimeout(900);
  return { ctx, page };
}
const tab = async (page, name) => { await page.locator('nav[aria-label] button', { hasText: name }).first().click({ force: true }); await page.waitForTimeout(1300); };
const full = async (page, name) => {
  await page.addStyleTag({ content: 'nav[aria-label]{visibility:hidden !important}' });
  await page.screenshot({ path: `${out}/${name}.png`, fullPage: true });
  await page.addStyleTag({ content: 'nav[aria-label]{visibility:visible !important}' });
  console.log('full', name);
};
{ const { ctx, page } = await session('vedic');
  const nav = page.locator('nav[aria-label]').first();
  await nav.screenshot({ path: `${out}/nav-today.png` });
  await full(page, 'today');
  await tab(page, 'Plan'); await nav.screenshot({ path: `${out}/nav-plan.png` }); await full(page, 'plan');
  await tab(page, 'Chart'); await nav.screenshot({ path: `${out}/nav-chart.png` }); await full(page, 'chart-vedic');
  await tab(page, 'Ask'); await nav.screenshot({ path: `${out}/nav-ask.png` });
  await tab(page, 'Plan');
  await page.getByRole('radio', { name: 'Match' }).or(page.getByRole('tab', { name: 'Match' })).or(page.getByRole('button', { name: 'Match', exact: true })).first().click({ force: true });
  await page.waitForTimeout(700);
  await page.getByRole('button', { name: /Asha \(you\)/ }).first().click({ force: true });
  await page.getByRole('button', { name: /^Rohan/ }).last().click({ force: true });
  await page.waitForTimeout(300);
  await page.getByRole('button', { name: 'Match these two' }).click({ force: true });
  await page.waitForTimeout(2000);
  await full(page, 'match');
  await ctx.close(); }
{ const { ctx, page } = await session('western');
  await tab(page, 'Chart'); await full(page, 'chart-western');
  await ctx.close(); }
await browser.close();
