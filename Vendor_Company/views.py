from django.shortcuts import render
from .models import Vendor


def vendor_list(request):
   data = Vendor.objects.all()

   context = {
      'all_data':data
   }

   return render(request,'venor_list.html',context)
