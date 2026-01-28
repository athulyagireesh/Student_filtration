from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # stds = Students.objects.all()
        # courses =[]
        # if request.method=='POST':
        # course = request.POST['course']
        # stds = Students.objects.filter(course=course)
        stds =Students.objects.filter(uname=request.user.pk)
        return render(request,'index.html',{'stds':stds})
    else:
        return redirect(loginUser)


def addstudent(request):
    if request.user.is_authenticated:
         courses=Course.objects.all()
         if request.method=='POST':
             name=request.POST['name']
             email=request.POST['email']
             age=request.POST['age']
             phone=request.POST['phone']
             course=request.POST['course']
             cname=Course.objects.get(cname=course)
             data=Students.objects.create(name=name,email=email,age=age,phone=phone,cname=cname,uname=request.user)
             data.save()
        # return redirect(index)
         return render(request,'addstudent.html',{'courses':courses})
    else:
         return redirect(loginUser)




def editstudents(request,pk):
    std=Students.objects.get(pk=pk)
    course=Course.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        course=request.POST['course']
        cname=Course.objects.get(cname=course)
        Students.objects.filter(pk=pk).update(name=name,email=email,age=age,phone=phone,cname=cname)
        return redirect(index)
    return render(request,'editstudents.html',{'std':std,'courses':course})


def delete(request,pk):
    Students.objects.get(pk=pk).delete()
    return redirect(index)


def registerUser(request):
    if request.method=='POST':
        name=request.POST['firstname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cnf_password=request.POST['cnf_password']
        if password == cnf_password:
            data = User.objects.create_user(first_name=name,username=username,email=email,password=password)
            data.save()
            return redirect(loginUser)
        else:
             print('password does not match')
    return render(request,'register.html')
    

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(index)
        else:
            return redirect(loginUser)
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect(loginUser)