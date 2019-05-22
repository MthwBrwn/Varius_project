
from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='time-home'),
    path('timepost/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]