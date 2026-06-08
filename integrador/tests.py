from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import responses

class FullIntegrationServiceTests(TestCase):

    def setUp(self):
        self.url_prod = reverse('cargar-productos')
        self.url_stock = reverse('cargar-stock')
        self.url_sucursal = reverse('cargar-sucursales')
        self.url_venta = reverse('cargar-ventas')

    @responses.activate
    def test_flujo_completo_exitoso(self):
        # Mocks para todos los microservicios Spring Boot
        responses.add(responses.POST, "http://localhost:8082/api/productos", status=201)
        responses.add(responses.POST, "http://localhost:8085/api/stock", status=201)
        responses.add(responses.POST, "http://localhost:8084/api/sucursales", status=201)
        responses.add(responses.POST, "http://localhost:8081/api/ventas", status=201)

        # 1. Probar Productos
        r = self.client.post(self.url_prod, {"datos": [{"prod_sku": "A1", "prod_name": "P1", "retail_price": 100}]}, content_type='application/json')
        self.assertEqual(r.data["integrados_exitosamente"], 1)

        # 2. Probar Stock
        r = self.client.post(self.url_stock, {"datos": [{"cod_prod": 1, "tienda_id": 1, "disponibles": 5}]}, content_type='application/json')
        self.assertEqual(r.data["integrados_exitosamente"], 1)

        # 3. Probar Sucursales
        r = self.client.post(self.url_sucursal, {"datos": [{"branch_code": "S1", "branch_name": "Tienda Centro", "county": "Santiago"}]}, content_type='application/json')
        self.assertEqual(r.data["integrados_exitosamente"], 1)

        # 4. Probar Ventas
        r = self.client.post(self.url_venta, {"datos": [{"prod_id": 1, "shop_id": 1, "qty": 2, "total_amount": 5000}]}, content_type='application/json')
        self.assertEqual(r.data["integrados_exitosamente"], 1)

    def test_formatos_invalidos(self):
        response = self.client.post(self.url_prod, {"datos": "no_es_lista"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)