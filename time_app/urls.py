
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostWeekArchiveView,
    OverviewListView,
    SelectedListView,
    show_selected_view,
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
    path(
        '<int:year>/week/<int:week>/',
        PostWeekArchiveView.as_view(),
        name='post-week'
        ),
    path('overview/', OverviewListView.as_view(), name='overview-create'),
    path(
        'overview/selectedview/showselectedview',
        show_selected_view, 
        name='show-selected-view'
        ),
    path('overview/selectedview/', SelectedListView, name='selected-view')
]