from django.contrib import admin
from .models import Room, BookedRoom, Notification, Month
from account.models import CustomUser


class UserTabInline(admin.TabularInline):
    model = CustomUser

class BookedRoomAdmin(admin.ModelAdmin):
    inlines = (UserTabInline,)

admin.site.register(Room)
admin.site.register(BookedRoom)
admin.site.register(Notification)
admin.site.register(Month)

