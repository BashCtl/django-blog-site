from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from datetime import date
from .models import Post, Author, Tag
from .forms import CommentForm

# Create your views here.


class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {"post": post, "tags": post.tags.all(),
                   "form": CommentForm()}
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

      
        context = {"post": post, "tags": post.tags.all(),
                   "form": form}
        return render(request, "blog/post-detail.html", context)
