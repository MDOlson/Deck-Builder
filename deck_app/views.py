from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

def welcome(request):
    return redirect('/')

def m_list(request):
    return redirect('/')

def d_list(request):
    return redirect('/')

def hardware(request):
    return redirect('/')

# Logging in and registering
def register(request):
    if request.POST['pw'] != request.POST['confpw']:
        return redirect("/")
    else:
        errors = User.objects.basic_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
        request.session["user"] = new_user.first_name
        request.session["id"] = new_user.id
    return redirect("/success")

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST["email"])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session["user"] = logged_user.first_name
            request.session["id"] = logged_user.id
            return redirect("/success")
    return redirect("/")

def logout(request):
    request.session.clear()
    print(request.session)
    return redirect("/")   
