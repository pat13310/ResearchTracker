# forms.py

from django import forms
from .models import Project
from datetime import datetime


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Si l'objet existe (c'est une mise à jour)
            self.initial['start_date'] = self.instance.start_date.strftime('%Y-%m-%d')
            self.initial['end_date'] = self.instance.end_date.strftime('%Y-%m-%d')
            self.fields['start_date'].widget.attrs['readonly'] = True
        else:  # Mode création
            self.initial['start_date'] = datetime.now().strftime('%Y-%m-%d')
            self.fields['start_date'].widget.attrs['readonly'] = False

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'status']
        labels = {
            'title': '',
            'description': '',
            'start_date': 'Date de début',
            'end_date': 'Date de fin',
            'status': 'Statut',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-input',
                'placeholder': 'Titre'
            }),
            'description': forms.Textarea(attrs={
                'class': 'custom-input',
                'placeholder': 'Description'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'custom-input',
                'type': 'date',
                'format': 'yyyy-MM-dd'  # Format d'affichage
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'custom-input',
                'type': 'date',
                'format': 'yyyy-MM-dd'  # Format d'affichage
            }),
            'status': forms.Select(attrs={
                'class': 'custom-input'
            }),
        }
