from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User

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

