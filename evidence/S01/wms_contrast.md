# S01 · Contraste WMS (T02)

## Estado

- Fecha: 2026-10-20.
- Alcance ejecutado: T02 únicamente.
- Resultado: WMS 30.000×16; cobertura de telemetría 8.000 de 8.000; 22.000 órdenes WMS sin telemetría; cruces conformes.
- Límite: WMS se usó solo como contraste; no se importó en Power BI ni se incorporó al inventario oficial.

## Método

- DATA-007: `andinalog_wms_orders_silver.csv`.
- Cruces en memoria con `csv`; ninguna tabla se cargó en Power BI.
- Claves: `order_id` para WMS y telemetría; `camion_id` para flota; `lote_id` para inventario; `chofer_id` + mes de `fecha_despacho` para `andinalog_hr_drivers_silver.csv`; `cliente_id` para `andinalog_clientes_silver.csv`.
- El mes se deriva de `fecha_despacho[:7]` y de `periodo_mes[:7]`.
- El centro base se compara para las 8.000 órdenes WMS con telemetría, usando el `camion_id` de la lectura.
- No se modificaron DATA-001, DATA-003, DATA-004, DATA-007, `andinalog_hr_drivers_silver.csv` ni `andinalog_clientes_silver.csv`.

## Cobertura

| Control | Resultado | Esperado P02 | Estado |
| --- | --- | ---: | --- |
| Filas y columnas WMS | 30.000 × 16 | 30.000 × 16 | Conforme |
| Órdenes WMS únicas | 30.000 | 30.000 | Conforme |
| Órdenes con telemetría | 8.000 | 8.000 | Conforme |
| Cobertura de órdenes de telemetría | 8.000 de 8.000 | 8.000 de 8.000 | Conforme |
| Órdenes WMS sin telemetría | 22.000 | 22.000 | Conforme |

Las 8.000 órdenes de telemetría están contenidas en las 30.000 órdenes WMS. Las 22.000 restantes no tienen lectura térmica y quedan fuera de los cruces de temperatura.

## Cruces WMS

| Cruce | Coincidencias | Esperado | Sin referencia | Discrepancias |
| --- | ---: | ---: | ---: | ---: |
| Centro WMS vs. centro base del camión, órdenes con telemetría | 8.000 | 8.000 | 0 | 0 |
| Centro del lote WMS vs. centro del inventario | 30.000 | 30.000 | 0 | 0 |
| Centro del chofer-mes vs. centro WMS | 30.000 | 30.000 | 0 | 0 |
| Zona del cliente vs. centro WMS | 30.000 | 30.000 | 0 | 0 |

No hubo conflictos de `camion_id` por `order_id` en telemetría. Los cruces usan fuentes auxiliares (`andinalog_hr_drivers_silver.csv`, 7.200×8; `andinalog_clientes_silver.csv`, 400×4) sin importarlas al modelo.

## Particiones y límites térmicos

| Control | Resultado | Esperado P02/spec |
| --- | ---: | ---: |
| Órdenes con lecturas en dos particiones | 14 | 14 |
| Lecturas de esas órdenes | 339 | 339 |
| Lecturas positivas de esas órdenes | 43 | 43 |
| Viajes con lecturas en dos particiones | 14 | 14 |
| Lecturas de esos viajes | 339 | 339 |
| Lecturas positivas de esos viajes | 43 | 43 |
| Lecturas en límites térmicos | 26 | 26 |
| Porcentaje de lecturas en límites | 0,0136 % | 0,0136 % |
| Viajes con lecturas en límites | 26 | 26 |
| Viajes que dependen solo de lecturas límite | 0 | 0 |

Las 26 lecturas límite se distribuyen así:

| Temperatura requerida | Tolerancia | Temperatura de cabina | Lecturas |
| ---: | ---: | ---: | ---: |
| -18 °C | 3 °C | -15 °C | 19 |
| 4 °C | 2 °C | 6 °C | 7 |

La clasificación de límite se reconstruyó como lectura marcada con `desviacion_termica_flag=1` y diferencia absoluta respecto de la temperatura requerida menor o igual a la tolerancia del producto. Es una reproducción de control, no una nueva regla de negocio.

## Productos y referencias

- 70 productos distintos en telemetría; 70 productos refrigerados o congelados en el catálogo.
- 0 productos de telemetría fuera de las categorías refrigeradas/congeladas.
- 0 referencias de producto faltantes.

## Discrepancias y límites

- No se encontraron discrepancias materiales frente a los valores esperados de P02.
- La cobertura de 8.000 de 30.000 órdenes limita cualquier conclusión sobre el total WMS: 22.000 órdenes no tienen telemetría.
- El contraste no atribuye los cruces al CSV oficial ni demuestra causalidad, ahorro o rendimiento.
- No se ejecutó Power BI Desktop, no se importó WMS y no se inició T03.
