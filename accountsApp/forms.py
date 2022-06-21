from django import forms
from django.contrib.auth import get_user_model  # add this
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accountsApp.models import *

# CustomUser Forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name','last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','first_name','last_name')
