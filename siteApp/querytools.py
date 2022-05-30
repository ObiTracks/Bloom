# Python packages
# import datetime as dt
from datetime import date, datetime, timedelta

import json
from ntpath import join
from django.core.serializers.json import DjangoJSONEncoder

# Imports for Django views
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Imports for django forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Imports for django models
from django.db.models import Count

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

from mgmtApp.forms import *
from .models import *


def getUsersPlacesAndAmenities(request, num_amenities=None, place_id=None):
    place_amenity_groupings = {}

    if place_id:
        place = Place.objects.get(id=place_id)
        places = place
        amenities = place.amenity_set.all() if not num_amenities else place.amenity_set.all()[:num_amenities]
        place_amenity_groupings[place] = amenities if amenities.count() > 0 else None

    else:
        place_relationships = PlaceProfileRelationship.objects.filter(
            profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
        places = [i.place for i in place_relationships]
        
        for place in places:
            print(place)
            amenities = place.amenity_set.all() if not num_amenities else place.amenity_set.all()[:num_amenities]
            print(amenities)

            place_amenity_groupings[place] = amenities if amenities.count() > 0 else None
    
    print(place_amenity_groupings)
    
    return places, place_amenity_groupings

def getUsersPlacesAndJoinRequest(request, number_of_joinrequests_each = None):
    place_relationships = PlaceProfileRelationship.objects.filter(
        profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
    places = [i.place for i in place_relationships]

    

    place_request_groupings = {}
    for place in places:
        joinrequests = place.joinrequest_set.exclude(profile=request.user.profile)
        # joinrequests = JoinRequest.objects.all()
        print(place)
        print(joinrequests)
        if joinrequests.count() > 0:
            place_request_groupings[place] = joinrequests 

    return places, place_request_groupings


