from rest_framework import serializers
from .models import Cinta, Sucursal

class CintaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinta
        fields = ('id', 'titulo', 'valor', 'disponible')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id','nombre','ciudad','direccion')

