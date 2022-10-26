from django.shortcuts import render
from .models import Post, Comment
from account.models import UserProfile
from .forms import PostForm


def home(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {"posts": posts}

    profile = UserProfile.objects.get(user=request.user)
    context["profile"] = profile

    if request.method == "POST":
        print(request.POST)
        post_id = request.POST["post_id"]
        content = request.POST["comment"]
        
        post = Post.objects.get(id=int(post_id))
        Comment.objects.create(user=request.user, content=content, post=post)

    return render(request, 'post/home.html', context)


def post_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'post/detail.html', context)

