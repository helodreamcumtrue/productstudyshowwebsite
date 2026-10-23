import re

with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check main tag / id="main"
main_match = re.search(r'<div[^>]*id=["\']main["\'][^>]*>', html)
if main_match:
    print("Found id='main':", main_match.group(0)[:200])

# Check data-framer-hydrate-v2
hydrate_match = re.search(r'data-framer-hydrate-v2=["\']([^"\']+)["\']', html)
if hydrate_match:
    print("Found hydrate attribute length:", len(hydrate_match.group(1)))
    print("Preview:", hydrate_match.group(1)[:150])
