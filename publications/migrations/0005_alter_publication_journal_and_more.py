# Generated by Django 5.0.6 on 2024-06-15 07:38

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_alter_publication_project_alter_publication_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='journal',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicationversion',
            name='journal',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
