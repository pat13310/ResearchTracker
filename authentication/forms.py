# authentication/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authentication.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                         'focus:ring-violet-400 focus:border-transparent'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                         'focus:ring-violet-400 focus:border-transparent'
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                 'focus:ring-violet-400 focus:border-transparent'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                 'focus:ring-violet-400 focus:border-transparent'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                 'focus:ring-violet-400 focus:border-transparent'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full px-4 py-1.5 border border-violet-300 rounded focus:outline-none focus:ring-2 '
                 'focus:ring-violet-400 focus:border-transparent'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
