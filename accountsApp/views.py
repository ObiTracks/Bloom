# Python packages
from datetime import date
import re
from django.contrib.admin.views.decorators import staff_member_required

# Imports for Django views
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Imports for django forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

# from .backends import *

from .forms import *
from .models import *
import siteApp
# Create your views here.
# Create your views here.
# LOGIN LOGOUT AND SIGNUP VIEWS


def auth_view(request):
    if request.user.is_authenticated:
        print("User is already logged in")
        return redirect('manage:manage-dashboard')

    page_title = "Login"
    login_form = LoginForm()
    register_form = CustomUserCreationForm()

    context = {
        'page_title': page_title,
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, '../templates/accountsApp/auth.html', context)


def login_request(request):
    if request.user.is_authenticated:
        print("Already logged in")
        return redirect('management-dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print(form.cleaned_data)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request, 
                username=email, 
                password=password,
                # backend='django.contrib.auth.backends.ModelBackend',
                )

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back")
                return redirect('manage:manage-dashboard')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect(request.META['HTTP_REFERER'])
        else:
            print("Form isn't valid")
    print("Website Load")
    return redirect(request.META['HTTP_REFERER'])


def signup_request(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Form filled")
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            profile = Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print("Authenitcating user...")
            # user = authenticate(
            #     request, 
            #     email=email, 
            #     password=password,
            # )

            login(request, user, backend='accountsApp.backends.EmailBackend')
            print("Authenitated")
            print("Logged in.")

            place = siteApp.models.Place.objects.create(
                owner=profile,
                name="{}'s Place".format(user.first_name),
                email=email
                )
            amenity = siteApp.models.Amenity.objects.create(name="Home", place=place)

            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Welcome to Bloom {first_name}!')
            # print("New user {} created".format(user))

            print("Redirecting to dashboard.")
            return redirect('manage:manage-dashboard')
        else:
            messages.error(request, f'Signup failed')

    return redirect(request.META['HTTP_REFERER'])

def logout_request(request):
    logout(request)
    return redirect('external:landing')
