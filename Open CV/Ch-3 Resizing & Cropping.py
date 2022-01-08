import cv2

img=cv2.imread("Resources/1.jpg")
print(img.shape)


imgResize=cv2.resize(img,(300,400))

imgCropped=img[0:200,150:350]  #height,width

cv2.imshow("img",img)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCropped",imgCropped)


cv2.waitKey(0)