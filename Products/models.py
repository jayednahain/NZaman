from django.db import models
from django.contrib.auth.models import User
from Vendor_Company.media_path_converter import upload_image_path



class Product_Unit(models.Model):
   title = models.CharField(max_length=50)
   short_name = models.CharField(max_length=50)
   def __str__(self):
      return self.title


class Product_Category(models.Model):
   category = models.CharField(max_length=50)

   def __str__(self):
      return self.category

class Product(models.Model):
   title          =  models.CharField(max_length=100)
   detail         = models.TextField(max_length=100)
   creator        = models.ForeignKey(User,on_delete=models.CASCADE)
   category       = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
   unit           = models.ForeignKey(Product_Unit,on_delete=models.CASCADE)
   product_photo  = models.ImageField(upload_to=upload_image_path,null=True)
   upload_date    = models.DateField(auto_now_add=True)
