from django import forms

from case.models import Category


class CategoryForms(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30)
    level = forms.IntegerField(label='Category Level')
    description = forms.CharField(label='Description', max_length=100)

    class Meta:
        model = Category
        fields = ('name', 'level', 'description')
