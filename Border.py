import cv2

img = cv2.imread("img.png")
borderedImage = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=1)

cv2.imshow("borderedImage",borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()