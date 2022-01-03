from django import forms
from django.contrib.auth import get_user_model  # add this
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import *

# CustomUser Forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')


# Fundamental Model Forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user',)


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = "__all__"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"


class AmenityProfileRelationship(forms.ModelForm):
    class Meta:
        model = AmenityProfileRelationship
        fields = "__all__"


class PlaceProfileRelationship(forms.ModelForm):
    class Meta:
        model = PlaceProfileRelationship
        fields = "__all__"
