from django import forms
from django.contrib.auth import get_user_model  # add this
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accountsApp.models import *

# CustomUser Forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
