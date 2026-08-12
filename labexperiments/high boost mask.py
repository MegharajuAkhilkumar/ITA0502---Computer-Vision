import cv2

img = cv2.imread("micky.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

A = 2
sharp = cv2.addWeighted(gray, A, blur, -(A - 1), 0)

cv2.imshow("Original Image", gray)
cv2.imshow("High-Boost Sharpened Image", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
