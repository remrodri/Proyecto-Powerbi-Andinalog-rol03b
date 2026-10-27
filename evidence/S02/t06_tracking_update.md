# T06 — Actualización de `S02 Mapa Silver`

Fecha de Build: 2026-10-27. Alcance autorizado: T06. No se inició T07.

## Archivo actualizado

| Momento | Tamaño | SHA-256 |
|---|---:|---|
| Antes | 33.844 bytes | `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1` |
| Después | 34.402 bytes | `D677C305BBD4C1AFA4B2A912E849DC822E78E3F90EE8AF96C1334AACB141BB5F` |

Archivo: `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`.

La diferencia de tamaño y SHA es compatible con los valores escritos y la reserialización de `openpyxl`; no se identificaron cambios no autorizados de valores, estilos materiales o metadatos.

## Celdas modificadas

| Celda | Valor final |
|---|---|
| `S02 Mapa Silver!B4` | `Grupo 06` |
| `S02 Mapa Silver!D4` | `03B` |
| `S02 Mapa Silver!F4` | `2026-10-27` |
| `S02 Mapa Silver!A7:G11` | DATA-001 a DATA-005, en el orden aprobado |

`F4` se escribió como texto ISO `YYYY-MM-DD`, con formato `General`, igual que `S01 Inventario!F4` (`2026-10-20`) y coherente con la plantilla SRC-201, que no define un formato numérico de fecha para esa celda. No se convirtió a número de serie.

La fila gris de ejemplo de Acería Andina (`fact_ordenes_silver.csv`) fue sustituida por la primera fila de datos. `A7:G7` se normalizó al estilo de datos de `A8:G8`; no se cambiaron anchos, altos, áreas de impresión, saltos de página ni configuración de hoja. La escritura en `B4`, `D4` y `F4` hizo que `openpyxl` normalizara la alineación por omisión (`None` a `general`/`bottom`); fuente, relleno, borde y formato numérico permanecen iguales.

## Contenido del mapa

Se conservaron literalmente los cinco archivos, las claves, los estados «Por acordar», la distinción observación/actualización, el alcance histórico de Inventario y la ausencia de WMS:

- `andinalog_iot_telemetry_silver.csv`
- `andinalog_productos_silver.csv`
- `andinalog_flota_silver.csv`
- `andinalog_inventory_tracking_silver.csv`
- `andinalog_warehouse_costs_silver.csv`

Frecuencia de Inventario: `Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar`.

`A7:G11` contiene exactamente cinco filas y siete columnas; `A12:G22` permanece vacío. No aparecen WMS, `DATA-006`, `DATA-007` ni una sexta fuente.

## Invariantes verificados

- 12 hojas, mismo orden.
- 50 fórmulas, mismas coordenadas y expresiones: 18 en `Fichas KPI`, 16 en `S07 KPI` y 16 en `S11 Pruebas RLS`.
- 11 validaciones de datos y 1 rango de formato condicional con 4 reglas.
- 19 combinaciones de celdas, sin cambios.
- `S01 Inventario`: dimensiones, valores y estilos sin cambios.
- Hojas distintas de `S02`: valores, estilos y metadatos sin cambios.
- `S02 Mapa Silver`: dimensiones, combinaciones, DV, CF y configuración de hoja sin cambios.
- Paquete XLSX válido: 23 miembros, `testzip` sin errores, CRC correctos, XML parseables y reapertura con `openpyxl`.
- SRC-201 intacto: `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30`, 36.907 bytes.
- PPTX de S02 intacto: `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D`; no existe PDF.

## Resultados

- `validation/results/S02/xlsx_invariants.json`: 18/18 controles, estado `PASS`.
- `validation/results/S02/map_checks.json`: 14/14 controles, estado `PASS`.

No se utilizó Excel COM ni se ejecutó revisión visual. La validación visual del XLSX corresponde a T09.
