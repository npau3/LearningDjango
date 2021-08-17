from rest_framework import routers
from .views import TaskViewSet, UserViewSet
from django.urls import include, path


router = routers.DefaultRouter()
router.register('task', TaskViewSet, 'task')
router.register('user', UserViewSet, 'user')


urlpatterns = router.urls
