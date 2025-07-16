import cv2
import numpy as np

src1 = cv2.imread("City1.png")
src2 = cv2.imread("City2.png")

h1 = np.hstack([src2, src1])
v1 = np.vstack([src1, src2])
cv2.imwrite("Image2.png", h1)
cv2.imwrite("Image3.png", v1)