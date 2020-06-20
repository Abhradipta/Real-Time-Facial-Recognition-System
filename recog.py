import cv2
import numpy as np
from PIL import Image
import os

def getImagesAndLabels(detector):

    faceSamples=[]
    ids= []

    count=0

    for each in os.listdir(os.curdir):
        if not each.startswith("s"):
            continue
        if each.startswith("st") or each.startswith("sm"):
            continue
        for get_image_path in os.listdir(each):
            count+=1
            actual_path=each+"/"+get_image_path
            print(actual_path)

            PIL_img = Image.open(actual_path).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(each[1:])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

    f=open("admin_files/trained.txt",'w')
    f.write(str(count))
    f.close()

    return faceSamples,ids

def begin():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path="./haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(path)
    
    faces,ids = getImagesAndLabels(detector)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer.yml')
    

