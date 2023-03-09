from .models import Room
from rest_framework import permissions
from .serializers import RoomSerializer


class IsBookedAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        id_ = view.kwargs.get('pk')
        a = Room.objects.filter(id=id_)
        serializer = RoomSerializer(a, many=True)
        try:
            for key in request.data: # Это время которое мы передаем (11)
                for i in serializer.data: # Это все данные по айди комнаты
                    if i[key] == request.user.id or i[key] == None:
                        return True
        except:
            return False




