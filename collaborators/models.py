from django.db import models
from projects.models import Project

class Collaborator(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='collaborators')

    def __str__(self):
        return self.name
