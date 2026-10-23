const fs = require('fs');

const html = fs.readFileSync('adyatha.html', 'utf8');

// Let's inspect the sections
// Look for data-framer-name or similar
const framerNames = html.match(/data-framer-name="[^"]+"/g) || [];
console.log('Unique data-framer-name values:');
console.log(Array.from(new Set(framerNames)).slice(0, 50));

// Let's find project details
const projectMatches = [];
// Look for project names
const projects = [
  '8 CLUB Onboarding Video',
  'Show me the money',
  'Enterprise Readiness GTM',
  'CA & Founder Collaboration',
  'Custom Access Controls',
  'You Are Okay'
];

projects.forEach(p => {
  const idx = html.indexOf(p);
  console.log(`\nProject: ${p} found at index ${idx}`);
  if (idx !== -1) {
    console.log(html.slice(Math.max(0, idx - 300), Math.min(html.length, idx + 500)));
  }
});
