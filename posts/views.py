from django.shortcuts import render

from django.views.generic import ListView
from  posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
