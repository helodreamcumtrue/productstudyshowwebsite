import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all image URLs from framerusercontent.com
img_urls = set(re.findall(r'https://framerusercontent.com/images/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|webp|svg)', html))
print(f"Total unique base image URLs: {len(img_urls)}")
for u in sorted(img_urls):
    print(" ", u)
