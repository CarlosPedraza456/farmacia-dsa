from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField(primary_key=True)
    price_ref = models.FloatField()#precio en dolares
    available = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    lote = models.IntegerField()



    
    
