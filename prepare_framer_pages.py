import re
import os
import glob

COLOR_REPLACEMENTS = [
    # Framer token for primary accent color
    ('--token-7395beff-cbd1-4ab6-8298-561b3ea84b05:#d5546d', '--token-7395beff-cbd1-4ab6-8298-561b3ea84b05:#2563eb'),
    ('--token-7395beff-cbd1-4ab6-8298-561b3ea84b05: #d5546d', '--token-7395beff-cbd1-4ab6-8298-561b3ea84b05: #2563eb'),
    ('#d5546d', '#2563eb'),
    ('#D5546D', '#2563eb'),
    ('#ffa8b9', '#93c5fd'),
    ('#FFA8B9', '#93c5fd'),
    ('#e28799', '#60a5fa'),
    ('#E28799', '#60a5fa'),
    ('rgba(213, 84, 109, 0.3)', 'rgba(37, 99, 235, 0.3)'),
    ('rgba(213, 84, 109, 0.4)', 'rgba(37, 99, 235, 0.4)'),
    ('rgba(213, 84, 109,', 'rgba(37, 99, 235,'),
    ('rgba(179, 45, 71, 0.7)', 'rgba(29, 78, 216, 0.7)'),
    ('rgba(179, 45, 71,', 'rgba(29, 78, 216,'),
]

HERO_REPLACEMENTS = [
    # Replace all desktop hero variants
    (r'https://framerusercontent\.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk\.png(?:\?[^"\'\s,)]*)?', '/assets/hero_desktop_blue.png'),
    # Replace all tablet hero variants
    (r'https://framerusercontent\.com/images/6Uxw6b3gvj4edJoZKCESNTqnc\.png(?:\?[^"\'\s,)]*)?', '/assets/hero_tablet_blue.png'),
    # Replace all mobile hero variants
    (r'https://framerusercontent\.com/images/fXqibY48KxkV3CU0IWsPA4c61XM\.png(?:\?[^"\'\s,)]*)?', '/assets/hero_mobile_blue.png'),
]

THEME_SWITCHER_SNIPPET = """
<!-- Dynamic Theme Switcher Overlay -->
<style id="framer-theme-styles">
  :root {
    --accent-color: #2563eb;
    --accent-light: #93c5fd;
    --accent-mid: #60a5fa;
    --accent-dark: #1d4ed8;
    --accent-glow: rgba(37, 99, 235, 0.3);
  }
  .theme-switcher-pill {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(18, 18, 18, 0.88);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 0 15px -2px var(--accent-glow);
    padding: 8px 14px;
    border-radius: 999px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    transition: all 0.25s ease;
  }
  .theme-switcher-pill:hover {
    transform: translateY(-2px);
    border-color: rgba(255, 255, 255, 0.25);
  }
  .theme-switcher-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.7);
    margin-right: 4px;
  }
  .theme-btn {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 2px solid transparent;
    cursor: pointer;
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), border-color 0.2s ease;
    padding: 0;
  }
  .theme-btn:hover {
    transform: scale(1.25);
  }
  .theme-btn.active {
    border-color: #ffffff;
    box-shadow: 0 0 8px currentColor;
    transform: scale(1.15);
  }
</style>
<div class="theme-switcher-pill" id="theme-switcher-pill" title="Choose Website Accent Palette">
  <span class="theme-switcher-label">Color</span>
  <button class="theme-btn active" data-color="blue" style="background: #2563eb; color: #2563eb;" title="Electric Cobalt (Default)"></button>
  <button class="theme-btn" data-color="emerald" style="background: #059669; color: #059669;" title="Emerald Green"></button>
  <button class="theme-btn" data-color="violet" style="background: #7c3aed; color: #7c3aed;" title="Cyber Violet"></button>
  <button class="theme-btn" data-color="amber" style="background: #ea580c; color: #ea580c;" title="Sunset Amber"></button>
  <button class="theme-btn" data-color="cyan" style="background: #0891b2; color: #0891b2;" title="Ocean Cyan"></button>
  <button class="theme-btn" data-color="pink" style="background: #d5546d; color: #d5546d;" title="Original Pink (Reference)"></button>
</div>
<script>
(function() {
  const THEMES = {
    blue: {
      primary: '#2563eb',
      light: '#93c5fd',
      mid: '#60a5fa',
      dark: '#1d4ed8',
      glow: 'rgba(37, 99, 235, 0.3)',
      hero_desktop: '/assets/hero_desktop_blue.png',
      hero_tablet: '/assets/hero_tablet_blue.png',
      hero_mobile: '/assets/hero_mobile_blue.png'
    },
    emerald: {
      primary: '#059669',
      light: '#6ee7b7',
      mid: '#34d399',
      dark: '#047857',
      glow: 'rgba(5, 150, 105, 0.3)',
      hero_desktop: '/assets/hero_desktop_blue.png',
      hero_tablet: '/assets/hero_tablet_blue.png',
      hero_mobile: '/assets/hero_mobile_blue.png'
    },
    violet: {
      primary: '#7c3aed',
      light: '#c4b5fd',
      mid: '#a78bfa',
      dark: '#6d28d9',
      glow: 'rgba(124, 58, 237, 0.3)',
      hero_desktop: '/assets/hero_desktop_blue.png',
      hero_tablet: '/assets/hero_tablet_blue.png',
      hero_mobile: '/assets/hero_mobile_blue.png'
    },
    amber: {
      primary: '#ea580c',
      light: '#fdba74',
      mid: '#fb923c',
      dark: '#c2410c',
      glow: 'rgba(234, 88, 12, 0.3)',
      hero_desktop: '/assets/hero_desktop_blue.png',
      hero_tablet: '/assets/hero_tablet_blue.png',
      hero_mobile: '/assets/hero_mobile_blue.png'
    },
    cyan: {
      primary: '#0891b2',
      light: '#67e8f9',
      mid: '#22d3ee',
      dark: '#0e7490',
      glow: 'rgba(8, 145, 178, 0.3)',
      hero_desktop: '/assets/hero_desktop_blue.png',
      hero_tablet: '/assets/hero_tablet_blue.png',
      hero_mobile: '/assets/hero_mobile_blue.png'
    },
    pink: {
      primary: '#d5546d',
      light: '#ffa8b9',
      mid: '#e28799',
      dark: '#b7495e',
      glow: 'rgba(213, 84, 109, 0.3)',
      hero_desktop: 'https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png',
      hero_tablet: 'https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png',
      hero_mobile: 'https://framerusercontent.com/images/fXqibY48KxkV3CU0IWsPA4c61XM.png'
    }
  };

  function applyTheme(name) {
    const t = THEMES[name] || THEMES.blue;
    document.documentElement.style.setProperty('--token-7395beff-cbd1-4ab6-8298-561b3ea84b05', t.primary);
    document.documentElement.style.setProperty('--accent-color', t.primary);
    document.documentElement.style.setProperty('--accent-light', t.light);
    document.documentElement.style.setProperty('--accent-mid', t.mid);
    document.documentElement.style.setProperty('--accent-dark', t.dark);
    document.documentElement.style.setProperty('--accent-glow', t.glow);

    // Update active button state
    document.querySelectorAll('.theme-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.color === name);
    });

    // Update SVGs stroke colors
    document.querySelectorAll('svg path, svg line').forEach(el => {
      const stroke = el.getAttribute('stroke');
      if (stroke && (stroke === '#2563eb' || stroke === '#d5546d' || stroke === '#059669' || stroke === '#7c3aed' || stroke === '#ea580c' || stroke === '#0891b2')) {
        el.setAttribute('stroke', t.primary);
      } else if (stroke && (stroke === '#93c5fd' || stroke === '#ffa8b9' || stroke === '#6ee7b7' || stroke === '#c4b5fd' || stroke === '#fdba74' || stroke === '#67e8f9')) {
        el.setAttribute('stroke', t.light);
      }
    });

    // Update hero banner images
    document.querySelectorAll('img').forEach(img => {
      const src = img.getAttribute('src') || '';
      if (src.includes('hero_desktop') || src.includes('ZIGGNTa59t23FnqZrTBBmnU8Rxk')) {
        img.src = t.hero_desktop;
        img.srcset = t.hero_desktop;
      } else if (src.includes('hero_tablet') || src.includes('6Uxw6b3gvj4edJoZKCESNTqnc')) {
        img.src = t.hero_tablet;
        img.srcset = t.hero_tablet;
      } else if (src.includes('hero_mobile') || src.includes('fXqibY48KxkV3CU0IWsPA4c61XM')) {
        img.src = t.hero_mobile;
        img.srcset = t.hero_mobile;
      }
    });

    try { localStorage.setItem('user_theme', name); } catch(e){}
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.theme-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        applyTheme(btn.dataset.color);
      });
    });

    const saved = localStorage.getItem('user_theme') || 'blue';
    applyTheme(saved);
  });
})();
</script>
"""

def transform_html(content):
    # 1. Replace script & module URLs to local framer_dist/
    content = content.replace('https://framerusercontent.com/sites/2Lchxi9LzakPkRuMF1bj1g/', '/framer_dist/')
    
    # 2. Replace color tokens & styles
    for old_c, new_c in COLOR_REPLACEMENTS:
        content = content.replace(old_c, new_c)
        
    # 3. Replace hero banner images
    for pattern, rep in HERO_REPLACEMENTS:
        content = re.sub(pattern, rep, content)
        
    # 4. Insert theme switcher right before </body>
    if '</body>' in content:
        content = content.replace('</body>', THEME_SWITCHER_SNIPPET + '\n</body>')
    else:
        content += THEME_SWITCHER_SNIPPET
        
    return content

# 1. Transform root index.html
with open('framer_site_raw.html', 'r', encoding='utf-8') as f:
    raw_home = f.read()

home_transformed = transform_html(raw_home)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_transformed)
print("Updated index.html (Framer Home)")

# 2. Transform all route pages
os.makedirs('framer_pages_transformed', exist_ok=True)
for page_path in glob.glob('framer_pages/*.html'):
    name = os.path.basename(page_path)
    with open(page_path, 'r', encoding='utf-8') as f:
        page_content = f.read()
    page_transformed = transform_html(page_content)
    with open(f'framer_pages_transformed/{name}', 'w', encoding='utf-8') as f:
        f.write(page_transformed)
    print(f"Transformed page {name}")

print("All HTML pages prepared!")
