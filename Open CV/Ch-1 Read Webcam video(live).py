import cv2
cap=cv2.VideoCapture(0)
cap.set(3,800)  #width
cap.set(4,440)  #height
cap.set(10,100) #brightmess

while True:
    success,img=cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

