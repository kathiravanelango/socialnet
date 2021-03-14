from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
@login_required
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

@login_required
def singlePostView(request,id):
    try:
        post = Post.objects.get(pk=id)
    except:
        return HttpResponse('404')
    return render(request,'posts/singlePost.html',{'post':post})


@login_required
def editPostView(request,id):    
    try:
        post = Post.objects.get(pk=id)
    except:
        return HttpResponse('404')

    if post.author != request.user:
        return HttpResponse('403')

    if(request.method == 'POST'):
        form = PostForm(request.POST,request.FILES,instance=post)
        if(form.is_valid()):
            form.save()
            return redirect(f'/post/{post.id}')
        else:
            return render(request,'posts/newPost.html',{'form':form})

    form = PostForm(instance=post)
    return render(request,'posts/newPost.html',{'form':form})


def deletePostView(request,id):
    try:
        post = Post.objects.get(pk=id)
    except:
        return HttpResponse('404')

    if post.author != request.user:
        return HttpResponse('403')

    post.delete()
    messages.info(request,f'Post Deleted!')
    return redirect(f'/profile')

