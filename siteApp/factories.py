# Refererence tutorial
# https://mattsegal.dev/django-factoryboy-dummy-data.html
import factory
from factory.django import DjangoModelFactory

from accountsApp.models import CustomUser

# Defining a factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = '1qazxcvb'


# # Using a factory with auto-generated data
# admin = UserFactory()
# u.name # Kimberly
# u.id # 51

# # You can optionally pass in your own data
# u = UserFactory(name="Alice")
# u.name # Alice
# u.id # 52