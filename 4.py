import cv2
import numpy as np

src1 = cv2.imread("City17.webp")
new_dim = (200, 200)
src2 = cv2.resize(src1, new_dim, interpolation=cv2.INTER_CUBIC)
new_dim2 = (800, 800)
src3
src3 = cv2.resize(src2, new_dim2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Original", src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Resized", src2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Resized2", src3)
cv2.waitKey(0)
cv2.destroyAllWindows()
