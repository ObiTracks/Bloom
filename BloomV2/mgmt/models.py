from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
# Create your models here.


class Amenity(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    # day_time_availability = \
    # ArrayField(
    #     ArrayField(
    #         ArrayField(
    #             models.TimeField(null=True), size=2
    #         ), size=24, null=True, blank=True
    #     ), size=7, null=True
    # )

    duration_slot = models.TimeField(default=None, auto_now=False, auto_now_add=False)
    
