import datetime


from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from authentication.models import CustomUser
from projects.models import Project


class Funding(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(100000)])
    start_date = models.DateField(default=datetime.date.today)
    project = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    #project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='fundings', null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Donateur'
        verbose_name_plural = 'Donateurs'

    def __str__(self):
        return f"{self.name} - {self.project.title}"
