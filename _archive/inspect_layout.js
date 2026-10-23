const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

// Find styles for project cards
const cardStyles = html.match(/--framer-font-size:36px[\s\S]*?<\/div>/gi) || [];
console.log('Sample card title elements:', cardStyles.slice(0, 3));

// Check navbar layout and items
const navMatch = html.match(/<nav[\s\S]*?<\/nav>|<header[\s\S]*?<\/header>/gi) || [];
console.log('Nav/header tags found:', navMatch.length);

// If no semantic nav, look for HOME ABOUT RESUME
const navIdx = html.indexOf('HOME');
if (navIdx !== -1) {
  console.log('\nNavbar snippet:');
  console.log(html.slice(Math.max(0, navIdx - 300), Math.min(html.length, navIdx + 600)));
}

// Check footer
const footerIdx = html.indexOf('portfolio by');
if (footerIdx !== -1) {
  console.log('\nFooter snippet:');
  console.log(html.slice(Math.max(0, footerIdx - 300), Math.min(html.length, footerIdx + 500)));
}
