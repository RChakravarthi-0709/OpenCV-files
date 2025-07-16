import cv2
import numpy as np

master = []
for i in range(1, 17, 1):
    src = cv2.imread(f"City{i}.png")
    master.append(src)

h1 = np.hstack(master)
cv2.imwrite("Image6.png", h1)