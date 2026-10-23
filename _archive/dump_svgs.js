const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const tplIdx = html.indexOf('id="svg-templates"');
if (tplIdx !== -1) {
  const tplEnd = html.indexOf('</div>', tplIdx);
  const tplContent = html.slice(tplIdx, tplEnd + 6);
  fs.writeFileSync('all_svg_templates.html', tplContent, 'utf8');
  console.log('Saved all_svg_templates.html, length:', tplContent.length);
} else {
  console.log('No svg-templates found');
}
