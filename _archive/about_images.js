const fs = require('fs');
const html = fs.readFileSync('adyatha_about.html', 'utf8');

const images = [];
const imgRegex = /https:\/\/[^"'\s]+\.(?:png|jpg|jpeg|webp|svg|gif|avif)/gi;
let match;
while ((match = imgRegex.exec(html)) !== null) {
  images.push(match[0]);
}
console.log('About page unique images:', Array.from(new Set(images)));
