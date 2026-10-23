from PIL import Image
import numpy as np

img = Image.open('assets/hero_desktop_blue.png')
print("Blue image format:", img.format, "size:", img.size, "mode:", img.mode)

arr = np.array(img)
r, g, b, a = arr[:,:,0].astype(int), arr[:,:,1].astype(int), arr[:,:,2].astype(int), arr[:,:,3].astype(int)

# Count blue pixels
blue_mask = (a > 50) & (b > 120) & (b > r + 30)
print(f"Blue pixels count: {np.sum(blue_mask)}")

# Count remaining pink pixels
pink_mask = (a > 50) & (r > 120) & (r > g + 30) & (r > b + 10)
print(f"Remaining pink pixels count: {np.sum(pink_mask)}")

# Sample blue colors
unique_blues = np.unique(arr[blue_mask][:, :3], axis=0)
print(f"Unique blue colors: {len(unique_blues)}")
for ub in unique_blues[:10]:
    print(f"  #{ub[0]:02x}{ub[1]:02x}{ub[2]:02x} - RGB({ub[0]}, {ub[1]}, {ub[2]})")
