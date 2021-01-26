from rest_framework import serializers
from .models import Cinta, Cliente, Sucursal, Prestamo

class CintaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinta
        fields = ('id', 'titulo', 'valor', 'disponible')

class ClienteSerielizer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombres', 'apellidos', 'telefono')


class SucursalSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id','nombre','ciudad','direccion')

class PrestamoSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields =('id', 'codigo_cliente', 'codigo_cinta', 'codigo_sucursal',
        'fecha_prestamo', 'fecha_entrega')