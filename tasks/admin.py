from django.contrib import admin
from .models import Category, Task

admin.site.register(Category)
# admin.site.register(Task)

@admin.register(Task)
class Lesson(admin.ModelAdmin):
    list_display = ('title', 'completed', 'date')