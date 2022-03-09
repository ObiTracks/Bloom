from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from siteApp.models import Profile


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, username=None, first_name=None, last_name=None, password=None, alias=None):
        """
        Creates and saves a User with the given username, email and password.
        Additionally creates a profile for them and associates them together.
        This carries over to the create_superuser function so every superuser
        will also have a profile.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        if not first_name:
            raise ValueError('Users must have a first name')

        if not last_name:
            raise ValueError('Users must have a last name')

        if not alias:
            alias = username

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            alias=alias
        )
        print("User almost saved in database")
        user.set_password(password)
        user.save()
        print("User saved in database")


        return user

    def create_superuser(self, email, username, first_name, last_name,  password, alias=None):
        """
        Creates and saves a superuser with the given username, email and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            alias=alias
        )

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()

        # print(user, "is_superuser:", user.is_superuser)
        # print(user, "is_staff:", user.is_staff)
        # print(user, "is_active:", user.is_active)

        return user

    def make_random_password(self, length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$%^&*()-_'):
        "Generates a random password with the given length and given allowed_chars"
        # Note that default value of allowed_chars does not have "I" or letters
        # that look like it -- just to avoid confusion.
        from random import choice
        return ''.join([choice(allowed_chars) for i in range(length)])
