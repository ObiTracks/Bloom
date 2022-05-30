import os
import requests
from django.db import models
from django.conf import settings
from django.core.files import File
from django.db.models.fields.related import ForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from siteApp.middleware import RequestMiddleware

import base64
import datetime

import json
from django import template
from django.forms.models import model_to_dict

# Signals
import inspect
import os
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utilities import user_upload_directory_path

# BASE MODELS


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    bio = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to=user_upload_directory_path, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Amenity(models.Model):
    name = models.CharField(max_length=200, blank=False)
    place = models.ForeignKey(
        "siteApp.Place", blank=False, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    timeslots = models.JSONField(blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    backup_image_url = models.URLField(max_length=400,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "{} | {}".format(self.name, self.place)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    
    def set_random_backup_image_url(self):
        random_img_url = 'https://source.unsplash.com/random/?nature-wallpaper,tropical-vegetation'
        
        if not self.backup_image_url:
            response = requests.get(random_img_url)
            response_url = response.url
            print(response_url)

            self.backup_image_url = response_url
            self.save()

    def save(self):
        self.set_random_backup_image_url()
        super(Amenity, self).save()

# @receiver(post_save, sender=Amenity)
# def create_profile(sender, instance, created, **kwargs):
#     request = RequestMiddleware(get_response=None)
#     request = request.thread_local.current_request
#     user = request.user
#     if user:
#         if created:
#             AmenityProfileRelationship.objects.create(
#                 amenity=instance, profile=user.profile, profile_type='0')


class Place(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    backup_image_url = models.URLField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # images = ArrayField(base_field=models.ImageField(null=True), null=True)

    @property
    def image_url(self):
        from django.contrib.sites.models import Site
        domain = Site.objects.get_current().domain
        url = 'http://{domain}'.format(domain=domain)

        if self.image and hasattr(self.image, 'url'):
            return url + self.image.url

    
    def serialize_model_to_dict(self):
        print(self)
        dict_obj = model_to_dict(self)
        data = json.dumps(str(dict_obj))
        # data = dict_obj
        
        print(data)
        return data
    
    def set_random_backup_image_url(self):
        random_img_url = 'https://source.unsplash.com/random/?nature-wallpaper,tropical-vegetation'
        
        if not self.backup_image_url:
            response = requests.get(random_img_url)
            response_url = response.url
            print(response_url)

            self.backup_image_url = response_url
            self.save()

    def save(self):
        self.set_random_backup_image_url()
        super(Place, self).save()


    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "{}".format(self.name)


class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, blank=False)
    address_line_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "Address: {}".format(self.address_line_1)


class Reservation(models.Model):
    amenity_profile_relationship = models.ForeignKey(
        "siteApp.AmenityProfileRelationship", verbose_name=("AmenityRelationship for the Reservation"), blank=False, on_delete=models.CASCADE)
    place = models.ForeignKey(
        "siteApp.Place", blank=False, null=True, related_name="reservation_set", on_delete=models.CASCADE)
    # timeslot = models.JSONField(default=int)
    # timeslot = ArrayField(
    #     base_field=models.TimeField(null=False, blank=True), size=2, null=True)
    no_show = models.BooleanField(default=False)
    notes = models.TextField(max_length=500, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "{} {} Reservation".format(self.amenity_profile_relationship.profile, self.amenity_profile_relationship.amenity)


# RELATIONAL MODELS
class AmenityProfileRelationship(models.Model):
    amenity = models.ForeignKey("siteApp.Amenity", verbose_name=(
        "Amenity in the relationship"), on_delete=models.CASCADE, related_name="amenity_of")
    profile = models.ForeignKey("siteApp.Profile", verbose_name=(
        "Profile in the relationship"), on_delete=models.CASCADE, related_name="amenity_profile_of")

    PROFILE_TYPES = (('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'),
                     ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member'))
    profile_type = models.CharField(
        max_length=100, choices=PROFILE_TYPES, default='5')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} Relationship".format(self.amenity, self.profile)

    class Meta:
        verbose_name = 'Amenity Profile Relationship'
        verbose_name_plural = 'Amenity Profile Relationships'
        ordering = ('date_created',)


class PlaceProfileRelationship(models.Model):
    place = models.ForeignKey("siteApp.Place", verbose_name=(
        "Place in the relationship"), on_delete=models.CASCADE, related_name="place_of")
    profile = models.ForeignKey("siteApp.Profile", verbose_name=(
        "Profile in the relationship"), on_delete=models.CASCADE, related_name="place_profile_of")

    PROFILE_TYPES = (('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'),
                     ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member'))
    profile_type = models.CharField(
        max_length=100, choices=PROFILE_TYPES, default='Member')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Place Profile Relationship'
        verbose_name_plural = 'Place Profile Relationships'
        ordering = ('date_created',)

    def __str__(self):
        return "Place: {} | Profile: {} | Type: {}".format(self.place, self.profile, self.profile_type)


class JoinRequest(models.Model):
    profile = models.ForeignKey(
        "siteApp.Profile", null=False, blank=False, on_delete=models.CASCADE)
    place = models.ForeignKey(
        "siteApp.Place",  null=False, blank=False, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "Join Request: User({}) Place({})".format(self.profile, self.profile)


class TimeSlot(models.Model):
    nickname = models.CharField(max_length=200, blank=False)
    startime = models.TimeField(default=datetime.time(0, 0, 0), null=False)
    endtime = models.TimeField(default=datetime.time(0, 0, 0), null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return "{} {}-{}".format(self.nickname, self.startime, self.endtime)
