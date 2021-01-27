from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SucursalList, DisponiblesList, VentaDiario, TopVentas, Landing

urlpatterns = [
    path('', Landing),
    path('disponible/', DisponiblesList.as_view()),
    path('venta-diaria/', VentaDiario.as_view()),
    path('sucursal/', SucursalList.as_view()),
    path('top-ventas/', TopVentas.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)