from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ('owner', 'title', 'completed', 'category')


class TaskDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = '__all__'


