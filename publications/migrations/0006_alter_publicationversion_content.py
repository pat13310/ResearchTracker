# Generated by Django 5.0.6 on 2024-06-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_alter_publication_journal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationversion',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
