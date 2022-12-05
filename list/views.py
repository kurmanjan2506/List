from django.shortcuts import render
from . import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Tasks, Category
from rest_framework import permissions, response
from .permissions import IsAuthor
from rest_framework.decorators import api_view

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [permissions.AllowAny()]
    #     else:
    #         return [permissions.IsAdminUser()]
@api_view(['GET'])
def get_category(request):
    queryset = Category.objects.all()
    print(queryset, '!!!!!!!!!!!!!!!!11')
    rep = serializers.CategorySerializer(queryset)
    a = []
    for i in queryset:
        ser = serializers.CategorySerializer(i)
        a.append(ser)
    return response.Response(a)
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


