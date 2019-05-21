from django.shortcuts import render
from django.http import HttpResponse
from .models import TimePost

posts = TimePost.objects.all()


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'time_app/home.html', context)  
