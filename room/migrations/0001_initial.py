# Generated by Django 3.2.16 on 2023-01-01 09:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('message', models.TextField()),
                ('signals', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='BookedRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Встреча', max_length=50)),
                ('start_time', models.TimeField()),
                ('over_time', models.TimeField()),
                ('description', models.TextField(blank=True)),
                ('invite', models.ManyToManyField(related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='organizer', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.room')),
            ],
            options={
                'verbose_name': 'Резерв комнаты',
                'verbose_name_plural': 'Резерв комнат',
            },
        ),
        migrations.CreateModel(
            name='FavoritesPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_people', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('owner', 'person')},
            },
        ),
    ]
