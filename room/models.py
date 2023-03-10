from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Month:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    month = ((one, 'January'), (two, 'February'), (three, 'March'), (four, 'April'), (five, 'May'), (six, 'June'),
             (seven, 'July'), (eight, 'August'), (nine, 'September'), (ten, 'October'), (eleven, 'November'),
             (twelve, 'December'))


class Room(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    month = models.ForeignKey('Month', on_delete=models.CASCADE, related_name='months')
    # week = models.ForeignKey('Week', on_delete=models.CASCADE, related_name='weeks')
    ten = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='ten', blank=True)
    eleven = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='eleven', blank=True)
    twelve = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='twelve', blank=True)
    one = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='one', blank=True)
    two = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='two', blank=True)
    three = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='three', blank=True)
    four = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='four', blank=True)
    five = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='five', blank=True)
    six = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='six', blank=True)
    seven = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='seven', blank=True)
    eight = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='eight', blank=True)
    nine = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name='nine', blank=True)

    def __str__(self):
        return f'{self.title} -> {self.date}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Month(models.Model):
    title = models.CharField(max_length=50)
    month = models.SmallIntegerField(choices=Month.month)


@receiver(post_save, sender=Month)
def month_pre_save(sender, instance, *args, **kwargs):
    from datetime import date
    ls = []
    for x in range(32):
        try:
            ls.append(Room(title='Meeting', date=date(2023, instance.month, x), month=instance))
            ls.append(Room(title='Studio', date=date(2023, instance.month, x), month=instance))
            ls.append(Room(title='Production', date=date(2023, instance.month, x), month=instance))
        except ValueError:
            pass
    Room.objects.bulk_create(ls)


# class BookedRoom(models.Model):
#     title = models.CharField(max_length=50, default='Встреча')
#     owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='organizer', null=True)
#     room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
#     invite = models.ManyToManyField(CustomUser, related_name='invited')
#     start_time = models.TimeField()
#     over_time = models.TimeField()
#     description = models.TextField(blank=True)
#
#     class Meta:
#         verbose_name = 'Резерв комнаты'
#         verbose_name_plural = 'Резерв комнат'
#
#     def __str__(self):
#         return f'{self.title} - {self.owner} - {self.room} - {self.start_time}'
#
#
# class Notification(models.Model):
#     timestamp = models.DateTimeField(default=datetime.datetime.now)
#     message = models.TextField()
#     signals = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.message
#
#     class Meta:
#         verbose_name = 'Уведомление'
#         verbose_name_plural = 'Уведомления'


class FavoritesPeople(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', null=True)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites_people')

    class Meta:
        unique_together = ['owner', 'person']