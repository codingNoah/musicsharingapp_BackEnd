# Generated by Django 4.2.1 on 2023-05-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_music_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='category',
        ),
    ]