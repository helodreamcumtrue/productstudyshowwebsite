import urllib.request

urls = [
    'http://localhost:3000/',
    'http://localhost:3000/about',
    'http://localhost:3000/enterprise-readiness',
    'http://localhost:3000/framer_dist/script_main.DbzaP8xY.mjs',
    'http://localhost:3000/assets/hero_desktop_blue.png'
]

for u in urls:
    try:
        with urllib.request.urlopen(u) as resp:
            data = resp.read()
            ct = resp.headers.get('Content-Type')
            print(f"{u} -> {resp.status} ({ct}) length={len(data)}")
    except Exception as e:
        print(f"{u} -> ERROR: {e}")
