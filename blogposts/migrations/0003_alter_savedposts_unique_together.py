# Generated by Django 4.2 on 2023-05-07 14:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogposts', '0002_alter_comment_post_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='savedposts',
            unique_together={('post', 'user')},
        ),
    ]
