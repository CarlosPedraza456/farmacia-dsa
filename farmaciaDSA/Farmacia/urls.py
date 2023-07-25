from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('clientes/', views.clientess, name='clientes'),
    path('registroCliente/', views.registroClientes, name='registroCliente'),
    path('guardarCliente/', views.procesarCliente, name='guardarCliente')
]