from django import forms
from .models import RSSFeed


class RSSFeedForm(forms.ModelForm):
    class Meta:
        model = RSSFeed
        fields = ['title', 'url', 'description']
        labels = {'title': 'Titre', 'url': 'Lien URL', 'description': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-input'}),
            'url': forms.URLInput(attrs={'class': 'custom-input'}),
            'description': forms.Textarea(
                attrs={'class': 'custom-input'}),
        }
