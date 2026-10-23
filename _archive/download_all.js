const { execSync } = require('child_process');
const fs = require('fs');

const pages = [
  'show-me-the-money',
  'enterprise-readiness',
  'ca-founder-collab',
  'custom-access-controls',
  'you-are-okay'
];

for (const slug of pages) {
  const filename = `adyatha_${slug}.html`;
  if (!fs.existsSync(filename)) {
    console.log(`Downloading ${slug}...`);
    try {
      execSync(`curl.exe -sL https://adyatha.framer.website/${slug} -o ${filename}`);
      console.log(`Downloaded ${filename}`);
    } catch (e) {
      console.error(`Failed ${slug}`, e.message);
    }
  }
}
console.log('All pages downloaded!');
