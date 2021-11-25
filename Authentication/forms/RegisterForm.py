from django import forms



class RegsiterForm(forms.Form):
   frist_name = forms.CharField(
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

   #two password field valiedation


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


