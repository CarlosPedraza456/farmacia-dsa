from django.urls import path
from .views import Productos, Home,AgregarProducto, Proveedores,AgregarProveedor, EditarProductoView, DeleteProductoView

urlpatterns = [
    path('Productos/', Productos.as_view(), name="productos"),
    path('Productos/agregar/', AgregarProducto.as_view(), name="agregarProductos"),
    path('productos/<int:pk>/editar/', EditarProductoView.as_view(), name='editarProducto'),
    path('productos/<int:pk>/eliminar/', DeleteProductoView.as_view(), name='producto_delete'),
    path('Proveedores/', Proveedores.as_view(), name="proveedores"),
    path('AgregarProveedor/', AgregarProveedor.as_view(), name="agregarProveedor"),
    path("", Home.as_view(), name="home"),
]
