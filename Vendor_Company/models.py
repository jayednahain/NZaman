from django.db import models
from Vendor_Company.media_path_converter import upload_image_path

class Vendor(models.Model):
   vendor_name = models.CharField(max_length=100,null=True)
   country = models.CharField(max_length=50,null=True)
   address = models.CharField(max_length=100,null=True)
   phone_number = models.IntegerField(null=True)
   email = models.EmailField(max_length=20,null=True)
   vendor_photo = models.ImageField(upload_to=upload_image_path,null=True)
   running_status = models.BooleanField(null=True)



   def __str__(self):
      return self.vendor_name

