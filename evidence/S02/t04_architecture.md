# T04 — Diapositiva 2 de arquitectura

Fecha: 2026-10-27  
Alcance autorizado: completar solo la diapositiva 2 del PPTX entregable de S02. No se añadió el mapa Silver, no se inició T05, no se exportó PDF y no se modificaron Excel, Power BI, Silver ni referencias.

## Resultado

- **T04 completada**: 38/38 controles pasan en [`slide2_checks.json`](../../validation/results/S02/slide2_checks.json).
- PPTX final: `deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx`, **39.263 bytes**, SHA-256 `71DCE2F66C96EFB0FF7B3ADDB67ABDD9F1E41215D945388836C21C6F7A53664A`.
- Diapositivas: 2. Formas por diapositiva: 32 y 32.
- Render: [`s02_t04_architecture_slide.png`](screenshots/s02_t04_architecture_slide.png), 1920×1080, 87.401 bytes, SHA-256 `BA3EF09DBCDCFA2ABA2962AF6977B79ECFBCA1FD385E975CC39303A2A029B90F`.

## Inventario y cambios

Se inventariaron las 32 formas antes de editar. Se modificaron únicamente 10 formas de texto:

| Índice | Shape ID | Bloque | Cambio |
| ---: | ---: | --- | --- |
| 0 | 2 | Encabezado | Equipo 06 |
| 3 | 5 | Decisión | Solo el segundo párrafo; el título quedó intacto |
| 6 | 8 | Origen | Origen no documentado y sin atribución de sistemas |
| 10 | 12 | Tabla Silver | Cinco fuentes oficiales y grano |
| 14 | 16 | Power Query | Componentes existentes, sin cambios en S02 |
| 18 | 20 | Modelo semántico | Estado actual y propuesta para S06 |
| 22 | 24 | Indicador | KPI táctico y referencia a Fichas KPI |
| 25 | 27 | Brecha DCAM | C4, Evidencia, 1 Incipiente, no resuelta |
| 28 | 30 | Riesgo y control | Riesgo, hecho, control principal y complementario |
| 31 | 33 | Pendiente | Definición y validación empresarial, responsable y límite |

No se modificaron posiciones, tamaños, rotaciones, colores, flechas, contenedores ni etiquetas de sección. Las 10 formas editadas usan `auto_size = NONE`; la geometría de las 32 formas coincide con T03.

## Contenido final

- Encabezado: `PROYECTO INTEGRADOR · HITO S02 · EQUIPO 06`.
- Decisión: `La Jefatura de Operaciones decide cada semana dónde priorizar controles térmicos por producto y camión y qué lotes o centros revisar por vencimiento y merma.`
- Origen: `No documentado por archivo; por acordar. No se atribuye ERP, WMS, TMS ni telemetría a estas tablas.`
- Silver: `5 fuentes oficiales: DATA-001 a DATA-005. Una fila = una lectura, producto, camión, lote o centro-mes.`
- Power Query: `RutaSilver + File.Contents + Csv.Document; Encabezados y Tipado. Ya existente; sin cambios en S02.`
- Modelo: `5 tablas Import; 0 relaciones; 0 medidas. Modelo relacional: dimensiones y relaciones, propuestas para S06.`
- Indicador: `% de viajes con desviación. Nivel táctico; fórmula y unidad en Fichas KPI.`
- Brecha: `No encontramos definición explícita de centro_distribucion. C4 Conocimiento de los datos · Evidencia · 1 Incipiente. Ausencia documentada; no resuelta.`
- Riesgo y control: riesgo de interpretar mal qué representa el centro; hecho de 8.000/8.000 viajes emparejados sin discrepancias, con `centro WMS = centro base` y el límite de que no prueba significado empresarial; control principal de documentar ausencia, usos y límites conocidos y solicitar definición y validación empresarial; control complementario de no usar `centro_distribucion_base` como ruta u origen real y dejar `dim_centro` y controles de claves como propuestas posteriores.
- Pendiente: `Definición y validación empresarial de centro_distribucion; seguimiento Grupo 06; validador por acordar. No resuelto.`

WMS no aparece como sexta fuente: solo se menciona en la negación de origen y en el hecho de contraste. No aparecen DATA-006, DATA-007 ni el archivo WMS como fuente cargada. En el contenido de la diapositiva 2 no hay metas, ahorro, DAX, RLS ni validación ejecutada. La diapositiva 1 conserva el ejemplo de SRC-203, incluida su mención de «meta de 85 %», y queda fuera del contenido T04.

## Revisión visual

Método: exportación de la diapositiva 2 con PowerPoint COM 16.0 a PNG 1920×1080, sin guardar la presentación, seguida de inspección visual del render.

- Sin texto truncado, desbordado ni superpuesto.
- Contraste adecuado y flechas visibles.
- El bloque de riesgo/control es el más denso: usa 8 pt, conserva todos los significados y queda dentro de su contenedor; es legible a 1920×1080.
- Riesgo, control y pendiente son coherentes: el riesgo se plantea, no se atribuye una asignación incorrecta observada; la brecha sigue sin resolver.
- Durante Build se detectó y corrigió un guardado intermedio con acentos convertidos en `?` por codificación. El resultado final no contiene `?` en la diapositiva 2 y la comprobación 38/38 pasa.

## Integridad

- Diapositiva 1 XML: `0F944D0FB93C30E7CBAF0D7ED52D35900870A1E1E6BA20E31E0541D1770C7CC9`; idéntica a T03.
- Diapositiva 1 texto normalizado: `7023CF3D2379FFF73887AED7CAE75130646DB38F496D99C477D393E1B0F850FA`; idéntico a T03.
- Diapositiva 1 inventario de formas: `26CB5FA7859FD8082944BC3CACC57350C28EA14C7726F547EB7E231ABBE681BC`; idéntico a T03.
- SRC-203: 38.618 bytes, SHA-256 `36E4E9AE273DF191CCD05171F276697CB7A000698BBB3C523EA5C8A188F96516`; sin cambios.
- La huella binaria del PPTX cambió de `36E4E9AE…F96516` a `71DCE2F6…53664A` por la edición autorizada de T04.

## PowerPoint COM

- Versión 16.0; abrió sin reparación y en solo lectura (`ReadOnly = -1`).
- 2 diapositivas y 32 formas en la diapositiva 2.
- Exportó el PNG 1920×1080 y cerró sin guardar (`saved_by_com = false`, `save_calls = 0`).
- Sin procesos de PowerPoint antes; el proceso de COM cerró y la verificación independiente posterior registró 0 procesos.
- Resultado temporal: [`t04_com_result.json`](../../work/S02/t04_com_result.json).

## Límites

- No se añadió el mapa Silver, no se inició T05 y no se exportó PDF.
- No se ejecutó validación empresarial, Power BI Desktop, DAX, RLS ni publicación.
- La diapositiva 1 es el ejemplo preservado de SRC-203; no forma parte del contenido editado en T04.
