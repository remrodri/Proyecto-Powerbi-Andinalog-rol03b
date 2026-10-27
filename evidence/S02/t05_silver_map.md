# T05 — Mapa Silver en el PPTX

**Hito:** S02 — Decisión, arquitectura y mapa Silver  
**Fase:** Build  
**Fecha:** 2026-10-27  
**Alcance autorizado:** añadir el mapa Silver desde la diapositiva 3 del PPTX, sin editar Excel ni exportar el PDF final.

## Resultado

- Se añadieron **2 diapositivas** al PPTX: diapositivas 3 y 4.
- Paginación: **3 + 2 filas** completas.
  - `Mapa Silver — 1/2`: DATA-001, DATA-002 y DATA-003.
  - `Mapa Silver — 2/2`: DATA-004 y DATA-005.
- Cada página contiene una **tabla nativa de PowerPoint de 7 columnas** con las siete cabeceras repetidas.
- Fuente de tabla: **10.5 pt**; título: 24 pt; kicker: 9.5 pt. Mínimo global: **9.5 pt**.
- No se añadió texto flotante ni pie fuera de la tabla: el archivo está en la columna `Archivo / tabla` y todo el contenido del mapa vive en celdas.
- **WMS no aparece** en ninguna diapositiva del mapa, ni como fila, columna o nota. DATA-006 y DATA-007 tampoco aparecen.

## Huellas previas a la edición

| Elemento | Valor |
| --- | --- |
| PPTX T04 | 39.263 bytes; SHA-256 `71DCE2F66C96EFB0FF7B3ADDB67ABDD9F1E41215D945388836C21C6F7A53664A` |
| Diapositiva 1 — XML | `0F944D0FB93C30E7CBAF0D7ED52D35900870A1E1E6BA20E31E0541D1770C7CC9` |
| Diapositiva 1 — texto | `7023CF3D2379FFF73887AED7CAE75130646DB38F496D99C477D393E1B0F850FA` |
| Diapositiva 1 — inventario | `26CB5FA7859FD8082944BC3CACC57350C28EA14C7726F547EB7E231ABBE681BC` |
| Diapositiva 2 — XML | `87E251E0CDA2AD828D539905A0D7BA5886941DF6B851B9BD3A49DB648637619E` |
| Diapositiva 2 — texto | `09DC4C11B12649463E9BF059BF4034CCB2565462F117CF0007BB79745A5D3CA8` |
| Diapositiva 2 — inventario | `FCF19D50860C8889BE1660B9725B080E3F8AF4DCF272F21A888C67FEB7B2A52A` |

El inventario previo de la diapositiva 1 coincide con la huella de T03. La diapositiva 2 es la versión completada en T04.

## Estructura de las tablas

| Página | Filas de datos | Columnas | Alto de tabla | Filas |
| --- | ---: | ---: | ---: | --- |
| 1/2 | 3 | 7 | 5,50 in | cabecera 0,55 in; 3 × 1,65 in |
| 2/2 | 2 | 7 | 5,50 in | cabecera 0,55 in; 2 × 2,475 in |

- Posición: izquierda 0,35 in; superior 1,02 in; ancho 12,63 in.
- Anchos: 2,55 / 1,26 / 1,70 / 2,06 / 1,20 / 1,80 / 2,06 in.
- Cabeceras: `Archivo / tabla`, `Granularidad`, `Identificador único`, `Frecuencia`, `Propietario`, `Riesgo`, `Control propuesto`.
- Tablas editables, sin imágenes ni texto rasterizado.

## Contenido normativo conservado

- Telemetría: `viaje_id + minutos_desde_despacho`.
- Propietarios: `Por acordar; revisión Grupo 06` en las cinco filas.
- Inventario: `Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y salida; actualización por acordar`.
- Inventario: una fila por lote con ingreso, salida y merma en esta entrega; riesgo de leer vencimiento como stock vigente; control de lotes salidos y KPI históricos.
- Costos: un centro en un mes; `centro_distribucion + periodo_mes`; control `No asignar; relación temporal en S06`.
- Flota: riesgo de usar `centro_distribucion_base` como centro operativo; control de distinción base/operativo registrada como pendiente.
- No se añadieron definiciones del centro ni se declaró resuelta la brecha.

## Revisión visual

Se renderizaron las diapositivas 3 y 4 con PowerPoint COM a PNG de **1920 × 1080** y se revisaron una por una.

- **1/2:** siete columnas visibles, cabecera repetida, tres filas completas, sin truncamiento, desbordamiento, superposición ni fila partida. El nombre largo de archivo y la clave compuesta se leen completos; la clave se parte solo en el espacio junto a `+`.
- **2/2:** siete columnas visibles, cabecera repetida, dos filas completas, sin truncamiento, desbordamiento, superposición ni fila partida. La frecuencia larga de Inventario se lee completa.
- Orden visual: DATA-001, DATA-002, DATA-003, DATA-004, DATA-005.
- WMS ausente en ambas páginas.

| Página | PNG | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| 1/2 | `evidence/S02/screenshots/s02_t05_map_slide_1.png` | 62.341 | `4E838DC00B1007928C2A3C557A623D572DE953515C17A0046F744261A182582C` |
| 2/2 | `evidence/S02/screenshots/s02_t05_map_slide_2.png` | 56.179 | `C3CE2DB7A88FD44BB1312C3D8C67DAD568B77277BD0006AE457BA1869C0EEEE5` |

## Controles

Resultado: **45/45 controles pasan** en `validation/results/S02/pptx_checks.json`; estado `PASS`, `t05_complete=true`.

Comprobaciones principales:

- 2 diapositivas nuevas; 4 diapositivas totales; 16:9.
- 5 filas de datos exactas, sin duplicados ni omisiones; orden igual a `content.json`.
- 7 columnas por página; cabeceras idénticas y repetidas.
- Todas las celdas coinciden literalmente con `content.json`.
- Sin WMS, DATA-006 ni DATA-007 dentro del mapa.
- Tabla dentro de la diapositiva; sin superposición entre título, línea y tabla.
- Diapositivas 1 y 2 con XML, texto, inventario y geometría idénticos a T04.
- SRC-203, SRC-201, Excel de seguimiento, PBIP y los cinco Silver conservan sus hashes.
- No existe PDF final en `deliverables/S02/`.

## PowerPoint COM

- PowerPoint 16.0 abrió el PPTX **sin reparación** y en **solo lectura**.
- Exportó las dos diapositivas nuevas a PNG 1920×1080.
- No guardó: `save_calls=0`, `saved_by_com=false`.
- El conteo inmediato tras cerrar fue 1 proceso transitorio; la verificación posterior fue **0 procesos**.

## Integridad posterior

| Elemento | SHA-256 |
| --- | --- |
| PPTX final | `26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D` |
| SRC-203 | `36E4E9AE273DF191CCD05171F276697CB7A000698BBB3C523EA5C8A188F96516` |
| SRC-201 | `0CCC4A532C0B3091E6D9BD00857EFDD6761D4E1D3855B49B8FE7A66220D2DF30` |
| Excel de seguimiento | `E7F09B0AC9EF786096640F6D2B751E372A65BFA41B1595B545B535B562DB74F1` |
| PBIP | `F8712089DBB5BBF10C5DE3655522C84540184101F5D8A96BE6EA017AFA8A1CCE` |

Silver verificados contra `validation/results/S01/source_manifest.json`:

| Fuente | SHA-256 |
| --- | --- |
| DATA-001 | `A193F92A0C14EC95ED88DFC60125E530135F4E6E5C54A308AA53D5F076CF3BBE` |
| DATA-002 | `E27824EB494ACE66AED9B9BBEDB82195B033A2FC6400EFF31FF1075E0DFEF28F` |
| DATA-003 | `A30FF0BC0A0DED58B549AB03E8F196D187BCEE994C02FF749D1B492F13228307` |
| DATA-004 | `13EFBE4E2D7BB0EB60075E918600023FB1BAEAC9A930E5AF4D8CE2A2BF92A406` |
| DATA-005 | `D3D238E629D6C98E56D678AEF4B0D208A8E31C9CEFF1ECD91F5699AA5C192AC0` |

El PPTX final tiene 43.872 bytes y 4 diapositivas.

## Pendiente

- T06 no iniciado.
- Excel y PDF no modificados.
- No se declara T05 como cierre de S02; la auditoría independiente sigue pendiente.
