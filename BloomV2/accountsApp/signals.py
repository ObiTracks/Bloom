# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models and my custom Middleware
from mainApp.middleware import RequestMiddleware
from accountsApp.models import CustomUser
from accountsApp.models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
