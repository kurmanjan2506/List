from .models import Room
from rest_framework import permissions
from .serializers import RoomSerializer


class IsBookedAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        id_ = view.kwargs.get('pk')
        a = Room.objects.filter(id=id_)
        serializer = RoomSerializer(a, many=True)
        try:
            for key in request.data:
                for i in serializer.data:
                    if i[key] == request.user.id or i[key] == None:
                        return True
        except:
            return False




