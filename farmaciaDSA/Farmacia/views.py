from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AgregarProducto(TemplateView):
    template_name="agregarProducto.html"