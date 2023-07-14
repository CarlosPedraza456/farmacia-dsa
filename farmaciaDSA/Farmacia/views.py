from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm, EditProductForm

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

class EditarProductoView(UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'producto/editarProducto.html'  # Reemplaza con el nombre de tu template
    success_url = reverse_lazy('productos')  # Reemplaza con la URL a la que deseas redirigir después de editar un producto

class DeleteProductoView(DeleteView):
    model = Product
    success_url = reverse_lazy('productos')  # URL a la que se redirigirá después de eliminar el producto
    template_name = 'producto/producto_delete.html'  # Nombre de tu plantilla de confirmación de eliminación
class Proveedores(TemplateView):
    template_name="proveedores.html"

class AgregarProveedor(TemplateView):
    template_name="agregarProveedor.html"