# Generated by Django 5.1.3 on 2024-12-24 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_rename_create_ad_comment_create_at_and_more'),
        ('posts', '0002_alter_post_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
    ]
