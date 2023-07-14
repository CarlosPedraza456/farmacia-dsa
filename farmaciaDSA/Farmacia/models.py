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

    def get_absolute_url(self):
        return reverse("productos", kwargs={"pk": self.pk}) # entre llaves = diccionario python /post_detal ya que la app se llama post




    
    
