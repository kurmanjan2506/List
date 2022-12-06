from django.urls import path, include
from .views import CategoryViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
