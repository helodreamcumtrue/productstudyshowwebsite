const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const slugs = [
  '8club-onboarding-video',
  'show-me-the-money',
  'enterprise-readiness',
  'ca-founder-collab',
  'custom-access-controls',
  'you-are-okay'
];

slugs.forEach(slug => {
  const regex = new RegExp(`<a[^>]*href="\\.\\/${slug}"[\\s\\S]*?<\\/a>`, 'i');
  const match = html.match(regex);
  if (match) {
    const aTag = match[0];
    const imgs = aTag.match(/src="([^"]+)"/g) || [];
    console.log(`\n=== SLUG: ${slug} ===`);
    console.log(imgs);
  }
});
