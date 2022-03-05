from django import forms
from django.contrib.auth import get_user_model  # add this
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mainApp.models import *

# CustomUser Forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     profile = None
    #     if commit:
    #         user.save()
    #         profile = Profile.objects.create(
    #             user=user)
    #         profile.save()

    #     return


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
