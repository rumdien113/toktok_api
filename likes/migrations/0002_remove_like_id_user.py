# Generated by Django 5.1.3 on 2024-12-22 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='id_user',
        ),
    ]
