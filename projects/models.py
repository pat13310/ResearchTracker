from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ResearchTracker import settings


class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'En cours'),
        ('published', 'Publié'),
        ('rejected', 'Rejeté'),
        ('corrected', 'Corrigé'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_projects', on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='collaborative_projects', blank=True)
    title = models.CharField(max_length=200)
    description = CKEditor5Field(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
