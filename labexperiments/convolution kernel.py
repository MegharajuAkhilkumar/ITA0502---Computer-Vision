import cv2
import numpy as np

img = cv2.imread("micky.png", 0)

if img is None:
    print("Image not found")
    exit()

# Laplacian convolution kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
