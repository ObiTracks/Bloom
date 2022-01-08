# Python packages
from datetime import date
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

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *
# Create your views here.


def dashboard_view(request):
    page_title = "Main Dashboard"
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
    template_name = '../templates/pages/dashboard.html'
    return render(request, template_name, context)


def amenityhub_view(request):
    # Object data
    page_title = "Amenity Hub"
    page_subtitle = "Places and Amenities"
    try:
        amenity_relationships = AmenityProfileRelationship.objects.filter(
            profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
        amenities = [i.amenity for i in amenity_relationships]
    except:
        amenities = None

    # Form Interaction
    form = AmenityForm(request.user)
    if request.method == 'POST':
        form = AmenityForm(request.user, request.POST, request.FILES)

        if form.is_valid():
            amenity = form.save()
            amenityprofile_relationship = AmenityProfileRelationship.objects.create(
                amenity=amenity, profile=request.user.profile, profile_type="3")
            amenityprofile_relationship.save()

            return redirect('amenityhub')
        else:
            messages.error(request, "Form is invalid")

    context = {
        'page_title': page_title,
        'form': form,
        'amenities': amenities,
    }
    template_name = '../templates/pages/amenityhub.html'
    return render(request, template_name, context)


def amenityobject_view(request):
    page_title = "Amenity Name"
    page_subtitle = "Amenities"
    context = {'page_title': page_title, 'page_subtitle': page_subtitle}
    template_name = '../templates/pages/amenityobject.html'
    return render(request, template_name, context)


def memberhub_view(request):
    page_title = "Member Hub"
    page_subtitle = "Members"

    # MEMBERS AND PLACES
    try:
        place_relationships = PlaceProfileRelationship.objects.filter(
            profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
        places_managed = [i.place for i in place_relationships]
    except:
        places_managed = None

    member_groupings = {}
    for place in places_managed:
        place_member_relationships = PlaceProfileRelationship.objects.filter(
            place=place, profile_type__in=['5'])
        members = [i.profile for i in place_member_relationships]
        if place not in member_groupings:
            member_groupings[place] = members
        # else:
        #     member_groupings[place]

    print(member_groupings)

    # RESERVATIONS
    reservations = []
    for place in places_managed:
        place_reservations = place.reservation_set
        print(place_reservations)
        reservations.append(place_reservations)

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'place_relationships': place_relationships,
        'member_groupings': member_groupings,
        'reservations': reservations,
    }
    template_name = '../templates/pages/memberhub.html'
    return render(request, template_name, context)


def memberobject_view(request):
    page_title = "Amenity Name"
    page_subtitle = "Amenities"
    context = {'page_title': page_title, 'page_subtitle': page_subtitle}
    template_name = '../templates/pages/memberobject.html'
    return render(request, template_name, context)
