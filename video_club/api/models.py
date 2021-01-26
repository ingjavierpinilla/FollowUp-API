from django.db import models

# Create your models here.

class Cinta(models.Model):
    titulo = models.CharField(max_length = 60, null = False)
    valor = models.FloatField(default = 0.0)
    disponible = models.BooleanField(default=True)
class Cliente(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    telefono = models.IntegerField(null=True)
class Sucursal(models.Model):
    ciudad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
class Prestamo(models.Model):
    codigo_cliente = models.IntegerField(null = False)
    codigo_cinta = models.IntegerField(null = False)
    codigo_sucursal = models.IntegerField(null = False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True)