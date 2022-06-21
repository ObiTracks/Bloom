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
        # profile = Profile.objects.get_or_create(user=instance)
        print("New user created ")
        # print("Place added to their account ", place)

