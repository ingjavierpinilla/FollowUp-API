from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SucursalList, SucursalDetail, CintaList,  CintaDetail, Venta, Landing

urlpatterns = [
    path('', Landing),
    path('cinta/', CintaList.as_view()),
    path('cinta/<int:pk>', CintaDetail.as_view()),
    path('sucursal/', SucursalList.as_view()),
    path('sucursal/<int:pk>/', SucursalDetail.as_view()),
    path('venta/', Venta.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)