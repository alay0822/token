from rest_framework.routers import DefaultRouter
from todo_plss.views import TodoItemViewSet

router = DefaultRouter()
router.register(r'tasks', TodoItemViewSet)

urlpatterns = router.urls