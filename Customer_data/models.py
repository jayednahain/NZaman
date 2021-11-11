from django.db import models

class divisions(models.Model):
   div_name = models.CharField(max_length=50)

class customer(models.Model):
   customer_name = models.CharField(max_length=50)
   phone_number = models.CharField(max_length=20)
   address = models.CharField(max_length=30)
   craeted_date = models.DateTimeField(auto_now_add=True)
   active_status = models.BooleanField(null=True)

   class Meta:
      verbose_name_plural="Customer Data"


   def __str__(self):
      return str(self.customer_name)


