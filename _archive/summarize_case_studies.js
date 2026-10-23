const fs = require('fs');

const pages = [
  { slug: '8club-onboarding-video', title: '8 CLUB Onboarding Video' },
  { slug: 'show-me-the-money', title: 'Show me the money' },
  { slug: 'enterprise-readiness', title: 'Enterprise Readiness GTM' },
  { slug: 'ca-founder-collab', title: 'CA & Founder Collaboration' },
  { slug: 'custom-access-controls', title: 'Custom Access Controls' },
  { slug: 'you-are-okay', title: 'You Are Okay' }
];

const results = {};

pages.forEach(({ slug, title }) => {
  const filename = `adyatha_${slug}.html`;
  if (fs.existsSync(filename)) {
    const html = fs.readFileSync(filename, 'utf8');
    const text = html
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
      .replace(/<svg[^>]*>[\s\S]*?<\/svg>/gi, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    
    // find images in this case study
    const imgs = html.match(/https:\/\/framerusercontent\.com\/images\/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|webp|svg)/g) || [];
    const uniqueImgs = Array.from(new Set(imgs));
    
    // find video links (vimeo, youtube, mp4)
    const videos = html.match(/https:\/\/(?:www\.)?(?:vimeo\.com|youtube\.com|youtu\.be)[^\s"']+/g) || [];
    
    results[slug] = {
      title,
      textLength: text.length,
      sampleText: text.slice(0, 400),
      imagesCount: uniqueImgs.length,
      images: uniqueImgs.slice(0, 10),
      videos: Array.from(new Set(videos))
    };
  }
});

console.log(JSON.stringify(results, null, 2));
fs.writeFileSync('case_studies_summary.json', JSON.stringify(results, null, 2), 'utf8');
