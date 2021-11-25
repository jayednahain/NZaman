# Generated by Django 3.2.8 on 2021-11-12 17:33

import Vendor_Company.media_path_converter
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('vendor_photo', models.ImageField(null=True, upload_to=Vendor_Company.media_path_converter.upload_image_path)),
                ('running_status', models.BooleanField(null=True)),
            ],
        ),
    ]
