# Generated by Django 3.2.8 on 2021-11-11 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction_app', '0011_rename_total_balance_inventory_total_quantity_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Transaction_app.purchase'),
        ),
    ]
