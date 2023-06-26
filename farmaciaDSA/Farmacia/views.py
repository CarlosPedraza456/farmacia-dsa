from django.views.generic import TemplateView

# Create your views here.
class Productos(TemplateView):
    template_name="productos.html"

class Home(TemplateView):
    template_name="Home.html"

class AgregarProducto(TemplateView):
    template_name="agregarProducto.html"

class Proveedores(TemplateView):
    template_name="proveedores.html"

class AgregarProveedor(TemplateView):
    template_name="agregarProveedor.html"