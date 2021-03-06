# Generated by Django 3.0.8 on 2020-08-09 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='date',
        ),
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='day_after_field',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 0, 51, 35, 772192)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='apt_number',
            field=models.IntegerField(default='205'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default='someemail@gmail.com', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Person Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='805.555.3809', max_length=200, null=True),
        ),
    ]
