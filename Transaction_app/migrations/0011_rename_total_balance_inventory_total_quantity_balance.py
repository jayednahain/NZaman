# Generated by Django 3.2.8 on 2021-11-11 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction_app', '0010_alter_inventory_updated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='total_balance',
            new_name='total_quantity_balance',
        ),
    ]
