const fs = require('fs');

const slugs = [
  '8club-onboarding-video',
  'show-me-the-money',
  'enterprise-readiness',
  'ca-founder-collab',
  'custom-access-controls',
  'you-are-okay'
];

const data = {};

slugs.forEach(slug => {
  const filename = `adyatha_${slug}.html`;
  if (!fs.existsSync(filename)) return;
  const html = fs.readFileSync(filename, 'utf8');

  // Extract meta
  const pTypeMatch = html.match(/Project Type[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i);
  const targetMatch = html.match(/Target Audience[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i);
  const timeMatch = html.match(/Timeframe[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i);

  const clean = (str) => str ? str.replace(/<[^>]+>/g, '').trim() : '';

  // Extract sections
  const problemMatch = html.match(/Problem[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i);
  
  // Extract images
  const imgs = Array.from(new Set(html.match(/https:\/\/framerusercontent\.com\/images\/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|webp|svg)/g) || []))
    .filter(url => !url.includes('PY7NmnLSv2zAwrstpLG1ZbuKNNk') && !url.includes('WxhNkCxP37sohFvrfFSZGp478'));

  data[slug] = {
    projectType: clean(pTypeMatch ? pTypeMatch[1] : ''),
    targetAudience: clean(targetMatch ? targetMatch[1] : ''),
    timeframe: clean(timeMatch ? timeMatch[1] : ''),
    problem: clean(problemMatch ? problemMatch[1] : ''),
    images: imgs.slice(0, 6)
  };
});

console.log('Extracted case studies info:', JSON.stringify(data, null, 2));
fs.writeFileSync('full_case_studies_data.json', JSON.stringify(data, null, 2), 'utf8');
