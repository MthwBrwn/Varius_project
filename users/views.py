from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    '''
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Welcome back,!')
        else:
            form = UserCreationForm() 
        return redirect('time-home')
    return render(request, 'users/sign_in.html', {'form': form})

