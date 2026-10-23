const fs = require('fs');

const homeHtml = fs.readFileSync('adyatha.html', 'utf8');

// Find all css rules or inline styles mentioning pink or hex colors
const colorMatches = homeHtml.match(/#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)/g) || [];
const counts = {};
colorMatches.forEach(c => {
  const norm = c.toLowerCase();
  counts[norm] = (counts[norm] || 0) + 1;
});

const sortedColors = Object.entries(counts).sort((a,b) => b[1] - a[1]);
console.log('Top colors used on home page:');
sortedColors.forEach(([col, count]) => {
  console.log(`  ${col}: ${count}`);
});

// Let's inspect the fonts used
const fontMatches = homeHtml.match(/font-family:[^;]+/gi) || [];
console.log('\nFont families used:');
console.log(Array.from(new Set(fontMatches)));

// Let's inspect SVG icons
const svgs = homeHtml.match(/<svg[\s\S]*?<\/svg>/gi) || [];
console.log('\nTotal SVGs on home page:', svgs.length);
if (svgs.length > 0) {
  fs.writeFileSync('sample_svgs.html', svgs.join('\n<hr>\n'), 'utf8');
}
