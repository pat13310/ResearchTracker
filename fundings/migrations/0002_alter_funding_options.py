# Generated by Django 5.0.6 on 2024-06-17 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funding',
            options={'verbose_name': 'Donateur', 'verbose_name_plural': 'Donateurs'},
        ),
    ]
