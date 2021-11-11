from django.contrib import admin
from Transaction_app.models import Transaction_Method,Purchase,Sale,Inventory

# Register your models here.
admin.site.register(Transaction_Method)
#admin.site.register(Purchase)
#admin.site.register(Sale)
#admin.site.register(Inventory)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','product','vendor','quantity','price','total_amount','purchase_date']



@admin.register(Inventory)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','product','purchase','sale','purchase_quantity','sale_quantity','total_quantity_balance','updated_date']


@admin.register(Sale)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','product','customer','quantity','price','total_amount','sale_date']
