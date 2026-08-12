import cv2
import numpy as np

img = cv2.imread("micky.png")

mask = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, mask)

cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
