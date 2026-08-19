import cv2

img = cv2.imread("micky.png")

if img is None:
    print("Image not found")
    exit()

watermark = "AKHIL KUMAR"

cv2.putText(img, watermark, (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2)

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
