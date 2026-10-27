# S01 · Inventario y procedencia Bronze–Silver (T02)

## Estado

- Fecha: 2026-10-20.
- Alcance ejecutado: T02 únicamente.
- Resultado: P01, P02 y P06 conformes; 0 discrepancias materiales en la corrida final.
- Artefactos: [`s01_inventory.py`](../../validation/checks/s01_inventory.py), [`csv_checks.json`](../../validation/results/S01/csv_checks.json).
- Límite: no se abrió Power BI, no se importaron tablas, no se completó la plantilla y no se ejecutó T03.

## Método

- Comando: `python validation/checks/s01_inventory.py`.
- Lectura de solo lectura con `csv.DictReader`, codificación `utf-8-sig` y punto decimal.
- Conteo de filas y columnas, celdas vacías, claves, balance de inventario y procedencia DATA-006.
- P01: comparación de las 10 huellas SHA-256 con [`source_manifest.json`](../../validation/results/S01/source_manifest.json).
- No se modificaron CSV, referencias, plantillas ni datos Silver.

## Inventario de fuentes

| ID | Archivo | Rol | Filas | Columnas | Claves comprobadas | Resultado |
| --- | --- | --- | ---: | ---: | --- | --- |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | Oficial | 191.710 | 15 | `viaje_id` + `minutos_desde_despacho`; `viaje_id` + `timestamp` | Claves únicas, 0 vacías |
| DATA-002 | `andinalog_productos_silver.csv` | Oficial | 120 | 7 | `producto_id` | Clave única, 0 vacías |
| DATA-003 | `andinalog_flota_silver.csv` | Oficial | 100 | 6 | `camion_id` | Clave única, 0 vacías |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | Oficial | 7.782 | 12 | `lote_id`; `movimiento_id` | Claves únicas, 0 vacías |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | Oficial | 144 | 5 | `centro_distribucion` + `periodo_mes` | Clave única, 0 vacías |
| DATA-006 | `GIAD-M3_v10_auditoria_bronze_silver.csv` | Procedencia | 33 | 10 | No aplica | 5 registros oficiales localizados |
| DATA-007 | `andinalog_wms_orders_silver.csv` | Contraste | 30.000 | 16 | `order_id` | Clave única, 0 vacías |

Las filas y columnas de DATA-001 a DATA-005 coinciden con lo esperado en P02. Las siete fuentes no presentaron celdas vacías en los campos leídos. El detalle por campo y por clave está en `csv_checks.json`.

## Procedencia DATA-006

DATA-006 contiene 33 registros. Se transcriben los cinco registros de las fuentes oficiales de 03B:

| Bronze | Silver | Filas Bronze | Filas Silver | Duplicados Bronze | Duplicados Silver | Centinelas Bronze | Centinelas Silver | Conversiones F→C | Columnas Silver |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `andinalog_iot_telemetry.csv` | `andinalog_iot_telemetry_silver.csv` | 192.285 | 191.710 | 575 | 0 | 288 | 0 | 6.709 | 15 |
| `andinalog_productos.csv` | `andinalog_productos_silver.csv` | 121 | 120 | 1 | 0 | 0 | 0 | 0 | 7 |
| `andinalog_flota.csv` | `andinalog_flota_silver.csv` | 101 | 100 | 1 | 0 | 0 | 0 | 0 | 6 |
| `andinalog_inventory_tracking.csv` | `andinalog_inventory_tracking_silver.csv` | 7.805 | 7.782 | 23 | 0 | 11 | 0 | 0 | 12 |
| `andinalog_warehouse_costs.csv` | `andinalog_warehouse_costs_silver.csv` | 144 | 144 | 0 | 0 | 0 | 0 | 0 | 5 |

Los cinco `filas_silver` y `columnas_silver` coinciden exactamente con la lectura actual: 191.710×15, 120×7, 100×6, 7.782×12 y 144×5. Los cinco registros tienen `duplicados_silver=0` y `celdas_centinela_silver=0`; la telemetría documenta 6.709 conversiones Fahrenheit→Celsius.

DATA-006 también contiene el registro de WMS:

| Bronze | Silver | Filas Bronze | Filas Silver | Duplicados Bronze | Duplicados Silver | Centinelas Bronze | Centinelas Silver | Conversiones F→C | Columnas Silver |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `andinalog_wms_orders.csv` | `andinalog_wms_orders_silver.csv` | 30.090 | 30.000 | 90 | 0 | 0 | 0 | 0 | 16 |

Ese registro se conserva por su uso en el contraste, pero no se contabiliza como uno de los cinco oficiales. Así se evita presentar seis registros como si fueran los cinco exigidos por la spec.

## Observaciones de inventario

- 7.782 movimientos; 0 celdas vacías; 0 movimientos sin `fecha_salida`.
- 0 desbalances entre `cantidad_ingreso` y `cantidad_salida + cantidad_merma`.
- `lote_id` y `movimiento_id` son únicos, sin duplicados ni claves vacías.

## Controles

- P01: 10/10 huellas sin cambios.
- P02: conteos, claves, procedencia y observaciones conformes; 0 discrepancias en la corrida final.
- P06: contraste WMS calculado en memoria, sin cargar DATA-007 en Power BI.

La primera corrida marcó un falso fallo en `boundary_dependent_trips` porque comparó una lista vacía con `0`. Se corrigió la comparación a `len(...)` y se repitió el control; no cambió ningún dato ni resultado de las fuentes.

## Límites

- Este control no sustituye la inspección en Power BI Desktop, la copia de plantilla ni la auditoría de S01.
- No se corrigieron anomalías ni se imputaron valores.
- Los cruces WMS son cálculos propios de contraste y no se atribuyen al CSV oficial.
- El contraste WMS y sus límites están en [`wms_contrast.md`](wms_contrast.md).
