from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from mainApp.models import *
from accountsApp.models import *


class CreateSuperUser_and_Profile_TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = "admin@admin.com"
        self.username = "admin"
        self.first_name = "admin"
        self.last_name = "admin"
        self.password = CustomUser.objects.make_random_password()
        superuser = CustomUser.objects.create_superuser(
            email=self.email, username=self.username, first_name=self.first_name, last_name=self.last_name, password=self.password
        )

        print(superuser, "is_superuser:", superuser.is_superuser)
        print(superuser, "is_staff:", superuser.is_staff)
        print(superuser, "is_active:", superuser.is_active)

    def test_superuser_was_created_with_profile(self):
        superuser = CustomUser.objects.get(email="admin@admin.com")
        profile = superuser.profile
        assert superuser == profile.user
        assert superuser is not None
        assert profile is not None
        print(superuser, "User Belongs to Profile:", superuser == profile.user)
