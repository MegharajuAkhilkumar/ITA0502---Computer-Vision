import cv2

img1 = cv2.imread("micky.png")
img2 = cv2.imread(r"D:\Downloads\download.jpg")

if img1 is None or img2 is None:
    print("Image not found")
    exit()

# Crop part of first image
crop = img1[50:200, 50:200]

# Resize crop
crop = cv2.resize(crop, (150, 150))

# Paste into second image
img2[50:200, 50:200] = crop

cv2.imshow("Original Image", img1)
cv2.imshow("Cropped and Pasted Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
