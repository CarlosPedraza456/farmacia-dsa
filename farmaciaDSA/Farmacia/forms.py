from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # O puedes especificar los campos que deseas mostrar

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price_ref','available', 'category', 'lote']