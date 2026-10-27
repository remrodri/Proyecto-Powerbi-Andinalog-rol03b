# S01 · Mapa de celdas y verificación de T04

Fecha: 2026-10-20.
Alcance: T04 únicamente. Se copió la plantilla y se completaron identificación, inventario y los campos KPI/decisión de S01. No se abrió Power BI, no se ejecutó T05 y no se asignó componente DCAM.

## 1. Archivos

| Elemento | Ruta | SHA-256 | Tamaño |
| --- | --- | --- | ---: |
| Original intacto | `references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30` | 36.907 |
| Copia de trabajo | [`deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`](../../deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx) | `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1` | 33.844 |
| Revisión visual S01 | [`t04_s01_inventory.pdf`](t04_s01_inventory.pdf) | — | 152.776 |
| Revisión visual Fichas KPI | [`t04_fichas_kpi.pdf`](t04_fichas_kpi.pdf) | — | 224.515 |

La huella del original se comprobó antes y después: no cambió. La diferencia de tamaño de la copia se debe a la reserialización de `openpyxl`; no se usa como prueba de contenido. Las fórmulas y los valores se compararon celda a celda.

## 2. Identificación

| Hoja | Celda | Campo | Valor |
| --- | --- | --- | --- |
| S01 Inventario | B4 | Equipo | `Grupo 06` |
| S01 Inventario | D4 | Subcaso | `03B` |
| S01 Inventario | F4 | Fecha | `2026-10-20` (texto ISO) |
| Fichas KPI | B4 | Equipo | `Grupo 06` |
| Fichas KPI | D4 | Subcaso | `03B` |
| Fichas KPI | F4 | Fecha | `2026-10-20` (texto ISO) |

`Grupo 06` es el responsable de revisión ya registrado en `preparation.md`; no se inventaron personas ni responsables empresariales.

## 3. S01 Inventario

La fila 7 de ejemplo se reemplazó por DATA-001. Las filas 8–11 contienen DATA-002 a DATA-005. Las filas 12–22 no se editaron.

| Fila | ID | A · Tabla / archivo | B · Qué representa una fila | C · Columnas clave | D · Filas | E · Columnas | F · Brecha observada | G · Responsable |
| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- |
| 7 | DATA-001 | `andinalog_iot_telemetry_silver.csv` | Una lectura dentro de un viaje. | `viaje_id` + `minutos_desde_despacho`; también `viaje_id` + `timestamp`. | 191.710 | 15 | Excepción demostrada: 26 lecturas en límites térmicos; 14 órdenes o viajes con 339 lecturas en dos particiones y 43 positivas. Se registran y no se corrigen en S01. | Grupo 06 |
| 8 | DATA-002 | `andinalog_productos_silver.csv` | Un producto. | `producto_id`. | 120 | 7 | Sin brecha observada. Diferencia de cobertura: 70 de 120 productos aparecen en telemetría; no es error de calidad. | Grupo 06 |
| 9 | DATA-003 | `andinalog_flota_silver.csv` | Un camión. | `camion_id`. | 100 | 6 | Sin brecha observada. Diferencia de definición: el centro base no equivale necesariamente al centro operativo; decisión de modelado pendiente. | Grupo 06 |
| 10 | DATA-004 | `andinalog_inventory_tracking_silver.csv` | Un lote con ingreso, salida y merma. | `lote_id`; `movimiento_id`. | 7.782 | 12 | Sin brecha observada. Limitación de alcance: todos los lotes ya salieron; no hay stock vigente en esta entrega. | Grupo 06 |
| 11 | DATA-005 | `andinalog_warehouse_costs_silver.csv` | Un centro en un mes. | `centro_distribucion` + `periodo_mes`. | 144 | 5 | Sin brecha observada. Decisión de modelado: relación temporal con el calendario pendiente; no es error de calidad. | Grupo 06 |

Correspondencia: filas 7–11 de la hoja = filas DATA-001–DATA-005 de `preparation.md`, sección 3. Las columnas D y E conservan formato `#,##0`.

## 4. Fichas KPI

La fila 7 de ejemplo se reemplazó por el KPI 1. Las filas 8–11 contienen los KPI 2–5. Solo se completaron las columnas S01: A (KPI) y B (decisión que apoya). Los campos de S02–S11 quedaron vacíos.

| Fila | A · KPI | B · Decisión que apoya (pregunta) | Origen |
| ---: | --- | --- | --- |
| 7 | `% de viajes con desviación` | ¿Qué proporción de viajes tiene al menos una lectura marcada? Apoya la priorización de controles por producto y camión. | `preparation.md`, KPI 1 |
| 8 | `% de lecturas con desviación` | ¿Qué proporción de lecturas queda marcada? Apoya la lectura de intensidad aparente y la comparación entre productos o camiones. | `preparation.md`, KPI 2 |
| 9 | `Merma por cantidades` | ¿Cuánta cantidad se pierde? Apoya la revisión de lotes y centros con peor desempeño. | `preparation.md`, KPI 3 |
| 10 | `% de lotes salidos vencidos` | ¿Qué proporción de lotes sale vencida? Apoya la revisión de gestión de lotes y centros. | `preparation.md`, KPI 4 |
| 11 | `Días promedio en almacén` | ¿Cuánto permanece un lote antes de salir? Apoya la revisión de permanencia histórica por centro o producto. | `preparation.md`, KPI 5 |

Se limpiaron los valores de ejemplo de Acería Andina en C7:R7 y T7:Z7. Se conservaron las fórmulas S7 y AA7 y las de S8:S15 y AA8:AA15. No se completaron nivel de decisión, fórmula, unidad, fuente, calidad, grano, dimensiones, DAX, frecuencia, línea base, polaridad, metas, umbrales, responsables, acciones, RLS, perspectiva, tipo, relaciones ni impacto económico: pertenecen a S02–S11.

## 5. Fórmulas y campos preservados

- Fichas KPI conserva 18 fórmulas: S7:S15 y AA7:AA15.
- S07 KPI conserva 16 fórmulas en F7:F22.
- S11 Pruebas RLS conserva 16 fórmulas en F7:F22.
- Total del libro: 50 fórmulas; la copia conserva exactamente las mismas fórmulas que el original.
- Fichas KPI conserva las validaciones C7:C15, N7:N15, W7:W15 y X7:X15, y el formato condicional S7:S15.
- Se conservaron nombres de hojas, celdas combinadas, anchos de columna, formatos numéricos y alturas fuera de las filas editadas.
- Las hojas S02 a S12 y `Instrucciones` no se editaron.

Fórmulas conservadas en la primera fila:

```text
S7  = IF(OR(L7="",N7="",Q7="",R7=""),"",IF(N7="Más es mejor",...))
AA7 = IF(A7="","",COUNTA(A7:R7,T7:Z7)/25)
```

## 6. Verificación P04

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Original sin cambios | Pasa | SHA-256 original idéntico antes y después |
| Copia legible y abierta por Excel | Pasa | Excel 16.0 abrió, calculó y exportó sin reparación |
| Identificación y cinco filas de inventario | Pasa | Celdas B4, D4 y F4, y A7:G11; cotejo 5/5 con `preparation.md`, 0 diferencias |
| Cinco KPI y decisiones S01 | Pasa | Celdas B4, D4 y F4, y A7:B11; cotejo 5/5 con `preparation.md`, 0 diferencias |
| Sin campos S02–S11 completados | Pasa | C7:R7 y T7:Z7 limpios; C8:Z15 sin datos de ejemplo; S8:S15 y AA8:AA15 solo contienen fórmulas |
| Fórmulas intactas | Pasa | 50 de 50 iguales; S7 vacío y AA7 = 8 % tras cálculo |
| Sin cambios fuera del rango autorizado | Pasa | 74 cambios permitidos; 0 diferencias de valor, formato numérico, combinación, validación, formato condicional, altura o ancho fuera de lo permitido |
| Presentación visual de celdas editadas | Pasa | PDF de S01: cinco filas visibles sin recorte; PDF de Fichas: cinco KPI/decisiones visibles, fila 7 con estilo normal y campos de ejemplo limpios |
| Áreas de impresión | Sin cambios | La plantilla produce 2 páginas en S01; la segunda contiene filas vacías. Fichas produce 8 páginas por su ancho. No se modificaron áreas de impresión |

**P04: PASA.** T04 queda completada. La comprobación visual se hizo sobre las páginas 1–2 exportadas desde Excel: S01 completa y Fichas con identificación y columnas A/B. Las páginas restantes de Fichas contienen columnas no editadas.

No se asignó componente DCAM ni se inventaron responsables. La medida de apoyo y la brecha DCAM no tienen campos propios en la hoja y permanecen en `preparation.md`, secciones 5 y 6. No se abrió Power BI ni se avanzó a T05 durante T04.

## 7. Conciliación T06

Fecha: 2026-10-21. Alcance: T06 únicamente; comprobación de solo lectura.

- La copia conservó el SHA-256 `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`; no se modificó en T06.
- Identificación `Grupo 06` / `03B` / `2026-10-20` y celdas A7:G11: coinciden con `preparation.md` y con los conteos MCP de las cinco tablas.
- KPI y decisiones A7:B11: los cinco nombres y sus decisiones coinciden con `preparation.md`, sección 5; no se recalcularon valores de KPI.
- Desktop y MCP confirman los mismos archivos y columnas; Productos y Flota muestran el total exacto en Desktop, mientras Inventario, CostosAlmacen y Telemetria muestran `Rows: 99+` y su total exacto se acredita por MCP.
- No se hallaron diferencias de contenido. Los formatos `191.710`/`191710` y las fechas ISO/fechas de interfaz son representaciones del mismo valor.
- Resultado: P04 se mantiene conforme y T06 concilia 5/5 fuentes con 0 discrepancias materiales. No se alteraron la plantilla, la copia, los datos ni los requisitos.
