# Generated by Django 3.2.8 on 2021-11-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction_app', '0005_alter_purchase_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
