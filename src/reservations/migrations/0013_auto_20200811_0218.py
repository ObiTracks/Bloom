# Generated by Django 3.0.8 on 2020-08-11 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_auto_20200811_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='apt_number',
            new_name='apt',
        ),
    ]
