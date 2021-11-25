from django.contrib import admin
from Transaction_app.models import Transaction_Method,Purchase,Sale,Inventory

# Register your models here.
admin.site.register(Transaction_Method)



@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','product','vendor','quantity','price','total_amount','purchase_date']





@admin.register(Sale)
class PurchaseAdmin(admin.ModelAdmin):
   list_display = ['id','product','customer','quantity','price','total_amount','sale_date']


@admin.register(Inventory)
class PurchaseAdmin(admin.ModelAdmin):

   search_fields = ['product__title'] #passing data base fields look up perameter into the list!
   list_display = ['id','product','product_unit','purchase_quantity','sale_quantity','total_quantity_balance','updated_date','sale_date','purchase_date']

