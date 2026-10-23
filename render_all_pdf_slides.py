import fitz
import os

os.makedirs('assets/slides/discord', exist_ok=True)
os.makedirs('assets/slides/dominos', exist_ok=True)
os.makedirs('assets/slides/insta', exist_ok=True)
os.makedirs('assets/slides/pnb', exist_ok=True)

pdf_map = {
    'pnb': 'PNB Redesign by Lakshay.pdf',
    'discord': 'Discord product teardown by Lakshay.pdf',
    'dominos': 'Domino_s product teardown by Lakshay.pdf',
    'insta': 'Insta product teardown by Lakshay.pdf'
}

for key, pdf_name in pdf_map.items():
    doc = fitz.open(pdf_name)
    print(f"Rendering {pdf_name} ({len(doc)} pages)...")
    for i, page in enumerate(doc):
        # Render high-res 150 DPI
        pix = page.get_pixmap(dpi=150)
        out_path = f'assets/slides/{key}/page_{i+1}.png'
        pix.save(out_path)
    print(f"Done {key}: {len(doc)} pages saved to assets/slides/{key}/")

print("All slides rendered successfully!")
