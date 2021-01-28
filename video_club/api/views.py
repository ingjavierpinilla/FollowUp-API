from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Sucursal, Prestamo, Cinta
from .serializer import  SucursalSerializer, CintaSerializer
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from django.utils.timezone import datetime

def Landing(request):
    return render(request, "base.html")

class CintaList(APIView):

    def get(self, request, format=None):
        disponible = request.GET.get('disponible')
        try:
            if disponible == 'True':
                cinta  = Cinta.objects.filter(disponible=True)
            else:
                cinta  = Cinta.objects.all()
            serializer = CintaSerializer(cinta, many=True)
            return Response(serializer.data)
        except:
            return Response({'Bad request.'}, status = status.HTTP_400_BAD_REQUEST)

class CintaDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            cinta = Cinta.objects.filter(id=pk)
            if not cinta:
                return Response({f'Cinta {pk} no encontrada'}, status = status.HTTP_204_NO_CONTENT)
            
            serializer = CintaSerializer(cinta, many=True)
            return Response(serializer.data)
        except:
            return Response({'ID invalido.'}, status = status.HTTP_400_BAD_REQUEST)

class SucursalList(APIView):

    def get(self, request, format=None):
        serializer = SucursalSerializer(Sucursal.objects.all(), many=True)
        return Response(serializer.data)

class SucursalDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            sucursal = Sucursal.objects.filter(id=pk)
            if not sucursal:
                return Response({f'Sucursal {pk} no encontrada'}, status = status.HTTP_204_NO_CONTENT)
            
            sucursal = Prestamo.objects.select_related('codigo_cinta').filter(codigo_sucursal=pk).annotate(mes=TruncMonth('fecha_prestamo')).values('mes').annotate(valor_venta=Sum('codigo_cinta__valor')).order_by('mes')
            return Response(sucursal)
        except:
            return Response({'ID invalido.'}, status = status.HTTP_400_BAD_REQUEST)

class Venta(APIView):
    """
    parametros de query:
        Todas las fechas en formato ISO 8601 sin incluir la hora, minutos y segundos
        i.e. 2010-12-16

        (?P<fecha>.+)/$
        o 
        (?P<de>.+)/$/(?P<hasta>.+)/$
    """
    def get(self, request, format=None):
        fecha = request.GET.get('fecha')
        if fecha is not None:
            try:
                prestamo = Prestamo.objects.select_related('codigo_cinta').filter(fecha_prestamo__date=fecha).values('codigo_sucursal').annotate(cintas_alquiladas=Count('codigo_sucursal'), valor_venta=Sum('codigo_cinta__valor')).order_by('codigo_sucursal')
            except:
                return Response({'Fecha no valida.'}, status = status.HTTP_400_BAD_REQUEST)

            if not prestamo:
                return Response({f'Sin informacion para la fecha requerida. {fecha}'}, status = status.HTTP_204_NO_CONTENT)

            return Response(prestamo, status=status.HTTP_200_OK)

        de = request.GET.get('de')
        hasta = request.GET.get('hasta')
        if de is not None and hasta is not None:
            try:
                if hasta < de:
                    raise NameError('HiThere')
                prestamo = Prestamo.objects.select_related('codigo_cinta','codigo_sucursal').filter(fecha_prestamo__range=[de, hasta]).values('codigo_sucursal','codigo_sucursal__nombre').annotate(valor_venta=Sum('codigo_cinta__valor')).order_by('-valor_venta')
                if prestamo:
                    return Response(prestamo[0], status=status.HTTP_200_OK)
                else:
                    return Response({f'Sin informacion para la fecha requerida. {de}-{hasta}'}, status = status.HTTP_204_NO_CONTENT)
            except NameError:
                return Response({'\'Hasta\' ocurre antes que \'de\''}, status = status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Fecha no valida.'}, status = status.HTTP_400_BAD_REQUEST)

        try:
            prestamo = Prestamo.objects.select_related('codigo_cinta').filter(fecha_prestamo__date=datetime.today()).values('codigo_sucursal').annotate(cintas_alquiladas=Count('codigo_sucursal'), valor_venta=Sum('codigo_cinta__valor')).order_by('codigo_sucursal')
            if prestamo:
                return Response(prestamo, status=status.HTTP_200_OK)
            else:
                return Response({f'Sin informacion para la fecha requerida. {datetime.today()}'}, status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({'Bad request.'}, status = status.HTTP_400_BAD_REQUEST)