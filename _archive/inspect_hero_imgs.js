const fs = require('fs');
const html = fs.readFileSync('adyatha.html', 'utf8');

const imgs = [
  'PY7NmnLSv2zAwrstpLG1ZbuKNNk.png',
  'WxhNkCxP37sohFvrfFSZGp478.png',
  'ZIGGNTa59t23FnqZrTBBmnU8Rxk.png',
  '6Uxw6b3gvj4edJoZKCESNTqnc.png',
  'fXqibY48KxkV3CU0IWsPA4c61XM.png'
];

imgs.forEach(img => {
  const idx = html.indexOf(img);
  console.log(`\nImage ${img} at idx ${idx}:`);
  if (idx !== -1) {
    console.log(html.slice(Math.max(0, idx - 200), Math.min(html.length, idx + 300)));
  }
});
