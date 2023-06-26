from django.contrib import admin

# Register your models here.

from Farmacia.models import product
from Farmacia.models import clientes

admin.site.register(product)
admin.site.register(clientes)