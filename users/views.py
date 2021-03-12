from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def indexView(request):
    if(request.user.is_authenticated):
        pass
    return render(request,'users/index.html')

def loginView(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if(next):
                return redirect(next)
            return redirect('indexView')
        else:
           messages.warning(request,f'Username and Password combination does not match')

    return render(request,'users/login.html')

def logoutView(request):
    logout(request)
    return redirect('indexView')

def signupView(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password)
        profile = Profile.objects.create(user=user)
        profile.save()
        return redirect('loginView')
    return render(request,'users/signup.html')        

@login_required
def profileView(request):
    # post
    return render(request,'users/profile.html',{})