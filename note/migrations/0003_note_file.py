# Generated by Django 5.0.6 on 2024-06-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_note_note_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads/'),
        ),
    ]
