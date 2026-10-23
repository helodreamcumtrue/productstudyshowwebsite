from PIL import Image
import numpy as np

def recolor_image(input_path, output_path, target_hue=218/360.0): # 218 deg is electric cobalt blue
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img, dtype=np.float32)

    r, g, b, a = arr[:,:,0]/255.0, arr[:,:,1]/255.0, arr[:,:,2]/255.0, arr[:,:,3]
    
    # Vectorized RGB to HSV
    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    diff = cmax - cmin

    # Hue calculation
    h = np.zeros_like(r)
    mask_r = (cmax == r) & (diff > 0)
    mask_g = (cmax == g) & (diff > 0)
    mask_b = (cmax == b) & (diff > 0)

    h[mask_r] = ((g[mask_r] - b[mask_r]) / diff[mask_r]) % 6.0
    h[mask_g] = ((b[mask_g] - r[mask_g]) / diff[mask_g]) + 2.0
    h[mask_b] = ((r[mask_b] - g[mask_b]) / diff[mask_b]) + 4.0
    h = h / 6.0 # Normalize 0 to 1

    # Saturation
    s = np.zeros_like(r)
    s[cmax > 0] = diff[cmax > 0] / cmax[cmax > 0]

    # Value
    v = cmax

    # Pink / Magenta / Crimson range:
    pink_mask = ((h >= 0.90) | (h <= 0.05)) & (s > 0.18) & (v > 0.20)

    # Shift pink hue to target_hue (e.g. 218/360 = 0.605, Cobalt Blue)
    new_h = np.copy(h)
    new_h[pink_mask] = target_hue
    
    new_s = np.copy(s)
    new_s[pink_mask] = np.clip(s[pink_mask] * 1.05, 0, 1.0)

    # Convert back from HSV to RGB
    c = v * new_s
    x = c * (1.0 - np.abs(((new_h * 6.0) % 2.0) - 1.0))
    m = v - c

    new_r = np.zeros_like(r)
    new_g = np.zeros_like(g)
    new_b = np.zeros_like(b)

    cond0 = (new_h >= 0) & (new_h < 1/6)
    cond1 = (new_h >= 1/6) & (new_h < 2/6)
    cond2 = (new_h >= 2/6) & (new_h < 3/6)
    cond3 = (new_h >= 3/6) & (new_h < 4/6)
    cond4 = (new_h >= 4/6) & (new_h < 5/6)
    cond5 = (new_h >= 5/6) & (new_h <= 1.0)

    new_r[cond0], new_g[cond0], new_b[cond0] = c[cond0], x[cond0], 0
    new_r[cond1], new_g[cond1], new_b[cond1] = x[cond1], c[cond1], 0
    new_r[cond2], new_g[cond2], new_b[cond2] = 0, c[cond2], x[cond2]
    new_r[cond3], new_g[cond3], new_b[cond3] = 0, x[cond3], c[cond3]
    new_r[cond4], new_g[cond4], new_b[cond4] = x[cond4], 0, c[cond4]
    new_r[cond5], new_g[cond5], new_b[cond5] = c[cond5], 0, x[cond5]

    out_r = np.where(pink_mask, new_r + m, r)
    out_g = np.where(pink_mask, new_g + m, g)
    out_b = np.where(pink_mask, new_b + m, b)

    out_arr = np.stack([
        np.clip(out_r * 255.0, 0, 255).astype(np.uint8),
        np.clip(out_g * 255.0, 0, 255).astype(np.uint8),
        np.clip(out_b * 255.0, 0, 255).astype(np.uint8),
        np.clip(a, 0, 255).astype(np.uint8)
    ], axis=-1)

    out_img = Image.fromarray(out_arr, 'RGBA')
    out_img.save(output_path, 'PNG')
    print(f"Saved recolored image to {output_path} (shifted {np.sum(pink_mask)} pixels)")

recolor_image('assets/hero_desktop.png', 'assets/hero_desktop_blue.png')
recolor_image('assets/hero_tablet.png', 'assets/hero_tablet_blue.png')
recolor_image('assets/hero_mobile.png', 'assets/hero_mobile_blue.png')
