import datetime

from django import forms

from case.models import Category, Case
from user.models import User

CASE_STATUS = [
    (0, 'Not Reported'),
    (1, 'Reported'),
    (2, 'Solved'),
]


class CategoryForms(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30)
    level = forms.IntegerField(label='Category Level')
    description = forms.CharField(label='Description', max_length=100)

    class Meta:
        model = Category
        fields = ('name', 'level', 'description')


class CaseForm(forms.ModelForm):
    category = forms.ModelChoiceField(Category.objects.all(), label="Case Category")
    status = forms.IntegerField(widget=forms.Select(choices=CASE_STATUS))
    description = forms.CharField(label="Description", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
    time = forms.DateTimeField(label="Date & Time",initial=datetime.date.today)
    picture = forms.ImageField(label="Picture")
    class Meta:
        model = Case
        fields = ('category', 'status', 'description', 'location', 'time', 'picture')
