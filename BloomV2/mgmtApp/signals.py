# code
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from accountsApp.models import CustomUser

from mgmtApp.middleware import RequestMiddleware
from mgmtApp.models import Amenity, AmenityProfileRelationship, Place, PlaceProfileRelationship


@receiver(post_save, sender=Amenity)
def create_amenity(sender, instance, created, **kwargs):
    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    if user:
        if created:
            AmenityProfileRelationship.objects.create(
                amenity=instance, profile=user.profile, profile_type='0')

            print("\n\n\nYEOOO Amenity Relationship created\n\n\n")


@receiver(post_save, sender=Place)
def create_amenity(sender, instance, created, **kwargs):
    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    if user:
        if created:
            PlaceProfileRelationship.objects.create(
                place=instance, profile=user.profile, profile_type='0')

            print("\n\n\nYEOOO Place Relationship created\n\n\n")