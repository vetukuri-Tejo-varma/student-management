from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
from studentapp.models import *

def login_fun(request):
    if request.method == "POST":
        username = request.POST['txtname']
        password = request.POST['txtpassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html",{'data':'Username and email is invalid'})
    else:
        return render(request,"login.html",{'data':''})


def register_fun(request):
    return render(request,"register.html",{'data':''})

def regdata_fun(request):
    user_name = request.POST['txtusername']
    user_password = request.POST['txtuserpassword']
    user_email = request.POST['txtemail']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, "register.html",{'data':'Username and email is already exists'})
    else:
        user = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        user.save()
        return redirect('log')

def home_fun(request):
    return render(request,"home.html")


def add_fun(request):
    City=city.objects.all()# the data will be in list format
    Course=course.objects.all()
    s1=Student()
    if request.method=='POST':
        s1.student_name=request.POST['txtname']
        s1.student_age=request.POST['txtage']
        s1.student_Phnoe=request.POST['txtphno']
        s1.student_city=city.objects.get(city_name=request.POST['ddlcity'])
        s1.student_course=course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect("add")
    else:
        return render(request,"addstudent.html",{'City_Data':City,'Course_Data':Course})


def logout_fun(request):
    logout(request)
    return redirect("/")


def disp_fun(request):
    s1 = Student.objects.all()
    return render(request,"display.html",{'data':s1})

def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    City=city.objects.all()
    Course=course.objects.all()
    if request.method=='POST':
        s1.student_name = request.POST['txtname']
        s1.student_age = request.POST['txtage']
        s1.student_Phnoe = request.POST['txtphno']
        s1.student_city = city.objects.get(city_name=request.POST['ddlcity'])
        s1.student_course = course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_Data':City,'Course_Data':Course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')