# Generated by Django 4.0 on 2022-04-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_question_description_en_question_description_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_ru',
        ),
    ]
