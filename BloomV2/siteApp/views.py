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


from .models import *
from .querytools import getUsersPlacesAndAmenities
# Create your views here.


def landingpage_view(request):
    page_title = "Welcome to Bloom"
    context = {'page_title': page_title, }
    template_name = 'landingpage.html'
    return render(request, template_name, context)

#******************
# ENDPOINT VIEWS
#******************
def sendjoin_request(request, place_pk=None):
    if place_pk == None:
        messages.error(request, 'Place not provided for join request')
        return

    profile = request.user.profile
    place = Place.objects.get(pk=place_pk)

    #Check if the user has access already - ie existing place profile relationship
    exists = PlaceProfileRelationship.objects.filter(
        place=place,
        profile=profile,
    ).exists()
    if exists:
        messages.error(request, 'Already member of the place')
        return
    
    join_request = JoinRequest.objects.create(profile=profile, place=place)
    join_request.save()

    return

def approvejoin_request(request, joinrequest_pk):
    if joinrequest_pk == None:
        messages.error(request, 'Join Request id not provided for join request')
        return

    try:
        joinrequest = JoinRequest.objects.get(pk=joinrequest_pk)
        joinrequest.approved = True
        joinrequest.save()
    except JoinRequest.DoesNotExist:
        messages.error(request, 'Join Request does not exist')
        return

    #Check if the user has access already - ie existing place profile relationship
    try:
        relationship = PlaceProfileRelationship.objects.get(
            profle =joinrequest.place,
            place=joinrequest.place
        )
        messages.error(request, 'Already member of the place')
        return
    except PlaceProfileRelationship.DoesNotExist:
        relationship = PlaceProfileRelationship(
            place=joinrequest.place, 
            profile=joinrequest.profile,
            profile_type='5'
        ).save()

        joinrequest.delete()
        pass

    return

def rejectjoin_request(request, joinrequest_pk):
    if joinrequest_pk == None:
        messages.error(request, 'Join Request id not provided for join request')
        return

    try:
        joinrequest = JoinRequest.objects.get(pk=joinrequest_pk)
        joinrequest.delete()
    except JoinRequest.DoesNotExist:
        messages.error(request, 'Join Request not provided for join request')

    return