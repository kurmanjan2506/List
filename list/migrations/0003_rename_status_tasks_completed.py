# Generated by Django 3.2.16 on 2022-12-05 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_tasks_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='status',
            new_name='completed',
        ),
    ]
