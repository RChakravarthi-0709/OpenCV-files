import cv2
import numpy as np

src1 = cv2.imread("City1.png")
new_dim = (1000,1000)
src2 = cv2.resize(src1, new_dim, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Original",src1)
cv2.imshow("Resized", src2)
cv2.waitKey(0)
cv2.destroyAllWindows()