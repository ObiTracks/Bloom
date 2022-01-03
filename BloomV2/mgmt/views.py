# Python packages
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required

# Imports for Django views
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
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *
# Create your views here.


def dashboard_view(request):
    page_title = "Main Dashboard"
    context = {'page_title': page_title}
    template_name = '../templates/pages/dashboard.html'
    return render(request, template_name, context)


def amenityhub_view(request):
    page_title = "Amenity Hub"
    amenity_relationships = AmenityProfileRelationship.objects.filter(
        profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
    amenities = [i.amenity for i in amenity_relationships]

    objects = ("0", "1", "2", "3")
    object_context = {'objects': objects}
    context = {
        'page_title': page_title,
        'amenities': amenities,
        'object_context': object_context
    }
    template_name = '../templates/pages/amenityhub.html'
    return render(request, template_name, context)


def amenityobject_view(request, pk):
    page_title = "Amenity Name"
    page_subtitle = "Amenities"
    context = {'page_title': page_title, 'page_subtitle': page_subtitle}
    template_name = '../templates/pages/amenityobject.html'
    return render(request, template_name, context)


# LOGIN LOGOUT AND SIGNUP VIEWS

def login_view(request):
    if request.user.is_authenticated:
        print("User is already logged in")
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("User logged In")
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, '../templates/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('landingpage')


def signup_view(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, f'Welcome to Bloom')
            print("New user created")

            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        register_form = UserRegisterForm()

    context = {'register_form': register_form}

    return render(request, '../templates/signup.html', context)
