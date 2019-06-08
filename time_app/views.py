from django.shortcuts import render
from .models import TimePost, Project, Client
from django.contrib.auth.models import User
from .forms import TimePostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView, WeekArchiveView,
)
posts = TimePost.objects.all()
clients = Client.objects.all()
projects = Project.objects.all()
users = User.objects.all()


def load_projects(request):
    """
    """
    client_id = request.GET.get('client')
    projects = Project.objects.filter(client_id=client_id).order_by('name')
    return render(
        request, 'time_app/project_dropdown_list_options.html',
        {'projects': projects}
        )


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


def show_selected_view(request):
    posts = TimePost.objects.all()

    project_query = request.GET.get('project')
    client_query = request.GET.get('client')
    user_query = request.GET.get('user')
    # date_start_query = request.GET.get('date_start')
    # date_end_query = request.GET.get('date_end')
    
    if user_query != "0":
        posts = posts.filter(user_id=user_query)

    if project_query != "0":
        posts = posts.filter(project_id=project_query)
    
    elif client_query != "0":
        posts = posts.filter(client_id=client_query)

    # if date_start_query != "" or date_start_query is not None:
    #     posts = posts.filter(date__gte=date_start_query)

    # if date_end_query != "" or is not None:

    total_hours = 0
    for post in posts:
        total_hours += post.time_spent
    
    context = {
        'posts': posts,
        'total_hours': total_hours,
    }
    return render(request, 'time_app/overview.html', context)


def SelectedListView(request):
    # project_query = request.GET.get('project')
    # client_query = request.GET.get('client')
    # user_query = request.GET.get('user')
    # date_start_query = request.GET.get('date_start')
    # date_end_query = request.GET.get('date_end')

    
    context = {
        'clients': clients,
        'projects': projects,
        'users': users,
    }
    return render(request, 'time_app/selected_view_form.html', context)
