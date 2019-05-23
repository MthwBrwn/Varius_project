from django.shortcuts import render
from django.http import HttpResponse
from .models import TimePost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView
)

# posts = TimePost.objects.all()


# def home(request):
#     context = {
#         'posts': posts
#     }
#     return render(request, 'time_app/home.html', context) 


class PostListView(ListView):
    model = TimePost
    template_name = 'time_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = TimePost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TimePost
    fields = ['time_spent', 'notes', 'client', 'project_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
