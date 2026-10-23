import urllib.request
import re

url = 'https://framerusercontent.com/sites/2Lchxi9LzakPkRuMF1bj1g/script_main.DbzaP8xY.mjs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    js = resp.read().decode('utf-8')

print("Main JS size:", len(js))
with open('script_main.mjs', 'w', encoding='utf-8') as f:
    f.write(js)

# Find routes in script_main
routes = re.findall(r'\"(/[^\"]*)\"', js)
print("Routes/Paths found:")
for r in set(routes):
    if len(r) < 30 and not r.endswith('.mjs'):
        print("  ", r)

# Find imported modules
imports = re.findall(r'from\s*[\"\']([^\"\']+)[\"\']|import\s*[\"\']([^\"\']+)[\"\']', js)
print("\nImports:")
for imp in set([i[0] or i[1] for i in imports]):
    print("  ", imp)
