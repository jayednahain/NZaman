from django.contrib import admin
from .models import customer

# Register your models here.
#admin.site.register(customer)


@admin.register(customer)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','customer_name','phone_number','address','craeted_date','active_status']

