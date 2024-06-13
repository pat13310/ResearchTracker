from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {'name': 'Nom',
                  'email': 'Email',
                  'message': 'Message', }

        widgets = {'name': forms.TextInput(attrs={'class': 'mb-2 custom-input',
                                                  'placeholder': 'Nom'}),
                   'email': forms.TextInput(attrs={'class': 'mb-2 custom-input',
                                                   'placeholder': 'Email'}),
                   'message': forms.Textarea(attrs={'class': 'mb-2 custom-input',
                                                    'placeholder': 'Message'}),
                   }
