import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all <img> tags
img_tags = re.findall(r'<img[^>]+>', html)
print(f"Total img tags: {len(img_tags)}")
for img in img_tags:
    src_match = re.search(r'src=["\']([^"\']+)["\']', img)
    src = src_match.group(1) if src_match else 'none'
    alt_match = re.search(r'alt=["\']([^"\']+)["\']', img)
    alt = alt_match.group(1) if alt_match else ''
    print(f"img: src={src[:80]} | alt={alt}")

# Search for hero background images or pictures
picture_tags = re.findall(r'<picture[^>]*>.*?</picture>', html, re.DOTALL)
print(f"\nTotal picture tags: {len(picture_tags)}")
for pic in picture_tags:
    print("--- PICTURE TAG ---")
    print(pic[:300])

# Search for hero text occurrences and their surroundings
for match in re.finditer(r'(visual designer|kerning|storyteller)', html, re.I):
    start = max(0, match.start() - 150)
    end = min(len(html), match.end() + 150)
    print(f"\nContext around '{match.group(1)}':")
    print(html[start:end])
