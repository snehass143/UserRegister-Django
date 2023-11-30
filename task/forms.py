from django import forms
from .models import RegisteredUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ['full_name', 'email', 'gender', 'phone_number', 'photo', 'username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
