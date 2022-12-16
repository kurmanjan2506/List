from .models import Room
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class IsBookedAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            course_id = int(request.data['booked_room'])
            owner = get_object_or_404(Room, id=course_id).owner
            return request.user == owner
        except:
            return False

class IsBookedAuthorTwo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner