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

    def generate_places(self, profile):
        place = Place.objects.create(
            owner=profile, name="{}'s Place".format(profile.user.first_name))
        PlaceProfileRelationship.objects.create(
            place=place, profile=profile, profile_type='0')
        amenity = Amenity.objects.create(name="Home Amenity", place=place)
        AmenityProfileRelationship.objects.create(
            amenity=amenity,
            profile=profile,
            profile_type='0'
        )

    def clear_db_user(self, email):
        CustomUser.objects.get(email=email).delete()
        # Profile.objects.get(user=user).delete()
        # user.delete()

    def create_user(self, email, username, first_name, last_name, password):
        try:
            self.clear_db_user(email)
        except:
            pass
        user = CustomUser.objects.create_superuser(
            email, username, first_name, last_name, password)
        # time.sleep()
        profile = Profile.objects.get(user=user)
        self.generate_places(profile)

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating superusers")
        
        for i in range(1,3):
            if i == 1:
                n = ''
            else:
                n = str(i)
            print("\nIteration", i)
            email = f"admin{n}@admin.com"
            username = f"Admin{n}"
            first_name = f"Admin{n}"
            last_name = f"Admin{n}"
            password = "1qazxcvb"
            self.create_user(email, username, first_name, last_name, password)
            print(f"\n#{n} superuser created\n")

        # email = "admin2@admin2.com"
        # username = "Admin2"
        # first_name = "Admin2"
        # last_name = "Admin2"
        # password = "1qazxcvb"
        # self.create_user(email, username, first_name, last_name, password)
