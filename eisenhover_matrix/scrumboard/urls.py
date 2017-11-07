from rest_framework.routers import DefaultRouter

from .api import TaskViewSet

router = DefaultRouter()
router.register(r'^task', TaskViewSet)
urlpatterns = router.urls
