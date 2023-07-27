from django.urls import path
from .views import Productos, Home,AgregarProductoView, EditarProductoView, DeleteProductoView
from .views import Proveedores,AgregarProveedorView,EditarProveedorView,DeleteProductoView
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('Productos/', Productos.as_view(), name="producto_list"),
    path('Productos/add/', AgregarProductoView.as_view(), name="producto_add"),
    path('productos/<int:pk>/edit/', EditarProductoView.as_view(), name='producto_edit'),
    path('productos/<int:pk>/delete/', DeleteProductoView.as_view(), name='producto_delete'),
    path('Proveedores/', Proveedores.as_view(), name="proveedor_list"),
    path('Proveedores/add/', AgregarProveedorView.as_view(), name="proveedor_add"),
    path('Proveedores/<int:pk>/edit/', EditarProveedorView.as_view(), name='proveedor_edit'),
    path('productos/<int:pk>/delete/', DeleteProductoView.as_view(), name='proveedor_delete'),
    
]
