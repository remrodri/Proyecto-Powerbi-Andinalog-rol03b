# S01 · Traspaso documental a S02

## 1. Estado y alcance

- Fecha: 2026-10-21.
- Alcance ejecutado: **parte documental de T07**.
- Resultado: traspaso preparado y **T07 completada** con C4 aprobado y Rodrigo Tucuman, integrante del Grupo 06, designado para pantalla.
- No se inició auditoría, no se modificó la spec en sus requisitos, no se alteraron datos, modelo, PBIP, Excel ni requisitos y **no se declaró cerrado S01**.
- Los resultados de este documento son de Build y de la conciliación T06; **no son una auditoría independiente**.

## 2. Decisión que apoya el proyecto

La **Jefatura de Operaciones**, con **revisión semanal**, decide dónde priorizar controles térmicos por producto y camión y qué lotes o centros requieren revisión por vencimiento y merma.

La decisión no autoriza a afirmar causalidad, ahorro realizado, ruta real ni inventario vigente. La selección final de KPI corresponde a S02; las metas y umbrales, a S08; los responsables empresariales, a S11.

## 3. Inventario y resultados disponibles

Las cinco fuentes oficiales son las únicas del inventario principal. WMS se usó solo como contraste y no forma parte del modelo.

| ID | Tabla / archivo | Grano | Clave | Filas | Columnas | Resultado y límite principal |
| --- | --- | --- | --- | ---: | ---: | --- |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | Una lectura dentro de un viaje | `viaje_id` + `minutos_desde_despacho`; también `viaje_id` + `timestamp` | 191.710 | 15 | 26 lecturas en límites térmicos y 14 viajes/órdenes con 339 lecturas en dos particiones; no se corrigen. |
| DATA-002 | `andinalog_productos_silver.csv` | Un producto | `producto_id` | 120 | 7 | Sin brecha de calidad observada; 70 de 120 productos aparecen en telemetría. |
| DATA-003 | `andinalog_flota_silver.csv` | Un camión | `camion_id` | 100 | 6 | Sin brecha de calidad observada; el centro base no demuestra el centro operativo del viaje. |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | Un lote con ingreso, salida y merma | `lote_id`; `movimiento_id` | 7.782 | 12 | Sin desbalances; todos los lotes tienen salida y no hay stock vigente en esta entrega. |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | Un centro en un mes | `centro_distribucion` + `periodo_mes` | 144 | 5 | Sin brecha de calidad observada; falta precisar la relación temporal con el calendario. |

Las cinco claves son únicas y no tienen valores vacíos en los controles de T02. Los conteos y columnas coinciden entre CSV, Markdown, Excel, Desktop y MCP; la conciliación T06 no encontró discrepancias materiales.

## 4. KPI candidatos

Son candidatos, no KPI finales ni metas. Los valores son referencias documentadas; no se recalcularon en T06.

| # | KPI | Fórmula y unidad | Denominador contextual | Referencia | Límite que debe conservarse |
| ---: | --- | --- | --- | --- | --- |
| 1 | % de viajes con desviación | Viajes con al menos una lectura marcada / viajes observados; porcentaje | Viajes del contexto | 14,3625 % global | No demuestra duración, causa, ruta ni ahorro. |
| 2 | % de lecturas con desviación | Lecturas marcadas / lecturas observadas; porcentaje | Lecturas del contexto | 6,1395 % global | Es proporción de observaciones; no mide duración exacta ni intensidad térmica. |
| 3 | Merma por cantidades | Suma de `cantidad_merma` / suma de `cantidad_ingreso`; porcentaje | Suma de `cantidad_ingreso` del contexto | 7,3573 % | No equivale a merma por valor; no promediar porcentajes por lote. |
| 4 | % de lotes salidos vencidos | Lotes con salida posterior al día de vencimiento / lotes salidos; porcentaje | Lotes salidos del contexto | 1.069 de 7.782; 13,7 % | Comparar fechas sin hora: salir el mismo día del vencimiento no cuenta como vencido. |
| 5 | Días promedio en almacén | Promedio de `dias_en_almacen`; días | Lotes con salida en el contexto | 38,9805 días | Es permanencia histórica, no rotación ni causa; no se validó como valor final en T05. |

**Medida de apoyo:** número de lotes vencidos; conteo de lotes cuya salida es posterior al día de vencimiento; referencia global 1.069. No es KPI principal ni meta.

En S02 corresponde seleccionar 5–8 KPI, precisar nivel de decisión, fórmula en palabras, unidad y responsables. Las metas y umbrales pertenecen a S08; los responsables empresariales, a S11.

## 5. Evidencias verificadas

| Evidencia | Contenido | Estado |
| --- | --- | --- |
| [`preparation.md`](preparation.md) | Decisión, inventario, observaciones, KPI y brecha DCAM; sección 9 concilia T06. | Disponible para S02. |
| [`desktop_checks.md`](desktop_checks.md) | Evidencia Desktop auténtica de las cinco tablas, archivo, columnas, filas, decimales y Flota sin decimales; conciliación final T06. | T05 confirmada por el usuario. |
| [`mcp_model_checks.md`](mcp_model_checks.md) | Consultas DAX y totales exactos de las cinco tablas; estructura del PBIP en solo lectura. | Disponible; no sustituye por sí solo la captura Desktop. |
| [`screenshots/`](screenshots/) | Capturas `s01_t05_01` a `s01_t05_13`, con hashes en `desktop_checks.md`. | Disponible para auditoría. |
| [`template_mapping.md`](template_mapping.md) | Copia Excel, celdas completadas, fórmulas y conciliación T06. | Disponible. |
| [`csv_checks.json`](../../validation/results/S01/csv_checks.json) | Conteos, encabezados, claves y controles de T02. | Reproducible. |
| [`M4_Equipo06_Proyecto_Integrador_v2.xlsx`](../../deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx) | Copia de seguimiento con las cinco fuentes y cinco KPI/decisiones S01. | SHA-256 `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1`. |
| [`AndinaLog_03B.pbip`](../../powerbi/AndinaLog_03B.pbip) | `RutaSilver`, cinco tablas Import, 0 relaciones, 0 medidas y sin visuales. | SHA-256 `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE`. |

Resultados concretos de la conciliación T06:

- Productos 120 × 7, Flota 100 × 6, Inventario 7.782 × 12, CostosAlmacen 144 × 5 y Telemetria 191.710 × 15.
- Productos y Flota muestran el total exacto en Desktop. En Inventario, CostosAlmacen y Telemetria el preview muestra `Rows: 99+`; el total exacto se acreditó por MCP y no se infirió del CSV.
- Decimales leídos con punto: `23.73`, `34.05`, `47.11`, `32.9`, `37983.68`, `155267.38`, `4.27`, `66.98` y `13.18`. Flota no contiene campos decimales.
- El modelo agrega una columna interna `RowNumber`; no pertenece al CSV y no se cuenta como columna de origen.
- 0 relaciones, 0 medidas, 0 roles y un informe sin visuales. El PBIP es una implementación mínima, no un tablero terminado.

## 6. Brecha DCAM: estado y búsqueda de respaldo

### 6.1 Brecha priorizada

| Campo | Estado actual |
| --- | --- |
| Hecho | **No encontramos una definición explícita de `centro_distribucion` en las fuentes revisadas.** Los seis centros aparecen de forma consistente, pero no se documenta si representan centro operativo, almacenamiento, despacho, ámbito de responsabilidad u otra combinación. Esto no afirma una ausencia empresarial. |
| Dimensión | **Evidencia**. |
| Puntaje tentativo | **1 — Incipiente**, confianza baja, alcance documental. |
| Evidencia disponible | Seis centros consistentes entre inventario, flota y costos; coincidencias de centro en los cruces documentados de T02; lista C1-C8 consultada en `SRC-208`, celda `Instrucciones!B10`. |
| Evidencia faltante | Definición aprobada, propietario, regla para `centro_distribucion_base` frente a `centro_distribucion`, uso en filtros y RLS. |
| Riesgo | Asignar viajes, lotes o costos al centro equivocado y sacar conclusiones operativas no demostradas. |
| Componente DCAM aplicable | **C4 — Conocimiento de los datos del negocio**, aprobado por el usuario el 2026-10-21 (DEC-026). |

La brecha no es un error de calidad de los datos: es una brecha de definición y conocimiento del dato. Tampoco autoriza usar el centro base como ruta real ni como inventario vigente. C4 identifica el componente, pero **no sustituye la definición del campo**.

### 6.2 Referencia complementaria y referencia metodológica

- La lista se consultó en `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx`, hoja `Instrucciones`, celda **`B10`** (SRC-208; SHA-256 `D6FE317D30241BA3705A7B18F4D1B28CA5B55A187E9AEDBF2B6B9E7A1A294686`). Se leyó **solo como referencia complementaria de la lista**, sin completar ni modificar el Excel.
- La celda enumera: “C1 Estrategia y caso de negocio · C2 Programa y financiamiento · C3 Gobierno de datos · **C4 Conocimiento de los datos del negocio** · C5 Calidad de datos · C6 Tecnología y arquitectura · C7 Operación de los datos · C8 Entorno de control y cultura”.
- El PDF SRC-202, `references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf`, sigue siendo la **referencia metodológica** para el diagnóstico: hecho, dimensión, evidencia, escala y riesgo. No se le atribuye la lista C1-C8.

### 6.3 Justificación de C4

C4 corresponde al conocimiento y significado de los datos del negocio. La brecha es documental y semántica: no sabemos qué representa `centro_distribucion` en las fuentes revisadas y esa falta de definición afecta filtros, cortes y RLS. No es un valor erróneo —C5—, un problema técnico —C6— ni una falla operativa —C7—. Tampoco hay evidencia de que el problema sea falta de propietario, política o derecho de decisión —C3—. C1, C2 y C8 quedan más lejos del hecho documental.

El **respaldo de la elección es la aprobación del usuario registrada en DEC-026**, apoyada por la lista de `Instrucciones!B10`. El Excel no contiene un mapeo de esta brecha a C4; no se le atribuye ese alcance. La elección se mantiene sujeta a revisión si aparece evidencia nueva.

## 7. Persona que compartirá pantalla en S02

**Rodrigo Tucuman, integrante del Grupo 06**, compartirá pantalla en S02, por designación del usuario del 21 de octubre de 2026 (DEC-027).

## 8. Pendientes actuales para S02 y para el cierre de S01

| Prioridad | Pendiente | Estado / qué falta |
| --- | --- | --- |
| 1 | Componente DCAM aplicable | **Resuelto:** C4 — Conocimiento de los datos del negocio, aprobado en DEC-026; lista en `Instrucciones!B10` como referencia complementaria. |
| 2 | Persona que compartirá pantalla en S02 | **Resuelto:** Rodrigo Tucuman, integrante del Grupo 06 (DEC-027). |
| 3 | T07 | **Completada el 2026-10-21**; no acredita cierre de S01. |
| 4 | Auditoría T08 | No iniciada; requiere autorización independiente y no debe confundirse con T06. |
| 5 | Cierre de S01 | No declarado; falta auditoría y aprobación de cierre. |
| 6 | Selección final de KPI | Corresponde a S02; los cinco candidatos no son definitivos. |
| 7 | Metas, umbrales y responsables empresariales | S08 y S11. |
| 8 | Merma por valor | DUD-S01-05 sigue abierta; no se suma a merma por cantidades como si fuera el mismo concepto. |
| 9 | Semántica de `centro_distribucion` | DUD-S01-04 sigue abierta; afecta filtros, ruta, inventario y RLS. |
| 10 | Modelo y tablero | Estado actual mínimo: sin relaciones, medidas ni visuales. No presentarlo como producto terminado. |

Límites de datos que deben acompañar cualquier lectura:

- 26 lecturas en límites térmicos; su tratamiento no se cambió en S01.
- 14 viajes/órdenes con dos particiones y 339 lecturas; no unir particiones sin regla aprobada.
- Cobertura de 70 de 120 productos en telemetría; no extrapolar KPI térmicos a todo el catálogo.
- 8.000 de 30.000 órdenes WMS con telemetría; WMS es contraste, no verdad operativa total.
- Todos los lotes tienen salida; los KPI de vencimiento son históricos, no alertas de stock actual.
- El objetivo de 60 minutos no observa una hora completa al final del viaje.

## 9. Archivos de entrada para S02

Orden sugerido de lectura:

1. [`specs/001-s01-inventory/spec.md`](../../specs/001-s01-inventory/spec.md): requisitos, criterios y dudas.
2. [`preparation.md`](preparation.md): decisión, inventario, KPI y brecha; sección 9 para la conciliación.
3. [`desktop_checks.md`](desktop_checks.md) y [`mcp_model_checks.md`](mcp_model_checks.md): evidencia ejecutada y límites.
4. [`template_mapping.md`](template_mapping.md): correspondencia con la copia Excel.
5. [`csv_checks.json`](../../validation/results/S01/csv_checks.json) y [`provenance.md`](provenance.md): controles y procedencia.
6. [`wms_contrast.md`](wms_contrast.md): contraste separado, pendiente de auditoría.
7. [`M4_Equipo06_Proyecto_Integrador_v2.xlsx`](../../deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx): seguimiento y KPI/decisiones S01.
8. `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx`, `Instrucciones!B10` (SRC-208): lista C1-C8 consultada como referencia complementaria; no se copió, completó ni modificó.

## 10. Cierre de T07 y pendientes de S01

T07 se completa el 2026-10-21 porque:

- C4 — Conocimiento de los datos del negocio quedó identificado y aprobado por el usuario, con la lista de `Instrucciones!B10` como referencia complementaria y el PDF como referencia metodológica; y
- Rodrigo Tucuman, integrante del Grupo 06, quedó designado para compartir pantalla en S02.

**T07 no cierra S01.** Para cerrar S01 falta la auditoría independiente T08, resolver los hallazgos que de ella surjan —T09— y obtener la aprobación de cierre T10. También siguen abiertos los pendientes de negocio, especialmente la definición de `centro_distribucion` para filtros y RLS. Este documento no sustituye la auditoría ni autoriza el cierre de S01.
