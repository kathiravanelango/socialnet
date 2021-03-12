from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
def newPostView(request):
    
    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.instance.author = request.user
            form.save()
            return redirect('/')
        else:
            return render(request,'posts/newPost.html',{'form':form})
        
    form = PostForm()
    return render(request,'posts/newPost.html',{'form':form})