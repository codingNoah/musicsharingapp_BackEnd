# Generated by Django 4.2.1 on 2023-05-09 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('genre', models.CharField(choices=[('Pop', 'Pop'), ('Rock', 'Rock'), ('Hip-Hop/Rap', 'Hip-Hop/Rap'), ('R&B/Soul', 'R&B/Soul'), ('Country', 'Country'), ('Electronic/Dance', 'Electronic/Dance'), ('Jazz', 'Jazz'), ('Blues', 'Blues'), ('Classical', 'Classical')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MusicModel',
        ),
    ]
