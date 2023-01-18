from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import RoomViewSet, BookedRoomViewSet, NotificationViewSet, DateApiView

router = SimpleRouter()
router.register('room', RoomViewSet)
router.register('booked', BookedRoomViewSet)
router.register('notification', NotificationViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/room1/<str:date>/', DateApiView.as_view()),
]
