const fs = require('fs');

const html = fs.readFileSync('adyatha.html', 'utf8');

// Find all CSS rules containing 179, 45, 71 or d5546d or ffa8b9 or e28799
const cssBlocks = html.match(/<style[^>]*>[\s\S]*?<\/style>/gi) || [];
const allCss = cssBlocks.join('\n');

const pinkRules = [];
const lines = allCss.split('\n');
lines.forEach(line => {
  if (/179,\s*45,\s*71|d5546d|ffa8b9|e28799|213,\s*84,\s*109/i.test(line)) {
    pinkRules.push(line.trim());
  }
});

console.log(`Found ${pinkRules.length} pink CSS rules. Sample:`);
pinkRules.slice(0, 30).forEach(r => console.log('  ' + r));

// Also check inline style attributes
const inlinePinks = html.match(/style="[^"]*(?:179,\s*45,\s*71|d5546d|ffa8b9|e28799|213,\s*84,\s*109)[^"]*"/gi) || [];
console.log(`\nFound ${inlinePinks.length} inline styles with pink. Sample:`);
inlinePinks.slice(0, 15).forEach(s => console.log('  ' + s));
