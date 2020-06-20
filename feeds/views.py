from django.shortcuts import render
from os import listdir
import numpy as np
import os
import cv2
import sys
from PIL import Image
from django.contrib.auth.models import User
import recog
import identify
import webcam

def detection(request):
    return render(request,"start_captures.html")

def init_url(request):
    url=request.POST['url']

    f=open("admin_files/link.txt",'w')
    f.write(url)
    f.close()

    msg=get_files_untrained()
    return render(request,"model_detection.html",{'msg':msg})

def init_server(request):
    f=open("admin_files/link.txt",'w')
    f.write('')
    f.close()

    msg=get_files_untrained()
    return render(request,"model_detection.html",{'msg':msg})

def start(request):
    #first train the model
    subjects=['UNKNOWN']
    user_objects=User.objects.all()
    for each in user_objects:
        get_name=each.username
        if(get_name=='admin'):
            continue
        subjects.append(get_name)

    f=open("admin_files/link.txt",'r')
    url=f.read()
    f.close()


    if(url!=''):
        try:
            webcam.remote(url,subjects)
        except:
            return render(request,"start_captures.html",{'error':'Could not start detection. Check url name.'})
    else:
        identify.captures(subjects)
    return render(request,"model_detection.html")
    

def end(request):
    return render(request,"start_captures.html")

def get_files_untrained():
    f=open("admin_files/trained.txt",'r')
    s=0
    
    for each in f:
        s=int(each)

    f.close()

    #Get total files in s' folders
    count=0
    for each in os.listdir(os.curdir):
        if not each.startswith('s'):
            continue
        if each.startswith('st'):
            continue
        for j in os.listdir(each):
            count+=1

    diff=0
    if(count!=s):
        diff=count-s
    
    if(diff<0):
        diff=-diff
        
    if(diff==0):
        return "All data have been previously trained. You can skip with training process."
    else:
        return "You have "+str(diff)+" pending data. You should train the model"

def train(request):
    try:
        recog.begin()
        return render(request,"model_detection.html",{'msg':"Training over."})
    except:
        return render(request,"model_detection.html",{'msg':"Some error occured while training."})

