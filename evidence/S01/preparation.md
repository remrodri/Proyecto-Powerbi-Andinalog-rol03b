# S01 · Preparación del proyecto integrador (T03)

## 1. Estado y alcance

- Fecha: 2026-10-20.
- Alcance ejecutado: T03 únicamente.
- Entradas reales: controles de T02 en [`csv_checks.json`](../../validation/results/S01/csv_checks.json), procedencia en [`provenance.md`](provenance.md) y contraste en [`wms_contrast.md`](wms_contrast.md).
- Resultado: documento de preparación completo; P03 conforme con pendientes declarados. P03 no acredita cierre DCAM.
- Actualización 2026-10-21: T07 completada; C4 aprobado en DEC-026 y Rodrigo Tucuman designado en DEC-027. S01 permanece abierto.
- Límites: no se completó el Excel, no se ejecutó T04, no se abrió Power BI, no se importaron tablas y no se declaró ninguna prueba Desktop.

## 2. Decisión y preguntas

### 2.1 Decisión que se apoya

La **Jefatura de Operaciones**, con **revisión semanal**, decide dónde priorizar controles térmicos por producto y camión y qué lotes o centros requieren revisión por vencimiento y merma. Las señales futuras de un viaje solo se usan para evaluar reglas de alerta; no demuestran la ruta real, el inventario vigente ni una decisión ya tomada.

La decisión no autoriza atribuir causalidad, ahorro realizado ni efectividad empresarial. La selección final de KPI corresponde a S02; las metas y umbrales a S08; los responsables empresariales a S11.

### 2.2 Preguntas de negocio y vínculo con datos

| Pregunta | Tabla o campo | KPI candidato o respuesta |
| --- | --- | --- |
| ¿Qué productos y camiones concentran viajes o lecturas con desviación? | DATA-001; producto y camión como dimensiones | % de viajes con desviación; % de lecturas con desviación |
| ¿Cuánta cantidad se pierde en los lotes? | DATA-004; `cantidad_merma`, `cantidad_ingreso` | Merma por cantidades |
| ¿Qué proporción de lotes sale vencida? | DATA-004; `fecha_salida`, `fecha_vencimiento` | % de lotes salidos vencidos; número de lotes vencidos como apoyo |
| ¿Cuánto permanece un lote antes de salir? | DATA-004; `dias_en_almacen` | Días promedio en almacén |
| ¿Qué lotes o centros requieren revisión por vencimiento y merma? | DATA-004; DATA-005 | Contexto de los KPI de inventario, sin suma automática entre granos |
| ¿Qué señales previas podrían evaluar una regla de alerta? | DATA-001; `desviacion_proximos_60min_flag` y predictores | Pregunta de S10; no es un KPI final de S01 |

## 3. Inventario de las cinco fuentes oficiales

Ruta base: `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/`. Los conteos y claves provienen de T02; las huellas y tamaños están en [`source_manifest.json`](../../validation/results/S01/source_manifest.json).

| ID | Nombre | Grano | Clave | Filas | Columnas | Brecha y clasificación | Responsable |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | Una lectura dentro de un viaje. | `viaje_id` + `minutos_desde_despacho`; también `viaje_id` + `timestamp`. | 191.710 | 15 | Excepción demostrada: 26 lecturas en límites térmicos; 14 órdenes o viajes con 339 lecturas en dos particiones y 43 positivas. Se registran y no se corrigen en S01. | Grupo 06 |
| DATA-002 | `andinalog_productos_silver.csv` | Un producto. | `producto_id`. | 120 | 7 | Sin brecha observada. Diferencia de cobertura: 70 de 120 productos aparecen en telemetría; no es error de calidad. | Grupo 06 |
| DATA-003 | `andinalog_flota_silver.csv` | Un camión. | `camion_id`. | 100 | 6 | Sin brecha observada. Diferencia de definición: el centro base no equivale necesariamente al centro operativo; decisión de modelado pendiente. | Grupo 06 |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | Un lote con ingreso, salida y merma. | `lote_id`; `movimiento_id`. | 7.782 | 12 | Sin brecha observada. Limitación de alcance: todos los lotes ya salieron; no hay stock vigente en esta entrega. | Grupo 06 |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | Un centro en un mes. | `centro_distribucion` + `periodo_mes`. | 144 | 5 | Sin brecha observada. Decisión de modelado: relación temporal con el calendario pendiente; no es error de calidad. | Grupo 06 |

Las cinco claves son únicas y no tienen valores vacíos en T02. DATA-006 documenta 33 registros, cinco oficiales y un registro WMS separado; WMS no es una sexta fuente del modelo.

## 4. Observaciones clasificadas

| ID | Observación | Clasificación | Evidencia T02 o documental | Efecto y siguiente paso |
| --- | --- | --- | --- | --- |
| OBS-01 | 26 lecturas marcadas caen en el límite de tolerancia: 19 a −15 °C con referencia −18 °C y tolerancia 3 °C; 7 a 6 °C con referencia 4 °C y tolerancia 2 °C. | Excepción demostrada | T02: 26 lecturas, 0,0136 %, 26 viajes, 0 viajes dependientes solo de ellas. | No cambiar la etiqueta ni redefinir la regla. Tratar en S03–S04 y explicar en S02 si afecta la lectura del KPI. |
| OBS-02 | 14 órdenes o viajes contienen 339 lecturas en dos particiones; 43 de esas lecturas son positivas. | Excepción demostrada y límite de partición | T02: 14 órdenes y 14 viajes; 339 lecturas; 43 positivas en ambos cortes. | No unir particiones ni reasignar cortes sin una regla aprobada. Documentar el grano en S05 y el horizonte en S10. |
| OBS-03 | 70 de 120 productos del catálogo aparecen en telemetría; todos los 70 son refrigerados o congelados. | Diferencia de cobertura | T02: 70 productos distintos; 0 productos de telemetría fuera de esas categorías. | No es error de calidad. No extrapolar los KPI térmicos a los 120 productos sin declarar la cobertura. |
| OBS-04 | 8.000 órdenes tienen telemetría y 22.000 órdenes WMS no la tienen. | Diferencia de cobertura | T02: cobertura 8.000 de 8.000 órdenes de telemetría; 22.000 WMS sin telemetría. | El contraste WMS no describe el total de la operación. Mantener WMS fuera del modelo y no usarlo como verdad operativa. |
| OBS-05 | Los 7.782 lotes tienen salida; no hay stock vigente. | Limitación de alcance | T02: 0 movimientos sin `fecha_salida`; 0 desbalances entre ingreso, salida y merma. | Los KPI de vencimiento son históricos. No presentarlos como alertas de stock actual. |
| OBS-06 | No encontramos una definición explícita de `centro_distribucion` en las fuentes revisadas y el centro base del camión no demuestra el centro operativo del viaje. | Decisión de modelado y brecha DCAM | DUD-S01-04; T02 muestra 30.000/30.000 coincidencias de centro de lote, chofer-mes y zona, y 8.000/8.000 de centro base, pero no define el concepto. | No usar el centro base como ruta real ni como inventario vigente. Definir la semántica antes de filtros y RLS. |
| OBS-07 | El objetivo de 60 minutos no observa una hora completa al final del viaje. | Limitación documentada | `docs/context.md`: 16.000 registros en las últimas dos posiciones, 1.129 con objetivo positivo; no recalculado en T02. | No interpretar el cero final como una hora completa sin desviación. Conservar la limitación en S10. |
| OBS-08 | La merma por cantidades no es merma por valor; la medida económica sigue pendiente. | Decisión pendiente | DEC-017; DATA-004; DATA-005. | Mantener la merma por cantidades como candidata. No sumar merma de inventario y costos como conceptos independientes. |

También se comprobó que las cinco claves son únicas, que no hay celdas vacías en los campos leídos y que el balance `cantidad_ingreso = cantidad_salida + cantidad_merma` se cumple en los 7.782 lotes. Esos resultados no convierten la ausencia de nulos en una validación semántica.

## 5. KPI candidatos y medida de apoyo

Los valores siguientes son **referencias** de la spec o de controles documentados; no son metas. No se recalcularon nuevos KPI por valor en T03.

| # | KPI candidato | Pregunta y decisión que apoya | Fórmula y unidad | Denominador contextual | Fuente | Límite y estado |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | % de viajes con desviación | ¿Qué proporción de viajes tiene al menos una lectura marcada? Apoya la priorización de controles por producto y camión. | Viajes con al menos una lectura marcada / viajes observados; porcentaje. | Viajes del contexto; 14,3625 % es referencia global sin filtros. | DATA-001; DATA-002. | No demuestra duración, causa ni ahorro. Candidato; selección S02; meta S08. |
| 2 | % de lecturas con desviación | ¿Qué proporción de lecturas queda marcada? Apoya la lectura de intensidad aparente y la comparación entre productos o camiones. | Lecturas marcadas / lecturas observadas; porcentaje. | Lecturas del contexto; 6,1395 % es referencia global sin filtros. | DATA-001; DATA-002. | Es proporción de observaciones; no mide duración exacta, intensidad térmica ni cobertura del monitoreo. Candidato; selección S02; meta S08. |
| 3 | Merma por cantidades | ¿Cuánta cantidad se pierde? Apoya la revisión de lotes y centros con peor desempeño. | Suma de `cantidad_merma` / suma de `cantidad_ingreso`; porcentaje. | Suma de `cantidad_ingreso` de los lotes del contexto. | DATA-004. | No equivale a merma por valor; no promediar porcentajes por lote. Candidato; selección S02; meta S08. |
| 4 | % de lotes salidos vencidos | ¿Qué proporción de lotes sale vencida? Apoya la revisión de gestión de lotes y centros. | Lotes cuya fecha de salida es posterior al día de vencimiento / lotes salidos; porcentaje. | Lotes salidos del contexto; 1.069 de 7.782 y 13,7 % son referencias globales. | DATA-004. | Se comparan fechas sin hora: salir el mismo día del vencimiento no cuenta como vencido. El denominador filtrado debe ser el del contexto. Candidato; selección S02; meta S08. |
| 5 | Días promedio en almacén | ¿Cuánto permanece un lote antes de salir? Apoya la revisión de permanencia histórica por centro o producto. | Promedio de `dias_en_almacen`; días. | Lotes con salida en el contexto. | DATA-004. | 38,9805 días es referencia, pendiente de validación Desktop. Es permanencia histórica, no rotación ni causa. Candidato; selección S02; meta S08. |

**Medida de apoyo:** número de lotes vencidos. Fórmula: conteo de lotes cuya fecha de salida es posterior al día de vencimiento, comparando fechas sin hora; unidad: lotes; sin denominador; fuente DATA-004; referencia global 1.069. Salir el día del vencimiento no cuenta. No es un KPI principal ni una meta.

La selección final de 5–8 KPI es de S02. Las metas y umbrales son de S08. Los responsables empresariales se completan en S11. La medida económica de merma por valor sigue pendiente y no se incorpora como candidata.

## 6. Brecha DCAM priorizada

### 6.1 Hecho y prioridad

**Brecha A:** **no encontramos una definición explícita de `centro_distribucion` en las fuentes revisadas.** Los seis centros aparecen de forma consistente, pero no se documenta si el campo representa centro operativo, centro de almacenamiento, centro de despacho, ámbito de responsabilidad o combinación. El centro base de flota tampoco demuestra el centro operativo real de un viaje. La formulación no afirma una ausencia empresarial; se limita al alcance documental revisado.

La brecha se prioriza porque afecta filtros, interpretación de costos, atribución de inventario y RLS. No se presenta como error de calidad de los datos: es una brecha de definición y conocimiento del dato.

### 6.2 Componente, dimensión y puntaje

| Campo | Registro |
| --- | --- |
| Componente | **C4 — Conocimiento de los datos del negocio**, aprobado por el usuario el 2026-10-21 (DEC-026). |
| Dimensión | **Evidencia**: falta un artefacto aprobado que defina el campo y su uso. |
| Puntaje tentativo | **1 — Incipiente**, con confianza baja y alcance documental. |
| Fundamento | La brecha es semántica: no encontramos la definición en las fuentes revisadas y T02 demuestra consistencia entre fuentes, no significado operativo. C4 corresponde al conocimiento y significado del dato; no es un error de calidad —C5—, un problema técnico —C6— ni una falla operativa —C7—. |
| Evidencia disponible | Seis centros consistentes entre inventario, flota y costos; T02: 30.000/30.000 coincidencias de lote, chofer-mes y zona; 8.000/8.000 de centro base para órdenes con telemetría; lista C1–C8 en `SRC-208`, `Instrucciones!B10`. |
| Evidencia faltante | Definición aprobada, propietario, regla para `centro_distribucion_base` frente a `centro_distribucion`, uso en filtros y RLS. |
| Riesgo | Filtros o RLS que asignen viajes, lotes o costos al centro equivocado; conclusiones operativas sobre ruta o inventario no demostradas. |
| Estado | **C4 identificado y aprobado; no cierra S01 por sí solo.** |

Se conservan la dimensión **Evidencia**, el puntaje **1 — Incipiente** y la confianza **baja** con alcance documental. La lista se consultó en `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx`, hoja `Instrucciones`, celda **`B10`** (SRC-208; SHA-256 `D6FE317D30241BA3705A7B18F4D1B28CA5B55A187E9AEDBF2B6B9E7A1A294686`), **únicamente como referencia complementaria de la lista**. El Excel no se completó ni se modificó y no contiene un mapeo de esta brecha a C4. El PDF SRC-202 sigue siendo la **referencia metodológica** para hecho, dimensión, evidencia, escala y riesgo.

La asignación se apoya en la aprobación explícita del usuario registrada en DEC-026 y en la justificación anterior. C4 identifica el componente, pero no sustituye la definición de `centro_distribucion` ni resuelve filtros o RLS. C3 no se elige porque no hay evidencia de que la brecha sea falta de propietario, política o derecho de decisión.

### 6.3 Historial de la asignación

- T03 registró inicialmente **C4 — Conocimiento de los datos del negocio** como propuesta, a partir de la lista histórica C1–C8 referida por la guía S01 y por `docs/context.md`.
- Revisión 2026-10-20: se verificó que esa lista es histórica y que SRC-202 no enumera C1–C8. No se localizó una fuente activa que respalde C4 ni una decisión que haya autorizado asignarlo.
- Se retira C4 de la asignación vigente y se sustituye por «**componente pendiente de identificación y respaldo**». Se conservan la dimensión Evidencia, el puntaje 1 tentativo y la confianza baja.
- **2026-10-21:** el usuario autorizó consultar la lista del Excel del taller solo como referencia complementaria y aprobó **C4** para la brecha documental. Se registra DEC-026, se cita `Instrucciones!B10` y se mantiene el PDF como referencia metodológica. La definición del campo y el tratamiento en filtros/RLS siguen pendientes.

## 7. Trazabilidad de estados y límites

| Afirmación o dato | Estado | Fuente |
| --- | --- | --- |
| Conteos, claves y balance de las cinco fuentes | Cálculo propio reproducible | T02; `csv_checks.json` |
| Procedencia y recuentos Bronze–Silver | Dato entregado por DATA-006 | T02; `provenance.md` |
| Cruces WMS y cobertura 8.000/22.000 | Cálculo propio de contraste | T02; `wms_contrast.md` |
| 14,3625 %, 6,1395 %, 7,3573 %, 1.069, 13,7 % y 38,9805 | Referencias de la spec; no metas ni recálculo de T03 | Spec, anexo B; contexto |
| Hecho de la brecha DCAM | Documental: no encontramos una definición explícita en las fuentes revisadas | DUD-S01-04; DEC-026 |
| Componente DCAM y puntaje 1 | **C4 aprobado**; dimensión Evidencia, puntaje 1 tentativo y confianza baja | DEC-026; SRC-208 `Instrucciones!B10`; SRC-202 |
| Asignación C4 en la primera versión de T03 | Historial; retirada y luego aprobada con referencia complementaria y decisión | Guía S01; `docs/context.md`; DEC-018; DEC-022; DEC-026 |
| Desktop, Excel y T04 | Ejecutados y conciliados en T06; ver sección 9 | T04, T05 y T06 |

Límites que permanecen:

- C4 identifica el componente, pero no define `centro_distribucion` ni sustituye la semántica necesaria para filtros y RLS.
- Rodrigo Tucuman quedó designado para compartir pantalla en S02 (DEC-027).
- Los datos son sintéticos y no demuestran causalidad, ahorro ni generalización a toda la empresa.
- La cobertura de 8.000 de 30.000 órdenes WMS limita las conclusiones sobre la operación total.

## 8. Comprobación P03

Estado histórico al ejecutar P03; no describe el estado actual, que se registra en la sección 9.

P03 se ejecutó como revisión documental contra la spec, T02 y los límites autorizados: decisión con usuaria y frecuencia; cinco fuentes oficiales con grano, clave, filas, columnas, brecha y responsable; observaciones clasificadas; cinco KPI candidatos con fórmula, unidad, denominador, fuente y límite; medida de apoyo; DCAM tentativa con componente pendiente de identificación y respaldo; Desktop, Excel y T04 no ejecutados.

Resultado: **P03 conforme con pendientes declarados**. P03 no acredita cierre DCAM. En el corte de P03, RF-S01-07, CA-S01-03 y el cierre de S01 permanecían pendientes por falta de respaldo del componente DCAM y persona de pantalla. Esos dos pendientes quedaron resueltos después en DEC-026/027; véase la sección 10. No se declara S01 cumplido.

## 9. Conciliación T06 después de Desktop

- Fecha: 2026-10-21.
- Alcance: T06 únicamente. Comparación de solo lectura entre `preparation.md`, `template_mapping.md`, `desktop_checks.md`, `mcp_model_checks.md`, `csv_checks.json` y la copia Excel.
- Sin cambios en CSV, Excel, modelo, PBIP, spec ni requisitos.
- Huellas comprobadas sin cambios: copia Excel `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`; plantilla original `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30`; `AndinaLog_03B.pbip` `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE`.

### 9.1 Matriz de conciliación

| Fuente | T02: CSV | T03: Markdown | T04: Excel | T05: Desktop | T05: MCP | Resultado |
| --- | --- | --- | --- | --- | --- | --- |
| DATA-001 Telemetria | 191.710 × 15 | 191.710 × 15 | 191.710 × 15 | 15 columnas; preview `Rows: 99+` | 191.710 filas | Coincide; total exacto por MCP |
| DATA-002 Productos | 120 × 7 | 120 × 7 | 120 × 7 | 120 filas × 7 columnas | 120 filas | Coincide |
| DATA-003 Flota | 100 × 6 | 100 × 6 | 100 × 6 | 100 filas × 6 columnas; 0 decimales | 100 filas | Coincide; sin campos decimales |
| DATA-004 Inventario | 7.782 × 12 | 7.782 × 12 | 7.782 × 12 | 12 columnas; preview `Rows: 99+` | 7.782 filas | Coincide; total exacto por MCP |
| DATA-005 CostosAlmacen | 144 × 5 | 144 × 5 | 144 × 5 | 5 columnas; preview `Rows: 99+` | 144 filas | Coincide; total exacto por MCP |

Los nombres de archivo, grano, clave, brecha y responsable de las cinco filas de la hoja `S01 Inventario` coinciden con la sección 3. Los cinco nombres de KPI y sus decisiones coinciden con la sección 5; los valores de KPI no se recalcularon en T06. El cotejo cubrió 35 celdas de inventario y 10 de KPI, con 0 diferencias de contenido. Las filas de Excel 7–11 corresponden a DATA-001–DATA-005 en ese orden; la hoja no contiene una columna separada para el ID.

### 9.2 Diferencias reales y su clasificación

| Diferencia observada | Clasificación | Tratamiento |
| --- | --- | --- |
| Markdown escribe `191.710`; Excel almacena `191710` | Formato numérico | No es discrepancia; mismo valor. |
| Desktop muestra fechas como `8/5/2025 1:47:11 AM`; CSV/Origen como `2025-08-05 01:47:11` | Formato regional de la interfaz | No es discrepancia; mismo instante. |
| Desktop muestra `Rows: 99+` en Inventario, CostosAlmacen y Telemetria | Límite de la vista previa | El total exacto se toma de MCP, no del CSV ni del preview. |
| El modelo agrega `RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61` | Columna interna del motor | No pertenece al CSV y no se cuenta como columna de origen. |
| Excel pesa 33.844 bytes y la plantilla 36.907 | Reserialización de `openpyxl` | No es discrepancia de contenido; se compararon valores y fórmulas. |

No se identificaron discrepancias materiales ni datos del inventario sin procedencia. Tampoco se reemplazó una observación de Desktop por el valor esperado del CSV: en las tres tablas con preview parcial, el conteo exacto consta como verificación MCP separada. No hay discrepancia abierta que corregir.

### 9.3 Resultado

**T06: PASA.** La observación Desktop, los controles T02, el inventario Markdown y la copia Excel son coherentes para las cinco fuentes. En el corte de T06 se mantenían como límites el preview parcial de tres tablas, el componente DCAM pendiente, la persona de pantalla sin designar y los demás pendientes de S01. No se modificaron datos ni requisitos; S01 no se declara cerrado.

## 10. Actualización T07: C4 aprobado y pantalla designada

- Fecha: 2026-10-21. Alcance: documentación de T07; sin cambios en datos, modelo, PBIP, Excel original ni requisitos.
- El usuario aprobó **C4 — Conocimiento de los datos del negocio** para la brecha documental priorizada (DEC-026). Se mantienen dimensión **Evidencia**, puntaje **1 — Incipiente** y confianza **baja**.
- El hecho se formula como **«no encontramos una definición explícita de `centro_distribucion` en las fuentes revisadas»**; no se afirma una ausencia empresarial.
- La lista se consultó en `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx`, `Instrucciones!B10`, solo como referencia complementaria. El PDF SRC-202 sigue siendo la referencia metodológica. El Excel no se completó ni se modificó.
- **Rodrigo Tucuman** quedó designado para compartir pantalla en S02 (DEC-027).
- **T07 completada.** S01 sigue abierto: falta auditoría T08, resolver hallazgos T09 y aprobar el cierre T10. La definición del campo y su uso en filtros/RLS continúan pendientes.
