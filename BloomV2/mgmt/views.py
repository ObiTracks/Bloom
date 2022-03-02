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
    template_name = 'pages/manager/dashboard.html'
    return render(request, template_name, context)


def amenityhub_view(request):
    # Object data
    page_title = "Amenity Hub"
    page_subtitle = "Places and Amenities"

    # PLACES MANAGED
    try:
        place_relationships = PlaceProfileRelationship.objects.filter(
            profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
        places_managed = [i.place for i in place_relationships]
    except:
        places_managed = None

    amenity_groupings = {}
    for place in places_managed:
        amenities = Amenity.objects.filter(
            place=place)
        if place not in amenity_groupings:
            amenity_groupings[place] = amenities

    # Forms & Interactions
    amenity_form = AmenityForm(request.user)
    new_amenity(request)

    place_form = PlaceForm()
    new_place(request)

    context = {
        'page_title': page_title,
        'amenity_form': amenity_form,
        'place_form': place_form,
        'amenity_groupings': amenity_groupings,
    }
    template_name = 'pages/manager/amenityhub.html'
    return render(request, template_name, context)

# Amenity Form Handler


def new_amenity(request):
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

# Place Form Handler


def new_place(request):
    if request.method == 'POST':
        place_form = PlaceForm(request.POST, request.FILES)

        if place_form.is_valid():
            place = place_form.save()
            placeprofile_relationship = PlaceProfileRelationship.objects.create(
                place=place, profile=request.user.profile, profile_type="0")
            placeprofile_relationship.save()

            return redirect('amenityhub')
        else:
            messages.error(request, "Place Form is invalid")

    return


def amenityobject_view(request, pk):
    amenity = Amenity.objects.get(pk=pk)
    page_title = amenity.name
    page_subtitle = "Amenities"

    context = {'page_title': page_title, 'page_subtitle': page_subtitle, 'amenity':amenity}
    template_name = 'pages/manager/amenityobject.html'
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

    print("Member Groupings", member_groupings)

    # RESERVATIONS
    reservations = []
    for place in places_managed:
        place_reservations = list(place.reservation_set.all())
        print("Reservations: ", place,
              len(place_reservations), place_reservations)

        if place_reservations:

            reservations.extend(place_reservations)
    print(reservations)

    # STATISTICS
    UserManagedReservations = Reservation.objects \
        .filter(place__place_of__profile_type__in=['0', '1', '2', '3', '4'],
                place__place_of__profile=request.user.profile)\

    # Statistic: total_members
    total_members = UserManagedReservations.count()

    # Statistic: reservations_today
    reservations_today = UserManagedReservations \
        .filter(date_created__gte=date.today())

    # Statistic: no_shows_past_week
    no_shows_past_week = UserManagedReservations.filter(
        date_created__gte=date.today() - timedelta(days=7)).filter(no_show=True)

    # Statistic: members_managed
    members_managed = set()
    for place in places_managed:
        members = set(Profile.objects.filter(
            place_profile_of__profile_type__in=['5']))
        staged = [members_managed.add(i) for i in members]
    members_managed = list(members_managed)
    print(members_managed)

    new_members_this_month = None
    # new_members_this_month = [member for member in members_managed if member.date_created > (
    #     date.today() - timedelta(days=30))]

    statistics = {}
    statistics["total_members"] = total_members
    statistics["reservations_today"] = reservations_today
    statistics["no_shows_past_week"] = no_shows_past_week
    statistics["new_members_this_month"] = new_members_this_month

    # print(statistics[reservations_today])

    context = {
        'statistics': statistics,
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'place_relationships': place_relationships,
        'member_groupings': member_groupings,
        'reservations': reservations,
    }
    template_name = 'pages/manager/memberhub.html'
    return render(request, template_name, context)


def memberobject_view(request):
    page_title = "Amenity Name"
    page_subtitle = "Amenities"
    context = {'page_title': page_title, 'page_subtitle': page_subtitle}
    template_name = 'pages/manager/memberobject.html'
    return render(request, template_name, context)
