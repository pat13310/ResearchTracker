from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {'name': 'Nom',
                  'email': 'Email',
                  'message': 'Message', }

        widgets = {'name': forms.TextInput(attrs={'class': 'form-input',
                                                  'placeholder': 'Nom'}),
                   'email': forms.TextInput(attrs={'class': 'form-input',
                                                   'placeholder': 'Email'}),
                   'message': forms.Textarea(attrs={'class': 'form-input',
                                                    'placeholder': 'Message'}),
                   }
