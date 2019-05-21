from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required



@ login_required
def profile(request):
    return render(request, 'users/profile.html') 

