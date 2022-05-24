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
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

# from .backends import *
from .forms import *
from .models import *
# Create your views here.
# Create your views here.
# LOGIN LOGOUT AND SIGNUP VIEWS


def login_view(request):
    if request.user.is_authenticated:
        print("User is already logged in")
        return redirect('manage-dashboard')

    page_title = "Login"
    login_form = AuthenticationForm(request)
    register_form = CustomUserCreationForm()

    context = {
        'page_title': page_title,
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, '../templates/accountsApp/login.html', context)


def login_request(request):
    if request.user.is_authenticated:
        print("User is already logged in")
        return redirect('management-dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("User logged In")
            return redirect('manage-dashboard')
        else:
            messages.error(request, 'Username OR password is incorrect')

    # context = {'page_title': page_title}
    return redirect('login')


def signup_request(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Welcome to Bloom')
            # print("New user {} created".format(user))

            return redirect('siteApp:dashboard')

    return login_view(request)


def logout_request(request):
    logout(request)
    return redirect('login')
