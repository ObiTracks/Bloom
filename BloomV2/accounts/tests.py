from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
from accounts.models import *
from django.urls import reverse


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
