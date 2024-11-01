from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return redirect ('signup')
        user = user.object.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,'signup successful! please login')
        return redirect ('login')
    return render (request,'accounts/signup.html')

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'Invalid login')
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required
def homepage_view(request):
    return render(request,'accounts/homepage.html')

def logout_view(request):
    logout(request)
    return redirect('login')





