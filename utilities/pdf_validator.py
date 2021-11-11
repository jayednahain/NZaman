from django.core.exceptions import ValidationError

def pdf_validator(value):
   import os

   ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
   valid_extensions = ['.pdf']
   if not ext.lower() in valid_extensions:
      raise ValidationError('Please upload file in pdf')