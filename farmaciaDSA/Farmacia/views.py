from django.shortcuts import render

from Farmacia.forms import ClienteFormulario


# Create your views here.

def homePage(request):
    return render(request, 'home.html', {})

def registro(request):
        return render(request, 'clientes/registroClientes.html', {})


def clientes(request):
    return render(request, 'clientes/clientes.html',{})

    



