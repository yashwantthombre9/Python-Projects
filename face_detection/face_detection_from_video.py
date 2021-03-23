### software and hardware requirements

# 1) download 'haarcascade_frontalface_default.xml' file
# 2) install opencv2 python framework in order to use functionality of the same


import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture  = cv2.VideoCapture(0)
while True:
    _,img = capture.read()
    


    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,10)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
capture.release()
