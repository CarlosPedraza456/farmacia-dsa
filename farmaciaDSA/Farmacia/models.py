from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField(primary_key=True)
    price_ref = models.FloatField()#precio en dolares
    available = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    lote = models.IntegerField()

class clientes(models.Model):
    cliente_name = models.CharField(max_length=35)
    cliente_apellido = models.CharField(max_length=35)
    cliente_telefono = models.CharField(max_length=35)
    cliente_correo = models.CharField(max_length=35)
    cliente_cedula = models.CharField(max_length=15)
    cliente_fecha = models.DateField()
    