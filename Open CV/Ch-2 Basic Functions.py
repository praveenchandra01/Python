import cv2
import numpy as np
kernal=np.ones((5,5),np.uint8)

img=cv2.imread("Resources/1.jpg")


imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(9,9),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded=cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow("Image",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)













