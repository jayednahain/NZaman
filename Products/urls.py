from django.urls import path,include
from .views import *


urlpatterns = [
    path('all',product_gallery,name='product_gallery_link'),
    path('detail/<int:pk>',product_detail,name = 'product_detail_link')

]