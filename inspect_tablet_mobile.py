from PIL import Image
import numpy as np

for name in ['tablet', 'mobile']:
    img = Image.open(f'assets/hero_{name}.png').convert('RGBA')
    arr = np.array(img)
    r = arr[:, :, 0].astype(int)
    g = arr[:, :, 1].astype(int)
    b = arr[:, :, 2].astype(int)
    a = arr[:, :, 3].astype(int)
    pink_mask = (a > 50) & (r > 120) & (r > g + 30) & (r > b + 10)
    unique_pinks = np.unique(arr[pink_mask][:, :3], axis=0)
    print(f"{name} pink pixels count: {np.sum(pink_mask)}, unique: {len(unique_pinks)}")
    for p in unique_pinks:
        print(f"  #{p[0]:02x}{p[1]:02x}{p[2]:02x}")
