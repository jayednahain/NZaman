from django.urls import path,include
from .views import *


urlpatterns = [

    path('login',log_in_page,name='login_page'),
    path('welcome',test_welcome,name='test'),
    path('Reg',user_registation,name='registation_link')

]