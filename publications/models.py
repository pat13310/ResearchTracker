from django.db import models
from django.conf import settings
from projects.models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_ckeditor_5.fields import CKEditor5Field


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


class Publication(models.Model):
    SOURCE_CHOICES = [
        ('web', 'Web'),
        ('manuelle', 'Manuelle'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    authors = models.TextField()
    publication_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='publications', null=True, blank=True,
                                default="Aucun")
    journal = CKEditor5Field(blank=True, null=True)
    doi = models.CharField(max_length=100)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='manuelle')
    initial_version = models.ForeignKey('PublicationVersion', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='initial_publication')
    current_version = models.ForeignKey('PublicationVersion', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='current_publication')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PublicationVersion(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='versions', blank=True,
                                    null=True)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publication_date = models.DateField()
    journal = CKEditor5Field(blank=True, null=True)  # contenu du journal
    doi = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=10, blank=True)
    media_files = models.ManyToManyField('Media', blank=True, related_name='publication_versions')

    def save(self, *args, **kwargs):
        if not self.version:
            self.version = self.calculate_version()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Version {self.pk} de {self.title}"

    def calculate_version(self):
        last_version = self.publication.versions.order_by('-created_at').first()
        if last_version and last_version.version.startswith('Rev-'):
            # Incrémenter la lettre après 'Rev-'
            last_letter = last_version.version.split('-')[-1]
            new_letter = chr(ord(last_letter) + 1)
            return f"Rev-{new_letter}"
        else:
            return "Rev-A"


# On créé la version initiale juste après la création de la publication
@receiver(post_save, sender=Publication)
def create_initial_version(sender, instance, created, **kwargs):
    if created:
        version = PublicationVersion.objects.create(
            publication=instance,
            title=instance.title,
            authors=instance.authors,
            publication_date=instance.publication_date,
            journal=instance.journal,
            doi=instance.doi
        )
        instance.initial_version = version
        instance.current_version = version
        instance.save()
