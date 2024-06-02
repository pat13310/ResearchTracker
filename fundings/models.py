from django.db import models
from projects.models import Project


class Funding(models.Model):
    source = models.CharField(max_length=200)
    amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='fundings')

    def __str__(self):
        return f"{self.source} - {self.project.title}"
