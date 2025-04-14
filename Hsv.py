import cv2

image = cv2.imread("img.png")
hsvImg = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("normal",image)
cv2.imshow("HSV",hsvImg)
cv2.waitKey(0)
cv2.destroyAllWindows()