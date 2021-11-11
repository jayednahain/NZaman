from django.db import models
from utilities.pdf_validator import pdf_validator
from employee_data.media_path_converter import upload_image_path,em_document_path

# Create your models here.



class Employee_designation(models.Model):
   designation_names = models.CharField(max_length=50)

class Blood_group(models.Model):
   blood_group = models.CharField(max_length=10)

class Employee(models.Model):
   name = models.CharField(max_length=50,null=True)
   phone_number = models.CharField(max_length=50,null=True)
   email = models.CharField(max_length=50,null=True)
   address = models.CharField(max_length=50,null=True)
   designation = models.ForeignKey(Employee_designation,on_delete=models.CASCADE,null=True)

   employee_profile_photo = models.ImageField(upload_to=upload_image_path,null=True)
   employee_special_document_photo = models.ImageField(upload_to=em_document_path,null=True)
   employee_cv = models.FileField(upload_to='Employee_CV/%Y/%m/%d',validators=[pdf_validator],null=True)

   blood_group = models.ForeignKey(Blood_group,on_delete=models.CASCADE,null=True)
   district = models.CharField(max_length=50,null=True)
   thana = models.CharField(max_length=50,null=True)
   division = models.CharField(max_length=50,null=True)
   post_office = models.CharField(max_length=50,null=True)


