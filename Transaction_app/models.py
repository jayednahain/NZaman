from django.db import models
from Products.models import Product
from Vendor_Company.models import Vendor

# Create your models here.
class Transaction_Method(models.Model):
   method_name = models.CharField(max_length=20)
   class Meta:
      verbose_name_plural="Transaction Method"

class Purchase(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
   quantity = models.FloatField()
   price = models.FloatField()
   total_amount = models.FloatField()
   purchase_date = models.DateField(auto_now_add=True)


   class Meta:
      verbose_name_plural="Purchase Data"
