from django.db import models

class divisions(models.Model):
   div_name = models.CharField(max_length=50)