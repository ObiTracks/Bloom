from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
import base64
import datetime

# Custom User Management
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# CUSTOM USER MODEL

class CustomUser(AbstractUser):
    # Tutorial that helped build and set this up
    # https://learndjango.com/tutorials/django-custom-user-model
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=20, blank=False, unique=True)
    alias = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # define the user manager class for User
    objects = CustomUserManager()

    def __str__(self):
        return "@{}".format(self.email)

    def get_short_name(self):
        return self.alias

# BASE MODELS


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    bio = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Amenity(models.Model):
    name = models.CharField(max_length=200, blank=False)
    place = models.ForeignKey("mgmt.Place", null=True,
                              blank=True, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    # availability = ArrayField(
    #     base_field=models.CharField(max_length=100, blank=True), null=True)
    # images = models.JSONField(_(""), encoder=base64, decoder=)
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#:~:text=or%20TextInput%20otherwise.-,JSONField,-%C2%B6
    # https://stackoverflow.com/questions/64134687/django-jsonfield-with-default-and-custom-encoder
    # https://stackoverflow.com/questions/28036404/django-rest-framework-upload-image-the-submitted-data-was-not-a-file/28036805#28036805
    # https://www.py4u.net/discuss/205629

    def __str__(self):
        return "{} | {}".format(self.name, self.place)


class Place(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    address = models.ForeignKey(
        "mgmt.Address", null=True, blank=True, on_delete=models.DO_NOTHING)
    capacity = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)
    # images = ArrayField(base_field=models.ImageField(null=True), null=True)

    def __str__(self):
        return "{}".format(self.name)


class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, blank=False)
    address_line_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "Address: {}".format(self.address_line_1)


class Reservation(models.Model):
    profile = models.ForeignKey(
        "mgmt.Profile", verbose_name=("Profile for Reservation"), on_delete=models.CASCADE)
    amenity = models.ForeignKey(
        "mgmt.Amenity", verbose_name=("Amenity for Reservation"), on_delete=models.DO_NOTHING)
    # timeslot = models.JSONField(default=int)
    # timeslot = ArrayField(
    #     base_field=models.TimeField(null=False, blank=True), size=2, null=True)
    no_show = models.BooleanField(default=False)
    notes = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return "{} {} Reservation".format(self.profile, self.amenity)


# RELATIONAL MODELS
class AmenityProfileRelationship(models.Model):
    amenity = models.ForeignKey("mgmt.Amenity", verbose_name=(
        "Amenity in the relationship"), on_delete=models.CASCADE)
    profile = models.ForeignKey("mgmt.Profile", verbose_name=(
        "Profile in the relationship"), on_delete=models.CASCADE)

    PROFILE_TYPES = (('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'),
                     ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member'))
    profile_type = models.CharField(
        max_length=100, choices=PROFILE_TYPES, default='5')

    def __str__(self):
        return "{} {} Relationship".format(self.amenity, self.profile)

    class Meta:
        verbose_name = 'Amenity Profile Relationship'
        verbose_name_plural = 'Amenity Profile Relationships'


class PlaceProfileRelationship(models.Model):
    place = models.ForeignKey("mgmt.Amenity", verbose_name=(
        "Place in the relationship"), on_delete=models.CASCADE)
    profile = models.ForeignKey("mgmt.Profile", verbose_name=(
        "Profile in the relationship"), on_delete=models.CASCADE)

    PROFILE_TYPES = (('Owner', 'Owner'), ('Manager', 'Manager'), ('Supervisor', 'Supervisor'),
                     ('Staff', 'Staff'), ('Authorized User', 'Authorized User'), ('Member', 'Member'))
    profile_type = models.CharField(
        max_length=100, choices=PROFILE_TYPES, default='Member')

    def __str__(self):
        return "{} {} Relationship".format(self.place, self.profile)

    class Meta:
        verbose_name = 'Place Profile Relationship'
        verbose_name_plural = 'Place Profile Relationships'
