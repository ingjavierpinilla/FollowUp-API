from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Sucursal, Prestamo, Cinta
from .serializer import  SucursalSerializer, CintaSerializer
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth

class DisponiblesList(APIView):
    def get(self, request, format=None):
        cinta  = Cinta.objects.filter(disponible=True)
        serializer = CintaSerializer(cinta, many=True)
        return Response(serializer.data)

class VentaDiario(APIView):
    """
    parametros de query:
        (?P<fecha>.+)/$: fecha en formato ISO 8601 sin incluir la hora, minutos y segundos
        i.e. 2010-12-16
    """
    def get(self, request, format=None):
        fecha = request.GET.get('fecha')
        prestamo = Prestamo.objects.select_related('codigo_cinta').filter(fecha_prestamo__date=fecha).values('codigo_sucursal').annotate(cintas_alquiladas=Count('codigo_sucursal'), valor_venta=Sum('codigo_cinta__valor')).order_by('cintas_alquiladas')
        if not prestamo:
            return Response({'Sin informacion para la fecha requerida.'}, status = status.HTTP_404_NOT_FOUND)

        return Response(prestamo)

class TopVentas(APIView):
    """
    parametros de query:
        (?P<de>.+)/$: fecha en formato ISO 8601 sin incluir la hora, minutos y segundos
        i.e. 2010-12-16
        (?P<hasta>.+)/$: igual al anterior
    """
    def get(self, request, format=None):
        de = request.GET.get('de')
        hasta = request.GET.get('hasta')
        prestamo = Prestamo.objects.select_related('codigo_cinta','codigo_sucursal').filter(fecha_prestamo__range=[de, hasta]).values('codigo_sucursal','codigo_sucursal__nombre').annotate(valor_venta=Sum('codigo_cinta__valor')).order_by('-valor_venta')[0]
        if not prestamo:
            return Response({'Sin informacion para la fecha requerida.'}, status = status.HTTP_404_NOT_FOUND)

        return Response(prestamo)

class SucursalList(APIView):
    """
    parametros de query:
        (?P<id>.+)/$
    """

    def get(self, request, format=None):
        id_ = request.GET.get('id')
        if id_ is not None:
            sucursal = Sucursal.objects.filter(id=id_)
            if not sucursal:
                return Response({'Sucursal no encontrada': 'ID invalido.'}, status = status.HTTP_404_NOT_FOUND)
            sucursal = Prestamo.objects.select_related('codigo_cinta').filter(codigo_sucursal=id_).annotate(mes=TruncMonth('fecha_prestamo')).values('mes').annotate(valor_venta=Sum('codigo_cinta__valor')).order_by('mes')
            return Response(sucursal)
        else:
            sucursal = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursal, many=True)
        return Response(serializer.data)

