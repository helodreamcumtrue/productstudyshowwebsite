const fs = require('fs');

const html = fs.readFileSync('adyatha.html', 'utf8');

// Find all text nodes or structured parts
// In Framer sites, content is often inside data-framer-component or styled divs, or serialized JSON
console.log('HTML size:', html.length);

// Let's check for __framer or page data
const scripts = html.match(/<script[^>]*>([\s\S]*?)<\/script>/gi) || [];
console.log('Total scripts:', scripts.length);

// Let's check images
const images = [];
const imgRegex = /https:\/\/[^"'\s]+\.(?:png|jpg|jpeg|webp|svg|gif|avif)/gi;
let match;
while ((match = imgRegex.exec(html)) !== null) {
  images.push(match[0]);
}
const uniqueImages = Array.from(new Set(images));
console.log('Unique image URLs found:', uniqueImages.length);
console.log('Sample images:', uniqueImages.slice(0, 20));

// Let's search for text content
const textContent = html
  .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
  .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
  .replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/\s+/g, ' ')
  .trim();

console.log('Text content sample (first 1000 chars):');
console.log(textContent.slice(0, 1000));

fs.writeFileSync('extracted_text.txt', textContent, 'utf8');
console.log('Saved extracted_text.txt, length:', textContent.length);
