# Generated by Django 4.0 on 2022-04-08 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('community', '0018_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
