from django.shortcuts import render
from .models import TimePost, Project
from .forms import TimePostForm, TimeGetForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView, WeekArchiveView,
)


def load_projects(request):
    """
    """
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

class OwnObjectsMixin():
    """
    This is a custom mixin to show only those time entries 
    for the specific user
    """
    def get_queryset(self):
        user = self.request.user
        return super(OwnObjectsMixin, self).get_queryset().filter(user=user)


class PostListView(LoginRequiredMixin, OwnObjectsMixin, ListView):
    model = TimePost
    template_name = 'time_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10
    paginate_orphans = 2
    


class PostWeekArchiveView(WeekArchiveView):
    queryset = TimePost.objects.all()
    date_field = "date"
    week_format = "%W"
    allow_future = False


class PostDetailView(LoginRequiredMixin, OwnObjectsMixin, DetailView):
    model = TimePost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TimePost
    form_class = TimePostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        form.save()


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TimePost
    form_class = TimePostForm
    success_url = '/'

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

    
class OverviewListView(ListView):
    model = TimePost
    template_name = 'time_app/overview.html'
    context_object_name = 'posts'
    ordering = ['-date']


def SelectedListView(request):

    return render(request, selected_view.html)
    # model = TimePost
    # template_name = 'time_app/selected_view'
    # context_object_name = 'posts'
    # ordering = ['-date']