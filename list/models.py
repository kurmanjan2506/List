import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tasks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=80, verbose_name='Задача')
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
