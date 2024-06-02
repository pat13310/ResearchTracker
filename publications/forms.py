from django import forms
from .models import Publication, PublicationVersion, Media
from datetime import date

class PublicationForm(forms.ModelForm):
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
                'class': 'form-input mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2',
                'placeholder': 'Titre'
            }),
            'authors': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2',
                'placeholder': 'Auteurs'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2',
                'type': 'date',
                'value': date.today().strftime('%Y-%m-%d')
            }),
            'project': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2'
            }),
            'journal': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2',
                'placeholder': 'Journal'
            }),
            'doi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-gray-400 shadow-sm focus:border-violet-300 focus:ring focus:ring-violet-200 focus:ring-opacity-50 focus:outline-none p-2',
                'placeholder': 'DOI'
            }),
        }

class PublicationVersionForm(forms.ModelForm):
    media_files = forms.ModelMultipleChoiceField(
        queryset=Media.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = PublicationVersion
        fields = ['title', 'authors', 'publication_date', 'journal', 'doi', 'media_files']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media_type', 'file', 'description']
