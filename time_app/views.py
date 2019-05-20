from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'time_app/base.html')  
