
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    OverviewListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='time-home'),
    path('timepost/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('timepost/new/', PostCreateView.as_view(), name='post-create'),
    path(
        'timepost/<int:pk>/update/', 
        PostUpdateView.as_view(), name='post-update'
        ),
    path(
        'timepost/<int:pk>/delete/',
        PostDeleteView.as_view(), name='post-delete'
        ),
    path(
        'ajax/load-projects/',
        views.load_projects,
        name='ajax_load_projects'
        ),
    path('overview/', OverviewListView.as_view(), name='overview-create')
]