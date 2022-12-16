from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import BookedRoom, Notification
from celery import shared_task


@shared_task()
def task(created:bool, instance):
    if created:
        Notification.objects.create(
            message=f'Состоится встреча {instance.get("title")}\n'
                    f'Чтобы посмотреть детали встречи, перейдите на нее'

        )
    else:
        Notification.objects.create(
            message=f'Состоится встреча {instance.get("title")}\n'
                    f'Чтобы посмотреть детали встречи, перейдите на нее'
        )


@receiver(post_save, sender=BookedRoom)
def post_save_meet(created, **kwargs):
    instance = kwargs.get("instance")
    instance = {
        "title": instance.title,
    }
    task.delay(True if created else False, instance)