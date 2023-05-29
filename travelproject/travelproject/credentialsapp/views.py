from django.contrib.auth.models import User
from django.contrib import messages, auth

from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"User already exist")
                #return  redirect('register')
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                #return  redirect('register')
                return render(request, "register.html")
            else:
                 user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                 user.save();
                 return redirect('login')
                 #print("User created")
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
            #print("User not created")
            #return render (request,"register.html")

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return  redirect('/')