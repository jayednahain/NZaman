# Generated by Django 3.2.8 on 2021-11-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction_app', '0006_alter_sale_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]