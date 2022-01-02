from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(Address)
admin.site.register(Reservation)
