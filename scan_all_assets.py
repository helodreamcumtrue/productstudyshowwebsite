import re
import glob

all_text = []

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    all_text.append(f.read())

for p in glob.glob('framer_pages/*.html'):
    with open(p, 'r', encoding='utf-8') as f:
        all_text.append(f.read())

for m in glob.glob('framer_dist/*.mjs'):
    with open(m, 'r', encoding='utf-8') as f:
        all_text.append(f.read())

combined = "\n".join(all_text)

# Find all images
images = set(re.findall(r'https://framerusercontent.com/images/([a-zA-Z0-9_-]+\.[a-zA-Z0-9]+)', combined))
print(f"Total unique images found: {len(images)}")
for im in sorted(images):
    print("  img:", im)

# Check search indices
search_indices = set(re.findall(r'https://framerusercontent.com/sites/[^/]+/([a-zA-Z0-9_-]+\.json)', combined))
print(f"\nSearch indices: {search_indices}")
