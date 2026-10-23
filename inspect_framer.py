import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', html)
print('Script count:', len(scripts))
for s in scripts[:10]:
    print('  Script:', s)

modules = re.findall(r'https://framerusercontent.com/modules/[^\s"\'\)]+', html)
print('Modules found:', len(modules))
for m in list(set(modules))[:5]:
    print('  Module:', m)

# Let's inspect images in framer_site_raw.html
images = re.findall(r'https://framerusercontent.com/images/[^\s"\'\)]+', html)
print('Images found:', len(images))
for img in list(set(images))[:10]:
    print('  Image:', img)

# Let's search for pink-like hex colors in html
hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', html))
print('Unique hex colors in html:', len(hex_colors))
for hc in sorted(hex_colors):
    print(' ', hc)
