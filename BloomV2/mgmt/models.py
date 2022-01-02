from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import base64
import datetime
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)


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


class Place(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    address = models.ForeignKey(
        "mgmt.Address", null=True, blank=True, on_delete=models.DO_NOTHING)
    capacity = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)
    # images = ArrayField(base_field=models.ImageField(null=True), null=True)


class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, blank=False)
    address_line_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)


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
