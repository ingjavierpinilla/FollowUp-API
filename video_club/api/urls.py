from django.urls import path, include
from .views import ClienteView

urlpatterns = [
    path('cliente', ClienteView.as_view())
]