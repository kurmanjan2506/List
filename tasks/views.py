from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import Category, Task
from .permissions import IsTaskAuthor, IsTaskAuthorTwo


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'GET':
            return [IsTaskAuthorTwo()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskListSerializer
        return serializers.TaskDetailSerializer













