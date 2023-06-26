from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=25)
    product_id = models.CharField(max_length=25)
    product_price = models.IntegerField()
    product_lot = models.IntegerField()

class clientes(models.Model):
    cliente_name = models.CharField(max_length=35)
    cliente_apellido = models.CharField(max_length=35)
    cliente_cedula = models.CharField(max_length=15)
    cliente_edad = models.IntegerField()
    cliente_fecha = models.DateField()
    