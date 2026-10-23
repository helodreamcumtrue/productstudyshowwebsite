const fs = require('fs');
const html = fs.readFileSync('adyatha_about.html', 'utf8');

const pinkMatches = html.match(/(?:179,\s*45,\s*71|d5546d|ffa8b9|e28799|213,\s*84,\s*109)/gi) || [];
console.log('About page pink matches count:', pinkMatches.length);

// Let's find images or hero of about page
const aboutHero = html.match(/About Me/g) || [];
console.log('About Me count:', aboutHero.length);

// Find what banner or visuals exist on about page
const bannerImgs = html.match(/https:\/\/framerusercontent\.com\/images\/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|webp)/g) || [];
console.log('About banner images:', Array.from(new Set(bannerImgs)).slice(0, 10));
