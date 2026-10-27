# T07 - Fichas KPI C7:E11

Fecha: 2026-10-27

## Alcance ejecutado

Se completó únicamente `Fichas KPI!C7:E11` del XLSX de seguimiento. No se modificaron A7:B11, las columnas F-AA, las otras hojas, el PPTX, el PDF, las referencias, los Silver, la spec, el plan ni las decisiones. No se inició T08.

## Archivo y huellas

| Momento | Tamaño | SHA-256 |
| --- | ---: | --- |
| Antes de T07 | 34.402 bytes | `D677C305BBD4C1AFA4B2A912E849DC822E78E3F90EE8AF96C1334AACB141BB5F` |
| Después de T07 | 34.584 bytes | `C2F691F4CD5EDD47AD5E900A593740A9CD5EC11A197B5D5703DF9963E0C7D0D4` |

La diferencia corresponde a los 15 valores escritos y a la reserialización del paquete. Solo cambiaron valores en `Fichas KPI!C7:E11`; no hubo cambios de estilos ni de fórmulas.

## Valores escritos

| Fila | KPI | Nivel | Fórmula en palabras | Unidad |
| ---: | --- | --- | --- | --- |
| 7 | % de viajes con desviación | Táctico | Viajes con al menos una lectura marcada dividido entre viajes observados, multiplicado por 100. | Porcentaje |
| 8 | % de lecturas con desviación | Táctico | Lecturas marcadas dividido entre lecturas observadas, multiplicado por 100. | Porcentaje |
| 9 | Merma por cantidades | Táctico | Suma de cantidad_merma dividida entre suma de cantidad_ingreso, multiplicada por 100. | Porcentaje |
| 10 | % de lotes salidos vencidos | Táctico | Lotes con salida posterior al día de vencimiento divididos entre lotes salidos, multiplicado por 100. | Porcentaje |
| 11 | Días promedio en almacén | Táctico | Promedio de dias_en_almacen de los lotes con salida. | Días |

La redacción de D sigue los bullets aprobados por el usuario; el Anexo B confirma la semántica y las unidades. Se conservó el identificador exacto `dias_en_almacen`, sin tilde. No se añadieron metas, umbrales, DAX, responsables, referencias globales, merma por valor ni la medida de apoyo de lotes vencidos.

## Controles ejecutados

- **25/25 controles pasan** en `validation/results/S02/xlsx_invariants.json` y `validation/results/S02/kpi_checks.json`.
- Se conservaron 12 hojas en orden, 50 fórmulas, 11 validaciones de datos, 1 rango de formato condicional con 4 reglas y 19 celdas combinadas.
- `S01 Inventario` y `S02 Mapa Silver` son idénticas al cierre T06.
- A7:B11, las columnas F-AA y el resto de `Fichas KPI` no cambiaron en valores, estilos ni metadatos.
- Los estilos de `C7:E11` se conservaron sin diferencias.
- El libro reabre con `openpyxl`; ZIP y CRC son válidos; las partes requeridas están presentes.
- SRC-201 conserva `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30`; el PPTX conserva `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D`; no existe PDF.

## Limitaciones y pendientes

- No se usó Excel COM ni se realizó revisión visual; la inspección visual del libro corresponde a T09.
- No se ejecutaron recálculo, pruebas en Power BI Desktop, DAX, RLS, validación empresarial ni publicación.
- T08 no se inició.

Evidencia de soporte: `validation/results/S02/kpi_checks.json`, `validation/results/S02/xlsx_invariants.json`, `work/S02/t07_pre_state.json` y `work/S02/t07_post_state.json`.
