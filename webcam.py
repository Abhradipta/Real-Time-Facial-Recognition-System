import cv2
import sys
import requests
import numpy as np
import alerts
import datetime
import time

def remote(url,names):
    file1=open("admin_files/logs.txt","a+")
    file2=open("admin_files/mobile_no.txt","r")

    data=file2.read()
    file2.close()


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    cascadePath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

    #Variable to counter valid and invalid
    valid=0
    invalid=0

    flag=0
    while (flag==0):

        site=requests.get(url)
        img_arr=np.array(bytearray(site.content),dtype=np.uint8)
        img=cv2.imdecode(img_arr,-1)


        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 3,
            minSize=(10,10)
        )

     
        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            text=""
            if(confidence<48):
                valid+=1
                text=names[id]
                if(valid>=60):
                    
                    cv2.putText(img, str("Logged to system"), (x+5,y-5), font, 1, (255,255,255), 2)                     
                    cv2.putText(img, str("Paused for few minutes.."), (x+5,y+5+270), font, 1, (255,255,255), 2)     
                    cv2.imshow('camera',img)
                    if  cv2.waitKey(1) &0xFF == ord('q'):
                        flag=1
                        break

                    x=datetime.datetime.now()
                    x=x.strftime("%m/%d/%Y, %H:%M:%S")
                    msg="\n "+text+" logged at "+x
                    file1.write(msg)
                    valid=0
                    invalid=0
                    
                    time.sleep(3)
                    
                else:
                    cv2.putText(img, str("Detected "+text), (x+5,y-5), font, 1, (255,255,255), 2) 
                    cv2.imshow('camera',img) 
                    if  cv2.waitKey(1) &0xFF == ord('q'):
                        flag=1
                        break

            else:
                invalid+=1
                if(invalid>=150):
                    cv2.putText(img, str("Cannot detect the face system will be alerted.."), (x+5,y-5), font, 1, (255,255,255), 2) 
                    cv2.imshow('camera',img)
                    if  cv2.waitKey(1) &0xFF == ord('q'):
                        flag=1
                        break

                    alerts.alert(data)
                    invalid=0
                    valid=0
                else:
                    cv2.putText(img, str("Detecting.."), (x+5,y-5), font, 1, (255,255,255), 2) 
                    cv2.imshow('camera',img)                                 
                    if  cv2.waitKey(1) &0xFF == ord('q'):
                        flag=1
                        break

        cv2.imshow('camera',img)                          
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.release()
    cv2.destroyAllWindows()

    file1.close()
