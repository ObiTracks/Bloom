from django.test import TestCase
from django.test.client import Client
from mgmt.models import *


class CreateSuperUser_and_Profile_TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = "admin@admin.com"
        self.username = "admin"
        self.first_name = "admin"
        self.last_name = "admin"
        self.password = CustomUser.objects.make_random_password()
        user = CustomUser.objects.create_superuser(
            email=self.email, username=self.username, first_name=self.first_name, last_name=self.last_name, password=self.password,
        )

        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(
            email=self.email, password=self.password)
        self.assertTrue(loginresponse)  # should now return "true"

    def test_superuser_was_created_with_profile(self):
        user = CustomUser.objects.get(email="admin@admin.com")
        profile = user.profile
        assert user is not None
        assert profile is not None
