# Generated by Django 5.1.2 on 2024-11-25 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_text_content_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
    ]
