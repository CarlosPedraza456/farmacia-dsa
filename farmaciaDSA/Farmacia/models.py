from django.db import models
from django.forms import model_to_dict

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField(primary_key=True)
    price_ref = models.FloatField()#precio en dolares
    available = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    lote = models.IntegerField()
    cantidad =  models.IntegerField()
    iva = models.BooleanField()

    def __str__(self):
        return self.name

class clientes(models.Model):
    cliente_name = models.CharField(max_length=35)
    cliente_apellido = models.CharField(max_length=35)
    cliente_telefono = models.CharField(max_length=35)
    cliente_correo = models.CharField(max_length=35)
    cliente_cedula = models.CharField(max_length=15)
    cliente_fecha = models.DateField()

    def __str__(self):
        return self.cliente_name

 
class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(clientes, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(product, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item   