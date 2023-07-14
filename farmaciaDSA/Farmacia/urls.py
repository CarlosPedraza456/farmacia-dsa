from django.urls import path
from .views import Productos, Home,AgregarProducto, Proveedores,AgregarProveedor

urlpatterns = [
    path('Productos/', Productos.as_view(), name="productos"),
    path('Productos/agregarProductos/', AgregarProducto.as_view(), name="agregarProductos"),
    path('Proveedores/', Proveedores.as_view(), name="proveedores"),
    path('AgregarProveedor/', AgregarProveedor.as_view(), name="agregarProveedor"),
    path("", Home.as_view(), name="home"),
]
