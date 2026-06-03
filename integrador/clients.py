import requests
from django.conf import settings

class SpringBootClient:
    @staticmethod
    def enviar_a_stock(payload):
        url = f"{settings.MS_STOCK_URL}/api/v1/stock"
        try:
            response = requests.post(url, json=payload, timeout=5)
            #retorna si el backend responde con exito
            return response.status_code in [200, 201]
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con MS Stock: {e}")
            return False
        
    @staticmethod
    def enviar_a_ventas(payload):
        url = f"{settings.MS_VENTAS_URL}/api/v1/ventas"
        try:
            response = requests.post(url, json=payload, timeout=5)
            return response.status_code in [200, 201]
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con MS Ventas: {e}")
            return False