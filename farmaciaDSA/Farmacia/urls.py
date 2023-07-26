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


    path('productos/', views.productos, name='productos'),
    path('registroProducto/', views.registroProductos, name='registroProducto'),
    path('guardarProducto/', views.procesarProducto, name='guardarProducto'),
    path('editarProducto/<int:id_producto>', views.editarProducto, name='editarProducto'),
    path('actualizarProducto/<int:id_producto>', views.actualizarProducto, name='actualizarProducto'),
    path('eliminarProducto/<int:id_producto>', views.eliminarProducto, name='eliminarProducto'),
    
    



]