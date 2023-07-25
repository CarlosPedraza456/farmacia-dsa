from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('clientes/', views.clientess, name='clientes'),
    path('registroCliente/', views.registroClientes, name='registroCliente'),
    path('guardarCliente/', views.procesarCliente, name='guardarCliente'),
    path('editarCliente/<int:id_cliente>', views.editarClientes, name='editarCliente'),
    path('actualizarCliente/<int:id_cliente>', views.actualizarCliente, name='actualizarCliente'),
    path('eliminarCliente/<int:id_cliente>', views.eliminarCliente, name='eliminarCliente'),
]