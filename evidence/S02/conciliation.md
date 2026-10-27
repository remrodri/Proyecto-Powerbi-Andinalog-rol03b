# Conciliación final de S02 — T10

- Fecha UTC: 2026-10-27.
- Fase: Build, T10.
- Alcance: comprobar la correspondencia entre spec, contrato, Excel, PPTX y PDF; no corregir artefactos.
- Script: `validation/checks/s02_concile.py`.
- Resultado estructurado: `validation/results/S02/conciliation.json`.
- Resultado: **39/39 controles PASS; 0 FAIL; `all_pass: true`**.

## 1. Método y límites

Se ejecutaron controles de solo lectura sobre los entregables y las fuentes registradas. No se abrió PowerPoint ni Excel mediante COM, no se generaron capturas y no se modificó ningún artefacto auditado. La única escritura fue el JSON de resultados.

La comparación usó texto normalizado: NFKC; colapso de espacios y saltos de línea; `casefold` solo para comparar; normalización de comillas tipográficas y guiones; retiro de backticks y énfasis Markdown; conversión de `→` a `->`. No se usó coincidencia difusa.

Equivalencias registradas:

- spec `decide, con revisión semanal` ~ entregables `decide cada semana`; compactación admitida en T04 sin cambio de significado.
- spec `Cinco CSV oficiales` ~ diapositiva/PDF `5 fuentes oficiales`; mismo conjunto DATA-001 a DATA-005.
- spec `Interpretar incorrectamente` ~ diapositiva/PDF `interpretar mal`; abreviatura sin cambio semántico.
- Excel `dividido entre`/`multiplicado por` ~ spec/contrato `/`/`×`; equivalencia aritmética.
- `Hecho observado`/`Control principal`/`Control complementario` ~ `Hecho`/`Control`/`Complemento`; compactación de etiquetas.
- saltos de línea del PDF y del PPTX colapsados; no se altera el contenido.

## 2. Huellas antes y después

| Artefacto | Bytes | SHA-256 antes | SHA-256 después | Resultado |
| --- | ---: | --- | --- | --- |
| `specs/002-s02-architecture/spec.md` | 28.474 | `A91958C34BADCF6E5AAF3D0F063AC94C3FE458436A9C30AF6AE1362FD626598A` | `A91958C34BADCF6E5AAF3D0F063AC94C3FE458436A9C30AF6AE1362FD626598A` | Igual |
| `work/S02/content.json` | 13.094 | `A7C3A75D43841B72E542F7A05F7B6FC882F7DA8316EF8689B8A92205BF1C7882` | `A7C3A75D43841B72E542F7A05F7B6FC882F7DA8316EF8689B8A92205BF1C7882` | Igual |
| `work/S02/content.md` | 9.375 | `00109A5D0F03A7C3E6892D3C2FCBDA978845A24F05FFD4875A122EE360C427BC` | `00109A5D0F03A7C3E6892D3C2FCBDA978845A24F05FFD4875A122EE360C427BC` | Igual |
| XLSX de seguimiento | 39.510 | `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D` | `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D` | Igual |
| PPTX S02 | 43.872 | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | Igual |
| PDF S02 | 237.204 | `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42` | `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42` | Igual |
| `powerbi/AndinaLog_03B.pbip` | 292 | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` | Igual |

El árbol `references/` conserva 52 archivos. El agregado SHA-256 del manifiesto ordenado es `62BCF5FDDA329847257E96761FEB818DA1CE41CCF106F5A3AC077727DE8B90C8` antes y después.

La integridad de las fuentes registró 13 comprobaciones: diez entradas de `validation/results/S01/source_manifest.json` más SRC-201, SRC-203 y PBIP del manifiesto inicial. Todas conservan tamaño y SHA-256. SRC-201 aparece también en el manifiesto de S01; se conserva como referencia clave de T01.

## 3. Controles aplicados

### Hashes e integridad de fuentes — 8

| ID | Control | Resultado |
| --- | --- | --- |
| T10-H01 | Spec v0.4, tamaño, hash y coincidencia con `content.json` | PASS |
| T10-H02 | `content.json` sin cambios | PASS |
| T10-H03 | `content.md` sin cambios | PASS |
| T10-H04 | XLSX sin cambios; hash T09 conservado | PASS |
| T10-H05 | PPTX sin cambios; hash conservado | PASS |
| T10-H06 | PDF sin cambios; hash conservado | PASS |
| T10-H07 | Silver, referencias clave y PBIP con sus huellas registradas | PASS |
| T10-H08 | Árbol `references/` con el mismo manifiesto agregado | PASS |

### Decisión y arquitectura — 6

| ID | Control | Resultado |
| --- | --- | --- |
| T10-D01 | Decisión semanal de Jefatura de Operaciones, una frase, mismo significado en los cinco soportes | PASS |
| T10-D02 | Cinco cajas origen → Silver → Power Query → modelo → indicador | PASS |
| T10-D03 | Origen no documentado/por acordar; sin atribución a ERP, WMS, TMS ni telemetría | PASS |
| T10-D04 | 5 tablas, 0 relaciones y 0 medidas; propuesta para S06 diferenciada | PASS |
| T10-D05 | Brecha DCAM como ausencia documentada, no resuelta; DUD-S02-07 abierta | PASS |
| T10-D06 | Riesgo, hecho, límite, controles y pendiente coherentes | PASS |

### Mapa Silver — 6

| ID | Control | Resultado |
| --- | --- | --- |
| T10-M01 | DATA-001 a DATA-005; 5 filas y 7 campos por fila | PASS |
| T10-M02 | 35 campos coinciden en spec, contrato, Markdown, Excel y PPTX | PASS |
| T10-M03 | PDF con mapa completo 3+2 y siete campos por fuente | PASS |
| T10-M04 | Cada fuente aparece una vez en Excel, PPTX y PDF | PASS |
| T10-M05 | Frecuencia y grano de inventario exactos en todos los soportes | PASS |
| T10-M06 | WMS fuera del mapa y del modelo; contraste no cargado | PASS |

### KPI — 7

| ID | Control | Resultado |
| --- | --- | --- |
| T10-K01 | Cinco KPI, mismo nombre y orden | PASS |
| T10-K02 | Cinco niveles tácticos | PASS |
| T10-K03 | Fórmula en palabras, unidad y denominador | PASS |
| T10-K04 | `dias_en_almacen` sin tilde; tilde solo en el nombre visible | PASS |
| T10-K05 | Número de lotes vencidos como medida de apoyo separada | PASS |
| T10-K06 | Merma por valor excluida y registrada como pendiente | PASS |
| T10-K07 | Sin metas, umbrales, DAX ni responsables completados en S02 | PASS |

### Pendientes y declaraciones — 8

| ID | Control | Resultado |
| --- | --- | --- |
| T10-P01 | Trece pendientes con estado, responsable e hito | PASS |
| T10-P02 | Spec y contrato con los mismos campos por pendiente | PASS |
| T10-P03 | «Por acordar» conservado donde no hay respaldo | PASS |
| T10-P04 | Centro, origen y frecuencia siguen abiertos; registrar no resuelve | PASS |
| T10-P05 | Validación empresarial del centro pendiente; DCAM no resuelta | PASS |
| T10-P06 | Origen, propietarios y frecuencia pendientes | PASS |
| T10-P07 | Sesión compartida no ejecutada ni declarada | PASS |
| T10-P08 | Publicación en Service prevista y no ejecutada | PASS |

### Integridad estructural — 4

| ID | Control | Resultado |
| --- | --- | --- |
| T10-I01 | Excel: 12 hojas, 50 fórmulas, 11 DV, 1 rango CF/4 reglas, 19 combinadas, mapa `A1:G11` | PASS |
| T10-I02 | PPTX: 4 diapositivas, diapositiva 1 intacta, sin ejemplo de Acería en las entregadas | PASS |
| T10-I03 | PDF: 3 páginas 16:9, sin ejemplo de Acería | PASS |
| T10-I04 | Modelo: 5 tablas, 0 medidas y 0 relaciones | PASS |

## 4. Hallazgos

No se registraron diferencias materiales ni controles fallidos. Los cuatro FAIL observados durante el ajuste del propio script fueron defectos de las comprobaciones —normalización de énfasis Markdown, variantes equivalentes de redacción y representación del área de impresión—, no de los artefactos. Se corrigieron en el script y la ejecución final quedó 39/39 PASS.

## 5. Conclusión

**T10 se declara completada.** S02 deja Build T01–T10 completo; la auditoría independiente T11 no se inició ni está autorizada. No se creó `AUDIT.md` ni se declara S02 cerrada.

Los pendientes se conservan en `evidence/S02/pendientes.md`; la sesión y las autorizaciones se registran en `evidence/S02/session.md` y `evidence/S02/authorizations.md`.
