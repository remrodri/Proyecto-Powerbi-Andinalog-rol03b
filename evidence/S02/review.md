# T09 — Revisión visual de PPTX, XLSX y PDF

**Hito:** S02 — Decisión, arquitectura y mapa Silver  
**Fase:** Build  
**Fecha:** 2026-10-27  
**Alcance:** T09 únicamente. Revisión visual sobre el PPTX entregable, el PDF entregable y una copia temporal del XLSX. No se corrigieron defectos, no se modificaron entregables y no se inició T10.

## 1. Resultado

**T09 no se declara completada.**

- PPTX: **pasa** la revisión visual de la arquitectura y de las dos páginas del mapa.
- PDF: **pasa** la revisión visual de sus tres páginas.
- `Fichas KPI` del XLSX: la tabla C7:E11 es legible, pero el título A3 aparece truncado en la exportación A1:E11.
- `S02 Mapa Silver` del XLSX: **falla** la revisión visual por truncamiento de texto en varias celdas de las filas 7–11.

El defecto del mapa impide cumplir el criterio de T09: «no hay textos truncados, objetos superpuestos, filas partidas entre páginas ni columnas ilegibles». No se corrigió porque T09 no autoriza cambios en el XLSX.

## 2. Archivos y herramientas

| Artefacto | Revisión | Herramienta | Resultado |
| --- | --- | --- | --- |
| `deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx` | Diapositivas 2, 3 y 4 | PowerPoint COM 16.0 | Pasa |
| `deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf` | Páginas 1, 2 y 3 | `pypdfium2` 5.14.0 | Pasa |
| `work/S02/review.xlsx` | `S02 Mapa Silver!A1:G11` y `Fichas KPI!A1:E11` | Excel COM 16.0 | Falla por truncamiento |

- El PPTX se abrió en **solo lectura** y no se guardó: `save_calls=0`, `saved_by_com=false`.
- `work/S02/review.xlsx` es una copia byte a byte del XLSX entregable: 34.584 bytes y SHA-256 `C2F691F4CD5EDD47AD5E900A593740A9CD5EC11A197B5D5703DF9963E0C7D0D4` antes y después. Excel COM recalculó y exportó, pero **no guardó** la copia.
- El PDF se abrió y renderizó en solo lectura con `pypdfium2`.
- No hay procesos `EXCEL.EXE` ni `POWERPNT.EXE` activos en la comprobación posterior. El resultado de Excel COM registró un proceso transitorio al finalizar el script; la verificación independiente posterior encontró cero.

## 3. Huellas de las capturas

Todas las capturas se generaron el 2026-10-27.

| Captura | Resolución | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `screenshots/s02_t09_ppt_architecture.png` | 1920×1080 | 87.401 | `BA3EF09DBCDCFA2ABA2962AF6977B79ECFBCA1FD385E975CC39303A2A029B90F` |
| `screenshots/s02_t09_ppt_map_01.png` | 1920×1080 | 62.341 | `4E838DC00B1007928C2A3C557A623D572DE953515C17A0046F744261A182582C` |
| `screenshots/s02_t09_ppt_map_02.png` | 1920×1080 | 56.179 | `C3CE2DB7A88FD44BB1312C3D8C67DAD568B77277BD0006AE457BA1869C0EEEE5` |
| `screenshots/s02_t09_pdf_page_01.png` | 2880×1620 | 364.515 | `83FB6B1951E3C7C67E78B0039C70EDB849CD00F39D8D15CDDEF4A15DDD2EA87B` |
| `screenshots/s02_t09_pdf_page_02.png` | 2880×1620 | 234.505 | `F0FC08349DD573A949F5E844027743E6229BAD49ADED2D17BFAE44BA7386333C` |
| `screenshots/s02_t09_pdf_page_03.png` | 2880×1620 | 177.244 | `CDF21FCDBA791F0520ADC77D98CF57C574FC970E068C0CF5DF0C54B30D92EA99` |
| `screenshots/s02_t09_xlsx_map.png` | 2376×1836 | 183.005 | `AC4BB4C440951C25A7DBDE5D38E001673C3E4B6464875C798768F23150CD76F6` |
| `screenshots/s02_t09_xlsx_kpi.png` | 2376×1836 | 347.754 | `718435067127810C4B79A11A79289FB0FDEF8E6127D74286AA9517EB8B530475` |

Las capturas de PPTX coinciden en SHA-256 con las evidencias de T04 y T05: `BA3EF09D…B90F`, `4E838DC0…582C` y `C3CE2DB7…EEE5`. Esto confirma que las diapositivas entregables no cambiaron entre T04/T05 y T09.

## 4. PPTX

### 4.1 Arquitectura — diapositiva 2

- Se ven las cinco cajas: Origen, Tabla Silver, Power Query, Modelo Semántico e Indicador.
- La decisión de la Jefatura de Operaciones se lee completa.
- Los bloques «Brecha DCAM de partida», «Riesgo principal → control» y «Pendiente y responsable» están completos.
- No hay texto cortado, desbordado, superpuesto ni flechas ocultas.
- El bloque de riesgo usa 8 pt y sigue siendo legible a 1920×1080.

### 4.2 Mapa Silver — diapositivas 3 y 4

- `Mapa Silver — 1/2`: siete columnas, cabecera repetida y tres filas completas.
- `Mapa Silver — 2/2`: siete columnas, cabecera repetida y dos filas completas.
- Orden visible: DATA-001 a DATA-005, sin filas partidas ni columnas separadas.
- Los nombres largos de archivo, la frecuencia de Inventario y las claves compuestas se leen completos.
- WMS no aparece en las cinco filas del mapa.
- No hay objetos superpuestos ni texto fuera de las celdas.

## 5. PDF

| Página | Contenido | Revisión |
| ---: | --- | --- |
| 1 | Diagrama de arquitectura | Completa; coincide visualmente con la diapositiva 2 |
| 2 | `Mapa Silver — 1/2` | Completa; siete columnas y tres filas |
| 3 | `Mapa Silver — 2/2` | Completa; siete columnas y dos filas |

- Las tres páginas miden 960×540 pt (16:9) y no están vacías.
- No aparece «ACERÍA» ni la diapositiva de ejemplo.
- No se observan páginas cortadas, filas partidas, columnas ilegibles ni diferencias visuales materiales frente al PPTX.
- La comparación PPTX–PDF fue visual e individual; no se calculó una diferencia pixel a pixel entre formatos de distinta resolución.

## 6. XLSX — `S02 Mapa Silver`

### 6.1 Contenido estructural

- Se ven las siete columnas y las cinco filas DATA-001 a DATA-005.
- Las filas no se parten entre páginas: el rango se exportó en una sola página.
- La tabla conserva los encabezados y el orden del mapa.
- Los valores completos existen en el libro; el problema es de **altura de fila y ajuste de impresión**, no de pérdida de datos.

### 6.2 Defecto visual material — `OV-T09-01`

La exportación `S02 Mapa Silver!A1:G11` trunca el contenido de varias celdas porque las filas 8–11 conservan 15 pt de alto y la fila 7 no tiene altura suficiente para todo el texto ajustado. Ejemplos observados:

- `A8`: `andinalog_productos_silver.c`, sin `sv` final.
- `A10`: `andinalog_inventory_trackin`, sin `g_silver.csv`.
- `A11`: `andinalog_warehouse_costs`, sin `_silver.csv`.
- `B10`: `Un lote con ingreso, salida y`, sin `merma en esta entrega`.
- `D7`: `Observación cada 30 min;`, sin `actualización por acordar`.
- `D8` y `D9`: `Catálogo;`, sin `actualización por acordar`.
- `D10`: `Sin`, sin el resto de la frecuencia de Inventario.
- `D11`: `Mensual;`, sin `actualización por acordar`.
- `E8`–`E11`: `Por acordar;`, sin `revisión Grupo 06`.
- `F8`: `Extrapolar KPI térmicos a todo el`, sin `catálogo`.
- `F9`: `Usar centro_distribucion_base`, sin `como centro operativo`.
- `F10`: `Leer vencimiento como stock`, sin `vigente`.
- `G9`: `Mantener la distinción`, sin `base/operativo y registrarla como pendiente`.
- `G10`: `Declarar que todos los lotes salieron;`, sin `KPI históricos`.

**Impacto:** la evidencia visual no permite leer el mapa completo; el entregable no cumple el criterio de celdas legibles en su presentación exportada. El defecto corresponde a la copia exacta del XLSX entregable, no a una copia alterada.

No se corrigió en T09. La corrección de alturas de fila o del área/ajuste de impresión requiere autorización dentro de Build o Fix.

## 7. XLSX — `Fichas KPI`

- La tabla C7:E11 muestra las cinco filas completas:
  - C7:C11 = `Táctico`.
  - D7:D11 = fórmulas en palabras completas.
  - E7:E10 = `Porcentaje`; E11 = `Días`.
- No aparece un sexto KPI ni «merma por valor».
- Las columnas A–E de la tabla son legibles y no hay filas partidas.

### Observaciones secundarias

- **OV-T09-02:** el título fusionado `A3:AA3` se corta al exportar solo A:E; se lee hasta `…es la entrad:`.
- El rótulo `Fecha:` queda visible sin su valor porque F4 está fuera del área exportada A:E.

Estas observaciones no afectan los cinco KPI ni los valores C7:E11, pero impiden declarar que toda la captura del libro está libre de truncamiento.

## 8. Integridad posterior

| Archivo | Bytes | SHA-256 | Estado |
| --- | ---: | --- | --- |
| PPTX entregable | 43.872 | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | Igual al baseline T09 |
| XLSX entregable | 34.584 | `C2F691F4CD5EDD47AD5E900A593740A9CD5EC11A197B5D5703DF9963E0C7D0D4` | Igual al baseline T09 |
| PDF entregable | 237.204 | `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42` | Igual al baseline T09 |
| SRC-201 | 36.907 | `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30` | Sin cambios |
| SRC-203 | 38.618 | `36E4E9AE273DF191CCD05171F276697CB7A000698BBB3C523EA5C8A188F96516` | Sin cambios |
| PBIP | 292 | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` | Sin cambios |

No se modificaron spec, plan, `tasks.md`, `MEMORY.md`, referencias, Silver, S01 ni el modelo Power BI.

## 9. Artefactos de soporte

- `work/S02/t09_precheck.json`: huellas iniciales.
- `work/S02/t09_ppt_result.json`: apertura en solo lectura, 4 diapositivas, capturas 2–4 y cierre sin guardar.
- `work/S02/t09_render_pdf.json`: 3 páginas de 960×540 pt y capturas de las páginas.
- `work/S02/t09_xlsx_result.json`: copia, recálculo, exportaciones y hashes.
- `work/S02/t09_xlsx_render.json`: exportaciones de una página por rango y PNG.
- `work/S02/t09_xlsx_map.pdf`: 148.799 bytes, SHA-256 `D772D1AD4733F1DC6CE8A0247DF3C2C67C62AEAF9BCFB764B79522187BF36072`.
- `work/S02/t09_xlsx_kpi.pdf`: 152.688 bytes, SHA-256 `12E1066EED39BE51724F1063453B28E08547EDB387984F6EDD52ACB53F255E7F`.

## 10. Conclusión y pendiente

- **PPTX:** pasa.
- **PDF:** pasa.
- **XLSX `Fichas KPI`:** tabla C7:E11 pasa; título A3 y valor de fecha presentan defectos visuales secundarios.
- **XLSX `S02 Mapa Silver`:** falla por truncamiento material en filas 7–11.
- T09 permanece `[ ]`. No se inicia T10 ni se corrige el libro.
- Se requiere autorización para corregir el XLSX y repetir la revisión visual de T09.

---

## 11. Ronda 2 — Corrección y nueva revisión

**Fecha:** 2026-10-27  
**Alcance:** corregir únicamente `S02 Mapa Silver` en el XLSX entregable y repetir la revisión visual de T09 con evidencia separada para `Fichas KPI`. No se modifica `Fichas KPI!A3:AA3`, no se alteran celdas combinadas, no se inicia T10 y no se reduce el alcance futuro de la plantilla.

La conclusión de la sección 10 corresponde a la primera ronda y se conserva como historial. Esta sección registra la corrección y la segunda revisión.

### 11.1 Cambio aplicado al entregable

Se respaldó el XLSX anterior en `work/S02/t09_fix_backup.xlsx` antes de modificarlo.

| Comprobación | Antes | Después |
| --- | ---: | ---: |
| Bytes del XLSX | 34.584 | 39.510 |
| SHA-256 del XLSX | `C2F691F4CD5EDD47AD5E900A593740A9CD5EC11A197B5D5703DF9963E0C7D0D4` | `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D` |

Cambios materiales guardados en `S02 Mapa Silver`:

- Alturas de filas 7–11: de `27,75 / 15 / 15 / 15 / 15` pt a `45` pt.
- Área de impresión: `A1:G11`.
- A4 horizontal, ajuste a una página de ancho y una de alto, márgenes de 18 pt y centrado horizontal.
- No se cambiaron valores, fórmulas, estilos efectivos, anchos de columna, validaciones, formato condicional ni celdas combinadas.

Excel COM guardó el libro y después lo reabrió en solo lectura para exportar `work/S02/t09_fix_map_r2.pdf`. La exportación confirma que Excel puede abrir el archivo posterior sin reparación.

### 11.2 Evidencia de `Fichas KPI` sin modificar el entregable

`Fichas KPI!A3:AA3` conserva su combinación original en el entregable. No se guardó ningún cambio de área, altura, visibilidad ni escala en el XLSX entregable.

Para la revisión visual se usó `work/S02/review.xlsx`, copia byte a byte del XLSX corregido, y se generaron dos exportaciones temporales:

1. Encabezado y metadatos: área temporal `A1:F4`, fila 3 a 60 pt y columnas `G:AA` ocultas solo en la copia temporal. Esto permitió que el título completo de `A3:AA3` se ajustara dentro de A:F y que se viera `F4 = 2026-10-20`. El merge `A3:AA3` se comprobó intacto; la copia no se guardó.
2. Contenido de S02: área temporal `A4:F11`, que muestra Equipo, Subcaso, Fecha/F4, los cinco KPI, nivel táctico, fórmula en palabras y unidad.

El corte anterior del título fue causado por exportar únicamente `A1:E11`, dejando fuera parte de una celda combinada hasta `AA`; no era contenido truncado dentro del XLSX.

### 11.3 Resultado de la segunda revisión

| Elemento | Resultado | Evidencia |
| --- | --- | --- |
| `S02 Mapa Silver` | Pasa: filas 7–11 completas, sin truncamiento, columnas legibles y sin filas partidas | `screenshots/s02_t09_xlsx_map_r2.png` |
| `Fichas KPI` — encabezado | Pasa: título completo, Equipo, Subcaso, Fecha y valor de F4 visibles | `screenshots/s02_t09_xlsx_kpi_header_r2.png` |
| `Fichas KPI` — tabla | Pasa: cinco KPI, nivel táctico, fórmulas y unidades completos | `screenshots/s02_t09_xlsx_kpi_table_r2.png` |
| PPTX | Pasa sin cambios | Capturas de la primera ronda; hash sin cambios |
| PDF | Pasa sin cambios | Capturas de la primera ronda; hash sin cambios |

### 11.4 Capturas nuevas

| Captura | Resolución | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `screenshots/s02_t09_xlsx_map_r2.png` | 2376×1836 | 258.157 | `7B38E173ADE2FD46092A30787A850353F07434A17766CC042BD393879C96B672` |
| `screenshots/s02_t09_xlsx_kpi_header_r2.png` | 2376×1836 | 106.629 | `F27E3ED687816724A1882E71E2BE858EACBD75E2E342E9DECD6D957FB68E3BB8` |
| `screenshots/s02_t09_xlsx_kpi_table_r2.png` | 2376×1836 | 304.895 | `BFC3A35FF18D1ED8CD2AF4215D292286DA50F331BE787AAB6E717B978653DD5C` |

PDFs temporales:

| PDF | Bytes | SHA-256 |
| --- | ---: | --- |
| `work/S02/t09_fix_map_r2.pdf` | 149.693 | `076CB628207EC56D875730FE1F135C996F604AD3F55F405F81132ED885E0E1F6` |
| `work/S02/t09_fix_kpi_header_r2.pdf` | 139.877 | `960829DE1CA154E34C82289D9715EB14874CA6F6CD8D21A6BEA6571670A3AAF2` |
| `work/S02/t09_fix_kpi_table_r2.pdf` | 142.792 | `B011D64909A6C5A3C45076B99760642C2F9FBA0216B0943E81C23FD9C893BE14` |

### 11.5 Integridad posterior

| Archivo | Bytes | SHA-256 | Estado |
| --- | ---: | --- | --- |
| PPTX entregable | 43.872 | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` | Sin cambios |
| XLSX entregable | 39.510 | `31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D` | Corregido solo en Mapa Silver |
| PDF entregable | 237.204 | `07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42` | Sin cambios |
| SRC-201 | 36.907 | `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30` | Sin cambios |
| SRC-203 | 38.618 | `36E4E9AE273DF191CCD05171F276697CB7A000698BBB3C523EA5C8A188F96516` | Sin cambios |
| PBIP | 292 | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` | Sin cambios |

Controles de integridad ejecutados:

- 12 hojas en el mismo orden; 50 fórmulas idénticas; valores idénticos en todas las hojas.
- 11 validaciones conservadas en tipo, fórmula, rango y mensajes; 1 rango de formato condicional conservado.
- 19 celdas combinadas conservadas; anchos y visibilidad de columnas sin cambios.
- `Fichas KPI` conserva valores, filas, estilos efectivos y configuración de impresión; su `print_area` sigue vacío en el entregable.
- `S01 Inventario` y las demás hojas conservan valores, estilos efectivos y configuración de impresión efectiva.
- El libro es un ZIP válido de 27 partes, sin errores CRC y con las partes requeridas.
- Excel COM reabrió el XLSX posterior y exportó el mapa; no quedaron procesos `EXCEL.EXE`.
- Los valores por defecto que Excel reserializó (`font.family`, alineaciones generales, `operator`/`errorStyle` de validaciones y campos nulos de formato condicional) no alteran el contenido ni el aspecto efectivo.

Artefactos de control: `validation/results/S02/t09_fix_checks.json` (`XF01`–`XF19`, todos en `true`), `work/S02/t09_fix_apply_result.json`, `work/S02/t09_fix_kpi_result.json`, `work/S02/t09_fix_kpi_header_result.json`, `work/S02/t09_fix_render.json`, `work/S02/t09_fix_pre_state.json` y `work/S02/t09_fix_post_state.json`. La primera copia de revisión se conserva como `work/S02/review_r1.xlsx`; `work/S02/review.xlsx` corresponde al XLSX corregido.

### 11.6 Conclusión

- `OV-T09-01` queda cerrado: el mapa se lee completo en la segunda exportación.
- `OV-T09-02` queda cerrado como efecto del área de exportación, no como truncamiento del libro; la evidencia separada muestra el título completo y F4.
- **T09 se declara completada.** No se inicia T10.
