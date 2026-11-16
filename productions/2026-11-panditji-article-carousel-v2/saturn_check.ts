// Saturn's sign in the Western (tropical) and Vedic (sidereal, Lahiri) zodiacs, using Panditji's own engine.
import { tropicalLongitude } from './src/engine/core/ephemeris';
import { tropicalToSidereal, computeAyanamsa } from './src/engine/core/ayanamsa';
import { signOf, degInSign } from './src/engine/core/zodiac';
const SIGNS = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces'];
const fmt = (lon: number) => `${SIGNS[signOf(lon)]} ${degInSign(lon).toFixed(2)}°`;
for (const iso of ['2026-11-16T06:30:00Z', '2026-10-01T06:30:00Z', '2026-06-01T06:30:00Z']) {
  const d = new Date(iso);
  const trop = tropicalLongitude('Saturn', d);
  const sid = tropicalToSidereal(trop, d);
  console.log(iso.slice(0,10), '| tropical (Western):', fmt(trop), '| sidereal Lahiri (Vedic):', fmt(sid), '| ayanamsa', computeAyanamsa(d).toFixed(3));
}
