import cv2
import numpy as np

img = cv2.imread("micky.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = np.array([
    [1,  1,  1],
    [1, -8,  1],
    [1,  1,  1]
])

lap = cv2.filter2D(gray, cv2.CV_64F, mask)

sharp = cv2.convertScaleAbs(gray.astype(np.float64) - lap)

cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
