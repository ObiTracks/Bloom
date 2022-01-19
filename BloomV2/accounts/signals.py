# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models and my custom Middleware
from mgmt.middleware import RequestMiddleware
from accounts.models import CustomUser
from accounts.models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
