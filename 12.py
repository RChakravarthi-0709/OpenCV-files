import cv2
import numpy as np

def collage(name, outfile):
    master = []
    for i in range(1, 17, 1):
        src = cv2.imread(f"{name}{i}.png")
        master.append(src)

    h1 = np.hstack(master)
    cv2.imwrite(outfile, h1)
collage("City", "Image9.png")