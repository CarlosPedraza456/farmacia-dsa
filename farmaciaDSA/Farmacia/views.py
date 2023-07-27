from django.shortcuts import render
from django.http import HttpRequest

from Farmacia.forms import ClienteFormulario
from Farmacia.forms import ProductoFormulario
from Farmacia.models import clientes
from Farmacia.models import product
from Farmacia.models import Egreso
from Farmacia.models import ProductosEgreso


# Create your views here.

def homePage(request):
    return render(request, 'home.html', {})

""" gestion de clientes """

def clientess(request):
     clients = clientes.objects.all()
     return render(request, 'clientes/clientes.html',{"clientes": clients})

def registroClientes(request):
     cliente = ClienteFormulario()
     return render(request, "clientes/registroClientes.html", {"form":cliente})

def procesarCliente(request):
     cliente = ClienteFormulario(request.POST)
     if cliente.is_valid():
          cliente.save()
          cliente = ClienteFormulario()

     return render(request, "clientes/registroClientes.html", {"form":cliente, "mensaje": 'Ok'})

def editarClientes(request, id_cliente):
     cliente = clientes.objects.filter(id=id_cliente).first()
     form = ClienteFormulario(instance=cliente)
     return render(request, "clientes/editClientes.html", {"form": form,'cliente': cliente})

def actualizarCliente(request, id_cliente):
     cliente = clientes.objects.get(pk=id_cliente)
     form = ClienteFormulario(request.POST, instance=cliente)
     if form.is_valid():
          form.save()
     clientess = clientes.objects.all()
     return render(request,'clientes/clientes.html', {"clientes": clientess, "mensaje": 'Ok'} )

def eliminarCliente(request, id_cliente):
     cliente = clientes.objects.get(pk=id_cliente)
     cliente.delete()
     clientess = clientes.objects.all()
     return render(request, "clientes/clientes.html", {"clientes": clientess, "mensaje": 'Ok'})

""" gestion de productos """

def productos(request):
     products = product.objects.all()
     return render(request, 'producto/productos.html', {"productos": products})

def registroProductos(request):
     producto_agregar = ProductoFormulario()
     return render(request, "producto/registroProductos.html", {"form":producto_agregar})

def procesarProducto(request):
     producto_procesar = ProductoFormulario(request.POST)
     if producto_procesar.is_valid():
          producto_procesar.save()
          producto_procesar = ProductoFormulario()
     
     return render(request, "producto/registroProductos.html", {"form": producto_procesar, "mensaje": 'Ok'})

def editarProducto(request, id_producto):
     producto_editar = product.objects.filter(id=id_producto).first()
     form = ProductoFormulario(instance=producto_editar)
     return render(request, "producto/editProductos.html", {"form": form, 'producto': producto_editar})

def actualizarProducto(request, id_producto):
     producto_actualizado = product.objects.get(pk=id_producto)
     form = ProductoFormulario(request.POST, instance=producto_actualizado)
     if form.is_valid():
          form.save()
     productos = product.objects.all()
     return render(request, "producto/productos.html", {"productos": productos, "mensaje": 'Ok'})

def eliminarProducto(request, id_producto):
     producto = product.objects.get(pk=id_producto)
     producto.delete()
     productos = product.objects.all()
     return render(request, "producto/productos.html", {"productos": productos, "mensaje": 'Ok'})

""" ventas """

def ventas(request):
     products = product.objects.all()
     clients = clientes.objects.all()
     return render(request, 'ventas/ventas.html', {"productos": products,"clientes":clients})