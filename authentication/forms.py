# authentication/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authentication.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'custom-input'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'custom-input'
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'custom-input'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'custom-input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'custom-input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'custom-input'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
