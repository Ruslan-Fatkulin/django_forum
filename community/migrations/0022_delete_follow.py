# Generated by Django 4.0 on 2022-04-10 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0021_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]