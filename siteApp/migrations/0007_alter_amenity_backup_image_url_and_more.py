# Generated by Django 4.0 on 2022-06-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0006_rename_backup_random_image_url_amenity_backup_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='backup_image_url',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='place',
            name='backup_image_url',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]