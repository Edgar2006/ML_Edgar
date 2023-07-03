import cv2

image = cv2.imread("Vrej", cv2.IMREAD_COLOR)


grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Blac and whithe Image", grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

