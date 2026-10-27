# T01 — Huellas iniciales y calificación de COM

Fecha de ejecución: 2026-10-27, 20:33–20:34 UTC.
Alcance autorizado: Build T01 únicamente. No se creó `deliverables/S02/`, no se modificó el PPTX entregable, no se inició T02.

## 1. Entorno y aislamiento

- Al iniciar T01 no había procesos `EXCEL`, `POWERPNT` ni `WINWORD` en ejecución.
- Las copias de trabajo se crearon en `work/S02/` con nombres únicos; nunca se abrieron los originales con COM.
- Cada herramienta se creó con `New-Object -ComObject`, se usó su propia instancia, se cerró el libro o la presentación y se llamó `Quit`.
- Al finalizar no quedaron procesos de Office en ejecución.
- No se cerró ni se actuó sobre ninguna aplicación del usuario.

## 2. Resultado de la calificación

| Prueba | Herramienta | Resultado | Archivo de resultado |
| --- | --- | --- | --- |
| V02A | PowerPoint COM 16.0 (16.0.20527.20088) | **Calificada** | `work/S02/v02a_result.json` |
| V02B | Excel COM 16.0 (16.0.20527.20088) | **Calificada** | `work/S02/v02b_result.json` |

Ambas herramientas estaban instaladas y registradas antes de T01, pero **no estaban calificadas**. La calificación se obtiene en esta tarea; antes de T01 solo constaba su disponibilidad.

## 3. V02A — PowerPoint COM

Versión COM informada: `16.0`. Binario: `POWERPNT.EXE 16.0.20527.20088`.

| Operación | Resultado |
| --- | --- |
| Abrir `work/S02/com_ppt_test.pptx` | Correcto; 2 diapositivas; sin error ni diálogo de reparación |
| Guardar copia | `SaveCopyAs` a `work/S02/com_ppt_saved.pptx`; 42.700 bytes |
| Renderizar diapositiva 1 | PNG 1920 × 1080, RGB, contenido no vacío |
| Exportar a PDF | `work/S02/com_ppt_test.pdf`; 2 páginas; 2.057 caracteres extraídos |
| Releer resultados | PNG verificado con Pillow; PDF con `pypdfium2`; PPTX guardado con `python-pptx` (2 diapositivas, 32 formas cada una) |

Evidencia:

| Archivo | Tamaño | SHA-256 |
| --- | ---: | --- |
| `work/S02/com_ppt_slide1.png` | 87.510 | `65C27DD3953089CBDF69BEEA58BAB503DD0211331C28D5F76B409C0BC343E9DA` |
| `work/S02/com_ppt_test.pdf` | 289.629 | `FF69E59C97056B10DA7877CA0F4BCC6C0841E2017D7D87D3A145FB3D20C85285` |
| `work/S02/com_ppt_saved.pptx` | 42.700 | `F4D15C0797B66326A3D1F99E1A2C9CAEEA84B782D5C6CBFF5CF44BC5D6895BEE` |

El PDF conserva la diapositiva 1 de ejemplo (`EJEMPLO · ACERÍA ANDINA`) y la diapositiva 2 de plantilla. Esto es esperado en T01: la exportación definitiva sin el ejemplo corresponde a T08.

## 4. V02B — Excel COM

Versión COM informada: `16.0`. Binario: `EXCEL.EXE 16.0.20527.20088`.

| Operación | Resultado |
| --- | --- |
| Abrir `work/S02/com_excel_test.xlsx` | Correcto, en solo lectura; 12 hojas; sin error ni diálogo de reparación |
| Recalcular | `CalculateFull()` sin error |
| Exportar `S02 Mapa Silver` | `work/S02/com_excel_S02_Mapa_Silver.pdf`; 1 página; 437 caracteres |
| Exportar `Fichas KPI` | `work/S02/com_excel_Fichas_KPI.pdf`; 8 páginas; 3.765 caracteres |
| Cerrar sin guardar | `Workbook.Close(False)` |
| Releer resultados | Ambos PDF abiertos con `pypdfium2` |
| Integridad de la copia | SHA-256 sin cambios tras abrir, recalcular y exportar: `E7F09B0A…DB74F1` |

Evidencia:

| Archivo | Tamaño | SHA-256 |
| --- | ---: | --- |
| `work/S02/com_excel_S02_Mapa_Silver.pdf` | 150.124 | `D99F3CF81892C1EEBD4CA37F3AC092767558ED0480B1DA0D0FF0D5C3454E5FC9` |
| `work/S02/com_excel_Fichas_KPI.pdf` | 223.772 | `6AB7AB6612548ECF373642A881B61DF5402E6A1BC75D087BFAC4BB4DBDDD4FEA` |

La hoja `S02 Mapa Silver` se exportó con el ejemplo de Acería todavía presente y sin las cinco filas del subcaso; es evidencia de que la exportación funciona, no del contenido final. `Fichas KPI` conserva sus 8 páginas por el ancho de la hoja, comportamiento ya observado en S01.

## 5. Disponible frente a calificado

| Herramienta | Antes de T01 | Después de T01 |
| --- | --- | --- |
| PowerPoint COM | Instalada y registrada; sin prueba de apertura, guardado, render ni exportación | **Calificada** para abrir, guardar, renderizar y exportar copias temporales |
| Excel COM | Instalada y registrada; sin prueba de apertura, recálculo ni exportación | **Calificada** para abrir copias temporales en solo lectura, recalcular y exportar evidencia visual |

La calificación se limita a esta máquina y a estas copias. No demuestra que PowerPoint o Excel abran sin reparación el PPTX o el XLSX entregables definitivos, ni sustituye la revisión visual de T09.

## 6. Integridad de los objetos con huella

| Objeto | Ruta | Tamaño | SHA-256 |
| --- | --- | ---: | --- |
| SRC-201 | `references/general/GIAD-M4_Plantillas_Proyecto_Integrador_v2.xlsx` | 36.907 | `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30` |
| SRC-203 | `references/S02/GIAD-M4-S02_Plantilla_Diagrama_Arquitectura.pptx` | 38.618 | `36E4E9AE273DF191CCD05171F276697CB7A000698BBB3C523EA5C8A188F96516` |
| Copia Excel | `deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx` | 33.844 | `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1` |
| Spec S02 | `specs/002-s02-architecture/spec.md` | 28.474 | `A91958C34BADCF6E5AAF3D0F063AC94C3FE458436A9C30AF6AE1362FD626598A` |
| PBIP (adicional) | `powerbi/AndinaLog_03B.pbip` | 292 | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` |

Las cinco huellas se releyeron al terminar y coinciden con `validation/results/S02/initial_manifest.json`. La copia Excel entregable y la copia temporal conservan el mismo hash, lo que confirma que el recálculo no se guardó.

## 7. Limitaciones

- La calificación no incluye revisión de legibilidad, recortes ni solapamientos; eso corresponde a T09.
- No se probó la exportación del PDF final ni la eliminación de la diapositiva 1; corresponde a T08.
- No se abrió Power BI Desktop ni se ejecutaron pruebas de modelo o Service.
- Los PDF de Excel se generaron desde una copia temporal en solo lectura; no se modificó el libro entregable.
