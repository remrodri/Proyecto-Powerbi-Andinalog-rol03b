# Auditoría — S02 - Decisión, arquitectura y mapa Silver

## Estado actual

Ronda vigente: 02. Fecha: 2026-10-27. Versión auditada: spec v0.4, SHA-256 `6C1BDBF37D96D5FC3157C769F7AD9DDAB19A9FBE93F86A157551566AAB0C2DB6`; XLSX corregido `415A3C55F616E466E4072E3AE4E44E4E3C308FC62DDAB642B28740F367E9EF31`; PPTX `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D`; PDF `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42`.

Veredicto: **CONFORME AL ALCANCE; APTO PARA PROPUESTA DE CIERRE**.

**Cierre aprobado:** el usuario aprobó explícitamente el cierre de S02 el 2026-10-27 después de recibir el resultado de la ronda 02. S02 queda cerrado; esta aprobación no inicia S03 ni resuelve los pendientes trasladados a hitos posteriores.

**Consolidación posterior (2026-10-27):** a solicitud del usuario se retiraron temporales y registros duplicados de Build. Sus resultados se condensaron en `evidence/S02/evidence.md` y `validation/results/S02/validation.json`; se conservó `evidence/S02/screenshots/s02_t09_xlsx_map_r2.png` porque prueba el hallazgo abierto. Las menciones inferiores a archivos auxiliares retirados describen la evidencia disponible durante la ronda 01 y no constituyen entregables vigentes. La consolidación no cambia el veredicto ni cierra hallazgos.

Alcance y exclusiones: se auditaron los 30 elementos de T11 —RF-S02-01 a RF-S02-11, RNF-S02-01 a RNF-S02-09 y CA-S02-01 a CA-S02-10— mediante controles de solo lectura sobre entregables, evidencias, resultados y modelo del repositorio. No se abrió Power BI Desktop, no se usaron COM/Excel/PowerPoint, no se ejecutaron DAX, RLS, publicación ni sesión compartida, y no se rehasharon los diez Silver externos de `C:\GIAD` por la restricción de acceso de esta ronda. No se modificaron spec, plan, tareas, entregables, referencias, Silver, PBIP, `MEMORY.md` ni decisiones. El único archivo creado es este `AUDIT.md`.

Método independiente: lectura directa de spec, decisiones, tareas y evidencias; recálculo de conteos XLSX con `openpyxl`; comparación de valores del XLSX actual contra `work/S02/t09_fix_backup.xlsx`; lectura de tablas PPTX con `python-pptx`; extracción de texto y páginas PDF con `pypdfium2`; lectura del TMDL; comparación de las 52 referencias contra las entradas de T08; inspección visual de las capturas de T09. Los controles T01–T10 se usaron como rastro documental, no como sustituto de la comprobación independiente.

## Matriz vigente de aceptación

| Requisito/criterio | Prueba y contexto | Resultado | Evidencia | Hallazgo |
| --- | --- | --- | --- | --- |
| RF-S02-01 | Cotejo de la frase de decisión en spec §1.2, PPTX diapositiva 2, PDF página 1 y `content.json`: Jefatura de Operaciones, revisión semanal, controles térmicos y revisión de lotes/centros, sin causalidad. | PASA | `spec.md` §1.2; PPTX shape 3; PDF p.1; `work/S02/content.json` `decision`; T04/T09 | Ninguno |
| RF-S02-02 | Verificación de las cinco cajas en la diapositiva 2 y PDF: origen, Silver, Power Query, modelo e indicador; origen no documentado; sin WMS en el modelo. | PASA | PPTX diapositiva 2; PDF p.1; TMDL `model.tmdl`; `content.json` `slide_blocks` | Ninguno |
| RF-S02-03 | Lectura de `S02 Mapa Silver!A7:G11`: exactamente cinco filas DATA-001 a DATA-005 y siete campos; grano, claves, frecuencias y propietarios coinciden con spec §3.2/Anexo A; D10 contiene la frecuencia completa y es visible; WMS no ocupa fila. | PASA | XLSX actual; `spec.md` §3.2 y Anexo A; captura corregida | Ninguno |
| RF-S02-04 | Verificación de la brecha como «ausencia documentada», con usos, límites, solicitud de definición y seguimiento; `dim_centro` y controles de claves solo como propuestas; no se declara resuelta. | PASA | `spec.md` §8, §8.3 y Anexo C; PPTX diapositiva 2; `content.json` `dcam`; `docs/decisions.md` DEC-031 | Ninguno |
| RF-S02-05 | Cotejo del riesgo principal y control propuesto en PPTX, mapa y spec; el control no se presenta como aplicado y el pendiente tiene responsable. | PASA | PPTX diapositiva 2; `S02 Mapa Silver!F7:G11`; `spec.md` §7; `evidence/S02/t04_architecture.md` | Ninguno |
| RF-S02-06 | Verificación de exactamente cinco KPI, todos tácticos, con fórmula en palabras y unidad; nombres y orden conservados; no se añaden metas, umbrales ni DAX. | PASA | `Fichas KPI!C7:E11`; `spec.md` Anexo B; S01 `spec.md` Anexo B; `content.json` `kpis` | Ninguno |
| RF-S02-07 | Comparación de nombres, fórmulas, denominadores y límites con el anexo B de S01 y DEC-017; `merma por valor` no es KPI; las referencias se presentan como líneas base. | PASA | S01 `spec.md` Anexo B; `Fichas KPI!A7:E11`; `content.json` `kpis`; `docs/decisions.md` DEC-017 | Ninguno |
| RF-S02-08 | Recuento independiente y comparación: 12 hojas, 50 fórmulas, 11 validaciones, 1 rango de formato condicional con 4 reglas, 19 combinadas; filas 7–11 de `Fichas KPI` completas; SRC-201 intacto. | PASA | `xlsx_invariants.json`; `t09_fix_checks.json`; `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx`; hash SRC-201 | Ninguno |
| RF-S02-09 | Verificación de PDF de 3 páginas, diagrama en p.1 y mapa en p.2–3, tamaño 960×540 pt, y PPTX editable en `deliverables/S02/`. | PASA | `pdf_structure.json`; `pdf_text.json`; PPTX y PDF entregables | Ninguno |
| RF-S02-10 | Revisión de `session.md`, `authorizations.md`, `review.md` y `conciliation.md`: se distingue archivo generado, revisión visual y prueba no ejecutada; la sesión figura como no ejecutada, sin fecha ni persona que la hubiera compartido. | PASA | `evidence/S02/session.md`; `authorizations.md`; `review.md`; `conciliation.md` | Ninguno |
| RF-S02-11 | Recuento de los 13 pendientes y cotejo de estado, responsable e hito en spec §8.3 y `pendientes.md`; se conserva «Por acordar» donde no hay respaldo. | PASA | `spec.md` §8.3; `evidence/S02/pendientes.md`; `content.json` `pending` | Ninguno |
| RNF-S02-01 | Rastreo de afirmaciones y cifras a spec, decisiones, S01 o fuentes; no se encontraron páginas, orígenes ni propietarios inventados; el origen permanece no documentado y los propietarios por acordar. | PASA | `spec.md` Anexo C; `docs/decisions.md`; `content.json`; mapa y PPTX | Ninguno |
| RNF-S02-02 | Separación explícita entre dato observado, referencia, propuesta, ausencia documentada y pendiente; los controles y `dim_centro` se identifican como propuestas. | PASA | `spec.md` §7–§8; PPTX diapositiva 2; `content.json` `dcam`, `pending` | Ninguno |
| RNF-S02-03 | Repetición de conteos XLSX/PPTX/PDF y rutas relativas en documentación; `RutaSilver` aparece una sola vez y las cinco tablas la consumen. El agregado de referencias tiene dos valores por métodos distintos (T08 `708F…`, T10 `62BC…`), aunque las 52 entradas individuales coinciden. | PASA | TMDL `expressions.tmdl`; `model.tmdl`; `map_checks.json`; `t08_precheck.json`; `conciliation.json` | Ninguno; limitación de método de agregado |
| RNF-S02-04 | Revisión de idioma y términos: español en explicaciones, nombres propios en inglés y `dias_en_almacen` conservado sin tilde; nombres de archivo y columnas intactos. | PASA | `Fichas KPI`; `S02 Mapa Silver`; `content.json`; `spec.md` §Anexo B | Ninguno |
| RNF-S02-05 | Verificación de Markdown como fuente de verdad y de que la plantilla se completó sin regenerarla; no se duplican informes completos. | PASA | `spec.md`; `work/S02/content.md`; `evidence/S02/`; `xlsx_invariants.json` | Ninguno |
| RNF-S02-06 | Rehash independiente de DATA-001 a DATA-005 desde sus cinco rutas exactas: tamaños y SHA-256 coinciden con `source_manifest.json`. SRC-201, SRC-203, PPTX, PDF y PBIP conservan las huellas registradas. | PASA (ronda 02) | Cinco Silver externos; `validation/results/S01/source_manifest.json`; hashes de ronda 02 | Ninguno |
| RNF-S02-07 | Inspección independiente del XLSX y de la nueva captura: D10 conserva sus 107 caracteres, `WrapText`, ancho D y estilos; la fila 10 mide 150 pt y el texto completo es visible con las siete columnas legibles. | PASA (ronda 02) | `evidence/S02/screenshots/s02_t12_xlsx_map_fixed.png`; XLSX `S02 Mapa Silver!D10` | A-S02-001 cerrado |
| RNF-S02-08 | Búsqueda de credenciales, secretos, tokens y datos personales innecesarios en spec, evidencias y contrato: solo aparece la mención de política y el nombre designado Rodrigo Tucuman; no hay secretos ni credenciales. | PASA | `spec.md`; `evidence/S02/`; `work/S02/content.json`; búsqueda de patrones | Ninguno |
| RNF-S02-09 | Verificación de que no se declara sesión, publicación, actualización, DAX ni RLS ejecutados; `session.md` y `content.json` lo mantienen como pendiente y el TMDL no contiene medidas, roles ni relaciones. | PASA | `session.md`; `content.json` `claims`; `model.tmdl`; TMDL de tablas | Ninguno |
| CA-S02-01 | Cotejo de la decisión con DEC-016 y con los cinco soportes; una sola frase con quién, qué y cada cuánto. | PASA | `spec.md` §1.2; DEC-016; PPTX diapositiva 2; PDF p.1 | Ninguno |
| CA-S02-02 | Cotejo visual y estructural de las cinco cajas de la cadena, la brecha DCAM y el origen no inventado en PPTX y PDF. | PASA | PPTX diapositiva 2; PDF p.1; `slide2_checks.json`; `pdf_text.json` | Ninguno |
| CA-S02-03 | Verificación de cinco filas DATA-001 a DATA-005, siete campos y WMS fuera del mapa y del modelo; D10 conserva la frecuencia completa y su presentación corregida es legible. | PASA (ronda 02) | `S02 Mapa Silver!A7:G11`; TMDL `model.tmdl`; `s02_t12_xlsx_map_fixed.png` | Ninguno |
| CA-S02-04 | Cotejo del riesgo y control propuestos con la brecha, y del pendiente con responsable; el control no se declara aplicado. | PASA | `spec.md` §7; PPTX diapositiva 2; `S02 Mapa Silver!F7:G11`; `pendientes.md` | Ninguno |
| CA-S02-05 | Verificación de la brecha en estado «ausencia documentada», con estado de validación y seguimiento; no se inventa definición ni se declara resuelta. | PASA | `spec.md` §8; DEC-031; PPTX diapositiva 2; `content.json` `dcam` | Ninguno |
| CA-S02-06 | Verificación de cinco KPI tácticos, fórmula y unidad, sin metas, umbrales ni DAX en el contenido S02. La diapositiva 1 del PPTX editable conserva el ejemplo de Acería, marcado «NO SE ENTREGA», y el PDF lo excluye. | PASA | `Fichas KPI!C7:E11`; `spec.md` Anexo B; PPTX diapositivas 1–2; PDF p.1; `content.json` `claims` | Ninguno |
| CA-S02-07 | Cotejo con S01/DEC-017: nombres, fórmulas, denominadores y límites coinciden; `merma por valor` no figura como KPI; referencias como líneas base. | PASA | S01 `spec.md` Anexo B; `Fichas KPI`; `content.json`; DEC-017 | Ninguno |
| CA-S02-08 | Comparación de valores actuales contra `t09_fix_backup.xlsx`: 0 diferencias; 50 fórmulas, 11 validaciones, 1 rango CF/4 reglas, 19 combinadas y 12 hojas conservadas; SRC-201 sin cambios. | PASA | XLSX entregable; `work/S02/t09_fix_backup.xlsx`; `xlsx_invariants.json`; hash SRC-201 | Ninguno |
| CA-S02-09 | Verificación del PDF de 3 páginas, diagrama y mapa en páginas separadas, y existencia del PPTX editable. | PASA | PDF; PPTX; `pdf_structure.json`; `pdf_text.json` | Ninguno |
| CA-S02-10 | Recuento y cotejo de los 13 pendientes, con estado documentado/trasladado, responsable e hito; «Por acordar» se conserva donde falta respaldo. | PASA | `spec.md` §8.3; `pendientes.md`; `content.json` `pending` | Ninguno |

**Resumen vigente de la matriz:** 30 PASA, 0 FALLA y 0 PENDIENTE DE VERIFICACIÓN.

## Registro acumulado de hallazgos

| ID estable | Requisito | Evidencia e impacto | Corrección necesaria | Estado | Verificación de cierre |
| --- | --- | --- | --- | --- | --- |
| A-S02-001 | RNF-S02-07; criterio visual «no hay textos truncados» | **Severidad media.** La ronda 01 demostró truncamiento visual de D10 sin pérdida del valor. | Aumentar solo la altura de la fila 10, conservar valor/ancho/estilo y generar evidencia fiel. | **Cerrado** | Ronda 02: altura 150 pt, D10 completo y siete columnas legibles; integridad estructural conforme |

## Observaciones y limitaciones

- La ronda 01 no pudo repetir las huellas Silver. La ronda 02 rehasheó las cinco fuentes oficiales desde sus rutas exactas y resolvió RNF-S02-06. Las otras tablas del directorio no forman parte del mapa S02 y no se incluyeron.
- El agregado de `references/` no es único entre T08 y T10: T08 usa un JSON de entradas con rutas Windows y obtiene `708F12A…`; T10 usa líneas `ruta|sha256` con barras normales y obtiene `62BCF5F…`. Las 52 entradas individuales coinciden y no hay archivos faltantes o nuevos. Se registra como limitación de reproducibilidad del agregado, sin diferencia material de contenido.
- La introducción de `review.md` conserva la conclusión de la ronda 1 de que T09 no estaba completada; §11 la identifica expresamente como historial y registra la ronda 2. No se considera contradicción de estado, pero conviene que la corrección haga explícito el estado final junto con A-S02-001.
- La diapositiva 1 del PPTX editable conserva el ejemplo de Acería, incluida su meta de 85 %, marcado «NO SE ENTREGA». El PDF excluye esa diapositiva y el contenido S02 no la usa; no se considera una meta de S02. Se deja como limitación de la plantilla, no como hallazgo.
- La comprobación visual se hizo sobre capturas existentes; T11 no reabrió Excel, PowerPoint ni PDF con COM. La captura r2 es suficiente para demostrar el truncamiento de D10, pero no sustituye una nueva revisión visual posterior a la corrección.
- No se identificaron defectos visuales en `Fichas KPI` r2 (tabla completa), en las diapositivas 3–4 del PPTX ni en las páginas 2–3 del PDF; el texto PDF y las tablas PPTX conservan la frecuencia completa de inventario.

## Historial de rondas

### Ronda 02 — 2026-10-27

- Alcance: verificación independiente del Fix A-S02-001 y de RNF-S02-06, sin modificar entregables, spec, plan, tareas, evidencia, validación, PBIP, referencias o Silver.
- A-S02-001: D10 conserva 107 caracteres, `WrapText=true`, ancho D=13 y altura de fila 10=150 pt. El texto completo es visible y las siete columnas siguen legibles. El libro conserva 12 hojas, 50 fórmulas, 11 validaciones, 1 rango de formato condicional con 4 reglas y 19 combinaciones; ZIP/CRC válido. Hallazgo cerrado.
- RNF-S02-06: DATA-001 a DATA-005 se rehashearon desde sus rutas exactas. Tamaños y SHA-256 coinciden con `validation/results/S01/source_manifest.json`: `A193F92A…3BBE`, `E27824EB…F28F`, `A30FF0BC…8307`, `13EFBE4E…A406` y `D3D238E6…2AC0`.
- Integridad: PPTX `26324855…325D`, PDF `07516A56…1A42`, SRC-201 `0CCC4A53…DF30`, SRC-203 `36E4E9AE…6516` y PBIP `F8712089…1CCE` permanecen intactos.
- Resultado: 30/30 requisitos y criterios pasan; 0 hallazgos abiertos y 0 verificaciones pendientes. Veredicto **CONFORME AL ALCANCE; APTO PARA PROPUESTA DE CIERRE**.
- Límite: esta ronda no cierra S02 ni inicia S03. El cierre requiere aprobación explícita del usuario.

### Ronda 01 — 2026-10-27

- Alcance, versión y pruebas ejecutadas: se auditaron los 30 elementos de T11 sobre spec v0.4 y los entregables con los hashes indicados. Se ejecutaron comprobaciones de solo lectura: hashes y estructura, 52 referencias contra T08, valores XLSX contra el respaldo T09, tablas PPTX, texto y dimensiones PDF, TMDL y revisión de capturas. No se usó COM ni se accedió a los Silver externos.
- Resultados y limitaciones: 28 PASA, 1 FALLA y 1 PENDIENTE DE VERIFICACIÓN. La revisión visual propia de `s02_t09_xlsx_map_r2.png` contradice la declaración de T09: D10 está truncada aunque el valor completo permanece en la celda. La única pendiente es el rehash de los Silver externos, no una diferencia material observada. El agregado de referencias tiene dos métodos y dos valores, con 52/52 archivos iguales.
- Hallazgos nuevos/cerrados/reabiertos: se registra A-S02-001 como hallazgo nuevo, abierto. No se cierra ningún hallazgo previo porque no existía una ronda anterior de S02. No se reabre T09 como tarea en este archivo; se deja constancia de que su condición de finalización no se cumple mientras A-S02-001 siga abierto.
- Veredicto y siguiente acción: **REQUIERE CORRECCIONES**. T12 no se inicia; requiere autorización de Fix. Después de corregir y repetir la evidencia, se necesitará una nueva ronda de auditoría. S02 no se declara cerrada y S03 no se inicia.
