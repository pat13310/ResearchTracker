from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django_ckeditor_5.fields import  CKEditor5Field

# from userprofile.models import UserProfile


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username

    @property
    def initials(self):
        if self.last_name:
            return self.last_name[:3].capitalize()
        return self.username[:3].capitalize()


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_user_receiver, sender=CustomUser)


class UserProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    bio = CKEditor5Field(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    preferences = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'


