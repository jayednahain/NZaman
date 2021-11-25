from django.shortcuts import render, redirect
from Authentication.forms.LoginForm import LoginForm
from Authentication.forms.RegisterForm import RegsiterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


def test_welcome(request):
   return render(request,'welcome_test.html')

def log_in_page(request):
   form = LoginForm(request.POST or None)
   contenxt = {
      'form': form
   }
   if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('test')
         print("you are logged in")
      else:
         print("Error")
      #reset the form
      contenxt['form']=LoginForm()
   return render(request,'login.html',contenxt)





def user_registation(request):
   form = RegsiterForm(request.POST or None)
   contenxt = {
      'form': form
   }
   if form.is_valid():
      print(form.cleaned_data)
      contenxt['form']=RegsiterForm()

   return render(request,'register.html',contenxt)
