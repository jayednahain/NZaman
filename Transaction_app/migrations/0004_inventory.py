# Generated by Django 3.2.8 on 2021-11-11 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_product_product_photo'),
        ('Transaction_app', '0003_auto_20211111_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_quantity', models.FloatField(default=0)),
                ('sale_quantity', models.FloatField(default=0)),
                ('total_balance', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
                ('purchase', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Transaction_app.purchase')),
                ('sale', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Transaction_app.sale')),
            ],
        ),
    ]
