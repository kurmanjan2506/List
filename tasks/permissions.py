from .models import Task
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class IsTaskAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            course_id = int(request.data['course'])
            owner = get_object_or_404(Task, id=course_id).owner
            return request.user == owner
        except:
            return False

class IsTaskAuthorTwo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

