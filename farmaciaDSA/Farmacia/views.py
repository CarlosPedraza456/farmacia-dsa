from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

# Create your views here.

class Home(TemplateView):
    template_name="comun/home.html"

class Productos(ListView):
    model=Product
    template_name="producto/productos.html"


class AgregarProducto(CreateView):
    model=Product
    form_class = ProductForm
    template_name="producto/agregarProducto.html"
    success_url = reverse_lazy('productos')

class Proveedores(TemplateView):
    template_name="proveedores.html"

class AgregarProveedor(TemplateView):
    template_name="agregarProveedor.html"