from django import forms

from residence.models import Residence


class ResidenceRegistrationForms(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=30)
    location = forms.CharField(label="Location", max_length=50)
    care_taker_text = forms.CharField(label="Care Taker Text", max_length=50)

    class Meta:
        model = Residence
        fields = ('name', 'location', 'care_taker_text')
