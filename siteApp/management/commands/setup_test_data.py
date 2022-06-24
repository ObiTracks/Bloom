import random
import time
# import factory
from faker import Faker


from django.db import transaction
from django.core.management.base import BaseCommand

from accountsApp.models import CustomUser
from siteApp.models import Place, Profile, Amenity, PlaceProfileRelationship, AmenityProfileRelationship
# from siteApp.factories import UserFactory


NUM_USERS = 5
NUM_PLACES = 1


class Command(BaseCommand):
    help = "Generates test data"

    def generate_places(self, profile):
        place = Place.objects.create(
            owner=profile, name="{}'s Place".format(profile.user.first_name))
        PlaceProfileRelationship.objects.create(
            place=place, profile=profile, profile_type='0')
        amenity = Amenity.objects.create(name="Home Base", place=place)
        AmenityProfileRelationship.objects.create(
            amenity=amenity,
            profile=profile,
            profile_type='0'
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [CustomUser]
        for m in models:
            m.objects.filter(is_staff=False).delete()

        self.stdout.write("...\n\n...")
        self.stdout.write("Creating new data...")

        faker = Faker()

        for _ in range(NUM_USERS):
            username = str(faker.user_name())
            first_name = str(faker.first_name())
            last_name = str(faker.last_name())
            email = f"{first_name[0].lower()}{last_name.lower()}@email.com"
            password = '1qazxcvb'
            print(email, first_name, last_name)
            try:
                CustomUser.objects.get(email=email).delete()
            except:
                pass
            user = CustomUser.objects.create_user(
                email=email, username=username, first_name=first_name, last_name=last_name, password=password)
            self.generate_places(profile=Profile.objects.get(user=user))
            time.sleep(0.1)
