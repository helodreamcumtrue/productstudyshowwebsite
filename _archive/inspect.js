const fs = require('fs');

const wop = fs.readFileSync('wop_adyatha.html', 'utf8');
console.log('=== WOP (wallofportfolios) ===');
console.log('Length:', wop.length);
const wopTitle = wop.match(/<title>([\s\S]*?)<\/title>/i);
console.log('Title:', wopTitle ? wopTitle[1].trim() : 'none');

// Look for colors, pinks, etc.
const wopPinks = wop.match(/#[0-9a-fA-F]{6}|rgba?\([^)]+\)|rgb\([^)]+\)/g) || [];
console.log('Sample wop colors:', Array.from(new Set(wopPinks)).slice(0, 15));

const adyatha = fs.readFileSync('adyatha.html', 'utf8');
console.log('\n=== ADYATHA FRAMER ===');
console.log('Length:', adyatha.length);
const adyTitle = adyatha.match(/<title>([\s\S]*?)<\/title>/i);
console.log('Title:', adyTitle ? adyTitle[1].trim() : 'none');

const adyPinks = adyatha.match(/#[0-9a-fA-F]{6}|rgba?\([^)]+\)|rgb\([^)]+\)/g) || [];
console.log('Total color occurrences in adyatha:', adyPinks.length);
console.log('Unique colors in adyatha (first 25):', Array.from(new Set(adyPinks)).slice(0, 25));
