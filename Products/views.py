from django.http import Http404
from django.shortcuts import render
from .models import Product
from Transaction_app.models import Inventory
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

   if stock_query:
      total_stock = stock_query.total_quantity_balance
      update_date = stock_query.updated_date

   else:
      stock = 0

   if query_set.exists() and query_set.count() == 1:
      instance = query_set.first()
   else:
      raise Http404("Custom ! error ! nO product Found")
   context ={
      'object':instance,
      'total_last_stock':int(total_stock),
      'update_date':update_date
   }
   return render(request, 'product_detail.html',context)

