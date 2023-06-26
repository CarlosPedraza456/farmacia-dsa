from django.shortcuts import render

# Create your views here.

def registro(request):
    return render(request, 'registroClientes.html', {})



def clientes(request):
    return render(request, 'clientes.html', {})



