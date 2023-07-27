from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField(primary_key=True)
    price_ref = models.FloatField()#precio en dolares
    available = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    lote = models.IntegerField()
    cantidad=models.IntegerField()
    iva=models.BooleanField()

    def get_absolute_url(self):
        return reverse("productos", kwargs={"pk": self.pk}) # entre llaves = diccionario python /post_detal ya que la app se llama post


class Proveedor(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    cedula= models.IntegerField()
    phone_number = models.FloatField()
    email = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse("proveedores", kwargs={"pk": self.pk}) # entre llaves = diccionario python /post_detal ya que la app se llama post




    
    
