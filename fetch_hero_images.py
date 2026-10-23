import urllib.request
from PIL import Image
import io

urls = [
    ('desktop', 'https://framerusercontent.com/images/ZIGGNTa59t23FnqZrTBBmnU8Rxk.png'),
    ('tablet', 'https://framerusercontent.com/images/6Uxw6b3gvj4edJoZKCESNTqnc.png'),
    ('mobile', 'https://framerusercontent.com/images/fXqibY48KxkV3CU0IWsPA4c61XM.png')
]

for name, u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    img = Image.open(io.BytesIO(data))
    print(f"{name}: size={img.size}, mode={img.mode}, bytes={len(data)}")
    with open(f"assets/hero_{name}.png", "wb") as f:
        f.write(data)
    print(f"  saved to assets/hero_{name}.png")
