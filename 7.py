import cv2
import numpy as np

src1 = cv2.imread("City1.png")
src2 = cv2.imread("City2.png")
src3 = cv2.imread("City3.png")

src4 = cv2.imread("City4.png")
src5 = cv2.imread("City5.png")
src6 = cv2.imread("City6.png")

src7 = cv2.imread("City7.png")
src8 = cv2.imread("City8.png")
src9 = cv2.imread("City9.png")

h1 = np.hstack([src1, src2, src3])
h2 = np.hstack([src4, src5, src6])
h3 = np.hstack([src7, src8, src9])

v1 = np.vstack([h1, h2, h3])
cv2.imwrite("Image4.png", v1)