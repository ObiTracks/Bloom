# Python packages
# import datetime as dt
from datetime import date, datetime, timedelta

import json

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

from .forms import *
from mgmt.models import *
# Create your views here.


def dashboard_view(request):
    page_title = "Dashboard"
    # AMENITIES
    amenity_relationships = AmenityProfileRelationship.objects.filter(
        profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
    amenities = [i.amenity for i in amenity_relationships]

    # Grouping Amenities by Place
    amenity_groupings = {}
    for amenity in amenities:
        if amenity.place not in amenity_groupings:
            amenity_groupings[amenity.place] = [amenity]
        else:
            amenity_groupings[amenity.place].append(amenity)

    print(amenity_groupings)

    # MEMBERS
    # members = [i.member_set for i in amenities]

    context = {'page_title': page_title,
               'amenity_groupings': amenity_groupings}

    template_name = 'pages/member/memberdashboard.html'
    return render(request, template_name, context)


def places_view(request):
     # AMENITIES
    amenity_relationships = AmenityProfileRelationship.objects.filter(
        profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
    amenities = [i.amenity for i in amenity_relationships]

    # Grouping Amenities by Place
    amenity_groupings = {}
    for amenity in amenities:
        if amenity.place not in amenity_groupings:
            amenity_groupings[amenity.place] = [amenity]
        else:
            amenity_groupings[amenity.place].append(amenity)


    # Object data
    page_title = "Places"
    page_subtitle = "Your Places"

    place_relationships = PlaceProfileRelationship.objects.filter(
        profile=request.user.profile, profile_type__in=['5', ])
    places = [i.place for i in place_relationships]
    recent_amenities = Reservation.objects.filter(place__in=places)[:3]

    

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'recent_amenities': recent_amenities,
        'amenity_groupings':amenity_groupings,
    }
    template_name = 'pages/member/places.html'
    return render(request, template_name, context)


def amenity_view(request):
    # Object data
    page_title = ""
    page_subtitle = ""

    context = {
        'page_title': page_title,
    }
    template_name = 'pages/member/amenityhub.html'
    return render(request, template_name, context)


def send_joinrequest(request):
    if request.method == 'POST':
        amenity_form = AmenityForm(request.user, request.POST, request.FILES)

        if amenity_form.is_valid():
            amenity = amenity_form.save()
            amenityprofile_relationship = AmenityProfileRelationship.objects.create(
                amenity=amenity, profile=request.user.profile, profile_type="3")
            amenityprofile_relationship.save()

            return redirect('amenityhub')
        else:
            messages.error(request, "Amenity Form is invalid")

    return