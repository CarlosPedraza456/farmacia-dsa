from django.urls import path

from . import views

from django.urls import path
from Farmacia.views import informe_diario, informe_mensual, informe_anual

urlpatterns = [
    path('informe_diario/', informe_diario, name='informe_diario'),
    path('informe_mensual/', informe_mensual, name='informe_mensual'),
    path('informe_anual/', informe_anual, name='informe_anual')
]
