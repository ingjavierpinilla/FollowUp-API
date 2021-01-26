from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cliente, Sucursal, Prestamo
from .serializer import ClienteSerializer, SucursalSerializer
import datetime

class ClienteList(APIView):
    def get(self, request, format=None):
        cliente  = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

class SucursalList(APIView):

    def get(self, request, format=None):
        ids = request.GET.get('id')
        year = request.GET.get('year')
        if ids is not None:
            sucursal = Sucursal.objects.filter(id=ids)
            if not sucursal:
                return Response({'Sucursal no encontrada': 'ID invalido.'}, status = status.HTTP_404_NOT_FOUND)
            
            if year_validator(year):
                aux = Prestamo.objects.filter(codigo_sucursal=ids, fecha_prestamo__year=int(year)).select_related()
                print('***********************')
                print(aux)
            else:
                return Response({'Year no valido.'}, status = status.HTTP_404_NOT_FOUND)

        else:
            sucursal = Sucursal.objects.all()

        serializer = SucursalSerializer(sucursal, many=True)
        return Response(serializer.data)

def year_validator(value):
    value = int(value)
    if value < 1900 or value > datetime.datetime.now().year:
        return False
    return True