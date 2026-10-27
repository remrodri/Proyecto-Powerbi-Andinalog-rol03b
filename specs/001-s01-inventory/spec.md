# Spec · S01 — Preparación del proyecto integrador

| Campo | Valor |
| --- | --- |
| ID | 001-s01-inventory |
| Hito | S01 — Preparación del proyecto integrador |
| Versión | 0.4 |
| Fecha | 2026-10-20; estado actualizado el 2026-10-22 |
| Estado de la spec | Aprobada; S01 cerrado con limitaciones documentadas |
| Cumplimiento de S01 | Cumplido; cierre aprobado por el usuario el 2026-10-22 |
| Entrada | Guía S01, PDF DCAM, lista C1–C8 complementaria en SRC-208, plantilla del Proyecto Integrador, cinco Silver oficiales y WMS de contraste. |
| Salida | Documentación de decisión, fuentes, preparación inicial, brecha DCAM, KPI candidatos y evidencia esperada. |
| Fase | S01 cerrado; S02 no iniciado. El Build posterior se rige por el plan y las autorizaciones de cada hito. |

**Aprobación:** el usuario aprobó esta especificación el 20 de octubre de 2026. La versión 0.4 incorpora únicamente los ajustes expresamente autorizados sobre el alcance DCAM y la verificación decimal/Flota; conserva las demás condiciones de la v0.3. La aprobación de la spec habilitó la planificación; el cierre de S01 se registra por separado y fue aprobado el 2026-10-22.

**Historial de versiones:** v0.3 (2026-10-20) estableció la base aprobada; v0.4 (2026-10-20) registra DEC-022 (componente DCAM aplicable) y DEC-023 (verificación decimal/Flota) sin alterar las demás condiciones. Actualización editorial 2026-10-20: EV-S01-WMS quedó guardado como `evidence/S01/wms_contrast.md` en T02; no cambia requisitos ni cierra DUD-S01-06. Actualización de estado 2026-10-21: DEC-026 respalda C4 con SRC-208 y DEC-027 designa a Rodrigo Tucuman; no cambian requisitos. Actualización de estado 2026-10-22: el usuario aprobó el cierre de S01 con las limitaciones documentadas; no se modificaron requisitos ni se resolvieron los pendientes trasladados.

**Cumplimiento de S01:** **cerrado con limitaciones documentadas el 2026-10-22**, tras las auditorías T08 (rondas 01 y 02), la corrección T09 y la aprobación T10. El componente DCAM y la persona de pantalla quedaron respaldados en DEC-026 y DEC-027 y verificados en T08. Los pendientes trasladados a S02, S08 y S11 no se declaran resueltos.

**Idioma y formato:** contenido en español; nombres de archivos y carpetas en inglés. Markdown es la fuente de verdad. La copia de la plantilla oficial se completa durante Build.

## 1. Contexto y decisión

### 1.1 Hecho que motiva S01

AndinaLog 03B reúne operaciones, planificación y datos para apoyar decisiones sobre cadena de frío, vencimiento y merma. Antes de construir el proyecto Power BI se necesita una base acordada: qué decisión se apoya, quién la usa, con qué fuentes, qué límites existen y qué evidencia demostrará el trabajo.

S01 no produce el tablero. Prepara el proyecto integrador y deja constancia de lo que se sabe, lo que se supone y lo que falta.

### 1.2 Decisión que se apoya

La decisión corresponde a la **Jefatura de Operaciones** y se revisa **semanalmente**. Debe permitir:

1. Priorizar productos y camiones con controles térmicos más exigentes.
2. Identificar lotes y centros con peor desempeño histórico de vencimiento y merma para revisar su gestión.
3. Evaluar, más adelante, reglas de alerta con información disponible antes de la salida o durante el viaje.

Las señales futuras de un viaje solo pueden evaluar reglas de alerta. No se usan para suponer la ruta real, el inventario vigente ni una decisión ya tomada. La decisión no autoriza atribuir causalidad ni ahorros sin evidencia.

### 1.3 Preguntas que la spec debe responder

- ¿Qué decisión, usuaria y frecuencia quedan registradas?
- ¿Qué tablas y campos sostienen esa decisión?
- ¿Qué brechas demostradas, diferencias de cobertura, limitaciones de alcance o decisiones de modelado se observan?
- ¿Qué KPI son candidatos y cuándo se seleccionan, se les asignan metas y se completan sus responsables?
- ¿Qué evidencia demuestra legibilidad y preparación sin confundirla con Build?
- ¿Qué falta para que S01 pueda considerarse cerrado?

### 1.4 Alcance de esta fase

Documentar la preparación de S01: decisión, fuentes, controles, brecha DCAM, KPI candidatos, límites, responsables de revisión, riesgos y dudas. Se permite inspeccionar fuentes en solo lectura y registrar resultados.

### 1.5 Fuera de alcance en Specify

- Crear el proyecto `.pbip`, el modelo semántico, consultas de transformación, relaciones, medidas DAX o visuales.
- Limpiar, imputar, corregir etiquetas o modificar los Silver.
- Cargar WMS en el modelo.
- Completar plantillas oficiales, fichas KPI o el informe final.
- Publicar en Power BI Service, configurar RLS o ejecutar What-if.
- Declarar pruebas Desktop, actualización, publicación o resultados predictivos no ejecutados.

### 1.6 Límite del Build permitido

El Build podrá crear únicamente la importación mínima necesaria, el parámetro `RutaSilver` y los tipos iniciales. No se autorizan en S01 limpieza, relaciones, medidas, visuales ni corrección de anomalías regionales. El tipado inicial permitido no autoriza corregir anomalías regionales; se registran para tratamiento posterior.

## 2. Objetivo y resultado esperado

**Objetivo:** dejar una base verificable para planificar S01 y el Build posterior, sin convertir supuestos en datos ni propuestas en resultados.

**Resultado esperado:** una spec aprobada que identifique la decisión, las fuentes, los controles realizados, los KPI candidatos, la brecha DCAM priorizada, las evidencias esperadas y las dudas que impiden el cierre.

## 3. Fuentes y evidencia

### 3.1 Fuentes principales

| ID | Fuente | Uso en S01 |
| --- | --- | --- |
| SRC-101 | `references/S01/GIAD-M4-S01_Preparacion_Proyecto_Integrador.docx` | Requisitos y entregables de S01. |
| SRC-202 | `references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf` | Referencia DCAM metodológica: Compromiso, Proceso y Evidencia; escala 1–5. No enumera C1–C8. |
| SRC-201 | `references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | Estructura de seguimiento y fichas; su copia se completa en Build. |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | Lecturas térmicas y viajes. |
| DATA-002 | `andinalog_productos_silver.csv` | Producto, familia y perfil térmico. |
| DATA-003 | `andinalog_flota_silver.csv` | Camión, centro base y capacidad. |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | Lotes, centro, ingreso, salida y vencimiento. |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | Costos de almacén por centro y mes. |
| DATA-006 | `GIAD-M3_v10_auditoria_bronze_silver.csv` | Procedencia Bronze–Silver y correcciones oficiales. |
| DATA-007 | `andinalog_wms_orders_silver.csv` | Contraste orden→centro; no se carga al modelo. |

Los cinco Silver oficiales son DATA-001 a DATA-005. WMS se mantiene separado como fuente de contraste y no se cuenta como sexta fuente del modelo. DATA-006 documenta procedencia y no es una tabla del modelo. SRC-208, `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx`, se usa solo como referencia complementaria de la lista C1–C8 en `Instrucciones!B10`; no se copia, completa ni modifica.

### 3.2 Inventario de las cinco fuentes oficiales

| Fuente | Nombre | Ruta | Grano | Clave | Filas | Columnas | Brecha y clasificación | Responsable de revisión |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Una lectura dentro de un viaje. | `viaje_id + minutos_desde_despacho`; también `viaje_id + timestamp`. | 191.710 | 15 | Brecha demostrada: 26 lecturas en límites térmicos y 14 viajes con lecturas en dos particiones. Se registran y no se corrigen en S01. | Grupo 06. |
| DATA-002 | `andinalog_productos_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Un producto. | `producto_id`. | 120 | 7 | Sin brecha demostrada. Diferencia de cobertura: 70 de 120 productos aparecen en telemetría; no es error de calidad. | Grupo 06. |
| DATA-003 | `andinalog_flota_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Un camión. | `camion_id`. | 100 | 6 | Sin brecha demostrada. Diferencia de definición: el centro base no equivale necesariamente al centro operativo; decisión de modelado pendiente, no error de calidad. | Grupo 06. |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Un lote con ingreso, salida y merma. | `lote_id`; `movimiento_id`. | 7.782 | 12 | Sin brecha demostrada. Limitación de alcance: todos los lotes ya salieron y no hay stock vigente; no es error de calidad. | Grupo 06. |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Un centro en un mes. | `centro_distribucion + periodo_mes`. | 144 | 5 | Sin brecha demostrada. Decisión de modelado pendiente: relación temporal con el calendario; no es error de calidad. | Grupo 06. |

### 3.3 WMS como fuente de contraste

WMS no forma parte del inventario principal ni del modelo 03B. Se usa solo para comprobar la lectura orden→centro.

| Fuente | Nombre | Ruta | Grano | Clave | Filas | Columnas | Clasificación | Responsable de revisión |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| DATA-007 | `andinalog_wms_orders_silver.csv` | `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/` | Una orden. | `order_id`. | 30.000 | 16 | Diferencia de cobertura: 22.000 órdenes no tienen telemetría; no es error de calidad y no se carga al modelo. | Grupo 06. |

### 3.4 Procedencia Bronze–Silver

DATA-006 registra la auditoría oficial: 33 registros, de los cuales 5 corresponden a 03B. Se usa para documentar correcciones, recuentos y procedencia. No es una tabla del modelo ni sustituye la evidencia Desktop.

### 3.5 Evidencia esperada

- Registro documental en esta spec y en `docs/context.md`.
- Resultados de controles independientes sobre los CSV.
- Evidencia Desktop por tabla, cuando el Grupo 06 la ejecute.
- Archivo `EV-S01-WMS` en `evidence/S01/wms_contrast.md`, guardado en T02; pendiente de auditoría.
- Copia de SRC-201 en `deliverables/tracking/`, completada solo con campos de S01 durante Build.
- Captura o registro de la brecha DCAM y del componente aplicable. C4 queda respaldado por DEC-026; no se inventan componentes ni se reconstruye documentación reservada.

La evidencia documental no acredita apertura, actualización ni funcionamiento en Power BI Desktop.

## 4. Requisitos funcionales

| ID | Requisito | Hecho cuando |
| --- | --- | --- |
| RF-S01-01 | Registrar decisión, usuaria, frecuencia y criterio de intervención. | La spec indica Jefatura de Operaciones, revisión semanal y qué debe priorizar; distingue información histórica de señales futuras. |
| RF-S01-02 | Definir alcance analítico y preguntas de negocio. | Cada pregunta se relaciona con una tabla o campo y con un KPI candidato; no se promete causalidad. |
| RF-S01-03 | Inventariar las cinco fuentes oficiales con nombre, ruta, grano, clave, filas, columnas, brecha y responsable de revisión. | La tabla 3.2 contiene exactamente DATA-001 a DATA-005; WMS aparece separado como contraste y no se cuenta como sexta fuente del modelo. |
| RF-S01-04 | Registrar la brecha demostrada por tabla o, si no existe, «sin brecha observada» con las comprobaciones y la diferencia pendiente respecto de la guía. | Cada brecha cita campo, evidencia y efecto; si no hay brecha demostrada, se registra «sin brecha observada», las comprobaciones y la diferencia pendiente. No se inventa una brecha ni se convierten diferencias de cobertura, ausencia de stock vigente o decisiones de modelado en errores de calidad. |
| RF-S01-05 | Documentar la preparación inicial y sus límites. | Se registran `RutaSilver`, tipos iniciales, región decimal, fechas y anomalías observadas; no se corrige ni se imputa. |
| RF-S01-06 | Verificar legibilidad en Desktop por tabla. | Existe evidencia de archivo, filas y columnas/encabezados por tabla. En las tablas con columnas decimales se registra al menos un decimal leído o una anomalía regional documentada; en flota se comprueban enteros y fechas y se documenta que no contiene campos decimales. Esto no exime de comprobar archivo, filas y columnas. |
| RF-S01-07 | Evaluar la brecha DCAM priorizada. | Se registran hecho, componente aplicable, dimensión, evidencia, puntaje tentativo y confianza; el componente se identifica y respalda. No se exige evaluar C1–C8 ni reconstruir documentación reservada; si falta respaldo del componente elegido, el criterio sigue pendiente. |
| RF-S01-08 | Proponer KPI candidatos con ficha mínima. | Cada KPI indica pregunta, fórmula, unidad, denominador contextual, fuente, límite y estado; la selección final se difiere a S02 y las metas y umbrales a S08. |
| RF-S01-09 | Completar una copia de la plantilla durante Build y comprobar su correspondencia con Markdown. | La copia de SRC-201 existe en `deliverables/tracking/`, contiene solo los campos de S01 y coincide con esta spec en decisión, fuentes, KPI y brecha; el original permanece intacto. |
| RF-S01-10 | Delimitar la implementación permitida en S01. | Se permiten `RutaSilver`, importación mínima y tipos iniciales; no se crean limpieza, relaciones, medidas ni visuales. El tipado inicial no corrige anomalías regionales. |
| RF-S01-11 | Registrar la procedencia Bronze–Silver. | DATA-006 queda identificada con 33 registros, 5 de 03B, y se distingue de WMS y de la evidencia Desktop. |

## 5. Requisitos no funcionales

| ID | Requisito |
| --- | --- |
| RNF-S01-01 | Trazabilidad: toda afirmación relevante cita fuente, cálculo o decisión; no se inventan páginas, cifras ni componentes. |
| RNF-S01-02 | Separación de estados: dato entregado, cálculo propio, supuesto, referencia docente, propuesta y recomendación se identifican. |
| RNF-S01-03 | Reproducibilidad: rutas relativas en documentación; ruta Silver externa centralizada; conteos y controles repetibles. |
| RNF-S01-04 | Claridad: español para explicaciones, nombres propios en inglés y términos de negocio conservados. |
| RNF-S01-05 | Formato: Markdown como fuente de verdad; copia de plantilla solo en Build; sin duplicar informes completos. |
| RNF-S01-06 | Integridad: no modificar Silver, referencias docentes ni plantillas originales. |
| RNF-S01-07 | Evidencia: distinguir control automático, revisión documental y prueba efectivamente ejecutada en Desktop. |
| RNF-S01-08 | Seguridad: no registrar credenciales, secretos ni datos personales innecesarios. |
| RNF-S01-09 | Honestidad de alcance: no declarar publicación, actualización, entrenamiento, RLS ni validación de negocio no ejecutados. |

## 6. Criterios de aceptación

| ID | Criterio | Evidencia |
| --- | --- | --- |
| CA-S01-01 | Decisión, usuaria, frecuencia y alcance están registrados y son coherentes con la guía S01. | Esta spec y DEC-016. |
| CA-S01-02 | Las cinco fuentes oficiales tienen nombre, ruta, grano, clave, filas, columnas, brecha y responsable de revisión; WMS está separado como contraste. | Sección 3.2, sección 3.3 y `docs/sources.md`. |
| CA-S01-03 | La brecha DCAM está priorizada y el componente aplicable está identificado y respaldado; si falta respaldo, el criterio sigue pendiente. No se exige evaluar C1–C8 ni reconstruir documentación reservada. | Esta spec, DEC-018, DEC-022, DEC-026, SRC-202 y SRC-208. |
| CA-S01-04 | Existe evidencia Desktop por tabla de archivo, filas y columnas/encabezados. En tablas con campos decimales se registra al menos un decimal leído o una anomalía regional documentada; en flota se comprueban enteros y fechas y se documenta que no contiene campos decimales. Una declaración de prueba pendiente no satisface este criterio. | `evidence/S01/`, registro del Grupo 06 y DEC-023. |
| CA-S01-05 | KPI candidatos tienen ficha mínima y límites; la selección final queda para S02, las metas y umbrales para S08, y los responsables empresariales para S11. | Anexo B y DEC-017. |
| CA-S01-06 | La copia de SRC-201 coincide con el Markdown y el original permanece intacto. | `deliverables/tracking/` y comprobación de correspondencia. |

### Condiciones de cierre de S01

S01 no se declara cumplido hasta que se satisfagan CA-S01-01 a CA-S01-06 y se auditen de forma independiente. El componente DCAM y la persona de pantalla quedaron resueltos en DEC-026 y DEC-027; su verificación corresponde a T08. La aprobación de esta spec no sustituye ninguna de estas condiciones.

Los responsables de revisión de S01 son Grupo 06. Los responsables empresariales de KPI se completan progresivamente y la ficha KPI los exige en S11; no son una obligación de cierre de S02.

**Cumplimiento:** CA-S01-01 a CA-S01-06 se demostraron y auditaron de forma independiente. El usuario aprobó el cierre el 2026-10-22 con las limitaciones documentadas en RF-S01-06, RF-S01-07, RF-S01-09, CA-S01-03, CA-S01-04 y CA-S01-06. La aprobación no inicia S02 ni resuelve los pendientes trasladados.

## 7. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
| --- | --- | --- |
| Confundir la aprobación de la spec con el cumplimiento de S01. | Se declararía cumplido un hito con evidencias pendientes. | Mantener estados separados; el cierre exige CA-S01-01 a CA-S01-06 auditados, incluido CA-S01-03 y la designación de pantalla. |
| Convertir diferencias de cobertura, limitaciones o decisiones de modelado en errores de calidad. | Se inventarían brechas y se alteraría la evidencia. | Usar «sin brecha demostrada» y conservar la clasificación de cada diferencia. |
| Atribuir a DATA-006 los cruces WMS. | Procedencia incorrecta y evidencia no reproducible. | Registrar WMS como DATA-007 y los cruces como EV-S01-WMS. |
| Inventar el componente DCAM o una brecha no demostrada. | Pérdida de trazabilidad docente. | No reconstruir C1–C8 ni documentación reservada; registrar el componente y su fuente, o dejarlo pendiente. |
| Corregir anomalías regionales durante el tipado inicial. | Se alteraría el dato sin regla aprobada. | Registrar la anomalía y diferir su tratamiento. |
| Interpretar el porcentaje global de lecturas como concentración o duración. | Conclusión operativa incorrecta. | Analizar junto al porcentaje de viajes, conteos y productos o camiones afectados. |
| Usar WMS como verdad operativa o cargarlo al modelo. | Cambio de alcance y grano. | Mantenerlo solo como contraste y no cargarlo. |
| Asignar a S02 el cierre de responsables empresariales. | Se adelantaría una obligación que corresponde a S11. | Mantener Grupo 06 como revisión de S01 y completar responsables en la ficha de S11. |

## 8. Casos límite y criterios de decisión

- **Tabla sin brecha demostrada:** registrar «sin brecha observada», las comprobaciones realizadas y la diferencia pendiente respecto de la guía. No inventar una brecha ni declarar cumplimiento automático.
- **Diferencia de cobertura:** registrarla como cobertura, no como error de calidad. Ejemplo: 70 de 120 productos en telemetría.
- **Ausencia de stock vigente:** registrarla como limitación de alcance; todos los lotes ya salieron.
- **Decisión de modelado:** registrarla como pendiente; el centro base no demuestra la ruta ni el centro operativo.
- **Anomalía regional:** registrarla con archivo, campo y ejemplo; el tipado inicial no la corrige. Se difiere a una transformación posterior justificada.
- **Valores centinela:** documentarlos; no imputar ni eliminar sin regla aprobada.
- **Duplicados:** usar los conteos de la auditoría oficial; no corregirlos en S01.
- **Lecturas térmicas en límite:** registrar los 26 casos y su tratamiento pendiente; no cambiar etiquetas por suposición.
- **Viajes que cruzan particiones:** registrar las 14 órdenes y sus 339 lecturas; no unirlas sin definir el grano.
- **Futuro incompleto:** no usar información posterior al momento de evaluar una regla de alerta.
- **Centro del viaje:** el centro base del camión no demuestra la ruta real ni el inventario vigente. Su definición permanece pendiente.
- **WMS:** solo contraste orden→centro; no se carga ni se usa para reemplazar telemetría o inventario.
- **Merma:** la medida por cantidades es candidata; la medida económica por valor y su impacto siguen pendientes.
- **KPI sin denominador:** no se publica como porcentaje ni se compara con metas.
- **Componente DCAM sin respaldo:** no se infiere de C1–C8 ni se reconstruye documentación reservada; se registra la dependencia y el criterio queda pendiente.

## 9. Dudas abiertas

| ID | Duda | Qué bloquea | Estado |
| --- | --- | --- | --- |
| DUD-S01-01 | No se dispone de una fuente activa que enumere C1–C8. | El alcance aprobado no exige la lista completa; sí exige identificar y respaldar el componente aplicable a la brecha priorizada. | Resuelta: lista consultada en SRC-208; C4 respaldado por DEC-026. |
| DUD-S01-02 | Falta designar a la persona que compartirá pantalla en S02. | Condición de cierre de S01 y continuidad del hito. | Resuelta: Rodrigo Tucuman, DEC-027. |
| DUD-S01-03 | Faltan los responsables empresariales de KPI. | Se completan progresivamente; la ficha KPI los exige en S11, no en S02. | Abierta. |
| DUD-S01-04 | No existe definición explícita de `centro_distribucion`. | Interpretación de centro, ruta, filtros y RLS. | Abierta; se mantiene como brecha y límite de interpretación. |
| DUD-S01-05 | No se decidió si se añade una medida económica de merma por valor. | Ficha KPI y análisis económico posterior. | Abierta. |
| DUD-S01-06 | El archivo de evidencia EV-S01-WMS se guardó como `evidence/S01/wms_contrast.md` en T02; falta su auditoría. | Demostración reproducible del contraste WMS. | Abierta: archivo disponible; auditoría pendiente. |
| DUD-S01-07 | No se verificó la versión ni la disponibilidad de Power BI Desktop. | Evidencia Desktop y Build. | Abierta. |
| DUD-S01-08 | Faltan rúbrica v4, guías S12–S13 y lista de comisionamiento. | Cumplimiento de requisitos afectados. | Abierta. |

## 10. Cierre y traspaso

**Aprobación:** el usuario aprobó el cierre de S01 el **2026-10-22**, con las limitaciones documentadas y las precisiones de RF-S01-06, RF-S01-07, RF-S01-09, CA-S01-03, CA-S01-04 y CA-S01-06. T10 quedó completada; S02 no se inició.

**Resultado de aceptación:** 26/26 requisitos/criterios pasan (18 `Pasa`, 6 `Pasa con limitación` y 2 `Pasa (ronda 02)`). Las auditorías T08 rondas 01 y 02, la corrección T09 y el hallazgo cerrado A-S01-001 constan en [AUDIT.md](AUDIT.md).

**Entregable y evidencia:** copia `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` con identificación S01, cinco fuentes y cinco KPI; original de SRC-201 intacto. Evidencia en `evidence/S01/`, controles en `validation/` y PBIP mínimo en `powerbi/`.

**Pendientes trasladados, no resueltos:** S02 debe seleccionar los KPI finales 5-8 y precisar fórmula/nivel, semántica de `centro_distribucion`, filtros y RLS, tratamiento de límites térmicos, particiones y WMS, merma por valor, relaciones, medidas, visuales e informe. S08 define metas y umbrales; S11, responsables empresariales y RLS definitiva. Las observaciones de `s01_t05_06` y DUD-S01-07 se mantienen como no bloqueantes.

**Limitación histórica conservada:** la marca `03:08` de `mcp_model_checks.md` no puede releerse porque T09 actualizó el archivo. La verificación actual se apoya en 13/13 huellas y en la reconstrucción exacta de los TMDL históricos; no se usa la hora perdida como prueba.

## Anexo A. Contraste WMS

WMS se usa solo para comprobar la lectura orden→centro. No es una tabla del modelo 03B ni una sexta fuente del inventario principal.

| Comprobación | Resultado |
| --- | --- |
| Estructura | 30.000 filas × 16 columnas; `order_id` único. |
| Cobertura de órdenes de telemetría | 8.000 de 8.000 órdenes cubiertas. |
| Centro WMS frente a centro base del camión | 8.000 de 8.000 coincidencias. |
| Centro de lote, chofer-mes y zona de cliente | 30.000 de 30.000 coincidencias. |
| Órdenes WMS sin telemetría | 22.000; diferencia de cobertura, no error de calidad. |
| Órdenes con lecturas en dos particiones | 14 órdenes, 339 lecturas, 43 positivas. |
| Lecturas en límites térmicos | 26 lecturas, 0,0136 %, 26 viajes; ningún viaje depende solo de ellas. |

Estas comprobaciones son propias y se registran como **EV-S01-WMS**. No se atribuyen a DATA-006, que corresponde a la auditoría Bronze–Silver. El archivo de evidencia se guardó en T02 como `evidence/S01/wms_contrast.md` y queda pendiente de auditoría.

## Anexo B. KPI candidatos

| KPI candidato | Pregunta | Fórmula o unidad | Denominador | Fuente | Decisión y límite |
| --- | --- | --- | --- | --- | --- |
| % de viajes con desviación | ¿Qué proporción de viajes presenta al menos una lectura marcada? | Viajes marcados / viajes observados; porcentaje. | Viajes del contexto analizado; 8.000 es referencia global sin filtros. | DATA-001, DATA-002. | 14,3625 % de referencia. Priorizar productos y camiones con mayor proporción de viajes marcados, junto al porcentaje de lecturas y los conteos. No atribuye causa. |
| % de lecturas con desviación | ¿Qué proporción de observaciones queda marcada? | Lecturas marcadas / lecturas observadas; porcentaje. | Lecturas del contexto analizado; 191.710 es referencia global sin filtros. | DATA-001, DATA-002. | 6,1395 % de referencia. Priorizar productos y camiones con mayor proporción de lecturas marcadas, analizada junto al porcentaje de viajes y los conteos. Es proporción de observaciones; no demuestra duración exacta, intensidad térmica ni cobertura del monitoreo, y por sí solo no permite concluir concentración o dispersión. |
| Merma por cantidades | ¿Cuánta cantidad se pierde? | Suma de `cantidad_merma` / suma de `cantidad_ingreso`; porcentaje. | Suma de `cantidad_ingreso` de los lotes en el contexto. | DATA-004. | 7,3573 % de referencia. Candidata acordada. No equivale a merma por valor; no se usan promedios de porcentajes por lote. |
| % de lotes salidos vencidos | ¿Qué proporción de lotes salió vencida? | Lotes vencidos / lotes salidos; porcentaje. | Lotes salidos en el contexto analizado; 7.782 es referencia global sin filtros. | DATA-004. | 1.069 lotes vencidos; 13,7 % de referencia global. El denominador filtrado debe ser el del contexto, no un total fijo. |
| Días promedio en almacén | ¿Cuánto permanece un lote antes de salir? | Promedio de `dias_en_almacen`. | Lotes con salida en el contexto analizado. | DATA-004. | 38,9805 de referencia, pendiente de validación Desktop. Es permanencia histórica; no es rotación ni causa. |
| Número de lotes vencidos | ¿Cuántos lotes vencidos salieron? | Conteo. | No aplica. | DATA-004. | 1.069. Medida de apoyo, no KPI principal. |

La selección final de 5–8 KPI corresponde a S02. Las metas y umbrales corresponden a S08. Los responsables empresariales de KPI se completan progresivamente y la ficha KPI los exige en S11; los responsables de revisión de S01 son Grupo 06.

Los valores mostrados son referencias calculadas o documentadas, no metas. No se incluye «merma por valor» como KPI candidato; su medida económica sigue pendiente.

## Anexo C. Trazabilidad

| Requisito | Fuente o decisión |
| --- | --- |
| RF-S01-01, RF-S01-02 | SRC-101; DEC-016. |
| RF-S01-03, RF-S01-05 | SRC-101; DATA-001 a DATA-005; DEC-019. |
| RF-S01-04 | SRC-101; DATA-006; controles propios. |
| RF-S01-06 | SRC-101; DEC-023; evidencia Desktop verificada en T05 y auditada en T08. |
| RF-S01-07 | SRC-202; SRC-208; DEC-018; DEC-022; DEC-026. |
| RF-S01-08 | SRC-005; DEC-017; anexo B. |
| RF-S01-09 | SRC-201; DEC-020. |
| RF-S01-10 | SRC-101; DEC-004; límite de Build. |
| RF-S01-11 | DATA-006; SRC-101. |
