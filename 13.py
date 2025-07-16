import cv2
import numpy as np

def collage(name, size, outfile):
    master = []
    for i in range(1, size+1, 1):
        src = cv2.imread(f"{name}{i}.png")
        master.append(src)

    h1 = np.hstack(master)
    cv2.imwrite(outfile, h1)
collage("City", 16,"Image10.png")