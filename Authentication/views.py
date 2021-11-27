from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Authentication.forms.LoginForm import LoginForm
from Authentication.forms.RegisterForm import RegsiterForm
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.models import User
#class views
from django.views import generic

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




# User = get_user_model()
def user_registation(request):
   form = RegsiterForm(request.POST or None)
   contenxt = {
      'form': form
   }
   if form.is_valid():

      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')
      username = form.cleaned_data.get('username')

      new_user = User.objects.create_user(username, email, password)
      new_user.first_name = first_name
      new_user.last_name = last_name
      new_user.save()
      print(new_user)

      contenxt['form']=RegsiterForm()

      return redirect('login_page')

   return render(request,'register.html',contenxt)


# class User_Registretion_Form(generic.CreateView):
#    model = User
#    form_class = RegsiterForm
#    template_name = "register.html"
#    success_url = reverse_lazy('login_page')
