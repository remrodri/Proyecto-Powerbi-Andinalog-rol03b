# Tareas — S01 Preparación

Spec: [spec.md](spec.md), v0.4 corregida, aprobada.
Plan: [plan.md](plan.md), v0.2, aprobado por el usuario el 20 de octubre de 2026.
Tareas aprobadas y ejecutadas: T01–T10 completadas; cierre de S01 aprobado el 2026-10-22. S02 no iniciado.

- [x] **T01 — Verificar entradas y entorno.**
  - Requisitos: RF-S01-05/10; RNF-S01-03/06/08/09.
  - Depende de: plan aprobado y autorización del alcance.
  - Trabajo: comprobar rutas/archivos, runtime/bibliotecas y disponibilidad real de Desktop; obtener tamaños/hashes y registrar herramientas y límites. No instalar ni iniciar otro trabajo por defecto.
  - Artefactos: validation/results/S01/source_manifest.json; registro de entorno en evidence/S01/desktop_checks.md inicialmente como procedimiento pendiente.
  - Prueba: P01; verificación no destructiva de entorno.
  - Hecho cuando: entradas identificadas, herramientas y limitaciones documentadas, originales sin cambios. Desktop no disponible queda como bloqueo de T05, no como prueba ejecutada.

- [x] **T02 — Reproducir inventario, procedencia y contraste.**
  - Requisitos: RF-S01-03/04/11; soporte de RF-S01-07/08; RNF-S01-01/02/03/06/08.
  - Depende de: T01 para herramientas de lectura; no de Desktop.
  - Trabajo: crear control de lectura, contar cinco fuentes completas, comprobar claves y observaciones necesarias; transcribir los cinco registros DATA-006 con sus columnas reales; reproducir cruces WMS y registrar fuentes auxiliares usadas sin importarlas al modelo.
  - Artefactos: validation/checks/s01_inventory.py, validation/results/S01/csv_checks.json, evidence/S01/provenance.md y wms_contrast.md.
  - Pruebas: P01/P02/P06; resultados exactos según plan y discrepancias explícitas.
  - Hecho cuando: controles ejecutados, resultados reproducibles y evidencia de contraste/procedencia guardada sin atribuir al CSV oficial los cruces propios. Diferencias materiales investigadas o reportadas como bloqueo, nunca maquilladas.

- [x] **T03 — Consolidar preparación S01 en Markdown.**
  - Requisitos: RF-S01-01/02/03/04/07/08; RNF-S01-01/02/04/05/08.
  - Depende de: T02 y decisiones ya aprobadas. El respaldo del componente DCAM aplicable puede seguir pendiente (DEC-022).
  - Trabajo: decisión, cinco filas con grano/claves/conteos, observaciones clasificadas, Grupo 06 como revisión, cinco candidatos y apoyo con fórmulas contextuales, DCAM tentativa con componente aplicable y dudas. No nuevas metas ni KPI por valor.
  - Artefacto: evidence/S01/preparation.md.
  - Prueba: P03, cruce con spec y resultados de T02.
  - Hecho cuando: documento completo y consistente con acuerdos, pendiente de respaldo del componente DCAM visible y ninguna afirmación de Desktop inventada. Esto no cierra RF-S01-07 ni S01 mientras falte respaldo del componente aplicable.

- [x] **T04 — Completar copia de seguimiento y comprobar correspondencia.**
  - Requisitos: RF-S01-08/09; RNF-S01-04/05/06.
  - Depende de: T03 y herramienta XLSX disponible; preservar una copia previa si existe.
  - Trabajo: copiar plantilla a deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx; completar identificación/inventario y columnas KPI/decisión de S01, conservar fórmulas y hojas futuras; DCAM y apoyo se enlazan al Markdown porque no tienen campos propios en esa hoja.
  - Artefactos: libro y evidence/S01/template_mapping.md.
  - Prueba: P04, cotejo de valores/fórmulas y revisión visual de hojas editadas; original por hash.
  - Hecho cuando: copia legible y verificaciones demuestran correspondencia y ausencia de cambios no autorizados. Si falta revisión visual, la tarea queda pendiente de esa comprobación.

- [x] **T05 — Ejecutar y documentar inspección Desktop.**
  - Requisitos: RF-S01-05/06/10; RNF-S01-06/07/08/09.
  - Depende de: T01, Desktop disponible y autorización para esa ejecución; puede realizarla Grupo 06.
  - Trabajo: importar solo cinco fuentes, RutaSilver y tipado mínimo permitidos; comprobar archivo, filas y columnas; en tablas con campos decimales, lectura decimal; en flota, enteros y fechas y ausencia de campos decimales; sin corregir anomalías. No relaciones ni medidas. Guardar proyecto mínimo solo si se acuerda.
  - Artefactos: evidence/S01/desktop_checks.md y screenshots/; proyecto opcional en powerbi/.
  - Prueba: P05, tablas identificadas, fecha/versión, archivo, filas y columnas; decimales donde correspondan; para flota, enteros y fechas y documentación de ausencia de campos decimales (spec v0.4, DEC-023).
  - Hecho cuando: evidencia Desktop auténtica cubre las cinco tablas con archivo, filas, columnas y criterio decimal/Flota; se explican diferencias; instrucciones sin ejecutar no completan la tarea. Sin Desktop: bloqueada, continuar tareas independientes.

- [x] **T06 — Conciliar documentos después de Desktop.**
  - Requisitos: RF-S01-03/04/05/06/09; RNF-S01-01/02/05/07.
  - Depende de: T04 y T05.
  - Trabajo: comparar observación Desktop con controles, inventario y copia; actualizar resultados reales sin corregir fuentes ni alterar requisitos. Mantener discrepancias abiertas.
  - Artefactos: registros de T03/T04/T05 afectados y MEMORY.md.
  - Pruebas: P03/P04/P05.
  - Hecho cuando: cada dato del inventario tiene procedencia y evidencia coherentes; no se reemplaza un resultado Desktop por el esperado del CSV.

- [x] **T07 — Resolver condiciones humanas y preparar traspaso S02.**
  - Requisitos: RF-S01-07; condiciones de cierre y RNF-S01-01/02/09.
  - Depende de: T03; para finalizar, respuesta del usuario/docente.
  - Trabajo: identificar el componente DCAM aplicable y obtener su respaldo (DEC-022); designación de pantalla, registrar fuente/aprobación y revisar puntaje si cambia evidencia; reunir decisión, inventario, candidatos, DCAM y pendientes.
  - Artefactos: evidence/S01/s02_handoff.md, preparation.md y decisiones/fuentes cuando corresponda.
  - Prueba: P07.
  - Hecho cuando: componente aplicable identificado y respaldado y persona identificada; si falta respaldo, la tarea y CA-S01-03 siguen pendientes. Grupo 06 sin persona concreta no resuelve esa exigencia. Borrador de traspaso puede hacerse antes, tarea permanece abierta. **Cumplido el 2026-10-21:** C4 respaldado por DEC-026 y Rodrigo Tucuman, integrante del Grupo 06, designado en DEC-027; verificación en T08.

- [x] **T08 — Auditar S01 sin modificar lo auditado.**
  - Requisitos: RF-S01-01 a RF-S01-11, RNF-S01-01 a RNF-S01-09, CA-S01-01 a CA-S01-06 y condiciones de cierre.
  - Depende de: alcance de auditoría autorizado; una ronda parcial puede revisar lo ya disponible antes de T05/T07, sin declarar conformidad global.
  - Trabajo: revisar evidencia independiente, original intacto, copia, Desktop, datos y condiciones humanas. Crear o añadir ronda al único AUDIT.md; no corregir artefactos durante auditoría.
  - Prueba: P08; matriz requisito → evidencia → resultado, hallazgos estables.
  - Hecho cuando: ronda documentada con veredicto limitado al alcance. Esta casilla acredita ejecución de la ronda, no cumplimiento del hito; los fallos y pendientes siguen bloqueando cierre. Nuevas rondas se conservan en el mismo documento.

- [x] **T09 — Corregir hallazgos autorizados y volver a auditar.**
  - Requisitos: los afectados por cada ID; RNF de integridad/trazabilidad.
  - Depende de: T08 y autorización de correcciones.
  - Trabajo: Build separado para resolver hallazgos; actualizar pruebas/documentación y después Audit independiente por fase. No modificar spec ni cambiar criterios para lograr aprobación sin autorización.
  - Artefactos: los afectados y AUDIT.md, con historial preservado.
  - Hecho cuando: cada hallazgo que impide cumplimiento está cerrado por nueva evidencia de auditoría. Si no hubo hallazgos, registrar no aplica con fundamento; no inventar correcciones.

- [x] **T10 — Proponer cierre de S01.**
  - Requisitos: todos; CA y condiciones de cierre.
  - Depende de: T06, T07, auditoría conforme y T09 resuelta o no aplicable.
  - Trabajo: presentar resumen de aceptación y pendientes de etapas posteriores, solicitar aprobación de cierre. Actualizar estado de spec y memoria solo tras esa aprobación.
  - Artefactos: AUDIT.md, MEMORY.md y estado de spec si se aprueba.
  - Hecho cuando: todos criterios y condiciones demostrados y cierre explícitamente aprobado; no iniciar S02 automáticamente.

## Cobertura de aceptación

| Criterio | Tareas principales |
| --- | --- |
| CA-S01-01 | T03, T08 |
| CA-S01-02 | T02, T03, T06, T08 |
| CA-S01-03 | T03, T07, T08 |
| CA-S01-04 | T05, T06, T08 |
| CA-S01-05 | T03, T04, T08 |
| CA-S01-06 | T04, T06, T08 |
| Componente DCAM aplicable y persona de pantalla | T07, T08, T10 |

## Registro de ejecución

- 2026-10-20 · T01 ejecutada: fuentes y referencias localizadas, SHA-256 y tamaños registrados; P01 verificó 10/10 huellas sin cambios; Python, bibliotecas y paquete Desktop identificados. Evidencia: `validation/results/S01/source_manifest.json` y `evidence/S01/desktop_checks.md`. No se importaron tablas, no se completaron plantillas y no se ejecutó T02.
- 2026-10-20 · T02 ejecutada: control reproducible de lectura creado y ejecutado; cinco fuentes oficiales con filas/columnas y claves conformes; DATA-006 transcrito con cinco registros oficiales; WMS contrastado sin importarlo; P01/P02/P06 conformes y 0 discrepancias materiales. Evidencia: `validation/checks/s01_inventory.py`, `validation/results/S01/csv_checks.json`, `evidence/S01/provenance.md` y `evidence/S01/wms_contrast.md`. No se abrió Power BI, no se importaron tablas, no se completaron plantillas y no se ejecutó T03.
- 2026-10-20 · T03 ejecutada: `evidence/S01/preparation.md` consolida decisión, inventario de cinco fuentes, observaciones clasificadas, cinco KPI candidatos, medida de apoyo y brecha DCAM tentativa con C4 propuesto, retirado en la revisión posterior. P03 conforme con pendientes declarados; P03 no acredita cierre DCAM. Respaldo DCAM, persona de pantalla y pruebas Desktop siguen pendientes. Se actualizaron las menciones de EV-S01-WMS en spec, sources y DEC-019 sin cambiar requisitos. No se completó el Excel y no se ejecutó T04.
- 2026-10-20 · Revisión T03: se verificó que C4 procedía de la lista histórica C1–C8 y que SRC-202 no la enumera; no se localizó decisión que autorizara C4. Se sustituyó por «componente pendiente de identificación y respaldo» en `preparation.md`, conservando el historial, la dimensión Evidencia, el puntaje 1 tentativo y la confianza baja. No se ejecutó T04.
- 2026-10-20 · T04 ejecutada: copia `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` creada desde la plantilla, con identificación, cinco fuentes, cinco KPI y decisiones S01. Se limpiaron los campos de ejemplo, se conservaron 50 fórmulas y las hojas futuras, y el original mantuvo su SHA-256. P04 pasa: 0 diferencias fuera del rango autorizado, Excel 16.0 abrió/calculó/exportó sin reparación y la revisión visual de las celdas editadas consta en `evidence/S01/template_mapping.md` y los PDF enlazados. No se asignó DCAM, no se inventaron responsables, no se abrió Power BI y no se ejecutó T05.
- 2026-10-21 · T05 ejecutada y confirmada: evidencia Desktop auténtica de las cinco tablas en `evidence/S01/screenshots/` y `desktop_checks.md`, con archivo, filas, columnas, decimales y Flota sin campos decimales. Productos 120×7, Flota 100×6, Inventario 7.782×12, CostosAlmacen 144×5 y Telemetria 191.710×15; los totales exactos de las tres últimas se acreditaron por MCP porque el preview mostraba `Rows: 99+`. El usuario confirmó la finalización. No se reimportaron datos, no se modificó el PBIP y no se inició T06 hasta esa confirmación.
- 2026-10-21 · T06 ejecutada: conciliación de solo lectura entre `desktop_checks.md`, `mcp_model_checks.md`, `csv_checks.json`, `preparation.md` y la copia Excel. Las cinco fuentes coinciden en archivo, filas, columnas, grano, clave, brecha y responsable; los cinco nombres de KPI y sus decisiones coinciden con el Markdown; 0 diferencias de contenido y 0 discrepancias materiales. No se recalcularon valores de KPI. Se documentaron como diferencias de representación el separador de miles, las fechas ISO frente al formato regional, el preview `Rows: 99+`, la columna interna `RowNumber` y la reserialización del Excel. Huellas sin cambios: Excel `E7F09B0A...DB74F1`, plantilla `0CCC4A53...D2DF30` y PBIP `F8712089...8A1CCE`. No se modificaron datos ni requisitos; no se inició T07 ni se declaró cerrado S01. Evidencia: `preparation.md` sección 9, `template_mapping.md` sección 7 y `desktop_checks.md` sección final.
- 2026-10-21 · T07 parcial (solo documental): se creó `evidence/S01/s02_handoff.md` con decisión, inventario, KPI candidatos, evidencias T02–T06, límites y pendientes. La revisión de SRC-202, SRC-101, SRC-201 y las demás referencias locales no localizó una lista activa C1–C8 ni un respaldo del componente aplicable; el componente se mantiene pendiente y no se reintrodujo C4 por inferencia. El usuario indicó **Grupo 06** para compartir pantalla; el criterio de T07 sigue exigiendo persona identificada, por lo que se registra la designación grupal sin marcarla completa. T07 permanece `[ ]`, no se inició auditoría y no se declaró cerrado S01.
- 2026-10-21 · T07 completada y verificada (P07: PASA): el usuario aprobó C4, Conocimiento de los datos del negocio, para la brecha A y designó a **Rodrigo Tucuman, integrante del Grupo 06**, para compartir pantalla. Se consultó `Instrucciones!B10` de SRC-208 como referencia complementaria (SHA-256 `D6FE317D...A294686`), sin editar ni completar el Excel. Se registraron DEC-026/027, se actualizaron `s02_handoff.md`, `preparation.md`, `decisions.md`, `sources.md`, `context.md`, `spec.md` y esta tarea. El hecho se limita a las fuentes revisadas y el puntaje 1 sigue tentativo. No se inició T08 ni se declaró cerrado S01.
- 2026-10-22 — T08 completada: rondas 01 y 02 documentadas en `AUDIT.md`. La ronda 01 dejó 24/26 y abrió A-S01-001; la ronda 02 verificó 13/13 huellas, reconstruyó exactamente los TMDL históricos y cerró el hallazgo con 26/26. No se modificó el modelo auditado. S01 no se cerró en esa fase.
- 2026-10-22 — T09 completada: corrección documental de A-S01-001 en `mcp_model_checks.md`, con historial T05 preservado y `cache.abf` marcado como estado local variable. La nueva evidencia de la ronda 02 cerró el hallazgo; no se modificaron modelo ni datos.
- 2026-10-22 — T10 completada: el usuario aprobó el cierre de S01 con las limitaciones documentadas y las precisiones de RF-S01-06, RF-S01-07, RF-S01-09, CA-S01-03, CA-S01-04 y CA-S01-06. Se actualizaron el estado de la spec, `AUDIT.md` y `MEMORY.md`; los pendientes trasladados a S02, S08 y S11 no se declaran resueltos. No se modificaron modelo ni entregables y no se inició S02.
