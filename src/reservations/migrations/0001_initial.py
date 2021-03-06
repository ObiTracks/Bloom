# Generated by Django 3.0.8 on 2020-08-08 23:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('apt_number', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('lease_members', models.ManyToManyField(blank=True, related_name='_customer_lease_members_+', to='reservations.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 8, 9))),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(default='Choose a time window', max_length=10, null=True)),
                ('pool_status_full', models.BooleanField(default=False, verbose_name='Time slot at capacity')),
                ('capacity', models.IntegerField(blank=True, default=13)),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_show', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='reservations.Customer')),
                ('party_members', models.ManyToManyField(blank=True, related_name='party_members', to='reservations.Customer')),
                ('timeslot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.TimeSlot')),
            ],
        ),
    ]
