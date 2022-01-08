import cv2
import numpy as np 

img=np.zeros((512,512,3),np.uint8)
# print(img)
img[:]=55,55,200
# img[200:300,100:300]=55,55,200


# Line 
# cv2.line(img,(0,0),(300,300),(0,255,22),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,22),3)  #Height,width

# Rectangle
# cv2.rectangle(img,(0,0),(300,300),(55,55,55),cv2.FILLED)  
cv2.rectangle(img,(0,0),(300,300),(55,55,55),3)


# Circle
cv2.circle(img,(300,300),90,(100,160,0),3)

# Put Text on image
cv2.putText(img,"Praveen",(350,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,55,255),2) #Scale,color,thicknes


cv2.imshow("Output",img)
cv2.waitKey(0)