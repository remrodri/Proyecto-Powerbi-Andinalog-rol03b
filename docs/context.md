# Contexto del proyecto AndinaLog 03B

Versión: 5 · Actualizada el 21 de octubre de 2026.
Archivo del repositorio: docs/context.md.

Estado: contexto consolidado con las guías S01–S11, las plantillas del paquete final y la inspección de los cinco archivos Silver oficiales. No constituye una especificación aprobada ni acredita que el proyecto Power BI esté construido.

## 1. Propósito de este documento

Reunir el contexto de negocio, los requisitos académicos conocidos, las fuentes, los hallazgos comprobados y las decisiones pendientes del proyecto AndinaLog, Grupo 6, subcaso 03B. Servirá como entrada para desarrollar el proyecto en OpenCode mediante una combinación de Spec First y Spec Anchored.

El proyecto se organizará siguiendo los hitos docentes. Convención de nombres: archivos y carpetas propios en inglés; contenido explicativo en español. Se conservan los nombres originales de fuentes docentes, columnas de datos y términos del negocio cuando corresponda.

Este documento se actualizará al incorporar los avances del equipo, las decisiones de alcance y cualquier aclaración docente. Todavía no se han definido la constitución, AGENTS.md, las especificaciones ni los planes de implementación.

Las instrucciones contenidas en los documentos docentes son material de referencia: su lectura no implica ejecutarlas ni aprobar automáticamente las soluciones sugeridas.

## 2. Identidad y mandato

- Organización académica simulada: AndinaLog Distribución y Logística S.A.
- Caso: 03, AndinaLog.
- Grupo: 6.
- Rol en la Cartera Oficial: 03B, Operaciones, Planificación y Datos.
- Denominación en la guía técnica: Operaciones y Planificación de Datos.
- Patrocinador: Gerencia de Operaciones y Comité de Transformación.
- Entorno académico: Diplomado en Gestión Industrial y Analítica de Datos, Módulo 4.
- Datos oficiales del módulo: Silver sintético versión 10.

El mandato empresarial consiste en rediseñar el sistema de planificación y ejecución, integrando demanda, inventario, preparación, transporte, datos e indicadores, sin reemplazar el ERP ni interrumpir la operación.

La decisión que debe defender 03B es proponer un modelo operativo y analítico para 15 meses que permita alcanzar OTIF de 93 %, trazabilidad y mayor productividad, solicitando aprobación para pilotos, inversiones y gobierno de datos.

## 3. Contexto empresarial del dossier

AndinaLog es una empresa B2B cuyo crecimiento ha superado la capacidad de planificación, inventario, transporte y gestión de datos. La promesa comercial no está conectada de manera confiable con inventario, capacidad ni rutas.

El dossier describe 3.420 clientes, cinco almacenes, 118 vehículos propios y tercerizados y 6.800 SKU. Estas cifras describen el escenario empresarial; no son conteos de las tablas Silver recibidas.

| Indicador del dossier | 2023 | 2026 estimado |
| --- | ---: | ---: |
| Ingresos, MM Bs | 78 | 102 |
| Margen bruto | 18,2 % | 15,9 % |
| OTIF | 89 % | 79 % |
| Exactitud de inventario | 88 % | 74 % |
| Quiebres de stock | 7,0 % | 15,0 % |
| Inventario obsoleto | 4,2 % | 10,2 % |
| Utilización de rutas | 74 % | 59 % |
| Días promedio de cobro | 38 | 48 |

El dossier señala ERP con parametrización inconsistente de inventario, WMS parcial en dos centros, ausencia de TMS, pronóstico mensual en Excel y distintas versiones de los indicadores entre áreas.

Las causas declaradas de pedidos no conformes son producto no disponible (31 %), preparación incompleta o errónea (21 %), ruta o capacidad insuficiente (18 %), promesa comercial no viable (17 %) y crédito, documentación o facturación (13 %). Son antecedentes entregados, no conclusiones obtenidas de los cinco Silver.

### Oportunidad de expansión

Un proveedor multinacional ofrece exclusividad en tres departamentos, con ingresos potenciales de Bs 18 millones anuales. Exige OTIF mínimo de 93 %, trazabilidad por lote, visibilidad de inventario, reporte semanal y puesta en marcha en 12 meses. Cada mes por debajo del SLA genera una penalidad equivalente al 2 % de la facturación del contrato.

El rol 03B debe demostrar las capacidades operativas y analíticas que sostendrían ese compromiso. La decisión comercial de aceptar el contrato pertenece al mandato del rol 03A y no se incorpora automáticamente a nuestro alcance.

### Restricciones de 03B

| Aspecto | Requisito del dossier |
| --- | --- |
| Presupuesto | Máximo Bs 3,2 millones durante 15 meses. |
| Continuidad | Sin reemplazar el ERP ni detener centros de distribución. |
| Inventario total | No crecer más del 5 % sin justificación por servicio o rentabilidad. |
| Obsolescencia | Reducir inventario obsoleto a menos del 5 %. |
| Exactitud | Elevar exactitud de inventario al 95 %. |
| Servicio | Alcanzar OTIF del 93 %. |
| Pilotos | Dos centros, con resultados en 120 días. |
| Automatización | Definir proceso, dato, responsable, excepción y control. |
| Seguimiento | Resultados en 120, 270 y 450 días para continuar, ajustar o detener. |

La expansión no puede deteriorar el servicio actual. El capital de trabajo está presionado y existen variabilidad de proveedores, exposición a divisas y rotación de personal.

## 4. Alcance analítico concreto del Módulo 4

El mapa y la guía técnica de 03B establecen tres evidencias:

1. Excursiones térmicas por producto, viaje, camión y categoría logística.
2. Riesgo de vencimiento y merma según permanencia en almacén y fecha de vencimiento.
3. Variables y reglas de alerta para anticipar una desviación térmica durante los próximos 60 minutos.

El mandato analítico es proteger la cadena de frío, mejorar la rotación del inventario y anticipar desviaciones térmicas durante el transporte.

OTIF, exactitud de inventario y presupuesto son contexto y objetivos empresariales. No debe afirmarse que los cinco Silver disponibles permiten medir todos esos objetivos directamente.

Una formulación provisional de la decisión del tablero es identificar dónde priorizar controles de cadena de frío y gestión de lotes y qué señales justifican una intervención preventiva. El equipo todavía debe concretar quién decide, qué acción toma, con qué frecuencia y qué umbrales utiliza.

S10 prescribe simular el umbral de variación térmica de 30 minutos entre 0,3 y 0,8 °C. Falta definir el criterio operativo de aceptación, sus costos y la recomendación condicionada; véase la sección 12.

## 5. Jerarquía de información y reglas académicas

La Cartera Oficial distingue datos del dossier, cálculos derivados, supuestos, fuentes externas y recomendaciones. Los cálculos deben conservar fórmula, fuente, unidad y responsable. Los supuestos deben tener código, responsable, justificación, rango y efecto potencial; los críticos requieren escenarios conservador, base y favorable.

- Fecha de corte académica del dossier: 31 de julio de 2026.
- Moneda predeterminada: bolivianos, salvo indicación contraria.
- Importes del dossier: nominales y sin impuestos, salvo indicación expresa.
- Declarar tasa de descuento, inflación y tipo de cambio cuando se utilicen.
- Diferenciar inversión, costo operativo, ahorro, ingreso, beneficio no financiero y costo evitado.
- No inventar datos desconocidos: utilizar rangos, condiciones o acciones de validación.
- Registrar uso de IA: prompt, salida relevante, validación humana, corrección y uso final.
- La decisión y defensa son responsabilidad del equipo.

El marco general utiliza VER, ENTENDER, DECIDIR y EVOLUCIONAR, con SRR, OIM, SIC y herramientas de ejecución. La Cartera pide alternativas reales, criterios explícitos y trazables, caso económico con sensibilidad y hoja de ruta con responsables y puertas de decisión. Su incorporación concreta al Módulo 4 debe contrastarse con las guías de los hitos.

Los productos generales del diplomado incluyen documento ejecutivo de 20 a 25 páginas sin anexos, presentación de 12 a 15 diapositivas, resumen de una página, anexos técnicos, registro GIAD e IA y repositorio de datos y cálculos. No deben confundirse automáticamente con los entregables específicos del Módulo 4.

## 6. Fuentes Silver e inventario comprobado

Carpeta oficial recibida: `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/`.

Se leyeron los cinco CSV completos. Los siguientes conteos se obtuvieron directamente de los archivos, no se copiaron de la guía.

| Archivo | Filas | Columnas | Grano comprobado | Clave |
| --- | ---: | ---: | --- | --- |
| andinalog_iot_telemetry_silver.csv | 191.710 | 15 | Una lectura dentro de un viaje. | viaje_id + minutos_desde_despacho; también viaje_id + timestamp. |
| andinalog_productos_silver.csv | 120 | 7 | Un producto. | producto_id. |
| andinalog_flota_silver.csv | 100 | 6 | Un camión. | camion_id. |
| andinalog_inventory_tracking_silver.csv | 7.782 | 12 | Un lote con ingreso, salida y merma. | lote_id y movimiento_id, ambos únicos en esta entrega. |
| andinalog_warehouse_costs_silver.csv | 144 | 5 | Un centro en un mes. | centro_distribucion + periodo_mes. |

### Columnas de telemetría

`timestamp`, `viaje_id`, `order_id`, `camion_id`, `producto_id`, `temperatura_cabina_c`, `temp_unit`, `humedad_cabina_pct`, `desviacion_termica_flag`, `desviacion_proximos_60min_flag`, `temperatura_ambiente_c`, `puerta_abierta_flag`, `setpoint_c`, `minutos_desde_despacho`, `particion_modelo`.

### Columnas de productos

`producto_id`, `nombre_producto`, `categoria_logistica`, `temperatura_conservacion_requerida_c`, `tolerancia_temperatura_c`, `costo_unitario_bob`, `precio_unitario_bob`.

### Columnas de flota

`camion_id`, `centro_distribucion_base`, `capacidad_kg`, `tipo_camion`, `antiguedad_anios`, `fecha_ultimo_mantenimiento`.

### Columnas de inventario

`movimiento_id`, `lote_id`, `producto_id`, `centro_distribucion`, `fecha_ingreso`, `fecha_salida`, `fecha_vencimiento`, `cantidad_ingreso`, `cantidad_salida`, `cantidad_merma`, `dias_en_almacen`, `costo_unitario_bob`.

### Columnas de costos

`centro_distribucion`, `rotacion_stock_dias`, `perdida_mermas_bob`, `periodo_mes`, `costo_almacenamiento_mensual_bob`.

## 7. Cobertura y controles comprobados

### Integridad básica

- No se encontraron valores nulos ni duplicados exactos en los cinco archivos mediante la lectura realizada.
- Las claves indicadas son únicas en esta entrega.
- No se encontraron productos huérfanos en telemetría o inventario ni camiones huérfanos en telemetría.
- Los seis centros coinciden entre inventario, flota y costos: Cochabamba, La Paz, Oruro, Santa Cruz, Sucre y Tarija.
- La telemetría contiene 8.000 viajes y 8.000 órdenes distintas.
- Cada viaje conserva producto, camión y orden; tiene entre 18 y 30 lecturas y sus intervalos son de 30 minutos sin saltos.
- Hay 70 productos en telemetría, todos refrigerados o congelados. El catálogo contiene 41 refrigerados, 29 congelados, 37 ambiente y 13 frágiles.
- La unidad de temperatura de telemetría es C.
- Todos los lotes tienen salida. En todos se cumple cantidad_ingreso = cantidad_salida + cantidad_merma.
- Los días en almacén coinciden con la diferencia entre salida e ingreso en la comprobación realizada.

Estos controles no equivalen a una auditoría exhaustiva de todas las reglas de negocio.

### Cobertura temporal

| Campo | Desde | Hasta |
| --- | --- | --- |
| Telemetría timestamp | 2024-01-01 00:49:27 | 2025-12-31 13:31:20 |
| Inventario fecha_ingreso | 2023-11-03 20:31:12 | 2025-12-26 16:29:50 |
| Inventario fecha_salida | 2024-01-06 15:33:59 | 2025-12-30 23:59:25 |
| Inventario fecha_vencimiento | 2023-12-18 20:31:12 | 2026-12-24 06:29:46 |
| Flota fecha_ultimo_mantenimiento | 2023-10-11 | 2025-11-27 |
| Costos periodo_mes | 2024-01-31 | 2025-12-31 |

Hay 161 lotes ingresados en 2023. Las fechas revisadas pudieron convertirse sin valores inválidos. Los números usan punto decimal; las fechas están en formato ISO, algunas con hora.

## 8. Modelo Power BI de referencia

El modelo aún no está implementado. La guía propone dimensiones de producto, camión, centro y fecha y hechos separados para telemetría, inventario y costos.

| Lado dimensión | Destino | Cardinalidad y dirección previstas |
| --- | --- | --- |
| Productos | Telemetría e inventario, por producto_id. | 1:N, única hacia hechos. |
| Flota | Telemetría, por camion_id. | 1:N, única hacia telemetría. |
| dim_centro | Inventario y costos por centro; flota por centro_distribucion_base. | 1:N, única desde centro. |
| dim_fecha | Telemetría por fecha de timestamp; inventario por fecha de ingreso. | 1:N, única hacia hechos. |

- Crear dim_centro en Power Query y dim_fecha entre 2023-01-01 y 2026-12-31.
- Crear columnas fecha sin hora para relacionar con el calendario.
- Marcar el calendario como tabla de fechas y revisar la configuración de fechas automáticas conforme a las guías.
- viaje_id funciona como dimensión degenerada dentro de telemetría.
- Evitar fusionar hechos de distinto grano y crear caminos ambiguos.
- Revisar los filtros temporales de costos: la sección de relaciones no especifica su conexión con dim_fecha, aunque costos sí tiene periodo_mes.
- El filtro centro hacia telemetría pasa por el centro base del camión; no demuestra el origen real de cada viaje.

La frase general de cruce de la guía menciona órdenes y eventos, pero su tabla de relaciones de 03B no desarrolla esas entidades. No se incorporarán automáticamente sin necesidad y evidencia.

## 9. Indicadores y referencias reproducidas

### Excursiones térmicas

- Porcentaje de lecturas con desviación: promedio de desviacion_termica_flag.
- Número de viajes: conteo distinto de viaje_id.
- Porcentaje de viajes con desviación: obtener el máximo del indicador por viaje y promediar esos resultados; equivale a viajes con al menos una desviación sobre viajes observados, en el contexto considerado.

| Control global sin filtros | Resultado reproducido |
| --- | ---: |
| Viajes con desviación | 14,3625 % |
| Lecturas con desviación | 6,1395 % |

Un filtro por fecha puede recortar las lecturas de un viaje. Debe decidirse si el indicador evaluará solo las lecturas visibles o la totalidad del viaje seleccionado.

### Vencimiento y merma

- Vida remanente al salir: fecha de vencimiento menos fecha de salida, expresada en días calendario al normalizar fechas.
- Salió vencido: vida remanente menor que cero; salir el día del vencimiento no cuenta como vencido bajo esa regla.
- Merma porcentual: suma de cantidad_merma dividida entre suma de cantidad_ingreso. No promediar porcentajes por lote como sustituto.
- Días promedio en almacén: promedio de dias_en_almacen.

| Control global | Resultado reproducido |
| --- | ---: |
| Lotes salidos vencidos | 1.069 |
| Lotes con vida remanente menor que 7 días, incluyendo vencidos | 1.317 |
| Lotes con vida remanente entre 0 y 6 días | 248 |
| Merma porcentual | 7,3573 % |
| Días promedio en almacén | 38,9805 |
| Merma valorizada, cantidad_merma × costo_unitario_bob | Bs 35.574.924,68 |

La guía advierte que en v10 la merma no aumenta con la permanencia en almacén. No debe presentarse esa causalidad como hallazgo demostrado.

### Conciliación económica

La suma de perdida_mermas_bob de costos es Bs 35.574.924,68 y coincide con la merma valorizada de inventario. La conciliación también se cumple en los 144 grupos centro–mes al agrupar lotes por fecha de salida, con diferencias numéricas insignificantes de coma flotante.

La suma de costo_almacenamiento_mensual_bob es Bs 20.602.067,19 en los 24 meses disponibles.

No sumar merma de inventario y merma de costos como conceptos independientes. rotacion_stock_dias es un indicador centro–mes y no debe confundirse automáticamente con dias_en_almacen de un lote.

### Señales de desviación futura

La temperatura anterior corresponde a la misma entidad viaje_id y a minutos_desde_despacho − 30. La variación de 30 minutos es temperatura actual menos anterior. La primera lectura de cada viaje no tiene rezago.

| Condición | Frecuencia observada de desviación futura | Cobertura de positivos futuros |
| --- | ---: | ---: |
| Todas las lecturas | 6,7983 % | No aplica. |
| Desviación actual | 90,0085 % | 81,2860 % |
| Variación de 30 min > 0,5 °C | 36,6956 % | 18,5069 % |
| Puerta abierta | 6,5661 % | 5,3096 % |
| Sin las tres señales anteriores | 0,6691 % | 8,5399 % |

Las condiciones pueden superponerse: sus coberturas no se suman como si fueran grupos excluyentes. En la comprobación de ausencia de señales, una primera lectura sin variación disponible no se considera señal de aumento; esta convención debe explicitarse si se utiliza.

La medida docente Prob. Desviación 60 min es el promedio de desviacion_proximos_60min_flag en un contexto. Es una frecuencia empírica del resultado observado, no la salida individual de una regresión logística. La medida Cobertura de la Regla utiliza ALLSELECTED y deberá probarse en el contexto de filtros del informe.

## 10. Contexto predictivo heredado del Módulo 3

La guía de datos define para 03B:

- Modelo mínimo: regresión logística.
- Unidad: una lectura de telemetría.
- Objetivo: desviacion_proximos_60min_flag.
- Fuente mínima: andinalog_iot_telemetry_silver.csv.
- Predictoras sugeridas: temperatura, humedad, desviación actual, temperatura anterior y variación de 30 minutos.
- Rezagos calculados dentro de viaje_id y únicamente con información anterior o actual.
- Separación temporal utilizando particion_modelo.

| Partición | Filas comprobadas | Primera lectura | Última lectura |
| --- | ---: | --- | --- |
| TRAIN | 119.771 | 2024-01-01 00:49:27 | 2025-03-30 23:58:01 |
| VALIDATION | 23.984 | 2025-03-31 00:00:49 | 2025-06-29 23:56:44 |
| TEST | 47.955 | 2025-06-30 00:04:03 | 2025-12-31 13:31:20 |

Las métricas docentes de TEST son ROC-AUC 0,959, PR-AUC 0,858 y F1 0,817. Son referencias del autor, no resultados reproducidos de nuestro modelo ni metas obligatorias.

No se ha entrenado un modelo en este trabajo ni se han recibido sus probabilidades, artefactos o métricas del equipo. Tampoco se ha decidido si el alcance de implementación incluirá entrenarlo nuevamente o integrar uno existente.

## 11. Brechas y limitaciones detectadas

### Particiones temporales

La guía describe TRAIN hasta marzo de 2025, VALIDATION abril–junio y TEST julio–diciembre. Los archivos comienzan VALIDATION el 31 de marzo y TEST el 30 de junio. Además, 14 viajes contienen lecturas de dos particiones.

Se conservaron los valores originales. Antes de modelar habrá que decidir y documentar el tratamiento de cortes, viajes compartidos y objetivos cuyo horizonte cruza una frontera temporal.

### Indicador térmico en el límite

Hay 26 lecturas que no coinciden con reconstruir la desviación como diferencia absoluta respecto de temperatura requerida mayor que la tolerancia:

- 19 lecturas a −15 °C con referencia −18 °C y tolerancia 3 °C.
- 7 lecturas a 6 °C con referencia 4 °C y tolerancia 2 °C.

Todas están marcadas con desviación. El redondeo previo es una hipótesis posible, no confirmada. No se corrigen ni se redefine el indicador sin aclarar su regla de generación.

### Objetivo de 60 minutos al final del viaje

El objetivo coincide en todas las filas con el máximo de las dos lecturas siguientes del viaje, tomando cero cuando una lectura futura no existe. Las últimas lecturas tienen objetivo cero; la penúltima solo cuenta con una lectura posterior. Hay 16.000 registros en las últimas dos posiciones de los viajes, de los cuales 1.129 tienen objetivo positivo.

Un cero al cierre no demuestra una hora completa observada sin desviación. Debe conservarse esta limitación al evaluar y presentar resultados.

### Cobertura del caso

El dossier y Silver representan escalas diferentes: cinco frente a seis centros, 118 frente a 100 vehículos y 6.800 frente a 120 SKU. No se ha documentado si Silver es una muestra o una simplificación. No extrapolar resultados a toda la empresa sin justificarlo.

### Otras limitaciones

- Todos los lotes ya salieron; no hay una foto directa de stock vigente para alertas actuales de vencimiento.
- El centro base del camión no equivale necesariamente al centro operativo del viaje.
- Los datos sintéticos permiten aprendizaje; su señal predictiva no demuestra eficacia real ni causalidad empresarial.
- Las fechas de mantenimiento son atributos de una tabla estática; antes de usarlas históricamente debe aclararse su vigencia.
- Brecha DCAM A identificada y asignada a C4, Conocimiento de los datos del negocio, con dimensión Evidencia, puntaje 1 tentativo y confianza baja (DEC-026); sujeta a auditoría y validación docente.
- No se inventarán errores de calidad para completar una fila por tabla.

## 12. Requisitos por hito y trazabilidad

Las guías S01–S11 están revisadas. Los hitos son formativos y la calificación del proyecto se realiza en S13. La revisión documental no acredita implementación. El libro del proyecto se completa progresivamente; los ejemplos se reemplazan y las fórmulas automáticas se preservan cuando se autorice su edición.

### S01 Preparación

- Formular una decisión a partir del mandato y del mapa de indicadores.
- Inventariar las cinco fuentes: nombre, grano, claves, filas, columnas, brecha y responsable.
- Abrirlas en Power BI y registrar lo observado; los conteos con Python son contraste, no sustituyen evidencia de Desktop.
- Proponer 3–5 KPI candidatos con la decisión que apoyan.
- Priorizar una brecha DCAM: hecho, componente, dimensión, puntaje tentativo y riesgo.
- Entregar inventario, decisión, persona que compartirá pantalla en S02, fichas iniciales y brecha priorizada.

Dimensiones DCAM: Compromiso, Proceso y Evidencia. Escala: 1 Incipiente, 2 Repetible, 3 Definido, 4 Medido, 5 Optimizado. La lista C1–C8 se consultó como referencia complementaria en SRC-208 `Instrucciones!B10`: C1 Estrategia y caso de negocio; C2 Programa y financiamiento; C3 Gobierno de datos; C4 Conocimiento de los datos del negocio; C5 Calidad de datos; C6 Tecnología y arquitectura; C7 Operación de los datos; C8 Entorno de control y cultura. SRC-208 no contiene el mapeo de la brecha ni se editó; C4 fue aprobado en DEC-026.

Por indicación del usuario, el PDF references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf sigue siendo la referencia metodológica DCAM. La lista C1–C8 se consulta en SRC-208 solo como referencia complementaria. Se mantiene la plantilla general del Proyecto Integrador. El PDF exige hecho, criterio, puntaje, evidencia disponible/faltante y riesgo; sus ejemplos no son hallazgos de AndinaLog. Rodrigo Tucuman quedó designado para compartir pantalla en S02 (DEC-027).

### S02 Decisión, arquitectura y mapa Silver

- Cerrar una frase con quién decide, qué decide y cada cuánto.
- Completar la segunda diapositiva de arquitectura con origen → Silver → Power Query → modelo semántico → indicador. La primera es un ejemplo que no se entrega.
- Partir de la brecha DCAM e identificar riesgo, control y pendiente con responsable.
- Completar S02 Mapa Silver: archivo, grano, identificador, frecuencia, propietario, riesgo y control.
- Seleccionar 5–8 KPI y completar nivel de decisión, fórmula en palabras y unidad.
- Entregar arquitectura y mapa Silver en M4_EquipoXX_S02_Arquitectura.pdf, versiones editables y Fichas KPI.

Distinguir frecuencia de observación de frecuencia de actualización. La clave compuesta de telemetría debe documentarse. Los sistemas operativos de origen y los propietarios no se inventarán a partir de los nombres de los CSV. Está pendiente definir cómo reunir el mapa del Excel y el diagrama en el PDF.

### S03 Conexión y linaje

- Crear RutaSilver, texto, con valor `C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\`.
- Todas las consultas deben leer mediante `File.Contents(RutaSilver & "nombre_del_archivo.csv")`.
- Configurar región en-US antes de conectar y justificar privacidad de cada fuente.
- Activar perfil sobre todo el conjunto, no solo la muestra inicial.
- Completar S03 Linaje por fuente: conector, parámetro, privacidad, conteos, excepción y regla propuesta para S04; asignar revisión.
- Registrar tablas fuente de cada KPI.
- Entregar captura del parámetro y del paso Origen, linaje, excepciones y fichas.

Conservar fecha-hora para telemetría y derivar fecha para calendario y días calendario. fecha_salida no está vacía. Las excepciones detectadas se documentan antes de decidir su tratamiento.

### S04 Reglas aplicadas y reversibles

- Elegir 2–3 excepciones prioritarias por impacto en la decisión.
- Aplicar reglas en Power Query con pasos descriptivos.
- Registrar filas antes, afectadas y después, tratamiento y limitaciones.
- Revisar datos personales y justificar eliminación, enmascaramiento o seudonimización cuando corresponda.
- Vincular cada KPI con la regla de calidad que lo protege.
- Entregar captura de pasos, S04 Antes-después, fichas y pendientes.

Para 03B se exige convertir a fecha sin hora las columnas usadas para días calendario. Una regla puede marcar registros sin disminuir filas. No eliminar duplicados o rellenar vacíos que no existen. No corregir las 26 lecturas límite ni las particiones sin fundamento aprobado. Los cinco archivos no incluyen nombres de choferes.

### S05 Pipeline consolidado

- Declarar grano y claves en S05-S06 Modelo.
- Combinar hechos con catálogos solo tras validar tipo y unicidad de claves y contar antes/después.
- Mantener consultas de excepciones sin carga para registros sin correspondencia, incluso si el conteo es cero.
- Agregar cuando cambie el grano y demostrar conservación de totales.
- Control específico: agrupar telemetría por viaje produce 8.000 viajes y 14,36 % con desviación.
- Revisar fuentes de KPI y entregar dependencias de consultas, minuta con conteos/balance y pendientes.

Combinar con catálogo único no equivale a fusionar hechos de distinto grano. Conservar telemetría por lectura; la carga del agregado por viaje queda por decidir. S06 no exige dimensión de viajes.

### S06 Modelo y filtros

- Establecer hechos y dimensiones con claves únicas y sin vacíos.
- Crear calendario 2023–2026, marcarlo como tabla de fechas y desactivar fechas automáticas.
- Relacionar calendario solo con hechos mediante fechas sin hora.
- Usar varios a uno y dirección única; quitar relaciones automáticas incorrectas y justificar excepciones.
- dim_centro tiene seis centros y filtra inventario, costos y flota; viaje_id queda degenerada.
- Probar filtros con matrices para cada dimensión y hecho correspondiente.
- Completar grano y dimensiones en fichas; entregar minuta, captura de modelo y pendientes.

Producto no filtra costos de almacén por sí solo. No asignar costos mensuales a productos sin una regla explícita. Sigue pendiente precisar la relación temporal de costos y el significado del centro base para telemetría.

### S07 DAX y líneas base

- Validar al menos tres KPI; al menos uno debe ser proporción. El catálogo final contiene 5–8.
- Programar medidas, usar DIVIDE en divisiones y separar numerador/denominador cuando corresponda; VAR para subexpresiones repetidas.
- Comparar cálculo independiente y Power BI bajo igual contexto y precisión.
- Registrar desde fila 8 en S07 KPI; porcentajes como valores porcentuales, no números multiplicados por cien.
- Completar fórmula DAX, frecuencia, línea base y contexto en Fichas KPI.
- Referencias globales 03B: viajes 14,36 %, lecturas 6,14 %, 1.069 lotes vencidos y merma 7,36 %.
- Entregar captura de tabla/matriz, hojas y pendientes.

Propuesta no aprobada: validar inicialmente porcentaje de viajes con desviación, merma por cantidades y número de lotes vencidos. El informe final amplía la validación a todos los KPI del catálogo.

### S08 Diseño y primera página

- Explicar quién usa la página, qué decide, contexto de uso y riesgo de interpretar mal la señal.
- Antes de construir, definir polaridad, meta justificada y umbrales de los tres KPI de S07.
- Storyboard de estado/brecha → localización → evidencia, con pregunta, visual, transición y criterio de aceptación.
- Página con cabecera/segmentadores, estado, análisis y detalle.
- Metas como medidas; brecha = KPI − meta; colores derivados de reglas de ficha, acompañados de texto y símbolo.
- Títulos con unidad de análisis, variable y periodo; distinguir viajes y lecturas.
- Contraste mínimo 4,5:1, tabulación, texto alternativo, escala de grises y consistencia entre ficha y tarjeta bajo el mismo contexto.
- Entregar captura, storyboard, fichas y resultado de cada prueba con pendientes.

El PDF complementario añade prueba de cinco segundos; contexto visible; nombres del negocio; barras ordenadas desde cero; líneas con rango explícito e inclusión de meta cuando se compara; separación entre referencias fijas y valores filtrados; consulta de evidencia y siguiente acción. Las diferencias entre porcentajes se rotulan en puntos porcentuales (pp). Los símbolos deben aclarar si expresan estado o tendencia. Una señal no prueba una causa. Tabulación, filtros y accesibilidad no se certifican con una captura.

La guía admite polaridad «en rango», pero el libro solo contempla «Más es mejor» y «Menos es mejor». Si se necesita rango, debe resolverse la incompatibilidad antes de usar el estado automático. Los valores docentes son líneas de referencia, no metas predeterminadas.

### S09 Interacción y rendimiento

- Elegir parámetro de campo, tooltip o segmentadores sincronizados para una pregunta del storyboard.
- Probar dos selecciones distintas, resultados correctos y contexto conservado.
- Escribir escenario: página, filtros, acción y visual; repetirlo tres veces en el Analizador de rendimiento.
- Registrar Consulta DAX, Presentación visual y Otros en ms y componente dominante.
- Proponer siguiente mejora sin aplicarla todavía en este hito.
- Para 03B, comparar lectura anterior con LOOKUPVALUE frente a versión con FILTER.
- Completar tipo resultado/impulsor y relaciones entre KPI.
- Entregar interacción, escenario, capturas expandidas o exportación, tiempos, mejora y pendientes.

Separar pruebas funcionales con dos selecciones de las tres corridas del mismo escenario. Precisar si se mide cálculo durante actualización o consulta del visual: no son el mismo costo. El paquete final pide comparación antes/después de cambios. Las relaciones causa–efecto propuestas deben distinguir hipótesis de evidencia.

### S10 Escenario prescriptivo

Decisión: seleccionar un umbral de alerta térmica según el equilibrio entre falsas alarmas, casos omitidos y capacidad de intervención; su responsable, frecuencia y criterio de aceptación siguen pendientes.

- Parámetro Umbral Variación, entero 3–8, paso 1, predeterminado 5; dividir entre diez para °C.
- Condición: Variación 30 min > umbral; no mayor o igual.
- Medidas de escenario separadas y rótulos observado/escenario.
- Prob. Desviación Escenario: frecuencia del objetivo futuro entre lecturas que disparan alerta, equivalente a precisión de esta regla.
- Cobertura Escenario: positivos futuros captados por regla / positivos futuros del contexto.
- Registrar fuente, unidad, mínimo, centro, máximo, constantes y resultados en S10 Supuestos desde fila 8.
- Recomendación aprobar/validar/detener, umbral, evidencia que la cambiaría, pendientes y responsable.
- Impacto económico por unidad de mejora en columna Z de al menos un KPI.

Controles recalculados directamente con telemetría completa:

| Umbral | Lecturas con alerta | Precisión | Cobertura |
| --- | ---: | ---: | ---: |
| 0,3 °C | 23.760 | 18,44697 % | 33,63002 % |
| 0,5 °C | 6.573 | 36,69557 % | 18,50687 % |
| 0,8 °C | 1.600 | 63,56250 % | 7,80327 % |

La guía utiliza 5 como centro/referencia; el punto medio matemático de 3 y 8 es 5,5. Conservar esa distinción. Cambiar el umbral cambia clasificación de alertas, no temperatura real ni pérdidas evitadas. Son evaluaciones retrospectivas de una regla, no probabilidades de regresión logística.

Impacto económico: la guía cita aproximadamente Bs 4,83 millones por punto de merma. El valor ingresado comprobado es Bs 481.607.067,40; un pp de merma por valor equivale a Bs 4.816.070,67, manteniendo base constante. El 7,36 % corresponde a merma por cantidades. Relacionar una reducción de ese porcentaje con dinero requiere un supuesto sobre productos afectados. No atribuir automáticamente este ahorro al umbral de alerta.

### S11 Seguridad y paquete de PreEntrega

- Crear usuarios_rls sin relaciones, columnas correo, rol y valor_autorizado, con correos ficticios .example.
- Regla dinámica con USERPRINCIPALNAME sobre dim_centro[centro]: Gerencia ve todo; otros usuarios ven centros autorizados.
- El filtro alcanza inventario/costos y, por flota, telemetría.
- Probar en Ver como, marcando el rol y Otro usuario; una positiva por rol, negativa y correo sin mapeo.
- Registrar S11 Pruebas RLS desde fila 8. Referencias docentes: Gerencia 7.782 lotes; Tarija 1.572 lotes y 39.609 lecturas; sin mapeo cero. Los 39.609 requieren validación adicional y prueba Desktop; no se declaran aquí como comprobados.
- Completar responsables, acciones ante rojo, visibilidad y perspectiva. Fichas KPI al 100 %, incluyendo campos previos e impacto económico.
- Aplicar comisionamiento de datos, modelo, rendimiento, experiencia y seguridad y registrar resultados.
- PreEntrega: proyecto .pbip, diccionario, informe de pruebas, presentación de 20 minutos y libro completo. Entrega antes de S12; sesión de 30 minutos: 20 exposición, 7 retroalimentación, 3 registro de mejoras.

La fórmula base del docente busca un rol único por correo y valores autorizados mediante la tabla desconectada. Si se permite varios centros por usuario, asegurar consistencia del rol. La prueba negativa debe demostrar ausencia de acceso aunque el centro prohibido no aparezca en el segmentador. El usuario sin mapeo es una excepción deliberada a la indicación de usar correos de la tabla. Verificar también tablas desconectadas y auxiliares que puedan exponer información.

### Fichas KPI y relación con Módulo 5

La ficha reúne decisión, nivel, fórmula, unidad, fuentes, calidad, grano, dimensiones, DAX, frecuencia, línea base/contexto, polaridad, meta/justificación, umbrales, responsable, acción, acceso, perspectiva, tipo, relaciones e impacto económico. El enlace estratégico es propuesta para validación en Módulo 5. El porcentaje de completitud no demuestra calidad ni validez de lo escrito.

La referencia KPI confirma como núcleo viajes con desviación 14,36 %, merma 7,36 % y lotes vencidos 13,7 %. Su catálogo define merma como valor perdido / valor ingresado, mientras la guía técnica usa cantidades: documentar ambas definiciones y seleccionar explícitamente. No confundir 1.069 lotes con su porcentaje.

## 12A. Paquete final, pruebas y defensa

### Diccionario

Describir el .pbip efectivamente entregado: tablas con grano, origen, conteos y claves; columnas cargadas o eliminadas a propósito con tipo, significado, unidad, rango, privacidad y uso; medidas con explicación, formato, KPI y referencia/contexto; parámetros de ruta y What-if y roles con regla en palabras. Ampliar filas si hace falta: el espacio inicial no limita la documentación.

Las fichas definen KPI, el diccionario explica su implementación y el informe demuestra su validación. Mantener los tres alineados con el proyecto.

### Informe de pruebas

1. Ficha: decisión, tablas, relaciones, medidas, páginas, seguridad y rutas.
2. Calidad: reglas contadas, conciliación, datos personales y portabilidad a otra computadora cambiando solo parámetros.
3. Modelo y rendimiento: relaciones/excepciones y medición antes/después bajo escenario idéntico.
4. Medidas: esperado independiente frente a Power BI para cada KPI del catálogo.
5. What-if: mínimo, centro, máximo y punto/condición de cambio de recomendación.
6. RLS: pruebas positivas por cargo, negativa y sin mapeo.
7. Arquitectura de publicación prevista y justificada.
8. Hallazgos, fallos y pendientes con acciones.
9. Tres a cinco mejoras de PreEntrega con evidencia antes/después.
10. Uso de IA: etapa, herramienta, propuesta, corrección y comprobación.

Conservar pruebas fallidas. Los resultados deben verse en el .pbip, idealmente en página Pruebas. No rellenar filas vistas ni estados Pasa sin ejecución.

La plantilla establece que en el curso no hay licencias Service: publicación prevista, no ejecutada. Documentar origen → puerta de enlace → modelo/área de trabajo → distribución → usuarios; roles de mantenimiento y consulta; actualización/credenciales/responsable; pertenencia RLS y limitaciones. Las propuestas concretas del ejemplo, como horario, responsables o ubicación de datos, no son decisiones de AndinaLog. No confundir roles de edición de área de trabajo con restricciones de filas; validar la configuración efectiva si en el futuro se publica.

### Presentación final

Diez diapositivas: portada/decisión; mejoras posteriores a S12; usuario/decisión/DCAM; calidad; modelo/rendimiento; KPI; demo del tablero; escenario/recomendación; seguridad/publicación; valor/límites/siguiente paso.

Se exige correspondencia con proyecto, diccionario e informe; demo en vivo del tablero, parámetro en sus tres valores y una prueba RLS. La plantilla final propone 22 minutos de exposición/demo y 8 de preguntas. No confundir con los 20 minutos de exposición de PreEntrega.

Abrir la defensa, después de portada, con las 3–5 mejoras de S12 y mostrar cambios efectivos en el proyecto. La plantilla del informe/presentación usa Aplicada, Justificada o Pendiente; el libro S12 usa Aplicada, Parcial o No aplicada (justificar). Conservar o acordar correspondencia sin modificar opciones silenciosamente.

Los archivos finales se nombran para Equipo06 según plantilla: proyecto comprimido, diccionario, informe y presentación, además del libro de hitos/fichas. Confirmar convención final con rúbrica. El diccionario e informe indican entrega antes de S13; S11 pide versión de PreEntrega antes de S12.

Las plantillas aportan estructura de comisionamiento, pero remiten a la práctica y a la rúbrica v4. Esos documentos completos no se recibieron; no se presume que la lista de criterios esté agotada.

## 13. Método de trabajo acordado

El usuario trabajará con una combinación de Spec First y Spec Anchored en OpenCode. Cada hito tendrá una especificación y un ciclo de planificación, construcción y auditoría. La base documental se prepara primero con el usuario; las specs se desarrollarán después en OpenCode.

Organización documental acordada:

- Contexto: hechos, requisitos, referencias, hallazgos y preguntas.
- Constitución: principios estables del proyecto.
- AGENTS.md: instrucciones operativas para los agentes.
- Especificaciones: resultados exigidos y criterios de aceptación por etapa o grupo de hitos.
- Planes y tareas: implementación de cada especificación.
- Registro de decisiones y evidencias: motivos, validaciones y limitaciones.

Los hitos docentes deberán conservar trazabilidad aunque una especificación agrupe varios. No se copiarán los ejemplos de otros casos. Todavía no se ha autorizado iniciar implementación, completar las plantillas ni construir el proyecto Power BI. La autorización actual comprende revisar y actualizar la base documental, sin iniciar specs ni implementación.

### Estructura y continuidad

La estructura utiliza README.md, AGENTS.md y MEMORY.md en la raíz; docs/context.md, docs/constitution.md, docs/prompts.md, docs/decisions.md y docs/sources.md como base documental; references/, specs/, powerbi/, validation/, evidence/, deliverables/ y work/ como áreas de trabajo.

Cada carpeta de especificación contiene spec.md, plan.md, tasks.md y un único AUDIT.md. Este último conserva el estado actual, los hallazgos con identificadores estables y todas las rondas de auditoría, sin borrar revisiones anteriores.

El ciclo acordado es Spec aprobada → Plan → Build → Auditoría → Correcciones → Nueva auditoría → Cierre. La auditoría inspecciona sin modificar los artefactos auditados. Las correcciones se hacen en Build y se verifican nuevamente hasta cumplir los criterios de la spec. Los cambios de alcance requieren acuerdo y actualización de requisitos antes de implementarse.

MEMORY.md se lee al iniciar y se actualiza tras avances significativos: estado, trabajo realizado, verificaciones, decisiones, pendientes y siguiente paso. No sustituye tareas, decisiones ni evidencias detalladas.

El usuario crea la estructura y solicita cada archivo paso a paso. No se inicia un hito ni se crean documentos adicionales sin el alcance autorizado. Se mantiene un único proyecto Power BI de trabajo y se usa control de versiones para su evolución.

Las rutas documentales se alinearon con los nombres ingleses y las fuentes presentes en references/. Los Silver permanecen en su ubicación oficial externa.

## 14. Flujo de prompts de referencia

Los documentos de prompts revisados aportan un método general adaptable: contexto → decisión/KPI/supuestos → preparación/modelo → medidas → What-if → página/interacción → seguridad/comisionamiento → generación final del proyecto.

Cada etapa utiliza lo revisado en la anterior y termina con una prueba. El proyecto previsto es Power BI en formato .pbip; su estructura, páginas, seguridad y formato de informe definitivos se decidirán al leer todas las guías.

Hay que distinguir comprobaciones de archivos de comprobaciones en Power BI Desktop. No se declarará publicación, configuración o prueba en Power BI Service si no se ejecutó. El informe final establece publicación prevista y no ejecutada en el curso por falta de licencias. La disponibilidad particular del equipo no se ha comprobado; no cambia el requisito académico de describir lo no ejecutado con transparencia.

Los valores, inversiones, usuarios y fórmulas del ejemplo de otro negocio no se trasladan a AndinaLog.

## 15. Pendientes antes de especificar e implementar

1. Obtener la rúbrica v4 y, si existen, guías S12–S13 y lista completa de comisionamiento de la práctica. Ya se revisaron S01–S11.
2. Conocer avances, decisiones, entregas y resultados predictivos previamente realizados por el equipo.
3. Cerrar usuario, decisión concreta, frecuencia, acciones y prioridades del tablero.
4. Seleccionar 5–8 KPI, resolver merma por cantidades frente a valor y documentar metas/umbrales.
5. Brecha DCAM A priorizada y C4 asignado con respaldo del usuario (DEC-026); falta validación docente/auditoría y completar responsables empresariales.
6. Revisar GIAD-M3_v10_auditoria_bronze_silver.csv, mencionado pero no recibido.
7. Documentar cobertura, lecturas límite, horizonte futuro y particiones; decidir tratamientos sin alterar originales.
8. Definir alcance del componente predictivo: integración de resultados existentes o nuevo entrenamiento.
9. Adoptar el What-if prescrito por S10 y establecer criterio de recomendación, costos de errores y capacidad de atención. Su variable y rango ya están definidos por la guía.
10. Precisar relación temporal de costos, centro base de camión y carga o no del agregado por viaje.
11. Definir usuarios/roles por centro y ejecutar pruebas RLS, incluida telemetría de Tarija, negativos y tablas auxiliares.
12. Acordar estructura SDD y herramientas, formato del informe Power BI, criterios de aceptación y evidencias por hito.
13. Resolver diferencias de estados de mejoras, tiempos de exposición, polaridad en rango y documentación de impacto económico en todas las fichas.

## 16. Fuentes revisadas

### Documentación de negocio y módulo

- `references/general/Cartera_Oficial_Tres_Casos_Negocio_GIAD_v1.0.pdf` — protocolo común, dossier AndinaLog y mandato 03B.
- `references/S01/GIAD-M4-S01_Preparacion_Proyecto_Integrador.docx` — requisitos S01.
- `references/general/GIAD-M4_Seis_Subcasos_Mapas_Indicadores_v10.pptx` — diapositiva 6, mapa 03B.
- `references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` — estructura progresiva del proyecto.
- `references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf` — referencia DCAM metodológica activa. No enumera los componentes C1–C8.
- `C:\GIAD\HITOS01\GIAD-M4-S01_Plantilla_Taller_DCAM_v2.xlsx` — SRC-208, referencia complementaria de la lista C1–C8 en `Instrucciones!B10`; leída sin editar. SHA-256 `D6FE317D30241BA3705A7B18F4D1B28CA5B55A187E9AEDBF2B6B9E7A1A294686`.
- `references/general/GIAD-M4_PowerBI_Modelo_Relaciones_DAX_Seis_Subcasos_v10.docx` — reglas generales y sección 03B. Sus referencias se calcularon con Python por el autor; las medidas DAX no se ejecutaron en Desktop en su entorno.
- `references/general/GIAD-M3_datos_sinteticos_guia_v10.docx` — preparación Silver, contrato predictivo y referencias temporales.


### Guías y materiales adicionales revisados en esta versión

- `references/S02/GIAD-M4-S02_Hito_Proyecto_Integrador.docx`.
- `references/S02/GIAD-M4-S02_Plantilla_Diagrama_Arquitectura.pptx`.
- `references/general/GIAD-M4_Referencia_KPI.docx`.
- `references/S03/GIAD-M4-S03_Hito_Proyecto_Integrador.docx`.
- `references/S04/GIAD-M4-S04_Hito_Proyecto_Integrador.docx`.
- `references/S05/GIAD-M4-S05_Hito_Proyecto_Integrador.docx`.
- `references/S06/GIAD-M4-S06_Hito_Proyecto_Integrador.docx`.
- `references/S07/GIAD-M4-S07_Hito_Proyecto_Integrador.docx`.
- `references/S08/GIAD-M4-S08_Hito_Proyecto_Integrador.docx`.
- `references/S08/GIAD-M4-S08_Dashboard_Diseno_Visual.pdf`.
- `references/S09/GIAD-M4-S09_Hito_Proyecto_Integrador.docx`.
- `references/S10/GIAD-M4-S10_Hito_Proyecto_Integrador.docx`.
- `references/S11/GIAD-M4-S11_Hito_Proyecto_Integrador.docx`.
- `references/delivery/M4_EquipoXX_Presentacion_v01.pptx`.
- `references/delivery/M4_EquipoXX_InformePruebas_v01.docx`.
- `references/delivery/M4_EquipoXX_Diccionario_v01.xlsx`.

### Método de prompts

- `references/prompts/GIAD-M4_Referencia_Prompts_Proyecto_WhatIf.docx`.
- `references/prompts/GIAD-M4_Ejemplo_Prompts_Proyecto_WhatIf.docx`.

Se utiliza su método general; el contenido empresarial del ejemplo queda fuera de este contexto.

### Datos inspeccionados

Los cinco CSV de la sección 6, ubicados en `C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver/`.

## 17. Estado al cierre de esta versión

Se revisaron los documentos listados y se realizaron comprobaciones de lectura sobre los cinco Silver. El PBIP existe con `RutaSilver`, cinco tablas, 0 relaciones, 0 medidas y sin visuales; su estructura y datos se verificaron en Desktop durante T05. No se transformaron archivos fuente, no se completó el libro docente original —la copia de seguimiento contiene solo campos de S01—, no se entrenó un modelo, no se publicó y no se probó Power BI Service.

El contexto permanece abierto. S01 se cerró con limitaciones documentadas el 2026-10-22. S02 se cerró el 2026-10-27 con 30/30 requisitos y criterios conformes. S03 se cerró el 2026-10-28 con 21/21 requisitos y criterios conformes, `A-S03-001` cerrado y evidencia Desktop de región, privacidad y perfil completo. S04–S11 no se iniciaron. Los pendientes trasladados a hitos posteriores siguen abiertos y no se declaran resueltos.

Desde el 2026-10-27 rige la estructura documental mínima: un `evidence.md`, un `validation.json` y un `AUDIT.md` por hito; no se conservan temporales, renders duplicados, dependencias descargadas ni informes por microtarea.
