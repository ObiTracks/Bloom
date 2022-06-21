import random
import time

from django.db import transaction
from django.core.management.base import BaseCommand

from accountsApp.models import CustomUser

from siteApp.factories import UserFactory


NUM_USERS = 20
NUM_PLACES = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating superuser")
        email = "admin@admin.com"
        username = "Admin"
        first_name = "Admin"
        last_name = "Admin"
        password = "1qazxcvb"
        try:
            CustomUser.objects.get(email=email).delete()
        except:
            pass
        CustomUser.objects.create_superuser(email, username, first_name, last_name, password)

        email = "admin2@admin2.com"
        username = "Admin2"
        first_name = "Admin2"
        last_name = "Admin2"
        password = "1qazxcvb"
        try:
            CustomUser.objects.get(email=email).delete()
        except:
            pass
        CustomUser.objects.create_superuser(email, username, first_name, last_name,password)