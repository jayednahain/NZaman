from django.contrib import admin
from Transaction_app.models import Transaction_Method,Purchase

# Register your models here.
admin.site.register(Transaction_Method)
admin.site.register(Purchase)