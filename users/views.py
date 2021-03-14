from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
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
	posts = request.user.post_set.all().order_by('-date_posted')
	return render(request,'users/profile.html',{'posts'  : posts })

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
	