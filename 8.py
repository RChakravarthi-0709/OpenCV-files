import cv2
import numpy as np

master = []
src = cv2.imread("City1.png")
master.append(src)

src = cv2.imread("City2.png")
master.append(src)

src = cv2.imread("City3.png")
master.append(src)

src = cv2.imread("City4.png")
master.append(src)

src = cv2.imread("City5.png")
master.append(src)

src = cv2.imread("City6.png")
master.append(src)

src = cv2.imread("City7.png")
master.append(src)

src = cv2.imread("City8.png")
master.append(src)

src = cv2.imread("City9.png")
master.append(src)

h1 = np.hstack(master)
cv2.imwrite("Image5.png", h1)