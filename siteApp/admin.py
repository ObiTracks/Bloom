from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(Address)
admin.site.register(JoinRequest)
admin.site.register(Reservation)

# Relational Models
admin.site.register(AmenityProfileRelationship)
admin.site.register(PlaceProfileRelationship)
