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
        self.stdout.write("Deleting old data...")
        models = [CustomUser]
        for m in models:
            m.objects.filter(is_staff=False).delete()
        
        self.stdout.write("...\n\n\n\n...")
        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)
