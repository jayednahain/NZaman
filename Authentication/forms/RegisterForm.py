from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# User = get_user_model()


class RegsiterForm(forms.Form):
   first_name = forms.CharField(
      label= "",
      widget=forms.TextInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder' : 'Frist Name'
         },
      )
   )
   last_name = forms.CharField(
      label="",
      widget=forms.TextInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder': 'Last Name'
         },
      )
   )
   username = forms.CharField(
      label="",
      widget=forms.TextInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder': 'User name'
         },
      )
   )
   email = forms.EmailField(
      label="",
      widget=forms.EmailInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder': 'Email'
         },
      )
   )
   password = forms.CharField(
      label="",
      widget=forms.PasswordInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder': 'Type Password'
         },
      )
   )
   confirm_password = forms.CharField(
      label="",
      widget=forms.PasswordInput(
         attrs={
            'class': 'form-control form-control-lg mt-1',
            'placeholder': 'Confirm Password'
         },
      )
   )



   def clean_username(self):
      username = self.cleaned_data.get('username')
      query_data = User.objects.filter(username=username)
      if query_data.exists():
         raise forms.ValidationError("this user name already exists")

      return username

   def clean_email(self):
      email = self.cleaned_data.get('email')
      query_data = User.objects.filter(email=email)
      if query_data.exists():
         raise forms.ValidationError("this user name already exists")
      return email


   def clean_frist_name(self):
      frist_name = self.cleaned_data.get('frist_name')
      for i in range(len(frist_name)):
         if i == 0:
            if frist_name[i].islower()==True:
               raise forms.ValidationError("Please start with Capital letter")
               break
      return frist_name

   def clean_last_name(self):
      l_name = self.cleaned_data.get('last_name')
      for i in range(len(l_name)):
         if i == 0:
            if l_name[i].islower()==True:
               raise forms.ValidationError("Please start with Capital letter")
               break
      return l_name

   def clean(self):
      data = self.cleaned_data
      password_one = self.cleaned_data.get('password')
      password_two = self.cleaned_data.get('confirm_password')

      if password_one != password_two:
         raise forms.ValidationError("Both password must be same")
      return data


