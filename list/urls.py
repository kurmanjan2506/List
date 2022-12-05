from django.db import router
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from list.views import CategoryViewSet, get_category

router = SimpleRouter()
router.register('category', CategoryViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('get_category/', get_category),
]
