# Generated by Django 4.2.19 on 2025-04-28 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0027_image_description'),
        ('home', '0015_rename_carousel_image_homepagegalleryimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagegalleryimages',
            name='image_setoise_part1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
