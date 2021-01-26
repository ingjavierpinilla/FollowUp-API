from django.shortcuts import render
from rest_framework import generics, status
from .models import Cliente
from .serializer import ClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ClienteView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer