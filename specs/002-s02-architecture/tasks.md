# Tareas — S02 Decisión, arquitectura y mapa Silver

Spec y plan aprobados: `specs/002-s02-architecture/spec.md` v0.4 (2026-10-27) y `specs/002-s02-architecture/plan.md` v0.1 (2026-10-27).
Estado: **Build en curso. T01–T09 completadas; T10–T13 pendientes.** Audit, Fix y Close no están autorizados.

- [x] **T01 — Inventario inicial, cuatro huellas y calificación separada de COM.**
  - Requisitos: RNF-S02-03, RNF-S02-06, RNF-S02-07; base de RF-S02-08 y RF-S02-09; CA-S02-08 y CA-S02-09.
  - Depende de: autorización de Build.
  - Artefactos: `validation/results/S02/initial_manifest.json`, `evidence/S02/tooling.md`, archivos temporales en `work/S02/`.
  - Puede modificar: manifiesto, registro de herramientas y temporales de `work/S02/`.
  - Debe preservar: los cuatro objetos con huella y, adicionalmente, el PBIP.
  - Verificación y evidencia: registrar las **cuatro huellas obligatorias**:
    1. SRC-201, plantilla Excel original.
    2. SRC-203, plantilla PowerPoint original.
    3. Copia Excel de seguimiento `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`.
    4. Spec S02 aprobada `specs/002-s02-architecture/spec.md`.
    - Registrar además, sin modificar, el hash del PBIP `powerbi/AndinaLog_03B.pbip` como artefacto preservado.
    - Calificar **PowerPoint COM**: copiar SRC-203 a `work/S02/com_ppt_test.pptx`; abrirla, guardarla, renderizar una diapositiva y exportar un PDF.
    - Calificar **Excel COM**: copiar el XLSX de seguimiento a `work/S02/com_excel_test.xlsx`; abrirlo, recalcularlo y exportar a PDF las hojas `S02 Mapa Silver` y `Fichas KPI`, sin guardar la copia.
  - Hecho cuando: 4/4 huellas registradas y verificadas; PowerPoint abre, guarda, renderiza y exporta sin reparación; Excel abre, recalcula y exporta sin reparación; los entregables conservan su hash. Si una calificación falla, se registra el fallo y se detiene solo la parte dependiente.
  - Estado: **completada el 2026-10-27**. V02A y V02B calificadas; evidencia en `evidence/S02/tooling.md` y `validation/results/S02/initial_manifest.json`.

- [x] **T02 — Contrato de contenido normativo desde la spec.**
  - Requisitos: RF-S02-01 a RF-S02-07 y RF-S02-11; RNF-S02-01, RNF-S02-02 y RNF-S02-04; CA-S02-01 a CA-S02-07 y CA-S02-10.
  - Depende de: T01.
  - Artefactos: `work/S02/content.json`, `work/S02/content.md`, `validation/checks/s02_content.py`, `validation/results/S02/content_checks.json`.
  - Puede modificar: los cuatro archivos indicados.
  - Debe preservar: spec, SRC-201/203, copia XLSX, Silver y referencias.
  - Verificación y evidencia: transcribir sin reinterpretar; marcar propuestas y referencias; incluir el riesgo DCAM con sus cuatro componentes aprobados; ejecutar el validador.
  - Hecho cuando: el validador confirma 5 filas de mapa, 5 KPI tácticos, frecuencia exacta de inventario, `dias_en_almacen`, origen «no documentado», pendientes «por acordar» y **WMS ausente de las cinco filas del mapa**. WMS solo puede aparecer en una nota separada de contraste no cargado.
  - Estado: **completada el 2026-10-27**. 26/26 controles pasan; JSON y Markdown coinciden materialmente. Evidencia en `validation/results/S02/content_checks.json`.

- [x] **T03 — Copia editable de la presentación.**
  - Requisitos: RF-S02-02, RF-S02-09; CA-S02-02, CA-S02-09.
  - Depende de: T01.
  - Artefactos: `deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx`, `validation/results/S02/pptx_copy_checks.json`.
  - Puede modificar: solo el PPTX de destino y el resultado de verificación.
  - Debe preservar: SRC-203 intacto; diapositiva 1 sin cambios.
  - Verificación y evidencia: hash de SRC-203; copia binaria; apertura con `python-pptx` en solo lectura; listado de diapositivas, formas y textos.
  - Hecho cuando: el destino existe, conserva 2 diapositivas y 32 formas por diapositiva, la diapositiva 1 mantiene su texto y SRC-203 conserva su hash.
  - Estado: **completada el 2026-10-27**. Copia binaria exacta: 38.618 bytes y SHA-256 `36E4E9AE…F96516`; 13/13 controles pasan. Evidencia en `validation/results/S02/pptx_copy_checks.json`.

- [x] **T04 — Completar la diapositiva 2 de arquitectura.**
  - Requisitos: RF-S02-01, RF-S02-02, RF-S02-04, RF-S02-05, RF-S02-11; RNF-S02-02, RNF-S02-04; CA-S02-01, CA-S02-02, CA-S02-04, CA-S02-05.
  - Depende de: T02, T03 y V02A.
  - Artefactos: PPTX de T03, `validation/results/S02/slide2_checks.json`, `evidence/S02/t04_architecture.md` y `evidence/S02/screenshots/s02_t04_architecture_slide.png`.
  - Puede modificar: solo textos de la diapositiva 2.
  - Debe preservar: diapositiva 1, geometría, flechas, colores y notas.
  - Verificación y evidencia: sustituir con estos contenidos y comparar contra el contrato de T02:
    - Encabezado: `PROYECTO INTEGRADOR · HITO S02 · EQUIPO 06`.
    - Decisión: `La Jefatura de Operaciones decide cada semana dónde priorizar controles térmicos por producto y camión y qué lotes o centros revisar por vencimiento y merma.`
    - Origen: `No documentado por archivo; por acordar. No se atribuye ERP, WMS, TMS ni telemetría a estas tablas.`
    - Silver: `Cinco CSV oficiales (DATA-001 a DATA-005). Una fila = una lectura, un producto, un camión, un lote o un centro-mes.`
    - Power Query: `RutaSilver + File.Contents + Csv.Document; Encabezados y Tipado. Sin cambios en S02.`
    - Modelo: `5 tablas Import; 0 relaciones y 0 medidas. Dimensiones y relaciones propuestas para S06.`
    - Indicador: `% de viajes con desviación (táctico). Fórmula y unidad en Fichas KPI.`
    - Brecha: `No encontramos definición explícita de centro_distribucion · C4 Conocimiento de los datos · Evidencia · 1 Incipiente. Ausencia documentada; no resuelta.`
    - Riesgo: `Interpretar incorrectamente qué representa el centro y usarlo en filtros o conclusiones.`
    - Hecho observado: `Los cruces revisados no encontraron discrepancias entre centro WMS y centro base en los 8.000 viajes emparejados; esta consistencia no demuestra significado empresarial.`
    - Control principal: `Documentar la ausencia de definición, los usos y límites conocidos, y solicitar la definición y validación empresarial.`
    - Control complementario: `No usar centro_distribucion_base como ruta u origen real; dim_centro y los controles de claves son propuestas posteriores.`
    - Pendiente: `Definición y validación de centro_distribucion: seguimiento Grupo 06; validador por acordar. No resuelto.`
  - Hecho cuando: los textos conservan los significados de la spec —se admite compactación para ajustar el espacio sin eliminar significados—; el riesgo no atribuye una asignación incorrecta observada; la brecha no se declara resuelta; no hay desbordamiento; la diapositiva 1 no cambió; SRC-203 conserva su hash.
  - Estado: **completada el 2026-10-27**. 38/38 controles pasan. Se modificaron 10 formas de texto y se conservó la geometría de las 32; diapositiva 1 con XML, texto e inventario idénticos a T03; SRC-203 intacto. PowerPoint COM 16.0 abrió sin reparación, renderizó la diapositiva 2 a PNG 1920×1080 y cerró sin guardar. Evidencia en `slide2_checks.json`, `t04_architecture.md` y la captura. T05 no se inició.

- [x] **T05 — Añadir el mapa Silver como tabla editable.**
  - Requisitos: RF-S02-03, RF-S02-05; RNF-S02-04; CA-S02-03, CA-S02-04.
  - Depende de: T02, T03, T04.
  - Artefactos: diapositivas nuevas desde la 3 del PPTX, `validation/results/S02/pptx_checks.json`.
  - Puede modificar: solo diapositivas nuevas del mapa.
  - Debe preservar: diapositivas 1 y 2, geometría del diagrama y SRC-203.
  - Verificación y evidencia: crear una o más diapositivas 16:9 con tabla real de 7 columnas y encabezado repetido; incluir DATA-001 a DATA-005; repartir por filas completas; fuente mínima 8 pt; ajustar altura de fila antes que reducir fuente; pie con archivo y hoja de origen.
  - Hecho cuando: existen exactamente 5 filas de datos, 7 columnas por página, encabezado repetido, ninguna fila partida, ninguna columna separada, **WMS ausente de las cinco filas** y todas las celdas son legibles. Si WMS se menciona como contraste, va en una nota separada, nunca como sexta fila.
  - Estado: **completada el 2026-10-27**. Se añadieron 2 diapositivas 16:9 (3 y 4): `Mapa Silver — 1/2` con DATA-001 a DATA-003 y `Mapa Silver — 2/2` con DATA-004 y DATA-005. Tablas nativas de 7 columnas, cabeceras repetidas, fuente de tabla 10.5 pt y cero filas partidas. La identificación de archivo/tabla está en la primera columna; no se añadió texto flotante fuera de las celdas. **45/45 controles pasan** en `pptx_checks.json`; diapositivas 1 y 2 conservan XML, texto, inventario y geometría de T04; SRC-203, Excel, PBIP y los cinco Silver permanecen intactos; no se creó PDF ni se editó Excel. Evidencia: `evidence/S02/t05_silver_map.md` y las capturas de las diapositivas 3 y 4. T06 no se inició.

- [x] **T06 — Actualizar `S02 Mapa Silver`.**
  - Requisitos: RF-S02-03, RF-S02-08; CA-S02-03, CA-S02-08.
  - Depende de: T01, T02.
  - Artefactos: copia XLSX de seguimiento, `validation/results/S02/xlsx_invariants.json`, `validation/results/S02/map_checks.json`.
  - Puede modificar: `S02 Mapa Silver` B4, D4, F4 y A7:G11.
  - Debe preservar: encabezados, formato, otras 11 hojas, S01, fórmulas, DV, CF y combinadas.
  - Verificación y evidencia: snapshot de invariantes y de `S01 Inventario`; escritura de identificación (`Grupo 06`, `03B`, fecha real de Build) y de las cinco filas del Anexo A; sustituir el ejemplo de Acería; no añadir WMS; comparación antes/después.
  - Hecho cuando: A7:G11 tiene 5 filas, sin WMS, con claves de S01 y frecuencia exacta; 50 fórmulas y 12 hojas se conservan; S01 no cambió.
  - Estado: **completada el 2026-10-27**. B4=`Grupo 06`, D4=`03B`, F4=`2026-10-27` como texto ISO/General, igual que S01. A7:G11 contiene DATA-001 a DATA-005, sin WMS, con la frecuencia literal de Inventario; se sustituyó la fila de ejemplo y se normalizó A7:G7 al estilo de A8:G8. Se conservaron 12 hojas, 50 fórmulas, 11 DV, 1 rango de CF con 4 reglas, 19 combinadas y S01 sin cambios. `openpyxl` normalizó la alineación por omisión de B4/D4/F4, sin cambio material de fuente, relleno, borde o formato. **18/18 invariantes y 14/14 controles del mapa pasan**; ZIP/CRC/XML válidos y reabribles. SRC-201 y PPTX intactos; no se creó PDF ni se usó Excel COM. Evidencia: `xlsx_invariants.json`, `map_checks.json` y `evidence/S02/t06_tracking_update.md`. T07 no se inició.

- [x] **T07 — Completar `Fichas KPI` C7:E11.**
  - Requisitos: RF-S02-06, RF-S02-07; CA-S02-06, CA-S02-07.
  - Depende de: T06.
  - Artefactos: copia XLSX de seguimiento, `validation/results/S02/kpi_checks.json`.
  - Puede modificar: `Fichas KPI` C7:E11.
  - Debe preservar: A7:B11, columnas F–AA, otras hojas, formatos y validaciones.
  - Verificación y evidencia: escribir «Táctico», fórmula del Anexo B y unidad; comparar contra el contrato; no completar metas, umbrales, DAX ni responsables.
  - Hecho cuando: 5/5 filas con C–E completas, A–B sin cambios, sin merma por valor y sin columnas posteriores modificadas.
  - Estado: **completada el 2026-10-27**. C7:C11=`Táctico`; D7:D11 con la fórmula en palabras aprobada y E7:E10=`Porcentaje`, E11=`Días`. Se conservaron A7:B11, F–AA, estilos, 12 hojas, 50 fórmulas, 11 DV, 1 rango de CF con 4 reglas, 19 combinadas, S01 y S02 sin cambios; solo cambiaron 15 valores. **25/25 controles pasan** en `kpi_checks.json` y `xlsx_invariants.json`; XLSX final: 34.584 bytes y SHA-256 `C2F691F4CD5EDD47AD5E900A593740A9CD5EC11A197B5D5703DF9963E0C7D0D4`; ZIP/CRC/XML válidos y reabribles. No se añadieron metas, umbrales, DAX, responsables, referencias globales, merma por valor ni medida de apoyo. SRC-201 y PPTX intactos; no se creó PDF ni se usó Excel COM. Evidencia: `evidence/S02/t07_fichas_kpi.md`. T08 no se inició.

- [x] **T08 — Exportar el PDF con diagrama y mapa.**
  - Requisitos: RF-S02-09; CA-S02-02, CA-S02-03, CA-S02-09.
  - Depende de: T04, T05 y V02A.
  - Artefactos: `work/S02/export.pptx`, `deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf`, `evidence/S02/pdf_treatment.md`, `validation/results/S02/pdf_structure.json`, `validation/results/S02/pdf_text.json`.
  - Puede modificar: los archivos indicados.
  - Debe preservar: PPTX entregable, XLSX, SRC-203 y SRC-201.
  - Verificación y evidencia: leer la guía SRC-102 y registrar por escrito que la diapositiva 1 es un ejemplo excluido del PDF; copiar el PPTX a `work/S02/export.pptx`; eliminar en esa copia solo la diapositiva 1; exportar con PowerPoint COM; contar páginas y extraer texto.
  - Hecho cuando: el PDF tiene 1 página de diagrama + N de mapa; tamaño 16:9; aparecen los 5 archivos y «Por acordar»; no aparece «ACERÍA» ni WMS dentro del mapa; el PDF abre en `pypdfium2`.
  - Estado: **completada el 2026-10-27**. SRC-102 registra que la diapositiva 1 es un ejemplo; se excluyó solo de `work/S02/export.pptx`. La copia quedó con 3 diapositivas y el PPTX editable conserva 4. PDF: 237.204 bytes, SHA-256 `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42`, 3 páginas de 960 x 540 pt. Estructura 8/8 PASS y texto 10/10 PASS; los cinco archivos aparecen una vez en el mapa, sin WMS ni contenido de Acería. PPTX, XLSX, SRC-201, SRC-203, spec, PBIP, referencias, Silver y S01 conservan sus huellas. Evidencia: `evidence/S02/pdf_treatment.md`, `pdf_structure.json` y `pdf_text.json`. T09 no se inició.

- [x] **T09 — Revisión visual de PPTX, XLSX y PDF.**
  - Requisitos: CA-S02-02, CA-S02-03, CA-S02-06, CA-S02-09; RNF-S02-07, RNF-S02-09.
  - Depende de: T04, T05, T07, T08 y V02A; para la parte Excel, V02B.
  - Artefactos: `evidence/S02/review.md`, `evidence/S02/screenshots/`, `work/S02/review.xlsx`.
  - Puede modificar: los archivos de evidencia y la copia temporal.
  - Debe preservar: entregables; Excel se revisa sobre copia temporal.
  - Verificación y evidencia: renderizar diapositivas con PowerPoint COM; páginas del PDF con `pypdfium2`; copia XLSX con Excel COM; capturar pantallas fechadas.
  - Hecho cuando: hay capturas de las diapositivas (diagrama y todas las del mapa), de `S02 Mapa Silver`, de `Fichas KPI` y de todas las páginas del PDF; no hay textos truncados, objetos superpuestos, filas partidas entre páginas ni columnas ilegibles; cada defecto queda registrado. Si Excel COM falla, se detiene solo la parte Excel, se documenta y la revisión visual de ese artefacto queda pendiente; no se declara V09 ejecutada para el libro.
  - Estado: **completada el 2026-10-27**. Ronda 1: PPTX y PDF pasan; `Fichas KPI` C7:E11 pasa; el título KPI se corta al exportar solo `A1:E11` y `S02 Mapa Silver` falla por truncamiento de filas 7–11. Ronda 2: se corrigió solo `S02 Mapa Silver` en el entregable (filas 7–11 a 45 pt; área `A1:G11`; A4 horizontal; ajuste 1×1; márgenes 18 pt; centrado) y se repitió la evidencia Excel. `Fichas KPI` no cambió en el entregable: título/metadatos y tabla se capturaron por separado desde `work/S02/review.xlsx` sin guardar; `A3:AA3` y 19 combinadas intactas. Capturas r2: mapa, encabezado KPI y tabla KPI, todas legibles y sin truncamiento; PPTX y PDF conservan las capturas y hashes de la ronda 1. **19/19 controles XF01–XF19 pasan** en `validation/results/S02/t09_fix_checks.json`; XLSX final 39.510 bytes y SHA-256 `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D`; 12 hojas, 50 fórmulas, 11 DV, 1 rango de CF, 19 combinadas y anchos sin cambios. Evidencia: `evidence/S02/review.md`, sección 11. T10 no se inició.

- [ ] **T10 — Conciliación final.**
  - Requisitos: RF-S02-03, RF-S02-06, RF-S02-07, RF-S02-09, RF-S02-11; RNF-S02-01, RNF-S02-02, RNF-S02-03; CA-S02-03, CA-S02-06, CA-S02-07, CA-S02-09, CA-S02-10.
  - Depende de: T09.
  - Artefactos: `validation/checks/s02_concile.py`, `validation/results/S02/conciliation.json`, `evidence/S02/conciliation.md`.
  - Puede modificar: los archivos indicados.
  - Debe preservar: todos los entregables.
  - Verificación y evidencia: comparar cadenas normalizadas y el reparto de filas por diapositiva/página; no corregir aquí.
  - Hecho cuando: 5/5 fuentes, 5/5 KPI, 5/5 niveles tácticos y 0 diferencias materiales; cada fila del mapa aparece una sola vez y completa en PPTX y PDF.

- [ ] **T11 — Auditoría independiente (ronda 01).**
  - Requisitos: **RF-S02-01 a RF-S02-11 (11), RNF-S02-01 a RNF-S02-09 (9) y CA-S02-01 a CA-S02-10 (10)**.
  - Depende de: T10 y autorización de Audit.
  - Artefactos: `specs/002-s02-architecture/AUDIT.md`.
  - Puede modificar: solo `AUDIT.md`.
  - Debe preservar: spec, entregables, XLSX, PPTX y PDF.
  - Verificación y evidencia: ejecutar controles en solo lectura; registrar matriz, hallazgos con ID y ronda fechada.
  - Hecho cuando: **30/30 elementos** tienen estado y evidencia; cada fallo tiene ID, impacto y corrección necesaria.

- [ ] **T12 — Corrección de hallazgos, si existen.**
  - Requisitos: los hallazgos de T11.
  - Depende de: T11 y autorización de Fix. **No aplica si no hay hallazgos.**
  - Artefactos: artefactos afectados y `evidence/S02/fixes.md`.
  - Puede modificar: solo lo relacionado con cada hallazgo autorizado.
  - Debe preservar: todo lo no relacionado con el hallazgo.
  - Verificación y evidencia: corregir, enlazar cada cambio a su ID y repetir el control afectado.
  - Hecho cuando: cada hallazgo tiene corrección vinculada y prueba repetida; queda «corregido, pendiente de verificación».

- [ ] **T13 — Ronda 02 (nueva Audit) y cierre (Close).**
  - Requisitos: los 30 elementos.
  - Depende de: T11, T12 si aplica, autorización de nueva Audit y aprobación de cierre.
  - Artefactos: `AUDIT.md` (ronda 02) y la propuesta de cierre.
  - Puede modificar: `AUDIT.md` y la propuesta.
  - Debe preservar: artefactos y spec.
  - **T13.1 — Ronda 02, nueva Audit (autorización separada):** reauditar los 30 elementos y las correcciones; no corrige.
  - **T13.2 — Close (aprobación explícita):** proponer y, solo con aprobación, registrar el cierre.
  - Verificación y evidencia: ronda 02 y propuesta de cierre.
  - Hecho cuando se cumplen **todas** estas condiciones:
    - 30/30 elementos auditados.
    - CA-S02-01 a CA-S02-10 demostrados.
    - Ningún hallazgo bloqueante abierto.
    - Las limitaciones permitidas por la spec están documentadas y **no sustituyen requisitos incumplidos**.
    - Existe aprobación explícita del usuario para cerrar S02.
    - S03 no se ha iniciado.

## Matriz de cobertura

| Requisito | Tareas | Artefacto | Comprobación |
| --- | --- | --- | --- |
| RF-S02-01 | T02, T04, T09, T10 | PPTX diap. 2 | V06 |
| RF-S02-02 | T02–T05, T08–T10 | PPTX/PDF | V06, V07, V09 |
| RF-S02-03 | T02, T05, T06, T08–T10 | PPTX/XLSX/PDF | V04, V08, V10 |
| RF-S02-04 | T02, T04, T09 | PPTX | V06, V09 |
| RF-S02-05 | T02, T04, T09 | PPTX | V06, V09 |
| RF-S02-06 | T02, T07, T09, T10 | XLSX | V05, V10 |
| RF-S02-07 | T02, T07, T10 | XLSX | V05, V10 |
| RF-S02-08 | T01, T06, T07 | XLSX | V03 |
| RF-S02-09 | T03–T05, T08 | PDF/PPTX | V07, V09 |
| RF-S02-10 | T09, T11, T13 | Evidencia | V09, V11 |
| RF-S02-11 | T02, T04, T10 | PPTX/evidencia | V11 |
| RNF-S02-01 | T02, T10, T11 | Contenido y evidencia | V10, V12 |
| RNF-S02-02 | T02, T04, T10 | PPTX/PDF | V06, V08, V10 |
| RNF-S02-03 | T01, T02, T10 | Scripts y manifiesto | V01, V10 |
| RNF-S02-04 | T02, T04, T05 | PPTX/XLSX/PDF | V06, V09 |
| RNF-S02-05 | T02, T05, T06, T07 | PPTX/XLSX | V03, V06 |
| RNF-S02-06 | T01, T06, T07, T08 | Manifiesto | V01, V03 |
| RNF-S02-07 | T01, T09, T10, T11 | `tooling.md`, capturas | V02A, V02B, V09, V12 |
| RNF-S02-08 | T02, T10, T11 | Documentos y resultados | V10, V12 |
| RNF-S02-09 | T08, T09, T11, T13 | PDF/evidencia | V07, V09, V11 |
| CA-S02-01 | T04, T09 | PPTX | V06 |
| CA-S02-02 | T04, T05, T08, T09 | PPTX/PDF | V06, V07, V09 |
| CA-S02-03 | T05, T06, T08, T09 | PPTX/XLSX/PDF | V04, V08, V09 |
| CA-S02-04 | T02, T04, T05 | PPTX | V06 |
| CA-S02-05 | T02, T04 | PPTX | V06 |
| CA-S02-06 | T07, T09 | XLSX | V05 |
| CA-S02-07 | T07, T10 | XLSX | V05, V10 |
| CA-S02-08 | T01, T06, T07 | XLSX | V03 |
| CA-S02-09 | T05, T08, T09 | PDF | V07, V08, V09 |
| CA-S02-10 | T02, T04, T10 | Evidencia | V11 |
