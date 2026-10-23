const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const aTags = html.match(/<a[^>]*>[\s\S]*?<\/a>/gi) || [];
console.log('Total <a> tags:', aTags.length);

const parsedLinks = aTags.map(a => {
  const href = (a.match(/href="([^"]+)"/) || [])[1];
  const text = a.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  const img = (a.match(/src="([^"]+)"/) || [])[1];
  return { href, text: text.slice(0, 50), img };
});

console.log('Sample parsed <a> tags:');
parsedLinks.forEach((l, i) => {
  console.log(`${i}: href=${l.href} | text="${l.text}" | img=${l.img ? l.img.slice(0, 40) : 'none'}`);
});
