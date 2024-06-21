from django import forms
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import CKEditor5Widget

from authentication.models import UserProfile, CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': '', 'last_name': '', 'email': ''}
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'text-sm custom-input mb-2 ',
                'placeholder': 'Nom de l\'utilisateur',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'text-sm custom-input mb-2',
                'placeholder': 'Prénom',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'text-sm custom-input mb-2',
                'placeholder': 'adresse e-mail',
            })
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location']
        labels = {'bio': '', 'location': '', 'preferences': ''}
        widgets = {
            'bio': CKEditor5Widget(config_name='default', attrs={
                'data-placeholder': 'Votre bio en quelques lignes ...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'text-sm custom-input mb-2',
                'placeholder': 'Localisation géographique',
            })
        }
