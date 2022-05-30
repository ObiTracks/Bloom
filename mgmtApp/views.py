# Python packages
# import datetime as dt
from datetime import date, datetime, timedelta

import json
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

from .forms import *
from siteApp.models import *
from siteApp.querytools import getUsersPlacesAndAmenities, getUsersPlacesAndJoinRequest
from mgmtApp.crud_views import new_place
# Create your views here.


def dashboard_view(request):
    page_title = "Dashboard"
    page_subtitle = "Manage"
    places, amenity_groupings = getUsersPlacesAndAmenities(request, 2)

    # print(amenity_groupings)
    if request.method == "POST":
        place_form = PlaceForm(
            request.POST, request.FILES)
        if place_form.is_valid():
            place = place_form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Amenity Form is invalid")

    place_form = PlaceForm()
    # new_place(request)

    context = {
        'page_title': page_title,
        'page_subtitle':page_subtitle,
        'amenity_groupings': amenity_groupings,
        'place_form': place_form,
        #    'amenity_form': amenity_form,
    }

    template_name = 'mgmtApp/dashboard.html'
    return render(request, template_name, context)


def places_view(request):
    # Object data
    page_title = "Places & Amenities"
    page_subtitle = "Manage"
    places, amenity_groupings = getUsersPlacesAndAmenities(request)

    # Forms & Interactions
    amenity_form = AmenityForm(request.user)
    if request.method == 'POST':
        amenity_form = AmenityForm(request.user, request.POST, request.FILES)

        if amenity_form.is_valid():
            amenity = amenity_form.save()
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('dashboard')
        else:
            messages.error(request, "Amenity Form is invalid")
    
    new_place(request)

    context = {
        'page_title': page_title,
        'page_subtitle':page_subtitle,
        'amenity_form': amenity_form,
        # 'place_form': place_form,
        'amenity_groupings': amenity_groupings,
    }
    template_name = 'mgmtApp/places.html'
    return render(request, template_name, context)

def place_view(request, pk):
    # Object data
    places, amenity_groupings = getUsersPlacesAndAmenities(request, place_id=pk)
    place = places
    page_title = place.name
    page_subtitle = "Places"

    place_form = PlaceForm(instance=place)
    if request.method == 'POST':
        place_form = PlaceForm(request.POST, request.FILES, instance=place)

        if place_form.is_valid():
            place = place_form.save()
            # return
            # return redirect(request.META['HTTP_REFERER'])

            return redirect(request.META['HTTP_REFERER'])
            # return redirect('dashboard')
        else:
            messages.error(request, "Place Form is invalid")

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'place_form': place_form,
        'place':place,
        'amenity_groupings':amenity_groupings
    }
    template_name = 'mgmtApp/place.html'
    return render(request, template_name, context)

def amenity_view(request, pk):
    # Object data
    amenity = Amenity.objects.get(id=pk)
    page_title = amenity.name
    page_subtitle = amenity.place.name

    amenity_form = AmenityForm(request.user, instance=amenity)
    if request.method == 'POST':
        amenity_form = AmenityForm(
            request.user, request.POST, request.FILES, instance=amenity)

        if amenity_form.is_valid():
            amenity = amenity_form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Amenity Form is invalid")

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity_form': amenity_form,
        'amenity':amenity
    }
    template_name = 'mgmtApp/amenity.html'
    return render(request, template_name, context)

def joinrequests_view(request):
    # Object data
    page_subtitle = "Manage"
    page_title = "Join Requests"

    _, joinrequest_groupings = getUsersPlacesAndJoinRequest(request, 5)
    
    print(joinrequest_groupings)
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'joinrequest_groupings': joinrequest_groupings
    }
    template_name = 'mgmtApp/joinrequests.html'
    return render(request, template_name, context)
