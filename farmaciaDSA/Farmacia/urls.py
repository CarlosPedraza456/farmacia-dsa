from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/registro/', views.registro, name='registro'),
]