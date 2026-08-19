import cv2
import numpy as np

img = cv2.imread("micky.png", 0)

if img is None:
    print("Image not found")
    exit()

kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
