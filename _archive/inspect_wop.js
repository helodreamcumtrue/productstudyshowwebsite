const fs = require('fs');

const wop = fs.readFileSync('wop_adyatha.html', 'utf8');
console.log('--- WOP Content Highlights ---');
// print all headings, links, images
const headings = wop.match(/<h[1-6][^>]*>[\s\S]*?<\/h[1-6]>/gi) || [];
console.log('Headings:', headings);

// check if there is an iframe or main section
const iframes = wop.match(/<iframe[^>]*>[\s\S]*?<\/iframe>|<iframe[^>]*\/?>/gi) || [];
console.log('Iframes:', iframes);

const buttons = wop.match(/<button[^>]*>[\s\S]*?<\/button>|<a[^>]*class="[^"]*(btn|button|cta|submit)[^"]*"[^>]*>[\s\S]*?<\/a>/gi) || [];
console.log('Buttons/CTAs count:', buttons.length);
