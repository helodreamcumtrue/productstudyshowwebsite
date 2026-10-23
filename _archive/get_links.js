const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const hrefs = [];
const hrefRegex = /href="([^"]+)"/g;
let m;
while ((m = hrefRegex.exec(html)) !== null) {
  hrefs.push(m[1]);
}
console.log('All unique hrefs:', Array.from(new Set(hrefs)));
