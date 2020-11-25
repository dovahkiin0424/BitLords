from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class Home(ListView):
    model = Post
    template_name = "home.html"

class Detail(DetailView):
    model = Post
    template_name = "detail.html"

class Create(CreateView):
    model = Post
    template_name = "create.html"
    fields = "__all__"
