import cv2
import numpy as np
def cv2_util1(image_fname, new_dim1):
    watermark_fname = "Watermark.png"
    watermark = cv2.imread(watermark_fname)
    watermark = cv2.resize(watermark, new_dim1, interpolation=cv2.INTER_LINEAR)
    watermark_rgb = watermark
    watermark_alpha = np.ones(watermark.shape[:2], dtype=np.uint8) * 100
    alpha_mask = cv2.merge([watermark_alpha, watermark_alpha, watermark_alpha]) / 255
    for i in range(1, 17, 1):
        src = cv2.imread(f"{image_fname}{i}.png")
        watermarked = (src * (1-alpha_mask) + watermark_rgb * alpha_mask).astype(np.uint8)
        cv2.imwrite(f"{image_fname}{i}.5.jpg", watermarked)
cv2_util1("City", (200,200))