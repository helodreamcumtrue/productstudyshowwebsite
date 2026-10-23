const fs = require('fs');
const html = fs.readFileSync('adyatha_about.html', 'utf8');

const textContent = html
  .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
  .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
  .replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/\s+/g, ' ')
  .trim();

console.log('=== ABOUT PAGE TEXT ===');
console.log(textContent);
fs.writeFileSync('about_text.txt', textContent, 'utf8');
