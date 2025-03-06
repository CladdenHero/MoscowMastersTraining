from django.urls import path
from . import views

app_name = 'stuff'

urlpatterns = [
    path('', views.index, name='index'),
    path('place', views.place, name='place'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
]
