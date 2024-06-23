# forms.py
from django import forms
from fundings.models import Funding


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        exclude = ['user']
        fields = ['name', 'amount', 'project', 'active']
        labels = {'name': 'Nom', 'amount': 'Montant', 'active': 'Actif', "project": "Projet"}

        widgets = {"name": forms.TextInput(attrs={'class': 'mt-4 mb-4 custom-input'}),
                   "amount": forms.NumberInput(attrs={'class': 'mt- 4 mb-4 custom-input'}),
                   "project": forms.TextInput(attrs={'class': 'mt-4 mb-4 custom-input'}),
                   "active": forms.CheckboxInput(attrs={'class': 'mt-4 mb-4'}),
                   }
