# todo_plss/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, SecureHelloView

router = DefaultRouter()
router.register(r'tasks', TodoItemViewSet)

urlpatterns = router.urls + [
    path('secure-hello/', SecureHelloView.as_view(), name='secure-hello'),
]
