from django.contrib import admin
from django.contrib.auth.models import User

from authentication.models import UserProfile, CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    verbose_name = 'Utilisateur'
    verbose_name_plural = 'Utilisateurs'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('bio', 'preferences', 'user__email')


    verbose_name = 'Profil'
    verbose_name_plural = 'Profils'
