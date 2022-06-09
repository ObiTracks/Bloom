# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models and my custom Middleware
from siteApp.middleware import RequestMiddleware
from accountsApp.models import CustomUser
from accountsApp.models import Profile
from siteApp.models import *


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        place = Place.objects.create(
            name="{}'s Place".format(profile.first_name),
            email=instance.email
            )
        amenity = Amenity.objects.create(
             name="{}'s Den".format(profile.first_name),
             place=place
        )
        PlaceProfileRelationship.objects.create(
            place=place,
            profile=profile,
            profile_type='0'
        )
        AmenityProfileRelationship.objects.create(
            amenity=amenity,
            profile=profile,
            profile_type='0'
        )

        

