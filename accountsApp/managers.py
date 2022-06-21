from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from siteApp.models import Profile, Place


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        """
        Creates and saves a User with the given email and password.
        Additionally creates a profile for them and associates them together.
        This carries over to the create_superuser function so every superuser
        will also have a profile.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.set_password(password)
        user.save()


        return user

    def create_superuser(self, email, username, first_name, last_name,password):
        """
        Creates and saves a superuser with the given, email and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()

        return user

    def make_random_password(self, length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$%^&*()-_'):
        "Generates a random password with the given length and given allowed_chars"
        # Note that default value of allowed_chars does not have "I" or letters
        # that look like it -- just to avoid confusion.
        from random import choice
        return ''.join([choice(allowed_chars) for i in range(length)])
