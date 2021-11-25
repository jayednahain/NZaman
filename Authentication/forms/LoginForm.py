from django import forms



class LoginForm(forms.Form):
   username = forms.CharField(
      label= "",
      widget=forms.TextInput(
         attrs={
            'class': 'form-control form-control-lg mt-5',
            'placeholder' : 'Enter User name'
         },
      )
   )

   password = forms.CharField(
      label="",
      widget=forms.PasswordInput(
         attrs={
            'class': 'form-control form-control-lg mt-3',
             'placeholder': 'Enter Passowrd'
         },
      )
   )
