from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    # Tutorial that helped build and set this up
    #  https://learndjango.com/tutorials/django-custom-user-model
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','first_name','last_name',]

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(Address)
admin.site.register(Reservation)

# Relational Models
admin.site.register(AmenityProfileRelationship)
admin.site.register(PlaceProfileRelationship)
