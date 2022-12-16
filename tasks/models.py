from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    category = ((one, 'Активные таски'), (two, 'Backlog'), (three, 'Встречи'), (four, 'Выполненные таски'),
                (five, 'Незавершенные'))

class Status:
    one = 1
    two = 2
    three = 3
    status = ((one, 'Не срочно'), (two, 'Срочно'), (three, 'Очень срочно'))


class Complete:
    one = 1
    two = 2
    three = 3
    complete = ((one, 'Активный'), (two, 'Завершенный'), (three, 'Незавершенный'))


class Task(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products', null=True)
    category = models.SmallIntegerField(choices=Category.category, default=2)
    description = models.TextField(null=True)
    completed = models.PositiveSmallIntegerField(choices=Complete.complete, default=1)
    date = models.DateField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=Status.status, default=1)
    deadline = models.DateField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


