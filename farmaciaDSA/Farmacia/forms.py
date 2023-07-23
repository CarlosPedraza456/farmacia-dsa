from django import forms
from .models import clientes, product

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
        widgets = {'cliente_fecha': forms.DateInput(attrs={'type':'date'})}