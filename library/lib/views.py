from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Student
from django . shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


def loginn(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user2 = Student.objects.get(email=email)
            print(user,user2)
        except Exception as e:
            print(f"error is {e}")
            print("user does not exist")
        user2 = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("invalid credentials")
    
    return render(request,'login.html')
    

def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("firstname")
            email = request.POST.get("email")
            usn = request.POST.get("usn")
            password = request.POST.get("password")
            first_name = request.POST.get("firstname")
            last_name = request.POST.get("lastname")
            
           

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered. Use a different email.')
                return redirect('signup')

            
            my_user = User.objects.create_user(username, email, password)

            # Create the Student object and associate it with the User
            user = Student.objects.create(
                user=my_user,
                student_id=usn,
                email=email,
                first_name=first_name,
                last_name=last_name,
                
            )

            
            my_user.save()
            user.save()

            
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home')

    except Exception as e:
        print(f"Error during signup: {e}")
        messages.error(request, 'An error occurred during signup.')
        return redirect('signup')

    return render(request, 'signup.html')




@login_required(login_url='login/')
def home(req):
    return render(req,'home.html')


@login_required(login_url='login/')
def logoutt(request):
    print("logging out ",request.user)
    logout(request)
    return redirect('/')




