from django.shortcuts import render
from rest_framework import permissions
from . import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Room, BookedRoom, Notification
from .permissions import IsBookedAuthor, IsBookedAuthorTwo


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permissions = (permissions.AllowAny(),)


class BookedRoomViewSet(ModelViewSet):
    queryset = BookedRoom.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookRoomSerializer
        return serializers.BookRoomDetailSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = serializers.NotificationSerializer






