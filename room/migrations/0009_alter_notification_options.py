# Generated by Django 3.2.16 on 2022-12-13 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_rename_massage_notification_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Уведомление', 'verbose_name_plural': 'Уведомления'},
        ),
    ]