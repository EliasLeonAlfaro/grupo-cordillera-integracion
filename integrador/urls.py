from django.urls import path
from .views import (
    CargaMasivaProductosAPIView, 
    CargaMasivaStockAPIView, 
    CargaMasivaSucursalesAPIView, 
    CargaMasivaVentasAPIView
)

urlpatterns = [
    path('cargar-productos/', CargaMasivaProductosAPIView.as_view(), name='cargar-productos'),
    path('cargar-stock/', CargaMasivaStockAPIView.as_view(), name='cargar-stock'),
    path('cargar-sucursales/', CargaMasivaSucursalesAPIView.as_view(), name='cargar-sucursales'),
    path('cargar-ventas/', CargaMasivaVentasAPIView.as_view(), name='cargar-ventas'),
]