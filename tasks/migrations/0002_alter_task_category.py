# Generated by Django 3.2.16 on 2022-12-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='Бэклог', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='tasks.category'),
        ),
    ]