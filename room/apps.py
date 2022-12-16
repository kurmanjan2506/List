from django.apps import AppConfig
from .celery import app as celery_app

class RoomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'room'

    def ready(self):
        import room.signals

__all__ = ('celery_app',)
