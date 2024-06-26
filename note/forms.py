# forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'note_type']
        labels = {'title': 'Titre', 'content': 'Contenu', 'note_type': 'Type de note', 'file':''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'custom-input mt-4 mb-4'}),
            'content': forms.Textarea(attrs={'class': 'custom-input mt-4 mb-4'}),
            'note_type': forms.Select(attrs={'class': 'custom-input mt-4 mb-4'}),
        }
