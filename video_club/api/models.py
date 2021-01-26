from django.db import models

class Cinta(models.Model):
    titulo = models.CharField(max_length = 60, null = False)
    valor = models.FloatField(default = 0.0)
    disponible = models.BooleanField(default=True)
    def __str__(self):
        if self.disponible:
            return f'{self.id} {self.titulo}, disponible'
        else:
            return f'{self.id} {self.titulo}, no disponible'

class Cliente(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Sucursal(models.Model):
    nombre = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60, null=True, blank=True)
    def __str__(self):
        return f'{self.id} {self.nombre}'

class Prestamo(models.Model):
    codigo_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codigo_cinta = models.ForeignKey(Cinta,on_delete=models.CASCADE)
    codigo_sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'Prestamo cinta: {self.codigo_cinta}, S {self.codigo_sucursal}, F {self.fecha_prestamo}'