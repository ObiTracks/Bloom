from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
from accountsApp.models import *
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

class LogInTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'email': "admin@admin.com",
            'username': "admin",
            'first_name': "admin",
            'last_name': "admin",
            'password': CustomUser.objects.make_random_password(),

        }

        self.user = CustomUser.objects.create_user(**self.credentials)

    # def test_signup_page_url(self):
    #     response = self.client.get("http://127.0.0.1:8000/auth/signup_request")
    #     self.assertEqual(response.status_code, 302)

    # def test_signup_page_view_name(self):
    #     response = self.client.get(reverse('signup_request'))
    #     self.assertEqual(response.status_code, 200)
        

    # def test_signup_form(self):
    #     response = self.client.post(reverse('signup_request'), data={
    #         'email': "admin@admin.com",
    #         'username': "admin",
    #         'first_name': "admin",
    #         'last_name': "admin",
    #         'password': CustomUser.objects.make_random_password(),
    #     })
    #     self.assertEqual(response.status_code, 200)

        # users = get_user_model().objects.all()
        # self.assertEqual(users.count(), 1)
