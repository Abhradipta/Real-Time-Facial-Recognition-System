import cv2
import os
import sys
import requests
import numpy as np
 
def record_vid(id,l,url):

    path='haarcascade_frontalface_default.xml'
    face_detector = cv2.CascadeClassifier(path)
 
    face_id = id
 
    count = 0
 
    while(True): 
        site=requests.get(url)
        img_arr=np.array(bytearray(site.content),dtype=np.uint8)
        img=cv2.imdecode(img_arr,-1)

        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.2, 3)
 
        for (x,y,w,h) in faces:
 
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
 
            cv2. imwrite(str(face_id) + '/' + str(count+l) + '.jpg', gray[y:y+h,x:x+w])
 
        cv2.imshow('image', img)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count == 15:
            return 