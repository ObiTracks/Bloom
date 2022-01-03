from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, username=None, first_name=None, last_name=None, password=None):
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

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save()

        from .models import Profile
        Profile.objects.create(
            user=user)
        return user

    def create_superuser(self, email, username, first_name, last_name,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        print(user, "is_superuser:", user.is_superuser)
        print(user, "is_staff:", user.is_staff)
        print(user, "is_active", user.is_active)

        return user
