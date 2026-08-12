import cv2
import numpy as np

img = cv2.imread("micky.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(gx, gy)

gradient = cv2.convertScaleAbs(gradient)

mask = cv2.normalize(gradient, None, 0, 1, cv2.NORM_MINMAX,
                     dtype=cv2.CV_32F)

sharp = gray.astype(np.float32) + mask * gray.astype(np.float32)

sharp = np.clip(sharp, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Sharpened Image", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
