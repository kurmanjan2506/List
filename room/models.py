from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model
import datetime


User = get_user_model()


class Room(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class BookedRoom(models.Model):
    title = models.CharField(max_length=50, default='Встреча')
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='organizer', null=True)
    room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
    invite = models.ManyToManyField(CustomUser, related_name='invited')
    start_time = models.TimeField()
    over_time = models.TimeField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Резерв комнаты'
        verbose_name_plural = 'Резерв комнат'

    def __str__(self):
        return f'{self.title} - {self.owner} - {self.room} - {self.start_time}'


class Notification(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    message = models.TextField()
    signals = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'


