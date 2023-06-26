from django.shortcuts import render
from .models import product
from django.db.models import Sum
from datetime import datetime


def informe_diario(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        ventas = product.objects.filter(fecha=fecha)
        total_ventas = ventas.aggregate(total_ventas=Sum('total')).get('total_ventas')
        context = {
            'fecha': fecha,
            'ventas': ventas,
            'total_ventas': total_ventas,
        }
        return render(request, 'farmaciaDSA/Templates/informe_diario.html', context)
    else:
        return render(request, 'farmaciaDSA/Templates/informe_diario.html')

def informe_mensual(request):
    if request.method == 'POST':
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')
        ventas = product.objects.filter(fecha__month=mes, fecha__year=anio)
        total_ventas = ventas.aggregate(total_ventas=Sum('total')).get('total_ventas')
        context = {
            'mes': mes,
            'anio': anio,
            'ventas': ventas,
            'total_ventas': total_ventas,
        }
        return render(request, 'farmaciaDSA/Templates/informe_mensual.html', context)
    else:
        return render(request, 'farmaciaDSA/Templates/informe_mensual.html')

def informe_anual(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        ventas = product.objects.filter(fecha__year=anio)
        total_ventas = ventas.aggregate(total_ventas=Sum('total')).get('total_ventas')
        context = {
            'anio': anio,
            'ventas': ventas,
            'total_ventas': total_ventas,
        }
        return render(request, 'farmaciaDSA/Templates/informe_anual.html', context)
    else:
        current_year = datetime.now().year
        return render(request, 'farmaciaDSA/Templates/informe_anual.html', {'current_year': current_year})
