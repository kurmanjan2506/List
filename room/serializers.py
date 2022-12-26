from rest_framework import serializers
from .models import Room, BookedRoom, Notification


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookRoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    invite = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BookedRoom
        fields = ('id', 'owner', 'start_time', 'invite' 'room')

class BookRoomDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    invite = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = BookedRoom
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
