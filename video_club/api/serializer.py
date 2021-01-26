from rest_framework import serializers
from .models import Cinta, Cliente, Sucursal, Prestamo

class CintaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinta
        fields = ('id', 'titulo', 'valor', 'disponible')

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombres', 'apellidos', 'direccion')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id','nombre','ciudad','direccion')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields =('id', 'codigo_cliente', 'codigo_cinta', 'codigo_sucursal',
        'fecha_prestamo', 'fecha_entrega')

class VentasDiariasSerializer(serializers.Serializer):
    codigo_sucursal = serializers.Field(source='codigo_sucursal')
    cintas_alquiladas = serializers.Field(source='total')
    #clientId = serializers.Field()