# Generated by Django 3.0.8 on 2020-08-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0013_auto_20200811_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
