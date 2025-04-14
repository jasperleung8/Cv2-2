import cv2
img = cv2.imread("img.png")

edges = cv2.Canny(img,200,100)

cv2.imshow("Original",img)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

