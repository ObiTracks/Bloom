# Generated by Django 3.0.8 on 2020-09-07 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_auto_20200907_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lease_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.Customer'),
        ),
    ]
