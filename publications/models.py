from django.db import models
from django.conf import settings
from projects.models import Project
from datetime import datetime


class Publication(models.Model):
    SOURCE_CHOICES = [
        ('web', 'Web'),
        ('manual', 'Manual'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    authors = models.TextField()
    publication_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='publications', null=True, blank=True)
    journal = models.CharField(max_length=200)
    doi = models.CharField(max_length=100)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='manual')
    initial_version = models.ForeignKey('PublicationVersion', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='initial_publication')
    current_version = models.ForeignKey('PublicationVersion', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='current_publication')
    created_at = models.DateTimeField(auto_now_add=True)  # Ajout d'une valeur par défaut

    def __str__(self):
        return self.title


class PublicationVersion(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='versions')
    title = models.CharField(max_length=200)
    authors = models.TextField()
    publication_date = models.DateField(default=datetime.today)
    journal = models.CharField(max_length=200)
    doi = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    media_files = models.ManyToManyField('Media', blank=True, related_name='publication_versions')

    def __str__(self):
        return f"{self.publication.title} - Version {self.pk}"


class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('rich_text', 'Rich Text'),
    ]

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='media/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.media_type} - {self.file.name}"
