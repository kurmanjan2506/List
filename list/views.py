from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Tasks, Category
from rest_framework import permissions, response
from .permissions import IsAuthor


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]



class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TaskListSerializer
        return serializers.TaskDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [IsAuthor()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


