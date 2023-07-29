from django.shortcuts import render
from django.http import HttpRequest

from Farmacia.forms import ClienteFormulario
from Farmacia.forms import ProductoFormulario
from Farmacia.forms import ProveedorFormulario
from Farmacia.forms import ventaForm
from Farmacia.models import clientes
from Farmacia.models import product
from Farmacia.models import Proveedor
from Farmacia.models import venta
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
     
     return render(request, "producto/registroProductos.html", {"form":producto_procesar, "mensaje": 'Ok'})

def editarProducto(request, id_producto):
     producto_editar = product.objects.filter(id=id_producto).first()
     form = ProductoFormulario(instance=producto_editar)
     return render(request, "producto/editProductos.html", {"form": form, 'producto':producto_editar})

def actualizarProducto(request, id_producto):
     producto_actualizado = product.objects.get(pk=id_producto)
     form = ProductoFormulario(request.POST, instance=producto_actualizado)
     if form.is_valid():
          form.save()
     productos = product.objects.all()
     return render(request, "producto/productos.html", {"productos":productos, "mensaje": 'Ok'})

def eliminarProducto(request, id_producto):
     producto = product.objects.get(pk=id_producto)
     producto.delete()
     productos = product.objects.all()
     return render(request, "producto/productos.html", {"productos":productos, "mensaje": 'Ok'})

""" ventas """

def ventas(request):
     products = product.objects.all()
     clients = clientes.objects.all()
     venta_agregar = ventaForm()
     return render(request, 'ventas/ventas.html', {"productos": products,"clientes":clients})

def registrarVenta(request):
     venta_agregar = ventaForm()
     return render(request, "ventas/ventas.html", {"form":venta_agregar})


def procesarVenta(request):
     ventaProc = ventaForm(request.POST)
     products = product.objects.all()
     clients = clientes.objects.all()
     if ventaProc.is_valid():
          ventaProc.save()
          ventaProc = ventaForm()

     return render(request, "ventas/ventas.html", {"form": ventaProc, "mesaje": 'Ok', "productos":products, "clientes":clients})

def lista_ventas(request):
     vendass = venta.objects.all()
     return render(request, 'ventas/lista_ventas.html',{"ventas":vendass})

""""Proveedores"""

def proveedoress(request):
     providers = Proveedor.objects.all()
     return render(request, 'proveedores/proveedores_list.html', {"proveedores":providers})

def registroProveedores(request):
     proveedor_agregar = ProveedorFormulario()
     return render(request, "proveedores/proveedores_add.html", {"form":proveedor_agregar})

def procesarProveedor(request):
     proveedor_Procesar = ProveedorFormulario(request.POST)
     if proveedor_Procesar.is_valid():
          proveedor_Procesar.save()
          proveedor_Procesar = ProveedorFormulario()
     
     return render(request, "proveedores/proveedores_add.html", {"form":proveedor_Procesar, "mensaje": 'Ok'})

def editarProveedor(request, id_Proveedor):
     proveedor_Editar = Proveedor.objects.filter(id=id_Proveedor).first()
     form = ProveedorFormulario(instance=proveedor_Editar)
     return render(request, "proveedores/proveedores_edit.html", {"form": form, 'proveedor': proveedor_Editar})

def actualizarProveedor(request, id_Proveedor):
     proveedor_actualizado = Proveedor.objects.get(pk = id_Proveedor)
     form = ProveedorFormulario(request.POST, instance=proveedor_actualizado)
     if form.is_valid():
          form.save()
     proveedores = Proveedor.objects.all()
     return render(request, "proveedores/proveedores_list.html", {"proveedores": proveedores, "mensaje": 'Ok'})

def eliminarProveedor(request, id_Proveedor):
     proveedor = Proveedor.objects.get(pk=id_Proveedor)
     proveedor.delete()
     proveedores = product.objects.all()
     return render(request, "proveedores/proveedores_list.html", {"proveedor": proveedores, "mensaje": 'Ok'})