from django.contrib import admin
from .models import Product_Unit
from .models import Product
from .models import Product_Category

# Register your models here.


admin.site.register(Product_Unit)
admin.site.register(Product)
admin.site.register(Product_Category)