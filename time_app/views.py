from django.shortcuts import render
from django.http import HttpResponse
from .models import TimePost, Project
from .forms import TimePostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


def load_projects(request):
    client_id = request.GET.get('client')
    projects = Project.objects.filter(client_id=client_id).order_by('name')
    return render(
        request, 'time_app/project_dropdown_list_options.html',
        {'projects': projects}
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


class OverviewListView(ListView):
    model = TimePost
    template_name = 'time_app/overview.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = TimePost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TimePost
    form_class = TimePostForm
    # fields = ['time_spent', 'client', 'project', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        form.save()


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TimePost
    form_class = TimePostForm
    # fields = ['time_spent', 'client', 'project', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        form.save()

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TimePost
    success_url = '/'
  
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True

    