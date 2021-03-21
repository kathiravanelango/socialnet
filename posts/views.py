from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from .utils import serializeManyPosts

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
        return HttpResponse(f'Post does not Exists',status=404)
    return render(request,'posts/singlePost.html',{'post':post})


@login_required
def editPostView(request,id):    
    try:
        post = Post.objects.get(pk=id)
    except:
        return HttpResponse(f'Post does not Exists',status=404)

    if post.author != request.user:
        return HttpResponse('Un Authorized Access',status=403)

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
        return HttpResponse(f'Post does not Exists',status=404)

    if post.author != request.user:
        return HttpResponse('Un Authorized Access',status=403)

    post.delete()
    messages.info(request,f'Post Deleted!')
    return redirect(f'/{request.user.username}')

def getMorePostsView(request):
    if not request.user.is_authenticated:
        return JsonResponse({'report':False,'message':'User not Authenticated'})

    page_num = int(request.GET.get('page_num',2))   
    posts, has_more, next_page = Post.paginate(page_num=page_num)
    posts = serializeManyPosts(posts)

    return JsonResponse({'report':True,'posts':posts,'has_more':has_more,'next_page':next_page})