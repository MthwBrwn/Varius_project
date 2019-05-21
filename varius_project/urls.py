
from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('time_app.urls')),
    path('signin/', user_views.register, name='sign-in'),
]
