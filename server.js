const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.pdf': 'application/pdf',
  '.map': 'application/json'
};

const ROUTE_MAP = {
  '/': 'index.html',
  '/about': 'framer_pages_transformed/about.html',
  '/enterprise-readiness': 'framer_pages_transformed/enterprise-readiness.html',
  '/show-me-the-money': 'framer_pages_transformed/show-me-the-money.html',
  '/you-are-okay': 'framer_pages_transformed/you-are-okay.html',
  '/ca-founder-collab': 'framer_pages_transformed/ca-founder-collab.html',
  '/8club-onboarding-video': 'framer_pages_transformed/8club-onboarding-video.html',
  '/custom-access-controls': 'framer_pages_transformed/custom-access-controls.html'
};

const server = http.createServer((req, res) => {
  let cleanUrl = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
  if (cleanUrl.endsWith('/') && cleanUrl.length > 1) {
    cleanUrl = cleanUrl.slice(0, -1);
  }

  // 1. Direct route mapping
  if (ROUTE_MAP[cleanUrl]) {
    const target = path.join(__dirname, ROUTE_MAP[cleanUrl]);
    fs.readFile(target, (err, content) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(`Internal Error: ${err.message}`);
      } else {
        res.writeHead(200, {
          'Content-Type': 'text/html; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
        res.end(content);
      }
    });
    return;
  }

  // 2. Static file serving (e.g. /framer_dist/..., /assets/...)
  let relativePath = cleanUrl;
  if (relativePath.startsWith('/')) {
    relativePath = relativePath.slice(1);
  }

  const filePath = path.join(__dirname, relativePath);
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        // Fallback for SPA routing if needed
        fs.readFile(path.join(__dirname, 'index.html'), (error, fallback) => {
          if (error) {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('Not Found');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end(fallback);
          }
        });
      } else {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(`Server Error: ${err.code}`);
      }
    } else {
      res.writeHead(200, {
        'Content-Type': contentType,
        'Access-Control-Allow-Origin': '*'
      });
      res.end(content);
    }
  });
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
