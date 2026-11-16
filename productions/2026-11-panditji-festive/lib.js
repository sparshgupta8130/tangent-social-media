// Shared helpers for the festive reels: easing, placement, the Panditji rig, a diya, fireworks, petals.
// The mascot is the male / traditional look from panditji/src/ui/Panditji.tsx, same paths and colours,
// split into parts so the reel can blink him, tilt his head and swap poses on the beat.

const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const eOut = (x) => 1 - Math.pow(1 - x, 3);
const eIn = (x) => x * x * x;
const eIO = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
const eBack = (x) => { const c1 = 1.9, c3 = c1 + 1; return x <= 0 ? 0 : 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
const eSpring = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.exp(-6 * x) * Math.cos(11 * x));
const lerp = (a, b, x) => a + (b - a) * x;
function rnd(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }
const $ = (id) => document.getElementById(id);

/** Position an absolutely placed element: x/y is its top-left; scale and rotation about its transform-origin. */
function place(el, { x = 0, y = 0, s = 1, sx, sy, r = 0, o = 1, filter = '' }) {
  el.style.transform = `translate(${x}px, ${y}px) rotate(${r}deg) scale(${sx ?? s}, ${sy ?? s})`;
  el.style.opacity = clamp(o);
  el.style.filter = filter || 'none';
  el.style.visibility = o <= 0.001 ? 'hidden' : 'visible';
}
/** Centre a text block horizontally at its natural width. */
function centreX(el, W) { return (W - el.offsetWidth) / 2; }

// ------------------------------------------------------------------ Panditji
const C = {
  skin: '#e9b482', skinDark: '#c98d58', kurta: '#ff9933', kurtaDark: '#e07c1a', shawl: '#fff3dc', shawlEdge: '#d9a23a',
  hair: '#3d2b28', hairLight: '#5a4541', bead: '#8a4b2a', beadLight: '#b06a3f', gold: '#ffd166', ink: '#2b2140',
  white: '#ffffff', cheek: '#ff7aa2', tilak: '#e8402f', tilakWhite: '#fff8ec',
};
const ARM = `stroke="${C.kurta}" stroke-width="18" stroke-linecap="round" fill="none"`;
const EDGE = `stroke="${C.kurtaDark}" stroke-width="21" stroke-linecap="round" fill="none"`;
const arm = (d) => `<path d="${d}" ${EDGE}/><path d="${d}" ${ARM}/>`;
const hand = (x, y, r = 10) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${C.skin}"/>`;

function mascotMarkup(id) {
  const mala = Array.from({ length: 9 }, (_, i) => {
    const a = Math.PI * (0.12 + (0.76 * i) / 8);
    return `<circle cx="${(100 + 26 * Math.cos(a)).toFixed(1)}" cy="${(132 + 22 * Math.sin(a)).toFixed(1)}" r="3.2"/>`;
  }).join('');
  const star = 'M0-7 2 -2 7 0 2 2 0 7 -2 2 -7 0 -2-2z';
  return `<svg viewBox="0 0 200 200" width="100%" height="100%" overflow="visible" xmlns="http://www.w3.org/2000/svg">
  <g>
    <path d="M100 118c-34 0-54 24-54 54 0 10 4 16 12 16h84c8 0 12-6 12-16 0-30-20-54-54-54z" fill="${C.kurta}"/>
    <path d="M58 180c6-6 18-10 42-10s36 4 42 10v8H58z" fill="${C.kurtaDark}" opacity="0.35"/>
    <path d="M62 150c10-12 24-18 38-18v56H54c-4-14-2-28 8-38z" fill="${C.shawl}"/>
    <path d="M100 132v56M62 150c10-12 24-18 38-18" stroke="${C.shawlEdge}" stroke-width="2.5" fill="none"/>
    <g fill="${C.bead}" stroke="${C.beadLight}" stroke-width="1">${mala}</g>
    <g id="${id}-armsDown">${arm('M62 150q-12 10-10 26')}${arm('M138 150q12 10 10 26')}${hand(52, 178)}${hand(148, 178)}</g>
    <g id="${id}-armsUp">${arm('M62 148q-14-16-16-36')}${arm('M138 148q14-16 16-36')}${hand(45, 108)}${hand(155, 108)}</g>
    <g id="${id}-armsWave">${arm('M62 150q-12 10-10 26')}${hand(52, 178)}<g id="${id}-waveArm">${arm('M138 148q14-16 16-36')}${hand(155, 108)}</g></g>
    <g id="${id}-armsNamaste">${arm('M58 150q10 10 30 8')}${arm('M142 150q-10 10-30 8')}</g>
    <g id="${id}-armsChin">${arm('M62 150q-12 10-10 26')}${hand(52, 178)}</g>
    <rect x="88" y="118" width="24" height="18" rx="8" fill="${C.skinDark}"/>
    <g id="${id}-head">
      <path d="M44 88c-5 12-4 26 4 38 6 3 11 0 12-6-4-10-5-21-3-32-5-2-9-2-13 0z" fill="${C.hair}"/>
      <path d="M156 88c5 12 4 26-4 38-6 3-11 0-12-6 4-10 5-21 3-32 5-2 9-2 13 0z" fill="${C.hair}"/>
      <path d="M106 48c-3-9 1-18 9-22 1 6 4 10 9 13-5 2-8 7-9 13-4-1-7-2-9-4z" fill="${C.hair}"/>
      <path d="M113 34c4 3 7 5 10 6" stroke="${C.hairLight}" stroke-width="2" stroke-linecap="round" fill="none"/>
      <path d="M104 49l12-3" stroke="${C.gold}" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="100" cy="96" r="54" fill="${C.skin}"/>
      <circle cx="46" cy="100" r="9" fill="${C.skin}"/><circle cx="154" cy="100" r="9" fill="${C.skin}"/>
      <circle cx="46" cy="100" r="4" fill="${C.skinDark}" opacity="0.5"/><circle cx="154" cy="100" r="4" fill="${C.skinDark}" opacity="0.5"/>
      <circle id="${id}-cheekL" cx="62" cy="112" r="8" fill="${C.cheek}" opacity="0.32"/><circle id="${id}-cheekR" cx="138" cy="112" r="8" fill="${C.cheek}" opacity="0.32"/>
      <path d="M88 58v12c0 9 24 9 24 0V58" stroke="${C.tilakWhite}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
      <path d="M100 55v22" stroke="${C.tilak}" stroke-width="4.5" stroke-linecap="round"/>
      <g stroke="${C.ink}" stroke-width="4.5" stroke-linecap="round" fill="none">
        <g id="${id}-browsNormal"><path d="M66 76q12-6 24 0"/><path d="M110 76q12-6 24 0"/></g>
        <g id="${id}-browsUp"><path d="M66 72q12-8 24-2"/><path d="M110 70q12-6 24 2"/></g>
        <g id="${id}-browsThink"><path d="M66 74q12-6 24 0"/><path d="M110 68q12-7 24-1"/></g>
      </g>
      <g id="${id}-eyesOpen">
        <ellipse cx="78" cy="94" rx="12.5" ry="14" fill="${C.white}"/><ellipse cx="122" cy="94" rx="12.5" ry="14" fill="${C.white}"/>
        <g id="${id}-pupils"><circle cx="80" cy="96" r="6.5" fill="${C.ink}"/><circle cx="124" cy="96" r="6.5" fill="${C.ink}"/>
        <circle cx="83" cy="93" r="2.3" fill="${C.white}"/><circle cx="127" cy="93" r="2.3" fill="${C.white}"/></g>
        <g id="${id}-lids"><ellipse cx="78" cy="94" rx="13.5" ry="15" fill="${C.skin}"/><ellipse cx="122" cy="94" rx="13.5" ry="15" fill="${C.skin}"/></g>
      </g>
      <g id="${id}-eyesHappy" stroke="${C.ink}" stroke-width="4.5" stroke-linecap="round" fill="none"><path d="M66 97q12-13 24 0"/><path d="M110 97q12-13 24 0"/></g>
      <g stroke="${C.ink}" stroke-width="3.5" fill="none">
        <circle cx="78" cy="94" r="17"/><circle cx="122" cy="94" r="17"/><path d="M95 92h10"/><path d="M61 92l-8-4M139 92l8-4"/>
      </g>
      <path d="M96 104q4 6 8 0" stroke="${C.skinDark}" stroke-width="3.5" stroke-linecap="round" fill="none"/>
      <path d="M84 113q8-6 16 0 8-6 16 0" stroke="${C.hair}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
      <path id="${id}-mouthSmile" d="M84 118q16 14 32 0" stroke="${C.ink}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
      <g id="${id}-mouthOpen"><path d="M82 118q18 22 36 0z" fill="${C.ink}"/><path d="M90 126q10 8 20 0 -4 7-10 7t-10-7z" fill="#ff8aa8"/></g>
      <ellipse id="${id}-mouthO" cx="100" cy="124" rx="6" ry="7.5" fill="${C.ink}"/>
      <path id="${id}-mouthSmall" d="M94 122q6 4 12 1" stroke="${C.ink}" stroke-width="4" stroke-linecap="round" fill="none"/>
    </g>
    <g id="${id}-handsNamaste">
      <path d="M100 140q-11 6-11 22 0 9 11 11 11-2 11-11 0-16-11-22z" fill="${C.skin}" stroke="${C.skinDark}" stroke-width="2"/>
      <path d="M100 142v29" stroke="${C.skinDark}" stroke-width="2" stroke-linecap="round"/>
    </g>
    <g id="${id}-handsChin">${arm('M140 156q6-16-16-26')}${hand(121, 130, 10.5)}${hand(113, 128, 4)}</g>
  </g>
  <g id="${id}-sparkles" fill="${C.gold}">
    <path id="${id}-sp0" d="${star}"/><path id="${id}-sp1" d="${star}"/><path id="${id}-sp2" d="${star}"/><path id="${id}-sp3" d="${star}"/>
  </g>
</svg>`;
}

/**
 * makeMascot(el) -> set(state). state: { arms: down|up|wave|namaste|chin, eyes: open|happy, brows: normal|up|think,
 * mouth: smile|open|o|small, px, py (pupil offset), blink 0..1, tilt (deg), sparkle 0..1, t (time, for twinkles) }
 */
function makeMascot(el, id) {
  el.innerHTML = mascotMarkup(id);
  const g = (k) => document.getElementById(`${id}-${k}`);
  const groups = {
    arms: { down: g('armsDown'), up: g('armsUp'), wave: g('armsWave'), namaste: [g('armsNamaste'), g('handsNamaste')], chin: [g('armsChin'), g('handsChin')] },
    eyes: { open: g('eyesOpen'), happy: g('eyesHappy') },
    brows: { normal: g('browsNormal'), up: g('browsUp'), think: g('browsThink') },
    mouth: { smile: g('mouthSmile'), open: g('mouthOpen'), o: g('mouthO'), small: g('mouthSmall') },
  };
  const show = (set, key) => { for (const [k, v] of Object.entries(set)) for (const n of [].concat(v)) n.style.display = k === key ? '' : 'none'; };
  const SP = [[28, 48, 1], [172, 42, 0.8], [166, 96, 0.6], [30, 104, 0.55]];
  return function set(st) {
    show(groups.arms, st.arms || 'down');
    show(groups.eyes, st.eyes || 'open');
    show(groups.brows, st.brows || 'normal');
    show(groups.mouth, st.mouth || 'smile');
    g('pupils').setAttribute('transform', `translate(${st.px || 0} ${st.py || 0})`);
    const b = clamp(st.blink || 0);
    g('lids').setAttribute('transform', `translate(0 79) scale(1 ${b}) translate(0 -79)`);
    g('head').setAttribute('transform', `rotate(${st.tilt || 0} 100 126)`);
    g('waveArm').setAttribute('transform', `rotate(${st.wave || 0} 138 148)`);
    const blush = 0.32 + 0.25 * (st.blush || 0);
    g('cheekL').setAttribute('opacity', blush); g('cheekR').setAttribute('opacity', blush);
    const sp = st.sparkle || 0, t = st.t || 0;
    SP.forEach(([x, y, s], i) => {
      const tw = sp * (0.55 + 0.45 * Math.sin(t * 9 + i * 1.7));
      g('sp' + i).setAttribute('transform', `translate(${x} ${y}) scale(${s * tw * 1.4}) rotate(${t * 90 + i * 30})`);
    });
  };
}

/** A blink curve: 0 open, 1 shut. Blinks at the listed times, 0.16 s each. */
function blinkAt(t, times) {
  for (const b of times) { const k = (t - b) / 0.16; if (k >= 0 && k <= 1) return Math.sin(Math.PI * k); }
  return 0;
}

// ------------------------------------------------------------------ diya
function diyaMarkup(id) {
  const dots = [52, 76, 100, 124, 148].map((x, i) => `<circle cx="${x}" cy="${i % 4 === 0 ? 90 : 96}" r="3.4"/>`).join('');
  return `<svg viewBox="0 0 220 170" width="100%" height="100%" overflow="visible" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="${id}-gl" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffcf6b" stop-opacity="0.85"/><stop offset="0.35" stop-color="#ff9a3c" stop-opacity="0.35"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient>
    <linearGradient id="${id}-fl" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff7a1a"/><stop offset="0.55" stop-color="#ffb43a"/><stop offset="1" stop-color="#ffe08a"/></linearGradient>
    <linearGradient id="${id}-bw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d4643a"/><stop offset="1" stop-color="#9c3a1c"/></linearGradient>
  </defs>
  <circle id="${id}-glow" cx="176" cy="44" r="150" fill="url(#${id}-gl)"/>
  <ellipse cx="100" cy="140" rx="40" ry="9" fill="#7a2c14"/>
  <path d="M14 76 C24 136 176 136 186 76 Z" fill="url(#${id}-bw)"/>
  <path d="M168 70 q26 -8 34 0 q-10 12 -30 12z" fill="#e2783e"/>
  <ellipse cx="100" cy="76" rx="86" ry="15" fill="#e8834a"/>
  <ellipse cx="98" cy="76" rx="72" ry="9" fill="#6e2610"/>
  <ellipse cx="96" cy="74" rx="40" ry="3" fill="#a24a1c" opacity="0.6"/>
  <g fill="#ffd166">${dots}</g>
  <path d="M30 104 q10 8 20 0 q10 8 20 0 q10 8 20 0 q10 8 20 0 q10 8 20 0 q10 8 20 0 q10 8 20 0" stroke="#ffd166" stroke-width="2.5" fill="none" opacity="0.8"/>
  <g id="${id}-flame" transform="translate(190 72)">
    <path d="M0 0 C-16 -14 -12 -44 0 -70 C12 -44 16 -14 0 0Z" fill="url(#${id}-fl)"/>
    <path d="M0 -4 C-7 -10 -6 -28 0 -40 C6 -28 7 -10 0 -4Z" fill="#fff6cf"/>
  </g>
</svg>`;
}
function makeDiya(el, id) {
  el.innerHTML = diyaMarkup(id);
  const flame = document.getElementById(`${id}-flame`), glow = document.getElementById(`${id}-glow`);
  return function set(lit, t, seed = 0) {
    const fl = 0.92 + 0.08 * Math.sin(t * 23 + seed) + 0.05 * Math.sin(t * 41 + seed * 2);
    const sk = 4 * Math.sin(t * 13 + seed);
    flame.setAttribute('transform', `translate(190 72) skewX(${sk * lit}) scale(${lit * (0.9 + 0.1 * fl)} ${lit * fl})`);
    glow.setAttribute('opacity', clamp(lit) * (0.85 + 0.15 * fl));
    glow.setAttribute('r', 150 * (0.6 + 0.4 * lit));
  };
}

// ------------------------------------------------------------------ fireworks (canvas, deterministic in t)
function makeBursts(list, seed) {
  const R = rnd(seed);
  return list.map((b) => ({
    ...b,
    parts: Array.from({ length: b.n || 70 }, (_, i) => ({
      a: (i / (b.n || 70)) * Math.PI * 2 + R() * 0.12, v: (b.v || 420) * (0.75 + R() * 0.35), c: b.colors[Math.floor(R() * b.colors.length)], tw: R() * 6,
    })),
  }));
}
function drawBursts(ctx, bursts, t) {
  for (const b of bursts) {
    // the rocket going up
    const rise = 0.45;
    if (t >= b.t0 - rise && t < b.t0) {
      const k = eOut((t - (b.t0 - rise)) / rise);
      const y = lerp(b.y + 700, b.y, k), x = b.x + Math.sin(k * 6) * 6;
      const g = ctx.createLinearGradient(x, y, x, y + 120);
      g.addColorStop(0, 'rgba(255,240,200,0.95)'); g.addColorStop(1, 'rgba(255,200,120,0)');
      ctx.strokeStyle = g; ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x, y + 120); ctx.stroke();
    }
    const dt = t - b.t0;
    if (dt < 0 || dt > 2.2) continue;
    // flash
    if (dt < 0.25) { const rr = 80 + dt * 500, gr = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, rr); gr.addColorStop(0, 'rgba(255,243,208,0.6)'); gr.addColorStop(1, 'rgba(255,243,208,0)'); ctx.globalAlpha = 1 - dt / 0.25; ctx.fillStyle = gr; ctx.beginPath(); ctx.arc(b.x, b.y, rr, 0, 6.283); ctx.fill(); }
    for (const p of b.parts) {
      const d = (k) => p.v * (1 - Math.exp(-k * 2.6)) / 1.0;
      const pos = (k) => [b.x + Math.cos(p.a) * d(k), b.y + Math.sin(p.a) * d(k) + 60 * k * k];
      const [x1, y1] = pos(dt), [x0, y0] = pos(Math.max(0, dt - 0.12));
      const fade = clamp(1.25 - dt * 0.75) * (dt > 0.9 ? 0.6 + 0.4 * Math.sin(dt * 30 + p.tw) : 1);
      ctx.globalAlpha = clamp(fade);
      ctx.strokeStyle = p.c; ctx.lineWidth = 5 * clamp(1.3 - dt * 0.5); ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      ctx.fillStyle = '#fff8e0'; ctx.beginPath(); ctx.arc(x1, y1, 3.2 * clamp(1.3 - dt * 0.6), 0, 6.283); ctx.fill();
    }
    ctx.globalAlpha = 1;
  }
}

// ------------------------------------------------------------------ marigold petals (canvas)
function makePetals(n, W, H, seed) {
  const R = rnd(seed);
  return Array.from({ length: n }, () => ({ x: R() * W, y0: -R() * H * 0.9, v: 260 + R() * 260, sw: 30 + R() * 60, f: 1 + R() * 2, r: 12 + R() * 14, rot: R() * 6.28, c: ['#ff9933', '#ffb020', '#ffc233', '#e8402f', '#ff7aa2'][Math.floor(R() * 5)] }));
}
function drawPetals(ctx, petals, t, t0, H, alpha = 1) {
  const k = t - t0; if (k < 0) return;
  for (const p of petals) {
    const y = p.y0 + p.v * k; if (y > H + 40 || y < -40) continue;
    const x = p.x + Math.sin(k * p.f + p.rot) * p.sw;
    ctx.save(); ctx.translate(x, y); ctx.rotate(p.rot + k * p.f * 1.5); ctx.scale(1, 0.55 + 0.45 * Math.sin(k * p.f * 3 + p.rot));
    ctx.globalAlpha = alpha; ctx.fillStyle = p.c; ctx.beginPath(); ctx.ellipse(0, 0, p.r, p.r * 0.62, 0, 0, 6.283); ctx.fill();
    ctx.restore();
  }
  ctx.globalAlpha = 1;
}
