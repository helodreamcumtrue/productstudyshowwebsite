import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for pink color codes in HTML/CSS
pinks = ['d5546d', 'e28799', 'ffa8b9', 'e28596', 'f9abb9', 'b7495e']
for p in pinks:
    matches = list(re.finditer(re.escape(p), html, re.I))
    print(f"Color #{p}: found {len(matches)} times")
    for m in matches[:5]:
        start = max(0, m.start() - 60)
        end = min(len(html), m.end() + 60)
        print("   Snippet:", html[start:end].replace('\n', ' '))

# Check rgb/rgba occurrences
rgba_matches = re.findall(r'rgba?\([^\)]+\)', html)
print(f"\nTotal rgba() in html: {len(rgba_matches)}")
for rm in set(rgba_matches):
    # check if reddish
    nums = re.findall(r'\d+', rm)
    if len(nums) >= 3:
        r, g, b = int(nums[0]), int(nums[1]), int(nums[2])
        if r > 150 and r > g + 40 and r > b + 20:
            print("  Reddish rgba:", rm)
