from django.db import models
from Products.models import Product
from Vendor_Company.models import Vendor
from Customer_data.models import customer

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
   total_amount = models.FloatField(editable=False,default=0)
   purchase_date = models.DateTimeField(auto_now_add=True)

   class Meta:
      verbose_name_plural="Purchase Data"
   
   def save(self,*args,**kwargs):
      self.total_amount = self.quantity*self.price
      super(Purchase, self).save(*args,**kwargs)


      #sending data to inventory                   #the current product we are purchaseing
      inventory_last_row_obj = Inventory.objects.filter(product=self.product).order_by('-id').first()
      if inventory_last_row_obj:
         #update product quantity
         totalbalance = inventory_last_row_obj.total_quantity_balance+self.quantity
      else:
         totalbalance=self.quantity

      #save update data to data base
      Inventory.objects.create(
         product=self.product,
         purchase=self,
         sale = None,
         purchase_quantity=self.quantity,
         sale_quantity=None,
         total_quantity_balance=totalbalance,
         updated_date=self.purchase_date
      )



class Sale(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   customer = models.ForeignKey(customer, on_delete=models.CASCADE)
   quantity = models.FloatField()
   price = models.FloatField()
   total_amount = models.FloatField(editable=False,default=0)
   sale_date = models.DateTimeField(auto_now_add=True)
   class Meta:
      verbose_name_plural="Sale Data"

   def save(self, *args, **kwargs):
      self.total_amount = self.quantity * self.price
      super(Sale, self).save(*args, **kwargs)

      inventory_last_row_obj = Inventory.objects.filter(product=self.product).order_by('-id').first()
      if inventory_last_row_obj:
         # update product quantity
         totalbalance = inventory_last_row_obj.total_quantity_balance - self.quantity
      else:
         totalbalance = self.quantity

      # save update data to data base
      Inventory.objects.create(
         product=self.product,
         purchase=None,
         sale=self,
         purchase_quantity=None,
         sale_quantity=self.quantity,
         total_quantity_balance=totalbalance,
         updated_date=self.sale_date
      )





class Inventory(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   purchase =models.ForeignKey(Purchase, on_delete=models.CASCADE,null=True)
   sale = models.ForeignKey(Sale, on_delete=models.CASCADE,default=0,null=True)
   purchase_quantity = models.FloatField(default=0,null=True)
   sale_quantity = models.FloatField(default=0,null=True)
   total_quantity_balance = models.FloatField(default=0)
   updated_date = models.DateTimeField(null=True)





