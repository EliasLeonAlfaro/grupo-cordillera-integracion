from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .services import DataIntegrationService

class BaseCargaAPIView(APIView):
    permission_classes = [AllowAny]
    
    def verificar_datos(self, request):
        datos = request.data.get("datos", [])
        if not datos or not isinstance(datos, list):
            return None
        return datos

class CargaMasivaProductosAPIView(BaseCargaAPIView):
    def post(self, request, *args, **kwargs):
        datos = self.verificar_datos(request)
        if datos is None:
            return Response({"error": "Se requiere una lista bajo la clave 'datos'"}, status=status.HTTP_400_BAD_REQUEST)
        resultado = DataIntegrationService.procesar_carga_masiva_productos(datos)
        return Response(resultado, status=status.HTTP_200_OK)

class CargaMasivaStockAPIView(BaseCargaAPIView):
    def post(self, request, *args, **kwargs):
        datos = self.verificar_datos(request)
        if datos is None:
            return Response({"error": "Se requiere una lista bajo la clave 'datos'"}, status=status.HTTP_400_BAD_REQUEST)
        resultado = DataIntegrationService.procesar_carga_masiva_stock(datos)
        return Response(resultado, status=status.HTTP_200_OK)

class CargaMasivaSucursalesAPIView(BaseCargaAPIView):
    def post(self, request, *args, **kwargs):
        datos = self.verificar_datos(request)
        if datos is None:
            return Response({"error": "Se requiere una lista bajo la clave 'datos'"}, status=status.HTTP_400_BAD_REQUEST)
        resultado = DataIntegrationService.procesar_carga_masiva_sucursales(datos)
        return Response(resultado, status=status.HTTP_200_OK)

class CargaMasivaVentasAPIView(BaseCargaAPIView):
    def post(self, request, *args, **kwargs):
        datos = self.verificar_datos(request)
        if datos is None:
            return Response({"error": "Se requiere una lista bajo la clave 'datos'"}, status=status.HTTP_400_BAD_REQUEST)
        resultado = DataIntegrationService.procesar_carga_masiva_ventas(datos)
        return Response(resultado, status=status.HTTP_200_OK)