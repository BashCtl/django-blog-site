from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail"),
]