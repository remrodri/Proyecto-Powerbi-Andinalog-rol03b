# Spec · S02 — Decisión, arquitectura y mapa Silver

| Campo | Valor |
| --- | --- |
| ID | 002-s02-architecture |
| Hito | S02 — Decisión, arquitectura y mapa Silver del subcaso |
| Versión | 0.4 |
| Fecha | 2026-10-27 |
| Estado de la spec | Aprobada por el usuario el 2026-10-27 |
| Cumplimiento de S02 | Specify, Plan y Build completados; auditoría ejecutada con un hallazgo abierto y una verificación pendiente; S02 no cerrado |
| Entrada | Guía S02 (SRC-102), plantilla de diagrama (SRC-203), plantilla del Proyecto Integrador (SRC-201), catálogo KPI (SRC-005), modelo de referencia 03B (SRC-003), cinco Silver oficiales y traspaso de S01. |
| Salida | Frase de decisión, diagrama de arquitectura, mapa Silver, cinco KPI con nivel táctico, fórmula y unidad, fichas KPI, riesgo/control y pendientes con hito de tratamiento. |
| Fase | Fix pendiente de autorización para A-S02-001; después corresponde una nueva Audit. |

**Aprobación:** el usuario aprobó esta especificación el **2026-10-27**. La aprobación se otorgó tras corregir la v0.3 y añadir una única precisión sobre la frecuencia de `andinalog_inventory_tracking_silver.csv`. Habilita la preparación del Plan de S02; no crea plan, tareas ni auditoría, y no inicia Build.

**Historial de versiones:** v0.1 estableció la base; v0.2 resolvió DUD-S02-01 a DUD-S02-06; v0.3 (2026-10-27) incorporó las cinco correcciones acordadas —tres estados DCAM, nivel táctico de KPI, grano de inventario, columna «Hito de tratamiento» y reformulación del riesgo semántico—; v0.4 (2026-10-27) corrigió el resultado esperado, dejó el mapa con exactamente cinco filas, retiró el linaje inventado, ajustó los hitos de los pendientes y precisó la frecuencia de inventario. No altera las decisiones acordadas.

**Idioma y formato:** contenido en español; nombres de archivos y carpetas en inglés. Markdown es la fuente de verdad. Las plantillas se completan durante Build.

## 1. Contexto y decisión

### 1.1 Hecho que motiva S02

S01 dejó una decisión registrada, cinco fuentes inventariadas, cinco KPI candidatos y una brecha DCAM priorizada. Falta explicar **por dónde viajan los datos** desde el origen hasta el indicador, **qué representa cada fila**, **quién responde por cada tabla** y **qué KPI se seleccionan** con su nivel de decisión.

S02 no construye el tablero ni el modelo relacional. Fija la arquitectura y el mapa Silver que los hitos posteriores implementarán.

### 1.2 Decisión que se apoya

La **Jefatura de Operaciones** decide, con **revisión semanal**, dónde priorizar controles térmicos por producto y camión y qué lotes o centros revisar por vencimiento y merma (DEC-016).

Los cinco KPI seleccionados son **tácticos**: apoyan esa decisión semanal de jefe de área. El nivel no se deduce del detalle de la observación ni del grano de la tabla, sino de quién decide y cada cuánto.

La decisión no autoriza afirmar causalidad, ahorro realizado, ruta real ni inventario vigente.

### 1.3 Preguntas que la spec debe responder

- ¿Quién decide, qué decide y cada cuánto, en una sola frase?
- ¿Cómo se recorre origen → tabla Silver → Power Query → modelo semántico → indicador, partiendo de la brecha DCAM?
- ¿Qué representa una fila de cada tabla y qué columna la identifica?
- ¿Con qué frecuencia se observa el dato y con qué frecuencia se actualiza?
- ¿Quién responde por cada tabla y qué riesgo y control se registran?
- ¿Qué 5–8 KPI se seleccionan, con qué nivel, fórmula en palabras y unidad?
- ¿Cómo se registra la brecha de `centro_distribucion` sin inventar una definición?
- ¿Qué queda pendiente, con qué responsable y en qué hito se trata?

### 1.4 Alcance de esta fase

Documentar la decisión, la arquitectura, el mapa Silver, los KPI seleccionados, el riesgo/control y los pendientes. Se permite inspeccionar fuentes en solo lectura y registrar resultados.

### 1.5 Fuera de alcance en Specify

- Crear o modificar consultas, relaciones, medidas, roles, visuales o el `.pbip`.
- Limpiar, imputar, corregir etiquetas o modificar Silver, referencias o plantillas originales.
- Cargar WMS al modelo.
- Completar metas, umbrales, DAX, RLS o impacto económico.
- Regenerar la copia Excel en lugar de actualizarla.
- Publicar, declarar la sesión compartida ejecutada o presentar pruebas no realizadas.

### 1.6 Límite del Build permitido

El Build de S02 podrá únicamente: completar la segunda diapositiva del diagrama, la hoja `S02 Mapa Silver`, los campos de nivel, fórmula y unidad en `Fichas KPI`, exportar el PDF, guardar la versión editable y registrar pendientes en `evidence/S02/`. No se autorizan cambios en el modelo semántico.

## 2. Objetivo y resultado esperado

**Objetivo:** dejar una arquitectura y un mapa Silver verificables que conecten la decisión semanal con las fuentes reales, sin inventar orígenes, propietarios ni definiciones.

**Resultado esperado de S02:**

1. Frase de decisión con quién decide, qué decide y cada cuánto.
2. Diagrama de arquitectura origen → tabla Silver → Power Query → modelo semántico → indicador, partiendo de la brecha DCAM.
3. Mapa Silver de las cinco fuentes oficiales (DATA-001 a DATA-005) con granularidad, identificador único, frecuencia, propietario, riesgo y control.
4. Fichas de los cinco KPI tácticos con nivel de decisión, fórmula en palabras y unidad.
5. Registro de pendientes con responsable e hito de tratamiento.

**Condición del flujo, no entregable:** la aprobación de esta spec habilita la planificación; no es un producto del hito y no sustituye la demostración de CA-S02-01 a CA-S02-10.

## 3. Fuentes y evidencia

### 3.1 Fuentes principales

| ID | Fuente | Uso en S02 |
| --- | --- | --- |
| SRC-102 | `references/S02/GIAD-M4-S02_Hito_Proyecto_Integrador.docx` | Requisitos y entregables de S02. |
| SRC-203 | `references/S02/GIAD-M4-S02_Plantilla_Diagrama_Arquitectura.pptx` | Plantilla del diagrama; la primera diapositiva es ejemplo y no se entrega. |
| SRC-201 | `references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | Hojas `S02 Mapa Silver`, `Fichas KPI` y `Campos ficha KPI`; su copia se completa en Build. |
| SRC-005 | `references/general/GIAD-M4_Referencia_KPI.docx` | Catálogo de KPI y definiciones. |
| SRC-003 | `references/general/GIAD-M4_PowerBI_Modelo_Relaciones_DAX_Seis_Subcasos_v10.docx` | Modelo, relaciones y valores de referencia del 03B. |
| DATA-001 a DATA-005 | Cinco Silver oficiales | Grano, clave, frecuencia y límites. |
| DATA-006 | `GIAD-M3_v10_auditoria_bronze_silver.csv` | Procedencia; no es tabla del modelo. |
| DATA-007 | `andinalog_wms_orders_silver.csv` | Solo contraste orden→centro; no se carga y no cuenta como sexta fuente oficial. |

### 3.2 Grano, clave y frecuencia

Esta tabla no es el mapa Silver; describe las fuentes y su grano. El mapa se completa en el anexo A.

| ID | Archivo | Grano | Identificador único | Frecuencia de observación | Frecuencia de actualización |
| --- | --- | --- | --- | --- | --- |
| DATA-001 | `andinalog_iot_telemetry_silver.csv` | Una lectura dentro de un viaje (191.710 × 15; 8.000 viajes; 18–30 lecturas por viaje) | `viaje_id` + `minutos_desde_despacho` (alterna `viaje_id` + `timestamp`) | Cada 30 minutos | Por acordar; la entrega es un lote estático |
| DATA-002 | `andinalog_productos_silver.csv` | Un producto (120 × 7) | `producto_id` | Catálogo, sin periodicidad declarada | Por acordar |
| DATA-003 | `andinalog_flota_silver.csv` | Un camión (100 × 6) | `camion_id` | Catálogo, sin periodicidad declarada | Por acordar |
| DATA-004 | `andinalog_inventory_tracking_silver.csv` | **Una fila por lote con ingreso, salida y merma en esta entrega** (7.782 × 12) | `lote_id`; `movimiento_id` también único en esta entrega | Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar | Por acordar |
| DATA-005 | `andinalog_warehouse_costs_silver.csv` | Un centro en un mes (144 × 5; 24 meses, 2024-01 a 2025-12) | `centro_distribucion` + `periodo_mes` | Mensual | Por acordar |
| DATA-007 | `andinalog_wms_orders_silver.csv` | Una orden (30.000 × 16) | `order_id` | Por orden | No aplica: solo contraste, no se carga ni cuenta como sexta fuente oficial |

El grano de inventario es **una fila por lote**, no filas separadas de ingreso y salida. La distinción entre grano, frecuencia de observación y frecuencia de actualización se conserva en el mapa Silver.

DATA-007 se incluye en esta sección solo como referencia de contraste orden→centro documentada en EV-S01-WMS. No forma parte del mapa Silver, no se carga al modelo y no se cuenta como sexta fuente oficial.

### 3.3 Arquitectura de referencia

Flujo de cinco cajas por cadena: **origen → tabla Silver → Power Query → modelo semántico → indicador**.

| Caja | Contenido verificable | Límite |
| --- | --- | --- |
| Origen | **No documentado por archivo; «por acordar».** Los nombres de los CSV no demuestran el sistema que los generó. | No se atribuye ERP, WMS, TMS ni telemetría a ninguna tabla. |
| Tabla Silver | Cinco CSV oficiales v10 | WMS queda fuera del modelo y solo se usa como contraste. |
| Power Query | `RutaSilver`, `File.Contents`, `Csv.Document`, `Encabezados`, `Tipado` | Ya construido en S01; S02 no lo modifica. |
| Modelo semántico | Cinco tablas Import; dimensiones y relaciones **propuestas** | 0 relaciones, 0 medidas, 0 roles en el estado actual; el modelo relacional es S06. |
| Indicador | Cinco KPI tácticos seleccionados | Sin metas, umbrales ni DAX en S02. |

**Nota separada — contexto del dossier, no linaje:** el dossier describe un ERP con parametrización inconsistente, WMS parcial en dos centros y ausencia de TMS. Es contexto empresarial general; no demuestra el origen de estos archivos y no se usa para completar la caja Origen ni la columna Propietario.

### 3.4 Evidencia esperada

- `deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf`: diagrama en una página y mapa en las páginas necesarias.
- Versión editable `.pptx` en `deliverables/S02/`.
- Actualización de `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` con hash antes y después; original `0CCC4A53…D2DF30` intacto.
- Registro en `evidence/S02/` de lo ejecutado, lo revisado y lo pendiente.

La evidencia documental no acredita apertura de Desktop, actualización, publicación ni sesión compartida.

## 4. Requisitos funcionales

| ID | Requisito | Hecho cuando |
| --- | --- | --- |
| RF-S02-01 | Cerrar la decisión en una frase con quién decide, qué decide y cada cuánto. | Una sola frase indica Jefatura de Operaciones, revisión semanal y las prioridades de DEC-016, sin atribuir causalidad. |
| RF-S02-02 | Dibujar el flujo origen → Silver → Power Query → modelo semántico → indicador partiendo de la brecha DCAM. | La segunda diapositiva contiene las cinco cajas; cada caja nombra un artefacto real; el origen no documentado se marca «por acordar»; WMS queda fuera del modelo. |
| RF-S02-03 | Completar el mapa Silver con exactamente las cinco fuentes oficiales y las siete columnas de la plantilla. | Archivo, granularidad, identificador único, frecuencia, propietario, riesgo y control están completos para DATA-001 a DATA-005; el mapa tiene exactamente cinco filas; grano y clave coinciden con S01; se distinguen frecuencia de observación y de actualización; en inventario la frecuencia se registra como «Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar»; el propietario desconocido se registra «por acordar» o como revisión del Grupo 06, sin inventarlo; DATA-007 se registra fuera del mapa como fuente de contraste que no se carga ni cuenta como sexta fuente. |
| RF-S02-04 | Registrar la brecha DCAM en uno de tres estados admitidos. | El estado es (a) definición respaldada con fuente citada; (b) definición propuesta marcada como provisional y pendiente de validación; o (c) ausencia documentada con usos, límites conocidos y solicitud concreta de definición y validación. Se registra el estado de validación y el seguimiento del Grupo 06; no se inventa definición; no se declara resuelta la brecha; `dim_centro` y los controles de claves se presentan solo como propuestas complementarias. |
| RF-S02-05 | Vincular el riesgo principal y su control a la brecha priorizada. | El riesgo y el control responden a la brecha; el control se describe como propuesto, no aplicado; lo no demostrado queda como pendiente con responsable. |
| RF-S02-06 | Seleccionar de 5 a 8 KPI y completar nivel, fórmula en palabras y unidad. | Se seleccionan entre 5 y 8 KPI del catálogo SRC-005; los cinco heredados figuran como **tácticos** porque apoyan la decisión semanal de la Jefatura de Operaciones; el detalle de la observación no se usa para fijar el nivel; cada KPI tiene fórmula sin ambigüedad y unidad. |
| RF-S02-07 | Mantener coherencia con S01 y DEC-017. | Nombres, fórmulas, denominadores contextuales y límites coinciden con el anexo B de S01; no se incorpora «merma por valor» como KPI; las referencias numéricas se citan como líneas base, no como metas. |
| RF-S02-08 | Completar las fichas KPI en la copia de trabajo sin regenerar la plantilla. | Las filas 7–11 de `Fichas KPI` completan nivel de decisión, fórmula en palabras y unidad; se conservan las 50 fórmulas, validaciones, formato condicional, celdas combinadas y hojas futuras; SRC-201 permanece intacto. |
| RF-S02-09 | Producir el diagrama y el mapa en los entregables exigidos. | El PDF `deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf` contiene el diagrama en una página y el mapa en las páginas necesarias; existe versión editable en `deliverables/S02/`. |
| RF-S02-10 | Registrar la ejecución real y su evidencia. | `evidence/S02/` distingue archivo generado, revisión visual y prueba no ejecutada; se indica si la sesión se realizó, con fecha y quién compartió pantalla, o queda pendiente; no se declara una sesión no ejecutada. |
| RF-S02-11 | Registrar los pendientes con responsable e «Hito de tratamiento». | Cada pendiente indica si S02 lo documenta o si su resolución se traslada, el responsable y el hito de tratamiento según las guías y decisiones existentes; si no hay respaldo, «por acordar»; registrar no equivale a resolver. |

## 5. Requisitos no funcionales

| ID | Requisito |
| --- | --- |
| RNF-S02-01 | Trazabilidad: toda afirmación cita fuente, cálculo o decisión; no se inventan páginas, cifras, orígenes ni propietarios. |
| RNF-S02-02 | Separación de estados: dato entregado, cálculo propio, supuesto, referencia docente, propuesta y recomendación se identifican. |
| RNF-S02-03 | Reproducibilidad: rutas relativas en documentación; `RutaSilver` centralizada; conteos y controles repetibles. |
| RNF-S02-04 | Claridad: español para explicaciones, nombres propios en inglés y términos de negocio conservados. |
| RNF-S02-05 | Formato: Markdown como fuente de verdad; la plantilla se completa solo en Build; sin duplicar informes completos. |
| RNF-S02-06 | Integridad: no modificar Silver, referencias docentes ni plantillas originales. |
| RNF-S02-07 | Evidencia: distinguir control automático, revisión documental y prueba efectivamente ejecutada. |
| RNF-S02-08 | Seguridad: no registrar credenciales, secretos ni datos personales innecesarios. |
| RNF-S02-09 | Honestidad de alcance: no declarar sesión compartida, publicación, actualización, DAX ni RLS no ejecutados. |

## 6. Criterios de aceptación

| ID | Criterio | Evidencia |
| --- | --- | --- |
| CA-S02-01 | La decisión está en una frase con quién, qué y cada cuánto, coherente con DEC-016. | Sección 1.2 y entregable S02. |
| CA-S02-02 | El diagrama tiene las cinco cajas por cadena, parte de la brecha DCAM y no inventa el origen. | SRC-203, segunda diapositiva y PDF. |
| CA-S02-03 | El mapa Silver contiene exactamente cinco filas, DATA-001 a DATA-005, con granularidad, identificador, frecuencia, propietario, riesgo y control; WMS queda fuera del mapa y solo como contraste. | Hoja `S02 Mapa Silver` y anexo A. |
| CA-S02-04 | El riesgo principal y su control responden a la brecha; el control es propuesto y los pendientes tienen responsable. | Sección 7 y entregable. |
| CA-S02-05 | La brecha DCAM se registra en uno de los tres estados admitidos, con estado de validación y seguimiento; no se inventa definición ni se declara resuelta. | Sección 8, DUD-S02-07 y DEC-018/DEC-026. |
| CA-S02-06 | Se seleccionan 5–8 KPI con nivel táctico justificado, fórmula en palabras y unidad; sin metas, umbrales ni DAX. | Anexo B y hoja `Fichas KPI`. |
| CA-S02-07 | Los KPI son coherentes con S01 y DEC-017; no se incluye merma por valor como KPI. | Anexo B, anexo B de S01 y DEC-017. |
| CA-S02-08 | La copia Excel conserva fórmulas, validaciones y hojas futuras; el original permanece intacto. | Hash antes/después y `evidence/S02/`. |
| CA-S02-09 | El PDF contiene el diagrama en una página y el mapa en las páginas necesarias; existe versión editable. | `deliverables/S02/`. |
| CA-S02-10 | Los pendientes indican documentado/trasladado, responsable e «Hito de tratamiento», con «por acordar» cuando no hay respaldo. | Sección 8.3 y anexo A de pendientes. |

### Condiciones de cierre de S02

S02 no se declara cumplido hasta que CA-S02-01 a CA-S02-10 se demuestren y se auditen de forma independiente. La aprobación de esta spec no sustituye esa condición. La ausencia de validador empresarial para `centro_distribucion` no bloquea el cierre si se registra como ausencia documentada.

## 7. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
| --- | --- | --- |
| **Interpretar incorrectamente qué representa el centro y usarlo en filtros o conclusiones.** | Se atribuirían viajes, lotes o costos a un centro equivocado. | Registrar el estado de definición y sus límites; no usar el centro base como ruta real; los cruces no hallaron discrepancias entre centro WMS y centro base en los 8.000 viajes emparejados, pero **esa consistencia no acredita el significado empresarial**; no presentar una asignación incorrecta como hallazgo observado. |
| Declarar la sesión compartida sin haberla ejecutado. | Evidencia falsa y pérdida de trazabilidad. | RF-S02-10: registrar solo lo realizado; lo demás queda pendiente. |
| Inventar propietarios u orígenes a partir de los nombres de archivo. | Mapa Silver no verificable. | «Por acordar» y revisión del Grupo 06; origen marcado como no documentado. |
| Confundir frecuencia de observación con frecuencia de actualización. | Lectura operativa errónea del mapa. | Dos campos separados en la sección 3.2 y en la hoja. |
| Asignar el nivel de KPI por el detalle de la observación. | Clasificación incorrecta del indicador. | Los cinco KPI son tácticos por la decisión semanal; el grano no determina el nivel. |
| Separar ingreso y salida en filas distintas de inventario. | Cambio de grano y duplicación de lotes. | Una fila por lote con ingreso, salida y merma en esta entrega. |
| Presentar un pendiente registrado como resuelto. | Se declararía cerrado lo que solo se documentó. | Columna «Hito de tratamiento» y distinción documentado/trasladado. |
| Regenerar la copia Excel. | Pérdida de fórmulas y formato condicional. | Actualizar la copia existente y conservar hash. |
| Cargar WMS o usarlo como verdad operativa. | Cambio de alcance y grano. | WMS solo contraste, fuera del modelo y del mapa. |

## 8. Casos límite y criterios de decisión

- **Definición de centro respaldada:** solo si existe fuente citada y verificable; se registra la fuente y el estado de validación.
- **Definición provisional:** se marca como propuesta, pendiente de validación, y no se usa para afirmar significado empresarial.
- **Ausencia documentada:** se registran usos, límites conocidos y una solicitud concreta de definición y validación; no se declara resuelta la brecha.
- **`dim_centro` y controles de claves:** solo propuestas complementarias; no sustituyen la definición del campo ni se presentan como aplicados.
- **Consistencia de centros:** 8.000 de 8.000 coincidencias entre centro WMS y centro base; acredita consistencia de lectura, no significado.
- **Inventario:** una fila por lote; sin periodicidad fija; todos los lotes salieron y no hay stock vigente en esta entrega.
- **Telemetría:** clave compuesta y 18–30 lecturas por viaje; no existe tabla de viajes.
- **Costos:** grano centro–mes; la relación temporal con el calendario se decide en S06.
- **Propietario desconocido:** «por acordar»; el Grupo 06 es responsable de revisión, no propietario de negocio (DEC-020).
- **Merma:** por cantidades es KPI; por valor queda pendiente y no se suma como si fuera el mismo concepto.
- **WMS:** solo contraste orden→centro; no se carga y no cuenta como sexta fuente.

### 8.3 Pendientes con hito de tratamiento

| Pendiente | Estado al cierre de S02 | Responsable | Hito de tratamiento |
| --- | --- | --- | --- |
| Definición y validación de `centro_distribucion` y `centro_distribucion_base` | Documentado como ausencia; no resuelto | Grupo 06; validador por acordar | S02 (documentación), S06 (filtros) y S11 (RLS) |
| Selección final de KPI | Resuelta en S02: cinco KPI tácticos | Grupo 06 | S02 |
| Metas y umbrales | Trasladado | Por acordar | S08 |
| Responsables empresariales de KPI | Trasladado | Por acordar | S11 |
| Roles y pruebas RLS | Trasladado | Por acordar | S11 |
| Merma por valor | Documentada como pendiente; no es KPI | Por acordar | Por acordar; impacto económico en S10 |
| 26 lecturas en límites térmicos | Trasladado | Grupo 06 | S04 |
| Particiones y horizonte futuro | Trasladado | Grupo 06 | S04 y S10 |
| Relación temporal de costos | Trasladado | Grupo 06 | S06 |
| Origen de los sistemas y propietarios de las fuentes | Documentado como no disponible; no resuelto | Grupo 06 documenta; propietario por acordar | Por acordar |
| Frecuencia de actualización | Documentada como «por acordar»; no resuelta | Por acordar | Por acordar |
| Sesión compartida de S02 (Rodrigo Tucuman) | No ejecutada ni declarada | Rodrigo Tucuman | S02 |
| Publicación en Service | Prevista, no ejecutada | Por acordar | S11 y entrega final |

S02 documenta el origen, los propietarios y la frecuencia de actualización, pero documentarlos no los resuelve. La guía S03 exige conector, parámetro, privacidad, perfil, excepciones y tablas fuente por KPI; no exige propietario empresarial ni frecuencia de actualización, por lo que no se les asigna ese hito.

## 9. Dudas abiertas

| ID | Duda | Qué bloquea | Estado |
| --- | --- | --- | --- |
| DUD-S02-01 | ¿Cómo se reúnen el mapa del Excel y el diagrama en un solo PDF? | Formato del entregable. | Resuelta: diagrama en una página y mapa en las páginas necesarias del mismo PDF. |
| DUD-S02-02 | ¿Qué representa `centro_distribucion`? | Filtros, ruta, inventario y RLS. | Abierta; se registra como ausencia documentada. No se resuelve en S02. |
| DUD-S02-03 | ¿Quién es el propietario de cada fuente? | Columna «Propietario» del mapa. | Abierta: «por acordar»; el Grupo 06 solo revisa. |
| DUD-S02-04 | ¿Cuál es la frecuencia de actualización de cada tabla? | Columna «Frecuencia». | Abierta: se distingue de la observación y se marca «por acordar». |
| DUD-S02-05 | ¿Qué KPI se seleccionan y con qué nivel? | Cierre de la ficha KPI. | Resuelta: cinco KPI, nivel táctico. |
| DUD-S02-06 | ¿Se incorpora merma por valor como KPI? | Catálogo final. | Resuelta: no; queda pendiente económica. |
| DUD-S02-07 | No está identificado el validador empresarial del significado de `centro_distribucion` y `centro_distribucion_base`. | Declarar la definición como respaldada o validada. | **Decidida su forma de registro: ausencia documentada.** No bloquea el cierre; no se declara resuelta la brecha. |

## 10. Cierre y traspaso

S02 no se inicia hasta que esta spec sea aprobada. Al cierre deberá dejar: frase de decisión, diagrama, mapa Silver, cinco KPI tácticos con fichas completas en nivel/fórmula/unidad, riesgo/control, pendientes con hito y evidencia en `evidence/S02/`.

**Traspaso previsto:** S03 recibe el mapa y las frecuencias; S04, los límites térmicos y las particiones; S06, `dim_centro`, filtros y relación temporal de costos; S08, metas y umbrales; S10, impacto económico; S11, responsables y RLS.

## Anexo A. Mapa Silver propuesto

| Archivo / tabla | Granularidad | Identificador único | Frecuencia | Propietario | Riesgo | Control propuesto |
| --- | --- | --- | --- | --- | --- | --- |
| `andinalog_iot_telemetry_silver.csv` | Una lectura dentro de un viaje | `viaje_id` + `minutos_desde_despacho` | Observación cada 30 min; actualización por acordar | Por acordar; revisión Grupo 06 | Interpretar el centro del camión como centro real del viaje | Documentar el límite y no usar el centro base como ruta; control de clave compuesta |
| `andinalog_productos_silver.csv` | Un producto | `producto_id` | Catálogo; actualización por acordar | Por acordar; revisión Grupo 06 | Extrapolar KPI térmicos a todo el catálogo | Registrar cobertura 70 de 120 en telemetría |
| `andinalog_flota_silver.csv` | Un camión | `camion_id` | Catálogo; actualización por acordar | Por acordar; revisión Grupo 06 | Usar `centro_distribucion_base` como centro operativo | Mantener la distinción base/operativo y registrarla como pendiente |
| `andinalog_inventory_tracking_silver.csv` | Un lote con ingreso, salida y merma en esta entrega | `lote_id`; `movimiento_id` único en esta entrega | Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar | Por acordar; revisión Grupo 06 | Leer vencimiento como stock vigente | Declarar que todos los lotes salieron; KPI históricos |
| `andinalog_warehouse_costs_silver.csv` | Un centro en un mes | `centro_distribucion` + `periodo_mes` | Mensual; actualización por acordar | Por acordar; revisión Grupo 06 | Asignar costos a productos sin regla | No asignar; relación temporal en S06 |

**Nota fuera del mapa:** DATA-007 `andinalog_wms_orders_silver.csv` no forma parte de este mapa ni del modelo semántico. Se conserva solo como fuente de contraste orden→centro (EV-S01-WMS), no se carga y no se cuenta como sexta fuente oficial.

## Anexo B. KPI seleccionados (tácticos)

| # | KPI | Nivel | Fórmula en palabras | Unidad | Denominador | Referencia |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | % de viajes con desviación | Táctico | Viajes con al menos una lectura marcada / viajes observados × 100 | Porcentaje | Viajes del contexto | 14,3625 % global |
| 2 | % de lecturas con desviación | Táctico | Lecturas marcadas / lecturas observadas × 100 | Porcentaje | Lecturas del contexto | 6,1395 % global |
| 3 | Merma por cantidades | Táctico | Suma de `cantidad_merma` / suma de `cantidad_ingreso` × 100 | Porcentaje | Suma de `cantidad_ingreso` del contexto | 7,3573 % |
| 4 | % de lotes salidos vencidos | Táctico | Lotes con salida posterior al día de vencimiento / lotes salidos × 100 | Porcentaje | Lotes salidos del contexto | 1.069 de 7.782; 13,7 % |
| 5 | Días promedio en almacén | Táctico | Promedio de `dias_en_almacen` | Días | Lotes con salida en el contexto | 38,9805 |

**Medida de apoyo:** número de lotes vencidos (conteo; 1.069). No es KPI principal.

Los cinco son tácticos porque apoyan la decisión semanal de la Jefatura de Operaciones. Las referencias son líneas base, no metas. Metas y umbrales: S08. DAX: S07. Responsables empresariales: S11.

`dias_en_almacen` se conserva exactamente como nombre de columna, sin tilde y sin cambio de identificador; la tilde permanece solo en el nombre visible del KPI.

## Anexo C. Trazabilidad

| Requisito | Fuente o decisión |
| --- | --- |
| RF-S02-01, CA-S02-01 | SRC-102; DEC-016. |
| RF-S02-02, RF-S02-09 | SRC-102; SRC-203; SRC-003. |
| RF-S02-03 | SRC-102; SRC-201; DATA-001 a DATA-005; DEC-020; DEC-032. |
| RF-S02-04, CA-S02-05 | SRC-102; DEC-018; DEC-026; DEC-031; DUD-S02-07. |
| RF-S02-05, CA-S02-04 | SRC-102; brecha A de S01. |
| RF-S02-06, CA-S02-06 | SRC-102; SRC-005; DEC-016; DEC-017; DEC-030. |
| RF-S02-07, CA-S02-07 | DEC-017; anexo B de S01. |
| RF-S02-08, CA-S02-08 | SRC-201; DEC-020. |
| RF-S02-10, RF-S02-11, CA-S02-10 | SRC-102; guías S03–S11; DEC-027; DEC-029. |
