from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm

# Create your views here.

# Starting or Landing Page
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3] # It's equal to Post.objects.all()[:3]
        return data

# All Posts Page
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "all_posts"

# Single Post
class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # commit=False means will not save yet
            comment.post = post # attaching post reference here
            comment.save() # manually calling save now

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form # if the form is invalid errors will be sent
        }
        return render(request, "blog/post-detail.html", context)
