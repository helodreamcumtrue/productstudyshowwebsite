from PIL import Image
import numpy as np

img = Image.open('assets/hero_desktop.png').convert('RGB')
arr = np.array(img)

# Let's find pixels where R is significantly higher than G and B (red/pink)
# Pink is high R, moderate G and B, with R > G and R > B
r = arr[:, :, 0].astype(int)
g = arr[:, :, 1].astype(int)
b = arr[:, :, 2].astype(int)

pink_mask = (r > 140) & (r > g + 40) & (r > b + 20) & (g < 140)
print("Total pink pixels in hero_desktop:", np.sum(pink_mask))
if np.sum(pink_mask) > 0:
    sample_r = r[pink_mask][:10]
    sample_g = g[pink_mask][:10]
    sample_b = b[pink_mask][:10]
    for sr, sg, sb in zip(sample_r, sample_g, sample_b):
        print(f"R:{sr} G:{sg} B:{sb} (hex: #{sr:02x}{sg:02x}{sb:02x})")
