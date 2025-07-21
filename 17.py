import cv2
import numpy as np
new_dim1 = (200, 200)
watermark = cv2.imread("Watermark.png")
watermark = cv2.resize(watermark, new_dim1, interpolation=cv2.INTER_LINEAR)
watermark_rgb = watermark
watermark_alpha = np.ones(watermark.shape[:2], dtype=np.uint8) * 100
alpha_mask = cv2.merge([watermark_alpha, watermark_alpha, watermark_alpha]) / 255
for i in range(1, 17):
    src = cv2.imread(f"City{i}.png")
    src = cv2.resize()
    watermarked = (src * (1 - alpha_mask) + watermark_rgb * alpha_mask).astype(np.uint8)
    cv2.imwrite(f"City{i}.5.jpg", watermarked)