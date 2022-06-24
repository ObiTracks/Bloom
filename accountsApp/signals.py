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
        user = instance
        profile = Profile.objects.create(user=user)
        time.sleep(0.1)
        # place = Place.objects.create(owner=profile, name=f"{user.first_name}'s Place")
        # post_save.send(Place, instance=place, created=True)
        print("\n\nPlace Created")
        print("New user created ")
        # print("Place added to their account ", place)

