from django.shortcuts import render
from django.http import HttpResponse
from .models import TimePost, Client
from django.contrib.auth.models import User


def home(request):
    context = {
        'user': User.objects.all(),
        'posts': TimePost.objects.all(),
    }
    return render(request, 'time_app/home.html', context)  
