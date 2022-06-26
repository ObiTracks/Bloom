from django import forms
from django.contrib.auth import get_user_model  # add this
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

import siteApp.models as models

# Fundamental Model Forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = "__all__"
        exclude = ('user',)


class PlaceForm(forms.ModelForm):
    # def __init__(self, user, *args, **kwargs):
    #     # user = kwargs.pop('user', None)
    #     super(PlaceForm, self).__init__(
    #         *args, **kwargs)
        # profile = user.profile
        # self.fields['owner'].initial = profile

    class Meta:
        model = models.Place
        fields = "__all__"
        exclude = ("owner",)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email for members to reach'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+(X)XXXXXXXXXX'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Location capacity'}),
            'description': forms.Textarea(attrs={'placeholder': 'Get people acquainted with a description'}),
        }


class AmenityForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(AmenityForm, self).__init__(
            *args, **kwargs)  # populates the form
        print(user)
        place_queryset = models.Place.objects.filter(
            place_of__profile__user=user)
        # Heres the link that explains this chained model filter
        # https://docs.djangoproject.com/en/4.0/topics/db/queries/#:~:text=Lookups%20that%20span-,relationships,-%C2%B6

        # Shows all the possible places to pick
        self.fields['place'].queryset = place_queryset

    class Meta:
        model = models.Amenity
        fields = "__all__"
        # exclude = ('place')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = "__all__"


class AmenityProfileRelationship(forms.ModelForm):
    class Meta:
        model = models.AmenityProfileRelationship
        fields = "__all__"


class PlaceProfileRelationship(forms.ModelForm):
    class Meta:
        model = models.PlaceProfileRelationship
        fields = "__all__"


class JoinRequest(forms.ModelForm):
    class Meta:
        model = models.JoinRequest
        fields = "__all__"
