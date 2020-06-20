from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
import os
from os import listdir


def base(request):
    return render(request,"home.html")
    

def login(request): 
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass1'])
        if (user!=None):
            auth.login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"log.html",{'error':'User does not exist or password is wrong.'})
    else:
        return render(request,"log.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect("home")

def signup(request):
    if request.method=="POST":
        if request.POST['pass1']==request.POST['pass2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'sign.html',{'error':'Sorry, Username already taken.'})
            except User.DoesNotExist:

                field1=request.POST['username']
                field2=request.POST['pass1']
                field3=request.POST['first']
                field4=request.POST['last']

                if(field1 and field2 and field3 and field4):
                    user=User.objects.create_user(field1,password=field2,first_name=field3,last_name=field4)
                    auth.login(request,user)
                    os.system("mkdir "+field1)
                    return render(request,"home.html")
                else:
                    return render(request,'sign.html',{'error':'* Fill all details *'})

        else:
            return render(request,'sign.html',{'error':'Sorry, Passwords do not match.'}) 
    else:
        return render(request,'sign.html')


def profile(request):
    if request.method=="POST":
        no=request.POST['mobile']
        file=open("admin_files/mobile_no.txt","w")
        file.write(no)
        file.close()

       
    mobile_no=""
    file=open("admin_files/mobile_no.txt","r")
    mobile_no=file.read()
    file.close()

    return render(request,'profile.html',{'no':mobile_no})

def logs(request):
    if request.method=="POST":
        file=open("admin_files/logs.txt","w")
        file.write("")
        file.close()

    file=open("admin_files/logs.txt","r")
    data=file.readlines()
    file.close()

    return render(request,'logs.html',{'data':data})

def about(request):
    user=request.user.username
    if request.method=='POST':
        user_obj=User.objects.get(username=request.user.username)
        fn=request.POST['fname']
        ln=request.POST['lname']
        user_obj.first_name=fn
        user_obj.last_name=ln
        user_obj.save()

        arr=listdir(user)
        l=len(arr)

        return render (request,'about.html',{'fn':fn,'ln':ln,'record':l})

    else:
        fn=request.user.first_name
        ln=request.user.last_name

        arr=listdir(user)
        l=len(arr)

        return render (request,'about.html',{'fn':fn,'ln':ln,'record':l})