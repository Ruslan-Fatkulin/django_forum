# Generated by Django 4.0 on 2022-04-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_answer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
