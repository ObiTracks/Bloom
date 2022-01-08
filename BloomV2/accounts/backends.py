from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import CustomUser

class CustomUserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        customer_id = kwargs['username']
        password = kwargs['password']
        try:
            user = CustomUser.objects.get(customer_id=customer_id)
            if user.user. user.check_password(password) is True:
                return user.user
        except CustomUser.DoesNotExist:
            pass