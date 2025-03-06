from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class SignUpForm(forms.Form):
    login = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, help_text='test email')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput())


class Login(AuthenticationForm):
    username = forms.CharField(label='Имя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
