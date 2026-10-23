const fs = require('fs');
const html = fs.readFileSync('adyatha_8club.html', 'utf8');

const textContent = html
  .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
  .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
  .replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/\s+/g, ' ')
  .trim();

console.log('=== 8CLUB PAGE TEXT ===');
console.log(textContent.slice(0, 1500));
