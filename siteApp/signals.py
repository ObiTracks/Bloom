# code
from time import sleep
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from accountsApp.models import CustomUser

from siteApp.middleware import RequestMiddleware
from siteApp.models import Amenity, AmenityProfileRelationship, Place, PlaceProfileRelationship

@receiver(post_save, sender=Place)
def create_place(sender, instance, created, **kwargs):
    request = RequestMiddleware(get_response=None)
    try:
        request = request.thread_local.current_request
    except AttributeError as e:
        return

    user = request.user
    if user:
        if created:
            # Getting the objects
            profile = user.profile
            place = instance
            # Setting the owner
            place.owner = profile
            place.save()
            # Creating the relationshi
            PlaceProfileRelationship.objects.create(
                place=place, profile=profile, profile_type='0')
            print("Sleeping")
            sleep(3)
            print("Done waiting")
            amenity = Amenity.objects.create(name="Home Amenity", place=place)
            AmenityProfileRelationship.objects.create(
                amenity=amenity,
                profile=profile,
                profile_type='0'
            )

            print("\nSignal: Place Relationship created\n")
        

@receiver(post_save, sender=Amenity)
def create_amenity(sender, instance, created, **kwargs):
    request = RequestMiddleware(get_response=None)
    try:
        request = request.thread_local.current_request
    except AttributeError as e:
        return

    user = request.user
    if user:
        if created:
            AmenityProfileRelationship.objects.create(
                amenity=instance, profile=user.profile, profile_type='0')

            print("\nSignal: Amenity Relationship created\n")


