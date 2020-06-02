from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

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
    return redirect("/welcome")

def new_register(request):
    return render(request, 'register.html')

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST["email"])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session["user"] = logged_user.first_name
            request.session["id"] = logged_user.id
            return redirect("/welcome")
    return redirect("/")

def logout(request):
    request.session.clear()
    print(request.session)
    return redirect("/")   

def welcome(request):
    return render(request, 'welcome.html')

def pick_mat(request):
    
    return render(request, 'pick_materials.html')

def results(request):
    formdata = User.objects.all()
    return render(request, "results.html")

def process(request):
    print(request.POST)
    pricing = {
        'cedar': 2.49,
        'trex': 2.17,
    }
    type_of_wood = request.POST['type']
    
    width = request.POST['type'][2]
    print(width, "this is the width")
    # figure out area of deck
    area = int(request.POST['length'][0]) * int(request.POST['width'][0])
    print(area, "this is the Area")


# I Need To Get This Calculation Working Properly, It is Not at the current moment!


    # how many boards to cover length of deck
    boards_for_length = int(request.POST['length'][0])*int(type_of_wood[4])
    print(boards_for_length, "here is the Number Of Boards")
    # how many boards to cover width of deck
    boards_for_width = int(request.POST['width'][0])*int(type_of_wood[2])
    print(boards_for_width, "Here are the Boards For Width")
   
    
    # end of Problem


    # spacing between boards
    total_spacing = boards_for_width * float(request.POST['spacing'])
    print(total_spacing, "here is the total Spacing")
    # final board count
    true_area = area - total_spacing
    print(true_area, "here is the True Area")
    total_boards = boards_for_length * boards_for_width
    print(total_boards, "Here are the Total Boards")

    # final pricing
    
    final_price = total_boards*pricing[request.POST['wood_type']]
    context = {
        "final_price": final_price
    }
    return render(request, "results.html", context)

def render_home(request):
        return render(request, "home.html")