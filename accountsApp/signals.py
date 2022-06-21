# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models and my custom Middleware
from siteApp.middleware import RequestMiddleware
from accountsApp.models import CustomUser
from accountsApp.models import Profile
from siteApp.models import *
import time

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        place = Place.objects.create(
            owner=profile,
            name="{}'s Place".format(profile.user.first_name),
            email=instance.email
            )
        
        PlaceProfileRelationship.objects.create(
                place=place, profile=profile, profile_type='0')

        amenity = Amenity.objects.create(name="Home Amenity", place=place)
        AmenityProfileRelationship.objects.create(
            amenity=amenity,
            profile=profile,
            profile_type='0'
        )
        print("New user created ")
        print("Place added to their account ", place)

