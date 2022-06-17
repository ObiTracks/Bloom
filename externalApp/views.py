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

from siteApp.forms import *
from siteApp.models import *
from siteApp.querytools import *
from mgmtApp.crud_views import new_place
# Create your views here.


def landing(request):

    context = {
    }

    template_name = 'externalApp/landing.html'
    return render(request, template_name, context)