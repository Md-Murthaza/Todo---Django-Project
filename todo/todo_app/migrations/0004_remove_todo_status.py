# Generated by Django 5.1 on 2024-11-05 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
    ]
