import urllib.request
import re

url = 'https://framerusercontent.com/sites/2Lchxi9LzakPkRuMF1bj1g/WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    js = resp.read().decode('utf-8')

print("Home page module size:", len(js))
with open('framer_home_page.mjs', 'w', encoding='utf-8') as f:
    f.write(js)

# Find pink hex colors in this module
hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', js))
print("Hex colors in home module:")
for hc in sorted(hex_colors):
    print(" ", hc)

# Find rgb/rgba
rgba = set(re.findall(r'rgba?\([^\)]+\)', js))
print("RGBA colors:", len(rgba))
for r in rgba:
    if '213' in r or '179' in r:
        print("  Red/pink rgba:", r)

# Find image references
imgs = set(re.findall(r'https://framerusercontent.com/images/[^\s\"\'\)]+', js))
print(f"Images in home module: {len(imgs)}")
for im in imgs:
    print("  img:", im)
