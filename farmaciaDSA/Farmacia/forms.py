from django import forms
from .models import clientes, product, Proveedor, venta

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'
        widgets = {'cliente_fecha': forms.DateInput(attrs={'type':'date'})}

class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'

class ProveedorFormulario(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'

class ventaForm(forms.ModelForm):

    class Meta:
        model = venta
        fields = '__all__'