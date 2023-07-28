from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Proveedor
from .forms import ProductForm, EditProductForm, ProveedorForm, EditProveedorForm

# Create your views here.

class Home(TemplateView):
    template_name="comun/home.html"

class Productos(ListView):
    model=Product
    template_name="producto/producto_list.html"

class AgregarProductoView(CreateView):
    model=Product
    form_class = ProductForm
    template_name="producto/producto_add.html"
    success_url = reverse_lazy('producto_list')

class EditarProductoView(UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'producto/producto_edit.html'  # Reemplaza con el nombre de tu template
    success_url = reverse_lazy('producto_list')  # Reemplaza con la URL a la que deseas redirigir después de editar un producto

class DeleteProductoView(DeleteView):
    model = Product
    success_url = reverse_lazy('producto_list')  # URL a la que se redirigirá después de eliminar el producto
    template_name = 'producto/producto_delete.html'  # Nombre de tu plantilla de confirmación de eliminación
class Proveedores(ListView):
    model=Proveedor
    template_name="proveedor/proveedor_list.html"

class AgregarProveedorView(CreateView):
    model=Proveedor
    form_class=ProveedorForm
    template_name="proveedor/proveedor_add.html"
    success_url = reverse_lazy('proveedor_list')

class EditarProveedorView(UpdateView):
    model = Proveedor
    form_class = EditProveedorForm
    template_name = 'proveedor/proveedor_edit.html'  # Reemplaza con el nombre de tu template
    success_url = reverse_lazy('proveedor_list')  # Reemplaza con la URL a la que deseas redirigir después de editar un producto

class DeleteProveedorView(DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_list')  # URL a la que se redirigirá después de eliminar el producto
    template_name = 'proveedor/proveedor_delete.html'  # Nombre de tu plantilla de confirmación de eliminación