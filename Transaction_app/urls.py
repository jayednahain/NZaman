from django.urls import path,include
from .views import *


urlpatterns = [
   path('pur_prodcut',purchase_data_view, name='pur_data_link'),
]