from django.shortcuts import render
from os import listdir
import cv2
import sys
from PIL import Image
import start
import remote_start

def fetch(request):
    user=request.user.username
    files=listdir(user+'/')
    l=len(files)

    get=request.FILES['id_image']
 
    path=user+"/img"+str(l+1)+".jpg"
    img=Image.open(get)
    img.save(path)

    return render(request,'page2.html',{'msg':'Got your image uploaded'})

def face(request):
    usr=request.user.username
    arr=listdir(usr)
    l=len(arr)
    if(l==0):
        msg=''
    else:
        msg=str(l)
    return render(request,'page1.html',{'msg':msg})

def get_face(request):
    usr=request.user.username
    arr=listdir(usr)
    l=len(arr)
    start.record_vid(usr,l)
    return render(request,'page2.html',{'msg':'Fetched images'})

def get_face_remote(request):
    usr=request.user.username
    arr=listdir(usr)
    l=len(arr)

    url=request.POST['link']
    print(url)

    try:
        remote_start.record_vid(usr,l,url)

    except:
        pass
    return render(request,'page2.html',{'msg':'Server did not start or completed fetching images'})