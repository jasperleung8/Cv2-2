import cv2

img = cv2.imread("img.png")
rows,cols,_ = img.shape

M=cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
res = cv2.warpAffine(img,M,(cols,rows))

result = cv2.rotate(img,cv2.ROTATE_90_ANITCLOCKWISE)
cv2.imshow("result",result)
cv2.imshow("original",img)
cv2.imshow("rotated",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
