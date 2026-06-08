from datetime import datetime
from .clients import SpringBootClient

class DataIntegrationService:

    @classmethod
    def procesar_carga_masiva_productos(cls, lista_datos_raw):
        registros_procesados = 0
        registros_fallidos = 0

        for item in lista_datos_raw:
            payload_estandarizado = {
                "sku": item.get("prod_sku"),
                "nombre": item.get("prod_name"),
                "descripcion": item.get("desc", ""),
                "precio": float(item.get("retail_price", 0.0)),
                "costo": float(item.get("wholesale_cost", 0.0)),
                "categoriaId": int(item.get("cat_id", 0)),
                "activo": True
            }

            # Regla de Integridad de Negocio
            if not payload_estandarizado["sku"] or not payload_estandarizado["nombre"] or payload_estandarizado["precio"] <= 0:
                registros_fallidos += 1
                continue

            if SpringBootClient.enviar_a_productos(payload_estandarizado):
                registros_procesados += 1
            else:
                registros_fallidos += 1

        return {"integrados_exitosamente": registros_procesados, "fallidos_o_rechazados": registros_fallidos}

    @classmethod
    def procesar_carga_masiva_stock(cls, lista_datos_raw):
        registros_procesados = 0
        registros_fallidos = 0

        for item in lista_datos_raw:
            payload_estandarizado = {
                "productoId": int(item.get("cod_prod", 0)),
                "sucursalId": int(item.get("tienda_id", 0)),
                "cantidadDisponible": int(item.get("disponibles", 0)),
                "cantidadReservada": int(item.get("reservados", 0))
            }

            if payload_estandarizado["productoId"] <= 0 or payload_estandarizado["cantidadDisponible"] < 0:
                registros_fallidos += 1
                continue

            if SpringBootClient.enviar_a_stock(payload_estandarizado):
                registros_procesados += 1
            else:
                registros_fallidos += 1

        return {"integrados_exitosamente": registros_procesados, "fallidos_o_rechazados": registros_fallidos}

    @classmethod
    def procesar_carga_masiva_sucursales(cls, lista_datos_raw):
        registros_procesados = 0
        registros_fallidos = 0

        for item in lista_datos_raw:
            payload_estandarizado = {
                "codigo": item.get("branch_code"),
                "nombre": item.get("branch_name"),
                "direccion": item.get("address", ""),
                "comuna": item.get("county"),
                "region": item.get("state"),
                "activa": True
            }

            # Validación basada en @NotBlank de tu clase Java Sucursal
            if not payload_estandarizado["codigo"] or not payload_estandarizado["nombre"] or not payload_estandarizado["comuna"]:
                registros_fallidos += 1
                continue

            if SpringBootClient.enviar_a_sucursales(payload_estandarizado):
                registros_procesados += 1
            else:
                registros_fallidos += 1

        return {"integrados_exitosamente": registros_procesados, "fallidos_o_rechazados": registros_fallidos}

    @classmethod
    def procesar_carga_masiva_ventas(cls, lista_datos_raw):
        registros_procesados = 0
        registros_fallidos = 0

        for item in lista_datos_raw:
            # CORREGIDO: Se cambia 'registro' por 'item' para evitar el error de variable indefinida
            # Sincronizado perfectamente con tu VentaModel de Java
            payload_estandarizado = {
                "productoId": int(item.get("prod_id", 0)),
                "sucursalId": int(item.get("shop_id", 0)),  
                "origen": str(item.get("source_type", "FISICO")),   
                "cantidad": int(item.get("qty", 0)),
                "montoTotal": float(item.get("total_amount", 0.0))
            }

            if payload_estandarizado["productoId"] <= 0 or payload_estandarizado["montoTotal"] <= 0 or payload_estandarizado["cantidad"] <= 0:
                registros_fallidos += 1
                continue

            if SpringBootClient.enviar_a_ventas(payload_estandarizado):
                registros_procesados += 1
            else:
                registros_fallidos += 1

        return {"integrados_exitosamente": registros_procesados, "fallidos_o_rechazados": registros_fallidos}