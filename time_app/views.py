from django.shortcuts import render
from django.http import HttpResponse
from .models import TimePost
from django.views.generic import ListView

posts = TimePost.objects.all()


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'time_app/home.html', context) 


class PostListView(ListView):
    model = TimePost
    template_name = 'time_app/home.html'
    context_object_name = 'posts'
