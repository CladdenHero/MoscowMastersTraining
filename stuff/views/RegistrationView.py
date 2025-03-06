from django.contrib.auth.models import User
from django.shortcuts import render
from django import views
from ..forms import SignUpForm


class RegistrationView(views.View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'stuff/registration.html', locals())

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            pw1 = form.cleaned_data['password1']
            # print(form.cleaned_data['password2'])
            user = User.objects.create_user(login, email, pw1)
        return  render(request, 'stuff/registration.html', locals())
