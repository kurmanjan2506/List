from django.shortcuts import render
from rest_framework import permissions, status
from . import serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Room, BookedRoom, Notification
from .permissions import IsBookedAuthor
from rest_framework.response import Response


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = (IsBookedAuthor,)
        elif self.request.method == 'POST':
            self.permission_classes = (permissions.IsAdminUser,)
        else:
            self.permission_classes = (permissions.AllowAny,)
        return super(RoomViewSet, self).get_permissions()


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


class DateApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, date):
        queryset = Room.objects.filter(date=date)
        serializer = serializers.RoomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




