# T08 - Exportación del PDF sin la diapositiva de ejemplo

Fecha: 2026-10-27
Alcance: Build T08 únicamente. No se inició T09, no se modificó el PPTX entregable, el XLSX, las referencias, los Silver, el PBIP ni los archivos de S01.

## 1. Tratamiento registrado de la diapositiva 1

Se leyó `references/S02/GIAD-M4-S02_Hito_Proyecto_Integrador.docx` (SRC-102). La guía indica: «La primera diapositiva es un ejemplo con Acería Andina; completen la segunda».

Por tanto, se registra por escrito que **la diapositiva 1 es un ejemplo y queda excluida del PDF**. La exclusión se aplicó únicamente a la copia temporal `work/S02/export.pptx`; el PPTX editable `deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx` conserva sus cuatro diapositivas y su diapositiva 1.

## 2. Archivos y huellas

| Archivo | Tamaño | SHA-256 | Estado |
| --- | ---: | --- | --- |
| PPTX entregable, antes y después | 43.872 bytes | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | Sin cambios |
| `work/S02/export.pptx`, copia inicial | 43.872 bytes | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | Idéntica al PPTX |
| `work/S02/export.pptx`, copia final de 3 diapositivas | 49.001 bytes | `890AD583FA93285BC97791BE14454ACB6BB328D2BEAFFE66719941E0C3FC94CF` | Solo se eliminó la diapositiva 1 |
| PDF entregable | 237.204 bytes | `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42` | 3 páginas |

La copia inicial era byte a byte idéntica al PPTX. El aumento de tamaño a 49.001 bytes corresponde a la reserialización de PowerPoint COM al guardar la copia sin la diapositiva 1; no se reescribieron textos, tablas ni formas.

## 3. Método de exportación

- Se copió el PPTX entregable a `work/S02/export.pptx`.
- Con **PowerPoint COM 16.0 (16.0.20527.20088)** se abrió la copia, se eliminó únicamente `Slides.Item(1)` y se guardó la copia con 3 diapositivas.
- Se reabrió la copia en solo lectura y se exportó a PDF con `Presentation.SaveAs(..., ppSaveAsPDF=32)`, método nativo de PowerPoint. No se usó impresora, LibreOffice, Edge, captura de pantalla ni render de páginas para producir el PDF.
- Se cerró sin guardar cambios adicionales. Al finalizar quedaron **0 procesos POWERPNT**.
- El PPTX entregable no se abrió con COM y conserva su hash.

PowerPoint COM normalizó el ancho de la copia de 12.191.695 a 12.192.000 EMU (0,024 pt) al guardarla. Las formas, textos y tablas de las tres diapositivas conservan el mismo inventario que las diapositivas 2–4 del PPTX fuente; la diferencia de tamaño es técnica y deja la copia en 16:9 exacto.

Correspondencia verificada:

| PPTX editable | Copia temporal | PDF |
| ---: | ---: | ---: |
| Diapositiva 2, arquitectura | Diapositiva 1 | Página 1 |
| Diapositiva 3, Mapa Silver 1/2 | Diapositiva 2 | Página 2 |
| Diapositiva 4, Mapa Silver 2/2 | Diapositiva 3 | Página 3 |

## 4. Controles del PDF

Herramienta: `pypdfium2` 5.14.0. Resultados en `validation/results/S02/pdf_structure.json` y `validation/results/S02/pdf_text.json`.

### Estructura: 8/8 PASS

- El PDF abre con `pypdfium2`; tiene exactamente 3 páginas.
- Página 1: diagrama de arquitectura del subcaso, con la decisión de la Jefatura de Operaciones y el bloque «1 · ORIGEN».
- Páginas 2 y 3: «Mapa Silver — 1/2» y «Mapa Silver — 2/2».
- Cada página mide 960 x 540 pt, ratio 1,777777778. Tolerancia aplicada: ±0,5 pt por dimensión y ±0,001 en el ratio; el PDF es 16:9 exacto, no A4.
- Ninguna página está vacía: longitudes de texto 1.651, 925 y 754 caracteres; fracción de píxeles no blancos 0,400718, 0,348002 y 0,433495.
- Las tres páginas se renderizaron a PNG de 1920 x 1080 en `work/S02/t08_pdf_page_1.png` a `t08_pdf_page_3.png`.
- No aparece `ACERÍA`, `ACERIA`, `EJEMPLO`, `Laminación`, `LAM-01`, `OEE` ni `SCADA` en el texto del PDF.

### Texto: 10/10 PASS

- Los cinco nombres oficiales aparecen exactamente una vez en el conjunto de las páginas 2–3:
  - `andinalog_iot_telemetry_silver.csv`
  - `andinalog_productos_silver.csv`
  - `andinalog_flota_silver.csv`
  - `andinalog_inventory_tracking_silver.csv`
  - `andinalog_warehouse_costs_silver.csv`
- `andinalog_wms_orders_silver.csv` aparece 0 veces. La palabra `WMS` no aparece en las páginas del mapa; solo permanece en la nota de origen de la arquitectura («No se atribuye ERP, WMS, TMS ni telemetría»), fuera del mapa.
- Aparece la decisión completa: «La Jefatura de Operaciones decide cada semana dónde priorizar controles térmicos por producto y camión y qué lotes o centros revisar por vencimiento y merma.»
- Aparecen «No documentado» y «Por acordar».
- La brecha DCAM y su estado no resuelto aparecen con «Brecha DCAM de partida», «C4 Conocimiento de los datos», «1 Incipiente» y «Ausencia documentada; no resuelta.»
- Las siete cabeceras —Archivo / tabla, Granularidad, Identificador único, Frecuencia, Propietario, Riesgo y Control propuesto— aparecen en cada página de mapa.
- No aparecen «merma por valor», «metas», «DAX» ni «RLS».
- No se afirma una validación empresarial ejecutada. «Validación empresarial» solo figura como solicitud o pendiente; «validador por acordar» se refiere al responsable pendiente.

## 5. Contenido preservado

Se comparó el inventario de formas, nombres, posiciones, tamaños, textos y tablas entre las diapositivas 2–4 del PPTX y las diapositivas 1–3 de la copia. Las tres comparaciones son iguales: 32 formas para arquitectura y 4 formas para cada página del mapa. No se reescribió el contenido de las diapositivas conservadas.

## 6. Integridad de los originales

| Archivo | Antes | Después | Resultado |
| --- | --- | --- | --- |
| PPTX entregable | `26324855...325D` | `26324855...325D` | Sin cambios |
| XLSX de seguimiento | `C2F691F4...D0D4` | `C2F691F4...D0D4` | Sin cambios |
| SRC-201 | `0CCC4A53...DF30` | `0CCC4A53...DF30` | Sin cambios |
| SRC-203 | `36E4E9AE...6516` | `36E4E9AE...6516` | Sin cambios |
| Spec S02 | `A91958C3...598A` | `A91958C3...598A` | Sin cambios |
| PBIP | `F8712089...1CCE` | `F8712089...1CCE` | Sin cambios |

También se conservaron las huellas agregadas de los árboles:

| Árbol | Archivos | SHA-256 agregado |
| --- | ---: | --- |
| `references/` | 52 | `708F12A190829A2DBFB0C729CF4E088C049EE9CFEF75700AE87D9565B20D0A65` |
| `specs/001-s01-inventory/` | 4 | `735F95716D46806C54B06C6E1F5BCA19CCDA4020B0218E863FFED78A7F7DC796` |
| `evidence/S01/` | 21 | `77E40D92A598691DB42C3C63BE8CE6C98F2D36BA599CB6D086A93C886B124538` |
| `powerbi/` | 23 | `1907B96A29AD0915AF129B4B0AE7D9A97658157D9078DBC6C37A444F45B33CD8` |
| Silver (`C:/GIAD/GIAD-M3_datos_sinteticos_v10_silver`) | 16 | `7CAE3B6923185A45B9C003AB937EE386E2C4C0C2FE920970345F9F21C71CCBBF` |

## 7. Limitaciones

- La revisión es estructural y textual. No se declara aprobada la revisión visual completa; corresponde a T09.
- Los PNG de las páginas se usaron solo para comprobar que el PDF es renderizable y no está vacío; no sustituyen la revisión visual de T09.
- No se ejecutaron pruebas en Power BI Desktop, DAX, RLS, publicación en Service ni validación empresarial.
- El PDF se generó desde la copia temporal sin la diapositiva 1; el PPTX editable conserva el ejemplo y las tres diapositivas de contenido.
- T08 no cierra S02. T09–T13 siguen pendientes.

## 8. Resultado

**T08 completada.** Los controles estructurales y textuales pasan, los originales conservan sus huellas y el PDF entregable contiene la arquitectura seguida del mapa completo. No se inicia T09.

Evidencia de soporte: `work/S02/t08_precheck.json`, `work/S02/t08_com_result.json`, `work/S02/t08_postcheck.json`, `work/S02/t08_pdf_page_1.png` a `t08_pdf_page_3.png`, `validation/results/S02/pdf_structure.json` y `validation/results/S02/pdf_text.json`.
