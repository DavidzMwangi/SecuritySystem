from django import forms
from django.contrib.auth.forms import UserCreationForm

from residence.models import Residence
from user.models import User, Student

USER_TYPES = [
    (0, 'Admin'),
    (1, 'Student'),
    (2, 'Resident'),
]

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=200)
    phone_no = forms.CharField(label='Phone Number', max_length=10)
    address = forms.CharField(label='Address', max_length=100)
    user_type = forms.IntegerField(widget=forms.Select(choices=USER_TYPES))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','phone_no','address','user_type')

class StudentRegisterForm(forms.ModelForm):
    course = forms.CharField(label='Course', max_length=100)
    reg_no = forms.CharField(label='Registration Number', max_length=50)
    year_of_study = forms.CharField(label='Year Of Study', max_length=30)
    residence = forms.ModelChoiceField(queryset=Residence.objects.all())
    class Meta:
        model = Student
        fields = ('course', 'reg_no', 'year_of_study', 'residence')
