from django.db import models
from django.utils import timezone

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=25)
    product_id = models.CharField(max_length=25)
    product_price = models.IntegerField()
    product_lot = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    fecha = models.DateField(default=timezone.now)


    def __str__(self):
        return f'Venta de {self.producto} - {self.fecha}'

