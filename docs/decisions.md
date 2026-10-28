# Registro de decisiones · AndinaLog 03B

Última actualización: 27 de octubre de 2026.

Este archivo registra decisiones relevantes y su fundamento. No sustituye el contexto, las specs ni las evidencias. «Confirmada» significa acordada por el usuario o exigida expresamente por una fuente docente; no implica implementación ni validación técnica.

## Convenciones del registro

- Conservar identificadores estables y el historial de cambios.
- Indicar origen, fecha, motivo, consecuencias y estado.
- Una propuesta pendiente no autoriza su implementación.
- Si una decisión cambia, marcar la anterior como sustituida y enlazar la nueva; no borrar la historia.
- Actualizar specs, planes y pruebas afectados antes de implementar un cambio de alcance autorizado.

## Decisiones confirmadas

### DEC-001 · Caso y fuentes oficiales

- Fecha: 2026-10-20.
- Estado: confirmada por documentación docente y alcance de la conversación.
- Decisión: trabajar exclusivamente sobre AndinaLog, Grupo 06, subcaso 03B, utilizando los Silver oficiales v10 indicados en docs/context.md.
- Fundamento: mandato 03B, mapa de indicadores y guías del Módulo 4.
- Consecuencia: los ejemplos de otros casos aportan procedimientos, pero no sus cifras, usuarios, metas ni soluciones de negocio.
- Implementación: los cinco archivos fueron inspeccionados; no se construyó el proyecto Power BI.

### DEC-002 · Entorno y método

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: desarrollar el proyecto en OpenCode con una combinación de Spec First y Spec Anchored.
- Fundamento: preferencia del usuario y ejemplos SDD proporcionados.
- Consecuencia: especificar y acordar objetivos antes de implementar; mantener implementación, requisitos y evidencia alineados.

### DEC-003 · Avance por hitos

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: organizar el trabajo siguiendo S01–S11 y desarrollar las specs progresivamente en OpenCode.
- Fundamento: trazabilidad con las guías y plantillas académicas.
- Consecuencia: una carpeta por hito con spec.md, plan.md, tasks.md y AUDIT.md. Los artefactos pueden compartirse entre hitos, pero los criterios de aceptación conservan su trazabilidad.
- Límite: los documentos recibidos incluyen cierre S12–S13; falta revisar sus guías específicas y la rúbrica v4.

### DEC-004 · Ciclo de construcción y auditoría

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: Spec aprobada → Plan → Build → Auditoría → Correcciones → Nueva auditoría → Cierre.
- Fundamento: flujo solicitado para detectar y resolver desviaciones hasta cumplir el objetivo.
- Consecuencia: auditar contra criterios explícitos; las correcciones corresponden a Build. La auditoría no modifica los artefactos auditados y el cierre exige evidencia de cumplimiento.

### DEC-005 · Historial único de auditoría

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: un único AUDIT.md por spec, con todas las rondas, estado actual y hallazgos con identificadores estables.
- Fundamento: evitar dispersar las revisiones en múltiples archivos.
- Consecuencia: añadir rondas y registrar cierre o reapertura sin borrar revisiones anteriores. El nombre originalmente propuesto en español se sustituye por AUDIT.md conforme a DEC-008.

### DEC-006 · Memoria de continuidad

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: mantener MEMORY.md en la raíz, con estado actual e historial resumido de avances significativos.
- Fundamento: continuidad entre sesiones y agentes.
- Consecuencia: leer al comenzar y actualizar al finalizar avances autorizados; enlazar detalles en lugar de duplicarlos. No registrar pruebas inexistentes, secretos ni propuestas como acuerdos.

### DEC-007 · Control del arranque

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: el usuario arma la estructura y solicita los documentos uno por uno. La base inicial se define en esta conversación; las specs se trabajarán en OpenCode.
- Fundamento: avanzar paso a paso y revisar el contenido antes del desarrollo.
- Consecuencia: entregar únicamente lo solicitado. Preparar un archivo descargable no acredita que esté instalado en el repositorio ni autoriza iniciar implementación.

### DEC-008 · Nombres en inglés

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: usar nombres propios de archivos y carpetas en inglés, salvo donde sea necesario conservar español.
- Fundamento: preferencia explícita del usuario.
- Consecuencia: docs/context.md, docs/constitution.md, docs/prompts.md, docs/decisions.md, docs/sources.md y AUDIT.md; carpetas references/, validation/, evidence/, deliverables/ y work/.
- Excepciones: conservar nombres originales de documentos docentes, fuentes, columnas y términos del negocio cuando corresponda. Contenido explicativo en español.
- Actualización: enlaces y nombres alineados en la revisión documental del 2026-10-20, sin cambios a los principios de la constitución.

### DEC-009 · Ubicación del proyecto

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: utilizar C:/Users/remrodri/Github/Proyecto-Powerbi-Andinalog-rol03b/ como carpeta del proyecto.
- Fundamento: ruta elegida expresamente.
- Consecuencia: referencias internas mediante rutas relativas. Se comprobó la presencia de los tres documentos raíz, cinco documentos en docs/ y las referencias reunidas por el usuario.

### DEC-010 · Conexión Silver parametrizada

- Fecha: 2026-10-20.
- Estado: requisito docente confirmado, pendiente de implementar.
- Decisión: conectar mediante el parámetro de texto RutaSilver con la ruta C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver\ y usar configuración regional compatible con números de punto decimal.
- Fundamento: guía S03.
- Consecuencia: ninguna consulta debe incluir su propia ruta absoluta de origen. Los Silver originales se mantienen intactos.

### DEC-011 · Escenario de S10

- Fecha: 2026-10-20.
- Estado: requisito docente confirmado, pendiente de implementar.
- Decisión: simular Umbral Variación entero de 3 a 8, paso 1, predeterminado 5, interpretado en décimas de °C. La regla utiliza variación de 30 minutos mayor que el umbral y se evalúa con precisión y cobertura.
- Fundamento: guía S10 para 03B.
- Consecuencia: distinguir evaluación retrospectiva de regla, predicción de un modelo y efecto económico real. El umbral operativo recomendado y sus costos permanecen pendientes.

### DEC-012 · Seguridad y publicación académica

- Fecha: 2026-10-20.
- Estado: requisitos docentes confirmados, pendientes de implementar y probar.
- Decisión: RLS dinámica por dim_centro, con usuarios_rls desconectada y pruebas positivas, negativa y sin mapeo. Documentar publicación Service como arquitectura prevista, conforme a la plantilla del curso.
- Fundamento: S11 e informe de pruebas final.
- Consecuencia: no afirmar publicación ni actualización programada ejecutadas. Definir autorizaciones y comprobar propagación a inventario, costos y telemetría. No trasladar usuarios ni horarios del ejemplo.

### DEC-013 · Referencia DCAM activa

- Fecha: 2026-10-20.
- Estado: confirmada por indicación explícita del usuario.
- Decisión: utilizar references/S01/GIAD-M4-S01_Sesion1_Completa-20-32.pdf como referencia DCAM metodológica activa. El Excel del taller se consulta solo como referencia complementaria de la lista C1–C8 en SRC-208; no sustituye al PDF. Se mantiene GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx.
- Consecuencia: diagnóstico basado en hechos, Compromiso/Proceso/Evidencia y escala didáctica 1–5. La lista C1–C8 se toma de SRC-208 `Instrucciones!B10`; el Excel no se edita ni completa y no se le atribuye un mapeo de la brecha.
- Actualización 2026-10-21: el usuario autorizó el Excel del taller como referencia complementaria de la lista; DEC-026 registra la asignación C4.

### DEC-014 · Referencias locales

- Fecha: 2026-10-20.
- Estado: ubicación comprobada.
- Decisión: usar las copias originales reunidas por el usuario en references/ y rutas relativas a la raíz para localizarlas.
- Consecuencia: fuentes, contexto e instrucciones alineados; no se modifican documentos originales ni se trasladan los Silver.

### DEC-016 · Decisión y usuario de S01

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: la decisión de S01 corresponde a Jefatura de Operaciones, con revisión semanal. Prioriza controles térmicos por producto y camión, y mejoras de lotes por centro con desempeño histórico. Las señales futuras solo evalúan reglas de alerta; no se supone ruta real ni inventario vigente.
- Fundamento: respuestas del usuario durante la especificación de S01.
- Consecuencia: orienta los KPI y visuales; no autoriza implementación ni atribuye causalidad.

### DEC-017 · KPI candidatos de S01

- Fecha: 2026-10-20.
- Estado: confirmada; selección final en S02, metas y umbrales en S08.
- Decisión: cinco candidatos: porcentaje de viajes con desviación, porcentaje de lecturas con desviación, merma por cantidades, porcentaje de lotes salidos vencidos y días promedio en almacén. Medida de apoyo: número de lotes vencidos. La merma por cantidades se calcula como suma de `cantidad_merma` entre suma de `cantidad_ingreso`; la medida económica por valor sigue pendiente.
- Fundamento: decisión de Jefatura de Operaciones y datos disponibles.
- Consecuencia: no se presentan como KPI finales ni metas. Cada uno requiere fórmula, unidad, denominador contextual, fuente y límite. Los responsables de revisión de S01 son Grupo 06; los responsables empresariales se completan progresivamente y la ficha KPI los exige en S11.
- Límite: el porcentaje de lecturas es una proporción de observaciones marcadas; no demuestra duración exacta, intensidad térmica ni cobertura del monitoreo, y por sí solo no permite concluir concentración o dispersión. Los días en almacén son permanencia histórica, no rotación ni causa.
- Actualización 2026-10-20: se precisan fórmula de merma, denominadores contextuales y momentos de selección, metas y responsables. Sustituye la formulación anterior que situaba metas y umbrales en S02.

### DEC-018 · Brecha DCAM priorizada (tentativa)

- Fecha: 2026-10-20.
- Estado: brecha A tentativa; componente C4 confirmado por el usuario en DEC-026; puntaje 1 y confianza baja sujetos a validación docente.
- Decisión: brecha A, ausencia de definición explícita de `centro_distribucion`; componente C4, Conocimiento de los datos del negocio; dimensión Evidencia; puntaje 1 tentativo y confianza baja, con alcance documental.
- Fundamento: SRC-202, revisión de fuentes y aprobación del usuario el 2026-10-21. El PDF DCAM no enumera C1–C8; la lista se consultó en SRC-208 como referencia complementaria.
- Consecuencia: no califica madurez empresarial; se registra el impacto y el respaldo documental. El puntaje no se convierte en medición empresarial.
- Límite: si el docente confirma otra lista o criterio, el componente, la brecha y el puntaje deben revisarse.
- Actualización 2026-10-20: DEC-022 precisa el alcance. El cierre exige el componente aplicable respaldado, no la lista C1–C8 ni documentación reservada.
- Actualización 2026-10-20 (revisión T03): la asignación C4 registrada inicialmente en `evidence/S01/preparation.md` se retira. C4 provenía de la lista histórica C1–C8 referida por la guía S01 y `docs/context.md`; SRC-202 no la enumera y ninguna decisión autorizó esa asignación. El componente sigue pendiente de identificación y respaldo. Se conservan dimensión Evidencia, puntaje 1 tentativo y confianza baja. P03 no acredita cierre DCAM.
- Actualización 2026-10-21: el usuario aprueba C4 con fundamento en la lista C1–C8 de SRC-208 y en el carácter semántico de la brecha. DEC-026 formaliza el respaldo; P03 no se reescribe.

### DEC-019 · WMS como contraste, sin carga

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: usar WMS solo para contrastar la lectura orden→centro; no cargarlo al modelo. Los cruces propios se registran como EV-S01-WMS y no se atribuyen a DATA-006.
- Fundamento: disponibilidad de la fuente y alcance de S01.
- Consecuencia: DATA-007 identifica WMS y DATA-006 la auditoría Bronze–Silver. Al adoptar esta decisión, el archivo de evidencia EV-S01-WMS no se había guardado.
- Actualización 2026-10-20: T02 guardó EV-S01-WMS en `evidence/S01/wms_contrast.md`; queda pendiente de auditoría. No cambia la decisión.

### DEC-020 · Formato, fases y responsabilidad de revisión

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: Markdown es la fuente de verdad. Durante Build se copia SRC-201 solo con los campos de S01 en `deliverables/tracking/` y se conserva el original. Las evidencias van en `evidence/S01/`. El Grupo 06 revisa cada fuente; el propietario de negocio está por confirmar y no se asigna custodia técnica empresarial.
- Fundamento: instrucciones del usuario y separación entre Specify y Build.
- Consecuencia: no se completan plantillas en Specify ni se declara validación de negocio sin propietario.

### DEC-021 · Rectificación de la spec S01

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: restaurar la v0.2 y aplicar solo los ajustes autorizados. El inventario principal contiene exactamente las cinco fuentes oficiales; WMS queda separado como contraste. La merma por cantidades usa suma de `cantidad_merma` entre suma de `cantidad_ingreso`. Los denominadores de KPI son contextuales. RF-S01-09 exige la copia de plantilla, RF-S01-10 delimita la implementación y RF-S01-11 registra la procedencia Bronze–Silver. La persona que compartirá pantalla sigue pendiente y es condición de cierre.
- Fundamento: correcciones solicitadas tras detectar cambios no aprobados en el guardado anterior.
- Consecuencia: la spec recupera la numeración y el contenido de la v0.2, con los cuatro ajustes de la v0.3. No se creó plan ni tareas y no se ejecutó Build.

### DEC-022 · Componente DCAM aplicable en S01

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: para cerrar S01 debe identificarse y respaldarse el componente DCAM aplicable a la brecha priorizada. No se exige evaluar los ocho componentes ni reconstruir documentación reservada. Si falta respaldo del componente elegido, el criterio sigue pendiente.
- Fundamento: autorización del usuario; el PDF DCAM activo no enumera C1–C8 y la lista histórica no es un requisito de cierre.
- Consecuencia: la spec v0.4 actualiza RF-S01-07, CA-S01-03, la condición de cierre, los riesgos, el caso límite y DUD-S01-01. Plan y tareas exigen el componente aplicable, no la lista completa.
- Límite: no se elige por suposición un componente distinto del que corresponde a la brecha; la lista C1–C8 no se reconstruye ni se presenta como evaluada.
- Actualización 2026-10-21: el componente aplicable queda identificado como C4 y respaldado por DEC-026. Esta condición de RF-S01-07/CA-S01-03 queda cubierta en el plano documental, sujeta a auditoría; no cierra S01.

### DEC-023 · Evidencia Desktop decimal y Flota

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: en Desktop se verifican decimales solo en las tablas que tengan columnas decimales. Para flota se comprueban enteros y fechas y se documenta que no contiene campos decimales. Esto no exime de comprobar archivo, filas y columnas.
- Fundamento: autorización del usuario y esquema de flota sin campos decimales.
- Consecuencia: la spec v0.4 actualiza RF-S01-06 y CA-S01-04; plan y tareas alinean P05/T05. No se inventa un decimal para flota ni se omite la comprobación estructural.
- Límite: no se declara evidencia Desktop ejecutada; la prueba y la captura siguen pendientes.

### DEC-024 · Aprobación del plan y autorización de T01

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario.
- Decisión: corregir solo la frase de autorización de la cabecera de la spec para indicar que habilita la planificación y no el Build; aprobar `plan.md` v0.2 y `tasks.md` alineadas. Autorizar únicamente T01 para verificar fuentes y entorno. No importar tablas, no completar plantillas, no abrir Power BI para importar y no avanzar a T02.
- Fundamento: instrucción expresa del usuario.
- Consecuencia: T01 se ejecuta y registra; las tareas T02–T10 permanecen pendientes. La aprobación del plan no acredita el cumplimiento de S01 ni autoriza por sí sola el resto del Build.
- Límite: los artefactos de T01 se limitan a manifiesto de fuentes y registro de entorno; no se completan entregables ni se transforman datos.

### DEC-028 · Aprobación de la spec S02 v0.4

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: aprobar y guardar la spec S02 v0.4 en `specs/002-s02-architecture/spec.md`, con la única precisión final sobre la frecuencia de `andinalog_inventory_tracking_silver.csv`. La aprobación habilita la preparación del Plan de S02.
- Fundamento: aprobación explícita del usuario tras corregir la v0.3 no aprobada.
- Consecuencia: S02 queda con Specify completada; Plan, tareas, Build y auditoría siguen pendientes. No se crean `plan.md`, `tasks.md` ni `AUDIT.md` por esta decisión.
- Límite: no autoriza Build, entregables, cambios en Power BI, plantillas, Excel o PowerPoint, ni iniciar el hito siguiente.

### DEC-029 · Arquitectura y mapa Silver de S02

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: el mapa Silver contiene exactamente cinco filas, DATA-001 a DATA-005. DATA-007 `andinalog_wms_orders_silver.csv` queda fuera del mapa, se registra solo como fuente de contraste orden→centro, no se carga y no cuenta como sexta fuente oficial. El origen de cada archivo se registra como «no documentado / por acordar»; el contexto del dossier —ERP con parametrización inconsistente, WMS parcial en dos centros y ausencia de TMS— es contexto general y no linaje comprobado.
- Fundamento: guía S02, inventario de S01 y correcciones solicitadas por el usuario.
- Consecuencia: RF-S02-03 y CA-S02-03 exigen cinco filas; la caja Origen no atribuye sistemas a las tablas. Origen y propietarios quedan como pendientes PEN-017.
- Límite: no se inventan propietarios, sistemas de origen ni linaje a partir de los nombres de archivo.

### DEC-030 · KPI tácticos de S02

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: seleccionar los cinco KPI heredados —porcentaje de viajes con desviación, porcentaje de lecturas con desviación, merma por cantidades, porcentaje de lotes salidos vencidos y días promedio en almacén— con nivel **táctico**, porque apoyan la decisión semanal de la Jefatura de Operaciones. El detalle de la observación o el grano no determinan el nivel. Se conserva «número de lotes vencidos» como medida de apoyo y no se incorpora «merma por valor» como KPI.
- Fundamento: DEC-016, DEC-017, guía S02 y catálogo SRC-005.
- Consecuencia: RF-S02-06 y CA-S02-06 exigen nivel, fórmula en palabras y unidad; metas y umbrales corresponden a S08, DAX a S07 y responsables empresariales a S11.
- Límite: los valores de referencia son líneas base, no metas. PEN-002 conserva su historial; la selección de S02 se registra en esta decisión.

### DEC-031 · Brecha DCAM de S02 como ausencia documentada

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: admitir tres estados para la brecha de `centro_distribucion` y `centro_distribucion_base`: definición respaldada con fuente citada; definición propuesta provisional pendiente de validación; o ausencia documentada con usos, límites conocidos y solicitud concreta de definición y validación. Para DUD-S02-07 se adopta **ausencia documentada**. En todos los casos se registra el estado de validación y el seguimiento del Grupo 06.
- Fundamento: DEC-018, DEC-026 y ausencia de un validador empresarial identificado.
- Consecuencia: RF-S02-04 y CA-S02-05 se cumplen con la ausencia documentada; `dim_centro` y los controles de claves quedan solo como propuestas complementarias. La validación empresarial sigue pendiente como PEN-019.
- Límite: no se inventa definición, no se declara resuelta la brecha y no se convierte al Grupo 06 en propietario empresarial.

### DEC-032 · Grano y frecuencia de inventario

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: `andinalog_inventory_tracking_silver.csv` mantiene **una fila por lote con ingreso, salida y merma en esta entrega**. Su frecuencia se registra como «sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar». No se separan filas de ingreso y salida.
- Fundamento: grano comprobado en S01 y precisión solicitada por el usuario al aprobar la spec.
- Consecuencia: el texto se aplica en §3.2, RF-S02-03 y Anexo A de la spec S02; se conserva la distinción entre grano, frecuencia de observación y frecuencia de actualización.
- Límite: no se declara una periodicidad de actualización que las fuentes no demuestran.

### DEC-033 · Aprobación del Plan S02 v0.1 y autorizaciones por fase

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: aprobar y guardar `plan.md` v0.1 y `tasks.md` de S02. El plan adopta la **vía PPT nativa**: la diapositiva 1 de la copia de SRC-203 conserva el ejemplo sin modificar, la 2 contiene el diagrama y las 3+ el mapa Silver como tabla editable de siete columnas; el PDF se exporta con PowerPoint COM desde una copia de trabajo sin la diapositiva 1. Se mantienen autorizaciones separadas: Build (T01–T10), Audit (T11), Fix (T12, solo con hallazgos), nueva Audit (T13.1) y Close (T13.2). La aprobación del plan no autoriza ejecutar ninguna fase.
- Fundamento: aprobación explícita del usuario y correcciones solicitadas sobre cobertura de auditoría, calificación de COM, riesgo DCAM, cierre y WMS.
- Consecuencia: T01–T13 quedan pendientes. PowerPoint COM y Excel COM se califican por separado en T01 (V02A y V02B) y no se consideran herramientas de ejecución hasta superar esa prueba. La auditoría deberá cubrir 11 RF + 9 RNF + 10 CA = 30 elementos.
- Límite: no se crean `AUDIT.md`, evidencia, resultados, temporales ni entregables de S02; no se modifican Excel, PowerPoint, Power BI, referencias ni Silver. El cierre exige 30/30 elementos auditados, los 10 CA demostrados, ningún hallazgo bloqueante y aprobación explícita, sin que una limitación sustituya un requisito incumplido.

## Decisiones pendientes

| ID | Tema | Qué falta resolver | Momento o dependencia |
| --- | --- | --- | --- |
| PEN-001 | Decisión del tablero | Resuelta por DEC-016: Jefatura de Operaciones, revisión semanal y prioridades acordadas. | S01–S02. |
| PEN-002 | KPI | Candidatos definidos en DEC-017; falta selección final de 5–8, responsables, metas y umbrales. | S02 y desarrollo progresivo. |
| PEN-003 | Brecha DCAM | Resuelta el 2026-10-21: brecha A con componente C4 respaldado por DEC-026; dimensión Evidencia, puntaje 1 tentativo y confianza baja. Sujeta a auditoría y validación docente. | S01. |
| PEN-004 | Merma | Cantidades acordadas en DEC-017; falta decidir la medida económica por valor y justificar su impacto. | Definición de KPI y S10. |
| PEN-005 | Lecturas térmicas límite | Tratamiento de 26 casos sin cambiar etiquetas por suposición. | S03–S04 y aclaración de fuente. |
| PEN-006 | Particiones y horizonte futuro | Tratamiento de viajes compartidos, fronteras temporales y fin de viaje. | Validación analítica/predictiva. |
| PEN-007 | Modelo temporal de costos | Conexión de periodo_mes y significado de cada filtro temporal. | S06. |
| PEN-008 | Centro del viaje | Uso e interpretación del centro base del camión. | Modelo, visuales y RLS. |
| PEN-009 | Agregado por viaje | Cargarlo o conservarlo como control sin carga. | S05–S06. |
| PEN-010 | Componente predictivo | Integrar modelo previo o entrenar uno; definir alcance y evidencia. | Contexto y specs pertinentes. |
| PEN-011 | Recomendación What-if | Costos de falsas alarmas y omisiones, capacidad y criterio de aceptación. | S10. |
| PEN-012 | Autorizaciones | Roles, correos ficticios, centros múltiples y pruebas negativas viables. | S11. |
| PEN-013 | Entorno | Versiones, herramientas, comandos y prueba del MCP si se adopta. | Antes del Build dependiente. |
| PEN-014 | Material faltante | Auditoría Bronze–Silver recibida como DATA-006; faltan rúbrica v4, guías S12–S13 y lista de comisionamiento. | Antes de cerrar requisitos afectados. |
| PEN-015 | Diferencias entre plantillas | Estados de mejoras, polaridad en rango y formato de entregas. | Specs afectadas. |
| PEN-016 | Convención final PBIP | Nombre, formato del informe y estructura efectiva de la versión Desktop. | Plan de implementación. |
| PEN-017 | Origen y propietarios de las fuentes | Los sistemas de origen y los propietarios de las cinco fuentes no están documentados; S02 los registra como «por acordar». Documentarlos no los resuelve. | Por acordar; seguimiento del Grupo 06. |
| PEN-018 | Frecuencia de actualización | La periodicidad de actualización de las tablas no está documentada; S02 la distingue de la frecuencia de observación y la marca «por acordar». | Por acordar. |
| PEN-019 | Validación empresarial del centro | Falta un validador que confirme el significado de `centro_distribucion` y `centro_distribucion_base`; la brecha se registra como ausencia documentada (DEC-031). | Por acordar; uso en filtros y RLS en S06 y S11. |

## Historial del registro

- 2026-10-20: registro inicial. Se separan acuerdos del usuario, restricciones docentes y decisiones pendientes. No se registran como implementadas las decisiones documentales ni técnicas que carecen de verificación.
- 2026-10-20: se añaden DEC-016 a DEC-020 sobre decisión, KPI candidatos, brecha DCAM, WMS y responsabilidad de revisión. Se actualizan PEN-001 a PEN-004 y PEN-014. La brecha DCAM y la selección de KPI conservan carácter tentativo o provisional.
- 2026-10-20: se añade DEC-021 para rectificar la spec S01 y se actualiza DEC-017 con fórmula de merma, denominadores contextuales y momentos de selección, metas y responsables.
- 2026-10-20: se añaden DEC-022 y DEC-023 sobre el componente DCAM aplicable y la verificación decimal/Flota; se actualiza la nota de alcance de DEC-018 y PEN-003.
- 2026-10-20: se añade DEC-024: corrección de la frase de autorización de la spec, aprobación del plan v0.2 y de las tareas alineadas, con autorización limitada a T01.
- 2026-10-20: se actualiza DEC-019 sin cambiar la decisión: T02 guardó EV-S01-WMS en `evidence/S01/wms_contrast.md`; la auditoría sigue pendiente.
- 2026-10-21: se añaden DEC-026 y DEC-027. C4 queda respaldado por aprobación del usuario con SRC-208 como referencia complementaria; Rodrigo Tucuman queda designado para compartir pantalla. Se actualizan DEC-013, DEC-018, DEC-022 y PEN-003. T07 se completa; S01 permanece abierto a auditoría.
- 2026-10-27: se añaden DEC-028 a DEC-032 y PEN-017 a PEN-019. Se registra la aprobación de la spec S02 v0.4, el mapa de cinco fuentes con WMS fuera, los KPI tácticos, la brecha como ausencia documentada y el grano/frecuencia de inventario. No se reescriben decisiones ni pendientes anteriores.
- 2026-10-27: se añade DEC-033. Se aprueba el Plan S02 v0.1 con vía PPT nativa, auditoría de 30 elementos, calificación separada de PowerPoint COM y Excel COM en T01 y autorizaciones independientes para Build, Audit, Fix, nueva Audit y Close. Las tareas permanecen pendientes y Build no se autoriza.


### DEC-015 · Skill reutilizable por fases

- Fecha: 2026-10-20.
- Estado: confirmada por el usuario; archivos creados, prueba en OpenCode pendiente.
- Decisión: skill local andinalog-sdd-workflow con Specify, Plan, Build, Audit, Fix y Close y plantillas compartidas. docs/prompts.md mantiene invocaciones en lugar de duplicar el procedimiento.
- Consecuencia: se reutiliza el flujo por hito sin copiar requisitos de negocio a la skill ni autorizar automáticamente fases posteriores.


### DEC-025 · MCP local Power BI por proyecto

- Fecha: 2026-10-21.
- Estado: autorizado por el usuario; configuración creada, conexión al modelo pendiente.
- Decisión: registrar powerbi-authoring-local en opencode.json de la raíz; usar el paquete oficial Microsoft 1.0.0 sin aceptar EULA por defecto ni alterar configuración global.
- Fundamento: acceso local a modelos Desktop/PBIP para construcción y auditoría de alcance autorizado.
- Límite: no automatiza toda la interfaz ni acredita pruebas visuales o S01. La aceptación de licencia requiere autorización explícita del usuario después de revisarla.
- Fuentes: https://learn.microsoft.com/en-us/power-bi/developer/mcp/power-bi-authoring-mcp y https://docs.opencode.ai/docs/mcp-servers/.

- Comprobación posterior: opencode mcp list confirmó servidor conectado; conexión al modelo y EULA siguen pendientes.

### DEC-026 · Componente C4 y respaldo de la brecha DCAM

- Fecha: 2026-10-21.
- Estado: confirmada por el usuario.
- Decisión: asignar la brecha A al componente **C4 · Conocimiento de los datos del negocio**, dimensión **Evidencia**, puntaje **1 — Incipiente** tentativo y confianza **baja**. El hecho se formula como «No encontramos una definición explícita de `centro_distribucion` en las fuentes revisadas».
- Fundamento: aprobación explícita del usuario. La lista C1–C8 se consultó en SRC-208 `Instrucciones!B10` como referencia complementaria; el PDF SRC-202 sigue siendo la referencia metodológica. La brecha es semántica y de conocimiento, no de calidad, tecnología, operación ni gobierno.
- Consecuencia: T07 queda cubierta en su condición DCAM y RF-S01-07/CA-S01-03 pueden auditarse con C4 respaldado. Se actualizan DEC-013, DEC-018, DEC-022, PEN-003 y la trazabilidad de S01.
- Límite: el Excel no contiene el mapeo de la brecha ni se editó; el respaldo es la aprobación del usuario, no una atribución al libro. No se afirma ausencia empresarial ni se evalúa madurez general de C4. El puntaje sigue sujeto a validación docente y auditoría.

### DEC-027 · Persona que compartirá pantalla en S02

- Fecha: 2026-10-21.
- Estado: confirmada por el usuario.
- Decisión: **Rodrigo Tucuman** compartirá pantalla en S02.
- Fundamento: designación explícita del usuario; sustituye la referencia grupal anterior.
- Consecuencia: se cubre la condición de persona identificada de T07. La calidad de la demostración y el contenido de S02 se verifican en la auditoría y en el hito correspondiente.
- Límite: la designación no acredita que la pantalla haya sido compartida ni que S02 esté ejecutado.

### DEC-034 · Presupuesto mínimo de artefactos

- Fecha: 2026-10-27.
- Estado: confirmada por solicitud del usuario y aplicada al repositorio.
- Decisión: cada hito conserva un único `evidence.md`, un único `validation.json` y un único `AUDIT.md`; los planes agrupan trabajo por entregable y mantienen entre tres y siete tareas orientadas a resultados.
- Consecuencia: se consolidó la evidencia de S02, se retiraron temporales, capturas duplicadas, resultados por microtarea y dependencias descargadas. `MEMORY.md` conserva solo el estado vigente.
- Excepción: se permite otro artefacto únicamente si un criterio de aceptación identifica por qué no puede incorporarse a los archivos existentes. Las capturas Desktop indispensables de S01 se conservan.
- Límite: la consolidación no altera los entregables ni cierra A-S02-001 o RNF-S02-06.

### DEC-035 · Aprobación de la spec S03 v0.1

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: aprobar y guardar la spec S03 v0.1 con cinco fuentes oficiales, `RutaSilver`, región Inglés (Estados Unidos), privacidad Organizacional propuesta y sujeta a comprobación Desktop, perfil sobre todo el conjunto, cinco filas de linaje y tablas fuente de cinco KPI.
- Consecuencia: Specify de S03 queda completada; Plan y Build permanecen sin iniciar. WMS sigue fuera del modelo y las excepciones se documentan sin tratarlas antes de S04.
- Límite: la aprobación no acredita región, privacidad, perfil, actualización ni contenido del libro; esas comprobaciones corresponden a Build y Audit.

- 2026-10-27: se añade DEC-035. La spec S03 v0.1 queda aprobada y guardada; no se autoriza Plan ni Build.

### DEC-036 · Aprobación del Plan S03

- Fecha: 2026-10-27.
- Estado: confirmada por el usuario.
- Decisión: aprobar el Plan S03 con tres tareas de Build orientadas a resultados y tres tareas para Audit, Fix y Close. Se mantienen un único `evidence.md`, un único `validation.json` y un único `AUDIT.md`.
- Consecuencia: Specify y Plan quedan completados; T01–T06 permanecen pendientes. El siguiente alcance posible es Build T01, sujeto a autorización independiente.
- Límite: la aprobación no autoriza abrir Desktop, modificar el PBIP o el libro, generar evidencia ni ejecutar Build.

- 2026-10-27: se añade DEC-036. Plan y tareas S03 quedan aprobados y guardados; Build permanece sin iniciar.

### DEC-037 · Cierre de S03

- Fecha: 2026-10-28.
- Estado: confirmado por autorización explícita del usuario para completar todas las tareas pendientes.
- Decisión: cerrar S03 después de la ronda 02 con 21/21 requisitos y criterios conformes. Se conservan tres capturas indispensables: región, privacidad y Power Query con `RutaSilver` y perfil completo.
- Consecuencia: T01–T06 quedan completadas y `A-S03-001` cerrado. S04 permanece sin iniciar.
- Límite: la privacidad de cuatro fuentes se apoya en revisión directa y confirmación del usuario; la captura representativa conserva la quinta y la lista completa. No se resolvieron las excepciones trasladadas a S04.

- 2026-10-28: se añade DEC-037. S03 queda cerrado; S04 requiere autorización independiente.
