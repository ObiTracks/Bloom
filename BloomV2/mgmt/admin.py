from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']

    class Meta:
        model = CustomUser


admin.site.register(CustomUser)


# Register your models here.
admin.site.register(Profile)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(Address)
admin.site.register(Reservation)

# Relational Models
admin.site.register(AmenityProfileRelationship)
admin.site.register(PlaceProfileRelationship)
