from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from . import serializers
from .models import Category, Task
from .permissions import IsTaskAuthor, IsTaskAuthorTwo

class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [IsTaskAuthorTwo()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskListSerializer
        return serializers.TaskDetailSerializer

    # def perform_update(self, serializer):
    #     instance = self.get_object()
    #     if instance.completed:
    #         instance.pop()
    #     print(instance, '!!!!!!!!!')






