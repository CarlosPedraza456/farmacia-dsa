from django import forms
from .models import Product,Proveedor

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # O puedes especificar los campos que deseas mostrar

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'  # O puedes especificar los campos que deseas mostrar

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price_ref','available', 'category','cantidad','iva','lote']

class EditProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name','cedula','phone_number', 'email']