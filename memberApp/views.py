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
from django.db.models import Count, Q

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from siteApp.models import *
from siteApp.querytools import getUsersPlacesAndAmenities
# Create your views here.


def dashboard_view(request):
    # Object data
    page_title = "Dashboard"
    page_subtitle = "Book"
    places, amenity_groupings = getUsersPlacesAndAmenities(request)


    context = {
        'page_title': page_title,
        'page_subtitle':page_subtitle,
        'amenity_groupings': amenity_groupings,
    }

    template_name = 'memberApp/dashboard.html'
    return render(request, template_name, context)


def community_view(request):
    page_title = "Browse the Community"
    page_subtitle = "Join a Community"

    # places = Place.objects.all()
    places = Place.objects.filter(~Q(place_of__profile=request.user.profile))
    
    
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'places':places
    }
    template_name = 'memberApp/community.html'
    return render(request, template_name, context)


def amenity_view(request, pk):
    # Object data
    amenity = Amenity.objects.get(id=pk)
    jsonTimeslots = amenity.timeslots

    page_title = amenity.name
    page_subtitle = amenity.place.name

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity':amenity,
        'jsonTimeslots':jsonTimeslots,
    }

    template_name = 'memberApp/amenity.html'
    return render(request, template_name, context)
