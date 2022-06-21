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
from django.db.models import Count, Q

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator


from .models import *
from .querytools import getUsersPlacesAndAmenities
# Create your views here.


#******************
# ENDPOINT VIEWS
#******************
def sendjoin_request(request, place_pk=None):
    if place_pk == None:
        messages.error(request, 'Place not provided for join request')
        return

    
    profile = request.user.profile
    place = Place.objects.get(pk=place_pk)

    #Check if the user has access already - ie existing join request exists
    request_exists = JoinRequest.objects.filter(place=place, profile=profile).exists()
    #Check if the user has access already - ie existing place profile relationship
    relationship_exists = PlaceProfileRelationship.objects.filter(place=place, profile=profile).exists()


    if request_exists or relationship_exists:
        print("Join Request Cancelling Operation\n")
        messages.error(request, 'Join Reqest already exists')
        return redirect(request.META['HTTP_REFERER'])
    
    join_request = JoinRequest.objects.create(profile=profile, place=place)
    join_request.save()

    return redirect(request.META['HTTP_REFERER'])
    # return redirect('manage-dashboard')

def approvejoin_request(request, joinrequest_pk):
    if joinrequest_pk == None:
        messages.error(request, 'Join Request id not provided for join request')
        return redirect(request.META['HTTP_REFERER'])

    try:
        joinrequest = JoinRequest.objects.get(pk=joinrequest_pk)
        joinrequest.approved = True
        joinrequest.save()
    except JoinRequest.DoesNotExist:
        messages.error(request, 'Join Request does not exist')
        return redirect(request.META['HTTP_REFERER'])

    #Check if the user has access already - ie existing place profile relationship
    try:
        relationship = PlaceProfileRelationship.objects.get(
            profile =joinrequest.profile,
            place=joinrequest.place
        )
        messages.error(request, 'Already member of the place')
        return redirect(request.META['HTTP_REFERER'])
    except PlaceProfileRelationship.DoesNotExist:
        relationship = PlaceProfileRelationship(
            place=joinrequest.place, 
            profile=joinrequest.profile,
            profile_type='5'
        ).save()

        joinrequest.delete()
        pass
    messages.success(request, 'Join request accepted')
    return redirect(request.META['HTTP_REFERER'])

def rejectjoin_request(request, joinrequest_pk):
    if joinrequest_pk == None:
        messages.error(request, 'Join Request id not provided for join request')
        return redirect(request.META['HTTP_REFERER'])

    try:
        joinrequest = JoinRequest.objects.get(pk=joinrequest_pk)
        joinrequest.delete()
    except JoinRequest.DoesNotExist:
        messages.error(request, 'Join Request not provided for join request')

    messages.error(request, 'Join request rejected')
    return redirect(request.META['HTTP_REFERER'])