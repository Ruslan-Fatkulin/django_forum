# Generated by Django 4.0 on 2022-04-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_alter_answer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='code',
            field=models.TextField(null=True),
        ),
    ]
