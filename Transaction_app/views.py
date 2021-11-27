from django.shortcuts import render
from .models import Sale,Purchase



def sale_data_view(request):
   all_sale_data = Sale.objects.all()
   context = {
      'all_sale_data':all_sale_data
   }
   return render(request,'all_sale_data.html',context)



def purchase_data_view(request):
   all_purchase_data = Purchase.objects.all()
   context = {
      'all_purchase_data':all_purchase_data
   }

   return render(request,'all_purchase_data.html',context)