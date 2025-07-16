import cv2
import numpy as np

def collage(outfile):
    src1 = cv2.imread("City1.png")
    src2 = cv2.imread("City2.png")
    src3 = cv2.imread("City3.png")
    src4 = cv2.imread("City4.png")

    src5 = cv2.imread("City5.png")
    src6 = cv2.imread("City6.png")
    src7 = cv2.imread("City7.png")
    src8 = cv2.imread("City8.png")

    src9 = cv2.imread("City9.png")
    src10 = cv2.imread("City10.png")
    src11 = cv2.imread("City11.png")
    src12 = cv2.imread("City12.png")

    src13 = cv2.imread("City13.png")
    src14 = cv2.imread("City14.png")
    src15 = cv2.imread("City15.png")
    src16 = cv2.imread("City16.png")

    h_stack1 = np.hstack([src1,src2, src3, src4])
    h_stack2 = np.hstack([src5, src6, src7, src8])
    h_stack3 = np.hstack([src9, src10, src11, src12])
    h_stack4 = np.hstack([src13, src14, src15, src16])

    v_stack1 = np.vstack([h_stack1, h_stack2, h_stack3, h_stack4])
    cv2.imwrite(outfile, v_stack1)

collage("Image2.png")
