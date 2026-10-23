const fs = require('fs');

const slugs = [
  '8club-onboarding-video',
  'show-me-the-money',
  'enterprise-readiness',
  'ca-founder-collab',
  'custom-access-controls',
  'you-are-okay'
];

slugs.forEach(slug => {
  const filename = `adyatha_${slug}.html`;
  if (!fs.existsSync(filename)) return;
  const html = fs.readFileSync(filename, 'utf8');

  console.log(`\n=== ${slug} ===`);
  const labels = ['Project Type', 'Target Audience', 'Timeframe'];
  labels.forEach(l => {
    const idx = html.indexOf(l);
    if (idx !== -1) {
      const snippet = html.slice(idx, idx + 250).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
      console.log(`  ${snippet}`);
    }
  });
});
