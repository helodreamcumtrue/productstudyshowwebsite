const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

// The hero is before the projects
const projIdx = html.indexOf('8 CLUB Onboarding Video');
const heroChunk = html.slice(0, projIdx);

// Look for text in heroChunk
const heroText = heroChunk
  .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
  .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
  .replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/\s+/g, ' ')
  .trim();

console.log('Hero text content:');
console.log(heroText);

// Look for images in heroChunk
const heroImgs = heroChunk.match(/https:\/\/[^"'\s]+\.(?:png|jpg|jpeg|webp|svg)/gi) || [];
console.log('Hero images:', Array.from(new Set(heroImgs)));
