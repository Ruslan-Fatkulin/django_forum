# Generated by Django 4.0 on 2022-04-08 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0019_alter_followerscount_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
    ]