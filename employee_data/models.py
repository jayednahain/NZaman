from django.db import models
from employee_data.media_path_converter import upload_image_path,em_document_path

# Create your models here.

class Employee(models.Model):
   name = models.CharField(max_length=50)
   phone_number = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   address = models.CharField(max_length=50)

   em_profile_photo = models.ImageField(upload_to=upload_image_path)
   special_document_photo = models.ImageField(upload_to=em_document_path)

   blood_group = models.CharField(max_length=50)
   district = models.CharField(max_length=50)
   thana = models.CharField(max_length=50)
   division = models.CharField(max_length=50)
   post_office = models.CharField(max_length=50)


