from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import RoomViewSet, BookedRoomViewSet, NotificationViewSet

router = SimpleRouter()
router.register('room', RoomViewSet)
router.register('booked', BookedRoomViewSet)
router.register('notification', NotificationViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
