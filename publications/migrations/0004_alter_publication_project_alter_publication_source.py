# Generated by Django 5.0.6 on 2024-06-14 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('publications', '0003_publicationversion_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(blank=True, default='Aucun', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='source',
            field=models.CharField(choices=[('web', 'Web'), ('manuelle', 'Manuelle')], default='manuelle', max_length=10),
        ),
    ]
