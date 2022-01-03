from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

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