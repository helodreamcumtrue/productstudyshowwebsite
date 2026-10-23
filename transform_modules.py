import re
import os
import glob

# Color mapping: Pink to Electric Cobalt Blue
COLOR_REPLACEMENTS = [
    # Hex colors
    ('#d5546d', '#2563eb'),
    ('#D5546D', '#2563eb'),
    ('#ffa8b9', '#93c5fd'),
    ('#FFA8B9', '#93c5fd'),
    ('#e28799', '#60a5fa'),
    ('#E28799', '#60a5fa'),
    # RGBA colors
    ('rgba(213, 84, 109, 0.3)', 'rgba(37, 99, 235, 0.3)'),
    ('rgba(213, 84, 109, 0.4)', 'rgba(37, 99, 235, 0.4)'),
    ('rgba(213, 84, 109,', 'rgba(37, 99, 235,'),
    ('rgba(179, 45, 71, 0.7)', 'rgba(29, 78, 216, 0.7)'),
    ('rgba(179, 45, 71,', 'rgba(29, 78, 216,'),
]

# Image replacements: Hero banners to recolored blue banners
HERO_REPLACEMENTS = [
    # Desktop hero
    ('https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png', '/assets/hero_desktop_blue.png'),
    ('https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png?scale-down-to=512&width=2560&height=1600', '/assets/hero_desktop_blue.png'),
    ('https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png?scale-down-to=1024&width=2560&height=1600', '/assets/hero_desktop_blue.png'),
    ('https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png?scale-down-to=2048&width=2560&height=1600', '/assets/hero_desktop_blue.png'),
    ('https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png?width=2560&height=1600', '/assets/hero_desktop_blue.png'),
    # Tablet hero
    ('https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png', '/assets/hero_tablet_blue.png'),
    ('https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png?scale-down-to=512&width=1620&height=2160', '/assets/hero_tablet_blue.png'),
    ('https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png?scale-down-to=1024&width=1620&height=2160', '/assets/hero_tablet_blue.png'),
    ('https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png?scale-down-to=2048&width=1620&height=2160', '/assets/hero_tablet_blue.png'),
    ('https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png?width=1620&height=2160', '/assets/hero_tablet_blue.png'),
    # Mobile hero
    ('https://framerusercontent.com/images/fXqibY48KxkV3CU0IWsPA4c61XM.png', '/assets/hero_mobile_blue.png'),
    ('https://framerusercontent.com/images/fXqibY48KxkV3CU0IWsPA4c61XM.png?scale-down-to=512&width=720&height=1620', '/assets/hero_mobile_blue.png'),
    ('https://framerusercontent.com/images/fXqibY48KxkV3CU0IWsPA4c61XM.png?width=720&height=1620', '/assets/hero_mobile_blue.png'),
]

# Process JS modules in framer_dist/
js_files = glob.glob('framer_dist/*.mjs')
print(f"Transforming {len(js_files)} JS modules...")
for jf in js_files:
    with open(jf, 'r', encoding='utf-8') as f:
        code = f.read()
    
    orig_len = len(code)
    for old_c, new_c in COLOR_REPLACEMENTS:
        code = code.replace(old_c, new_c)
    
    for old_h, new_h in HERO_REPLACEMENTS:
        code = code.replace(old_h, new_h)
    
    with open(jf, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"  Processed {os.path.basename(jf)}")

print("Done transforming JS modules.")
