# Plan — S02 Decisión, arquitectura y mapa Silver

Spec y versión aprobada: `specs/002-s02-architecture/spec.md`, v0.4, aprobada el 2026-10-27.
Estado del plan: **v0.1 aprobada por el usuario el 2026-10-27**. La aprobación del plan no autoriza iniciar Build ni crear artefactos de Build.

## Entradas y herramientas

| Recurso | Estado comprobado | Uso previsto | Condición o limitación |
| --- | --- | --- | --- |
| Spec S02 v0.4 | Aprobada; su hash se registra en T01 | Fuente normativa única; objeto de huella | No se modifica |
| SRC-201 `GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | Intacto; SHA-256 `0CCC4A53…D2DF30` | Solo lectura; no se regenera | Objeto de huella |
| Copia `M4_Equipo06_Proyecto_Integrador_v2.xlsx` | SHA-256 `E7F09B0A…DB74F1`; 12 hojas; 50 fórmulas | Se actualiza en sitio | Objeto de huella; `openpyxl` reserializa |
| SRC-203 `GIAD-M4-S02_Plantilla_Diagrama_Arquitectura.pptx` | Intacto; SHA-256 `36E4E9AE…F96516`; 2 diapositivas; 32 formas cada una | Solo lectura | Objeto de huella |
| Guía SRC-102 `GIAD-M4-S02_Hito_Proyecto_Integrador.docx` | Disponible | Define el tratamiento de la diapositiva de ejemplo | Se cita antes de exportar |
| `openpyxl` 3.1.5 | Disponible | Editar y verificar el XLSX | Puede perder extensiones no soportadas |
| `python-pptx` 1.0.2 | Disponible | Editar textos y añadir tablas | No renderiza |
| `pypdfium2` | Disponible | Contar páginas, extraer texto y renderizar PNG | Solo verificación |
| PowerPoint COM (Office 16) | Registrado; binario presente; **no calificado** | Abrir, guardar, renderizar y exportar | Se habilita solo con V02A |
| Excel COM (Office 16) | Registrado; binario presente; **no calificado** | Abrir copia temporal, recalcular y exportar evidencia visual | Se habilita solo con V02B |
| Word COM / Edge / Chrome / LibreOffice / Ghostscript / ImageMagick | No se usan | — | Sin contingencia automática |
| Rodrigo Tucuman | Designado (DEC-027) | Sesión de pantalla | Actividad humana; no se declara ejecutada |

## Implementación y trazabilidad

| Requisito | Artefacto | Diseño o transformación | Prueba | Dependencia |
| --- | --- | --- | --- | --- |
| RF-S02-01 / CA-S02-01 | PPTX diap. 2, caja de decisión | Frase única desde DEC-016 y spec §1.2 | Texto exacto y revisión visual | T02, T04 |
| RF-S02-02 / CA-S02-02 | PPTX diap. 2, cinco cajas y tres bloques | Origen no documentado; Silver; PQ existente; modelo propuesto; KPI táctico | Conteo de cajas y textos | T02, T04 |
| RF-S02-03 / CA-S02-03 | PPTX diap. 3+ y hoja `S02 Mapa Silver` | Tabla de 7 columnas; 5 filas; paginación por filas | Conteo, claves, frecuencia exacta, WMS ausente | T02, T05, T06 |
| RF-S02-04 / CA-S02-05 | PPTX bloque «Brecha DCAM» | Ausencia documentada; C4; Evidencia; 1 Incipiente; no resuelta | Texto y ausencia de definición inventada | T02, T04 |
| RF-S02-05 / CA-S02-04 | PPTX bloque riesgo→control y pendiente | Riesgo, hecho observado, control principal y complementario según la spec | Texto exacto, ausencia de hallazgo inventado y revisión visual | T02, T04 |
| RF-S02-06 / CA-S02-06 | Hoja `Fichas KPI` C7:E11 | Táctico; fórmula en palabras; unidad | Conteo 5 y C–E completas | T02, T07 |
| RF-S02-07 / CA-S02-07 | Fichas KPI y Anexo B | Coincidencia con S01/DEC-017; sin merma por valor | Comparación celda a celda | T02, T07 |
| RF-S02-08 / CA-S02-08 | Copia XLSX | Actualización en sitio | 50 fórmulas, DV, CF, combinadas y S01 intactos | T01, T06, T07 |
| RF-S02-09 / CA-S02-09 | PDF y PPTX en `deliverables/S02/` | Diagrama 1 página + mapa N páginas | Conteo y contenido del PDF | T04, T05, T08 |
| RF-S02-10 / CA-S02-10 | `evidence/S02/` | Registro de ejecutado, revisado y pendiente | Revisión documental | T09–T13 |
| RF-S02-11 / CA-S02-10 | PPTX bloque pendiente y `evidence/S02/pendientes.md` | Responsable e hito; «por acordar» sin respaldo | Tabla de pendientes | T02, T04 |
| RNF-S02-01 Trazabilidad | `content.json`, PPTX, XLSX, PDF | Toda afirmación cita fuente, cálculo o decisión; sin páginas, cifras, orígenes ni propietarios inventados | V10 y matriz de T11 | T02, T10, T11 |
| RNF-S02-02 Separación de estados | Diap. 2, `content.json`, PDF | Distinguir dato, cálculo, supuesto, referencia, propuesta y recomendación | V06, V08, V10 | T02, T04, T10 |
| RNF-S02-03 Reproducibilidad | `content.json`, scripts, evidencia | Rutas relativas; `RutaSilver` sin cambios; conteos repetibles | V01, V10 | T01, T02, T10 |
| RNF-S02-04 Claridad | PPTX, XLSX, PDF | Español en explicaciones; nombres propios en inglés; `dias_en_almacen` sin tilde | V06, V09 | T02, T04, T05 |
| RNF-S02-05 Formato | PPTX, XLSX, evidencia | Markdown como fuente de verdad; plantilla completada solo en Build; sin duplicar informes | V03, V06 | T02, T05, T06, T07 |
| RNF-S02-06 Integridad | Hashes y manifiesto | Silver, referencias y plantillas originales sin modificar | V01, V03 | T01, T06, T07, T08 |
| RNF-S02-07 Evidencia | `evidence/S02/` | Distinguir control automático, revisión documental y prueba ejecutada | V02A, V02B, V09, V11 | T01, T09, T10, T11 |
| RNF-S02-08 Seguridad | Documentos y resultados | Sin credenciales, secretos ni datos personales innecesarios | V10 y matriz de T11 | T02, T10, T11 |
| RNF-S02-09 Honestidad de alcance | PPTX, PDF, evidencia | No declarar sesión, publicación, actualización, DAX ni RLS no ejecutados | V07, V09, V11 | T08, T09, T11, T13 |

## Decisiones técnicas

1. **Composición nativa en PowerPoint.** La copia editable de SRC-203 conserva las dos diapositivas originales: la 1 es el ejemplo de Acería y **no se modifica**; la 2 contiene el diagrama de arquitectura del subcaso; las diapositivas 3 y siguientes contienen el mapa Silver como **tabla editable**.
2. **Mapa con siete columnas y cinco fuentes.** Cada página del mapa repite los encabezados `Archivo / tabla`, `Granularidad`, `Identificador único`, `Frecuencia`, `Propietario`, `Riesgo`, `Control propuesto`. Solo se incluyen DATA-001 a DATA-005.
3. **Paginación por filas, nunca por columnas.** Si el mapa no cabe en una diapositiva, se reparte por filas completas y se repite el encabezado. Una fila nunca se parte entre diapositivas; las siete columnas permanecen juntas.
4. **Tratamiento de la diapositiva 1.** Antes de exportar se lee la guía SRC-102 y se registra por escrito que la primera diapositiva es un ejemplo y queda excluida del PDF. La comprobación se hace sobre el PDF resultante: no debe contener el rótulo «ACERÍA».
5. **PDF generado con PowerPoint COM.** Se copia el PPTX entregable a `work/S02/export.pptx`, se elimina en esa copia la diapositiva 1 y se exporta el resto. El PDF contiene el diagrama seguido del mapa completo, en el tamaño de diapositiva 16:9 (13,333 × 7,5 pulgadas), no en A4.
6. **El PPTX entregable reproduce el PDF.** Las diapositivas 3+ del PPTX editable son la fuente del mapa en el PDF; el PDF solo se obtiene quitando el ejemplo en una copia de trabajo. No hay contenido del mapa que exista únicamente en el PDF.
7. **Calificación previa de COM, por separado.** PowerPoint COM se califica abriendo, guardando, renderizando y exportando una copia temporal. Excel COM se califica abriendo una copia temporal del XLSX, recalculándola y generando la evidencia visual, sin reparación ni modificación del entregable. Los resultados se registran por separado en `evidence/S02/tooling.md`. Un fallo de Excel COM detiene solo la parte dependiente; no se declara la revisión visual ejecutada ni se cambia de herramienta automáticamente.
8. **Sin contingencia automática.** Si PowerPoint COM falla en cualquier tarea, se detiene esa tarea, se documenta el error y se informa. No se cambia a HTML + Edge, Word COM ni otra vía sin autorización.
9. **Excel se actualiza, no se regenera.** Se conservan 12 hojas, 50 fórmulas, 4 validaciones, 1 formato condicional, celdas combinadas y el contenido de `S01 Inventario`.
10. **Sin cambios en Power BI, consultas, relaciones, medidas, roles, visuales, Silver ni referencias.**
11. **Fases y autorizaciones separadas.** T01–T10 pertenecen a **Build** y requieren autorización de Build. T11 pertenece a **Audit** y requiere autorización separada; no modifica artefactos auditados. T12 pertenece a **Fix**, solo se ejecuta si hay hallazgos y tras autorización expresa. La ronda 02 de T13 pertenece a una **nueva Audit** con autorización separada. El registro del cierre pertenece a **Close** y requiere aprobación explícita. Aprobar este plan y sus tareas no autoriza ejecutar T01–T13.
12. **Riesgo DCAM según la spec.** El riesgo es «Interpretar incorrectamente qué representa el centro y usarlo en filtros o conclusiones». El hecho observado es que los cruces revisados no encontraron discrepancias entre centro WMS y centro base en los 8.000 viajes emparejados, sin que esa consistencia demuestre significado empresarial. El control principal es documentar la ausencia de definición, los usos y límites conocidos, y solicitar definición y validación empresarial. El control complementario es no usar `centro_distribucion_base` como ruta u origen real; `dim_centro` y los controles de claves son propuestas posteriores. No se presenta una asignación incorrecta como hallazgo observado ni se declara resuelta la brecha.
13. **WMS fuera del mapa, nota de contraste permitida.** WMS debe estar ausente de las cinco filas del mapa. Puede aparecer únicamente en una nota separada como fuente de contraste no cargada; no se exige su ausencia de toda la documentación.
14. **Cierre sin sustitución de requisitos.** Una limitación permitida por la spec se documenta, pero no reemplaza un requisito incumplido. El cierre exige 30/30 elementos auditados, los 10 CA demostrados y ningún hallazgo bloqueante abierto.

## Estrategia de validación

| Prueba | Requisitos | Tipo | Contexto y esperado | Evidencia |
| --- | --- | --- | --- | --- |
| V01 Integridad de originales | RNF-S02-03, RNF-S02-06 | Automático | SRC-201, SRC-203, copia XLSX, spec S02 y PBIP con su hash inicial; relectura sin cambios | `validation/results/S02/initial_manifest.json` |
| V02A Calificación de PowerPoint COM | RNF-S02-07 | Automático | Abre, guarda, renderiza y exporta una copia temporal sin reparación; PDF y PNG con contenido | `evidence/S02/tooling.md`, sección PowerPoint |
| V02B Calificación de Excel COM | RNF-S02-07 | Automático | Abre una copia temporal, recalcula y exporta evidencia visual; sin reparación; el entregable conserva su hash | `evidence/S02/tooling.md`, sección Excel |
| V03 Invariantes del XLSX | RF-S02-08, CA-S02-08 | Automático | 12 hojas, 50 fórmulas, 4 DV, 1 CF, combinadas y S01 idéntico | `validation/results/S02/xlsx_invariants.json` |
| V04 Mapa Silver en Excel | RF-S02-03, CA-S02-03 | Automático | Exactamente 5 filas; DATA-001 a DATA-005; WMS ausente; frecuencia exacta | `validation/results/S02/map_checks.json` |
| V05 Fichas KPI | RF-S02-06/07, CA-S02-06/07 | Automático | 5 KPI; C–E completas; nombres y decisiones sin cambios | `validation/results/S02/kpi_checks.json` |
| V06 PPTX | RF-S02-01/02/04/05/11, CA-S02-01/02/04/05 | Automático | Textos esperados; diap. 1 intacta; tabla con 7 columnas y 5 filas | `validation/results/S02/pptx_checks.json` |
| V07 PDF estructura | RF-S02-09, CA-S02-09 | Automático | 1 página de diagrama + N de mapa; tamaño 16:9; sin «ACERÍA» | `validation/results/S02/pdf_structure.json` |
| V08 PDF contenido | CA-S02-03/09 | Automático | 5 archivos, 5 KPI, «No documentado», «Por acordar»; sin WMS en el mapa | `validation/results/S02/pdf_text.json` |
| V09 Revisión visual | CA-S02-02/03/06/09 | Visual ejecutada | Sin truncados, solapamientos, filas partidas ni columnas ilegibles; PPTX/PDF y Excel calificados por separado | `evidence/S02/screenshots/` y `review.md` |
| V10 Conciliación | RF-S02-07/09, CA-S02-07/09 | Automático | Spec ↔ content ↔ XLSX ↔ PPTX ↔ PDF; cada fila completa una sola vez | `validation/results/S02/conciliation.json` |
| V11 Pendientes, sesión y cierre | RF-S02-10/11 | Documental y manual | Pendientes con hito; sesión no declarada; cierre solo aprobado | `evidence/S02/pendientes.md`, `session.md`, `AUDIT.md` |
| V12 Cobertura de auditoría | Todos | Documental | 11 RF + 9 RNF + 10 CA = 30 elementos con estado y evidencia | `AUDIT.md` |
| V13 Autorizaciones por fase | RNF-S02-07/09 | Documental | Build, Audit, Fix, nueva Audit y Close con autorización registrada e independiente | `evidence/S02/authorizations.md` |

### Criterios que requieren intervención manual o herramienta no calificada

| Elemento | Tipo | Tratamiento |
| --- | --- | --- |
| PowerPoint COM | Herramienta no calificada | V02A en T01; sin ella no se ejecutan T04, T05, T08 ni la parte PPTX/PDF de T09 |
| Excel COM | Herramienta no calificada | V02B en T01; sin ella no se ejecuta la parte Excel de T09 y la revisión visual de ese artefacto queda pendiente, sin declararla ejecutada |
| Autorización de Build | Gate humano | Necesaria para T01–T10 |
| Autorización de Audit | Gate humano | Necesaria para T11 |
| Autorización de Fix | Gate humano | Necesaria para T12, solo si hay hallazgos |
| Autorización de nueva Audit | Gate humano | Necesaria para T13.1 (ronda 02) |
| Aprobación de cierre | Gate humano | Necesaria para T13.2 (Close) |
| Sesión compartida de S02 | Manual (Rodrigo Tucuman) | Se registra solo si ocurre; si no, queda pendiente |
| Carga en Classroom | Manual del usuario | Fuera del repositorio; no se declara ejecutada |

## Documentación y riesgos

| Riesgo | Impacto | Mitigación |
| --- | --- | --- |
| PowerPoint pide reparar el archivo o falla al exportar | Bloqueo de toda la vía PDF | V02A previa; si falla, se detiene la tarea y se documenta |
| Excel COM falla o abre con reparación | Sin evidencia visual del libro | V02B previa; se detiene solo esa parte y se documenta; no se declara ejecutada |
| `openpyxl` altera formato o extensiones | Pérdida de fórmulas o validaciones | Snapshot e invariantes; restaurar copia si falla |
| Desbordamiento en la diapositiva 2 | Diagrama ilegible | Ajuste de fuente y render real |
| Tabla del mapa no cabe en una página | Filas partidas o ilegibles | Paginación por filas con encabezado repetido; altura de fila antes que reducir fuente |
| Diferencia Excel–PPTX–PDF | Incumplimiento de CA-S02-03/09 | Contenido único en `content.json` y conciliación T10 |
| Diapositiva de ejemplo incluida por error | Entrega fuera de la guía | Copia de exportación sin diapositiva 1 y comprobación de texto |
| Fechas o cifras inventadas | Pérdida de trazabilidad | Solo valores de la spec; fecha real de Build o «por acordar» |
| Se ejecuta una fase sin su autorización | Cambios fuera de alcance | Gates explícitos para Build, Audit, Fix, nueva Audit y Close |
| Una limitación se usa para tapar un requisito | Cierre improcedente | T13 exige 30/30, 10/10 CA y cero hallazgos bloqueantes; la limitación no sustituye |
| Se declara la brecha DCAM resuelta por la consistencia WMS–base | Conclusión falsa | Texto aprobado: la consistencia no demuestra significado empresarial |
| Declarar sesión o revisión no ejecutada | Evidencia falsa | Registro explícito de lo ejecutado y lo pendiente |

## Orden y límites

Secuencia y gates:

- **Build (autorización de Build):** T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09 → T10.
- **Audit (autorización separada):** T11.
- **Fix (autorización expresa, solo si hay hallazgos):** T12.
- **Nueva Audit (autorización separada):** T13.1, ronda 02.
- **Close (aprobación explícita):** T13.2, propuesta y registro del cierre.

Reglas:

- T04, T05 y T08 no comienzan sin V02A aprobada.
- La parte Excel de T09 no comienza sin V02B aprobada; su ausencia deja esa revisión pendiente y no ejecutada.
- T06 y T07 modifican el mismo XLSX en orden, con guardado y verificación por tarea.
- T11 no modifica artefactos; solo crea `AUDIT.md`.
- T12 no cierra hallazgos; deja «corregido, pendiente de verificación».
- T13.1 no corrige; audita. T13.2 no cierra sin aprobación explícita.
- Aprobar este plan no autoriza ninguna fase.
- Cualquier fallo de COM detiene la tarea dependiente; no se cambia de herramienta sin autorización.
- S03 no se inicia como parte de S02.
