from django.http import Http404
from django.shortcuts import render
from .models import Product
from Transaction_app.models import Inventory,Sale,Purchase
# Create your tests here.


def product_gallery(request):
   query_set = Product.objects.all()
   context = {
      'all_product': query_set
   }
   return render(request,'product_gallary.html',context)





def product_detail(request,*args,**kwargs):
   query_set = Product.objects.filter(id = kwargs['pk'])
   stock_query = Inventory.objects.filter(product_id=kwargs['pk']).order_by('-id').first()
   last_purchase_rate = Purchase.objects.filter(product_id=kwargs['pk']).order_by('-id').first()
   last_sell_rate = Sale.objects.filter(product_id=kwargs['pk']).order_by('-id').first()


   if stock_query and last_purchase_rate and last_sell_rate:
      total_stock = stock_query.total_quantity_balance
      update_date = stock_query.updated_date

      last_pur_rate   = last_purchase_rate.price
      last_pur_rate_date = last_purchase_rate.purchase_date
      last_pur_vendor = last_purchase_rate.vendor


      last_sale_rate   = last_sell_rate.price
      last_sale_rate_date = last_sell_rate.sale_date
      last_sale_customer = last_sell_rate.customer

   else:

      total_stock = 0
      update_date ="No value"

      last_pur_rate = "No value"
      last_pur_rate_date = "No value"
      last_pur_vendor = "No value"

      last_sale_rate = "No value"
      last_sale_rate_date = "No value"
      last_sale_customer = "No value"

   if query_set.exists() and query_set.count() == 1:
      instance = query_set.first()
   else:
      raise Http404("Custom ! error ! nO product Found")
   context ={
      'object':instance,
      'total_last_stock':int(total_stock),
      'update_date':update_date,
      'last_pur_rate':last_pur_rate,
      'last_pur_rate_date':last_pur_rate_date,
      'last_sale_rate':last_sale_rate,
      'last_sale_rate_date':last_sale_rate_date,
      'last_pur_vendor':last_pur_vendor,
      'last_sale_customer':last_sale_customer
   }
   return render(request, 'product_detail.html',context)

