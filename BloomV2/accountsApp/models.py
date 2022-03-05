from django.db import models

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from mgmtApp.models import Profile

# Custom User Management
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# CUSTOM USER MODEL

class CustomUser(AbstractUser):
    # Tutorial that helped build and set this up
    # https://learndjango.com/tutorials/django-custom-user-model
    email = models.EmailField(verbose_name='Email',
                              unique=True, null=False, blank=False)
    username = models.CharField(max_length=20, blank=False, unique=True)
    alias = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # define the user manager class for User
    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.email)

