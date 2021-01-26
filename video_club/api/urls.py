from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClienteList, SucursalList

urlpatterns = [
    path('disponibles/', disponibles.as_view()),
    path('cliente/', ClienteList.as_view()),
    path('sucursal/', SucursalList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)