# Generated by Django 5.0.6 on 2024-06-27 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='file',
        ),
    ]
