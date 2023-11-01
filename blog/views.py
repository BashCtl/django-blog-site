from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag

# Create your views here.


def home_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    context = {"posts": latest_posts}
    return render(request, "blog/index.html", context)


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    context = {"posts": all_posts}
    return render(request, "blog/all-posts.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post, "tags": post.tags.all()}
    return render(request, "blog/post-detail.html", context)
