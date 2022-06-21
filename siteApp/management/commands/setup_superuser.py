import random
import time

from django.db import transaction
from django.core.management.base import BaseCommand

from accountsApp.models import CustomUser
from siteApp.models import *

from siteApp.factories import UserFactory


NUM_USERS = 20
NUM_PLACES = 10

class Command(BaseCommand):
    help = "Generates test data"

    def generate_places(self,profile):
        place = Place.objects.create(owner=profile, name="{}'s Place".format(profile))
        PlaceProfileRelationship.objects.create(
            place=place, profile=profile, profile_type='0')
        amenity = Amenity,.objects.create(name="Home Amenity", place=place)
        AmenityProfileRelationship.objects.create(
            amenity=amenity,
            profile=profile,
            profile_type='0'
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating superusers")
        email = "admin@admin.com"
        username = "Admin"
        first_name = "Admin"
        last_name = "Admin"
        password = "1qazxcvb"
        try:
            CustomUser.objects.get(email=email).delete()
        except:
            pass
        user = CustomUser.objects.create_superuser(email, username, first_name, last_name, password)
        profile = Profile.objects.create(user=user)
        self.generate_places(profile)

        email = "admin2@admin2.com"
        username = "Admin2"
        first_name = "Admin2"
        last_name = "Admin2"
        password = "1qazxcvb"
        try:
            CustomUser.objects.get(email=email).delete()
        except:
            pass
        user = CustomUser.objects.create_superuser(email, username, first_name, last_name,password)
        profile = Profile.objects.create(user=user)
        self.generate_places(profile)