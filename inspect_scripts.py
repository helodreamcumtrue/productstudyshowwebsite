import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all script tags
all_scripts = re.findall(r'<script([^>]*)>(.*?)</script>', html, re.DOTALL)
print('Total script tags:', len(all_scripts))
for i, (attrs, body) in enumerate(all_scripts):
    print(f"Script {i}: attrs={attrs.strip()} length={len(body)}")
    if len(body) > 0 and len(body) < 500:
        print(f"  Body: {body.strip()}")
    elif len(body) >= 500:
        print(f"  Body preview: {body.strip()[:200]}...")

# Find all modulepreloads
modulepreloads = re.findall(r'<link[^>]*rel=["\']modulepreload["\'][^>]*href=["\']([^"\']+)["\']', html)
print('Module preloads:', len(modulepreloads))
for mp in modulepreloads:
    print('  Preload:', mp)
