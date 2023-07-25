from django.shortcuts import render
from django.http import HttpRequest

from Farmacia.forms import ClienteFormulario
from Farmacia.models import clientes

# Create your views here.

def homePage(request):
    return render(request, 'home.html', {})


class registrarClientes():
     def registroClientes(request):
          cliente = ClienteFormulario()
          return render(request, "clientes/registroClientes.html", {"form":cliente})
     def procesarCliente(request):
          cliente = ClienteFormulario(request.POST)
          if cliente.is_valid():
               cliente.save()
               cliente = ClienteFormulario()

          return render(request, "clientes/registroClientes.html", {"form":cliente, "mensaje:": 'Ok'})


def registroClientes(request):
     cliente = ClienteFormulario()
     return render(request, "clientes/registroClientes.html", {"form":cliente})

def procesarCliente(request):
     cliente = ClienteFormulario(request.POST)
     if cliente.is_valid():
          cliente.save()
          cliente = ClienteFormulario()

     return render(request, "clientes/registroClientes.html", {"form":cliente, "mensaje:": 'Ok'})


def clientess(request):
     clients = clientes.objects.all()
     return render(request, 'clientes/clientes.html',{"clientes": clients})

    



