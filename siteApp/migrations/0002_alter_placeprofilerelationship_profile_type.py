# Generated by Django 4.0 on 2022-06-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeprofilerelationship',
            name='profile_type',
            field=models.CharField(choices=[('0', 'Owner'), ('1', 'Manager'), ('2', 'Supervisor'), ('3', 'Staff'), ('4', 'Authorized User'), ('5', 'Member')], default='Member', max_length=100),
        ),
    ]
