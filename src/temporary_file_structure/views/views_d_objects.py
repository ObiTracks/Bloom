from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, staff_member_required

#View imports here
from .models import (Customer, Day, TimeSlot, Reservation)
from .forms import *
from .filters import CustomerFilter

def customer(request, pk):
    resident = Customer.objects.get(id=pk)
    reservations = resident.reservation_set.all()
    page_title = "Customer " + resident.name
    context = {
        "page_title": page_title,
        'resident': resident,
        'reservations': reservations
    }
    template_name = 'customer/customer_info.html'

    return render(request, template_name, context)

def day(request, pk):
    day = Day.objects.get(id=pk)
    stats = {'stat1': {'name': 'Total Reservations', 'value': day.day}}
    page_title = day.day
    context = {"page_title": page_title, 'day': day, 'stats': stats}
    template_name = 'day/day_info.html'

    return render(request, template_name, context)

def timeslot(request, pk):
    timeslot = TimeSlot.objects.get(id=pk)
    page_title = "All Days"
    stats = {
        'stat1': {
            'title': 'Total Reservations',
            'value': timeslot.reservation_set.count
        },
        'stat2': {
            'title': 'Total No Shows',
            'value': 'some_value'
        },
        # 'stat3': {
        #     'title': 'Total Residents',
        #     'value': 'some_value'
        # },
        # 'stat4': {
        #     'title': 'Avg No Shows per Day',
        #     'value': 'some_value'
        # }
    }

    context = {
        'timeslot':timeslot,
        'page_title': page_title,
        'stats': stats
        }
    template_name = 'timeslot/timeslot_info.html'

    return render(request, template_name, context)

def reservation(request):
    context = {}
    template_name = 'reservation/reservation_info.html'

    return render(request, template_name, context)