import urllib.request
import os

routes = [
    'about',
    'enterprise-readiness',
    'show-me-the-money',
    'you-are-okay',
    'ca-founder-collab',
    '8club-onboarding-video',
    'custom-access-controls'
]

os.makedirs('framer_pages', exist_ok=True)

for r in routes:
    url = f'https://adyatha.framer.website/{r}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
        with open(f'framer_pages/{r}.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fetched /{r}: {len(content)} bytes")
    except Exception as e:
        print(f"Error fetching /{r}: {e}")
