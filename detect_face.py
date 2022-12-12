import cv2

import os
os.chdir(os.path.dirname(__file__)) #상대경로 사용시 에러방지

front_face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier('./xml/haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)
image = cv2.imread('./image/Cats.jpg') #임의로 넣은 이미지 파일 입니다.

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)# 좌우대칭을 마춰줌
    if ret:
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        front_faces = front_face_cascade.detectMultiScale(gray, 1.05, 1, minSize=(100,100))
        profile_faces = profile_face_cascade.detectMultiScale(gray,1.1,4)

        if len(front_faces) > 0 or len(profile_faces) > 0:
            for (x,y,w,h) in profile_faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('Video',frame)
        else:
            cv2.imshow('Video',image)
      
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
