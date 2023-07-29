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
    
    
    path('proveedores/', views.proveedoress ,name='proveedores'),
    path('registroProveedor/', views.registroProveedores, name='registroProveedor'),
    path('guardarProveedor/', views.procesarProveedor, name='guardarProveedor'),
    path('editarProveedor/<int:id_Proveedor>', views.editarProveedor, name='editarProveedor'),
    path('actualizarProveedor/<int:id_Proveedor>', views.actualizarProveedor, name='actualizarProveedor'),
    path('eliminarProveedor/<int:id_Proveedor>', views.eliminarProveedor, name='eliminarProveedor'),


    path('ventas/', views.ventas, name='ventas'),
    path('lista_ventas/', views.lista_ventas, name='lista_ventas'),
    path('guardarVenta/', views.procesarVenta, name ='guardarVenta')



]