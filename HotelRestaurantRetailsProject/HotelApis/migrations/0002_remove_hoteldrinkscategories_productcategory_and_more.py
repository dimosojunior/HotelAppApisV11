# Generated by Django 4.1.3 on 2023-10-07 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteldrinkscategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='hotelfoodcategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='restaurantdrinkscategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='restaurantfoodcategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='retailsdrinkscategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='retailsfoodcategories',
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='roomsclasses',
            name='ProductCategory',
        ),
    ]