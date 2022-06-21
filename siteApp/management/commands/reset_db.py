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
        self.stdout.write("Resetting database superuser")
        import os
        os.system("python manage.py flush")
