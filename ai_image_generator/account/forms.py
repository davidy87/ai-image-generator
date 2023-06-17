from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")

    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError("Username is not unique")
        
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")

    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email is not unique")
        
    #     return email