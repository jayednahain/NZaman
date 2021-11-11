# Generated by Django 3.2.8 on 2021-11-11 09:26

from django.db import migrations, models
import utilities.media_path_converter


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_photo',
            field=models.ImageField(null=True, upload_to=utilities.media_path_converter.upload_image_path),
        ),
    ]
