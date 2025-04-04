# todo_Bck/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_plss.urls')),  # This includes the URLs from the todo_plss app
]
