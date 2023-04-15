from django.db import models

# Create your models here.

class Clientes (models.Model):
    nombre_cliente=models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    email= models.EmailField()
    telefono=models.CharField(max_length=14)

    def __str__(self):
        return self.nombre_cliente


class Articulos(models.Model):
    nombre_articulo=models.CharField(max_length=30)
    seccion= models.CharField(max_length=50, verbose_name="Sección del producto")
    precio= models.IntegerField()


class Pedidos (models.Model):
    numero_pedido= models.IntegerField
    fecha= models.DateField()
    entregado= models.BooleanField()
