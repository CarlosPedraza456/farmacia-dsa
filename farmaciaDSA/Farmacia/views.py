from django.shortcuts import render
from django.http import HttpRequest

from Farmacia.forms import ClienteFormulario
from Farmacia.models import clientes

# Create your views here.

def homePage(request):
    return render(request, 'home.html', {})

def registroClientes(request):
     cliente = ClienteFormulario()
     return render(request, "clientes/registroClientes.html", {"form":cliente})

def procesarCliente(request):
     cliente = ClienteFormulario(request.POST)
     if cliente.is_valid():
          cliente.save()
          cliente = ClienteFormulario()

     return render(request, "clientes/registroClientes.html", {"form":cliente, "mensaje": 'Ok'})


def clientess(request):
     clients = clientes.objects.all()
     return render(request, 'clientes/clientes.html',{"clientes": clients})

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
     return render(request,'clientes/clientes.html', {"clientes": clientess} )

def eliminarCliente(request, id_cliente):
     cliente = clientes.objects.get(pk=id_cliente)
     cliente.delete()
     clientess = clientes.objects.all()
     return render(request, "clientes/clientes.html", {"clientes": clientess, "mensaje": 'Ok'})
