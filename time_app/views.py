from django.shortcuts import render
from django.http import HttpResponse

dummy = [
    {
        'client': 'wenatchee',
        'project': 'dam building',
        'time': 60,
        'notes': 'first posting',
        'date': 'now 2020',
    },
    {
        'client': 'bellevue',
        'project': 'city sewer',
        'time': 55,
        'notes': 'first posting for bellevue',
        'date': 'then 2020',
    }
]


def home(request):
    context = {
        'dummy': dummy
    }
    return render(request, 'time_app/home.html', context)  
