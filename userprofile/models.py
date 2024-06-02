from django.db import models
from django.contrib.auth.models import User

from authentication.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Ajouter des champs de profil utilisateur et préférences ici
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    preferences = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.user.username
