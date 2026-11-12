// Ask screen, live build, with a SAMPLE conversation: /api/agent is mocked. The first turn asks for real engine
// tools (the app computes Asha's actual chart values and draws its own "Because" badges); the reply text is a
// written sample. The two refusals use the server's real canned replies (api/_lib/guard.ts).
import { createRequire } from 'node:module';
const require = createRequire('/home/user/panditji/package.json');
const { chromium } = require('playwright');
const out = process.argv[2];
const now = Date.now();
const TODAY = new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(now));
const person = (id, name, relation, date, time, gender) => ({ id, name, relation, gender,
  birth: { date, time, timeKnown: true, place: { name: 'Delhi', admin1: 'Delhi', country: 'India', lat: 28.6139, lon: 77.209, timeZone: 'Asia/Kolkata' },
    utc: new Date(`${date}T${time}:00+05:30`).toISOString() }, createdAt: now, updatedAt: now });
const fixture = { schemaVersion: 2,
  settings: { lang: 'en', tradition: 'vedic', theme: 'light', textSize: 'normal', westernHouseSystem: 'placidus', ayanamsa: 'lahiri', nodeType: 'mean',
    monthScheme: 'purnimanta', panchangTimeModel: 'drik', alerts: { enabled: false, cadencePerWeek: 3 }, onboarded: true, mascot: 'male',
    ageVerifiedAt: now, ageAttestVersion: 1, aiConsentAt: now, aiConsentProvider: 'gemini' },
  people: [person('self', 'Asha', 'self', '1990-06-15', '09:30', 'female'), person('p1', 'Rohan', 'partner', '1988-11-02', '21:15', 'male')],
  selfId: 'self', currentPlace: null, intents: [], streak: { count: 7, best: 12, lastDay: TODAY }, ritual: { day: TODAY, done: ['reading'] },
  tours: { today: 1, timing: 1, ask: 1, chart: 1, you: 1 } };

const REPLY = [
  'This is a season for building, Asha, not for rushing.\n\n',
  'You are in your Saturn Mahadasha, a nineteen-year chapter that rewards steady, patient work, ',
  'and Jupiter\'s sub-period inside it runs until March 2029. Saturn sits strong in its own sign in your chart, ',
  'so effort you put in now tends to last.\n\n',
  'Use this year to deepen your skills and plan your next step. A leap made in haste is the one to avoid.',
];
const DEATH = 'I never predict death or how long anyone will live — no chart can say that, and I would not frighten you. Ask me about the chapters ahead in your chart instead.';
const COIN = 'I do not name stocks, coins or funds — please speak to a qualified adviser for that. What your chart says about your money cycles, I am glad to share.';
const sse = events => events.map(e => `data: ${JSON.stringify(e)}\n\n`).join('');

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'en-IN', timezoneId: 'Asia/Kolkata' });
await ctx.route('**/api/**', async route => {
  const url = route.request().url();
  if (url.includes('/api/access')) return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ ok: true, label: 'sample', quota: { questions: { used: 2, limit: 25 }, readings: { used: 0, limit: 3 } }, ai: 'gemini' }) });
  if (url.includes('/api/title')) {
    const q = route.request().postData() || '';
    return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ title: /die|coin/i.test(q) ? 'Questions I Turn Down' : 'Asha’s Career This Year' }) });
  }
  if (url.includes('/api/agent')) {
    const body = route.request().postData() || '';
    let events;
    if (/When will I die/.test(body) && !/crypto/.test(body)) events = [{ type: 'deflected', reason: 'death' }, { type: 'text', text: DEATH }, { type: 'done', finish: 'stop' }];
    else if (/crypto/.test(body)) events = [{ type: 'deflected', reason: 'finance' }, { type: 'text', text: COIN }, { type: 'done', finish: 'stop' }];
    else if (!/toolResult/.test(body)) { await new Promise(r => setTimeout(r, 3500)); events = [
      { type: 'toolCall', name: 'get_dasha_at', args: { personId: 'self', date: TODAY }, id: 'call_dasha' },
      { type: 'toolCall', name: 'get_chart', args: { personId: 'self' }, id: 'call_chart' },
      { type: 'done', finish: 'stop' }]; }
    else events = [...REPLY.map(text => ({ type: 'text', text })), { type: 'done', finish: 'stop' }];
    return route.fulfill({ status: 200, headers: { 'content-type': 'text/event-stream' }, body: sse(events) });
  }
  return route.fulfill({ status: 503, body: '{"error":"offline"}' });
});
await ctx.addInitScript(d => { localStorage.setItem('panditji:v2', JSON.stringify(d)); localStorage.setItem('panditji:access', 'ABCD-EFGH'); }, fixture);
const page = await ctx.newPage();
await page.goto('http://localhost:4173', { waitUntil: 'networkidle' });
await page.waitForTimeout(900);
await page.locator('nav[aria-label] button', { hasText: 'Ask' }).first().click({ force: true });
await page.waitForTimeout(1200);
await page.screenshot({ path: `${out}/ask-empty.png` });
const ask = async (q) => {
  const box = page.locator('textarea, input[type="text"]').last();
  await box.fill(q);
  await page.waitForTimeout(200);
  await page.getByRole('button', { name: 'Send', exact: true }).click({ force: true });
  await page.waitForTimeout(2500);
};
const toTop = () => page.evaluate(() => { document.querySelectorAll('*').forEach(el => { if (el.scrollHeight > el.clientHeight + 4) el.scrollTop = 0; }); window.scrollTo(0, 0); });
{
  const box = page.locator('textarea, input[type="text"]').last();
  await box.fill('What does my chart say about my career this year?');
  await page.getByRole('button', { name: 'Send', exact: true }).click({ force: true });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: out + "/ask-thinking.png" });
  await page.waitForTimeout(5000);
  await toTop(); await page.waitForTimeout(400);
  await page.screenshot({ path: out + "/ask-career.png" });
}
// a new conversation for the refusals
const plus = page.getByRole('button', { name: /new|plus|start/i }).first();
if (await plus.count()) { await plus.click({ force: true }); await page.waitForTimeout(800); }
await ask('When will I die?');
await ask('Tell me which crypto coin will 10x this year.');
await toTop(); await page.waitForTimeout(400);
await page.screenshot({ path: `${out}/ask-limits-live.png` });
console.log('done');
await browser.close();
