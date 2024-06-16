from django import forms
from .models import Publication, PublicationVersion, Media
from datetime import date, datetime
from django_ckeditor_5.widgets import CKEditor5Widget


class PublicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Si l'objet existe (c'est une mise à jour)
            self.initial['publication_date'] = self.instance.publication_date.strftime('%Y-%m-%d')
            self.fields['publication_date'].widget.attrs['readonly'] = True
        else:  # Mode création
            self.initial['publication_date'] = datetime.now().strftime('%Y-%m-%d')
            self.fields['publication_date'].widget.attrs['readonly'] = False

    class Meta:
        model = Publication
        fields = ['title', 'authors', 'publication_date', 'project', 'journal', 'doi']
        labels = {
            'title': '',
            'authors': '',
            'publication_date': 'Date de publication',
            'project': 'Projet',
            'journal': 'Journal',
            'doi': 'DOI',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-input',
                'placeholder': 'Titre'
            }),
            'authors': forms.TextInput(attrs={
                'class': 'custom-input',
                'placeholder': 'Auteurs'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'custom-input',
                'type': 'date',
                'value': date.today().strftime('%Y-%m-%d'),
                'format': 'YYYY-MM-DD'
            }),
            'project': forms.Select(attrs={
                'class': 'custom-input'
            }),
            'journal': CKEditor5Widget(config_name='default'),
            'doi': forms.TextInput(attrs={
                'class': 'custom-input',
                'placeholder': 'DOI'
            }),
        }


class PublicationVersionForm(forms.ModelForm):
    journal = forms.CharField(widget=CKEditor5Widget(), required=False)
    media_files = forms.ModelMultipleChoiceField(
        queryset=Media.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = PublicationVersion
        fields = ['title', 'authors', 'publication_date', 'journal']
        labels = {"title": "Titre", "authors": "Auteurs", "publication_date": "Date de publication", }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-input mb-4 text-sm',
                'placeholder': 'Titre'
            }),
            'authors': forms.TextInput(attrs={
                'class': 'custom-input mb-4 text-sm',
                'placeholder': 'Auteurs'
            }), 'publication_date': forms.DateInput(attrs={
                'class': 'custom-input mb-4 text-sm',
                'type': 'date',
                'format': 'YYYY-MM-DD'
            }), }


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media_type', 'file', 'description']
