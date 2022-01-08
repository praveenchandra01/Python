import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(
    "Resources/haarcascade_frontalface_default.xml")
# img = cv2.imread('Resources/1.jpg')
while True:
    success,img=cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 9)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # cv2.imshow("Result", img)

    cv2.imshow("Output",img)
    # cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

