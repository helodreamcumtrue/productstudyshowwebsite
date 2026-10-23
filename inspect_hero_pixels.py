from PIL import Image
import numpy as np

img = Image.open('assets/hero_desktop.png')
print("Image format:", img.format, "size:", img.size, "mode:", img.mode)

rgba = img.convert('RGBA')
arr = np.array(rgba)
print("arr shape:", arr.shape)

# Let's count colors with red > green and red > blue (pink shades)
r = arr[:, :, 0].astype(int)
g = arr[:, :, 1].astype(int)
b = arr[:, :, 2].astype(int)
a = arr[:, :, 3].astype(int)

# Identify non-transparent pinkish pixels
pink_mask = (a > 50) & (r > 120) & (r > g + 30) & (r > b + 10)
print(f"Pink pixels count: {np.sum(pink_mask)}")

# Let's see unique RGB values in pink_mask
unique_pinks = np.unique(arr[pink_mask][:, :3], axis=0)
print(f"Unique pink colors: {len(unique_pinks)}")
print("Sample pinks:")
for p in unique_pinks[:15]:
    print(f"  #{p[0]:02x}{p[1]:02x}{p[2]:02x} - RGB({p[0]}, {p[1]}, {p[2]})")
