from django.urls import path
from .views import AgregarProducto

urlpatterns = [
    path('/agragarProducto', AgregarProducto.as_view(), name="agregarProducto"),
]
