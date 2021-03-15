from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from posts.models import Post
from .forms import UserUpdateForm,ProfileUpdateForm

def indexView(request):
	if(request.user.is_authenticated):
		posts = Post.objects.all().order_by('-date_posted')
		return render(request,'users/index.html',{'posts':posts})
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

def changePasswordView(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/')
		else:
			return render(request,'users/changePassword.html',{'form':form})

	form = PasswordChangeForm(request.user)
	return render(request,'users/changePassword.html',{'form':form})

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
def profileView(request,usr):
	user = User.objects.filter(username=usr).first()
	if user is not None:
		posts = Post.objects.filter(author=user)
		context={
			'userobj': user,
			'posts'  : posts 
		}
		return render(request,'users/profile.html',context)	
	return HttpResponse('404')

@login_required
def profileEditView(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST,instance=request.user)
		profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		# instance is passsed to form because it has to know what User and Profile it has to update
		# if it is not passed it will try to create an another new object for User and Profile
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,f'Profile Successfully Updated')
			return redirect('/profile')		

	user_form = UserUpdateForm(instance=request.user)
	profile_form = ProfileUpdateForm(instance=request.user.profile)
	context = { 
		'user_form':user_form,
		'profile_form':profile_form
	}
	return render(request,'users/profileEdit.html',context)
	