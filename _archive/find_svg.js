const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const defs = html.match(/<svg[\s\S]*?id="svg-207030265_242"[\s\S]*?<\/svg>|<g id="svg-207030265_242"[\s\S]*?<\/g>/gi) || [];
console.log('Found svg-207030265_242:', defs.length);
if (defs.length > 0) {
  console.log(defs[0]);
} else {
  // search for the id
  const idx = html.indexOf('svg-207030265_242');
  console.log('Index:', idx);
  console.log(html.slice(Math.max(0, idx - 100), Math.min(html.length, idx + 400)));
}
