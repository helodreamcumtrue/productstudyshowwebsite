const fs = require('fs');

const html = fs.readFileSync('adyatha.html', 'utf8');

// Find all cards
// Let's search for "View case study"
let pos = 0;
const cards = [];
while (true) {
  const vcs = html.indexOf('View case study', pos);
  if (vcs === -1) break;
  // grab 3000 chars before and 1000 chars after
  const chunk = html.slice(Math.max(0, vcs - 2500), Math.min(html.length, vcs + 1000));
  
  // extract images inside chunk
  const imgs = Array.from(new Set(chunk.match(/https:\/\/framerusercontent\.com\/images\/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|webp)/g) || []));
  
  // extract link
  const linkMatch = chunk.match(/href="(\.\/[a-z0-9-]+)"/);
  
  // extract title
  const titleMatch = chunk.match(/--framer-font-size:36px[^>]*><p[^>]*>([\s\S]*?)<\/p>|--framer-font-size:36px[^>]*>([\s\S]*?)<\/p>/i);
  
  cards.push({
    chunkLength: chunk.length,
    vcsPos: vcs,
    imgs,
    link: linkMatch ? linkMatch[1] : null
  });
  pos = vcs + 15;
}

console.log('Total View case study matches:', cards.length);

// In Framer, responsive layouts duplicate elements for Desktop, Tablet, Mobile!
// Let's see unique project links
const uniqueProjects = Array.from(new Set(cards.map(c => c.link)));
console.log('Unique project links:', uniqueProjects);
