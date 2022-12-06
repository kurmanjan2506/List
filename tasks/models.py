from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', default='Входящие',
                                 null=True)
    title = models.CharField(max_length=80, null=True)
    text = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
