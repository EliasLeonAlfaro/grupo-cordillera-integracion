import requests
from django.conf import settings

class SpringBootClient:
    """
    Cliente REST unificado que comunica la capa de integración de Django
    con los microservicios distribuidos de Spring Boot.
    """

    @staticmethod
    def enviar_a_productos(payload):
        url = f"{settings.MS_PRODUCTOS_URL}/api/productos"
        try:
            response = requests.post(url, json=payload, timeout=5)
            return response.status_code in [200, 201]
        except requests.exceptions.RequestException:
            return False

    @staticmethod
    def enviar_a_stock(payload):
        url = f"{settings.MS_STOCK_URL}/api/stock"
        try:
            response = requests.post(url, json=payload, timeout=5)
            return response.status_code in [200, 201]
        except requests.exceptions.RequestException:
            return False

    @staticmethod
    def enviar_a_sucursales(payload):
        url = f"{settings.MS_SUCURSALES_URL}/api/sucursales"
        try:
            response = requests.post(url, json=payload, timeout=5)
            return response.status_code in [200, 201]
        except requests.exceptions.RequestException:
            return False

    # ... Tus otros métodos como enviar_a_sucursales, enviar_a_productos, etc. ...

    @staticmethod
    def enviar_a_ventas(payload):
        try:
            # CORREGIDO: Añadimos '/datos' para que calce EXACTO con el .requestMatchers() de Java
            url = "http://localhost:8081/api/datos/ventas" 
            response = requests.post(url, json=payload)
            
            if response.status_code not in [200, 201]:
                print(f"❌ Error en ms-ventas: Código {response.status_code}")
                print(f"📋 Respuesta de Java: {response.text}")

            return response.status_code in [200, 201]
        except Exception as e:
            print(f"💥 Error de conexión con ms-ventas: {e}")
            return False